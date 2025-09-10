---
layout: two-cols-header
---
<br>

# 🧩 Desafio: Integrar AHT10 e enviar telemetria para ThingsBoard

Objetivo: ler temperatura e umidade do sensor AHT10 no ESP32 e enviar esses valores para o ThingsBoard pelo tópico de telemetria.

::left::

<div class="text-xs leading-tight">   <!-- use text-xs se quiser ainda menor -->

### Requisitos
- ESP32 com AHT10 conectado (I2C)
- Bibliotecas: AHT10, PubSubClient, ArduinoJson
- Device criado no ThingsBoard e Access Token copiado

### Critérios de aceitação
- Leitura correta de temperatura e umidade
- Publicação periódica (ex.: a cada 30s) no tópico: `v1/devices/me/telemetry`
- Payload em JSON com pelo menos: temperature, humidity
- Conexão MQTT usando o Access Token como usuário

</div>

::right::

### Passos sugeridos
1. Instale as libs: AHT10, ArduinoJson, PubSubClient.
2. Inicialize I2C e AHT10 no `setup()`.
3. Conecte ao Wi‑Fi e ao broker ThingsBoard (`demo.thingsboard.io`).
4. No loop, faça leitura do AHT10 e monte um JSON. 
5. Mostre logs no Serial para confirmar envio.


--- 
layout: default
---

### Exemplo mínimo (include + definições)
````md magic-move
```cpp
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
  
```
```cpp
#include <WiFi.h>                 // Biblioteca para Wi-Fi no ESP32
#include <PubSubClient.h>         // Biblioteca MQTT (PubSubClient)
#include <ArduinoJson.h>          // Biblioteca para criar/serializar JSON
#include <Adafruit_AHT10.h>                // Biblioteca controle AHT10
#include <Wire.h>                 // Comunicação i2c

const char* WIFI_SSID  = "CURTOCIRCUITO";              // SSID da sua rede Wi-Fi
const char* WIFI_PASS  = "Curto@1020";                 // Senha da sua rede Wi-Fi
const char* MQTT_HOST  = "demo.thingsboard.io";        // Endereço do broker MQTT
const int   MQTT_PORT  = 1883;                         // Porta MQTT (1883 sem TLS)
const char* MQTT_TOPIC = "v1/devices/me/telemetry";    // Tópico onde vamos publicar
const char* CLIENT_TOKEN = "qxVF6fxpZwT1N3fUk34d";     // Token fixo do cliente (usaremos como senha)
const char* MQTT_USER    = CLIENT_TOKEN;               // Usuário do MQTT (ajuste conforme seu broker)
const char* MQTT_PASS    = "";                         // Senha do MQTT (aqui usando o token)

#define LED_PIN 2                               // LED interno ESP32
WiFiClient net;                                 // Cliente TCP para a pilha de rede
PubSubClient client(net);                       // Cliente MQTT usando o cliente TCP acima 
Adafruit_AHT10 aht;                                    

```
````

--- 
layout: default
---

### Exemplo mínimo (Setup + inicializações)

````md magic-move
```cpp
void setup() 
{                                  
    Serial.begin(115200);                         // Inicia a serial para logs (115200 bps)
    conectaWiFi();                                // Conecta ao Wi-Fi
    conectaMQTT();                                // Conecta ao broker MQTT
}    

```

```cpp
void setup()
{
    Serial.begin(115200); // Inicia a serial para logs (115200 bps)
    Serial.println("ESP32 + AHT10 - Iniciando...");
    pinMode(LED_PIN, OUTPUT);   // Configuração do LED
    digitalWrite(LED_PIN, LOW); // Led apagado

    Wire.begin(); // Inicializar I2C

    if (!aht.begin()) // Inicializar sensor AHT10
    { 
        Serial.println("❌ Erro: AHT10 não encontrado!");
        while (1)
        {
            delay(100);
        }
    }
    Serial.println("✅ AHT10 inicializado com sucesso!");
    delay(2000); // Aguardar estabilização
    Serial.println("Sistema pronto!"); 
    conectaWiFi(); // Conecta ao Wi-Fi
    conectaMQTT(); // Conecta ao broker MQTT
}
```
````

--- 
layout: default
---

### Exemplo mínimo (loop)

````md magic-move
```cpp
void loop()
{
    if (!client.connected()) // Verifica se a conexão MQTT caiu
        conectaMQTT();       // Se caiu, tenta reconectar
    client.loop();           // Processa a máquina de estados do MQTT
    StaticJsonDocument<96> doc; // Documento JSON estático (tamanho 96 bytes)
    doc["status"] = "ok";       // Campo "status" com valor "ok"
    doc["valor"] = 1;           // Campo "valor" com exemplo numérico
    String payload;                              // String para receber o JSON serializado
    serializeJson(doc, payload);                 // Converte o objeto JSON em texto (payload)
    client.publish(MQTT_TOPIC, payload.c_str()); // Publica o texto JSON no tópico MQTT
    delay(3000);
}

```

```cpp
void loop()
{
    // Piscar LED para indicar atividade
    digitalWrite(LED_PIN, HIGH);
    delay(100);
    digitalWrite(LED_PIN, LOW);
    // Ler dados do sensor
    sensors_event_t humidity, temp;
    aht.getEvent(&humidity, &temp); 
    float heatIndex = calculateHeatIndex(temp.temperature, humidity.relative_humidity);

    if (!client.connected())     // Verifica se a conexão MQTT caiu
        conectaMQTT();           // Se caiu, tenta reconectar
    client.loop();               // Processa a máquina de estados do MQTT
    StaticJsonDocument<256> doc; // Documento JSON estático (tamanho 96 bytes)
    doc["temperature"] = temp.temperature;
    doc["humidity"] = humidity.relative_humidity;
    doc["heatIndex"] = heatIndex;
    String payload;                              // String para receber o JSON serializado
    serializeJson(doc, payload);                 // Converte o objeto JSON em texto (payload)
    client.publish(MQTT_TOPIC, payload.c_str()); // Publica o texto JSON no tópico MQTT
    delay(3000);
}
```
````

--- 
layout: default
---

### Exemplo mínimo (funções)

````md magic-move
```cpp
void conectaWiFi()
{                                         // Função para conectar ao Wi-Fi
    WiFi.begin(WIFI_SSID, WIFI_PASS);     // Inicia a conexão com SSID e senha
    while (WiFi.status() != WL_CONNECTED) // Aguarda até obter estado "conectado"
        delay(200);
}
void conectaMQTT()
{
    client.setServer(MQTT_HOST, MQTT_PORT); // Define host e porta do broker no cliente MQTT
    while (!client.connected())
    { // Loop até conectar com sucesso
        client.connect("esp-32", MQTT_USER, MQTT_PASS);
        delay(200);
    }
}

```

```cpp
void conectaWiFi()
{                                         // Função para conectar ao Wi-Fi
    WiFi.begin(WIFI_SSID, WIFI_PASS);     // Inicia a conexão com SSID e senha
    while (WiFi.status() != WL_CONNECTED) // Aguarda até obter estado "conectado"
        delay(200);
}
void conectaMQTT()
{
    client.setServer(MQTT_HOST, MQTT_PORT); // Define host e porta do broker no cliente MQTT
    while (!client.connected())
    { // Loop até conectar com sucesso
        client.connect("esp-32", MQTT_USER, MQTT_PASS);
        delay(200);
    }
}
// Função para calcular índice de calor
float calculateHeatIndex(float temp, float humidity)
{
    return temp + (0.33 * (humidity / 100.0 * 6.105 * 
        exp((17.27 * temp) / (237.7 + temp)))) - 0.5;
}


```
````

--- 
layout: default
---

<br>


# 📈 Resultado — Telemetria Recebida

- O que checar: último valor, taxa de atualização, status do device
  
<div class="mt-4">
<video 
  autoplay 
  loop
  muted 
  controls 
   class="w-150 rounded-lg shadow-lg mx-auto" 
  >
>
  <source src="/videos/resultado.mp4" type="video/mp4">
  Seu navegador não suporta vídeos.
</video>
</div>