from fastapi_pagination import LimitOffsetPage, paginate, add_pagination

from pydantic import BaseModel



from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse

from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.orm import sessionmaker, declarative_base

from datetime import date

app = FastAPI(title=" A simple pagination learning exercise",

debug=True)

add_pagination(app)

class Student(Base):

__tablename__ = "student"

id = Column(Integer, primary_key=True)

name = Column(String)

roll_number = Column(String)

class StudentOut(BaseModel):

id: int

name: str

roll_number: str

class Config:

orm_mode = True

@app.get(path="/api/students/all", name="Gets all employees", response_model=LimitOffsetPage[StudentsOut])

async def get_all_students():

conn = connect_to_db()

results = conn.query(Student).all()


return templates.TemplateResponse("index.html", {"request": request, "data": paginate(results))


add_pagination(app)