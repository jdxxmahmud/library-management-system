from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = 'M'
    female = 'F'

class Students(BaseModel):
    id: int
    name: str
    className: str
    section: str
    gender: Gender

    