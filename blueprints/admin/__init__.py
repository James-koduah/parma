from flask import Blueprint
admin = Blueprint('admin', __name__, url_prefix='/admin')

from blueprints.admin.main import *
