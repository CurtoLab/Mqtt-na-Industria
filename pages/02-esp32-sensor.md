---
layout: section
---

# 🔌 ESP32 & Sensor IoT

Hardware e Programação Básica

---
layout: default
---

# 🎯 ESP32 DevKit - Visão Geral


<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### 📋 **Especificações Técnicas**
- **Processador**: Dual-core 240MHz
- **RAM**: 520KB SRAM
- **Flash**: 4MB (padrão)
- **Wi-Fi**: 802.11 b/g/n
- **Bluetooth**: 4.2 + BLE

### ⚡ **Vantagens**
- 🚀 **Performance**: Dual-core potente
- 🌐 **Conectividade**: Wi-Fi + Bluetooth nativo
- 💰 **Custo**: Muito acessível
- 🔧 **Facilidade**: Arduino IDE compatível
- 📚 **Comunidade**: Vasta documentação

</div>

<div class="flex flex-col items-center">

<img src="/images/esp32.png" alt="ESP32 DevKit" class="w-64 h-auto mb-4"/>

### 🔌 **Pinout Essencial**
```
GPIO Digitais: 0-39
GPIO Analógicos: 32-39
PWM: Todos os GPIO
I2C: GPIO 21 (SDA), 22 (SCL)
SPI: GPIO 23 (MOSI), 19 (MISO), 18 (SCK)
UART: GPIO 1 (TX), 3 (RX)
```

<div class="mt-4 p-3 bg-blue-100 rounded text-sm">
💡 <strong>Dica:</strong> Evite usar GPIO 0, 2, 12, 15 para sensores
</div>

</div>

</div>

---
layout: default
---

# 🌡️ Sensor AHT10


<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### 📊 **Características**
- **Protocolo**: I2C (0x38)
- **Temperatura**: -40°C a +85°C (±0.3°C)
- **Umidade**: 0% a 100% RH (±2%)
- **Tensão**: 2.2V a 5.5V
- **Corrente**: 0.25mA (ativo), 0.1µA (standby)
- **Tempo resposta**: 5 segundos
- **Interface**: 4 pinos (VCC, GND, SDA, SCL)

### ✅ **Vantagens vs DHT22**
- 🔧 **Interface I2C** (mais confiável)
- ⚡ **Menor consumo** de energia
- 📏 **Tamanho compacto**
- 🛡️ **Maior precisão**
- 💰 **Custo competitivo**
- 🔄 **Leitura mais rápida**

</div>

<div class="flex flex-col items-center">

<img src="/images/aht10.png" alt="AHT10 Sensor" class="w-48 h-auto mb-4"/>

### 🔌 **Conexões**
```
AHT10    →    ESP32
VCC      →    3.3V
GND      →    GND
SDA      →    GPIO 21
SCL      →    GPIO 22
```

<div class="mt-6 p-4 bg-green-100 rounded">
<strong>📚 Biblioteca necessária:</strong><br>
<code>AHT10</code> by Rob Tillaart
</div>

</div>

</div>

---
layout: default
---

# 🔧 Montagem do Circuito

## Esquema de Ligação

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

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### 🛠️ **Componentes Necessários**
- 1x ESP32 DevKit
- 1x Sensor AHT10
- 1x LED (opcional)
- 1x Resistor 220Ω (para LED)
- 1x Protoboard
- Jumpers macho-macho

</div>

<div>

### ⚠️ **Cuidados na Montagem**
- ✅ Verificar polaridade do LED
- ✅ AHT10 usar 3.3V (não 5V)
- ✅ Conexões I2C: SDA=21, SCL=22
- ✅ GND comum para todos componentes
- ⚠️ Não inverter VCC e GND

</div>

</div>

---
layout: default
---

# 💻 Configuração Arduino IDE



### 1️⃣ **Instalar ESP32 no Arduino IDE**
```
Boards Manager → Buscar "ESP32" → Esp32 by Espressif Systems → Install:

```

<div class="mt-4">
<video 
  autoplay 
  loop 
  muted 
  controls 
  class="w-full rounded-lg shadow-lg max-w-md mx-auto"
>
  <source src="/videos/install-board.mp4" type="video/mp4">
  Seu navegador não suporta vídeos.
</video>
<p class="text-center text-sm text-gray-600 mt-2">
  📹 Demonstração da instalação do ESP32 no Arduino IDE
</p>
</div>

---
layout: default
---

### 2️⃣ **Instalar Bibliotecas**
```
Library Manager → Buscar AHT10 → Adafruit AHT10 by Adafruit:
```

<div class="mt-4">
<video 
  autoplay 
  loop 
  muted 
  controls 
  class="w-full rounded-lg shadow-lg max-w-md mx-auto"
>
  <source src="/videos/install-lib.mp4" type="video/mp4">
  Seu navegador não suporta vídeos.
</video>
<p class="text-center text-sm text-gray-600 mt-2">
  📹 Demonstração da instalação da lib AHT10
</p>
</div>

---
layout: default
---

### 3️⃣ **Configurar Board**
```
Tools → Select other board → Buscar DOIT ESP32 DEVKIT → Selecionar Porta USB → OK

```
<div class="mt-4">
<video 
  autoplay 
  loop
  muted 
  controls 
  class="w-full rounded-lg shadow-lg max-w-md mx-auto"
>
  <source src="/videos/select-board.mp4" type="video/mp4">
  Seu navegador não suporta vídeos.
</video>
<p class="text-center text-sm text-gray-600 mt-2">
  📹 Demonstração da instalação do ESP32 no Arduino IDE
</p>
</div>


---
layout: two-cols-header
---

# 📝 Código Base - Setup

::left::

<div class="col-span-2 overflow-y-auto max-h-110 text-xs" style="line-height:1.1;">

```cpp
#include <Adafruit_AHT10.h>
#include <Wire.h>
// Definições
#define LED_PIN 2 // LED interno ESP32
// Inicialização do sensor
Adafruit_AHT10 aht;

void setup()
{
  Serial.begin(115200); // Configuração serial
  Serial.println("ESP32 + AHT10 - Iniciando...");
  pinMode(LED_PIN, OUTPUT); // Configuração do LED
  digitalWrite(LED_PIN, LOW);
  Wire.begin(); // Inicializar I2C
  if (!aht.begin())
  { // Inicializar sensor AHT10
    Serial.println("❌ Erro: AHT10 não encontrado!");
    while (1)
    {
      delay(100);
    }
  }
  Serial.println("✅ AHT10 inicializado com sucesso!");
  delay(2000); // Aguardar estabilização
  Serial.println("Sistema pronto!");
}
```
</div>

::right::

<div class="pl-6">

### 🔍 Explicação do código

### 📚 Bibliotecas
- `AHT10.h` — comunicação com o sensor AHT10
- `Wire.h` — protocolo I2C

### ⚙️ Definições
- `LED_PIN` — pino do LED para indicação visual

### ⚡ O que o `setup()` faz
1. Inicializa a porta Serial em 115200 baud
2. Configura o pino do LED como saída
3. Inicializa o barramento I2C
4. Tenta iniciar o sensor AHT10 e entra em loop se não for encontrado (delay para evitar busy-wait)
5. Aguarda estabilização antes de continuar

</div>

---
layout: two-cols-header
---

# 🔄 Código Base - Loop Principal

::left::

<div class="col-span-2 overflow-y-auto max-h-110 text-xs" style="line-height:1.1;">

```cpp
void loop()
{
  // Piscar LED para indicar atividade
  digitalWrite(LED_PIN, HIGH);
  delay(100);
  digitalWrite(LED_PIN, LOW);
  sensors_event_t humidity, temp;
  aht.getEvent(&humidity, &temp); 

  // Verificar se leitura foi bem-sucedida
  if (isnan(temp.temperature) || isnan(humidity.relative_humidity))
  {
    Serial.println("❌ Erro ao ler AHT10!");
    delay(2000);
    return;
  }

  // Exibir dados no Serial Monitor
  Serial.println("📊 === LEITURA SENSOR ===");
  Serial.print("🌡️  Temperatura: ");
  Serial.print(temp.temperature, 1);
  Serial.println("°C");

  Serial.print("💧 Umidade: ");
  Serial.print(humidity.relative_humidity, 1);
  Serial.println("%");

  // Calcular índice de calor
  float heatIndex = calculateHeatIndex(temp.temperature, humidity.relative_humidity);
  Serial.print("🔥 Sensação térmica: ");
  Serial.print(heatIndex, 1);
  Serial.println("°C");

  Serial.println("========================\n");

  // Aguardar próxima leitura
  delay(5000); // 5 segundos
}

// Função para calcular índice de calor
float calculateHeatIndex(float temp, float humidity)
{
  return temp + (0.33 * (humidity / 100.0 * 6.105 * exp((17.27 * temp) / (237.7 + temp)))) - 0.5;
}
```
</div>

::right::

<div class="pl-6 text-lg" > 

### 🔍 **Funcionalidades**

### **Indicação Visual:**
- 💡 LED pisca a cada leitura

### **Leitura de Dados:**
- 🌡️ Temperatura em °C (1 casa decimal)
- 💧 Umidade relativa em %
- 🔥 Índice de calor calculado


### **Tratamento de Erro:**
- ❌ Detecta falhas de leitura
- 🔄 Tenta novamente após delay

<br>

### 🎯 **Próximo Passo**
Integração com **MQTT** para envio dos dados ao **ThingsBoard**!

</div>



---
layout: two-cols-header
---

# 🚀 Teste e Verificação

::left::

## Validando o Funcionamento

<div class="pl-6 text-sm" > 

### 📋 **Checklist de Teste**

- ✅ **Upload do código sem erros**
- ✅ **LED pisca a cada 5 segundos**
- ✅ **Serial Monitor mostra dados**
- ✅ **Temperatura coerente (20-30°C)**
- ✅ **Umidade coerente (30-70%)**
- ✅ **Sem mensagens de erro**

### 🔧 **Resolução de Problemas**

### **Erro "AHT10 não encontrado":**
- Verificar conexões SDA/SCL
- Confirmar alimentação 3.3V
- Testar endereço I2C:

### **Dados estranhos:**
- Verificar se é AHT10 (endereço 0x38)
- Aguardar 2 minutos para estabilizar

</div>

::right::

### 📊 **Saída Esperada no Serial Monitor**

```
ESP32 + AHT10 - Iniciando...
✅ AHT10 inicializado com sucesso!
Sistema pronto!

📊 === LEITURA SENSOR ===
🌡️  Temperatura: 24.5°C
💧 Umidade: 45.2%
🔥 Sensação térmica: 24.8°C
========================

📊 === LEITURA SENSOR ===
🌡️  Temperatura: 24.6°C
💧 Umidade: 45.0%
🔥 Sensação térmica: 24.9°C
========================
```


✅ <strong>Tudo funcionando!</strong><br>
Próximo passo: Conectar ao MQTT
