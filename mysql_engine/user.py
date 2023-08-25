from sqlalchemy import Column, Integer, String, UniqueConstraint, Date, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from mysql_engine.base import Base

class User(Base):
    """An orm reprsentation of a user"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    public_id = Column(String(20), unique=True)
    profile_pic = Column(String(100))
    name = Column(String(100))
    username = Column(String(50), unique=True)
    email = Column(String(70), unique=True)
    password = Column(String(50))
    position = Column(String(50))
    login_token = Column(String(20))
    created_on = Column(Date, default=datetime.utcnow, nullable=False)
    updated_on = Column(Date, default=datetime.utcnow, nullable=False)
    hospitals = relationship('Hospital', secondary='user_hospital_junction', back_populates='staff', uselist=True)


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
