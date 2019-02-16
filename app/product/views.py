import json
from flask import jsonify, request
from ..store.store import store
from ..shared.middleware import admin_only, require_token
from ..shared.exceptions import DuplicationError
from ..product.models import Product

class ProductController:

    @staticmethod
    @require_token
    @admin_only
    def add_product ():
        product = Product(json.loads(request.data))
        # add product to the database
        try:
            new_product = store.add_product(product)
        except DuplicationError as e:
            return jsonify({ 'ok': False, 'message': e.message }), 409
        return jsonify({ 'ok': True, 'product': new_product.serialize() }), 201

    def view_products ():
        available_products = store.get_all_products()
        products = map(lambda prod: prod.serialize(), available_products)
        return jsonify({
            'products': list(products),
            'ok': True
        })
