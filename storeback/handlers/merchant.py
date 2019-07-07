from flask import Blueprint, request, jsonify
from storeback.models.merchants import Merchant
from storeback.models import db


merchant_api = Blueprint('merchant', __name__)

@merchant_api.route('/api/merchant', methods=['GET'])
def get_all_merchants():
    merchants = Merchant.query.all()
    return jsonify([merchant.to_json() for merchant in merchants])

@merchant_api.route('/api/merchant/<int:id>', methods=['GET'])
def get_one_merchant(id):
    merchant = Merchant.query.filter_by(id=id).first_or_404()
    return jsonify(merchant.to_json())

@merchant_api.route('/api/merchant', methods=['POST'])
def create_one_merchant():
    if not request.json:
        return 'Please provide a valid JSON body with your request', 400
    
    merchant = Merchant()
    merchant.name = request.json.get('name')
    db.session.add(merchant)
    db.session.commit()

    return jsonify(merchant.to_json())

@merchant_api.route('/api/merchant/<int:id>', methods=['PATCH'])
def patch_one_merchant(id):
    if not request.json:
        return 'Please provide a valid JSON body with your request', 400
    
    merchant = Merchant.query.filter_by(id=id).update(request.json)
    db.session.commit()

    patched_merchant = Merchant.query.filter_by(id=id).first_or_404()
    return jsonify(patched_merchant.to_json())

@merchant_api.route('/api/merchant/<int:id>', methods=['DELETE'])
def delete_one_merchant(id):
    merchant_to_delete = Merchant.query.filter_by(id=id).first()
    if merchant_to_delete:
        db.session.delete(merchant_to_delete)
        db.session.commit()
    return '', 204
