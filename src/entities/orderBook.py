from pydantic import BaseModel
from book import Books
from order import Orders

class OrderBook(BaseModel):
    id: int
    orderId: Orders
    bookId: Books


    