from flask import Blueprint
from storeback.models import db
from storeback.models.users import User

user_api = Blueprint('user_api', __name__)