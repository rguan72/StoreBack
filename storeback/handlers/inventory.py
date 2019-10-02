from flask import Blueprint, request, jsonify, abort
from flask_cors import CORS
from storeback.models import db
from storeback.models.inventories import Inventory
from storeback.models.keys import Key
from storeback.utils import utils

inventory_api = Blueprint('inventory_api', __name__)
CORS(inventory_api)

@inventory_api.route('/api/inventory', methods=['GET'])
def get_all_items():
    admin_id = utils.get_admin_id_from_headers()
    params = dict(request.args)
    params['admin_id'] = admin_id
    items = Inventory.query.filter_by(**params).all()
    return jsonify([item.to_json() for item in items])

@inventory_api.route('/api/inventory/<int:id>', methods=['GET'])
def get_one_item_by_id(id):
    admin_id = utils.get_admin_id_from_headers()
    item = Inventory.query.filter_by(id=id, admin_id=admin_id).first_or_404()
    return jsonify(item.to_json())

@inventory_api.route('/api/inventory', methods=['POST'])
def create_one_item():
    if not request.json:
        return "Please provide a valid JSON body with your request", 400
    admin_id = utils.get_admin_id_from_headers()
    item = Inventory()
    item.name = request.json.get('name')
    item.price = request.json.get('price')
    item.admin_id = admin_id
    db.session.add(item)
    db.session.commit()

    return jsonify(item.to_json())

@inventory_api.route('/api/inventory/<int:id>', methods=['PATCH'])
def patch_one_item(id):
    if not request.json:
        return 'Please provide a valid JSON body with your request', 400

    if 'created' in request.json or 'updated' in request.json or 'admin_id' in request.json:
        return 'Please provide a valid JSON body with your request. "created", "updated", and "admin_id" are reserved fields', 400
    
    admin_id = utils.get_admin_id_from_headers()
    item = Inventory.query.filter_by(id=id, admin_id=admin_id).update(request.json)
    db.session.commit()

    patched_item = Inventory.query.filter_by(id=id, admin_id=admin_id).first_or_404()
    return jsonify(patched_item.to_json())

@inventory_api.route('/api/inventory/<int:id>', methods=['DELETE'])
def delete_one_item(id):
    admin_id = utils.get_admin_id_from_headers()
    item_to_delete = Inventory.query.filter_by(id=id, admin_id=admin_id).first()
    if item_to_delete:
        db.session.delete(item_to_delete)
        db.session.commit()
    return '', 204

    

