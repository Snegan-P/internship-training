from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from schemas import Todo as TodoSchema
from database import SessionLocal
from model import Todo

app = FastAPI()


# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Todo
@app.post("/todos", response_model=TodoSchema)
def create(todo: TodoSchema, db: Session = Depends(get_db)):
    db_todo = Todo(**todo.dict())

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

    return db_todo