from sqlalchemy import (Column, Integer, Sequence, String)
from sqlalchemy.ext.hybrid import hybrid_property
from ..store.base import Base
from ..shared.utils import hash_password

class User(Base):
    __tablename__ = 'users'
    user_id_seq = Sequence('user_id_seq', start=1000, metadata=Base.metadata)
    # table columns
    id = Column( 'id', Integer, server_default=user_id_seq.next_value(), primary_key=True)
    username = Column('username', String(20), unique=True, nullable=False)
    _password = Column('password', String(255), nullable=False)
    role = Column('role', String(10), nullable=True, default='regular')

    def __init__ (self, raw_data):
        self.username = raw_data['username']
        self.password = raw_data['password']
        self.role = raw_data['role']

    def serialize (self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role
        }

    @hybrid_property
    def password(self):
        passhash = self._password
        return passhash

    @password.setter
    def password(self, value):
        passhash = hash_password(value)
        self._password = passhash
