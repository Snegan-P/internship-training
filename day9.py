from fastapi import FastAPI

app = FastAPI()


# Temporary database
students = [
    {
        "id": 1,
        "name": "Snegan",
        "department": "CSE",
        "year": 3
    }
]


# GET METHOD
# Get all students
@app.get("/students")
def get_students():
    return students



# GET METHOD with ID
# Get one student
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    return {
        "message": "Student not found"
    }



# POST METHOD
# Create new student
@app.post("/students")
def create_student(student: dict):

    students.append(student)

    return {
        "message": "Student added",
        "data": student
    }



# PUT METHOD
# Update complete student details
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: dict):

    for index, student in enumerate(students):

        if student["id"] == student_id:

            students[index] = updated_student

            return {
                "message": "Student completely updated",
                "data": updated_student
            }


    return {
        "message": "Student not found"
    }



# PATCH METHOD
# Update only specific fields
@app.patch("/students/{student_id}")
def patch_student(student_id: int, data: dict):

    for student in students:

        if student["id"] == student_id:

            student.update(data)

            return {
                "message": "Student partially updated",
                "data": student
            }


    return {
        "message": "Student not found"
    }



# DELETE METHOD
# Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return {
                "message": "Student deleted"
            }


    return {
        "message": "Student not found"
    }