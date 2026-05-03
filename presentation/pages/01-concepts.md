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

<div class="mt-8 p-4 bg-blue-900 rounded-lg">

**Key Shift**: Engineers focus on **architecture, specifications, and review** — not line-by-line implementation

</div>

---

# Key Characteristics

<v-clicks>

1. **Multi-Step Execution** — Tasks decomposed into sequences of actions, not a single prompt

2. **Tool Use** — Agents call real tools: read files, run tests, query APIs, search the web

3. **Observation & Iteration** — Agent observes results of each action and adjusts its next step

4. **Autonomy within Guardrails** — Works independently, but respects boundaries you define

5. **Context Accumulation** — Builds up context across steps to make informed decisions

6. **Goal-Oriented** — Drives toward a defined outcome, handling intermediate failures itself

</v-clicks>

---

# Why They Matter

<div class="grid grid-cols-3 gap-4 mt-4">

<div v-click>

### For Individual Devs
- Large refactors in minutes, not days
- Explore unfamiliar codebases autonomously
- Tests, bug fixes, docs — in parallel
- Focus on decisions needing human judgment

</div>

<div v-click>

### For Teams
- Consistent quality via shared standards (`CLAUDE.md`)
- Spec-driven workflows align AI with conventions
- Onboarding accelerated — agent knows the codebase
- Repetitive tasks automated at scale

</div>

<div v-click>

### For Organizations
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
zoom: 0.85
---

# Prompt Engineering Techniques

<div class="grid grid-cols-3 gap-3 mt-1" style="font-size:0.78rem;">

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**🎯 Zero-Shot**

No examples — rely on the model's training knowledge alone.

<p class="mt-1 text-orange-300 italic">"Classify as positive / negative / neutral: 'The flight was okay.'"<br/>→ <strong>Neutral</strong></p>

</div>

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**📚 Few-Shot**

Provide example pairs to guide in-context learning.

<p class="mt-1 text-orange-300 italic">"A baku is a large blue bird. 'We saw bakus in Maui.' → Now write a story about a baku on a ship."</p>

</div>

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**🔗 Chain-of-Thought**

Break complex tasks into explicit reasoning steps.

<p class="mt-1 text-orange-300 italic">"I had 8, gave 3, found 4. <em>Think step by step.</em>"<br/>→ 8−3=5, 5+4=<strong>9</strong></p>

</div>

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**🏗️ Meta Prompting**

Define structure and format, not specific content.

<p class="mt-1 text-orange-300 italic">Step 1: Define variables.<br/>Step 2: Apply formula.<br/>Step 3: Simplify & solve.</p>

</div>

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**♻️ Self-Consistency**

Sample multiple reasoning paths, pick the most consistent answer.

<p class="mt-1 text-orange-300 italic">"At 6 my sister was 3, gap = 3 yrs always."<br/>→ At 70, sister is <strong>67</strong></p>

</div>

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**🎭 Role Prompting**

Assign a persona to shape tone, priorities and domain focus.

<p class="mt-1 text-orange-300 italic">"You are a skeptical VC. List top 3 pros and cons of this pitch."</p>

</div>

</div>

<!--
Prompt engineering is the foundation before agents even enter the picture.

Six key techniques from simple to advanced:

1. Zero-Shot — no examples, just clear instructions. Works well for tasks the model was trained on.

2. Few-Shot — show don't just tell. Examples dramatically improve performance on novel or ambiguous tasks.

3. Chain-of-Thought — "think step by step" unlocks multi-step reasoning. Critical for math, logic, and planning tasks.

4. Meta Prompting — define structure abstractly, not with specific content. Excellent for token efficiency and generalization.

5. Self-Consistency — sample multiple reasoning paths and vote for the most consistent answer. Great for arithmetic and commonsense tasks.

6. Role Prompting — "You are a security auditor" changes what the model prioritizes. Aligns model behavior with domain expectations.

These techniques compose with each other — e.g., Few-Shot + Chain-of-Thought is especially powerful for complex reasoning.

Source: k2view.com/blog/prompt-engineering-techniques/
-->
