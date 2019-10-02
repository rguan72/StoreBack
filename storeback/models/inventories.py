import uuid
from datetime import datetime
from . import db


class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_json(self):
        res = {}
        for field in ('id', 'name', 'price', 'admin_id', 'created', 'updated'):
            value = getattr(self, field)
            res[field] = value

        return res

    def __repr__(self):
        return f'Item {self.name}'
