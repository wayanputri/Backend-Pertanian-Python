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
                    host="localhost",      # Alamat host PostgreSQL
                    user="postgres",       # Username untuk login ke PostgreSQL
                    password="wayan123",   # Password untuk user
                    dbname="MasaDepan",  # Nama database yang akan digunakan
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