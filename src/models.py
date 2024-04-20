# src/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Citizen(Base):
    __tablename__ = 'citizens'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    address = Column(String(255))

    def __repr__(self):
        return f"<Citizen(id={self.id}, name={self.name}, age={self.age}, address={self.address})>"
