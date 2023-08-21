from sqlalchemy import Column, Integer, String, UniqueConstraint, Date
from datetime import datetime
from sqlalchemy.orm import relationship
from mysql_engine.base import Base


class Hospital(Base):
    """An orm representing a table"""
    __tablename__ = 'hospitals'

    id = Column(Integer, primary_key=True)
    public_id = Column(String(20), unique=True)
    name = Column(String(100))
    address = Column(String(100))
    country = Column(String(100))
    staff = Column(Integer)

    def update(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {'id': self.public_id,
                'name': self.name,
                'location': self.location,
                'about': self.about
                }


