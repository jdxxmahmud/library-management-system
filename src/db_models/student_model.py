from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enums.genderEnum import Gender


class Students(Base):
    
    __tablename__ = "students"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    className = Column(String)
    section = Column(String)
    dateOfBirth = Column(DateTime)
    gender = Column(Gender)
