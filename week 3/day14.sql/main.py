    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel

    app = FastAPI()

    # In-memory database
    tasks = []

    # Pydantic model
    class Task(BaseModel):
        id: int
        title: str
        completed: bool = False

    @app.get("/")
    def home():
        return {"message": "Hello World"}

    # CREATE
    @app.post("/tasks")
    def create_task(task: Task):
        tasks.append(task)
        return task

    # READ ALL
    @app.get("/tasks")
    def get_tasks():
        return tasks

    # READ ONE
    @app.get("/tasks/{task_id}")
    def get_task(task_id: int):
        for task in tasks:
            if task.id == task_id:
                return task
        raise HTTPException(status_code=404, detail="Task not found")

    # UPDATE
    @app.put("/tasks/{task_id}")
    def update_task(task_id: int, updated_task: Task):
        for index, task in enumerate(tasks):
            if task.id == task_id:
                tasks[index] = updated_task
                return updated_task
        raise HTTPException(status_code=404, detail="Task not found")

    # DELETE
    @app.delete("/tasks/{task_id}")
    def delete_task(task_id: int):
        for index, task in enumerate(tasks):
            if task.id == task_id:
                tasks.pop(index)
                return {"message": "Deleted"}
        raise HTTPException(status_code=404, detail="Task not found")