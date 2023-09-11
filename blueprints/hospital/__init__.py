from flask import Blueprint
hospital = Blueprint('hospital', __name__, url_prefix='/hospital')

from blueprints.hospital.invite import *
from blueprints.hospital.main import *
from blueprints.hospital.nurse import *
from blueprints.hospital.doctor import *
