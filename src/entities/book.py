from pydantic import BaseModel 
from datetime import datetime

class Books(BaseModel):
    id: int
    author: str
    publishDate: datetime
    price: int
    genre: str

    
     