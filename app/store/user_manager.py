from ..user.models import User
from ..shared.utils import hash_password

class UserManager ():
    def __init__(self, Session):
        self.Session = Session

    def add_user(self, user):
        session = self.Session()
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
        return user

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
