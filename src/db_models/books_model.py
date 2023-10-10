from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

class Books(Base):
    
    __tablename__ = 'BOOKS'
    
    id = Column(Integer, primary_key = True)
    author = Column(String)
    publishDate = Column(DateTime)
    price = Column(Integer)
    genre = Column(Integer)

