from uuid import uuid4
from database import db
from sqlalchemy.orm import backref


class Comments(db.Model):
    __tablename__ = 'comments'

    # Foreign Key
    garbage_id = db.Column(db.Integer, db.ForeignKey('garbage.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    cooperative_id = db.Column(db.Integer, db.ForeignKey('cooperative.id'))
    user = db.relationship("User", backref=backref("users", uselist=False))

    comment_liked = db.relationship("CommentLikes", backref=backref("comment_likes", uselist=True))

    # Columns
    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    message = db.Column(db.String(1500), default=lambda: str(uuid4()))
    up_votes = db.Column(db.Integer)
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
