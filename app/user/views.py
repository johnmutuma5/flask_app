import os
import string
import json
import jwt
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from .models import User
from .. import app
from ..store.store import store
from ..shared.middleware import admin_only, require_token
from ..shared.exceptions import AuthenticationError, DuplicationError
from ..shared.handlers import add_to_store

APP_SECRET = app.config['APP_SECRET']

class UserController:

    @staticmethod
    @require_token
    @admin_only
    def add_user ():
        user = User(json.loads(request.data))
        return add_to_store(user)

    @staticmethod
    def authenticate ():
        login_credentials = json.loads(request.data)
        # get the user
        try:
            user = store.find_user(login_credentials)
        except AuthenticationError as e:
            return jsonify({ 'ok': False,'message': e.message }), 403
        # generate JWT token
        payload = { 'username': user.username, 'role': user.role }
        token = jwt.encode(payload, APP_SECRET, algorithm='HS256')
        return jsonify({ 'token': token.decode('utf8') })
