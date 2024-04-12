CREATE TABLE marcas_veiculos (
    tipo VARCHAR(15),
    nome VARCHAR(50),
    valor INT,
    created_at TIMESTAMP DEFAULT now()
);
CREATE TABLE tabela_veiculos (
    id SERIAL PRIMARY KEY,
    valor VARCHAR(20),
    marca VARCHAR(50),
    modelo VARCHAR(100),
    anoModelo INTEGER,
    combustivel VARCHAR(20),
    codigoFipe VARCHAR(20),
    mesReferencia VARCHAR(20),
    tipoVeiculo INTEGER,
    siglaCombustivel VARCHAR(5),
    dataConsulta TIMESTAMP
);