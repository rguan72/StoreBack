from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256
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
    password = db.Column(db.Unicode(128))
    admin_id = db.Column(db.Integer)
    carted = db.relationship('Inventory', secondary=carted_items, lazy='subquery', backref=db.backref('inventory', lazy=True))
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
        for field in ('id', 'firstname', 'lastname', 'email', 'admin_id', 'created', 'updated'):
            res[field] = getattr(self, field)
        res['carted'] = [carted_item.to_json() for carted_item in self.carted]
        return res

    def __repr__(self):
        return f'User {self.firstname} {self.lastname}'