from flask import Blueprint, request, jsonify
from storeback.models import db
from storeback.models.users import User, Inventory

user_api = Blueprint('user_api', __name__)

@user_api.route('/api/user', methods=['GET'])
def get_all_users():
    params = request.args
    users = User.query.filter_by(**params).all()
    return jsonify([user.to_json() for user in users])

@user_api.route('/api/user/<int:id>', methods=['GET'])
def get_one_user(id):
    user = User.query.filter_by(id=id).first_or_404()
    return jsonify(user.to_json())

@user_api.route('/api/user/<int:id>/cart', methods=['GET'])
def get_carted_items(id):
    user = User.query.filter_by(id=id).first_or_404()
    return jsonify(user.to_json()['carted'])

@user_api.route('/api/user', methods=['POST'])
def create_one_user():
    if not request.json:
        return 'Please include a valid JSON body with your request', 400
    user = User()
    user.firstname = request.json['firstname']
    user.lastname = request.json['lastname']
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

@user_api.route('/api/user/<int:id>', methods=['DELETE'])
def delete_one_user(id):
    user_to_delete = User.query.filter_by(id=id).first_or_404()
    db.session.delete(user_to_delete)
    db.session.commit()
    return '', 204
