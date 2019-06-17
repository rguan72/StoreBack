from flask import Blueprint


inventory_api = Blueprint('inventory_api', __name__)

@inventory_api.route('/api/inventory/', methods=['GET'])
def ping():
    return 'Inventory API hit'

