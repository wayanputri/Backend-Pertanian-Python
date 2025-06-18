from pymongo import MongoClient

def Init_mongo():
    try:
        # Menghubungkan ke MongoDB di localhost dan port default 27017
        client = MongoClient('mongodb://localhost:27017/')  # Ganti URL jika MongoDB kamu ada di server lain

        # Memilih database yang akan digunakan (jika belum ada, MongoDB akan membuatnya)
        db = client["masa_depan"]  # Ganti dengan nama database yang diinginkan

        # Memilih koleksi (collection) dalam database
        collection = db["masa_depan"]  # Ganti dengan nama koleksi yang diinginkan

        print("Koneksi ke MongoDB berhasil!")

        return db, collection

    except Exception as e:
        print(f"Gagal terhubung ke MongoDB: {e}")
        return None, None

# # Pemanggilan fungsi init_mongo
# db, collection = Init_mongo()

# # Jika koneksi berhasil, lakukan operasi pada database dan koleksi
# if db is not None and collection is not None:
#     # Menyisipkan data ke dalam koleksi
#     data = {"nama": "John Doe", "umur": 30, "kota": "Jakarta"}
#     collection.insert_one(data)

#     # Mengambil data dari koleksi
#     result = collection.find_one({"nama": "John Doe"})
#     print("Data yang diambil:", result)
