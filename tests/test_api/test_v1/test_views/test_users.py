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
MISSING_LAST_NAME_ATTR_MSG = 'Missing last_name!'
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