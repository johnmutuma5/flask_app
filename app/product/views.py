import json
from flask import jsonify, request
from ..shared.middleware import admin_only, require_token
from ..shared.handlers import add_to_store
from ..product.models import Product
from ..store.store import store

class ProductController:

    @staticmethod
    @require_token
    @admin_only
    def add_product ():
        product = Product(json.loads(request.data))
        return add_to_store(product)

    def view_products ():
        available_products = store.get_all_products()
        products = map(lambda prod: prod.serialize(), available_products)
        return jsonify({
            'products': list(products),
            'ok': True
        })
