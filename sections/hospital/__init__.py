from flask import Blueprint
hospital = Blueprint('hospital', __name__, url_prefix='/hospital')

from sections.hospital.dashboard import *
