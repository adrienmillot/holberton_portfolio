#!/usr/bin/python3
"""
    API Tests Module for Categories entrypoint.
"""
import json
from models import db_storage
from models.profile import Profile
from models.user import User
from models.category import Category
from os import getenv
import requests
from tests.test_api.test_v1.test_views.authenticated import AuthenticatedRequest

host = getenv('SS_API_HOST_API_HOST', '0.0.0.0')
port = getenv('SS_API_PORT', '5001')
version = '/v1'
api_url = 'http://{}:{}/api{}'.format(host, port, version)


WRONG_STATUS_CODE_MSG = 'Wrong status code!'
WRONG_TYPE_RETURN_MSG = 'Wrong return type return!'
WRONG_OBJ_TYPE_MSG = 'Wrong object type!'
MISSING_NAME_ATTR_MSG = 'Missing name!'
MISSING_CREATED_AT_ATTR_MSG = 'Missing created_at!'
MISSING_UPDATED_AT_ATTR_MSG = 'Missing updated_at!'
MISSING_CLASS_ATTR_MSG = 'Missing class!'


class ListCategoriesApiTest(AuthenticatedRequest):
    """
        Tests of API list action for Categories.
    """

    def setUp(self) -> None:
        """
            Set up API list categories action tests.
        """

        self.profile = Profile()
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test',
                         profile_id=self.profile_id)
        self.category = Category(name='toto')
        db_storage.new(self.profile)
        db_storage.new(self.user)
        db_storage.new(self.category)
        db_storage.save()
        self.url = '{}/categories'.format(api_url)

    def tearDown(self) -> None:
        """
            Tear down table Category of database used for tests.
        """

        db_storage.delete(self.category)
        db_storage.delete(self.user)
        db_storage.delete(self.profile)
        db_storage.save()

    def testList(self):
        """
            Test valid list categories action.
        """

        response = self.get_authenticated_response()
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)

    def testCount(self):
        """
            Test list categories length.
        """

        initial_count = len(db_storage.all(Category))
        response = self.get_authenticated_response()
        json_data = response.json()

        self.assertEqual(initial_count, len(json_data['results']))

    def testOnlyCategory(self):
        """
            Test valid list categories action with Category content only.
        """

        response = self.get_authenticated_response()
        json_data = response.json()

        for element in json_data['results']:
            self.assertEqual(element['__class__'],
                             'Category', WRONG_OBJ_TYPE_MSG)

