from fastapi import FastAPI,status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

items = { 1: "Item 1" , 2: "Item 2" , 3:"Item 3"}

@app.delete("/item/{item_id}")
def delete_item(item_id :int):
    if item_id in items:
        del items[item_id]
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=404 ,detail="Item não encontado")
