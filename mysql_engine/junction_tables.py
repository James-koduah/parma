from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from mysql_engine.base import Base


class Hospital_staff(Base):
    """A Junction table for Users and Hospitals"""
    __tablename__ = 'hospital_staff'

    id = Column(Integer, primary_key=True)
    public_id = Column(String(40), unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    hospital_id = Column(Integer, ForeignKey('hospitals.id'))
    user_role = Column(String(30))
    created_on = Column(Date, default=datetime.utcnow, nullable=False)


    def update(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
                "user_id": self.user_id,
                "hospital_id": self.hospital_id
                }
