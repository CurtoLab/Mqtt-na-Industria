---
layout: section
---

# 🎯 Objetivos do Curso

MQTT na Indústria 4.0

---
layout: two-cols
---

# O que você vai aprender

<!-- Wrap v-clicks so it can scroll if content is large -->
<div class="overflow-auto max-h-[60vh] pr-4">

<v-clicks class="text-sm">   <!-- reduz o tamanho do texto -->

## 🔧 Fundamentos:
- O que é MQTT e por que usar na indústria
- Casos de uso em ambiente industrial

## ⚙️ Técnico:
- Arquitetura broker/cliente
- Tópicos e wildcards
- Implementação com ESP32

## 🛠️ Prático:
- Integração com sistema Thingsboard
- Dashboards de monitoramento
- Desenvolvimento de sensores IoT


</v-clicks>

</div>

::right::

<div class="flex flex-col items-center justify-center min-h-0">
  <div class="text-4xl mb-4">🏭</div>
  
  **Cenário Industrial**
  
  <div class="mt-4 space-y-2 text-sm opacity-80">
    <div>🌡️ Sensores de temperatura</div>
    <div>⚡ Monitoramento de energia</div>
    <div>🔧 Status de máquinas</div>
    <div>📊 Dashboards em tempo real</div>
    <div>🚨 Alertas e notificações</div>
  </div>
</div>


---
layout: default
---

# 🎓 Pré-requisitos

<div class="grid grid-cols-2 gap-6 mt-6">

<div>

## 💻 Conhecimentos Técnicos
- Programação básica (C/C++)
- Conceitos de redes (TCP/IP, Wi-Fi)
- Noções de eletrônica básica
- Familiaridade com linha de comando

</div>

<div>

## 🛠️ Ferramentas Necessárias
- ESP32
- Arduino IDE
- ThingsBoard — instância (cloud ou local)

</div>
</div>

<div class="mt-8 p-4 bg-red-600 rounded-lg">
<strong>💡 Dica:</strong> Não se preocupe se não tem toda experiência! Vamos explicar tudo passo a passo.
</div>

---
layout: fact
---

# 94%
das empresas industriais planejam implementar IoT nos próximos 2 anos

<div class="text-sm opacity-60 mt-4">
Fonte: Industry 4.0 Survey 2024
</div>

---
layout: section
---

# 🔌 ThingsBoard — Integração prática

<div class="overflow-auto max-h-[72vh] text-sm">

**Pontos principais**
- **Autenticação:** `DEVICE_TOKEN` como username (senha vazia)
- **Telemetria:** tópico `v1/devices/me/telemetry`
- **Atributos compartilhados:** `v1/devices/me/attributes`
- **RPC (comandos):**  
  - Request: `v1/devices/me/rpc/request/+`  
  - Resposta: `v1/devices/me/rpc/response/<id>`
- **Segurança:** Use TLS (porta 8883) em produção

---
**Exemplo MQTT (CLI):**
```bash
# Publicar telemetria (username = DEVICE_TOKEN)
mosquitto_pub -h TB_HOST -p 1883 -t "v1/devices/me/telemetry" -u "DEVICE_TOKEN" -m '{"temperature":25.3}'

# Escutar RPC requests
mosquitto_sub -h TB_HOST -t "v1/devices/me/rpc/request/+" -u "DEVICE_TOKEN"
```

---

**Exemplo Python (paho-mqtt):**
```python
import paho.mqtt.client as mqtt
client = mqtt.Client()
client.username_pw_set("DEVICE_TOKEN", password=None)
client.connect("TB_HOST", 1883, 60)
client.publish("v1/devices/me/telemetry", '{"temp": 22.5}')
client.loop_stop()
```

---

**Exemplo ESP32 (Arduino - Pub):**
```cpp
client.connect("DEVICE_TOKEN"); // username
client.publish("v1/devices/me/telemetry", "{\"temp\":23.1}");
```

</div>

---
layout: default
---

# Próximo passo
- Criar dispositivo no ThingsBoard e anotar DEVICE_TOKEN  
- Testar publish/subscribe com mosquitto (ou script Python)  
- Criar dashboard básico e verificar telemetria
