from flask import Blueprint, abort, jsonify

error_api = Blueprint('error_api', __name__)

@error_api.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404
