from fastapi  import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students={
    1:{
        "name":"john",
        "age":17,
        "class":"year 12"
    }

}

class Student(BaseModel):
    name:str
    age:int
    year:str

@app.get("/")

def index():
    return {"message": "Hello World"}


@app.get("/get_student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id:int, name: Optional[str]=None, test : int=None):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id:int, student:Student):
    if student_id in students:
        return {"Error":"Student exists"}
    students[student_id]=student
    return students[student_id]
