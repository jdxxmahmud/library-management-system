from pydantic import BaseModel
from books import Books
from orders import Orders

class OrderBook(BaseModel):
    id: int
    orderId: Orders
    bookId: Books


    