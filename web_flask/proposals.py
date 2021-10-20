#!/usr/bin/python3
"""
    Profile routes
"""


from flask import Flask, render_template
from web_flask import app


@app.route('/proposals', methods=['GET'], strict_slashes=False)
def proposals_list():
    """
        return user's proposals page
    """

    return render_template('/proposals/proposals_list.html')


@app.route('/proposals/create', methods=['GET', 'POST'], strict_slashes=False)
def proposal_create():
    """
        return proposale create page
    """

    return render_template('/proposals/proposal_create.html')
