from app.database.DBConnections import DBConnection

class UserQuery:
    def __init__(self):
        # Mendapatkan koneksi ke PostgreSQL, MongoDB, Redis
        self.db = DBConnection.connect_postgresql()
        self.dbR = DBConnection.connect_mongo()
        self.dbM = DBConnection.connect_redis()

    def get_data_from_postgresql(self):
        """Query ke PostgreSQL"""
        query="SELECT id, name, email, role, password FROM public.users"
        cursor = self.db.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def get_data_from_mongo(self, query_filter):
        """Query ke MongoDB"""
        collection = self.dbR["masa_depan"]["masa_depan"]
        return collection.find(query_filter)

    def get_data_from_redis(self, key):
        """Query ke Redis"""
        return self.dbM.get(key)
