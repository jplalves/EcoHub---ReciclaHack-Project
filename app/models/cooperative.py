from database import db
from app.models.users import User
from sqlalchemy.orm import backref


class Cooperative(User):
    __tablename__ = 'cooperative'

    # Foreign Key
    type_of_garbage_accepted = db.relationship(
        "TypeOfGarbage", backref=backref("type_of_garbage", uselist=True)
    )
    preferencial_garbage = db.relationship(
        "Garbage", backref=backref("garbage", uselist=True)
    )

    def serialize(self):
        return {
                'id': self.id,
                'name': self.name,
                'email': self.email,
                'address': self.address,
                'complement': self.complement,
                'cpf': self.cpf,
                'birth_date': self.birth_date,
                'type_of_garbage_accepted': self.type_of_garbage_accepted,
                'preferencial_garbage': self.preferencial_garbage,
                'cep': self.cep,
                'active': self.active,
                }

