---
layout: section
---

# 📊 Monitoramento e Dashboards

Visualização de dados MQTT

---
layout: default
---

# 🎛️ Grafana Dashboard

## Visualização Profissional

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### 🚀 **Configuração Rápida**
```yaml
# docker-compose.yml
version: '3.8'
services:
  mosquitto:
    image: eclipse-mosquitto:2.0
    ports:
      - "1883:1883"
    volumes:
      - ./mosquitto.conf:/mosquitto/config/mosquitto.conf

  influxdb:
    image: influxdb:2.7
    ports:
      - "8086:8086"
    environment:
      - INFLUXDB_DB=factory_data

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin123
```

### 📈 **Métricas Industriais**
- Temperatura em tempo real
- Consumo energético
- Status de máquinas
- Produtividade (OEE)
- Alarmes ativos

</div>

<div>

### 📊 **Tipos de Gráficos**

**Time Series:**
```sql
SELECT mean("value") FROM "temperatura" 
WHERE time >= now() - 24h 
GROUP BY time(5m)
```

**Gauge (Medidor):**
```sql
SELECT last("value") FROM "pressao"
WHERE "machine" = 'compressor_01'
```

**Stat Panel:**
```sql
SELECT count() FROM "alarmes"
WHERE time >= now() - 1h 
AND "severity" = 'critical'
```

**Table:**
```sql
SELECT "machine", last("status"), last("temp")
FROM "status" 
GROUP BY "machine"
```

</div>

</div>

---
layout: default
---

# 🔗 Integração MQTT → InfluxDB

## Pipeline de Dados

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### 🐍 **Script Python Connector**
```python
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
import json

# Configuração InfluxDB
client_influx = InfluxDBClient(
    url="http://localhost:8086",
    token="your-token",
    org="factory"
)
write_api = client_influx.write_api()

def on_message(client, userdata, msg):
    try:
        # Parse da mensagem MQTT
        topic = msg.topic
        payload = json.loads(msg.payload.decode())
        
        # Criar ponto InfluxDB
        point = Point("sensor_data") \
            .tag("location", topic.split('/')[1]) \
            .tag("sensor_type", topic.split('/')[2]) \
            .field("value", payload['value']) \
            .field("unit", payload['unit'])
        
        # Escrever no banco
        write_api.write(bucket="factory", record=point)
        print(f"Dados salvos: {topic} = {payload['value']}")
        
    except Exception as e:
        print(f"Erro ao processar: {e}")

# Cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("factory/+/+")  # Todos os tópicos factory
client.loop_forever()
```

</div>

<div>

### 🔧 **Telegraf (Alternativa)**
```toml
# telegraf.conf
[[inputs.mqtt_consumer]]
  servers = ["tcp://localhost:1883"]
  topics = ["factory/+/temperature", "factory/+/pressure"]
  data_format = "json"
  
  [[inputs.mqtt_consumer.topic_parsing]]
    topic = "factory/+/+"
    measurement = "_/_/measurement"
    tags = "location/sensor_type/_"

[[outputs.influxdb_v2]]
  urls = ["http://localhost:8086"]
  token = "your-influxdb-token"
  organization = "factory"
  bucket = "sensors"
```

### ⚡ **Vantagens do Telegraf**
- Configuração sem código
- Plugins prontos para MQTT
- Transformações de dados
- Alta performance
- Monitoramento integrado

</div>

</div>

---
layout: default
---

# 📱 Dashboard Mobile com Node-RED

## Interface Web Responsiva

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### 🌐 **Node-RED Flow**
```json
[
  {
    "id": "mqtt-in",
    "type": "mqtt in",
    "topic": "factory/+/temperature",
    "broker": "broker-config"
  },
  {
    "id": "json-parse",
    "type": "json"
  },
  {
    "id": "gauge-widget",
    "type": "ui_gauge",
    "min": -10,
    "max": 100,
    "units": "°C"
  },
  {
    "id": "chart-widget",
    "type": "ui_chart"
  }
]
```

### 📊 **Widgets Disponíveis**
- **Gauge**: Medidores circulares
- **Chart**: Gráficos de linha/barra
- **Text**: Valores numéricos
- **Switch**: Controles on/off
- **Button**: Comandos MQTT
- **Table**: Tabelas de dados

</div>

<div>

### 📱 **Interface Mobile**

<div class="bg-gray-900 text-white p-4 rounded-lg">

```
┌─────────────────────┐
│ 🏭 Factory Monitor  │
├─────────────────────┤
│                     │
│   Linha 1: 🟢       │
│   ┌─────────────┐   │
│   │     78°C    │   │
│   │ ████████░░░ │   │
│   └─────────────┘   │
│                     │
│   Pressão: 2.5 bar │
│   Status: ✅ OK     │
│                     │
│   [🚨 Alertas: 0]   │
│   [⚙️ Configurar]   │
│                     │
└─────────────────────┘
```

</div>

### ⚙️ **Configuração**
```bash
# Instalar Node-RED
npm install -g node-red

# Instalar dashboard
npm install node-red-dashboard

# Executar
node-red
# Acesse: http://localhost:1880
```

</div>

</div>

---
layout: default
---

# 🚨 Sistema de Alertas

## Notificações Inteligentes

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### 📧 **Email + SMS Alert**
```python
import smtplib
from email.mime.text import MIMEText
import requests  # Para SMS API

class AlertManager:
    def __init__(self):
        self.email_config = {
            'smtp_server': 'smtp.gmail.com',
            'port': 587,
            'username': 'alerts@factory.com',
            'password': 'app_password'
        }
    
    def send_email_alert(self, subject, message, recipients):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.email_config['username']
        msg['To'] = ', '.join(recipients)
        
        server = smtplib.SMTP(
            self.email_config['smtp_server'],
            self.email_config['port']
        )
        server.starttls()
        server.login(
            self.email_config['username'],
            self.email_config['password']
        )
        server.send_message(msg)
        server.quit()
    
    def send_sms_alert(self, phone, message):
        # Usando API Twilio
        url = "https://api.twilio.com/2010-04-01/Accounts/YOUR_SID/Messages.json"
        data = {
            'From': '+1234567890',
            'To': phone,
            'Body': message
        }
        requests.post(url, data=data, auth=('SID', 'TOKEN'))

# Uso em callback MQTT
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    
    if data['temperatura'] > 80:
        alert = AlertManager()
        alert.send_email_alert(
            "🚨 TEMPERATURA CRÍTICA",
            f"Sensor {msg.topic}: {data['temperatura']}°C",
            ['supervisor@factory.com', 'manutencao@factory.com']
        )
        alert.send_sms_alert(
            '+5511999999999',
            f"ALERTA: Temp. crítica {data['temperatura']}°C"
        )
```

</div>

<div>

### 🔔 **Webhook Integrations**

**Slack:**
```python
def send_slack_alert(webhook_url, message):
    payload = {
        "text": "🚨 Alerta Industrial",
        "attachments": [{
            "color": "danger",
            "fields": [{
                "title": "Detalhes",
                "value": message,
                "short": False
            }]
        }]
    }
    requests.post(webhook_url, json=payload)
```

**Discord:**
```python
def send_discord_alert(webhook_url, message):
    payload = {
        "content": f"🏭 **Factory Alert**\n```{message}```",
        "username": "Factory Bot"
    }
    requests.post(webhook_url, json=payload)
```

**Teams:**
```python
def send_teams_alert(webhook_url, message):
    payload = {
        "@type": "MessageCard",
        "summary": "Factory Alert",
        "themeColor": "FF0000",
        "sections": [{
            "activityTitle": "🚨 Sistema Industrial",
            "activitySubtitle": "Alerta Crítico",
            "text": message
        }]
    }
    requests.post(webhook_url, json=payload)
```

</div>

</div>

---
layout: default
---

# 📈 Relatórios Automatizados

## Business Intelligence

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### 📊 **Relatório Diário Python**
```python
import pandas as pd
from influxdb_client import InfluxDBClient
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas

class DailyReport:
    def __init__(self):
        self.client = InfluxDBClient(
            url="http://localhost:8086",
            token="your-token",
            org="factory"
        )
    
    def generate_daily_report(self, date):
        # Consultar dados do dia
        query = f'''
        from(bucket: "sensors")
          |> range(start: {date}T00:00:00Z, 
                   stop: {date}T23:59:59Z)
          |> filter(fn: (r) => r._measurement == "temperature")
          |> aggregateWindow(every: 1h, fn: mean)
        '''
        
        result = self.client.query_api().query(query)
        
        # Processar dados
        df = pd.DataFrame()
        for table in result:
            for record in table.records:
                df = df.append({
                    'time': record.get_time(),
                    'location': record.values['location'],
                    'value': record.get_value()
                }, ignore_index=True)
        
        # Gerar gráficos
        self.create_charts(df, date)
        
        # Gerar PDF
        self.create_pdf_report(df, date)
    
    def create_charts(self, df, date):
        plt.figure(figsize=(12, 8))
        
        for location in df['location'].unique():
            data = df[df['location'] == location]
            plt.plot(data['time'], data['value'], 
                    label=f'Linha {location}')
        
        plt.title(f'Temperatura por Linha - {date}')
        plt.xlabel('Hora')
        plt.ylabel('Temperatura (°C)')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'temp_report_{date}.png')
        plt.close()
```

</div>

<div>

### 📋 **Template HTML Report**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Relatório Diário - Factory</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .header { background: #2563eb; color: white; padding: 20px; }
        .metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
        .metric-card { border: 1px solid #ddd; padding: 15px; border-radius: 8px; }
        .chart { text-align: center; margin: 20px 0; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🏭 Relatório Diário</h1>
        <p>Data: {{date}} | Gerado automaticamente</p>
    </div>
    
    <div class="metrics">
        <div class="metric-card">
            <h3>🌡️ Temperatura Média</h3>
            <p class="value">{{avg_temperature}}°C</p>
        </div>
        <div class="metric-card">
            <h3>⚡ Consumo Energético</h3>
            <p class="value">{{total_energy}} kWh</p>
        </div>
        <div class="metric-card">
            <h3>🚨 Alertas</h3>
            <p class="value">{{alert_count}} ocorrências</p>
        </div>
    </div>
    
    <div class="chart">
        <img src="temp_report_{{date}}.png" alt="Gráfico Temperatura">
    </div>
    
    <h2>📊 Resumo Executivo</h2>
    <ul>
        <li>Uptime geral: {{uptime}}%</li>
        <li>Eficiência energética: {{efficiency}}%</li>
        <li>Produção total: {{production}} unidades</li>
    </ul>
</body>
</html>
```

### ⏰ **Agendamento Automático**
```bash
# Crontab para relatório diário às 6h
0 6 * * * /usr/bin/python3 /opt/factory/daily_report.py

# Relatório semanal às sextas 18h
0 18 * * 5 /usr/bin/python3 /opt/factory/weekly_report.py
```

</div>

</div>

---
layout: fact
---

# 45%
aumento na eficiência operacional com dashboards IoT

<div class="text-sm opacity-60 mt-4">
Fonte: Deloitte IoT Industrial Survey 2024
</div>
