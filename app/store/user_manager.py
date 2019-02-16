from .store_helper import StoreHelper
from ..user.models import User
from ..shared.utils import hash_password
from ..shared.exceptions import AuthenticationError

class UserManager ():
    def __init__(self, Session):
        self.Session = Session
        self.storeHelper = StoreHelper(Session)

    def add_user(self, user):
        return self.storeHelper.add_item(user)

    def find_user(self, credentials):
        username = credentials['username']
        password = credentials['password']
        session = self.Session()
        target_user = session.query(User)\
            .filter(User.username == username)\
            .filter(User.password == hash_password(password))\
            .first()

        session.close()

        if not target_user:
            raise AuthenticationError('Invalid login credentials')

        return target_user
