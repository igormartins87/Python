# Basico utilizando query parmatro

from fastapi import FastAPI

app =FastAPI()

@app.get("/")
def read_root():
    return{"message": "API Funcionado"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return{"item_id": item_id ,"q": q}



