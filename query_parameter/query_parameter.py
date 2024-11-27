from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome_msg():
    return {"hello":"world"}

@app.get("/info")
def query_parameter(name: str, roll_no: int):
    return {"name":name,"roll_no":roll_no}
#http://127.0.0.1:8000/info?name=devanshu&roll_no=12

@app.get("/default_info")
#default value
def default_info(name: str = "ramu", roll_no: int=12):
    return {"name":name, "roll_no":roll_no}
#http://127.0.0.1:8000/default_info (default value will display or we can overwrite the value if it is passed in query string)

