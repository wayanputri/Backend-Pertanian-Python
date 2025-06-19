from pymongo import MongoClient

class MongoDBConnection:
    _connection = None
    _db = None

    @classmethod
    def connect(cls):
        if cls._connection is None:
            cls._connection = MongoClient("mongodb://localhost:27017/")
            cls._db = cls._connection["masa_depan"]
            print("mongo db connected")
        return cls._db

    @classmethod
    def close(cls):
        if cls._connection:
            cls._connection.close()
            cls._connection = None
            print("MongoDB connection closed.")
