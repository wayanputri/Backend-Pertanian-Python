import redis

class RedisConnection:
    _connection = None

    @classmethod
    def connect(cls):
        if cls._connection is None:
            cls._connection = redis.StrictRedis(
                host='localhost', port=6379, db=0)
            print("redis connected")
        return cls._connection

    @classmethod
    def close(cls):
        if cls._connection:
            cls._connection.connection_pool.disconnect()
            cls._connection = None
            print("Redis connection closed.")