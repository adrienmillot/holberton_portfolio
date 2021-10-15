#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Profiles.
"""

import json
from api.v1.views import app_views
from models.profile import Profile
from models import db_storage
from flask import jsonify, make_response
from flasgger.utils import swag_from


@app_views.route('/profiles', methods=['GET'], strict_slashes=False)
@swag_from('documentation/profile/all_profiles.yml')
def profiles_list() -> json:
    """
        Retrieves the list of all profile objects
        or a specific profile.
    """

    all_profiles = db_storage.all(Profile).values()
    list_profiles = []

    for profile in all_profiles:
        list_profiles.append(profile.to_dict())

    responseObject = {
        'status': 'success',
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
