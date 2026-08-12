from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import model, schemas

model.Base.metadata.create_all(bind=engine)

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def calculate_flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    for ch in name1[:]:
        if ch in name2:
            name1 = name1.replace(ch, "", 1)
            name2 = name2.replace(ch, "", 1)

    count = len(name1 + name2)

    flames = list("FLAMES")

    while len(flames) > 1:
        index = (count % len(flames)) - 1

        if index >= 0:
            flames = flames[index+1:] + flames[:index]
        else:
            flames.pop()

    return {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Sister"
    }[flames[0]]


@app.post("/calculate")
def calculate(data: schemas.FlamesRequest, db: Session = Depends(get_db)):
    result = calculate_flames(data.name1, data.name2)

    record = models.FlamesResult(
        name1=data.name1,
        name2=data.name2,
        result=result
    )

    db.add(record)
    db.commit()

    return {"result": result}