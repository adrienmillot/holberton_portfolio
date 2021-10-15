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
