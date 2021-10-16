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
