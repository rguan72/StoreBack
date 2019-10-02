from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256
from . import db


class Key(db.Model):
    __tablename__ = 'api_key'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Unicode(128), nullable=False)
    key_code = db.Column(db.String(255), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def to_json(self):
        res = {}
        for field in ('id', 'value', 'key_code', 'created', 'updated'):
            res[field] = getattr(self, field)
        res['admin'] = self.admin.to_json()
        return res

    def __repr__(self):
        f'API key with value {self.value}'
        