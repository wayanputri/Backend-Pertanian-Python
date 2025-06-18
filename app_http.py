import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pb'))

import sys
import os
from flask import Flask, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import grpc
import api_pb2
import api_pb2_grpc

# Setup Flask
app = Flask(__name__)

# Tentukan URL path untuk file Swagger JSON
SWAGGER_URL = '/swagger'  # URL untuk mengakses Swagger UI
API_URL = '/pb/api.swagger.json'  # URL untuk file Swagger JSON (dari folder 'pb')

# Tentukan blueprint Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My Swagger API"
    }
)

# Daftarkan blueprint ke aplikasi Flask
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Endpoint untuk mengakses file Swagger JSON
@app.route(API_URL)
def swagger_json():
    return send_from_directory('pb', 'api.swagger.json')  # Mengakses file Swagger dari folder 'pb'

# Koneksi ke server gRPC
def get_grpc_stub():
    channel = grpc.insecure_channel('localhost:50051')  # Menghubungkan ke server gRPC yang berjalan di port 50051
    stub = api_pb2_grpc.ApiServiceStub(channel)
    return stub

# Endpoint HTTP untuk mengambil user berdasarkan id
@app.route('/api/user/<int:id>', methods=['GET'])
def get_user(id):
    # Menghubungi server gRPC untuk mendapatkan data pengguna
    stub = get_grpc_stub()
    request = api_pb2.UserRequest(id=id)
    response = stub.GetUser(request)

    # Mengembalikan data dalam format JSON
    return jsonify({
        "name": response.name,
        "age": response.age
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Menjalankan server Flask di port 5000
