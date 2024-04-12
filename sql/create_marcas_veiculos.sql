CREATE TABLE marcas_veiculos (
    tipo VARCHAR(15),
    nome VARCHAR(50),
    valor INT,
    created_at TIMESTAMP DEFAULT now()
);