from datetime import datetime
from . import db
from .inventories import Inventory


class Merchant(db.Model):
    __tablename__ = 'merchant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    inventory = db.relationship('Inventory', backref='merchant', lazy=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_json(self):
        res = {}
        for field in ('id', 'name', 'created', 'updated'):
            res[field] = getattr(self, field)
            
        return res

    def __repr__(self):
        return f'Merchant {self.name}'
