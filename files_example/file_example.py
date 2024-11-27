from fastapi import FastAPI, File, UploadFile
app = FastAPI()

@app.get("/")
def welcome_mssg():
    return {"Welcome to file tutorial messages"}

@app.post("/file")
def create_file(file: bytes=File(...),):#this will work for short files (...three dots represnts required field)
    return {"file size": len(file)}

@app.post("upload_file")
def upload_file(file:UploadFile):#this will work for large file
    return {"filename":file.filename}