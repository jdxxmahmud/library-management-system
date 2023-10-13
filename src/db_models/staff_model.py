from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Staffs(Base):

    __tablename__ = "staffs"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    address = Column(String)
    phone = Column(String)
    email = Column(String)