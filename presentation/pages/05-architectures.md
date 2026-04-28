# Modern Architecture Patterns

---
layout: section
---

# Modern Architecture Patterns
## 8 Architectural Compositions (2025 Guide)

---

# Architecture Overview

<div class="mt-3 text-sm">

| # | Architecture | Key Metric | Best For |
|---|-------------|-----------|----------|
| 1 | **Single Agent + Tools (ReAct)** | Baseline | Simple tool-calling tasks |
| 2 | **Sequential Agents** | +15-25% completion | Multi-stage pipelines |
| 3 | **Single Agent + MCP + Tools** | 37% faster, 93% completion | External service integration |
| 4 | **Hierarchy + Parallel + Shared Tools** | 30-60% time reduction | Large parallel workloads |
| 5 | **Single Agent + Router** | 85-95% routing accuracy | Diverse request handling |
| 6 | **Human in the Loop** | 50-80% error reduction | High-stakes decisions |
| 7 | **Dynamic Agent Delegation** | Adaptive scaling | Open-ended complex tasks |
| 8 | **Hierarchy + Loop + Parallel + RAG** | Production-grade | Enterprise-scale workflows |

</div>

<div class="mt-3 p-2 bg-orange-900 bg-opacity-30 rounded" v-click>

**Principle**: Start with #1, add complexity only when benchmarks justify it

</div>

---

# Single Agent + Tools (ReAct)

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

## ReAct: Reason + Act Loop

<v-clicks>

The foundational architecture — a single agent reasons about what to do, acts via tools, observes results, and loops.

```
Goal
  ↓
[Reason] What do I need?
  ↓
[Act]    Call tool
  ↓
[Observe] Read result
  ↓
Goal achieved? No → back to Reason
              Yes → Return result
```

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## When to Use

- Well-scoped tasks with clear success criteria
- Tool calls are sequential (each depends on previous)
- Single domain of expertise required
- Baseline for measuring more complex architectures

## Strengths

- ✅ Simple to implement and debug
- ✅ Low latency (no coordination overhead)
- ✅ Easy to monitor and trace
- ✅ Solid foundation to build on

*Limitation: Context window fills quickly on long tasks; no parallel execution.*

</v-clicks>

</div>

</div>

---

# Sequential Agents

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

## Agent Pipeline with Handoff

<v-clicks>

Multiple specialized agents execute in sequence — each one receives the previous agent's output as context and builds on it.

```
Goal
  ↓
[Agent 1: Planner]
  Creates: task list + architecture
  ↓ (passes full context)
[Agent 2: Implementer]
  Creates: code based on plan
  ↓ (passes code + plan)
[Agent 3: Tester]
  Creates: test suite, runs tests
  ↓ (passes all context)
[Agent 4: Reviewer]
  Final: review + approval
```

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## Performance

**+15-25% higher task completion rate** vs single agent on complex tasks

**Why**: Each agent has a focused context — the planner's context isn't polluted with implementation details when reviewing

## Benefits

- 🎯 Each agent has clean, focused context
- 🔍 Easier to debug (inspect output at each stage)
- ♻️ Reuse stages across different workflows
- 📈 Higher completion on multi-phase tasks

*Best for: Multi-stage workflows where each phase requires different expertise*

</v-clicks>

</div>

</div>

---

# Single Agent + MCP + Tools

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

## MCP: Universal Tool Adapter

<v-clicks>

**Model Context Protocol** standardizes how agents connect to external services — write once, connect anywhere.

```
Agent
  ├─ MCP: GitHub server
  │    → read PRs, issues, code
  ├─ MCP: Sentry server
  │    → fetch errors, stack traces
  ├─ MCP: Database server
  │    → query, write data
  └─ MCP: Slack server
       → read channels, send messages
```

Without MCP: Custom integration for every tool
With MCP: Standard protocol, any compatible server

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## Performance Benchmarks

<div class="grid grid-cols-2 gap-4">

<div class="p-3 bg-gray-800 rounded text-center">

### Speed
**37% faster** task completion vs basic agent

</div>

<div class="p-3 bg-gray-800 rounded text-center">

### Completion
**93% task completion** rate on complex workflows

</div>

</div>

## Why the Improvement?

Agent has **real-time access** to live system state — no hallucinated context, no stale assumptions.

Instead of: *"The error might be in the auth service"*

With MCP: *reads actual Sentry error* → *"Error is on line 47 of auth/jwt.ts: token expired"*

*Best for: Any task requiring live data from external systems (GitHub, monitoring, databases)*

</v-clicks>

</div>

</div>

---

# Hierarchy + Parallel + Shared Tools

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

## Coordinated Parallel Architecture

<v-clicks>

A coordinator agent dispatches independent subtasks to multiple worker agents running in **parallel**, all sharing a common tool pool.

```
[Coordinator Agent]
  Analyzes goal, creates work units
  Dispatches to worker pool:
    ↓           ↓           ↓
[Worker A]  [Worker B]  [Worker C]
 Frontend    Backend     Tests
    ↓           ↓           ↓
  Result      Result      Result
         ↓
  [Coordinator] Merges results
```

All workers access **shared tools**: file system, test runner, linter

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## Performance

**30-60% time reduction** on parallelizable tasks

## Key Design Decisions

**Shared Tool Pool**: Workers read/write to the same file system — coordinator manages conflicts

**Work Unit Granularity**: Too coarse → under-utilization; too fine → coordination overhead dominates

**Dependency Tracking**: Coordinator must know which work units can run in parallel vs which must sequence

*Best for: Large tasks with genuinely independent subtasks — full-stack features, migrations*

</v-clicks>

</div>

</div>

---

# Single Agent + Router

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

## Intelligent Request Dispatch

<v-clicks>

A lightweight **classifier** sits in front of specialized handler agents. Routes based on intent, complexity, or domain.

```
Incoming Request
      ↓
[Router / Classifier LLM]
  Determines:
  - Category (billing / tech / general)
  - Complexity (simple / complex)
  - Domain (frontend / backend / infra)
      ↓
  ├─ Simple query → Small fast model
  ├─ Complex query → Advanced model
  ├─ Billing issue → Billing specialist
  └─ Tech support → Tech specialist
```

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## Performance

**85-95% routing accuracy** in production deployments

## Optimization Dimensions

| Dimension | Routing Strategy |
|-----------|-----------------|
| **Cost** | Simple → cheap model, Complex → advanced |
| **Speed** | High-frequency → cached responses |
| **Quality** | Domain-specific → specialist agent |
| **Safety** | Sensitive → human-reviewed path |

*Best for: Diverse request types — customer support, code assistants, multi-domain Q&A*

</v-clicks>

</div>

</div>

---

# Human in the Loop

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

## Checkpoint-Based Oversight

<v-clicks>

Strategic pause points where human judgment is **required** before the agent continues — a deliberate design, not just a safety net.

```
Agent executes autonomously
         ↓
[CHECKPOINT: High-stakes decision]
         ↓
Human: Approve / Reject / Modify
         ↓
Agent continues with human direction
```

**Insert checkpoints**:
- Before irreversible actions (deletes, deploys)
- After complex decisions (architecture choices)
- When regulations require human sign-off

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## Performance

**50-80% error reduction** on high-stakes workflows

## Checkpoint Spectrum

```
← Fully Autonomous · · · Fully Manual →
  Fast, risky           Slow, safe

Sweet spot: checkpoint critical decisions
```

## Adoption Trust Curve

- New users: ~20% auto-approve agent actions
- Experienced users: 40%+ auto-approve
- Trust grows as engineers learn agent strengths

*Best for: Legal, financial, security, production deployments*

</v-clicks>

</div>

</div>

---

# Dynamic Agent Delegation

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

## Hub-Spoke Orchestration

<v-clicks>

A central **orchestrator** (hub) dynamically **spawns specialized sub-agents** (spokes) on demand based on what the task requires — not a predefined team, but on-the-fly delegation.

```
[Orchestrator Hub]
  Receives complex goal
  Analyzes what's needed
  Spawns agents dynamically:
    → SpawnAgent("SecurityReviewer")
    → SpawnAgent("PerformanceAnalyzer")
    → SpawnAgent("DocumentationWriter")
  Collects and integrates results
  Spawns more agents if gaps found
```

The orchestrator can spawn agents at any point — **adaptive to what it discovers**

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## vs. Static Multi-Agent

| Static | Dynamic |
|--------|---------|
| Team defined upfront | Agents spawned on demand |
| Fixed specializations | Task-shaped specializations |
| Predictable cost | Variable cost (scales) |
| Lower overhead | Higher flexibility |

## Benefits

- 🔄 Adapts to unknown complexity
- 🎯 Only spawns agents actually needed
- 📈 Scales with task scope automatically
- 🛠️ Handles open-ended research tasks

*Best for: Complex research, exploratory debugging, unknown-scope migrations*

</v-clicks>

</div>

</div>

---

# Hierarchy + Loop + Parallel + RAG

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

## The Production-Grade Architecture

<v-clicks>

Combines all major patterns into a single sophisticated system — the architecture of choice for enterprise-scale agentic workflows.

```
[Orchestrator]
  │
  ├─ [Coordinator A] → [Workers in parallel]
  │     ↕ feedback loop
  ├─ [Coordinator B] → [Workers in parallel]
  │     ↕ feedback loop
  │
  └─ [RAG Memory Layer]
       ├─ Vector store (semantic search)
       ├─ Structured DB (structured queries)
       └─ Conversation history
```

Each coordinator runs a feedback loop until quality threshold is met, then passes results up

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## Component Roles

| Component | Role |
|-----------|------|
| **Hierarchy** | Coordinators delegate to workers |
| **Loop** | Feedback cycles until quality met |
| **Parallel** | Workers execute concurrently |
| **RAG** | Context from long-term knowledge |

## When to Use

- Enterprise workflows with diverse subtasks
- Tasks requiring domain knowledge + fresh data
- Systems where quality must be verifiably met
- Production systems where reliability matters

*Only reach for this when simpler patterns demonstrably fail — each added layer adds cost and complexity*

</v-clicks>

</div>

</div>

---

# Framework Comparison

<div class="mt-2 text-xs">

| Framework | Model | Strengths | Best For |
|-----------|-------|-----------|----------|
| **LangChain** | Flexible chains | Huge ecosystem, many integrations | Rapid prototyping, chain-based workflows |
| **LangGraph** | Stateful DAGs | Cyclical graphs, explicit state management | Complex agentic loops, production workflows |
| **AutoGen** | Multi-agent conversations | Agent-to-agent dialogue, easy role definition | Collaborative multi-agent systems |
| **CrewAI** | Role-based teams | Human-readable team definitions, task delegation | Team simulation, hierarchical workflows |

</div>

<div class="grid grid-cols-2 gap-6 mt-2 dense-col">

<div v-click>

### When Each Shines

- **LangChain**: Prototype fast with many pre-built components
- **LangGraph**: Precise control over state transitions and conditional loops

</div>

<div v-click>

- **AutoGen**: Workflow maps to agents conversing and negotiating
- **CrewAI**: Think in terms of roles, responsibilities, and team workflows

</div>

</div>

<div class="mt-2 p-2 bg-orange-900 bg-opacity-30 rounded text-sm" v-click>

**Recommendation**: Start with Claude Code (no framework needed for many tasks) → LangGraph for complex stateful workflows

</div>

---

# Architecture Selection Guide

<div class="mt-3">

Use these 5 criteria to select the right architecture:

</div>

<div class="grid grid-cols-2 gap-6 mt-2">

<div class="dense-col">

<v-clicks>

### 1. Task Complexity
- Simple, single-domain → **Single Agent + Tools**
- Multi-phase, multi-domain → **Sequential or Hierarchical**

### 2. Parallelism Available
- Tasks are independent → **Parallel workers**
- Tasks are sequential → **Sequential agents or single agent**

### 3. Human Oversight Required
- High-stakes, irreversible → **Human in the Loop**
- Routine, verifiable → **Fully autonomous**

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

### 4. Domain Expertise Needed
- Single domain → **Generalist agent**
- Multiple domains → **Routing or Multi-Agent**

### 5. Iteration Requirements
- First-pass accuracy acceptable → **No feedback loop**
- Quality must be verified → **Reflection / Feedback Loop**

</v-clicks>

<div v-click class="mt-4 p-3 bg-green-900 bg-opacity-30 rounded">

**Decision Rule**: Choose the **simplest architecture** that meets your requirements — add complexity only when you have a measured reason to do so

</div>

</div>

</div>
