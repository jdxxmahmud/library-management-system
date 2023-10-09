from datetime import datetime
from pydantic import basemodel
from ..enums.genderEnum import GenderEnum

class Authors(basemodel):
    id: int
    first_name: str
    last_name: str
    gender: GenderEnum
    date_of_birth: datetime = ""
    biography: str = ""
    country: str = ""

