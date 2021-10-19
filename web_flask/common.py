#!/usr/bin/python3
"""
    Common routes
"""


from flask import Flask, render_template, send_from_directory
from web_flask import app


@app.route('/favicon.ico', strict_slashes=False)
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'SurveyStorm_icon.png', mimetype='image/vnd.microsoft.icon')


@app.route('/', strict_slashes=False)
def homepage():
    """ return the index pasgeg """
    return render_template('homepage.html')


@app.route('/login', strict_slashes=False)
def login():
    """return login page"""
    return render_template('login.html')


# @app.route('/sign_up', methods=['POST', 'GET'], strict_slashes=False)
# def sign_up():
#     """ return sign_up page """
#     return render_template('sign_up.html')
