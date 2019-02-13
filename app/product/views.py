import json
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from ..store import store
from ..shared.middleware import admin_only, require_token
from ..product.models import Product

class ProductController:

    @staticmethod
    @require_token
    @admin_only
    def add_product ():
        raw_data = json.loads(request.data)
        product = Product(raw_data)
        # add product to the database
        try:
            new_product = store.add_product(product)
        except IntegrityError as e:
            return jsonify({ 'ok': False, 'message': 'Product already exists' }), 409
        return jsonify({
            'product': new_product.serialize(),
            'ok': True
        }), 201

    def view_products ():
        products_data = store.get_all_products()
        products = map(lambda prod: prod.serialize(), products_data)
        return jsonify({
            'products': list(products),
            'ok': True
        })
