import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pb'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'server/grpc/api'))

import grpc
from concurrent import futures
import time
import api_pb2_grpc
from app.database.DBConnections import DBConnection
import api_grpc

def serve():
    # Membuat server gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    DBConnection.connect_postgresql()
    DBConnection.connect_mongo()
    DBConnection.connect_redis()
    
    # Menambahkan servis ke server
    api_pb2_grpc.add_ApiServiceServicer_to_server(api_grpc.ApiService(), server)
    
    # Menentukan port server gRPC
    server.add_insecure_port('[::]:50051')
    
    print("Server gRPC berjalan di port 50051...")
    server.start()
    
    
    try:
        while True:
            time.sleep(86400)  # Menjaga server tetap berjalan
    except KeyboardInterrupt:
        server.stop(0)
        
    DBConnection.close_all()
        

if __name__ == '__main__':
    serve()
