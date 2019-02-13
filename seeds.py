from app.store import store
from app.user.models import User
from app import app

DEFAULT_ADMIN_USERNAME = app.config['DEFAULT_ADMIN_USERNAME']
DEFAULT_ADMIN_PASS = app.config['DEFAULT_ADMIN_PASS']

default_admin = {
    'username': DEFAULT_ADMIN_USERNAME,
    'password': DEFAULT_ADMIN_PASS,
    'role': 'admin'
}

def create_all ():
    print('Setting up the database tables')
    store.init_db()

def add_default_admin ():
    print('Adding the default admin')
    user = User(default_admin)
    try:
        store.add_user(user)
    except Exception as e:
        print('User already created')

create_all()
add_default_admin()
