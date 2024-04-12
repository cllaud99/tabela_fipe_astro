import pandera as pa
from pydantic import BaseModel, PositiveInt


class modelo_veiculos(BaseModel):
    nome: str
    valor: PositiveInt


class Veiculo(BaseModel):
    valor: str
    marca: str
    modelo: str
    anoModelo: int
    combustivel: str
    codigoFipe: str
    mesReferencia: str
    tipoVeiculo: int
    siglaCombustivel: str
    dataConsulta: str
