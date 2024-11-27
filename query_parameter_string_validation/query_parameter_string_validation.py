from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/fruit")
def fruits_name(fruit: Optional[str] = Query(None, min_length=2, max_length=5)):
    return {f"fruit name is :{fruit}"}