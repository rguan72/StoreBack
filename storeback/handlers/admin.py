from flask import Blueprint, request, jsonify
from storeback.models import db
from storeback.models.admins import Admin

admin_api = Blueprint('admin_api', __name__)