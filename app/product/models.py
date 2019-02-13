from sqlalchemy import (Column, Integer, Sequence, String)
from ..store.base import Base

class Product(Base):
    __tablename__ = 'products'
    prod_id_seq = Sequence('prod_id_seq', start=1000, metadata=Base.metadata)
    # table columns
    id = Column( 'id', Integer, server_default=prod_id_seq.next_value(), primary_key=True)
    name = Column('name', String(20), unique=True, nullable=False)
    price = Column('price', String(255), nullable=False)

    def __init__ (self, raw_data):
        self.name = raw_data['name']
        self.price = raw_data['price']

    def serialize (self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }
