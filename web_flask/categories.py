#!/usr/bin/python3
"""
    category routes
"""


from flask import Flask, render_template, request
from web_flask import app


@app.route('/categories', methods=['GET'], strict_slashes=False)
def categories_list():
    """
        return list of the categories page
    """
    page = request.args.get('page', 1)
    return render_template('/categories/categories_list.html', page=page)


@app.route('/categories/create', methods=['GET', 'POST'], strict_slashes=False)
def category_create():
    """
        return create category page
    """

    return render_template('/categories/category_create.html')


@app.route('/categories/<category_id>/show', methods=['GET'], strict_slashes=False)
def category_show(category_id):
    """
        return specific category page
    """

    return render_template('/categories/category_show.html')


@app.route('/categories/<category_id>/edit', methods=['GET', 'POST'], strict_slashes=False)
def category_edit(category_id):
    """
        return category edit page
    """

    return render_template('/categories/category_edit.html')
