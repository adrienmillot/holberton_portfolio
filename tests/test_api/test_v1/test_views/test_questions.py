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
MISSING_LABEL_ATTR_MSG = 'Missing label!'
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

        self.profile.save()
        self.user.save()
        self.category.save()
        self.survey.save()
        self.question.save()

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


class ShowQuestionsApiTest(AuthenticatedRequest):
    """
        Tests of API show action for Questions.
    """

    def setUp(self) -> None:
        """
            Set up API show question action tests.
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
        self.question_id = self.question.id

        self.profile.save()
        self.user.save()
        self.category.save()
        self.survey.save()
        self.question.save()

        self.url = '{}/questions/{}'.format(api_url, self.question_id)
        self.invalid_url = '{}/questions/{}'.format(api_url, 'toto')

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

    def testShow(self):
        """
            Test valid show question action
        """

        response = self.get_authenticated_response()
        headers = response.headers
        json_data = response.json()

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertIn('label', json_data)
        self.assertIn('created_at', json_data)
        self.assertIn('updated_at', json_data)
        self.assertIn('__class__', json_data)
        self.assertEqual(json_data['label'], self.question.label)

    def testNotFound(self):
        """
            Test show question action when given wrong question_id or no ID at all.
        """

        response = self.get_authenticated_response(url=self.invalid_url)
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertTrue(self.question == db_storage.get(
            Question, self.question_id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Question entity not found.')


class DeleteQuestionsApiTest(AuthenticatedRequest):
    """
        Tests of API delete action for Questions.
    """

    def setUp(self) -> None:
        """
            Set up API delete question action tests.
        """

        self.profile = Profile(last_name='toto')
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test',
                         profile_id=self.profile_id)
        self.user_id = self.user.id
        self.category = Category(name='toto')
        self.category_id = self.category.id
        self.survey = Survey(name='toto')
        self.survey_id = self.survey.id
        self.question = Question(
            label='toto', category_id=self.category_id, survey_id=self.survey_id)
        self.question_id = self.question.id

        self.profile.save()
        self.user.save()
        self.category.save()
        self.survey.save()
        self.question.save()

        self.url = '{}/questions/{}'.format(api_url, self.question_id)
        self.invalid_url = '{}/questions/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table Question of database used for tests.
        """

        question = db_storage.get_from_attributes(
            Question, id=self.question_id)
        if question is not None:
            db_storage.delete(question)
            db_storage.save()

        survey = db_storage.get_from_attributes(Survey, id=self.survey_id)
        if survey is not None:
            db_storage.delete(survey)
            db_storage.save()

        category = db_storage.get_from_attributes(
            Category, id=self.category_id)
        if category is not None:
            db_storage.delete(category)
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
            Test valid delete question action
        """

        response = self.get_authenticated_response(http_method='delete')
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        self.assertEqual(len(json_data), 0)
        db_storage.reload()
        self.assertIsNone(db_storage.get(Question, self.question_id))

    def testNotFound(self):
        """
            Test disable question action when given wrong question_id or no ID at all.
        """

        response = self.get_authenticated_response(
            http_method='delete', url=self.invalid_url)
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertTrue(self.question == db_storage.get(
            Question, self.question_id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Question entity not found.')


class CreateQuestionsApiTest(AuthenticatedRequest):
    """
        Tests of API create action for Questions.
    """

    def setUp(self) -> None:
        """
            Set up API create question action tests.
        """

        self.profile = Profile(last_name='toto')
        self.profile_id = self.profile.id
        self.user = User(username='test', password='test',
                         profile_id=self.profile_id)
        self.user_id = self.user.id
        self.category = Category(name='toto')
        self.category_id = self.category.id
        self.survey = Survey(name='toto')
        self.survey_id = self.survey.id
        self.question = Question(
            label='toto', category_id=self.category_id, survey_id=self.survey_id)
        self.question_id = self.question.id

        self.profile.save()
        self.user.save()
        self.category.save()
        self.survey.save()
        self.question.save()

        self.url = '{}/questions'.format(api_url)

    def tearDown(self) -> None:
        """
            Tear down table Question of database used for tests.
        """

        question = db_storage.get_from_attributes(
            Question, id=self.question_id)
        if question is not None:
            db_storage.delete(question)
            db_storage.save()

        survey = db_storage.get_from_attributes(Survey, id=self.survey_id)
        if survey is not None:
            db_storage.delete(survey)
            db_storage.save()

        category = db_storage.get_from_attributes(
            Category, id=self.category_id)
        if category is not None:
            db_storage.delete(category)
            db_storage.save()

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
            Test valid create question action tests.
        """

        data = {'label': 'toto', 'category_id': self.category_id, 'survey_id': self.survey_id}
        response = self.get_authenticated_response(
            http_method='post', json=data)
        headers = response.headers

        self.assertEqual(response.status_code, 201, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        question = db_storage.get(Question, json_data['id'])
        self.assertIsInstance(question, Question)
        self.assertIn('label', json_data, MISSING_LABEL_ATTR_MSG)
        self.assertIn('created_at', json_data, MISSING_CREATED_AT_ATTR_MSG)
        self.assertIn('updated_at', json_data, MISSING_UPDATED_AT_ATTR_MSG)
        self.assertIn('__class__', json_data, MISSING_CLASS_ATTR_MSG)
        self.assertEqual(json_data['label'], 'toto')
        db_storage.delete(question)
        db_storage.save()

    def testMissingLabelAttribute(self):
        """
            Test create question action when given dict without label key.
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
        self.assertEqual(json_data['message'], 'Missing label.')

    def testNotAJson(self):
        """
            Test create question action when given wrong data format.
        """

        data = {'label': 'toto'}
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
