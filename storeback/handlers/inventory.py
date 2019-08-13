from flask import Blueprint, request, jsonify
from storeback.models import db
from storeback.models.inventories import Inventory

inventory_api = Blueprint('inventory_api', __name__)

@inventory_api.route('/api/inventory', methods=['GET'])
def get_all_items():
    items = Inventory.query.all()
    return jsonify([item.to_json() for item in items])

@inventory_api.route('/api/inventory/<int:id>', methods=['GET'])
def get_one_item_by_id(id):
    item = Inventory.query.filter_by(id=id).first_or_404()
    return jsonify(item.to_json())

@inventory_api.route('/api/inventory', methods=['POST'])
def create_one_item():
    if not request.json:
        return "Please provide a valid JSON body with your request", 400

    item = Inventory()
    item.name = request.json.get('name')
    item.price = request.json.get('price')
    item.merchant_id = request.json.get('merchant_id')
    db.session.add(item)
    db.session.commit()

    return jsonify(item.to_json())

@inventory_api.route('/api/inventory/<int:id>', methods=['PATCH'])
def patch_one_item(id):
    if not request.json:
        return 'Please provide a valid JSON body with your request', 400

    if 'created' in request.json or 'updated' in request.json:
        return 'Please provide a valid JSON body with your request. "created" and "updated" are reserved fields', 400
    
    item = Inventory.query.filter_by(id=id).update(request.json)
    db.session.commit()

    patched_item = Inventory.query.filter_by(id=id).first_or_404()
    return jsonify(patched_item.to_json())

@inventory_api.route('/api/inventory/<int:id>', methods=['DELETE'])
def delete_one_item(id):
    item_to_delete = Inventory.query.filter_by(id=id).first()
    if item_to_delete:
        db.session.delete(item_to_delete)
        db.session.commit()
    return '', 204

    

