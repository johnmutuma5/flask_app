from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .base import Base
from .product_manager import ProductManager
from .user_manager import UserManager
from .. import app
from ..shared.exceptions import AuthenticationError

SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']

class Store():
    def __init__(self):
        self.dbEngine = create_engine(SQLALCHEMY_DATABASE_URI)
        self.Session = scoped_session(sessionmaker(bind=self.dbEngine))
        self.userManager = UserManager(self.Session)
        self.productManager = ProductManager(self.Session)

    def init_db (self):
        Base.metadata.create_all(bind=self.dbEngine)

    def drop_db (self):
        Base.metadata.drop_all(bind=self.dbEngine)

    def add_user(self, user_data):
        return self.userManager.add_user(user_data)

    def find_user(self, credentials):
        return self.userManager.find_user(credentials)

    def add_product(self, product_data):
        return self.productManager.add_product(product_data)

    def get_all_products(self):
        return self.productManager.get_all_products()

store = Store()
