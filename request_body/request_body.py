from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class student_info(BaseModel):
    name:str
    roll_no:int
    address:Optional[str]=None
    contact:int

@app.get("/")
def welcome_mssg():
    return {"hello":"world"}

# below code is used for response body (when data sends from client to server)
@app.post("/student_info")
def student_info(s:student_info):
    return {"name":s.name, "roll no":s.roll_no, "adress":s.address, "contact":s.contact}