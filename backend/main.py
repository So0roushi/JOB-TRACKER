from fastapi import FastAPI, Depends
from backend.models import Application
from backend.database import Base, engine, get_db
from sqlalchemy.orm import Session
from backend.schemas import ApplicationCreate, ApplicationRead

app = FastAPI()
Base.metadata.create_all(engine)

@app.post('/applications', response_model=ApplicationRead, status_code=201)
def create_application(body : ApplicationCreate, db: Session = Depends(get_db)):
    data = body.model_dump()
    row = Application(**data)
    db.add(row)
    db.commit()
    db.refresh(row)
    return row



@app.get('/')
async def root():
    return {"message:": "Hello World"}
