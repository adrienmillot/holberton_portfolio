#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Profiles.
"""

import json

from api.v1.views import app_views
from math import ceil
from models import db_storage
from models.profile import Profile
from models.user import User
from flask import request, jsonify, make_response
from flasgger.utils import swag_from



@app_views.route('/profiles', methods=['GET'], strict_slashes=False)
@swag_from('documentation/profile/all_profiles.yml')
def profiles_list() -> json:
    """
        Retrieves the list of all profile objects
        or a specific profile.
    """

    count = db_storage.count(Profile)
    page = request.args.get('page', None)
    limit = request.args.get('limit', None)
    if limit is not None:
        limit = int(limit)
    if page is not None:
        page = int(page)
    if page is None and limit is not None:
        page = 1

    page_count = int(ceil(count / limit)) if limit else 1
    all_profiles = db_storage.all(Profile, page=page, limit=limit).values()
    list_profiles = []

    for profile in all_profiles:
        list_profiles.append(profile.to_dict())

    responseObject = {
        'status': 'success',
        'count': count,
        'page_count': page_count,
        'results': list_profiles
    }

    return make_response(jsonify(responseObject), 200)


@app_views.route('/profiles/<profile_id>', methods=['GET'])
@swag_from('documentation/profile/get_profile.yml')
def profile_show(profile_id) -> json:
    """
        Retrieves a specified Profile object.

        Args:
            profile_id : ID of the wanted Profile object.

        Raises:
            NotFound: Raises a 404 error if profile_id
            is not linked to any Profile object.

        Returns:
            json: Wanted Profile object with status code 200.
    """

    profile = db_storage.get(Profile, profile_id)

    if profile is None:

        responseObject = {
            'status': 'fail',
            'message': 'Profile entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    return make_response(jsonify(profile.to_dict()), 200)


@app_views.route('/profiles/<profile_id>', methods=['DELETE'])
@swag_from('documentation/profile/delete_profile.yml')
def profile_delete(profile_id) -> json:
    """
        Deletes a specified Profile object.

        Args:
            profile_id : ID of the wanted Profile object.

        Raises:
            NotFound: Raises a 404 error if profile_id
            is not linked to any Profile object.

        Returns:
            json: Empty dictionary with the status code 200.
    """
    profile = db_storage.get(Profile, profile_id)

    if profile is None:
        responseObject = {
            'status': 'fail',
            'message': 'Profile entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    profile.delete()
    db_storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/profiles', methods=['POST'], strict_slashes=False)
@swag_from('documentation/profile/post_profile.yml')
def profile_create() -> json:
    """
        Creates a new Profile object.

        Error cases:
            BadRequest: If the given data is not a
            valid json or if the key 'name' is not
            present sends status code 400.

        Returns:
            json: The new Profile with the status code 201.
    """

    if not request.json:
        responseObject = {
            'status': 'fail',
            'message': 'Not a JSON.'
        }

        return make_response(jsonify(responseObject), 400)

    profile = Profile(**request.get_json())
    profile.save()

    return make_response(jsonify(profile.to_dict()), 201)


@app_views.route('/profiles/<profile_id>', methods=['PUT'])
@swag_from('documentation/profile/put_profile.yml')
def profile_update(profile_id) -> json:
    """
        Update a specified Profile object.

        Args:
            profile_id : Id of the wanted Profile object.

        Returns:
            json: The updated Profile object with the status code 200.
    """

    profile = db_storage.get(Profile, profile_id)

    if profile is None:
        responseObject = {
            'status': 'fail',
            'message': 'Profile entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    if not request.json:
        responseObject = {
            'status': 'fail',
            'message': 'Not a JSON.'
        }

        return make_response(jsonify(responseObject), 400)

    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            profile.__setattr__(key, value)

    profile.save()

    return make_response(jsonify(profile.to_dict()), 200)
