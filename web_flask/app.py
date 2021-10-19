#!/usr/bin/python3
""" Starts a Flask Web Application """


from web_flask import app
from web_flask.categories import *
from web_flask.common import *
from web_flask.profiles import *
from web_flask.questions import *
from web_flask.surveys import *
from web_flask.users import *


@app.route('/dashboard', methods=['GET'], strict_slashes=False)
def dashboard():
    """return dashboard page"""
    return render_template('dashboard.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
