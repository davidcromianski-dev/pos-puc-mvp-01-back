from sqlalchemy.ext.declarative import DeclarativeMeta
from abc import ABCMeta

# This was needed due to metaclasses conflicts between db.Model and ABC
class ModelMeta(DeclarativeMeta, ABCMeta):
    pass