from flask import Blueprint
user = Blueprint('user', __name__, url_prefix='/user')

from blueprints.user.main import *
