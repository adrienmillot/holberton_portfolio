#!/usr/bin/python3
"""
    API Tests Module for Categories entrypoint.
"""
import json
from models import db_storage
from models.profile import Profile
from models.user import User
from models.survey import Survey
from models.category import Category
from models.question import Question
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


class ListQuestionsApiTest(AuthenticatedRequest):
    """
        Tests of API list action for Questions.
    """

    def setUp(self) -> None:
        """
            Set up API list questions action tests.
        """

        self.profile = Profile()
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test',
                         profile_id=self.profile_id)
        self.category = Category(name='toto')
        self.category_id = self.category.id
        self.survey = Survey(name='toto')
        self.survey_id = self.survey.id
        self.question = Question(
            label='toto', category_id=self.category_id, survey_id=self.survey_id)
        db_storage.new(self.profile)
        db_storage.new(self.user)
        db_storage.new(self.category)
        db_storage.new(self.survey)
        db_storage.new(self.question)
        db_storage.save()
        self.url = '{}/questions'.format(api_url)

    def tearDown(self) -> None:
        """
            Tear down table Question of database used for tests.
        """

        db_storage.delete(self.question)
        db_storage.delete(self.survey)
        db_storage.delete(self.category)
        db_storage.delete(self.user)
        db_storage.delete(self.profile)
        db_storage.save()

    def testList(self):
        """
            Test valid list questions action.
        """

        response = self.get_authenticated_response()
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)

    def testCount(self):
        """
            Test list questions length.
        """

        initial_count = len(db_storage.all(Question))
        response = self.get_authenticated_response()
        json_data = response.json()

        self.assertEqual(initial_count, len(json_data['results']))

    def testOnlyQuestion(self):
        """
            Test valid list questions action with Question content only.
        """

        response = self.get_authenticated_response()
        json_data = response.json()

        for element in json_data['results']:
            self.assertEqual(element['__class__'],
                             'Question', WRONG_OBJ_TYPE_MSG)
