#!/usr/bin/python3
""" Starts a Flask Web Application """
from os import getenv
from flask import Flask, render_template, make_response, redirect, url_for
import jinja_partials
from flask_assets import Environment, Bundle

api_url = 'http://{}:5002/api/v{}'.format(getenv('WEB_URI', '0.0.0.0'), getenv('WEB_API_VERSION', '1'))
app = Flask(__name__)
app.debug = True
assets = Environment(app)
jinja_partials.register_extensions(app)

js = Bundle('scripts/event/log_out.js',
            'scripts/event/login_btn.js',
            'scripts/surveys_list.js',
            'scripts/event/survey_create.js',
            'scripts/event/survey_show.js',
            'scripts/event/survey_edit.js',
            'scripts/questions_list.js',
            'scripts/event/question_create.js',
            'scripts/event/question_show.js',
            'scripts/event/question_edit.js',
            'scripts/categories_list.js',
            'scripts/event/category_create.js',
            'scripts/event/category_edit.js',
            'scripts/event/category_show.js',
            'scripts/users_list.js',
            'scripts/event/user_create.js',
            'scripts/event/user_show.js',
            'scripts/event/proposal_show.js',
            'scripts/profiles_list.js',
            'scripts/event/profile_create.js',
            'scripts/event/profile_show.js',
            'scripts/proposals_list.js',
            'scripts/event/proposal_create.js',
            'scripts/event/proposal_show.js',
            output='gen/packed.js')
assets.register('js_all', js)

styles = Bundle('styles/footer.css')
assets.register('styles_all', styles)
assets.init_app(app)
