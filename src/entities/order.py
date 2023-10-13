from pydantic import BaseModel
from datetime import datetime
from student import Students
from staff import Staffs

class Orders(BaseModel):
    id: int
    studentID: Students
    orderDate: datetime
    returnDate: datetime
    staffId: Staffs






