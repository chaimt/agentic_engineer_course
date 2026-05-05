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

# About Me

<div class="flex gap-8 mt-4">

<div class="flex-shrink-0 flex flex-col items-center gap-3">
  <img src="/images/chaim-turkel.png" alt="Chaim Turkel" class="w-44 h-44 rounded-full object-cover border-4 shadow-lg" style="border-color:#ff8c00;" />
  <div class="text-xl font-bold text-orange-300">Chaim Turkel</div>
</div>

<div class="grid grid-cols-2 gap-4 flex-1">

<div class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 flex items-center gap-3">
  <mdi:account-circle class="text-4xl flex-shrink-0" style="color:#ff8c00;" />
  <div>
    <div class="text-base font-bold text-orange-300">Software Architect</div>
    <div class="text-xs opacity-70 mt-1">AI / Distributed & Data</div>
  </div>
</div>

<div class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 flex items-center gap-3">
  <mdi:account-group class="text-4xl flex-shrink-0" style="color:#ff8c00;" />
  <div>
    <div class="text-base font-bold text-orange-300">Group Leader @ Tikal</div>
    <div class="text-xs opacity-70 mt-1">Leading developer community & knowledge sharing</div>
  </div>
</div>

<div class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 flex items-center gap-3">
  <mdi:calendar-clock class="text-4xl flex-shrink-0" style="color:#ff8c00;" />
  <div>
    <div class="text-base font-bold text-orange-300">25+ Years in the Industry</div>
    <div class="text-xs opacity-70 mt-1">From early web to modern cloud-native systems</div>
  </div>
</div>

<div class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 flex items-center gap-3">
  <mdi:brain class="text-4xl flex-shrink-0" style="color:#ff8c00;" />
  <div>
    <div class="text-base font-bold text-orange-300">Distributed Data & AI</div>
    <div class="text-xs opacity-70 mt-1">Expertise in scalable systems & agentic workflows</div>
  </div>
</div>

</div>

</div>

<!--
A quick intro before we dive in.
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
