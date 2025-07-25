import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/pokemon/{name}")
async def get_pokemon(name: str):
    try:
        response =requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        if response.status_code == 200:
            data = data.response.json()
            return {
            "name": data.get["name"] ,
            "height": data.get["height"] ,
            "weight": data.get["weight"]
            }
        else:
            raise HTTPException(
                status_code=404,
                detail="Pokemon não encontrado"
            )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal Erro : {str(e)}"
        )
