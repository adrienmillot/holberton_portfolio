#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Categories.
"""

from api.v1.views import app_views
from models.category import Category
from models import db_storage
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/categories', methods=['GET'], strict_slashes=False)
@swag_from('documentation/category/all_categories.yml')
def categories_list():
    """
        Retrieves the list of all categories objects
        or a specific category.
    """

    all_categories = db_storage.all(Category).values()
    list_categories = []

    for category in all_categories:
        list_categories.append(category.to_dict())

    responseObject = {
        'status': 'success',
        'results': list_categories
    }

    return make_response(jsonify(responseObject), 200)

@app_views.route('/categories/<category_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/category/get_category.yml', methods=['GET'])
def get_category(category_id):
    """
        Retrieves an category.
    """

    category = db_storage.get(Category, category_id)

    if not category:
        responseObject = {
            'status': 'fail',
            'message': 'Category entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    return jsonify(category.to_dict())
