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
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
students = []

class student(BaseModel):
  name:str
  roll_number:int
  marks:int

@app.post("/add_student")
def add_student(student:student):
students.append(student)
return {"message":"student added successfully","student":student}


@app.get("/search_student/{roll_number}")
def search_student_by_roll_number(roll_number:int):
for student in students:
   if student.roll_number==roll_number:
   return {"message":"student searched successfully","student":student}
return {"error_message":"student not found"}


@app.put("/update_student_marks/{roll_number}")
def update_students_marks (roll_number:int,marks:int):
for student in students:
  if student.roll_number==roll_number:
  student.marks=marks:
  return {"message":"student marks updated","student":student}
return {"error_message": "student not found"}


@app.delete("/delete_student_record/{roll_number}")
def remove_student_record(roll_number:int):
for student in students:
  if student.roll_number==roll_number:
    students.remove(student)
    return{"message":"student_record_deleted","student":student}

return {"error_message": "student not found"}