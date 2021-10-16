#!/usr/bin/python3
"""
    API Tests Module for Surveys entrypoint.
"""
import json
from models import db_storage
from models.profile import Profile
from models.user import User
from models.survey import Survey
from os import getenv
import requests
from tests.test_api.test_v1.test_views.authenticated import AuthenticatedRequest
import unittest

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


class ListSurveysApiTest(AuthenticatedRequest):
    """
        Tests of API list action for Surveys.
    """

    def setUp(self) -> None:
        """
            Set up API list surveys action tests.
        """
        self.profile = Profile()
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test',
                         profile_id=self.profile_id)
        self.survey = Survey(name='toto')
        db_storage.new(self.profile)
        db_storage.new(self.user)
        db_storage.new(self.survey)
        db_storage.save()
        self.url = '{}/surveys'.format(api_url)

    def tearDown(self) -> None:
        """
            Tear down table Survey of database used for tests.
        """
        db_storage.delete(self.survey)
        db_storage.delete(self.user)
        db_storage.delete(self.profile)
        db_storage.save()

    def testList(self):
        """
            Test valid list surveys action.
        """
        response = self.get_authenticated_response()
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)

    def testCount(self):
        """
            Test list surveys length.
        """
        initial_count = len(db_storage.all(Survey))
        response = self.get_authenticated_response()
        json_data = response.json()

        self.assertEqual(initial_count, len(json_data['results']))

    def testOnlySurvey(self):
        """
            Test valid list surveys action with Survey content only.
        """
        response = self.get_authenticated_response()
        json_data = response.json()

        for element in json_data['results']:
            self.assertEqual(element['__class__'],
                             'Survey', WRONG_OBJ_TYPE_MSG)


class ShowSurveysApiTest(AuthenticatedRequest):
    """
        Tests of API show action for Surveys.
    """

    def setUp(self) -> None:
        """
            Set up API show survey action tests.
        """
        self.profile = Profile()
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test',
                         profile_id=self.profile_id)
        self.survey = Survey(name='toto')
        self.survey_id = self.survey.id
        db_storage.new(self.profile)
        db_storage.new(self.user)
        db_storage.new(self.survey)
        db_storage.save()
        self.url = '{}/surveys/{}'.format(api_url, self.survey_id)
        self.invalid_url = '{}/surveys/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table Survey of database used for tests.
        """
        db_storage.delete(self.survey)
        db_storage.delete(self.user)
        db_storage.delete(self.profile)
        db_storage.save()

    def testShow(self):
        """
            Test valid show survey action
        """
        response = self.get_authenticated_response()
        headers = response.headers
        json_data = response.json()

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertIn('name', json_data)
        self.assertIn('created_at', json_data)
        self.assertIn('updated_at', json_data)
        self.assertIn('__class__', json_data)
        self.assertEqual(json_data['name'], self.survey.name)

    def testNotFound(self):
        """
            Test show survey action when given wrong survey_id or no ID at all.
        """
        response = self.get_authenticated_response(url=self.invalid_url)
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertTrue(self.survey == db_storage.get(Survey, self.survey_id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Survey entity not found.')


class DeleteSurveysApiTest(AuthenticatedRequest):
    """
        Tests of API delete action for Surveys.
    """

    def setUp(self) -> None:
        """
            Set up API delete survey action tests.
        """
        self.profile = Profile(last_name='toto')
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test',
                         profile_id=self.profile_id)
        self.user_id = self.user.id
        self.survey = Survey(name='toto')
        self.survey_id = self.survey.id
        db_storage.new(self.profile)
        db_storage.new(self.user)
        db_storage.new(self.survey)
        db_storage.save()
        self.url = '{}/surveys/{}'.format(api_url, self.survey_id)
        self.invalid_url = '{}/surveys/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table Survey of database used for tests.
        """
        survey = db_storage.get_from_attributes(Survey, id=self.survey_id)
        if survey is not None:
            db_storage.delete(survey)
            db_storage.save()

        user = db_storage.get_from_attributes(User, id=self.user_id)
        if user is not None:
            db_storage.delete(user)
            db_storage.save()

        profile = db_storage.get_from_attributes(Profile, id=self.profile_id)
        if profile is not None:
            db_storage.delete(profile)
            db_storage.save()

    def testDelete(self):
        """
            Test valid delete survey action
        """
        response = self.get_authenticated_response(http_method='delete')
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        self.assertEqual(len(json_data), 0)
        db_storage.reload()
        self.assertIsNone(db_storage.get(Survey, self.survey_id))

    def testNotFound(self):
        """
            Test disable survey action when given wrong survey_id or no ID at all.
        """
        response = self.get_authenticated_response(
            http_method='delete', url=self.invalid_url)
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertTrue(self.survey == db_storage.get(Survey, self.survey_id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Survey entity not found.')


class CreateSurveysApiTest(AuthenticatedRequest):
    """
        Tests of API create action for Surveys.
    """

    def setUp(self) -> None:
        """
            Set up API create survey action tests.
        """
        self.profile = Profile()
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test',
                         profile_id=self.profile_id)
        self.user_id = self.user.id
        db_storage.new(self.profile)
        db_storage.new(self.user)
        db_storage.save()
        self.url = '{}/surveys'.format(api_url)

    def tearDown(self) -> None:
        """
            Tear down table Survey of database used for tests.
        """
        user = db_storage.get_from_attributes(User, id=self.user_id)
        if user is not None:
            db_storage.delete(user)
            db_storage.save()

        profile = db_storage.get_from_attributes(Profile, id=self.profile_id)
        if profile is not None:
            db_storage.delete(profile)
            db_storage.save()

    def testCreate(self):
        """
            Test valid create survey action tests.
        """
        data = {'name': 'toto'}
        response = self.get_authenticated_response(
            http_method='post', json=data)
        headers = response.headers

        self.assertEqual(response.status_code, 201, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        survey = db_storage.get(Survey, json_data['id'])
        self.assertIsInstance(survey, Survey)
        self.assertIn('name', json_data, MISSING_NAME_ATTR_MSG)
        self.assertIn('created_at', json_data, MISSING_CREATED_AT_ATTR_MSG)
        self.assertIn('updated_at', json_data, MISSING_UPDATED_AT_ATTR_MSG)
        self.assertIn('__class__', json_data, MISSING_CLASS_ATTR_MSG)
        self.assertEqual(json_data['name'], 'toto')
        db_storage.delete(survey)
        db_storage.save()

    def testMissingNameAttribute(self):
        """
            Test create survey action when given dict without name key.
        """
        data = {'bidule': 'toto'}
        response = self.get_authenticated_response(
            http_method='post', json=data)
        headers = response.headers

        self.assertEqual(response.status_code, 400, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json',
            WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Missing name.')

    def testNotAJson(self):
        """
            Test create survey action when given wrong data format.
        """
        data = {'name': 'toto'}
        response = self.get_authenticated_response(
            http_method='post', data=data)
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
