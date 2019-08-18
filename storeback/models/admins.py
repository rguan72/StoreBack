from datetime import datetime
from . import db
from .merchants import Merchant
from .keys import Key


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.Unicode(128))
    merchants = db.relationship('Merchant', backref='admin', lazy=True)
    keys = db.relationship('Key', backref='admin', lazy=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_json(self):
        res = {}
        for field in ('id', 'firstname', 'lastname', 'email', 'created', 'updated'):
            res[field] = getattr(self, field)
        res['merchants'] = [merchant.to_json() for merchant in self.merchants]
        return res

    def __repr__(self):
        return f'Admin {self.firstname} {self.lastname}'