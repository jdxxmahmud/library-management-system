from pydantic import BaseModel
from enums import genderEnum




class Students(BaseModel):
    id: int
    name: str
    className: str
    section: str
    gender: Gender

    