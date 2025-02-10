from fastapi  import FastAPI
from typing import Optional

app = FastAPI()

students={
    1:{
        "name":"john",
        "age":17,
        "class":"year 12"
    }

}

@app.get("/")

def index():
    return {"message": "Hello World"}


@app.get("/get_student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

@app.get("/get-by-name")
def get_student(*,name: Optional[str]=None, test : int):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not found"}