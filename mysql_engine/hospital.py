from sqlalchemy import Column, Integer, String, UniqueConstraint, Date
from datetime import datetime
from sqlalchemy.orm import relationship
from mysql_engine.base import Base


class Hospital(Base):
    """An orm representing a table"""
    __tablename__ = 'hospitals'

    id = Column(Integer, primary_key=True)
    public_id = Column(String(20), unique=True)
    name = Column(String(100))
    address = Column(String(100))
    country = Column(String(100))
    created_on = Column(Date, default=datetime.utcnow, nullable=False)
    updated_on = Column(Date, default=datetime.utcnow, nullable=False)
    staff = relationship('User', secondary='user_hospital_junction', back_populates='hospitals', uselist=True)

    def update(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {'id': self.public_id,
                'name': self.name,
                'location': self.location,
                'about': self.about
                }


