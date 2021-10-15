#!/usr/bin/python3
"""
    Status
"""
from api.v1.views import app_views
from flask import jsonify
from flasgger.utils import swag_from


@app_views.route('/status', methods=['GET'], strict_slashes=False)
@swag_from('documentation/common/status.yml')
def status():
    """ Status of API """
    return jsonify({"status": "OK"})
