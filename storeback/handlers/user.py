from flask import Blueprint, request, jsonify
from storeback.models import db
from storeback.models.users import User
from storeback.models.inventories import Inventory
from storeback.utils import utils

user_api = Blueprint('user_api', __name__)

@user_api.route('/api/user', methods=['GET'])
def get_all_users():
    params = dict(request.args)
    params['admin_id'] = utils.get_admin_id_from_headers()
    users = User.query.filter_by(**params).all()
    return jsonify([user.to_json() for user in users])

@user_api.route('/api/user/<int:id>', methods=['GET'])
def get_one_user(id):
    admin_id = utils.get_admin_id_from_headers()
    user = User.query.filter_by(id=id, admin_id=admin_id).first_or_404()
    return jsonify(user.to_json())

@user_api.route('/api/user/<int:id>/cart', methods=['GET'])
def get_carted_items(id):
    user = User.query.filter_by(id=id).first_or_404()
    return jsonify([carted_item.to_json() for carted_item in user.carted])

@user_api.route('/api/user', methods=['POST'])
def create_one_user():
    if not request.json:
        return 'Please include a valid JSON body with your request', 400
    user = User()
    user.firstname = request.json['firstname']
    user.lastname = request.json['lastname']
    user.password = User.generate_hash(request.json['password'])
    user.admin_id = utils.get_admin_id_from_headers()
    user.email = request.json['email']
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_json())

@user_api.route('/api/user/<int:id>', methods=['PATCH'])
def patch_one_user(id):
    if not request.json:
        return 'Please provide a valid json body with your request', 400
    User.query.filter_by(id=id).update(request.json)
    db.session.commit()

    patched_user = User.query.filter_by(id=id).first_or_404()
    return jsonify(patched_user.to_json())

@user_api.route('/api/user/<int:id>/cart', methods=['PATCH'])
def cart_one_item(id):
    if not request.json:
        return 'Please provide a valid json body with your request', 400
    user = User.query.filter_by(id=id).first_or_404()
    item_to_cart = Inventory.query.filter_by(id=request.json['item_id']).first()
    if not item_to_cart:
        return 'Item to cart does not exist', 400
    user.carted.append(item_to_cart)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json())

@user_api.route('/api/user/<int:id>/cart', methods=['DELETE'])
def uncart_one_item(id):
    user = User.query.filter_by(id=id).first_or_404()
    item_to_cart = Inventory.query.filter_by(id=request.args['item_id']).first()
    if not item_to_cart:
        return 'Item to un cart does not exist', 400
    user.carted.remove(item_to_cart)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json())

@user_api.route('/api/user/<int:id>', methods=['DELETE'])
def delete_one_user(id):
    user_to_delete = User.query.filter_by(id=id).first_or_404()
    db.session.delete(user_to_delete)
    db.session.commit()
    return '', 204