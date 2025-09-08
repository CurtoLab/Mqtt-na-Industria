---
# MQTT na Indústria
theme: default
# Background pode ser URL de imagem ou cor
background: https://source.unsplash.com/1920x1080/?industry,technology,iot
# favicon personalizado
favicon: "/favicons/favicon-32x32.png"
# Esquema de cores: 'auto', 'light', ou 'dark'
colorSchema: auto
# Proporção dos slides (16:9)
# aspectRatio: 1.77
# Largura real do canvas
canvasWidth: 980
# Informações sobre a apresentação
title: "MQTT na Indústria 4.0"
# Classe CSS para aplicar no slide atual
class: text-center
# Configuração de desenhos
drawings:
  persist: false
# Transições entre slides
transition: view-transition
# Habilitar sintaxe MDC
mdc: true
# Configuração de polls/quiz
pollSettings:
  anonymous: true
---

# MQTT na Indústria 4.0

<span style="font-size: 2rem; color: #0ea5e9;">Conectividade Industrial Inteligente</span>

<div class="mt-12 space-y-4">
  <div class="text-lg opacity-80">
    🏭 Protocolo Industrial • 🌐 IoT • 📊 Monitoramento em Tempo Real
  </div>
  
  <div class="mt-8">
    <span @click="$slidev.nav.next" class="px-6 py-3 rounded-lg cursor-pointer bg-blue-600 text-white hover:bg-blue-700 transition-colors">
      Iniciar Curso <carbon:arrow-right class="inline"/>
    </span>
  </div>
</div>

<div style="position: absolute; bottom: 2rem; left: 0; width: 100%; text-align: center;">
  <strong>curtoLab</strong><br>
  <span style="font-size: 0.9rem; opacity: 0.8;">MQTT na Indústria 4.0</span><br>
  <span style="font-size: 0.8rem; opacity: 0.6;">Curso Técnico - 2025</span>
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
src: ./pages/03-arquitetura-componentes.md
hide: false
---

---
src: ./pages/04-implementacao-pratica.md
hide: false
---

---
src: ./pages/05-casos-uso-industrial.md
hide: false
---

---
src: ./pages/06-monitoramento-dashboards.md
hide: false
---

---
layout: end
---

# Obrigado! 🎉

