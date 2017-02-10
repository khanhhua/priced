import os
import json

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean

DB_URL = os.getenv("DB_URL", None) or "postgresql://postgres:postgres@localhost/priced"
engine = create_engine(DB_URL, echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Serializable(object):
    """
    Allows serialization of modal
    """
    def to_dict(self):
        """
        Generate a JSON encodable dict instance
        """
        
        return {}
        
    def to_json(self):
        serializable = self.to_dict()
        
        return json.dumps(serializable)


class Product(Base, Serializable):
    __tablename__ = "products"
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    kind = Column(String, nullable=False)
