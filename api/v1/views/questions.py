#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Questions.
"""

import bcrypt
from os import getenv
from api.v1.views import app_views
from models.survey import Survey
from models.category import Category
from models.question import Question
from models import db_storage
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/questions', methods=['GET'], strict_slashes=False)
@swag_from('documentation/question/all_questions.yml')
def questions_list():
    """
        Retrieves the list of all question objects
        or a specific question.
    """

    all_questions = db_storage.all(Question).values()
    list_questions = []

    for question in all_questions:
        list_questions.append(question.to_dict())

    responseObject = {
        'status': 'success',
        'results': list_questions
    }

    return make_response(jsonify(responseObject), 200)
