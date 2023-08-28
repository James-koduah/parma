from sqlalchemy import Column, Integer, String, UniqueConstraint, Date, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from mysql_engine.base import Base

class Invite_staff(Base):
    """A table for inviting staff"""
    __tablename__ = 'invite_staff'

    id = Column(Integer, primary_key=True)
    public_id = Column(String(30), unique=True)
    hospital_name = Column(String(100))
    hospital_id = Column(String(20))
    user_name = Column(String(100))
    user_id = Column(String(20))
    role = Column(String(30))
    description = Column(Text())
    status = Column(String(20))
    created_on = Column(Date, default=datetime.utcnow, nullable=False)



    def update(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return f"Type: {self.__class__.__name__} ----- id: {self.id}"

    def to_dict(self):
        obj_dict = {}
        obj_dict['public_id'] = self.public_id
        obj_dict['hospital_id'] = self.hospital_id
        obj_dict['user_id'] = self.user_id
        obj_dict['role'] = self.role
        obj_dict['description'] = self.description
        obj_dict['status'] = self.status
        obj_dict['created_on'] = self.created_on
        return obj_dict
