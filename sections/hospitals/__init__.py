from flask import Blueprint
hospitals = Blueprint('hospitals', __name__, url_prefix='/hospitals')

from sections.hospitals.dashboard import *
from sections.hospitals.search_engine import *
