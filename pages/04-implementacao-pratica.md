---
layout: section
---

# 💻 Implementação Prática

ESP32 + MQTT na Indústria

---
layout: default
---

# 🛠️ Setup do Ambiente

## Ferramentas Necessárias

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### 📱 **Hardware**
- ESP32 DevKit
- Sensor DHT22 (temperatura/umidade)
- Resistor 10kΩ
- Protoboard e jumpers
- Fonte 5V (opcional)

### 💻 **Software**
- Arduino IDE ou PlatformIO
- Mosquitto Broker
- MQTT Explorer
- Biblioteca PubSubClient

</div>

<div>

### 🔧 **Instalação Mosquitto**

**Linux/Ubuntu:**
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl start mosquitto
sudo systemctl enable mosquitto
```

**Windows:**
```bash
# Download do site oficial
# Instalar como serviço
net start mosquitto
```

**Docker:**
```bash
docker run -it -p 1883:1883 eclipse-mosquitto
```

</div>

</div>

---
layout: default
---

# 🔌 Esquema de Ligação

<div class="flex justify-center mt-6">

```
ESP32 DevKit        DHT22
    ┌─────────┐      ┌─────┐
    │  3.3V   ├──────┤ VCC │
    │  GND    ├──────┤ GND │
    │  GPIO4  ├──────┤ DATA│
    │         │      └─────┘
    │  GPIO2  ├─── LED Status
    └─────────┘
```

</div>

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

### 🎯 **Pinout ESP32**
- **GPIO4**: Sensor DHT22
- **GPIO2**: LED status (built-in)
- **3.3V**: Alimentação sensor
- **GND**: Terra comum

</div>

<div>

### 📡 **Funcionalidades**
- Leitura de temperatura/umidade
- Publicação via MQTT
- LED indica status de conexão
- Reconexão automática Wi-Fi/MQTT

</div>

</div>

---
layout: default
---

# 📝 Código ESP32 - Configuração

```cpp {1-25|26-45|46-60}
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <ArduinoJson.h>

// Configurações Wi-Fi
const char* ssid = "SUA_REDE_WIFI";
const char* password = "SUA_SENHA_WIFI";

// Configurações MQTT
const char* mqtt_server = "192.168.1.100";  // IP do broker
const int mqtt_port = 1883;
const char* mqtt_user = "factory_user";
const char* mqtt_pass = "factory_pass";
const char* client_id = "esp32_sensor_001";

// Tópicos MQTT
const char* topic_temp = "factory/line1/temperature";
const char* topic_hum = "factory/line1/humidity";
const char* topic_status = "factory/line1/status";

// Configurações do sensor
#define DHT_PIN 4
#define DHT_TYPE DHT22
#define LED_PIN 2

// Objetos
WiFiClient espClient;
PubSubClient client(espClient);
DHT dht(DHT_PIN, DHT_TYPE);

// Variáveis de controle
unsigned long lastMsg = 0;
const long interval = 30000;  // 30 segundos
float temperature, humidity;
bool sensor_error = false;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  
  // Inicializar sensor
  dht.begin();
  
  // Conectar Wi-Fi
  setup_wifi();
  
  // Configurar MQTT
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
  
  Serial.println("Sistema inicializado!");
}

void setup_wifi() {
  delay(10);
  Serial.print("Conectando ao Wi-Fi: ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    digitalWrite(LED_PIN, !digitalRead(LED_PIN)); // Pisca LED
  }
  
  digitalWrite(LED_PIN, HIGH); // LED ligado = conectado
  Serial.println("\nWi-Fi conectado!");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}
```

---
layout: default
---

# 📝 Código ESP32 - MQTT e Loop

```cpp {1-30|31-60|61-85}
void callback(char* topic, byte* payload, unsigned int length) {
  String message;
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  
  Serial.print("Mensagem recebida [");
  Serial.print(topic);
  Serial.print("]: ");
  Serial.println(message);
  
  // Processar comandos remotos
  if (String(topic) == "factory/line1/command") {
    if (message == "restart") {
      ESP.restart();
    } else if (message == "status") {
      publish_status();
    }
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Tentando conexão MQTT...");
    
    if (client.connect(client_id, mqtt_user, mqtt_pass)) {
      Serial.println(" conectado!");
      
      // Subscrever a tópicos de comando
      client.subscribe("factory/line1/command");
      
      // Publicar status online
      publish_status();
      
    } else {
      Serial.print(" falhou, rc=");
      Serial.print(client.state());
      Serial.println(" tentando novamente em 5 segundos");
      
      // Piscar LED para indicar erro
      for(int i = 0; i < 10; i++) {
        digitalWrite(LED_PIN, !digitalRead(LED_PIN));
        delay(250);
      }
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  
  unsigned long now = millis();
  if (now - lastMsg > interval) {
    lastMsg = now;
    
    // Ler sensores
    read_sensors();
    
    // Publicar dados
    if (!sensor_error) {
      publish_temperature();
      publish_humidity();
    }
    
    publish_status();
  }
}

void read_sensors() {
  humidity = dht.readHumidity();
  temperature = dht.readTemperature();
  
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Erro ao ler sensor DHT!");
    sensor_error = true;
  } else {
    sensor_error = false;
    Serial.printf("Temperatura: %.2f°C, Umidade: %.2f%%\n", 
                  temperature, humidity);
  }
}

void publish_temperature() {
  StaticJsonDocument<200> doc;
  doc["value"] = temperature;
  doc["unit"] = "°C";
  doc["timestamp"] = millis();
  doc["sensor_id"] = client_id;
  
  char buffer[256];
  serializeJson(doc, buffer);
  
  client.publish(topic_temp, buffer, true); // retained = true
}

void publish_humidity() {
  StaticJsonDocument<200> doc;
  doc["value"] = humidity;
  doc["unit"] = "%";
  doc["timestamp"] = millis();
  doc["sensor_id"] = client_id;
  
  char buffer[256];
  serializeJson(doc, buffer);
  
  client.publish(topic_hum, buffer, true);
}

void publish_status() {
  StaticJsonDocument<300> doc;
  doc["status"] = sensor_error ? "error" : "online";
  doc["wifi_rssi"] = WiFi.RSSI();
  doc["free_heap"] = ESP.getFreeHeap();
  doc["uptime"] = millis();
  doc["ip"] = WiFi.localIP().toString();
  
  char buffer[350];
  serializeJson(doc, buffer);
  
  client.publish(topic_status, buffer, true);
}
```

---
layout: default
---

# 🧪 Teste do Sistema

## Comandos para Teste

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### 📡 **Publicar teste**
```bash
# Testar broker
mosquitto_pub -h localhost -t "test/topic" \
  -m "Hello MQTT"

# Simular comando
mosquitto_pub -h localhost \
  -t "factory/line1/command" -m "status"

# Simular sensor externo
mosquitto_pub -h localhost \
  -t "factory/line1/pressure" \
  -m '{"value": 2.5, "unit": "bar"}'
```

### 🎯 **Subscrever tópicos**
```bash
# Ver todos os dados da linha 1
mosquitto_sub -h localhost \
  -t "factory/line1/#"

# Ver apenas temperatura
mosquitto_sub -h localhost \
  -t "factory/line1/temperature"
```

</div>

<div>

### 📊 **Output esperado**
```json
// factory/line1/temperature
{
  "value": 23.5,
  "unit": "°C",
  "timestamp": 12345678,
  "sensor_id": "esp32_sensor_001"
}

// factory/line1/status
{
  "status": "online",
  "wifi_rssi": -45,
  "free_heap": 234567,
  "uptime": 120000,
  "ip": "192.168.1.105"
}
```

### 🔍 **Debugging**
```bash
# Ver logs do Mosquitto
tail -f /var/log/mosquitto/mosquitto.log

# Monitor de conexões
mosquitto_sub -h localhost -t '$SYS/#'
```

</div>

</div>
