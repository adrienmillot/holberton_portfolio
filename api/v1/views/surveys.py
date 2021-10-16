#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Surveys.
"""

import bcrypt
from os import getenv
from api.v1.views import app_views
from models.profile import Profile
from models.survey import Survey
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

    all_surveys = db_storage.all(Survey).values()
    list_surveys = []

    for survey in all_surveys:
        list_surveys.append(survey.to_dict())

    responseObject = {
        'status': 'success',
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
