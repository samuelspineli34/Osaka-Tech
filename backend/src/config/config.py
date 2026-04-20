import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Para dados NÃO sensíveis, podemos deixar um padrão (default)
    ENV = os.getenv('FLASK_ENV', 'development')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_USER = os.getenv('DB_USER', 'postgres')
    
    # Para SENHAS, nunca deixe um valor padrão no código.
    # Se não estiver no .env, DB_PASSWORD será None.
    DB_PASSWORD = os.getenv('DB_PASSWORD') 

    # O nome do banco também deve vir preferencialmente do .env
    # Mas podemos manter essa lógica de troca automática se quiser.
    if ENV == 'production':
        DB_NAME = 'servicedeskdb_prod'
    else:
        DB_NAME = os.getenv('DB_NAME', 'servicedeskdb_dev')

    @classmethod
    def get_db_config(cls):
        # Validação simples: se não houver senha, avisa no console
        if not cls.DB_PASSWORD:
            print("ATENCAO: DB_PASSWORD nao encontrada no arquivo .env")

        return {
            "host": cls.DB_HOST,
            "port": cls.DB_PORT,
            "user": cls.DB_USER,
            "password": cls.DB_PASSWORD,
            "database": cls.DB_NAME
        }