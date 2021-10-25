#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Questions.
"""

from math import ceil
import bcrypt
from os import getenv
from api.v1.views import app_views
from api.v1.views.surveys import surveys_list
from models.category import Category
from models.proposal import Proposal
from models.question import Question
from models.user import User
from models.survey import Survey
from models import db_storage
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from sqlalchemy.orm import session


@app_views.route('/questions', methods=['GET'], strict_slashes=False)
@swag_from('documentation/question/all_questions.yml')
def questions_list():
    """
        Retrieves the list of all question objects
        or a specific question.
    """

    data = request.get_json()
    count = db_storage.count(Question)
    page = data['page'] if data and 'page' in data.keys() else None
    limit = data['limit'] if data and 'limit' in data.keys() else None
    page_count = int(ceil(count / limit)) if limit else 1
    all_questions = db_storage.all(Question, page=page, limit=limit).values()
    list_questions = []

    for question in all_questions:
        list_questions.append(question.to_dict())

    responseObject = {
        'status': 'success',
        'count': count,
        'page_count': page_count,
        'results': list_questions
    }

    return make_response(jsonify(responseObject), 200)


@app_views.route('/questions/<question_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/question/get_question.yml')
def get_question(question_id):
    """
        Retrieves an question.
    """

    question = db_storage.get(Question, question_id)

    if not question:
        responseObject = {
            'status': 'fail',
            'message': 'Question entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    return jsonify(question.to_dict())


@app_views.route('/questions/<question_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/question/delete_question.yml')
def delete_question(question_id):
    """
        Deletes a question Object.
    """

    question = db_storage.get(Question, question_id)

    if not question:
        responseObject = {
            'status': 'fail',
            'message': 'Question entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    question.delete()
    db_storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/questions', methods=['POST'], strict_slashes=False)
@swag_from('documentation/question/post_question.yml')
def create_question():
    """
        Creates a question.
    """

    if not request.get_json():
        responseObject = {
            'status': 'fail',
            'message': 'Not a JSON.'
        }

        return make_response(jsonify(responseObject), 400)

    data = request.get_json()

    if 'label' not in data:
        responseObject = {
            'status': 'fail',
            'message': 'Missing label.'
        }

        return make_response(jsonify(responseObject), 400)

    if 'category_id' not in data:
        responseObject = {
            'status': 'fail',
            'message': 'Missing category_id.'
        }

        return make_response(jsonify(responseObject), 400)

    category = db_storage.get(Category, data['category_id'])

    if not category:
        responseObject = {
            'status': 'fail',
            'message': 'Category entity not found.'
        }

        return make_response(jsonify(responseObject), 400)

    if 'survey_id' not in data:
        responseObject = {
            'status': 'fail',
            'message': 'Missing survey_id.'
        }

        return make_response(jsonify(responseObject), 400)

    survey = db_storage.get(Survey, data['survey_id'])

    if not survey:
        responseObject = {
            'status': 'fail',
            'message': 'Survey entity not found.'
        }

        return make_response(jsonify(responseObject), 400)

    instance = Question(**data)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/questions/<question_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/question/put_question.yml')
def update_question(question_id):
    """
        Updates a question.
    """

    question = db_storage.get(Question, question_id)

    if not question:
        responseObject = {
            'status': 'fail',
            'message': 'Question entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    if not request.get_json():
        responseObject = {
            'status': 'fail',
            'message': 'Not a JSON.'
        }

        return make_response(jsonify(responseObject), 400)

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(question, key, value)
    db_storage.save()

    return make_response(jsonify(question.to_dict()), 200)


@app_views.route('/surveys/<survey_id>/question', methods=['GET'], strict_slashes=False)
@swag_from('documentation/question/unanswered_question.yml')
def survey_question(survey_id):
    """
        Show unanswered question of a survey for a specified user.
    """
    headers = request.headers
    auth_token = headers['Authorization'].split(' ')[1]
    user_id = User.decode_auth_token(auth_token)
    question = db_storage.random_survey_question(survey_id, user_id)

    if not question:
        responseObject = {
            'status': 'fail',
            'message': 'Question entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    responseObject = {
        'status': 'success',
        'result': question[1].to_dict(),
        'count': question[0]
    }

    return make_response(jsonify(responseObject), 200)
