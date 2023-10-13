from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from staff_model import Staff
from student_model import Student


class Orders(Base):
    
    __tablename__ = "orders"    

    id = Column(Integer, primary_key = True)
    studentID = Column(Student)
    orderDate = Column(DateTime)
    returnDate = Column(DateTime)
    staffId = Column(Staff)
     