from flask import request, jsonify, Blueprint
from storeback.models import db
from storeback.models.keys import Key

key_api = Blueprint('key_api', __name__)