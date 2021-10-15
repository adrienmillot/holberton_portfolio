#!/usr/bin/python3
import json
from models import db_storage
from models.profile import Profile
from models.user import User
from os import getenv
import requests
import unittest

from tests.test_api.test_v1.test_views.authenticated import AuthenticatedRequest


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
class ListProfilesApiTest(AuthenticatedRequest):
    """
        Tests of API list action for Profile.
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
        self.url = '{}/profiles'.format(api_url)

    def tearDown(self) -> None:
        db_storage.delete(self.user)
        db_storage.delete(self.profile)
        db_storage.save()

    def testList(self):
        """
            Test valid list action.
        """

        response = self.get_authenticated_response()
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)

    def testCount(self):
        """
            Test list length.
        """

        initial_count = len(db_storage.all(Profile))
        response = self.get_authenticated_response()
        json_data = response.json()

        self.assertEqual(initial_count, len(json_data['results']))

    def testOnlyProfile(self):
        """
            Test valid list action with Profile content only.
        """

        response = self.get_authenticated_response()
        json_data = response.json()

        for element in json_data['results']:
            self.assertEqual(element['__class__'], 'Profile', WRONG_OBJ_TYPE_MSG)


@unittest.skipIf(getenv('SS_SERVER_MODE') != 'API', "only testing api server mode")
class ShowProfilesApiTest(unittest.TestCase):
    """
        Tests of API show action for Profile.
    """

    def setUp(self) -> None:
        """
            Set up API show action tests.
        """

        self.profile = Profile(last_name='toto', first_name='titi',gender='Male')
        db_storage.new(self.profile)
        db_storage.save()
        self.url = '{}/profiles/{}'.format(api_url, self.profile.id)
        self.invalid_url = '{}/profiles/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table Profile of database used for tests.
        """
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
        self.assertIn('last_name', json_data)
        self.assertIn('first_name', json_data)
        self.assertIn('gender', json_data)
        self.assertIn('created_at', json_data)
        self.assertIn('updated_at', json_data)
        self.assertIn('__class__', json_data)
        self.assertEqual(json_data['last_name'], self.profile.last_name)
        self.assertEqual(json_data['first_name'], self.profile.first_name)
        self.assertEqual(json_data['gender'], self.profile.gender)

    def testNotFound(self):
        """
            Test show action when given wrong profile_id or no ID at all.
        """

        response = requests.get(url=self.invalid_url)
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertTrue(self.profile == db_storage.get(Profile, self.profile.id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Profile entity not found.')


@unittest.skipIf(getenv('SS_SERVER_MODE') != 'API', "only testing api server mode")
class DeleteProfilesApiTest(unittest.TestCase):
    """
        Tests of API delete action for Profile.
    """

    def setUp(self) -> None:
        """
            Set up API delete action tests.
        """

        self.profile = Profile(name='toto')
        self.profile_id = self.profile.id
        db_storage.new(self.profile)
        db_storage.save()
        self.url = '{}/profiles/{}'.format(api_url, self.profile.id)
        self.invalid_url = '{}/profiles/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table Profile of database used for tests.
        """

        profile = db_storage.get_from_attributes(Profile, id=self.profile.id)
        if profile is not None:
            db_storage.delete(profile)
            db_storage.save()

    def testDelete(self):
        """
            Test valid delete action.
        """

        self.assertTrue(self.profile == db_storage.get(Profile, self.profile_id))

        response = requests.delete(url=self.url)
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        self.assertEqual(len(json_data), 0)
        db_storage.reload()
        self.assertIsNone(db_storage.get(Profile, self.profile_id))

    def testNotFound(self):
        """
            Test delete action when given wrong profile_id or no ID at all.
        """

        response = requests.delete(url=self.invalid_url)
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertTrue(self.profile == db_storage.get(Profile, self.profile.id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Profile entity not found.')


@unittest.skipIf(getenv('SS_SERVER_MODE') != 'API', "only testing api server mode")
class CreateProfilesApiTest(unittest.TestCase):
    """
        Tests of API create action for Profile.
    """

    def setUp(self) -> None:
        """
            Set up API create action.
        """

        self.url = '{}/profiles/'.format(api_url)

    def testCreate(self):
        """
            Test valid create action tests.
        """

        data = {'last_name': 'toto'}
        response = requests.post(url=self.url, json=data)
        headers = response.headers

        self.assertEqual(response.status_code, 201, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        profile = db_storage.get(Profile, json_data['id'])
        self.assertIsInstance(profile, Profile)
        self.assertIn('last_name', json_data, MISSING_LAST_NAME_ATTR_MSG)
        self.assertIn('created_at', json_data, MISSING_CREATED_AT_ATTR_MSG)
        self.assertIn('updated_at', json_data, MISSING_UPDATED_AT_ATTR_MSG)
        self.assertIn('__class__', json_data, MISSING_CLASS_ATTR_MSG)
        self.assertEqual(json_data['last_name'], 'toto')
        db_storage.delete(profile)
        db_storage.save()

    def testNotAJson(self):
        """
            Test create action when given wrong data format.
        """

        data = {'name': 'toto'}
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
class UpdateProfilesApiTest(unittest.TestCase):
    """
        Tests of API update action for Profile.
    """

    def setUp(self) -> None:
        """
            Set up API update action tests.
        """

        self.profile = Profile(last_name='toto')
        self.profile_id = self.profile.id
        db_storage.new(self.profile)
        db_storage.save()
        self.url = '{}/profiles/{}'.format(api_url, self.profile_id)
        self.invalid_url = '{}/profiles/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table Profile of database used for tests.
        """

        profile = db_storage.get_from_attributes(Profile, id=self.profile.id)
        if profile is not None:
            db_storage.delete(self.profile)
            db_storage.save()

    def testUpdate(self):
        """
            Test valid update action.
        """

        self.assertTrue(self.profile == db_storage.get(Profile, self.profile_id))
        self.assertEqual(self.profile.last_name, 'toto')
        data = {'last_name': 'toto2'}
        response = requests.put(url=self.url, json=data)
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        db_storage.reload()
        profile = db_storage.get(Profile, self.profile_id)
        self.assertEqual(profile.last_name, 'toto2')
        self.assertIn('last_name', json_data, MISSING_LAST_NAME_ATTR_MSG)
        self.assertIn('created_at', json_data, MISSING_CREATED_AT_ATTR_MSG)
        self.assertIn('updated_at', json_data, MISSING_UPDATED_AT_ATTR_MSG)
        self.assertIn('__class__', json_data, MISSING_CLASS_ATTR_MSG)
        self.assertEqual(json_data['last_name'], 'toto2')
        db_storage.delete(profile)
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
        self.assertTrue(self.profile == db_storage.get(Profile, self.profile.id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Profile entity not found.')
