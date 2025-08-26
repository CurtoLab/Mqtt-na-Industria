# curtoLab - Template Slidev

Template profissional para criação de cursos e laboratórios técnicos usando [Slidev](https://sli.dev/).

## 🎯 Características

- **Template educacional** otimizado para cursos técnicos
- **Recursos interativos** (polls, quiz, demos)
- **Sincronização** entre dispositivos para apresentações
- **Demos de terminal** com Asciinema
- **Totalmente customizável** com Vue.js

## 🚀 Recursos Avançados

### 📊 Interatividade
- **Polls em tempo real** - Enquetes com a turma
- **Quiz interativo** - Avaliação instantânea
- **Sincronização** - Controle remoto entre dispositivos

### 🖥️ Demonstrações
- **Asciinema** - Gravação e reprodução de terminal
- **Snippets de código** - Blocos externos organizados
- **Componentes Vue** - Interações personalizadas

### 🎨 Personalização
- **Temas flexíveis** - Light/dark/auto
- **Logo customizável** - Branding institucional
- **Layout responsivo** - Múltiplos formatos

## 📦 Instalação

### Pré-requisitos
- Node.js 20+ (recomendado)
- npm ou pnpm

### Setup Rápido
```bash
# Clonar template
git clone <este-repositorio> meu-curso
cd meu-curso

# Instalar dependências
npm install

# Iniciar desenvolvimento
npm run dev
```

### Comandos Disponíveis
```bash
npm run dev          # Desenvolvimento com hot-reload
npm run build        # Build para produção
npm run export-pdf   # Exportar para PDF
npm run preview      # Visualizar build
```

## 📚 Como Usar

### 1. Estrutura de Arquivos
```
curtolab-template/
├── slides.md           # Apresentação principal
├── pages/             # Slides modulares
├── components/        # Componentes Vue
├── snippets/          # Código externo
├── public/           # Assets (imagens, etc)
└── package.json      # Configurações
```

### 2. Personalização Básica

Edite o cabeçalho do `slides.md`:
```yaml
---
title: 'Meu Curso Incrível'
background: 'https://minha-imagem.jpg'
colorSchema: auto
---
```

### 3. Adicionando Conteúdo

#### Slide Básico
```markdown
---
layout: default
---

# Título da Seção

Conteúdo do slide...
```

#### Demo de Terminal
```markdown
<Asciinema src="/demos/minha-demo.cast" />
```

#### Poll Interativo
```vue
<Poll question="Qual sua linguagem favorita?" 
      :answers="['Python', 'JavaScript', 'Go', 'Rust']" />
```

#### Quiz
```vue
<Quiz question="Qual a resposta correta?"
      :answers="['A', 'B', 'C', 'D']"
      correct="B" />
```

## 🎨 Customização Avançada

### Logo Institucional
1. Adicione seu logo em `public/logo.png`
2. Atualize `favicon` no cabeçalho do `slides.md`

### Temas e Cores
```yaml
# Em slides.md
colorSchema: auto  # light, dark, auto
theme: default     # ou theme customizado
```

### Componentes Personalizados
Crie componentes Vue em `components/` para funcionalidades específicas.

## 📱 Recursos para Apresentação

### Modo Apresentador
- Notas do palestrante
- Timer de apresentação
- Controles avançados

### Sincronização Remota
```bash
# Apresentação com controle remoto
npm run dev -- --remote=senha123 --host=0.0.0.0
```

### Exportação
```bash
# PDF para impressão
npm run export-pdf

# Site estático
npm run build
```

## 🛠️ Addons Incluídos

- **@olzhas-adiyatov/slidev-addon-asciinema** - Demos de terminal
- **slidev-addon-sync** - Sincronização entre dispositivos  
- **slidev-component-poll** - Polls e quiz interativos

## 📖 Exemplos

### Estrutura Sugerida para Cursos
1. **Introdução** - Objetivos e agenda
2. **Conceitos** - Teoria fundamental
3. **Demonstrações** - Exemplos práticos
4. **Hands-on** - Exercícios guiados
5. **Quiz** - Verificação de aprendizado
6. **Conclusão** - Resumo e próximos passos

### Templates de Slide

#### Slide de Conceito
```markdown
---
layout: two-cols
---

# Conceito Important

Explicação do lado esquerdo...

::right::

```python
# Código exemplo
def exemplo():
    return "Olá mundo!"
```

```

#### Slide de Exercício
```markdown
---
layout: default
---

# 🛠️ Exercício Prático

## Objetivo
Implementar uma função que...

## Instruções
1. Abra seu editor
2. Crie o arquivo `exercicio.py`
3. Implemente a solução

<Asciinema src="/demos/exercicio-solucao.cast" />
```

## 🤝 Contribuição

Para melhorar este template:
1. Fork do repositório
2. Crie uma branch para sua feature
3. Commit das mudanças
4. Pull request

## 📄 Licença

MIT License - veja [LICENSE](LICENSE) para detalhes.

## 🔗 Links Úteis

- [Documentação Slidev](https://sli.dev/)
- [Sintaxe Markdown](https://sli.dev/guide/syntax)
- [Temas e Layouts](https://sli.dev/resources/theme-gallery)
- [Componentes Vue](https://sli.dev/guide/component)

---

**curtoLab** - Template para educação técnica de qualidade 🚀
