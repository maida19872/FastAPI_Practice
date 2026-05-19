# Question 2 — Student Record System
# A school wants an API to manage student records.

# Create APIs for:
# Adding students
# Searching students by roll number	
# Updating student marks	
# Deleting student records	

# Additional Requirements:
# Store data using lists/dictionaries
# Use query parameters to filter students by class
# Validate request body using Pydantic
# Return custom error messages

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
students = []

class Student(BaseModel):
    name: str
    roll_number: int
    marks: int
    student_class: str

@router.post("/students")
def add_student(student: Student):
    students.append(student)
    return student

@router.get("/students/{roll_number}")
def search_student_by_roll_number(roll_number: int):
    for student in students:
        if student.roll_number == roll_number:
            return student
    return {"error": "Student not found"}

@router.put("/students/{roll_number}")
def update_student_marks(roll_number: int, marks: int):
    for student in students:
        if student.roll_number == roll_number:
            student.marks = marks
            return student
    return {"error": "Student not found"}

@router.delete("/students/{roll_number}")
def delete_student_record(roll_number: int):
    for student in students:
        if student.roll_number == roll_number:
            students.remove(student)
            return {"message": "Student record deleted successfully"}
    return {"error": "Student not found"}