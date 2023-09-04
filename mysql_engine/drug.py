from sqlalchemy import Column, Integer, String, UniqueConstraint, Date, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from mysql_engine.base import Base

class Drug(Base):
    """An orm representation for drugs in a hospital's stock"""
    __tablename__ = "drugs"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    quanitty = Column(Integer)
    price = Column(Integer)
    info = Column(Text())
    usage = Column(Text())
    hospital_id = Column(String(30))


    def update(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
                'id': self.id,
                'name': self.name,
                'quantity': self.quantity
                }
