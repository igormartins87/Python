from typing import Annotated, List
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Dados(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True)
    idade: int | None = Field(default=None ,index=True)
    apelido:str

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url,connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()
