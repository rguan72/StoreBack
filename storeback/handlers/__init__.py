from flask import Blueprint
from .merchant import merchant_api
from .inventory import inventory_api
from .user import user_api

ping_api = Blueprint('ping_api', __name__)
@ping_api.route('/ping', methods=['GET'])
def ping():
    return 'PONG.'

routes = [
    ping_api,
    merchant_api,
    inventory_api,
    user_api,
]
