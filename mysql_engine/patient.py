from sqlalchemy import Column, Integer, String, UniqueConstraint, Date, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from mysql_engine.base import Base

class Patient(Base):
    """An orm representation for a patient"""
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True)
    public_id = Column(String(20))
    name = Column(String(100))
    birth_date = Column(String(50))
    national_id = Column(String(100), unique=True)
    gender = Column(String(5))
    contact = Column(String(20))
    address = Column(String(50))
    hospital_id = Column(String(30))


    def update(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
                'id': self.public_id,
                'name': self.name,
                'birth_date': self.birth_date,
                'national_id': self.national_id,
                'contact': self.contact,
                'address': self.address,
                'gender': self.gender,
                }


