from sqlalchemy import Column, Integer, ForeignKey, String, UniqueConstraint, Date, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from mysql_engine.base import Base

class Patient(Base):
    """An orm representation for a patient"""
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    date_of_birth = Column(Date)
    gender = Column(String(1))
    contact = Column(String(20))
    address = Column(String(50))
    hospital_id = Column(String(30))

    #define relationship with assigned nurse
    nurse_id = Column(Integer, ForeignKey('nurse.id'))
    assigned_nurse = relationship('Nurse', back_populates='patients')


    def update(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
                'id': self.id,
                'name': self.name,
                'date_of_birth': self.date_of_birth,
                'contact': self.contact,
                'address': self.address,
                'gender': self.gender,
                }


