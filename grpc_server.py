import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pb'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'server/grpc/api'))

import grpc
from concurrent import futures
import time
import api_pb2_grpc
import asyncio
from app.database.DBConnections import DBConnection
import api_grpc

# Jadikan serve() sebagai async
async def serve():
    # Membuat server gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    DBConnection.connect_postgresql()
    DBConnection.connect_mongo()
    DBConnection.connect_redis()
    
    # Menambahkan servis ke server
    api_pb2_grpc.add_ApiServiceServicer_to_server(api_grpc.ApiService(), server)
    
    # Menentukan port server gRPC
    server.add_insecure_port('38.47.176.189:50052')
    
    print("Server gRPC berjalan di port 50052...")
    
    # Mulai server
    server.start()
    
    # Tunggu hingga server dihentikan
    await asyncio.Event().wait()  # Tunggu sampai dihentikan (dengan signal)
    
    DBConnection.close_all()
    print("Server dihentikan")
    
    try:
        while True:
            time.sleep(86400)  # Menjaga server tetap berjalan
    except KeyboardInterrupt:
        server.stop(0)
        
    DBConnection.close_all()

# Jalankan fungsi async menggunakan event loop
if __name__ == '__main__': 
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(serve())  # Pastikan serve() dipanggil dengan run_until_complete
