from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enums.genderEnum import Gender

class Authors(Base):

    __tablename__ = "authors"

    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(Gender)
    dateOfBirth = Column(DateTime)
    biography = Column(String)
    country = Column(String)
    