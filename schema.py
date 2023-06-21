
from pydantic import BaseModel


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Jerzetta",
                "last_name": "Kłosińska",
            }
        }

class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
	
    class Config:
        orm_mode = True	

class StudentUpdateSchema(BaseModel):
    id: int
    first_name: str
    last_name: str