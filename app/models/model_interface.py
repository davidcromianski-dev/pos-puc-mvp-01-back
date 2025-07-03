from sqlalchemy import Column
from abc import abstractmethod
from .. import db

class ModelInterface(db.Model):
    __abstract__ = True
    
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(db.Integer, primary_key=True)
    
    @abstractmethod
    def __repr__(self):
        pass
    
    @abstractmethod
    def to_dict(self):
        pass