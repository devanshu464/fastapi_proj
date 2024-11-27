from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Fruit(BaseModel):
    name: str
    price: int

@app.get('/')
def hello():
    return {"hello:world"}

# @app.get("/next/{item_no}")
# def root_2(item_no : int):
#     return {"item no":item_no}

# @app.put("/hello") #this will show methods not allowed because put need some data to be
# #send from server
# def root_3():
#     return {"1":"2"}

#interactive API docs
@app.get("/fruit_count/{count}")
def fruit_count(count:int):
    return {"total fruit count":count}

@app.put("/fruit_count/{count}")
def fruit_count(count: int, fruit: Fruit):
    return {"fruit count":count, "fruit name":fruit.name, "price":fruit.price}

