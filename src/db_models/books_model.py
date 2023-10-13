from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from enums.genreEnumEnum import Genre

Base = declarative_base()

class Books(Base):
    
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key = True)
    author = Column(String)
    publishDate = Column(DateTime)
    price = Column(Float)
    genre = Column(Genre)



