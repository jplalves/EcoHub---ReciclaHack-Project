from uuid import uuid4
from database import db
from sqlalchemy.orm import backref


class Garbage(db.Model):
    __tablename__ = 'garbage'

    # Columns
    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    type_of_garbage = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True)

    def serialize(self):
        return {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'type_of_garbage': self.type_of_garbage,
                'active': self.active
                }
