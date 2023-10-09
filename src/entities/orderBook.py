from pydantic import BaseModel
from book import Books
from order import Orders

class OrderBooks(BaseModel):
    id: int
    orderId: Orders
    bookId: Books


    