import requests

import pandas as pd
import requests
from pydantic import BaseModel, PositiveInt, validate_call
from .models import modelo_veiculos

@validate_call()
def call_api(url, end_point, schema):
    """
    Obtém dados de carros, caminhões e motos de uma API online da tabela Fipe.
    
    Args:
        url (str): URL base da API.
        end_point (str): Endereço específico para a solicitação na API.
        schema (class): Classe de esquema para validar e preencher os dados da resposta.

    Returns:
        list: Lista de objetos do tipo especificado pelo esquema, preenchidos com os dados obtidos da API.
    """
    data = []

    url = f"{url}{end_point}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        print(url)
        data.extend(response.json())
        
    return [schema(**item) for item in data]


if __name__ == "__main__":
    url = f"https://brasilapi.com.br/api/fipe/marcas/v1/"
    car_data = call_api(url, 'carros', modelo_veiculos)
    df = pd.DataFrame(car_data)
    print(df)