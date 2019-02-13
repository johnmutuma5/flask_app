import os
import string
import json
import jwt
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from ..store import store
from ..shared.exceptions import AuthenticationError
from .. import app
from ..shared.middleware import admin_only, require_token
from .models import User

APP_SECRET = app.config['APP_SECRET']

class UserController:

    @staticmethod
    @require_token
    @admin_only
    def add_user ():
        raw_data = json.loads(request.data)
        user = User(raw_data)
        # add user to the database
        try:
            new_user = store.add_user(user)
        except IntegrityError as e:
            return jsonify({ 'ok': False, 'message': 'User already exists' }), 409
        return jsonify({ 'ok': True, 'user': new_user.serialize() }), 201

    @staticmethod
    def authenticate ():
        login_credentials = json.loads(request.data)
        try:
            user = store.find_user(login_credentials)
        except AuthenticationError as e:
            return jsonify({ 'ok': False,'message': e.message }), 403
        # generate JWT token
        payload = { 'username': user.username, 'role': user.role }
        token = jwt.encode(payload, APP_SECRET, algorithm='HS256')
        return jsonify({ 'token': token.decode('utf8') })
