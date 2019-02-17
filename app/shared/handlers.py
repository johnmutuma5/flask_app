from flask import jsonify, request
from .exceptions import DuplicationError
from ..store.store import store

def add_to_store (item):
    item_label = item.__class__.__name__.lower()
    try:
        new_item = store.add(item)
    except DuplicationError as e:
        return jsonify({ 'ok': False, 'message': e.message }), 409
    return jsonify({ 'ok': True, item_label: new_item.serialize() }), 201
