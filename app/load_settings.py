import os
from dotenv import load_dotenv
from pathlib import Path


def load_settings():
    """Carrega as configurações de ambiente"""
    dotenv_path = Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "db_host": os.getenv("HOST"),
        "db_user": os.getenv("USER"),
        "db_pass": os.getenv("PASSWORD"),
        "db_name": os.getenv("DB")
    }

    return settings