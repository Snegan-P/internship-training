from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database
tasks = []

# Pydantic model

class Task(BaseModel):
    title: str
    description: str

class TaskResponse(Task):
    id: int

# CREATE
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: Task):
    task_dict = task.dict()
    task_dict["id"] = len(tasks) + 1
    tasks.append(task_dict)
    return task_dict

# READ ALL
@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks():
    return tasks

# READ ONE
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# UPDATE
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# DELETE
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return {"message": "Task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")