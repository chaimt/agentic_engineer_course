---
layout: section-header
---

# Agentic Workflows - Concepts

From LLMs to autonomous development partners

<img src="/images/agentic-hero.png" alt="Agentic Workflows" class="mx-auto mt-6 w-2/3 rounded-xl opacity-90 shadow-lg" />

---

# What are Agentic Workflows?

<v-clicks>

- **Definition**: AI capabilities chained across **multiple steps**, where each step builds on the last using tools (file reads, shell commands, API calls, web searches)

- **Not just autocomplete** — the agent plans, executes, observes, and iterates

- **Tools + Memory + LLM** = a system that can act on your behalf

- **Outcome**: Complex tasks completed autonomously, with the engineer directing at a higher level

</v-clicks>

<br>

> *"An AI agent is a system that perceives its environment, makes decisions, and takes actions to achieve goals — repeatedly, until done."*

---

# Mental Model Shift

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

### Old Model: AI as Autocomplete
- You write code, AI suggests the next line
- One-shot request → one-shot response
- You are the executor
- AI has no memory of what it did before
- Limited to text generation

</div>

<div>

### New Model: AI as Development Partner
- You define *goals*, AI executes *steps*
- Multi-step workflow with feedback loops
- AI is the executor, you are the reviewer
- AI reads files, runs commands, iterates on failures
- Acts through tools on real systems

</div>

</div>

<div class="mt-8 p-4 bg-orange-900 bg-opacity-20 rounded-lg border border-orange-700">

**Key Shift**: Engineers focus on **architecture, specifications, and review** — not line-by-line implementation

</div>

---

# Key Characteristics

<div class="grid grid-cols-3 gap-4 mt-4">

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🔄</div>
<div class="text-lg font-bold text-orange-300">Multi-Step Execution</div>
<div class="text-sm mt-1 opacity-80">Tasks decomposed into sequences of actions, not a single prompt</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🔧</div>
<div class="text-lg font-bold text-orange-300">Tool Use</div>
<div class="text-sm mt-1 opacity-80">Read files, run tests, query APIs, search the web</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">👁️</div>
<div class="text-lg font-bold text-orange-300">Observe & Iterate</div>
<div class="text-sm mt-1 opacity-80">Observes results of each action and adjusts the next step</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🛡️</div>
<div class="text-lg font-bold text-orange-300">Autonomy + Guardrails</div>
<div class="text-sm mt-1 opacity-80">Works independently, but respects boundaries you define</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🧠</div>
<div class="text-lg font-bold text-orange-300">Context Accumulation</div>
<div class="text-sm mt-1 opacity-80">Builds up context across steps to make informed decisions</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🎯</div>
<div class="text-lg font-bold text-orange-300">Goal-Oriented</div>
<div class="text-sm mt-1 opacity-80">Drives toward a defined outcome, handling intermediate failures itself</div>
</div>

</div>

---

# Why They Matter

<div class="grid grid-cols-3 gap-4 mt-4">

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600">
<div class="text-3xl mb-2 text-center">👨‍💻</div>
<div class="text-lg font-bold text-orange-300 text-center mb-2">For Individual Devs</div>

- Large refactors in minutes, not days
- Explore unfamiliar codebases autonomously
- Tests, bug fixes, docs — in parallel
- Focus on decisions needing human judgment

</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600">
<div class="text-3xl mb-2 text-center">👥</div>
<div class="text-lg font-bold text-orange-300 text-center mb-2">For Teams</div>

- Consistent quality via shared standards (`CLAUDE.md`)
- Spec-driven workflows align AI with conventions
- Onboarding accelerated — agent knows the codebase
- Repetitive tasks automated at scale

</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600">
<div class="text-3xl mb-2 text-center">🏢</div>
<div class="text-lg font-bold text-orange-300 text-center mb-2">For Organizations</div>

- Ship features faster, fewer context switches
- Reduce toil on routine engineering tasks
- Senior patterns encoded into agent instructions
- Competitive advantage through faster iteration

</div>

</div>

---

# Industry Adoption

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

- **Anthropic**: Majority of Claude's own code now **written by Claude Code** — eating their own dog food at scale

- **Trust Model**: New users auto-approve ~**20%** of actions; experienced users reach **40%+** as confidence grows

- **Pattern**: Start with bounded tasks → expand scope as confidence grows

- **Vendors**: GitHub Copilot, Cursor, Claude Code, Devin — all betting on agentic workflows as the future

</v-clicks>

</div>

<div class="flex flex-col justify-center gap-4">

<div class="p-3 bg-orange-900 bg-opacity-30 rounded-lg" v-click>

**20% → 40%+**  
Auto-approval rate as trust grows

</div>

<div class="p-3 bg-green-900 bg-opacity-30 rounded-lg" v-click>

💡 **Key Insight**: This isn't a future trend — engineers using these tools today are already shipping significantly faster

</div>

</div>

</div>

---
layout: default
---

# Prompt Engineering Techniques

<div class="grid grid-cols-3 gap-4 mt-3">

<div v-click class="p-4 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**🎯 Zero-Shot**

No examples — rely on the model's training knowledge alone.

<p class="mt-2 text-orange-300 italic">"Classify as positive / negative / neutral: 'The flight was okay.'"<br/>→ <strong>Neutral</strong></p>

</div>

<div v-click class="p-4 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**📚 Few-Shot**

Provide example pairs to guide in-context learning.

<p class="mt-2 text-orange-300 italic">"A baku is a large blue bird. 'We saw bakus in Maui.' → Now write a story about a baku on a ship."</p>

</div>

<div v-click class="p-4 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**🔗 Chain-of-Thought**

Break complex tasks into explicit reasoning steps.

<p class="mt-2 text-orange-300 italic">"I had 8, gave 3, found 4. <em>Think step by step.</em>"<br/>→ 8−3=5, 5+4=<strong>9</strong></p>

</div>

</div>

<!--
Prompt engineering is the foundation before agents even enter the picture.

1. Zero-Shot — no examples, just clear instructions. Works well for tasks the model was trained on.

2. Few-Shot — show don't just tell. Examples dramatically improve performance on novel or ambiguous tasks.

3. Chain-of-Thought — "think step by step" unlocks multi-step reasoning. Critical for math, logic, and planning tasks.
-->
