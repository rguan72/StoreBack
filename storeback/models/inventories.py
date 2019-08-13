import uuid
from datetime import datetime
from . import db


class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchant.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_json(self):
        res = {}
        for field in ('id', 'name', 'price', 'created', 'updated'):
            value = getattr(self, field)
            res[field] = value
        res['merchant'] = self.merchant.to_json()

        return res

    def __repr__(self):
        return f'Item {self.name}'
