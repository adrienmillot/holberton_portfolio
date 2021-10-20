#!/usr/bin/python3
"""
    Profile routes
"""


from flask import Flask, render_template
from web_flask import app


@app.route('/profiles', methods=['GET'], strict_slashes=False)
def profiles_list():
    """
        return user's profile page
    """

    return render_template('/profiles/profiles_list.html')


@app.route('/profiles/create', methods=['GET', 'POST'], strict_slashes=False)
def profile_create():
    """
        return user's profile page
    """

    return render_template('/profiles/profile_create.html')
