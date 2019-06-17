from . import db
import uuid


class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)

    def to_json(self):
        res = {}
        for field in ('id', 'name', 'price'):
            value = getattr(self, field)
            res[field] = value

        return res

    def __repr__(self):
        return f'Item {self.name}'
