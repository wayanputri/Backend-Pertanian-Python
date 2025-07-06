from app.database.DBConnections import DBConnection

class SensorQuery:
    def __init__(self):
        # Mendapatkan koneksi ke PostgreSQL, MongoDB, Redis
        self.db = DBConnection.connect_postgresql()
        self.dbR = DBConnection.connect_mongo()
        self.dbM = DBConnection.connect_redis()
    def insertSensorDHT11(self, value, sensor_id,nama):
    	# """Query ke PostgreSQL dan kembalikan ID yang baru dimasukkan"""
        query = """INSERT INTO sensor_readings (value, created_at, sensor_id,nama) VALUES (%s, NOW(), %s,%s) RETURNING id;"""
        cursor = self.db.cursor()
        cursor.execute(query, (value, sensor_id,nama))
        # Mendapatkan ID yang baru dimasukkan
        new_id = cursor.fetchone()[0]  # Mengambil nilai ID pertama dari hasil query
        self.db.commit()
        return new_id
    def insertSensor(self, sensor_type, location, farm_area_id):
    # """Query untuk insert data ke tabel sensors dan kembalikan id yang baru dimasukkan"""
    
         query = """
         INSERT INTO sensors (type, location, farm_area_id)
         VALUES (%s, %s, %s)
         RETURNING id;
         """
         cursor = self.db.cursor()
         cursor.execute(query, (sensor_type, location, farm_area_id))
    
        # Mendapatkan ID yang baru dimasukkan
         new_id = cursor.fetchone()[0]  # Mengambil ID pertama dari hasil query
         self.db.commit()
    
         return new_id



    # def get_data_from_mongo(self, query_filter):
    #     """Query ke MongoDB"""
    #     collection = self.dbR["masa_depan"]["masa_depan"]
    #     return collection.find(query_filter)

    # def get_data_from_redis(self, key):
    #     """Query ke Redis"""
    #     return self.dbM.get(key)
