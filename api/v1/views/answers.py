#!/usr/bin/python3

from api.v1.views import app_views
from flask import make_response, jsonify, request
from flasgger.utils import swag_from
from models import db_storage
from models.proposal import Proposal
from models.user import User

@app_views.route('/proposals/<proposal_id>/answers', methods=['POST'], strict_slashes=False)
@swag_from('documentation/answer/post_answer.yml')
def create_answer(proposal_id):
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
    
    # Test Proposal entity exists
    proposal = db_storage.get(Proposal, proposal_id)

    if proposal is None:
        responseObject = {
            'status': 'fail',
            'message': 'Proposal entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    user.answers.append(proposal)
    user.save()

    responseObject = {
        'status': 'success',
        'message': 'Thanks for answering.'
    }

    return make_response(jsonify(responseObject), 201)


@app_views.route('/proposals/<proposal_id>/answers', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/answer/delete_answer.yml')
def delete_answer(proposal_id):
    # Test Proposal entity exists
    proposal = db_storage.get(Proposal, proposal_id)

    if proposal is None:
        responseObject = {
            'status': 'fail',
            'message': 'Proposal entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    data = request.get_json()

    # Any user_id parameters was given
    if 'user_id' not in data:
        responseObject = {
            'status': 'fail',
            'message': 'Missing user_id.'
        }

        return make_response(jsonify(responseObject), 404)

    # Test User entity exists
    user = db_storage.get(User, data['user_id'])

    if user is None:
        responseObject = {
            'status': 'fail',
            'message': 'User entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    # Check if is answered
    if proposal not in user.answers:
        responseObject = {
            'status': 'fail',
            'message': "You didn't answered"
        }

        return make_response(jsonify(responseObject), 404)

    user.answers.remove(proposal)
    user.save()

    return make_response(jsonify({}), 200)
