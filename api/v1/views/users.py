#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Users.
"""

from math import ceil
import bcrypt
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

    count = db_storage.count(User)
    page = request.args.get('page', None)
    limit = request.args.get('limit', None)
    if limit is not None:
        limit = int(limit)
    if page is not None:
        page = int(page)
    if page is None and limit is not None:
        page = 1

    page_count = int(ceil(count / limit)) if limit else 1
    all_users = db_storage.all(User, page=page, limit=limit).values()
    list_users = []

    for user in all_users:
        list_users.append(user.to_dict())

    responseObject = {
        'status': 'success',
        'count': count,
        'page_count': page_count,
        'results': list_users
    }

    return make_response(jsonify(responseObject), 200)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml')
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
@swag_from('documentation/user/delete_user.yml')
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

    user.delete()
    db_storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml')
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


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/user/put_user.yml')
def update_user(user_id):
    """
        Updates a user.
    """

    user = db_storage.get(User, user_id)

    if not user:
        responseObject = {
            'status': 'fail',
            'message': 'User entity not found.'
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
            setattr(user, key, value)
    db_storage.save()

    return make_response(jsonify(user.to_dict()), 200)


@app_views.route('/auth/login', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/login.yml')
def login():
    try:
        post_data = request.get_json()

        if not post_data:
            responseObject = {
                'status': 'fail',
                'message': 'Not a JSON.'
            }

            return make_response(jsonify(responseObject), 400)

        user = db_storage.get_from_attributes(
            User, username=post_data.get('username'))

        if user is None:
            responseObject = {
                'status': 'fail',
                'message': 'User does not exist.'
            }

            return make_response(jsonify(responseObject), 404)

        if not bcrypt.checkpw(post_data.get('password').encode(), user.password.encode()):
            responseObject = {
                'status': 'fail',
                'message': 'Invalid username/password combination.'
            }

            return make_response(jsonify(responseObject), 400)

        auth_token = user.encode_auth_token(user.id)

        if auth_token:
            responseObject = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'auth_token': auth_token.decode()
            }
            return make_response(jsonify(responseObject), 200)
    except Exception as exception:
        return make_response(jsonify(exception.args[0]), 500)


@app_views.route('/me', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/me.yml')
def me():
    """
        Return the specified user informations.
    """
    headers = request.headers
    auth_token = headers['Authorization'].split(' ')[1]
    user_id = User.decode_auth_token(auth_token)
    user = db_storage.get(User, user_id)
    profile = db_storage.get(Profile, user.profile_id)
    user.profile = profile.to_dict()

    if user is None:
        responseObject = {
            'status': 'fail',
            'message': 'User entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    if profile is None:
        responseObject = {
            'status': 'fail',
            'message': 'Profile entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    responseObject = {
        'status': 'success',
        'user': user.to_dict(),
    }

    return make_response(jsonify(responseObject), 200)


@app_views.route('/auth/verify_page', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/verify_page.yml')
def has_right_to_display_page():
    headers = request.headers
    auth_token = headers['Authorization'].split(' ')[1]
    user_id = User.decode_auth_token(auth_token)
    user = db_storage.get(User, user_id)

    if user is None:
        responseObject = {
            'status': 'fail',
            'message': 'User entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    data = request.args.get('entrypoint', None)

    if data is None:
        responseObject = {
            'status': 'fail',
            'message': 'Missing page entrypoint.'
        }

        return make_response(jsonify(responseObject), 400)

    if (
        'ROLE_ADMIN' not in user.roles and 'ROLE_USER' in user.roles and data not in (
            '/', '/login', '/logout', '/answers', '/dashboard')
    ):
        responseObject = {
            'status': 'fail',
            'message': 'You have not right to display this page.'
        }

        return make_response(jsonify(responseObject), 400)

    responseObject = {
        'status': 'success',
        'message': 'You are authorized to display this page.'
    }

    return make_response(jsonify(responseObject), 200)
