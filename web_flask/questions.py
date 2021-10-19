#!/usr/bin/python3
"""
    question routes
"""


from flask import Flask, render_template
from web_flask import app


@app.route('/questions', methods=['GET'], strict_slashes=False)
def questions_list():
    """
        return list of the questions page
    """

    return render_template('/questions/questions_list.html')

@app.route('/questions/create', methods=['GET', 'POST'], strict_slashes=False)
def question_create():
    """
        return create question page
    """

    return render_template('/questions/question_create.html')

@app.route('/questions/<question_id>/show', methods=['GET'], strict_slashes=False)
def question_show(question_id):
    """
        return specific question page
    """

    return render_template('/questions/question_show.html')

@app.route('/questions/<question_id>/edit', methods=['GET', 'POST'],strict_slashes=False)
def question_edit(question_id):
    """
        return question edit page
    """

    return render_template('/questions/question_edit.html')
