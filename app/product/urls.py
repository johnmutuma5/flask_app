from flask import Blueprint
from .views import ProductController

product = Blueprint('products', __name__)

product.add_url_rule('', view_func=ProductController.add_product, methods=['POST'])
product.add_url_rule('', view_func=ProductController.view_products)
