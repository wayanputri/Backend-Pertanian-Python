import grpc
# from concurrent import futures
# import time

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pb'))
import api_pb2
import api_pb2_grpc


# Implementasi kelas untuk service gRPC
class ApiService(api_pb2_grpc.ApiServiceServicer):
    def GetUser(self, request, context):
        # Simulasikan pengambilan data pengguna berdasarkan ID
        user_data = {
            1: {"name": "John Doe", "age": 30},
            2: {"name": "Jane Smith", "age": 25},
        }
        
        user_id = request.id
        if user_id in user_data:
            user = user_data[user_id]
            return api_pb2.UserResponse(name=user["name"], age=user["age"])
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"User with ID {user_id} not found.")
            return api_pb2.UserResponse()