from flask import request, abort
from storeback.models.keys import Key
from .constants import APIKEY_HEADER, KEYCODE_HEADER

def get_admin_id_from_headers():
    api_key = request.headers[APIKEY_HEADER]
    key_code = request.headers[KEYCODE_HEADER]
    if not api_key or not key_code:
        abort(404, description="no items found")
    found_key = Key.query.filter_by(key_code=key_code).first_or_404()
    if Key.verify_hash(api_key, found_key.value):
        return found_key.admin_id
    else:
        abort(404, description="no items found")
