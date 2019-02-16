from .store_helper import StoreHelper
from ..product.models import Product

class ProductManager ():
    def __init__(self, Session):
        self.Session = Session
        self.storeHelper = StoreHelper(Session)

    def add_product(self, product):
        return self.storeHelper.add_item(product)

    def get_all_products(self):
        session = self.Session()
        products = session.query(Product).all()
        session.close()
        return products
