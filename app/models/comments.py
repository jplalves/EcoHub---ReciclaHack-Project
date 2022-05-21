from uuid import uuid4
from database import db
from sqlalchemy.orm import backref


class Comments(db.Model):
    __tablename__ = 'comments'

    # Foreign Key
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    post = db.relationship("Post", backref=backref("posts", uselist=False))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", backref=backref("users", uselist=False))

    # Columns
    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    message = db.Column(db.String(1500), default=lambda: str(uuid4()))
    up_votes = db.Column(db.Integer, default=lambda: str(uuid4()))
    is_coop = db.Column(db.Boolean(), default=False)
    active = db.Column(db.Boolean(), default=True)

    def serialize(self):
        return {
                'id': self.id,
                'message': self.message,
                'up_votes': self.up_votes,
                'is_coop': self.is_coop,
                'user': self.user.serialize(),
                'post_id': self.post_id,
                'active': self.active
                }
