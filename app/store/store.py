from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from . import Base
from .product_manager import ProductManager
from .user_manager import UserManager
from .. import app

SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']

class Store ():
    def __init__ (self):
        self.dbEngine = create_engine(SQLALCHEMY_DATABASE_URI)
        self.Session = scoped_session(sessionmaker(bind=self.dbEngine))
        self.userManager = UserManager(self.Session)
        self.productManager = ProductManager(self.Session)


    def add(self, item):
        section_manager = self.resolve_section_manager(item)
        return section_manager.add(item)


    def find_user(self, credentials):
        return self.userManager.find_user(credentials)

    def get_all_products(self):
        return self.productManager.get_all_products()

    def resolve_section_manager (self, item):
        item_class = item.__class__.__name__
        return {
            'User': self.userManager,
            'Product': self.productManager
        }[item_class]

    def init_db (self):
        Base.metadata.create_all(bind=self.dbEngine)

    def drop_db (self):
        Base.metadata.drop_all(bind=self.dbEngine)

store = Store()
