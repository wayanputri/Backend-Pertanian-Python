import psycopg2

def ConnectDB():
    try:
        # Menghubungkan ke database
        connection = psycopg2.connect(
            host="localhost",      # Ganti dengan host PostgreSQL kamu
            port="5432",           # Port default PostgreSQL
            dbname="MasaDepan", # Ganti dengan nama database kamu
            user="postgres",   # Ganti dengan username PostgreSQL kamu
            password="wayan123"     # Ganti dengan password PostgreSQL kamu
        )

        # Membuat cursor untuk menjalankan query
        cursor = connection.cursor()
        print("Koneksi berhasil!")
        return cursor

    except Exception as e:
        print("Gagal terhubung ke database:", e)
        return None  # Mengembalikan None jika koneksi gagal

# # Pemanggilan fungsi ConnectDB
# cursor = ConnectDB()

# # Pastikan koneksi berhasil sebelum melanjutkan
# if cursor:
#     # Lakukan operasi dengan cursor di sini, misalnya query SELECT
#     cursor.execute("SELECT id, name, email, role, password FROM public.users;")
#     result = cursor.fetchone()
#     print("PostgreSQL version:", result)

#     # Jangan lupa menutup cursor dan connection setelah selesai
#     cursor.close()
# else:
#     print("Tidak dapat melakukan operasi karena koneksi gagal.")
