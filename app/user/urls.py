from flask import Blueprint
from .views import UserController

user = Blueprint('user', __name__)

user.add_url_rule('/', view_func=UserController.add_user, methods=['POST'])
user.add_url_rule('/auth', view_func=UserController.authenticate, methods=['POST'])
