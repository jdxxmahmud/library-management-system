from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from order_model import Orders
from books_model import Books

class OrderBook(Base):
    
    __tablename__ = "order_book"

    id = Column(Integer, primary_key = True)
    orderID = Column(Orders)
    bookId = Column(Books)
    