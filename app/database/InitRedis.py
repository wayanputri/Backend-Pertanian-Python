import redis

def Init_redis():
    try:
        # Menghubungkan ke server Redis (localhost dengan port default 6379)
        r = redis.StrictRedis(
            host='localhost',   # Ganti dengan host Redis kamu (misalnya, IP server Redis)
            port=6379,          # Port default Redis
            db=0,               # Pilih database Redis (defaultnya 0)
            decode_responses=True  # Agar Redis mengembalikan string (bukan byte)
        )

        # Cek apakah Redis dapat terhubung dengan benar
        if r.ping():
            print("Koneksi ke Redis berhasil!")
        return r

    except Exception as e:
        print(f"Gagal menghubungkan ke Redis: {e}")
        return None

# Memanggil fungsi untuk inisialisasi Redis
# redis_client = Init_redis()

# # Jika koneksi berhasil, kamu bisa melakukan operasi dengan Redis
# if redis_client:
#     # Menyimpan data ke Redis
#     redis_client.set('my_key1', 'Hello, Wayan Aja')
    
#     # Mengambil data dari Redis
#     value = redis_client.get('my_key')
#     print(f"Nilai dari 'my_key' di Redis: {value}")
