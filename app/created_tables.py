import os

from dotenv import load_dotenv
from sqlalchemy import TIMESTAMP, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class MarcaVeiculo(Base):
    __tablename__ = "marcas_veiculos"

    tipo = Column(String(15))
    nome = Column(String(50))
    valor = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, server_default="now()", nullable=False)


class TabelaVeiculo(Base):
    __tablename__ = "tabela_veiculos"

    id = Column(Integer, primary_key=True)
    valor = Column(String(20))
    marca = Column(String(50))
    modelo = Column(String(100))
    anoModelo = Column(Integer)
    combustivel = Column(String(20))
    codigoFipe = Column(String(20))
    mesReferencia = Column(String(20))
    tipoVeiculo = Column(Integer)
    siglaCombustivel = Column(String(5))
    dataConsulta = Column(TIMESTAMP)


# Carregue as variáveis de ambiente do arquivo .env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Crie a string de conexão
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crie o engine e a tabela
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
