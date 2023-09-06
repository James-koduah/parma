from sqlalchemy import Column, Integer, String, UniqueConstraint, DateTime, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from mysql_engine.base import Base



class Appointment(Base):
    """An orm representation for appointments in the hospital"""
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    public_id = Column(String(20), unique=True)
    patient_id = Column(String(20))
    hospital_id = Column(String(20))
    created_on = Column(DateTime, default=datetime.utcnow, nullable=False)
    current_doctor_id = Column(String(20))
    status = Column(String(20))
    info = Column(Text())


    def update(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {'id': self.public_id,
                'name': self.name,
                'location': self.location,
                'about': self.about
                }


