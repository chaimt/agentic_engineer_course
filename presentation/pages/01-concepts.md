# Agentic Workflows - Concepts

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

# Developer Productivity Gains

<div class="grid grid-cols-3 gap-3 mt-3">

<div class="p-3 bg-gray-800 rounded-lg text-center" v-click>

### Speed
**55%** faster task completion (GitHub Copilot research, 2023)

</div>

<div class="p-3 bg-gray-800 rounded-lg text-center" v-click>

### Quality
**Fewer context switches** — agent handles boilerplate, engineer focuses on design

</div>

<div class="p-3 bg-gray-800 rounded-lg text-center" v-click>

### Scale
**Multi-agent systems** work in parallel — a sprint's work explored in hours

</div>

</div>

<div class="mt-3 text-sm" v-click>

**Practical metrics from teams using Claude Code:**

<div class="grid grid-cols-2 gap-x-6 mt-1">

- Large refactors (50+ files): hours → minutes
- Writing test coverage: ~10x faster

- Onboarding to unfamiliar codebases: dramatically faster
- Documentation generation: near-zero marginal cost

</div>

</div>
