from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

class Orders(Base):
    
    __tablename__ = "ORDERS"    

    id = Column(Integer, primary_key = True)
    studentID = Column()
    orderDate = Column(String)
    returnDate = Column(String)
    staffId = Column()
    