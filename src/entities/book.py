from pydantic import BaseModel 
from datetime import datetime
from enum.genreEnum import Genre

class Book(BaseModel):
    id: int
    author: str
    publishDate: datetime
    price: int
    genre: Genre

    
     