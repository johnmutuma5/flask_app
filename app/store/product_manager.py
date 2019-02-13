from ..product.models import Product

class ProductManager ():
    def __init__(self, Session):
        self.Session = Session

    def add_product(self, product):
        session = self.Session()
        try:
            session.add(product)
            session.commit()
            session.refresh(product)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
        return product

    def get_all_products(self):
        session = self.Session()
        products = session.query(Product).all()
        session.close()
        return products
