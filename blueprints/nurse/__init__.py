from flask import Blueprint
nurse = Blueprint('nurse', __name__, url_prefix='/nurse')

from blueprints.nurse.main import *