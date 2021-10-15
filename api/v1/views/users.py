#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Users.
"""

from os import getenv
from api.v1.views import app_views
from models.profile import Profile
from models.user import User
from models import db_storage
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def users_list():
    """
        Retrieves the list of all user objects
        or a specific user.
    """

    all_users = db_storage.all(User).values()
    list_users = []

    for user in all_users:
        list_users.append(user.to_dict())

    responseObject = {
        'status': 'success',
        'results': list_users
    }

    return make_response(jsonify(responseObject), 200)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_user(user_id):
    """
        Retrieves an user.
    """

    user = db_storage.get(User, user_id)

    if not user:
        responseObject = {
            'status': 'fail',
            'message': 'User entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/user/delete_user.yml', methods=['DELETE'])
def delete_user(user_id):
    """
        Deletes a user Object.
    """

    user = db_storage.get(User, user_id)

    if not user:
        responseObject = {
            'status': 'fail',
            'message': 'User entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    db_storage.delete(user)
    db_storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def create_user():
    """
        Creates a user.
    """

    if not request.get_json():
        responseObject = {
            'status': 'fail',
            'message': 'Not a JSON.'
        }

        return make_response(jsonify(responseObject), 400)

    if 'username' not in request.get_json():
        responseObject = {
            'status': 'fail',
            'message': 'Missing username.'
        }

        return make_response(jsonify(responseObject), 400)

    if 'password' not in request.get_json():
        responseObject = {
            'status': 'fail',
            'message': 'Missing password.'
        }

        return make_response(jsonify(responseObject), 400)

    if 'profile_id' not in request.get_json():
        responseObject = {
            'status': 'fail',
            'message': 'Missing profile_id.'
        }

        return make_response(jsonify(responseObject), 400)

    data = request.get_json()
    profile = db_storage.get(Profile, data['profile_id'])

    if not profile:
        responseObject = {
            'status': 'fail',
            'message': 'Profile entity not found.'
        }

        return make_response(jsonify(responseObject), 400)

    data = request.get_json()
    instance = User(**data)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)
