import os
print("coba",os.getcwd()) 
# import importlib
from app.database.InitDB import PostgreSQLConnection
from app.database.InitMongo import MongoDBConnection
from app.database.InitRedis import RedisConnection

import os
print("coba",os.getcwd()) 

class DBConnection:
    _connections = {
        "postgresql": None,
        "mongo": None,
        "redis": None
    }

    @staticmethod
    def connect_postgresql():
        """Mengembalikan koneksi PostgreSQL"""
        if DBConnection._connections["postgresql"] is None:
            # PostgreSQLConnection = importlib.import_module("app.database.InitDB.PostgreSQLConnection")
            DBConnection._connections["postgresql"] = PostgreSQLConnection.connect()
        return DBConnection._connections["postgresql"]

    @staticmethod
    def connect_mongo():
        """Mengembalikan koneksi MongoDB"""
        if DBConnection._connections["mongo"] is None:
            # MongoDBConnection = importlib.import_module("app.database.InitMongo.MongoDBConnection")
            DBConnection._connections["mongo"] = MongoDBConnection.connect()
        return DBConnection._connections["mongo"]

    @staticmethod
    def connect_redis():
        """Mengembalikan koneksi Redis"""
        if DBConnection._connections["redis"] is None:
            # RedisConnection = importlib.import_module("app.database.InitRedis.RedisConnection")
            DBConnection._connections["redis"] = RedisConnection.connect()
        return DBConnection._connections["redis"]

    @staticmethod
    def close_all():
        """Menutup semua koneksi"""
        # PostgreSQLConnection = importlib.import_module("InitDB.PostgreSQLConnection")
        # MongoDBConnection = importlib.import_module("InitMongo.MongoDBConnection")
        # RedisConnection = importlib.import_module("InitRedis.RedisConnection")

        # Menutup koneksi jika sudah dibuka
        if DBConnection._connections["postgresql"]:
            PostgreSQLConnection.close()
        if DBConnection._connections["mongo"]:
            MongoDBConnection.close()
        if DBConnection._connections["redis"]:
            RedisConnection.close()

        print("All database connections closed.")
        

