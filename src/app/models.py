from datetime import datetime
import json

from sqlalchemy import Column, Integer, String, CHAR, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
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
