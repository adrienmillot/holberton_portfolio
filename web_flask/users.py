#!/usr/bin/python3
"""
    user routes
"""


from flask import Flask, render_template, request
from web_flask import app


@app.route('/users', methods=['GET'], strict_slashes=False)
def users_list():
    """
        return list of the users page
    """
    page = request.args.get('page', 1)
    return render_template('/users/users_list.html', page=page)

@app.route('/users/create', methods=['GET', 'POST'], strict_slashes=False)
def user_create():
    """
        return create user page
    """

    return render_template('/users/user_create.html')

@app.route('/users/<user_id>/show', methods=['GET'], strict_slashes=False)
def user_show(user_id):
    """
        return specific user page
    """

    return render_template('/users/user_show.html')

@app.route('/users/<user_id>/edit', methods=['GET', 'POST'],strict_slashes=False)
def user_edit(user_id):
    """
        return user edit page
    """

    return render_template('/users/user_edit.html')

