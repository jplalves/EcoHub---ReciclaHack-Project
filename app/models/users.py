from database import db
from uuid import uuid4
from werkzeug.security import check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    # Columns
    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=True)
    name = db.Column(db.String(128), nullable=True)
    cep = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(128), nullable=True)
    complement = db.Column(db.String(128), nullable=True)
    cpf_or_cnpj = db.Column(db.String(20), nullable=True)
    birth_date = db.Column(db.Date(), nullable=True)
    active = db.Column(db.Boolean(), default=True)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def serialize(self):
        return {
                'id': self.id,
                'name': self.name,
                'email': self.email,
                'address': self.address,
                'complement': self.complement,
                'cpf': self.cpf,
                'birth_date': self.birth_date,
                'cep': self.cep,
                'active': self.active
                }
