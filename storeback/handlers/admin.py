from flask import Blueprint, request, jsonify
from storeback.models import db
from storeback.models.admins import Admin

admin_api = Blueprint('admin_api', __name__)

@admin_api.route('/api/admin', methods=['GET'])
def get_all_admins():
    params = request.args
    admins = Admin.query.filter_by(**params).all()
    return jsonify([admin.to_json() for admin in admins])

@admin_api.route('/api/admin/<int:id>', methods=['GET'])
def get_one_admin(id):
    admin = Admin.query.filter_by(id=id).first_or_404()
    return jsonify(admin.to_json())

@admin_api.route('/api/admin', methods=['POST'])
def create_one_admin():
    if not request.json:
        return 'Please provide a valid json body with your request', 400
    
    admin = Admin()
    admin.firstname = request.json['firstname']
    admin.lastname = request.json['lastname']
    admin.email = request.json['email']
    admin.password = request.json['password']
    db.session.add(admin)
    db.session.commit()
    return jsonify(admin.to_json())

@admin_api.route('/api/admin/<int:id>', methods=['PATCH'])
def patch_one_admin(id):
    if not request.json:
        return 'Please provide a valid json body with your request', 400
    
    Admin.query.filter_by(id=id).update(request.json)
    db.session.commit()

    patched_admin = Admin.query.filter_by(id=id).first_or_404()
    return jsonify(patched_admin.to_json())

@admin_api.route('/api/admin/<int:id>', methods=['DELETE'])
def delete_one_admin(id):
    admin_to_delete = Admin.query.filter_by(id=id).first_or_404()
    db.session.delete(admin_to_delete)
    db.session.commit()
    return '', 204