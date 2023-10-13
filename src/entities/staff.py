from pydantic import BaseModel

class Staff(BaseModel):
    id: int
    name: str
    address: str
    phone: str
    email: str

    