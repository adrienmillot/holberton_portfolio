#!/usr/bin/python3
"""
    Profile routes
"""


from flask import Flask, render_template, request
from web_flask import app


@app.route('/profiles', methods=['GET'], strict_slashes=False)
def profiles_list():
    """
        return user's profile page
    """
    page = request.args.get('page', 1)
    return render_template('/profiles/profiles_list.html', page=page)


@app.route('/profiles/create', methods=['GET', 'POST'], strict_slashes=False)
def profile_create():
    """
        return user's profile page
    """

    return render_template('/profiles/profile_create.html')

@app.route('/profiles/<profile_id>/show', methods=['GET'], strict_slashes=False)
def profile_show(profile_id):
    """
        return specific profile page
    """

    return render_template('/profiles/profile_show.html')

@app.route('/profiles/<profile_id>/edit', methods=['GET', 'POST'],strict_slashes=False)
def profile_edit(profile_id):
    """
        return profile edit page
    """

    return render_template('/profiles/profile_edit.html')
