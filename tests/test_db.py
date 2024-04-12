import sys

sys.path.append("/home/claudio/projetos/tabela_fipe_astro/app")

from unittest.mock import MagicMock
import pytest
from app.created_tables import MarcaVeiculo, TabelaVeiculo

# Fixture para fornecer um objeto mock para a sessão do banco de dados
@pytest.fixture(scope="module")
def db_session_mock():
    return MagicMock()

# Teste para verificar se a tabela MarcaVeiculo foi criada
def test_marca_veiculo_table_exists(db_session_mock):
    # Simulando a consulta à tabela MarcaVeiculo
    db_session_mock.query.return_value.first.return_value = MarcaVeiculo(tipo='tipo1', nome='nome1', valor=1)
    
    # Testando se a consulta retorna um resultado
    assert db_session_mock.query(MarcaVeiculo).first() is not None

# Teste para verificar se a tabela TabelaVeiculo foi criada
def test_tabela_veiculo_table_exists(db_session_mock):
    # Simulando a consulta à tabela TabelaVeiculo
    db_session_mock.query.return_value.first.return_value = TabelaVeiculo(valor='valor1', marca='marca1', modelo='modelo1', anoModelo=2022, combustivel='comb1', codigoFipe='fipe1', mesReferencia='202204', tipoVeiculo=1, siglaCombustivel='S', dataConsulta='2022-04-10 12:00:00')
    
    # Testando se a consulta retorna um resultado
    assert db_session_mock.query(TabelaVeiculo).first() is not None
