from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return "WELCOME"

# below example is of path parameter with data types using python hints types
@app.get("/{item}")
def show_items(item:int):
    return {"items":item}

@app.get("/text/{item}")
def show_text(item:int):
    return {"items": item}
