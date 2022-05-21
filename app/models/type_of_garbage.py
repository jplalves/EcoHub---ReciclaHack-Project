from uuid import uuid4
from database import db


class TypeOfGarbage(db.Model):
    __tablename__ = 'type_of_garbage'

    # Columns
    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    type = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.String(128), nullable=True)
    color = db.Column(db.String(128), nullable=True)
    active = db.Column(db.Boolean(), default=True)

    def serialize(self):
        return {
                'id': self.id,
                'type': self.type,
                'color': self.color,
                'active': self.active
                }
