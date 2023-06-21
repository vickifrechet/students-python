from fastapi import APIRouter

from storage import get_students_storage
from schema import StudentCreateSchema, StudentUpdateSchema, Student

router = APIRouter()
STUDENTS = get_students_storage()

@router.get("/{student_id}")
async def read_item(student_id):
    return {"student_id": student_id}



@router.post("/student/")
async def create_student(student: StudentCreateSchema):
    s = Student(**student.dict(), id=1)
    get_students_storage()[s.id] = s
    return s




@router.get("/")
async def root():
    return {"message": "Hello World"}
	
@router.get("/students/all")
async def get_students():
    return [student.dict() for student in STUDENTS.values()]
	
@router.put("/students")
async def update_item(id: int, first_name: str, last_name: str):
    if student_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        student = STUDENTS[student_id]
        student.first_name = first_name
        student.last_name = last_name

    return student

@router.post("/students")
async def create_student(student: StudentCreateSchema):
    id = len(STUDENTS) + 1
    new_student = Student(**student.dict(), id=id)
    STUDENTS[id] = new_student
    return new_student