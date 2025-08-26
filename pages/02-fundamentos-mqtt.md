---
layout: section
---

# 📡 Fundamentos MQTT

Message Queuing Telemetry Transport

---
layout: default
---

# 🤔 O que é MQTT?

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

## Definição
**MQTT** (Message Queuing Telemetry Transport) é um protocolo de mensagens leve, projetado para comunicação M2M (Machine-to-Machine) em redes com largura de banda limitada.

## Características
- **Leve**: Overhead mínimo
- **Confiável**: Diferentes níveis de QoS
- **Bidirecional**: Publish/Subscribe
- **Persistente**: Mensagens retidas
- **Seguro**: Suporte TLS/SSL

</div>

<div class="flex flex-col justify-center">

```mermaid
graph TD
    A[Sensor] -->|publish| B[Broker MQTT]
    C[Atuador] -->|publish| B
    B -->|subscribe| D[Dashboard]
    B -->|subscribe| E[Sistema ERP]
    B -->|subscribe| F[Alertas]
```

</div>

</div>

---
layout: two-cols
---

# 🆚 MQTT vs Outros Protocolos

## Por que MQTT na Indústria?

<v-clicks>

### ✅ **Vantagens do MQTT:**
- Baixo consumo de energia
- Funciona com conexões instáveis
- Suporte nativo ao IoT
- Escalabilidade horizontal
- Padrão aberto (ISO/IEC 20922)

### ⚡ **Comparação:**
- **HTTP**: Muito pesado para IoT
- **CoAP**: Bom, mas menos maduro
- **WebSocket**: Ótimo para web, complexo para embarcados
- **AMQP**: Robusto, mas pesado

</v-clicks>

::right::

<div class="mt-8">

| Protocolo | Overhead | Tempo Real | IoT Ready |
|-----------|----------|------------|-----------|
| **MQTT**  | 2 bytes  | ✅ Sim     | ✅ Sim    |
| HTTP      | ~200 bytes | ❌ Não    | ⚠️ Limitado |
| CoAP      | 4 bytes  | ✅ Sim     | ✅ Sim    |
| WebSocket | 6+ bytes | ✅ Sim     | ⚠️ Limitado |

<div class="mt-6 text-sm opacity-70">
💡 MQTT é 100x mais eficiente que HTTP
</div>

</div>

---
layout: default
---

# 🏗️ Modelo Publish/Subscribe

<div class="flex justify-center mt-8">

```mermaid
sequenceDiagram
    participant S as Sensor
    participant B as Broker
    participant D as Dashboard
    participant A as Alert System
    
    Note over B: Tópico: factory/temperature
    
    S->>B: PUBLISH temperature: 75°C
    Note over B: Broker retém a mensagem
    
    D->>B: SUBSCRIBE factory/temperature
    B->>D: 75°C
    
    A->>B: SUBSCRIBE factory/temperature
    B->>A: 75°C
    
    S->>B: PUBLISH temperature: 95°C
    B->>D: 95°C (automático)
    B->>A: 95°C (automático)
```

</div>

<div class="mt-6 grid grid-cols-3 gap-4 text-sm">
<div class="p-3 bg-green-50 rounded">
<strong>Publisher</strong><br>
Envia dados para tópicos
</div>
<div class="p-3 bg-blue-50 rounded">
<strong>Broker</strong><br>
Gerencia e roteia mensagens
</div>
<div class="p-3 bg-purple-50 rounded">
<strong>Subscriber</strong><br>
Recebe dados de tópicos
</div>
</div>

---
layout: default
---

# 🎯 Tópicos e Wildcards

## Sistema Hierárquico de Tópicos

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### 📝 Estrutura de Tópicos
```
factory/
├── line1/
│   ├── machine_a/temperature
│   ├── machine_a/pressure
│   └── machine_b/status
├── line2/
│   ├── conveyor/speed
│   └── robot/position
└── energy/
    ├── consumption
    └── generation
```

</div>

<div>

### 🔍 Wildcards

**Single Level (+)**
```
factory/line1/+/temperature
# Recebe:
# factory/line1/machine_a/temperature
# factory/line1/machine_b/temperature
```

**Multi Level (#)**
```
factory/line1/#
# Recebe TUDO de line1:
# factory/line1/machine_a/temperature
# factory/line1/machine_a/pressure
# factory/line1/machine_b/status
```

</div>

</div>

<div class="mt-6 p-4 bg-yellow-50 rounded-lg">
<strong>⚠️ Cuidado:</strong> Use wildcards com moderação em produção para evitar sobrecarga.
</div>
