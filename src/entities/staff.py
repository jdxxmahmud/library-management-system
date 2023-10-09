from pydantic import BaseModel

class Staffs(BaseModel):
    id: int
    name: str
    address: str
    phone: str
    email: str