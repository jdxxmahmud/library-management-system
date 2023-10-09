from pydantic import BaseModel 

class Books(BaseModel):
    id: int
    author: str
    publishDate: str
    price: int
    genre: str

    
     