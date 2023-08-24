from sqlalchemy import Column, Integer, String, UniqueConstraint, Date, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from mysql_engine.base import Base

class Admin(Base):
    """An orm reprsentation of a user"""
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(20))
    hospital_id = Column(String(20))
    created_on = Column(Date, default=datetime.utcnow, nullable=False)
    updated_on = Column(Date, default=datetime.utcnow, nullable=False)


    def update(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return f"Type: {self.__class__.__name__} ----- id: {self.id}"

    def to_dict(self):
        obj_dict = {}
        obj_dict['public_id'] = self.public_id
        obj_dict['profile_pic'] = self.profile_pic
        obj_dict['username'] = self.username
        obj_dict['position'] = self.position
        return obj_dict
