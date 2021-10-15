#!/usr/bin/python3
import json
from models import db_storage
from models import profile
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


@unittest.skipIf(getenv('SS_SERVER_MODE') != 'API', "only testing api server mode")
class ListProfilesApiTest(unittest.TestCase):
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

        response = requests.get(url=self.url)
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)

    def testCount(self):
        """
            Test list length.
        """

        initial_count = len(db_storage.all(Profile))
        response = requests.get(url=self.url)
        json_data = response.json()

        self.assertEqual(initial_count, len(json_data['results']))

    def testOnlyProfile(self):
        """
            Test valid list action with Profile content only.
        """

        response = requests.get(url=self.url)
        json_data = response.json()

        for element in json_data['results']:
            self.assertEqual(element['__class__'], 'Profile', WRONG_OBJ_TYPE_MSG)
