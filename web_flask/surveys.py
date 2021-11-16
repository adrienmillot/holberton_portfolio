#!/usr/bin/python3
"""
    Survey routes
"""


from flask import Flask, render_template, request
from web_flask import app


@app.route('/surveys', methods=['GET'], strict_slashes=False)
def surveys_list():
    """
        return list of the surveys page
    """
    page = request.args.get('page', 1)
    return render_template('/surveys/surveys_list.html', page=page)


@app.route('/surveys/create', methods=['GET', 'POST'], strict_slashes=False)
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


@app.route('/surveys/<survey_id>/edit', methods=['GET', 'POST'], strict_slashes=False)
def survey_edit(survey_id):
    """
        return survey edit page
    """
    return render_template('/surveys/survey_edit.html')


@app.route('/surveys/<survey_id>/<survey_name>/answer', methods=['GET', 'POST'], strict_slashes=False)
def answer_survey(survey_id, survey_name):
    """
		return survey anwer page
    """  
    return render_template('/answer.html', survey_id=survey_id, survey_name=survey_name)

@app.route('/surveys/fullcreate', methods=['GET', 'POST'], strict_slashes=False)
def survey_create_complete():
    """
		returne a full survey creation page
    """
    return render_template('surveys/survey_create_full.html')