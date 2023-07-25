#!/usr/bin/python3
"""
Importing Blueprint
"""

from api.v1.views import *

# api/v1/views/__init__.py

from flask import Blueprint

# Create the Blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import the views.index module
