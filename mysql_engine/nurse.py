from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from mysql_engine.appointment import Appointment
from mysql_engine.base import Base
from mysql_engine.constants import USERNAME_LENGTH, EMAIL_LENGTH, PROFILE_PIC_LENGTH, PUBLIC_ID_LENGTH, PASSWORD_LENGTH, POSITION_LENGTH, LOGIN_TOKEN_LENGTH

class Nurse(Base):
    __tablename__ = 'nurses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    department = Column(String(100))

    #Define relationship with booked patient
    patients = relationship('Patient', back_populates ='assigned_nurse')

    # def book_patient(self, patient, doctor, appointment_time):
    #     #create new appointment for the patient
    #     appointment = Appointment(nurse=self, patient=patient,doctor=doctor, appointment_time=appointment_time)
    #     return appointment