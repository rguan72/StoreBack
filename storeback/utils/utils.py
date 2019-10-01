from flask import request
from storeback.models.keys import Key
from .constants import APIKEY_HEADER

def get_admin_id_from_headers():
    api_key = request.headers[APIKEY_HEADER]
    if not api_key:
        abort(404, description="no items found")
    admin_id = Key.query.filter_by(value=api_key).first_or_404().admin_id
    return admin_id