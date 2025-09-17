from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from datetime import date
import uuid

app = FastAPI()

class Item(BaseModel):
    nome: str = Field(..., max_length=25)
    valor: float
    data: date

    # valida se a data não é maior que hoje
    @field_validator("data")
    def validar_data(cls, v):
        if v > date.today():
            raise ValueError("A data não pode ser superior à data atual")
        return v

@app.post("/items/")
def criar_item(item: Item):
    # gera um UUID e retorna junto ao objeto validado
    return {
        **item.dict(),
        "uuid": str(uuid.uuid4())
    }
