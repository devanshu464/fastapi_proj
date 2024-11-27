from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class FruitException(Exception):
    def __init__(self, name:str):
        self.name = name

app = FastAPI()

@app.exception_handler(FruitException)
def fruit_exception_handler(request:Request, exc:FruitException):
    return JSONResponse(
        status_code = 450,
        content = {"message":f'Fruit-{exc.name} is gone'}
    )

@app.get("/fruits/{name}")

def read_fruit(name:str):
    if name == 'Guava':
        raise FruitException(name=name)
    return {f'{name} Fruit is available'}