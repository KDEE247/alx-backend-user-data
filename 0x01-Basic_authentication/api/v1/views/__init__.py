!/usr/bin/env python3
from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.users import *
""" DocDocDocDocDocDoc
"""

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

User.load_from_file()
