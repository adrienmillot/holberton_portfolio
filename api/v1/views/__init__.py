#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.answers import *
from api.v1.views.categories import *
from api.v1.views.questions import *
from api.v1.views.profiles import *
from api.v1.views.proposals import *
from api.v1.views.status import *
from api.v1.views.surveys import *
from api.v1.views.users import *
