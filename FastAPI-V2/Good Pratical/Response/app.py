from fastapi import FastAPI,status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    nome:str
    descricao: Optional[str] =None
    preco: float
    oferta: Optional[bool] = False

items = {
    1: Item(nome="mouse", descricao= "mouse ergonomico" ,preco=50.20 ,oferta=False),
    2: Item(nome="cadeira", descricao= "cadeira game" ,preco=700.00 ,oferta=True),
    3: Item(nome="monitor", descricao= "monitor Game" ,preco=500.00 ,oferta=False),
}

#Create
@app.post("/items/",status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    proximo_id = max(item.keys(), default=0) + 1
    items[proximo_id] = item
    return{
        "message" : "Item adicionado com sucesso!",
        "id": proximo_id,
        **item.dict()
    }

#Read
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail=" Item não encontrado")
    return items [item_id]

#readALL
@app.get("/items/", response_model=dict[int,Item])
def list_item():
    return items

#Update
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int , item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail=" Item não encontrado")
    items [item_id] = item
    return item


@app.delete("/item/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id in items:
        raise HTTPException(status_code=404 ,detail="Item não encontado")
    del items[item_id]
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)


