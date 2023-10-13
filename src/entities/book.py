from pydantic import BaseModel 
from datetime import datetime

class Book(BaseModel):
    id: int
    author: str
    publishDate: datetime
    price: int
    genre: str

    
     