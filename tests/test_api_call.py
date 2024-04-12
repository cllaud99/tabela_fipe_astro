import sys

sys.path.append("/home/claudio/projetos/tabela_fipe_astro")

from unittest.mock import patch

import pytest

from app.extract import call_api
from app.models import modelo_veiculos


class MockSchema:
    def __init__(self, **kwargs):
        self.data = kwargs


@patch("app.extract.requests.get")
def test_call_api(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"make": "Toyota", "model": "Corolla", "year": 2020}
    ]

    expected_result = [MockSchema(make="Toyota", model="Corolla", year=2020)]

    result = call_api("http://example.com/", "cars", MockSchema)

    assert len(result) == len(expected_result)
    for i in range(len(result)):
        assert result[i].data == expected_result[i].data
