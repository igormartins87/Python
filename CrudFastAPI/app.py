from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    nome: str
    descricao: str = None
    preco: float
    avaliacao: bool = True

items = {}

@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, "item": item.dict()}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items.get(item_id)
    if item:
        return {"item": item.dict()}
    return {"error": "Item não encontrado"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in items:
        items[item_id] = item
        return {"mensage": "Item alterado com sucesso", "item": item.dict()}
    return {"error": "Item não encontrado"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"mensage": "Item deletado com sucesso"}
    return{"error": "Item não encontrado"}








