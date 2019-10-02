import secrets
from flask import request, jsonify, Blueprint
from storeback.models import db
from storeback.models.keys import Key
from storeback.models.admins import Admin

key_api = Blueprint('key_api', __name__)

@key_api.route('/api/key', methods=['GET'])
def get_all_keys():
    params = request.args
    keys = Key.query.filter_by(**params).all()
    return jsonify([key.to_json() for key in keys])

@key_api.route('/api/key/<int:id>', methods=['GET'])
def get_one_key(id):
    key = Key.query.filter_by(id=id).first_or_404()
    return jsonify(key.to_json())

@key_api.route('/api/key/generate', methods=['POST'])
def create_one_key():
    if not request.json:
        return 'Please provide a valid json body with your request', 400
    admin = Admin.query.filter_by(id=request.json['admin_id']).first()
    if not admin:
        return 'No admin matches the admin_id given', 400
    key = Key()
    key.key_code = secrets.token_urlsafe(8)
    api_key = secrets.token_urlsafe(16)
    key.value = Key.generate_hash(api_key)
    key.admin_id = admin.id
    db.session.add(key)
    db.session.commit()

    res = key.to_json()
    res['value'] = api_key
    return jsonify(res)

@key_api.route('/api/key/validate', methods=['POST'])
def validate_key():
    if not request.json:
        return 'Please provide a valid json body with your request', 400
    key = Key.query.filter_by(value=request.json['value']).first()
    return jsonify({'admin_id': key.admin_id})

@key_api.route('/api/key/<int:id>', methods=['DELETE'])
def delete_one_key(id):
    key = Key.query.filter_by(id=id).first_or_404()
    return '', 204
