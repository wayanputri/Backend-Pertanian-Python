import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pb'))

import sys
import os
from flask import Flask, jsonify,request, send_from_directory
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
    channel = grpc.insecure_channel('38.47.176.189:50052')  # Menghubungkan ke server gRPC yang berjalan di port 50051
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
        "role": response.role,
        "email":response.email
    })

@app.route('/data', methods=['POST'])
def receive_data():
    # Dapatkan data JSON dari body request
    data = request.json
    stub = get_grpc_stub()
    suhu = data.get('temperature')  # Pastikan ini float
    kelembapan = data.get('humidity')  # Pastikan ini float
    print(suhu)
    print(kelembapan)
    
    # Pastikan data yang diterima adalah float
    if isinstance(suhu, float) and isinstance(kelembapan, float):
        request1 = api_pb2.SensorRequest(temperature=suhu, kelembapan=kelembapan)
    else:
        return jsonify({"error": "Invalid data format"}), 400
    
    # Kirimkan data ke gRPC
    try:
        response = stub.GetSensorSuhu(request1)
        return jsonify({"message": response.data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Menjalankan aplikasi Flask pada port yang sesuai
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)  # Flask berjalan di port 5002
