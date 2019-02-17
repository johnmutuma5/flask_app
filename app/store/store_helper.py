from sqlalchemy.exc import IntegrityError
from ..shared.exceptions import DuplicationError

class StoreHelper ():
    def __init__ (self, Session, store_section_cls):
        self.Session = Session
        self.store_section_cls = store_section_cls

    def add (self, item):
        session = self.Session()
        try:
            session.add(item)
            session.commit()
            session.refresh(item)
        except IntegrityError as e:
            session.rollback()
            raise DuplicationError(f'{self.store_section_cls} already exists')
        finally:
            session.close()
        return item
