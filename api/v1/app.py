#!/usr/bin/python3
""" Flask Application """
from models import db_storage
from api.v1.views import app_views
from os import getenv
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

from models.user import User

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.before_request
def before_request():
    from flask import request

    # return make_response(jsonify(request.endpoint), 200)

    if request.endpoint in (
        'app_views.login',
        'flasgger.apidocs',
        'flasgger.static',
        'flasgger.apispec_1'
    ) or request.method == 'OPTIONS':
        return

    auth_header = request.headers.get('Authorization')

    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''

    if not auth_token:
        responseObject = {
            'status': 'fail',
            'message': 'You have to be logged.'
        }

        return make_response(jsonify(responseObject), 401)

    resp = User.decode_auth_token(auth_token)

    if resp == -1:
        responseObject = {
            'status': 'fail',
            'message': 'Invalid token.'
        }

        return make_response(jsonify(responseObject), 498)
    elif resp == -2:
        responseObject = {
            'status': 'fail',
            'message': 'Expired token.'
        }

        return make_response(jsonify(responseObject), 498)


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    db_storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'Survey Storm clone Restful API',
    'uiversion': 3
}

Swagger(app)


if __name__ == "__main__":
    """ Main Function """
    host = getenv('SS_API_HOST', '0.0.0.0')
    port = getenv('SS_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
