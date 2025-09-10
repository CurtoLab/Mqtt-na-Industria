---
# Configurações globais do Slidev
theme: default
colorSchema: auto
background: https://source.unsplash.com/1920x1080/?gradient
title: MQTT na Indústria 4.0
info: |
    ## MQTT na Indústria 4.0
    Conectando Dispositivos IoT com ESP32 & ThingsBoard

    Apresentação técnica sobre implementação de telemetria industrial
    usando protocolo MQTT, microcontroladores ESP32 e plataforma ThingsBoard.

    Autor: CurtoLab

# Configurações de apresentação
transition: fade
mdc: true
download: true
exportFilename: mqtt-industria-40
highlighter: shiki
lineNumbers: true
monaco: true
drawings:
    enabled: true
    persist: false

# Configurações de aparência
darkClass: "dark"
lightClass: "light"
canvasWidth: 980
htmlAttrs:
    dir: ltr
    lang: pt-br

# Fontes personalizadas
fonts:
    sans: "Inter"
    serif: "Playfair Display"
    mono: "Fira Code"

css: unocss
layout: center
---
# MQTT na Indústria 4.0

<span style="font-size: 2rem; color: #0ea5e9;">Conectividade Industrial Inteligente</span>

<div class="mt-12 space-y-4">
  <div class="text-lg opacity-80">
    🏭 Protocolo Industrial • 🌐 IoT • 📊 Monitoramento em Tempo Real
  </div>
  
  <div class="mt-8">
 
  </div>
</div>

<div style="position: absolute; bottom: 2rem; left: 0; width: 100%; text-align: center;">
  <strong>CurtoLab</strong><br>
  <span style="font-size: 0.9rem; opacity: 0.8;">MQTT na Indústria 4.0</span><br>
  <span style="font-size: 0.8rem; opacity: 0.6;">Workshop - 2025</span>
</div>

<!--
Estrutura modular do curso MQTT na Indústria 4.0
Cada módulo aborda aspectos específicos do protocolo e suas aplicações
-->

---
src: ./pages/01-introducao.md
hide: false
---

---
src: ./pages/02-esp32-sensor.md
hide: false
---

---
src: ./pages/03-fundamentos-mqtt.md
hide: false
---

---
src: ./pages/04-arquitetura-thingsboard.md
hide: false
---

---
src: ./pages/05-implementacao-pratica.md
hide: false
---

---
src: ./pages/06-desafio.md
hide: false
---

---
src: ./pages/07-monitoramento-dashboards.md
hide: false
---

---
src: ./pages/08-finalizacao.md
hide: false
---

---
src: ./pages/end.md
hide: false
---