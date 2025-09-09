---
layout: section
---

# 💻 Implementação Prática

ESP32 + MQTT na Indústria


---
layout: default
---

# 🔌 Esquema de Ligação

<div class="flex justify-center mt-6">

```
                    ESP32 DevKit
                   ┌─────────────┐
                   │             │
    AHT10          │             │
   ┌─────┐         │             │
   │ VCC │─────────│ 3.3V        │
   │ GND │─────────│ GND         │
   │ SDA │─────────│ GPIO 21     │
   │ SCL │─────────│ GPIO 22     │
   └─────┘         │             │
                   │             │
     LED           │             │
   ┌─────┐         │             │
   │  +  │─────────│ GPIO 2      │
   │  -  │────┐    │             │
   └─────┘    │    └─────────────┘
              │
           220Ω Resistor
              │
              GND
```
</div>


---
layout: default
---

# ➕ Instalar Bibliotecas:

### Arduino IDE (Library Manager)
1. Buscar e instalar:
   - "ArduinoJson" — Autor: Benoit Blanchon
   - "PubSubClient" — Autor: Nick O'Leary

<div class="mt-4">
<video 
  autoplay 
  loop
  muted 
  controls 
   class="w-120 rounded-lg shadow-lg mx-auto" 
  >
>
  <source src="/videos/add-libs.mp4" type="video/mp4">
  Seu navegador não suporta vídeos.
</video>
</div>






---
layout: default
---

<style>
pre, code {
  white-space: pre-wrap !important;
  word-break: break-word !important;
  overflow-wrap: anywhere !important;
}
.slide { overflow-x: hidden !important; }
</style>

# 📝 Código ESP32 - Configuração

```cpp {1-4|5-9|10-14|15-16|17-22}
#include <WiFi.h>                 // Biblioteca para Wi-Fi no ESP32
#include <PubSubClient.h>         // Biblioteca MQTT (PubSubClient)
#include <ArduinoJson.h>          // Biblioteca para criar/serializar JSON

const char* WIFI_SSID  = "CURTOCIRCUITO";              // SSID da sua rede Wi-Fi
const char* WIFI_PASS  = "Curto@1020";                 // Senha da sua rede Wi-Fi
const char* MQTT_HOST  = "demo.thingsboard.io";        // Endereço do broker MQTT
const int   MQTT_PORT  = 1883;                         // Porta MQTT (1883 sem TLS)
const char* MQTT_TOPIC = "v1/devices/me/telemetry";    // Tópico onde vamos publicar

const char* CLIENT_TOKEN = "qxVF6fxpZwT1N3fUk34d";     // Token fixo do cliente (usaremos como senha)
const char* MQTT_USER    = CLIENT_TOKEN;               // Usuário do MQTT (ajuste conforme seu broker)
const char* MQTT_PASS    = "";                         // Senha do MQTT (aqui usando o token)

WiFiClient net;                                 // Cliente TCP para a pilha de rede
PubSubClient client(net);                       // Cliente MQTT usando o cliente TCP acima                                 

void setup() {                                  
  Serial.begin(115200);                         // Inicia a serial para logs (115200 bps)
  conectaWiFi();                                // Conecta ao Wi-Fi
  conectaMQTT();                                // Conecta ao broker MQTT
}                  
```

---
layout: default
---

<style>
pre, code {
  white-space: pre-wrap !important;
  word-break: break-word !important;
  overflow-wrap: anywhere !important;
}
.slide { overflow-x: hidden !important; }
</style>

# 📝 Código ESP32 - MQTT e Loop

<div class="overflow-y-auto max-h-114 pl-4">

```cpp {1-12|13-17|18-29}

void loop() {                                   
  if (!client.connected())                      // Verifica se a conexão MQTT caiu
    conectaMQTT();                              // Se caiu, tenta reconectar
  client.loop();                                // Processa a máquina de estados do MQTT
  StaticJsonDocument<96> doc;                   // Documento JSON estático (tamanho 96 bytes)
  doc["status"] = "ok";                         // Campo "status" com valor "ok"
  doc["valor"]  = 1;                            // Campo "valor" com exemplo numérico
  String payload;                                // String para receber o JSON serializado
  serializeJson(doc, payload);                   // Converte o objeto JSON em texto (payload)
  client.publish(MQTT_TOPIC, payload.c_str());   // Publica o texto JSON no tópico MQTT
  delay(3000);                                   
}       
void conectaWiFi() {                            // Função para conectar ao Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASS);             // Inicia a conexão com SSID e senha
  while (WiFi.status() != WL_CONNECTED)         // Aguarda até obter estado "conectado"
    delay(200);                              
}                                              
void conectaMQTT() {                      
  client.setServer(MQTT_HOST, MQTT_PORT);       // Define host e porta 
  while (!client.connected()) {                 // Loop até conectar com sucesso
    client.connect("esp-32", MQTT_USER, MQTT_PASS);                                                                               
    delay(200);                                
  }                                          
}        
```
</div>

---
layout: default
---

# 🧪 Teste do Sistema

## Validação de Comunicação

<div class="mt-4">
<video 
  autoplay 
  loop
  muted 
  controls 
   class="w-120 rounded-lg shadow-lg mx-auto" 
  >
>
  <source src="/videos/comunicacao.mp4" type="video/mp4">
  Seu navegador não suporta vídeos.
</video>
</div>

