#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template, make_response, redirect, url_for
import jinja_partials

app = Flask(__name__)
app.debug = True


jinja_partials.register_extensions(app)


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


@app.route('/profiles_list', methods=['GET'],strict_slashes=False)
def profile_list():
    """return user's profile page"""
    return render_template('/profiles/profiles_list.html')

@app.route('/profile_create', methods=['GET', 'POST'],strict_slashes=False)
def profile_create():
    """return user's profile page"""
    return render_template('/profiles/profile_create.html')


@app.route('/surveys_list', methods=['GET'], strict_slashes=False)
def surveys_list():
    """return list of the surveys page"""
    return render_template('/surveys/surveys_list.html')

@app.route('/survey_create', methods=['GET', 'POST'],strict_slashes=False)
def survey_create():
    """return create survey page"""
    return render_template('/surveys/survey_create.html')

@app.route('/survey_show', methods=['GET'],strict_slashes=False)
def survey_show():
    """return specific survey page"""
    return render_template('/surveys/survey_show.html')

@app.route('/survey_edit', methods=['GET', 'POST'],strict_slashes=False)
def survey_edit():
    """return survey edit page"""
    return render_template('/surveys/survey_edit.html')

@app.route('/categories', methods=['GET', 'POST'],strict_slashes=False)
def categories_list():
    """return categories liste page"""
    return render_template('categories/categories_list.html')


@app.route('/dashboard', methods=['GET'], strict_slashes=False)
def dashboard():
    """return dashboard page"""
    return render_template('dashboard.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)