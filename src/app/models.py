from datetime import datetime
import json

from sqlalchemy import Column, Integer, String, CHAR, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import Float
Base = declarative_base()


class Serializable(object):
    """
    Allows serialization of modal
    """

    def to_dict(self):
        """
        Generate a JSON encodable dict instance
        """
        if "__serializable__" in self.__class__.__dict__:
            attrs = self.__class__.__dict__["__serializable__"]
            ret = {}
            for attr in attrs:
                value = getattr(self, attr)
                if type(value) is datetime:
                    value = value.isoformat()
                ret[attr] = value
            
            return ret
            
        return {}
        
    def to_json(self):
        serializable = self.to_dict()
        
        return json.dumps(serializable)


class Product(Serializable, Base):
    __tablename__ = "products"
    __serializable__ = ["id", "name", "kind"]
    
    id = Column(CHAR(16), primary_key=True)
    name = Column(String, nullable=False)
    kind = Column(String, nullable=False)

    pricings = relationship("Price")


class Price(Serializable, Base):

    __tablename__ = "prices"
    __serializable__ = ["id", "effective_at", "expired_at", "created_at", "value"]

    id = Column(CHAR(16), primary_key=True)
    product_id = Column(CHAR(16), ForeignKey("products.id"))
    product = relationship("Product", back_populates="pricings")

    effective_at = Column(DateTime, nullable=False)
    expired_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)

    value = Column(Float, nullable=False)


class Unit(Serializable, Base):
    __tablename__ = "units"
    __serializable__ = ["id", "name", "short_form"]
    
    id = Column(CHAR(16), primary_key=True)
    name = Column(String, nullable=False)
    short_form = Column(String, nullable=False)

    created_at = Column(DateTime, nullable=False)
    

class Scenario(Serializable, Base):
    """
    Scenarios are client specific
    Product code mentioned in scenario content is also client specific
    """
    __tablename__ = "scenarios"
    __serializable__ = ["id", "title", "description", "content"]
    
    id = Column(CHAR(16), primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    content = Column(String, nullable=False)
    
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


class Taxcode(Serializable, Base):
    """
    Taxcode to be executed per product purchased
    """
    __tablename__ = "taxcodes"
    __serializable__ = ["id", "title", "effective_at", "expired_at", "shared", "body", "created_at", "updated_at"]
    
    id = Column(CHAR(16), primary_key=True)
    title = Column(String, nullable=False)    
    effective_at = Column(DateTime, nullable=False)
    expired_at = Column(DateTime, nullable=False)
    shared = Column(Boolean, nullable=False)
    body = Column(String, nullable=False)
    
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
