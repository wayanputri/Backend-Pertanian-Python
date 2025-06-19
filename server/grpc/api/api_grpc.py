import grpc
# from concurrent import futures
# import time

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pb'))
# sys.path.append(os.path.join(os.path.dirname(__file__), 'repositori'))
import api_pb2
import api_pb2_grpc

from server.grpc.repositori.User import UserQuery


class ApiService(api_pb2_grpc.ApiServiceServicer):
    def GetUser(self, request, context):
        user_query = UserQuery()
        user_data = user_query.get_data_from_postgresql()
        print("user", user_data)
        
        user_id = request.id
        
        # Mengubah user_data menjadi dictionary berdasarkan ID untuk pencocokan lebih mudah
        user_dict = {user[0]: user for user in user_data}  # user[0] adalah ID, user[1:] adalah data pengguna
        
        if user_id in user_dict:
            user = user_dict[user_id]  # Ambil data pengguna berdasarkan ID
            print("user result", user)
            return api_pb2.UserResponse(name=user[1], email=user[2],role=user[3],password=user[4])  # Ambil nama dan role dari data pengguna
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"User with ID {user_id} not found.")
            return api_pb2.UserResponse()  # Kembalikan response kosong
        