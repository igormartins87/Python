from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item (BaseModel):
    nome  : str
    preco : float
    promocao : bool = None

@app.post("/items/")
def create_item (item : Item):
    return item

# Sempre declare modelos para dados complexos.

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return{"item_id": item_id , "item": item}
