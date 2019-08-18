from datetime import datetime
from . import db


class Key(db.Model):
    __tablename__ = 'api_key'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Unicode(128), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_json(self):
        res = {}
        for field in ('id', 'value', 'admin_id', 'created', 'updated'):
            res[field] = getattr(self, field)
        return res

    def __repr__(self):
        f'API key with value {self.value}'