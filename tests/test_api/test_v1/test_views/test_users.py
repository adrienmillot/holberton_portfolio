#!/usr/bin/python3
import json
from models import db_storage
from models.profile import Profile
from models.user import User
from os import getenv
import requests
import unittest


host = getenv('SS_API_HOST_API_HOST', '0.0.0.0')
port = getenv('SS_API_PORT', '5001')
version = '/v1'
api_url = 'http://{}:{}/api{}'.format(host, port, version)


WRONG_STATUS_CODE_MSG = 'Wrong status code!'
WRONG_TYPE_RETURN_MSG = 'Wrong return type return!'
WRONG_OBJ_TYPE_MSG = 'Wrong object type!'
MISSING_USERNAME_ATTR_MSG = 'Missing username!'
PASSWORD_ATTR_FOUND_MSG = 'Password attribute found!'
MISSING_CREATED_AT_ATTR_MSG = 'Missing created_at!'
MISSING_UPDATED_AT_ATTR_MSG = 'Missing updated_at!'
MISSING_CLASS_ATTR_MSG = 'Missing class!'


@unittest.skipIf(getenv('SS_SERVER_MODE') != 'API', "only testing api server mode")
class ListUsersApiTest(unittest.TestCase):
    """
        Tests of API list action for User.
    """

    def setUp(self) -> None:
        """
            Set up API list action tests.
        """

        self.profile = Profile()
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test', profile_id=self.profile_id)
        db_storage.new(self.profile)
        db_storage.new(self.user)
        db_storage.save()
        self.url = '{}/users'.format(api_url)

    def tearDown(self) -> None:
        db_storage.delete(self.user)
        db_storage.delete(self.profile)
        db_storage.save()

    def testList(self):
        """
            Test valid list action.
        """

        response = requests.get(url=self.url)
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)

    def testCount(self):
        """
            Test list length.
        """

        initial_count = len(db_storage.all(User))
        response = requests.get(url=self.url)
        json_data = response.json()

        self.assertEqual(initial_count, len(json_data['results']))

    def testOnlyUser(self):
        """
            Test valid list action with User content only.
        """

        response = requests.get(url=self.url)
        json_data = response.json()

        for element in json_data['results']:
            self.assertEqual(element['__class__'], 'User', WRONG_OBJ_TYPE_MSG)


@unittest.skipIf(getenv('SS_SERVER_MODE') != 'API', "only testing api server mode")
class ShowUsersApiTest(unittest.TestCase):
    """
        Tests of API show action for User.
    """

    def setUp(self) -> None:
        """
            Set up API show action tests.
        """

        self.profile = Profile(last_name='toto', first_name='titi',gender='Male')
        self.user = User(username='test', password='test', profile_id=self.profile.id)

        self.profile.save()
        self.user.save()

        self.url = '{}/users/{}'.format(api_url, self.user.id)
        self.invalid_url = '{}/users/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table User of database used for tests.
        """

        db_storage.delete(self.user)
        db_storage.delete(self.profile)
        db_storage.save()

    def testShow(self):
        """
            Test valid show action.
        """

        response = requests.get(url=self.url)
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        self.assertIn('username', json_data)
        self.assertNotIn('password', json_data)
        self.assertIn('created_at', json_data)
        self.assertIn('updated_at', json_data)
        self.assertIn('__class__', json_data)
        self.assertEqual(json_data['username'], self.user.username)

    def testNotFound(self):
        """
            Test show action when given wrong user_id or no ID at all.
        """

        response = requests.get(url=self.invalid_url)
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertTrue(self.user == db_storage.get(User, self.user.id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'User entity not found.')


@unittest.skipIf(getenv('SS_SERVER_MODE') != 'API', "only testing api server mode")
class DeleteUsersApiTest(unittest.TestCase):
    """
        Tests of API delete action for User.
    """

    def setUp(self) -> None:
        """
            Set up API delete action tests.
        """

        self.profile = Profile(last_name='toto')
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test', profile_id=self.profile_id)
        self.user_id = self.user.id

        self.profile.save()
        self.user.save()

        self.url = '{}/users/{}'.format(api_url, self.user.id)
        self.invalid_url = '{}/users/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table User of database used for tests.
        """

        user = db_storage.get_from_attributes(User, id=self.user.id)
        if user is not None:
            db_storage.delete(user)
            db_storage.save()

        profile = db_storage.get_from_attributes(Profile, id=self.profile.id)
        if profile is not None:
            db_storage.delete(profile)
            db_storage.save()

    def testDelete(self):
        """
            Test valid delete action.
        """

        self.assertTrue(self.user == db_storage.get(User, self.user_id))

        response = requests.delete(url=self.url)
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        self.assertEqual(len(json_data), 0)
        db_storage.reload()
        self.assertIsNone(db_storage.get(User, self.user_id))

    def testNotFound(self):
        """
            Test delete action when given wrong profile_id or no ID at all.
        """

        response = requests.delete(url=self.invalid_url)
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertTrue(self.user == db_storage.get(User, self.user.id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'User entity not found.')


@unittest.skipIf(getenv('SS_SERVER_MODE') != 'API', "only testing api server mode")
class CreateUsersApiTest(unittest.TestCase):
    """
        Tests of API create action for User.
    """

    def setUp(self) -> None:
        """
            Set up API create action.
        """

        self.profile = Profile(name='toto')
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test', profile_id=self.profile_id)
        self.user_id = self.user.id

        self.profile.save()
        self.user.save()

        self.url = '{}/users/'.format(api_url)

    def tearDown(self) -> None:
        """
            Tear down table User of database used for tests.
        """

        profile = db_storage.get_from_attributes(Profile, id=self.profile.id)
        if profile is not None:
            db_storage.delete(profile)
            db_storage.save()

    def testCreate(self):
        """
            Test valid create action tests.
        """

        data = {'username': 'toto', 'password': 'titi', 'profile_id': self.profile_id}
        response = requests.post(url=self.url, json=data)
        headers = response.headers

        self.assertEqual(response.status_code, 201, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        user = db_storage.get(User, json_data['id'])
        self.assertIsInstance(user, User)
        self.assertIn('username', json_data, MISSING_USERNAME_ATTR_MSG)
        self.assertNotIn('password', json_data, PASSWORD_ATTR_FOUND_MSG)
        self.assertIn('created_at', json_data, MISSING_CREATED_AT_ATTR_MSG)
        self.assertIn('updated_at', json_data, MISSING_UPDATED_AT_ATTR_MSG)
        self.assertIn('__class__', json_data, MISSING_CLASS_ATTR_MSG)
        self.assertEqual(json_data['username'], 'toto')
        db_storage.delete(user)
        db_storage.save()

    def testNotAJson(self):
        """
            Test create action when given wrong data format.
        """

        data = {'username': 'toto', 'password': 'titi', 'profile_id': self.profile_id}
        response = requests.post(url=self.url, data=data)
        headers = response.headers

        self.assertEqual(response.status_code, 400, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json',
            WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Not a JSON.')


@unittest.skipIf(getenv('SS_SERVER_MODE') != 'API', "only testing api server mode")
class UpdateUsersApiTest(unittest.TestCase):
    """
        Tests of API update action for User.
    """

    def setUp(self) -> None:
        """
            Set up API update action tests.
        """

        self.profile = Profile(last_name='toto')
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test', profile_id=self.profile_id)
        self.user_id = self.user.id

        self.profile.save()
        self.user.save()
        self.user.save()

        self.url = '{}/users/{}'.format(api_url, self.user_id)
        self.invalid_url = '{}/users/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table User of database used for tests.
        """

        user = db_storage.get_from_attributes(User, id=self.user_id)
        if user is not None:
            db_storage.delete(user)
            db_storage.save()

        profile = db_storage.get_from_attributes(Profile, id=self.profile_id)
        if profile is not None:
            db_storage.delete(profile)
            db_storage.save()

    def testUpdate(self):
        """
            Test valid update action.
        """

        self.assertTrue(self.user == db_storage.get(User, self.user_id))
        self.assertEqual(self.user.username, 'test')
        data = {'username': 'toto2'}
        response = requests.put(url=self.url, json=data)
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        db_storage.reload()
        user = db_storage.get(User, self.user_id)
        self.assertEqual(user.username, 'toto2')
        self.assertIn('username', json_data, MISSING_USERNAME_ATTR_MSG)
        self.assertNotIn('password', json_data, PASSWORD_ATTR_FOUND_MSG)
        self.assertIn('created_at', json_data, MISSING_CREATED_AT_ATTR_MSG)
        self.assertIn('updated_at', json_data, MISSING_UPDATED_AT_ATTR_MSG)
        self.assertIn('__class__', json_data, MISSING_CLASS_ATTR_MSG)
        self.assertEqual(json_data['username'], 'toto2')
        db_storage.delete(user)
        db_storage.save()

    def testNotAJson(self):
        """
            Test update action when given an invalid json.
        """

        data = {'name': 'toto'}
        response = requests.put(url=self.url, data=data)
        headers = response.headers

        self.assertEqual(response.status_code, 400, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json',
            WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Not a JSON.')

    def testNotFound(self):
        """
            Test update action when given a wrong ID.
        """

        data = {'name': 'toto'}
        response = requests.put(url=self.invalid_url, data=json.dumps(data))
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertTrue(self.user == db_storage.get(User, self.user.id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'User entity not found.')
