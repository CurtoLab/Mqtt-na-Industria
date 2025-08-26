---
layout: default
---

# 🎬 Demo: Snippets e Asciinema

<div class="grid grid-cols-2 gap-6">

<div>

## 📝 Código Externo
Usando snippet do arquivo `snippets/exemplo-conceito.py`:

<<< @/snippets/exemplo-conceito.py#conceito-basico

<div class="text-sm mt-4 opacity-75">
💡 Código mantido em arquivo separado para melhor organização
</div>

</div>

<div>

## 🖥️ Execução em Terminal

<Asciinema 
  src="/demos/exemplo-basico.cast" 
  :playerProps="{
    speed: 1.5, 
    rows: 12,
    autoplay: false
  }" 
/>

<div class="text-sm mt-4 opacity-75">
▶️ Clique para ver a execução do código
</div>

</div>

</div>

<!--
Demonstração dos recursos avançados do template:
- Snippets externos organizados por regiões
- Asciinema para demos de terminal interativas
-->

---
layout: center
---

# 🧠 Quiz Interativo

<Quiz 
  question="Qual é a principal vantagem de usar snippets externos em apresentações?"
  :answers="[
    'Código fica mais bonito nos slides',
    'Facilita manutenção e reutilização do código',
    'Permite usar mais cores na sintaxe',
    'Reduz o tamanho do arquivo slides.md'
  ]"
  correct="B"
  explanation="Snippets externos permitem manter o código em arquivos separados, facilitando testes, versionamento e reutilização em múltiplas apresentações!"
/>

<!--
Quiz interativo para verificar compreensão.
Use após conceitos importantes para fixação.
-->

---
layout: two-cols
---

# 🔄 Sincronização Multi-dispositivo

<v-clicks>

## Como funciona:
1. **Presenter** - Controla a apresentação
2. **Viewers** - Seguem automaticamente
3. **WebSocket** - Comunicação em tempo real
4. **Rede local** - Sem necessidade de internet

## Casos de uso:
- **Aulas presenciais** - Alunos acompanham no próprio device
- **Workshops** - Participantes seguem no ritmo
- **Apresentações remotas** - Sincronização global

</v-clicks>

::right::

<div v-click="5" class="mt-8">

```bash
# Iniciar com sincronização
npm run dev -- --remote=minhasenha --host=0.0.0.0

# URLs geradas:
# Presenter: localhost:3030/presenter/
# Viewers: localhost:3030/?password=minhasenha
```

<div class="mt-6 p-4 bg-blue-50 dark:bg-blue-900 rounded">
<strong>💡 Dica:</strong> Use senhas simples para facilitar acesso da turma!
</div>

</div>

<!--
Recurso diferencial do template: sincronização entre dispositivos.
Muito útil para cursos e workshops interativos.
-->
