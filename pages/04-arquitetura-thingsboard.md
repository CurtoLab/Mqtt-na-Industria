---
layout: section
---

#  🏭 **ThigsBoard**

Open-source IoT Platform

---
layout: two-cols-header
---

<br><br>

# 📊 ThingsBoard Platform

## Plataforma de IoT Completa

::left::

### 🎯 **O que é ThingsBoard**
- **Plataforma Open Source** para IoT
- **Coleta, processamento e visualização** de dados
- **Dashboards em tempo real**
- **Regras de negócio** configuráveis
- **APIs REST** para integração
- **Multi-tenant** (vários clientes)

::right::

### ⚡ **Características Principais**
- 🌐 **Protocolos**: MQTT, HTTP, CoAP, LoRaWAN
- 📊 **Dashboards**: Drag-and-drop visual
- 🔔 **Alertas**: Email, SMS, webhooks
- 📈 **Analytics**: Agregações, filtros
- 🔒 **Segurança**: JWT, OAuth2, X.509
- 🏢 **Escalabilidade**: Microservices



---
layout: two-cols-header
---

# 🎛️ Dashboard ThingsBoard

<br>

## Visualização em Tempo Real

::left::

### 📈 **Widgets Disponíveis**
- **Gráficos**: Linha, barra, pizza
- **Mapas**: Geolocalização de dispositivos  
- **Gauges**: Velocímetros, termômetros
- **Tables**: Dados tabulares
- **Cards**: Valores únicos
- **Controle**: Botões, switches
- **Alarme**: Lista de alertas

::right::
### 🎨 **Personalização**
- **Temas**: Claro, escuro, personalizado
- **Layout**: Drag-and-drop responsivo
- **Filtros**: Por device, tempo, valores
- **Exportação**: PDF, Excel, CSV

### ⚡ **Tempo Real**
- **WebSocket** para updates instantâneos
- **Refresh automático** configurável
- **Notificações push** no browser
- **Mobile responsive**

---
layout: two-cols-header
---

# 🔧 ThingsBoard + MQTT

## Integração com Dispositivos

::left::

### 🔒 **Autenticação**
- **Access Token**: Mais simples
- **Basic Authentication**: User/password  
- **X.509 Certificate**: Mais seguro

### 📊 **Funcionalidades**
- **Telemetria em tempo real**
- **Alertas configuráveis**
- **Dashboards interativos**
- **Rule Engine** para automação

::right::

### 📡 **MQTT Topics**
```
📤 Telemetria:
v1/devices/me/telemetry
📤 Atributos:
v1/devices/me/attributes
📥 RPC (Comandos):
v1/devices/me/rpc/request/+
📥 Configuração:
v1/devices/me/attributes/updates
```

### 🎯 **JSON Payload**
```json
{
  "temperature": 25.6,
  "humidity": 60.2,
  "pressure": 1013.25,
  "timestamp": 1609459200000
}
```

---
layout: default
---
# 👤➕ **Criar Conta Thingsboard**

- Acesse o site oficial: [ThingsBoard.io](https://thingsboard.io/)
- Demo público: [demo.thingsboard.io](https://demo.thingsboard.io/)


<!-- instrução curta -->
1. Clique em "Sign up" → preencha nome, e-mail e senha.  

<div class="mt-4">
<video 
  autoplay 
  loop
  muted 
  controls 
  class="w-full rounded-lg shadow-lg max-w-md mx-auto"
>
  <source src="/videos/login.mp4" type="video/mp4">
  Seu navegador não suporta vídeos.
</video>
<p class="text-center text-sm text-gray-600 mt-2">
  📹 Demonstração login ThingsBoard
</p>
</div>

---
layout: two-cols-header
---

# ➕ Criar Device no ThingsBoard

::left::

<div class="pr-10">

### Passo a passo rápido
1. No menu lateral vá em **Devices → Add new device**.
2. Preencha um nome (ex.: "ESP32-Temp-01") e clique em **Add**.
3. Abra o device criado → aba **Credentials** → copie o **Access Token**.
4. Use esse token como "username" no cliente MQTT do ESP32.

**Dica:** marque atributos e telemetry keys relevantes (temperature, humidity, timestamp).

</div>

::right::

### Exemplo MQTT (usar token copiado como USER)
```cpp
// onde TOKEN é o Access Token do device no ThingsBoard
const char* tb_server = "demo.thingsboard.io";
const char* token = "YOUR_DEVICE_TOKEN";
client.connect("ESP32Client", token, NULL);

```
<div class="mt-4">
<video 
  autoplay 
  loop
  muted 
  controls 
   class="w-120 rounded-lg shadow-lg mx-auto" 
  >
>
  <source src="/videos/add-device.mp4" type="video/mp4">
  Seu navegador não suporta vídeos.
</video>
<p class="text-center text-sm text-gray-600 mt-0">
  📹 Demonstração criação device thingsboard
</p>
</div>