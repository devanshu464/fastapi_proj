from fastapi import FastAPI

from typing import Optional

app = FastAPI()

@app.get("/")
def welcome_msg():
    return {"hello":"world"}

#below block is for multipath
@app.get("/fruit/{name}/count/{count}")
def fruit_info(name:str, count:int):
    return {"fruit_name":name, "fruit count":count}

#below block is for multipath with query parameter
@app.get("/fruit/{name}/count/{count}/")
def fruit_info(name:str, count:int, weight:int):
    return {"fruit name":name, "fruit count":count, 'fruit weight':weight}

#below bloack is for multipath with optional parameter
@app.get("/fruit/{name}/optional/{count}/")
def fruit_info(name:str, count:int, weight:Optional[int]=None):
    return {"fruit name":name, "fruit count":count, 'fruit weight':weight}

