from datetime import datetime
from . import db
from .inventories import Inventory

carted_items = db.Table('carted_items',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('inventory_id', db.Integer, db.ForeignKey('inventory.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    carted = db.relationship('Inventory', secondary=carted_items, lazy='subquery', backref=db.backref('inventory', lazy=True))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_json(self):
        res = {}
        for field in ('id', 'firstname', 'lastname', 'email', 'created', 'updated'):
            res[field] = getattr(self, field)
            
        return res

    def __repr__(self):
        return f'User {self.firstname} {self.lastname}'