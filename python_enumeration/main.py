from enum import Enum
from fastapi import FastAPI

class Fruits(str, Enum):
    orange = 'orange'
    apple = 'apple'
    grape = 'grapes'

app = FastAPI()

@app.get("/fruits/{fruits_name}")
def get_fruit(fruits_name: Fruits):
    if fruits_name == fruits_name.orange:
        return {"fruit_name_matched": fruits_name}
    if fruits_name.value == 'apple':
        return {"fruit_name_matched": fruits_name}
    return {"fruits_name": fruits_name}