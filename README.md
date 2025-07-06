"# Backend-Pertanian-Python" 

Berikut adalah kode untuk menghubungkan ESP8266 dengan sensor DHT11 dan mengirimkan data ke API.

```cpp

#include <ESP8266WiFi.h>         // Library untuk ESP8266
#include <DHT.h>                  // Library untuk sensor DHT
#include <ESP8266HTTPClient.h>    // Library untuk HTTP client

#define DHTPIN 2                 // Pin GPIO yang digunakan untuk sensor DHT11 (pin GPIO2 pada ESP8266)
#define DHTTYPE DHT11            // Jenis sensor yang digunakan (DHT11)

DHT dht(DHTPIN, DHTTYPE);       // Inisialisasi objek DHT

// WiFi credentials
const char* ssid = "Nama wifi";        // Ganti dengan SSID WiFi kamu
const char* password = "password"; // Ganti dengan password WiFi kamu

// API URL untuk mengirimkan data
const char* serverName = "http://192.168.98.76:5002/data";  // Ganti <IP_API_SERVER> dengan alamat IP server API kamu

void setup() {
  Serial.begin(115200);           // Mulai komunikasi serial
  dht.begin();                    // Inisialisasi sensor DHT

  // Hubungkan ke WiFi
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi!");
}

void loop() {
  // Membaca suhu dan kelembaban
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Mengecek apakah pembacaan sensor gagal
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Menampilkan data di Serial Monitor
  Serial.print("Suhu: ");
  Serial.print(temperature);
  Serial.print(" °C  Kelembaban: ");
  Serial.print(humidity);
  Serial.println(" %");

  // Kirimkan data ke API
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;  // Membuat objek HTTPClient

    http.begin(serverName);  // Mulai koneksi HTTP ke server
    http.addHeader("Content-Type", "application/json");  // Menambahkan header untuk JSON

    // Membuat payload JSON yang berisi data suhu dan kelembaban
    String jsonPayload = "{\"temperature\": " + String(temperature) + ", \"humidity\": " + String(humidity) + "}";

    // Mengirimkan permintaan POST dengan payload JSON
    int httpResponseCode = http.POST(jsonPayload);

    // Memeriksa respons dari server
    if (httpResponseCode > 0) {
      Serial.println("Data berhasil dikirim ke API!");
      Serial.println("HTTP Response Code: " + String(httpResponseCode));
    } else {
      Serial.println("Gagal mengirim data ke API!");
    }

    // Menutup koneksi HTTP
    http.end();
  } else {
    Serial.println("WiFi tidak terhubung!");
  }

  // Tunggu 10 detik sebelum mengirimkan data lagi
  delay(600000);
}

