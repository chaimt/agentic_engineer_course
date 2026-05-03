---
theme: default
background: '#000000'
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Agentic Workflows
  
  Educational presentation on agentic workflows - understanding the shift from AI as autocomplete to AI as development partner.
  
  Learn about:
  - What agentic workflows are and how they differ from LLMs
  - Practical implementation patterns
  - Advanced workflow techniques
  - Real-world applications
drawings:
  persist: false
transition: slide-left
title: Agentic Workflows
controls: false
hideInToc: True
mdc: true
---

<div class="flex flex-col items-center justify-center h-full gap-4">



<h1 class="text-6xl font-extrabold tracking-tight" style="color:#ff8c00;text-shadow:0 0 40px #ff6b0066,0 2px 8px #0008;">
  Agentic Workflows
</h1>

<p class="text-2xl font-light mt-1" style="color:#ffb86090;">
  From AI Autocomplete to Development Partner
</p>

<div class="pt-4 cursor-pointer" @click="$slidev.nav.next">
  <img src="/images/agentic-hero.png" alt="Agentic Hero" class="w-128 opacity-95 rounded-xl shadow-lg"/>
</div>

</div>

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <mdi:pencil />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <mdi:github />
  </a>
</div>

<!--
Welcome to the Agentic Workflows presentation!

This presentation will take you on a journey from understanding basic LLM capabilities to implementing sophisticated agentic workflows in your development practice.

Target time: 30-45 minutes total
- Introduction and concepts: 8 min
- Benefits and use cases: 7 min
- Workflow patterns: 10 min
- Practical tips: 8 min
- Q&A: 7 min
-->

---
layout: default
---

# Presentation Overview

<v-clicks>

## What We'll Cover

1. 🤖 **Agentic Workflows** - From LLMs to autonomous development partners

2. 🔧 **Tools & Memory** - The primitives that transform LLMs into agents

3. 🔄 **Core Patterns** - Reflection, Tool Use, and Planning in practice

4. 🏗️ **Frameworks** - CrewAI, Pydantic AI, LangGraph, and Agno compared

5. 🛠️ **Principles & Best Practices** - ACI design, hooks, spec-driven workflows

6. ❓ **Q&A** - Your questions and discussion

</v-clicks>

<!--
This is your roadmap for the next 30-45 minutes.

We'll start with foundational concepts, explore practical patterns, and finish with tips for adoption.

Each section builds on the previous one, so we'll progress from theory to practice.
-->

---
src: ./pages/01-concepts.md
---

---
src: ./pages/02-tools-memory.md
---

---
src: ./pages/04-patterns.md
---

---
src: ./pages/07-frameworks.md
---

---
src: ./pages/06-principles.md
---
