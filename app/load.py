import psycopg2
from load_settings import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD
from extract import call_api
from models import modelo_veiculos
from dotenv import load_dotenv

load_dotenv()

def insert_into_postgres(data, table_name):

    """
    Insere os dados em uma tabela do banco de dados PostgreSQL.

    Args:
        data (list): Lista de objetos a serem inseridos na tabela.
        table_name (str): Nome da tabela onde os dados serão inseridos.
    """

    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = conn.cursor()

    for item in data:

        placeholders = ', '.join(['%s'] * len(item.__dict__.keys()))
        columns = ', '.join(item.__dict__.keys())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"

        cursor.execute(query, list(item.__dict__.values()))

    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    url = f"https://brasilapi.com.br/api/fipe/marcas/v1/"
    car_data = call_api(url, "carros", modelo_veiculos)
    insert_into_postgres(car_data, 'marcas_veiculos')