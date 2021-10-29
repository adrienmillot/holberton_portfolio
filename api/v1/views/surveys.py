#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Surveys.
"""

from api.v1.views import app_views
from math import ceil
from models.survey import Survey
from models.user import User
from models import db_storage
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/surveys', methods=['GET'], strict_slashes=False)
@swag_from('documentation/survey/all_surveys.yml')
def surveys_list():
    """
        Retrieves the list of all survey objects
        or a specific survey.
    """

    count = db_storage.count(Survey)
    page = request.args.get('page', None)
    limit = request.args.get('limit', None)
    if limit is not None:
        limit = int(limit)
    if page is None and limit is not None:
        page = 1

    page_count = int(ceil(count / limit)) if limit else 1
    if page is not None:
        page = int(page)
        deviation = page - page_count
        page = abs(deviation) + 1

    all_surveys = db_storage.all(Survey, page=page, limit=limit).values()
    list_surveys = []

    for survey in all_surveys:
        list_surveys.append(survey.to_dict())

    responseObject = {
        'status': 'success',
        'count': count,
        'page_count': page_count,
        'results': list_surveys
    }

    return make_response(jsonify(responseObject), 200)


@app_views.route('/surveys/<survey_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/survey/get_survey.yml', methods=['GET'])
def get_survey(survey_id):
    """
        Retrieves an survey.
    """

    survey = db_storage.get(Survey, survey_id)

    if not survey:
        responseObject = {
            'status': 'fail',
            'message': 'Survey entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    return jsonify(survey.to_dict())


@app_views.route('/surveys/<survey_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/survey/delete_survey.yml', methods=['DELETE'])
def delete_survey(survey_id):
    """
        Deletes a survey Object.
    """

    survey = db_storage.get(Survey, survey_id)

    if not survey:
        responseObject = {
            'status': 'fail',
            'message': 'Survey entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    survey.delete()
    db_storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/surveys', methods=['POST'], strict_slashes=False)
@swag_from('documentation/survey/post_survey.yml', methods=['POST'])
def create_survey():
    """
        Creates a survey.
    """

    if not request.get_json():
        responseObject = {
            'status': 'fail',
            'message': 'Not a JSON.'
        }

        return make_response(jsonify(responseObject), 400)

    if 'name' not in request.get_json():
        responseObject = {
            'status': 'fail',
            'message': 'Missing name.'
        }

        return make_response(jsonify(responseObject), 400)

    data = request.get_json()
    instance = Survey(**data)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/surveys/<survey_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/survey/put_survey.yml', methods=['PUT'])
def update_survey(survey_id):
    """
        Updates a survey.
    """

    survey = db_storage.get(Survey, survey_id)

    if not survey:
        responseObject = {
            'status': 'fail',
            'message': 'Survey entity not found.'
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
            setattr(survey, key, value)
    db_storage.save()

    return make_response(jsonify(survey.to_dict()), 200)


@app_views.route('/surveys/unanswered', methods=['GET'], strict_slashes=False)
@swag_from('documentation/survey/unanswered_survey.yml')
def unanswered_survey():
    """
        List all unanswered survey for a specified user.
    """
    headers = request.headers
    auth_token = headers['Authorization'].split(' ')[1]
    user_id = User.decode_auth_token(auth_token)
    surveys = db_storage.unanswered_survey(user_id)

    if not surveys:
        responseObject = {
            'status': 'fail',
            'message': 'Survey list not found.'
        }

        return make_response(jsonify(responseObject), 404)

    list_surveys = []

    for survey in surveys:
        list_surveys.append(survey.to_dict())

    responseObject = {
        'status': 'success',
        'results': list_surveys,
        'count': len(list_surveys)
    }

    return make_response(jsonify(responseObject), 200)


@app_views.route('/surveys/<survey_id>/score', methods=['GET'], strict_slashes=False)
@swag_from('documentation/survey/survey_user_score.yml')
def survey_user_score(survey_id):
    """
        Show the score on a survey for a specified user.
    """
    headers = request.headers
    auth_token = headers['Authorization'].split(' ')[1]
    user_id = User.decode_auth_token(auth_token)
    survey = db_storage.get(Survey, survey_id)

    max_score = db_storage.max_score(Survey, survey_id)
    user_score = db_storage.user_score(Survey, survey_id, user_id)

    stats = {'max_score': max_score, 'user_score': user_score}

    survey.stats = stats

    responseObject = {
        'status': 'succes',
        'survey': survey.to_dict(),
        'message': 'Your score on this survey is {}/{}'.format(user_score, max_score)
    }

    return make_response(jsonify(responseObject), 200)

@app_views.route('/surveys/score', methods=['GET'], strict_slashes=False)
@swag_from('documentation/survey/all_user_score.yml')
def all_survey_user_score():
    """
        Show the score on a survey for a specified user.
    """
    headers = request.headers
    auth_token = headers['Authorization'].split(' ')[1]
    user_id = User.decode_auth_token(auth_token)

    if user_id is None:
        responseObject = {
            'status': 'fail',
            'message': 'User entity not found.'
        }

        return make_response(jsonify(responseObject), 404)
    
    limit = request.args.get('limit', None)
    if limit is not None:
        limit = int(limit)

    all_max_score = dict(db_storage.all_max_score(Survey, user_id, limit))
    all_user_score = dict(db_storage.all_user_score(Survey, user_id, limit))

    if all_max_score is None:
        responseObject = {
            'status': 'fail',
            'message': 'No data avalaible, please contribute\
                        to a survey in order to see some.'
        }

        return make_response(jsonify(responseObject), 404)

    for key, value in all_max_score.items():
        if key not in all_user_score:
            all_user_score.update({key: 0})

    responseObject = {
        'status': 'succes',
        'max_score': all_max_score,
        'user_score': all_user_score
    }

    return make_response(jsonify(responseObject), 200)
