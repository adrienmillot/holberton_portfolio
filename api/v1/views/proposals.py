#!/usr/bin/python3
"""
    objects that handle all default RestFul API actions for Proposals.
"""

from api.v1.views import app_views
from models.proposal import Proposal
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

    all_proposals = db_storage.all(Proposal).values()
    list_proposals = []

    for proposal in all_proposals:
        list_proposals.append(proposal.to_dict())

    responseObject = {
        'status': 'success',
        'results': list_proposals
    }

    return make_response(jsonify(responseObject), 200)
