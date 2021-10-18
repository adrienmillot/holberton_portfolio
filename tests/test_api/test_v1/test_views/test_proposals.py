#!/usr/bin/python3
"""
    API Tests Module for Proposals entrypoint.
"""
import json
from models import db_storage
from models.profile import Profile
from models.user import User
from models.survey import Survey
from models.category import Category
from models.question import Question
from models.proposal import Proposal
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


class ListProposalsApiTest(AuthenticatedRequest):
    """
        Tests of API list action for Proposals.
    """

    def setUp(self) -> None:
        """
            Set up API list proposals action tests.
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
        self.proposal = Proposal(label='toto', question_id=self.question_id)
        self.proposal_id = self.proposal.id

        self.profile.save()
        self.user.save()
        self.category.save()
        self.survey.save()
        self.question.save()
        self.proposal.save()

        self.url = '{}/proposals'.format(api_url)

    def tearDown(self) -> None:
        """
            Tear down table Proposal of database used for tests.
        """

        db_storage.delete(self.proposal)
        db_storage.delete(self.question)
        db_storage.delete(self.survey)
        db_storage.delete(self.category)
        db_storage.delete(self.user)
        db_storage.delete(self.profile)
        db_storage.save()

    def testList(self):
        """
            Test valid list proposals action.
        """

        response = self.get_authenticated_response()
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)

    def testCount(self):
        """
            Test list proposals length.
        """

        initial_count = len(db_storage.all(Proposal))
        response = self.get_authenticated_response()
        json_data = response.json()

        self.assertEqual(initial_count, len(json_data['results']))

    def testOnlyProposal(self):
        """
            Test valid list proposals action with Proposal content only.
        """

        response = self.get_authenticated_response()
        json_data = response.json()

        for element in json_data['results']:
            self.assertEqual(element['__class__'],
                             'Proposal', WRONG_OBJ_TYPE_MSG)


class ShowProposalsApiTest(AuthenticatedRequest):
    """
        Tests of API show action for Proposals.
    """

    def setUp(self) -> None:
        """
            Set up API list proposals action tests.
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
        self.proposal = Proposal(label='toto', question_id=self.question_id)
        self.proposal_id = self.proposal.id

        self.profile.save()
        self.user.save()
        self.category.save()
        self.survey.save()
        self.question.save()
        self.proposal.save()

        self.url = '{}/proposals/{}'.format(api_url, self.proposal_id)
        self.invalid_url = '{}/proposals/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table Proposal of database used for tests.
        """

        db_storage.delete(self.proposal)
        db_storage.delete(self.question)
        db_storage.delete(self.survey)
        db_storage.delete(self.category)
        db_storage.delete(self.user)
        db_storage.delete(self.profile)
        db_storage.save()

    def testShow(self):
        """
            Test valid show proposal action
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
        self.assertEqual(json_data['label'], self.proposal.label)

    def testNotFound(self):
        """
            Test show proposal action when given wrong porposal_id or no ID at all.
        """

        response = self.get_authenticated_response(url=self.invalid_url)
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertTrue(self.proposal == db_storage.get(
            Proposal, self.proposal_id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Proposal entity not found.')


class DeleteProposalsApiTest(AuthenticatedRequest):
    """
        Tests of API delete action for Proposals.
    """

    def setUp(self) -> None:
        """
            Set up API list proposals action tests.
        """

        self.profile = Profile()
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
        self.proposal = Proposal(label='toto', question_id=self.question_id)
        self.proposal_id = self.proposal.id

        self.profile.save()
        self.user.save()
        self.category.save()
        self.survey.save()
        self.question.save()
        self.proposal.save()

        self.url = '{}/proposals/{}'.format(api_url, self.proposal_id)
        self.invalid_url = '{}/proposals/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table Proposal of database used for tests.
        """

        proposal = db_storage.get_from_attributes(
            Proposal, id=self.proposal_id)
        if proposal is not None:
            db_storage.delete(proposal)
            db_storage.save()

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
            Test valid delete proposal action
        """

        response = self.get_authenticated_response(http_method='delete')
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        self.assertEqual(len(json_data), 0)
        db_storage.reload()
        self.assertIsNone(db_storage.get(Proposal, self.proposal_id))

    def testNotFound(self):
        """
            Test disable proposal action when given wrong proposal_id or no ID at all.
        """

        self.assertTrue(self.proposal == db_storage.get(
            Proposal, self.proposal_id))
        response = self.get_authenticated_response(
            http_method='delete', url=self.invalid_url)
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Proposal entity not found.')


class CreateProposalsApiTest(AuthenticatedRequest):
    """
        Tests of API create action for Proposals.
    """

    def setUp(self) -> None:
        """
            Set up API create proposal action tests.
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
        self.proposal = Proposal(label='toto', question_id=self.question_id)
        self.proposal_id = self.proposal.id

        self.profile.save()
        self.user.save()
        self.category.save()
        self.survey.save()
        self.question.save()
        self.proposal.save()

        self.url = '{}/proposals'.format(api_url)

    def tearDown(self) -> None:
        """
            Tear down table Question of database used for tests.
        """

        proposal = db_storage.get_from_attributes(
            Proposal, id=self.proposal_id)
        if proposal is not None:
            db_storage.delete(proposal)
            db_storage.save()

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
            Test valid create proposal action tests.
        """

        data = {'label': 'toto', 'question_id': self.question_id}
        response = self.get_authenticated_response(
            http_method='post', json=data)
        headers = response.headers

        self.assertEqual(response.status_code, 201, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        proposal = db_storage.get(Proposal, json_data['id'])
        self.assertIsInstance(proposal, Proposal)
        self.assertIn('label', json_data, MISSING_LABEL_ATTR_MSG)
        self.assertIn('created_at', json_data, MISSING_CREATED_AT_ATTR_MSG)
        self.assertIn('updated_at', json_data, MISSING_UPDATED_AT_ATTR_MSG)
        self.assertIn('__class__', json_data, MISSING_CLASS_ATTR_MSG)
        self.assertEqual(json_data['label'], 'toto')
        db_storage.delete(proposal)
        db_storage.save()

    def testMissingLabelAttribute(self):
        """
            Test create proposal action when given dict without label key.
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
            Test create proposal action when given wrong data format.
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


class UpdateProposalsApiTest(AuthenticatedRequest):
    """
        Tests of API update action for Proposals.
    """

    def setUp(self) -> None:
        """
            Set up API list proposals action tests.
        """

        self.profile = Profile()
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
        self.proposal = Proposal(label='toto', question_id=self.question_id)
        self.proposal_id = self.proposal.id

        self.profile.save()
        self.user.save()
        self.category.save()
        self.survey.save()
        self.question.save()
        self.proposal.save()

        self.url = '{}/proposals/{}'.format(api_url, self.proposal_id)
        self.invalid_url = '{}/proposals/{}'.format(api_url, 'toto')

    def tearDown(self) -> None:
        """
            Tear down table Proposal of database used for tests.
        """

        proposal = db_storage.get_from_attributes(
            Proposal, id=self.proposal_id)
        if proposal is not None:
            db_storage.delete(proposal)
            db_storage.save()

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

    def testUpdate(self):
        """
            Test valid update proposal action.
        """

        data = {'label': 'toto2'}
        self.assertTrue(self.proposal == db_storage.get(
            Proposal, self.proposal_id))
        response = self.get_authenticated_response(
            http_method='put', json=data)
        headers = response.headers

        self.assertEqual(response.status_code, 200, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        json_data = response.json()
        db_storage.reload()
        proposal = db_storage.get(Proposal, self.proposal_id)
        self.assertEqual(proposal.label, 'toto2')
        self.assertIn('label', json_data, MISSING_LABEL_ATTR_MSG)
        self.assertIn('created_at', json_data, MISSING_CREATED_AT_ATTR_MSG)
        self.assertIn('updated_at', json_data, MISSING_UPDATED_AT_ATTR_MSG)
        self.assertIn('__class__', json_data, MISSING_CLASS_ATTR_MSG)
        self.assertEqual(json_data['label'], 'toto2')
        db_storage.delete(proposal)
        db_storage.save()

    def testNotAJson(self):
        """
            Test update proposal action when given wrong data format.
        """

        data = {'label': 'toto'}
        response = self.get_authenticated_response(
            http_method='put', data=data)
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
            Test update proposal action when given wrong proposal_id or no ID at all.
        """

        data = {'label': 'toto2'}
        response = self.get_authenticated_response(
            http_method='put', url=self.invalid_url, json=data)
        headers = response.headers

        self.assertEqual(response.status_code, 404, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)
        self.assertTrue(self.proposal == db_storage.get(
            Proposal, self.proposal_id))
        json_data = response.json()
        self.assertIn('status', json_data)
        self.assertEqual(json_data['status'], 'fail')
        self.assertIn('message', json_data)
        self.assertEqual(json_data['message'], 'Proposal entity not found.')
