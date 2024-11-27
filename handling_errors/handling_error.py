
# To return an http response with error to the client we use HTTPException
from fastapi import FastAPI, HTTPException

app = FastAPI()
fruits = {"orange":"sour"}

@app.get("/")
def welcome_mssg():
    return {"Handling errors tutorial"}

@app.get("/fruit/{fruit_name}")
def check_fruits(fruit_name: str):
    if fruit_name not in fruits:
        raise HTTPException(status_code=404, detail="Invalid fruit name. Please provide a  fruit name")
    return {f"Properties of {fruit_name} is: {fruits[fruit_name]}"}

# Custom Exception
