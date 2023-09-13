from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from mysql_engine.base import Base

class Doctor(Base):
    """An ORM representation for doctors in the hospital"""
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    specialization = Column(String(255), nullable=False)
    bio = Column(Text(), nullable=True)  # Allow for optional additional information

    # Define a one-to-many relationship to appointments
    appointments = relationship("Appointment", back_populates="doctor")

    def __init__(self, name, specialization, bio=None):
        self.name = name
        self.specialization = specialization
        self.bio = bio

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'specialization': self.specialization,
            'bio': self.bio,
        }
