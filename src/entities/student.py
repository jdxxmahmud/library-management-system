from pydantic import BaseModel
from enums.genderEnum import Gender
from datetime import datetime

class Student(BaseModel):
    id: int
    name: str
    className: str
    section: str
    date_of_birth: datetime
    gender: Gender
