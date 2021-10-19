#!/usr/bin/python3
"""
    Survey routes
"""


from flask import Flask, render_template
from web_flask import app


@app.route('/surveys', methods=['GET'], strict_slashes=False)
def surveys_list():
    """
        return list of the surveys page
    """

    return render_template('/surveys/surveys_list.html')

@app.route('/surveys/new', methods=['GET', 'POST'], strict_slashes=False)
def survey_create():
    """
        return create survey page
    """

    return render_template('/surveys/survey_create.html')

@app.route('/surveys/<survey_id>/show', methods=['GET'], strict_slashes=False)
def survey_show(survey_id):
    """
        return specific survey page
    """

    return render_template('/surveys/survey_show.html')

@app.route('/surveys/<survey_id>/edit', methods=['GET', 'POST'],strict_slashes=False)
def survey_edit(survey_id):
    """
        return survey edit page
    """

    return render_template('/surveys/survey_edit.html')
