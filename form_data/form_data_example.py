from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
def welcome_msg():
    return {"Welcome to form data tutorail"}

@app.get("/signup")
def signup_form(username: str= Form(...), phone_no: int = Form(...)):
    return {}
