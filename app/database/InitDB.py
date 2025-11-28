import psycopg2
from psycopg2 import OperationalError

class PostgreSQLConnection:
    _connection = None

    @classmethod
    def connect(cls):
        if cls._connection is None:
            try:
                # Koneksi ke PostgreSQL
                cls._connection = psycopg2.connect(
                    host="38.47.176.189",      # Alamat host PostgreSQL
                    user="myuser",       # Username untuk login ke PostgreSQL
                    password="mypassword",   # Password untuk user
                    dbname="mydb",  # Nama database yang akan digunakan
                    port=5432              # Port PostgreSQL (default 5432)
                )
                print("Connected to PostgreSQL!")
            except OperationalError as e:
                print(f"Error connecting to PostgreSQL: {e}")
                raise
        return cls._connection
    
    @classmethod
    def close(cls):
        if cls._connection:
            cls._connection.close()
            cls._connection = None
            print("PostgreSQL connection closed.")