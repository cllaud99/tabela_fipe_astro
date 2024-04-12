import pandera as pa
from pydantic import BaseModel, PositiveInt


class modelo_veiculos(BaseModel):
    nome: str
    valor: PositiveInt
