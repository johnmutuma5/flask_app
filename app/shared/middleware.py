import jwt
from functools import wraps
from flask import request, jsonify
from .. import app

APP_SECRET = app.config['APP_SECRET']

def admin_only (func):
    @wraps(func)
    def wrapper (*args, **kwargs):
        token = request.headers['token']
        user = jwt.decode(token, APP_SECRET, algorithms=['HS256'])

        if not user['role'] == 'admin':
            return jsonify({
                'ok': False,
                'message': 'Please provide admin credentials'
            }), 403
        return func(*args, **kwargs)
    return wrapper


def require_token (func):
    @wraps(func)
    def wrapper (*args, **kwargs):
        try:
            token = request.headers['token']
            jwt.decode(token, APP_SECRET, algorithms=['HS256'])
        except Exception as e:
            return jsonify({
                'ok': False,
                'message': 'Please provide a valid token in request headers'
            }), 403
        return func(*args, **kwargs)
    return wrapper
