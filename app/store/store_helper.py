from sqlalchemy.exc import IntegrityError
from ..shared.exceptions import DuplicationError

class StoreHelper ():
    def __init__ (self, Session):
        self.Session = Session

    def add_item (self, item):
        session = self.Session()
        try:
            session.add(item)
            session.commit()
            session.refresh(item)
        except IntegrityError as e:
            session.rollback()
            raise DuplicationError(f'{item.__class__.__name__} already exists')
        finally:
            session.close()
        return item
