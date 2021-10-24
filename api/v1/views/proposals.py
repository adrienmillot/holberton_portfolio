#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Proposals.
"""

from api.v1.views import app_views
from math import ceil
from models.proposal import Proposal
from models.question import Question
from models import db_storage
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/proposals', methods=['GET'], strict_slashes=False)
@swag_from('documentation/proposal/all_proposals.yml')
def proposals_list():
    """
        Retrieves the list of all proposal objects
        or a specific proposal.
    """

    data = request.get_json()
    count = db_storage.count(Proposal)
    page = data['page'] if data and 'page' in data.keys() else None
    limit = data['limit'] if data and 'limit' in data.keys() else None
    page_count = int(ceil(count / limit)) if limit else 1
    all_proposals = db_storage.all(Proposal, page=page, limit=limit).values()
    list_proposals = []

    for proposal in all_proposals:
        list_proposals.append(proposal.to_dict())

    responseObject = {
        'status': 'success',
        'count': count,
        'page_count': page_count,
        'results': list_proposals
    }

    return make_response(jsonify(responseObject), 200)


@app_views.route('/proposals/<proposal_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/proposal/get_proposal.yml')
def get_proposal(proposal_id):
    """
        Retrieves an proposal.
    """

    proposal = db_storage.get(Proposal, proposal_id)

    if not proposal:
        responseObject = {
            'status': 'fail',
            'message': 'Proposal entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    return jsonify(proposal.to_dict())


@app_views.route('/proposals/<proposal_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/proposal/delete_proposal.yml')
def delete_proposal(proposal_id):
    """
        Deletes a proposal Object.
    """

    proposal = db_storage.get(Proposal, proposal_id)

    if not proposal:
        responseObject = {
            'status': 'fail',
            'message': 'Proposal entity not found.'
        }

        return make_response(jsonify(responseObject), 404)

    proposal.delete()
    db_storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/proposals', methods=['POST'], strict_slashes=False)
@swag_from('documentation/proposal/post_proposal.yml')
def create_proposal():
    """
        Creates a proposal.
    """

    if not request.get_json():
        responseObject = {
            'status': 'fail',
            'message': 'Not a JSON.'
        }

        return make_response(jsonify(responseObject), 400)

    data = request.get_json()

    if 'label' not in data:
        responseObject = {
            'status': 'fail',
            'message': 'Missing label.'
        }

        return make_response(jsonify(responseObject), 400)

    if 'question_id' not in data:
        responseObject = {
            'status': 'fail',
            'message': 'Missing question_id.'
        }

        return make_response(jsonify(responseObject), 400)

    question = db_storage.get(Question, data['question_id'])

    if not question:
        responseObject = {
            'status': 'fail',
            'message': 'Question entity not found.'
        }

        return make_response(jsonify(responseObject), 400)

    instance = Proposal(**data)
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/proposals/<proposal_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/proposal/put_proposal.yml')
def update_proposal(proposal_id):
    """
        Updates a proposal.
    """

    proposal = db_storage.get(Proposal, proposal_id)

    if not proposal:
        responseObject = {
            'status': 'fail',
            'message': 'Proposal entity not found.'
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
            setattr(proposal, key, value)
    db_storage.save()

    return make_response(jsonify(proposal.to_dict()), 200)

@app_views.route('/questions/<question_id>/proposals', methods=['GET'], strict_slashes=False)
@swag_from('documentation/survey/question_proposals.yml')
def question_proposals(question_id):
    """
        List all proposals for a specified question.
    """
    proposals = db_storage.all_question_proposals(question_id)

    if not proposals:
        responseObject = {
            'status': 'fail',
            'message': 'Proposal list not found.'
        }

        return make_response(jsonify(responseObject), 404)

    list_proposals = []

    for survey in proposals:
        list_proposals.append(survey.to_dict())

    responseObject = {
        'status': 'success',
        'results': list_proposals
    }

    return make_response(jsonify(list_proposals), 200)
