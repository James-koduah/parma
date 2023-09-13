from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from mysql_engine.base import Base
from mysql_engine.doctor import Doctor

class Appointment(Base):
    """An ORM representation for appointments in the hospital"""
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    public_id = Column(String(20), unique=True, nullable=False)
    patient_id = Column(String(20), nullable=False)
    hospital_id = Column(String(20), nullable=False)
    appointment_time = Column(DateTime, default=datetime.utcnow, nullable=False)
    doctor_id = Column(String(20), ForeignKey('doctors.id'), nullable=False)  # Link to doctors table
    status = Column(String(20), default=None)
    description = Column(Text(), nullable=True)  # Allow for optional additional information

    # Define a relationship to the Doctor model for easy access to doctor's information
    doctor = relationship("Doctor", back_populates="appointments")

    def __init__(self, public_id, patient_id, hospital_id, appointment_time, doctor_id, description, status=None):
        self.public_id = public_id
        self.patient_id = patient_id
        self.hospital_id = hospital_id
        self.appointment_time = appointment_time
        self.doctor_id = doctor_id
        self.description = description
        self.status = 'scheduled'  # Provide a default value here

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'hospital_id': self.hospital_id,
            'appointment_time': self.appointment_time.strftime('%Y-%m-%d %H:%M:%S'),
            'doctor_id': self.doctor_id,
            'status': self.status,
            'description': self.description,
        }
