from fastapi import FastAPI

app = FastAPI()

students = {
    1: {"name": "Snegan", "age": 21}
}

# GET
@app.get("/students")
def get_students():
    return students
...
# POST
@app.post("/students/{student_id}")
def add_student(student_id: int, name: str, age: int):
    students[student_id] = {"name": name, "age": age}
    return {"message": "Student added"}

# PUT
@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int):
    students[student_id] = {"name": name, "age": age}
    return {"message": "Student updated"}

# PATCH
@app.patch("/students/{student_id}")
def patch_student(student_id: int, age: int):
    students[student_id]["age"] = age
    return {"message": "Student patched"}

# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    del students[student_id]
    return {"message": "Student deleted"}