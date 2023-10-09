from pydantic import BaseModel
from datetime import datetime
from student import Students
from staff import Staff


class Orders(BaseModel):
    id: int
    studentID: Students
    orderDate: str
    returnDate: str
    staffId: Staff






