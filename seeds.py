from app.store import store
from app.user.models import User

default_admin = {
    'username': 'admin',
    'password': 'admin_pass',
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
