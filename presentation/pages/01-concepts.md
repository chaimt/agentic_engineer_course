# Agentic Workflows - Concepts

---
layout: cover
---

# Agentic Workflows
## Building AI-Assisted Development Systems

Presenter: [Your Name]
Date: [Presentation Date]

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

<div class="grid grid-cols-2 gap-6 mt-4">

<div v-click>

### For Individual Developers
- Handle large refactors in minutes, not days
- Explore unfamiliar codebases autonomously
- Write tests, fix bugs, generate docs — in parallel
- Focus on decisions that require human judgment

</div>

<div v-click>

### For Teams
- Consistent code quality through shared agent standards (`CLAUDE.md`)
- Spec-driven workflows align AI output with team conventions
- Onboarding accelerated — agent understands the codebase
- Repetitive tasks automated at scale

</div>

</div>

<div class="mt-6" v-click>

### For Organizations
- Ship features faster with fewer context switches
- Reduce toil on routine engineering tasks
- Scale expertise: senior patterns encoded into agent instructions
- Competitive advantage through faster iteration cycles

</div>

---

# Industry Adoption

<v-clicks>

- **Anthropic**: The majority of Claude's own code is now **written by Claude Code** — eating their own dog food at scale

- **Trust Model**: Adoption follows a trust curve:
  - New users auto-approve ~**20%** of agent actions
  - Experienced users reach **40%+** auto-approval
  - Trust grows as engineers learn what agents do well vs. where they need review

- **Pattern**: Start with bounded, well-defined tasks → expand scope as confidence grows

- **Industry signal**: GitHub Copilot, Cursor, Claude Code, Devin — all major vendors betting on agentic workflows as the future of software development

</v-clicks>

<div class="mt-6 p-3 bg-green-900 rounded" v-click>

💡 **Key Insight**: This isn't a future trend — engineers using these tools today are already shipping significantly faster

</div>

---

# Developer Productivity Gains

<div class="grid grid-cols-3 gap-4 mt-6">

<div class="p-4 bg-gray-800 rounded-lg text-center" v-click>

### Speed
**55%** faster task completion reported in controlled studies (GitHub Copilot research, 2023)

</div>

<div class="p-4 bg-gray-800 rounded-lg text-center" v-click>

### Quality
**Fewer context switches** — agent handles the boilerplate, engineer focuses on design

</div>

<div class="p-4 bg-gray-800 rounded-lg text-center" v-click>

### Scale
**Multi-agent systems** can work in parallel — what one engineer does in a sprint, a coordinated agent team can explore in hours

</div>

</div>

<div class="mt-6" v-click>

**Practical metrics from teams using Claude Code:**
- Large refactors (change 50+ files): hours → minutes
- Writing test coverage for existing code: ~10x faster
- Onboarding to unfamiliar codebases: dramatically reduced ramp time
- Documentation generation: near-zero marginal cost

</div>

---

# Use Cases

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

**Code Tasks**
- Full-feature implementation from specs
- Codebase-wide refactoring
- Automated test generation
- Bug reproduction and fixing
- Code review and quality analysis

**DevOps & Tooling**
- CI/CD pipeline configuration
- Infrastructure-as-code generation
- Monitoring and alerting setup

</v-clicks>

</div>

<div>

<v-clicks>

**Knowledge Work**
- Documentation generation from code
- Architecture decision records (ADRs)
- Onboarding guides and runbooks

**Research & Analysis**
- Exploring and summarizing large codebases
- Dependency audits and security scans
- Performance profiling and optimization suggestions

</v-clicks>

</div>

</div>

<div class="mt-4 p-3 bg-purple-900 rounded" v-click>

**Coming up**: We'll see these in action — starting with a live Claude Code demo
</div>
