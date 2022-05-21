from uuid import uuid4
from database import db


class Comments(db.Model):
    __tablename__ = 'comments'

    # Columns
    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    message = db.Column(db.String(1500), default=lambda: str(uuid4()))
    up_votes = db.Column(db.Integer, default=lambda: str(uuid4()))
    active = db.Column(db.Boolean(), default=True)

    def serialize(self):
        return {
                'id': self.id,
                'message': self.message,
                'up_votes': self.up_votes,
                'active': self.active
                }
