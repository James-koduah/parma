import bcrypt
from flask import session
from sqlalchemy import Column, Integer, String, UniqueConstraint, Date, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from mysql_engine.base import Base
from mysql_engine.constants import USERNAME_LENGTH, EMAIL_LENGTH, PROFILE_PIC_LENGTH, PUBLIC_ID_LENGTH, PASSWORD_LENGTH, POSITION_LENGTH, LOGIN_TOKEN_LENGTH

class User(Base):
    """An orm representation of a user"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    public_id = Column(String(PUBLIC_ID_LENGTH), unique=True)
    profile_pic = Column(String(PROFILE_PIC_LENGTH))
    name = Column(String(100))
    username = Column(String(USERNAME_LENGTH), unique=True)
    email = Column(String(EMAIL_LENGTH), unique=True)
    password = Column(String(PASSWORD_LENGTH))
    login_token = Column(String(LOGIN_TOKEN_LENGTH))
    created_on = Column(Date, default=datetime.utcnow, nullable=False)
    updated_on = Column(Date, default=datetime.utcnow, nullable=False)
    hospitals = relationship('Hospital', secondary='hospital_staff', back_populates='staff', uselist=True)

    #Method to update user info all at once
    def update(self, **kwargs):
        #defining a set of allowed attribute names that can be updated
        allowed_attributes = {'public_id', 'profile_pic','name', 'username', 'email', 'password', 'login_token', 'role'}
        for attr_name, attr_value in kwargs.items():
            if attr_name in allowed_attributes:
                setattr(self, attr_name, attr_value)

    def __repr__(self):
        return f"Type: {self.__class__.__name__} ----- id: {self.id}"

    def to_dict(self):
        obj_dict = {}
        obj_dict['public_id'] = self.public_id
        obj_dict['profile_pic'] = self.profile_pic
        obj_dict['username'] = self.username
        obj_dict['position'] = self.position
        return obj_dict
    
    def authenticate_user(self, username, password):
        #fetch user by username from the database
        user = session.query(User).filter_by(username=username).first()
        if user and bcrypt.checkpw(password.encode('utf8'), user.password):
            return user
        else:
            return None
