from uuid import uuid4
from database import db
from sqlalchemy.orm import backref


class Post(db.Model):
    __tablename__ = 'posts'

    # Foreign Key
    type_id = db.Column(db.Integer, db.ForeignKey('type_of_garbage.id'))
    type_of_garbage = db.relationship("TypeOfGarbage", backref=backref("type_of_garbage", uselist=False))

    garbage_id = db.Column(db.Integer, db.ForeignKey('garbage.id'))
    garbage = db.relationship("Garbage", backref=backref("garbage", uselist=False))

    comments = db.relationship(
        "Comments", backref=backref("comments", uselist=True)
    )

    # Columns
    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True)

    def serialize(self):
        return {
                'id': self.id,
                'name': self.name,
                'garbage': self.garbage.serialize(),
                'type_of_garbage': self.type_of_garbage.serialize(),
                'description': self.description,
                'comments': [comments.serialize() for comments in self.comments],
                'active': self.active
                }
