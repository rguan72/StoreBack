from flask import Blueprint
from .inventory import inventory_api
from .admin import admin_api
from .key import key_api
from .user import user_api
from .error import error_api

ping_api = Blueprint('ping_api', __name__)
@ping_api.route('/ping', methods=['GET'])
def ping():
    return 'PONG.'

routes = [
    ping_api,
    inventory_api,
    admin_api,
    key_api,
    user_api,
    error_api,
]
