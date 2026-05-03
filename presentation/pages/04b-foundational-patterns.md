---
layout: section
---

# Foundational Workflow Patterns
## Phil Schmid's 7 Core Patterns

---

# Pattern Overview

<div class="mt-4">

| Pattern | Type | Complexity | Best For |
|---------|------|-----------|----------|
| **Prompt Chaining** | Workflow | Low | Sequential data transformations |
| **Routing** | Workflow | Low | Classifying and dispatching requests |
| **Parallelization** | Workflow | Medium | Independent concurrent subtasks |
| **Reflection** | Agentic | Medium | Quality improvement through self-critique |
| **Tool Use** | Agentic | Medium | Real-world system interaction |
| **Planning** | Agentic | High | Complex goal decomposition |
| **Multi-Agent** | Agentic | High | Collaborative specialized execution |

</div>

<div class="mt-6 p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-700" v-click>

**Progression**: Patterns build on each other — start simple (chaining), grow to sophisticated (multi-agent) only as your needs require

</div>

---

# Prompt Chaining

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

## How It Works

<v-clicks>

Output of each LLM call becomes the input of the next — a **sequential pipeline** of transformations.

```
Input → [LLM 1] → Output 1
              ↓
       [LLM 2] → Output 2
              ↓
       [LLM 3] → Final Output
```

**Document Generation Example**:

```
User Request
    ↓
[LLM 1] Create outline
    ↓
[LLM 2] Validate structure
    ↓
[LLM 3] Write each section
    ↓
[LLM 4] Format as markdown
    ↓
Final Document
```

</v-clicks>

</div>

<div>

<v-clicks>

## When to Use

- Steps are known upfront
- Each step transforms the previous output
- No branching or decision-making needed
- Clear separation of concerns per stage

## Benefits

- ✅ Easy to debug (inspect intermediate outputs)
- ✅ Reusable pipeline stages
- ✅ Predictable, deterministic behavior
- ✅ Simple to test each stage independently

## Limitation

No autonomous decision-making — if you need branching, use Routing instead

</v-clicks>

</div>

</div>

---

# Routing (Handoff)

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

## How It Works

<v-clicks>

A **classifier LLM** categorizes the input and dispatches it to the appropriate specialist handler.

```
User Request
    ↓
[Classifier LLM]
  ├─ "billing" → Billing Agent
  ├─ "technical" → Tech Support Agent
  └─ "general" → General Agent
```

**Coordinator-Delegate Architecture**:

- `TravelPlannerAgent` (coordinator)
  - Routes to `FlightAgent`
  - Routes to `HotelAgent`
  - Routes to `CarRentalAgent`

Each delegate has specialized tools and domain knowledge

</v-clicks>

</div>

<div>

<v-clicks>

## Benefits

- 💰 Cost optimization — use cheap models for simple tasks, powerful for complex
- ⚡ Latency — fast path for common queries
- 🎯 Quality — specialists outperform generalists in their domain
- 📊 Clean separation of concerns

## Real-World Performance

**85-95% routing accuracy** achievable in production systems

## When to Use

When incoming requests have distinct categories with specialized handlers for each

</v-clicks>

</div>

</div>

---

# Parallelization

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

## How It Works

<v-clicks>

Independent subtasks **execute concurrently** across multiple LLMs. A final aggregator synthesizes all results.

```
           Input
             ↓
    [Decompose/Fan-Out]
   /         |         \
[LLM A]  [LLM B]  [LLM C]
   \         |         /
    [Aggregate/Reduce]
             ↓
        Final Output
```

**NER-Based Parallel Delegation**:

```
"Book flights to Paris and hotel in Rome"
         ↓ [Extract entities]
  ├─ "Paris flights" → FlightAgent
  └─ "Rome hotel"   → HotelAgent
         ↓ [Merge results]
    Combined itinerary
```

</v-clicks>

</div>

<div>

<v-clicks>

## Benefits

- ⚡ Speed — 3 parallel tasks = latency of 1 task
- 🎯 Quality — multiple perspectives synthesized
- 📈 Scale — add workers to increase throughput
- 🔄 Coverage — explore different angles simultaneously

## Key Requirement

Subtasks must be **independent** — no task B depending on task A's output

## RAG Example

```
Complex query
    ↓ Decompose into 3 sub-queries
[Search A] [Search B] [Search C]  ← parallel
    ↓         ↓         ↓
      [Aggregate results]
    ↓
Comprehensive answer
```

</v-clicks>

</div>

</div>

---

# Reflection

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

## Actor-Critic Framework

<v-clicks>

Two roles in a loop: **Actor** generates content, **Critic** reviews it, loop continues until a quality threshold is met.

```
Goal
  ↓
[Actor LLM] → Draft output
                  ↓
          [Critic LLM] → Critique
                  ↓
         Quality threshold met?
           No → back to Actor
          Yes → Final output
```

**Each agent has a distinct system prompt**:
- Actor: *"Generate the best possible implementation"*
- Critic: *"Review for security issues, edge cases, and style"*

</v-clicks>

</div>

<div>

<v-clicks>

## Use Cases

- Code quality improvement (write → review → fix)
- Documentation refinement
- Security vulnerability scanning
- Architecture review
- Test case generation

## Benefits

- ✅ Higher quality without human intervention
- ✅ Consistent standards (Critic is always the same)
- ✅ Self-correcting behavior
- ✅ Reduced human review time

## Limitation

Requires the agent to know what "good" looks like — not ideal for genuinely novel problems

</v-clicks>

</div>

</div>

---

# Tool Use

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

## Function Calling / ACI

<v-clicks>

The agent **selects and invokes tools** based on its current goal, observes results, and adjusts its next action.

```
Goal: "Check if tests pass after my change"
  ↓
Agent decides: call run_tests()
  ↓
Tool executes: npm test
  ↓
Agent observes: 2 failures in auth.test.ts
  ↓
Agent decides: read auth.test.ts, fix failures
  ↓
Tool executes: edit file
  ↓
Agent observes: all tests pass ✓
```

</v-clicks>

</div>

<div>

<v-clicks>

## Tool Definition Best Practices

```python
{
  "name": "search_codebase",
  "description":
    # Detailed: helps agent decide when to call
    "Search repository for function definitions,
     class names, variable declarations, or any
     code pattern. Returns file paths and line numbers.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search term or regex pattern"
      }
    },
    "required": ["query"]
  }
}
```

**Key**: Clear descriptions help the agent decide *when* to use each tool

</v-clicks>

</div>

</div>

---

# Planning

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

## Orchestrator-Workers Pattern

<v-clicks>

An **orchestrator** agent receives a complex goal, decomposes it into subtasks, delegates to **worker** agents, and synthesizes results.

```
Goal: "Add user authentication"
  ↓
[Orchestrator]
  Plans:
  1. Create User model
  2. Implement password hashing
  3. Build login endpoint
  4. Add JWT generation
  5. Create auth middleware
  6. Write tests
  ↓
[Worker 1] Model + schema
[Worker 2] Auth service
[Worker 3] Routes + middleware
[Worker 4] Test suite
  ↓
[Orchestrator] Integrate + verify
```

</v-clicks>

</div>

<div>

<v-clicks>

## Dynamic Decomposition

The most advanced variant — the orchestrator **generates its own subtask list** dynamically based on the goal. No predefined decomposition.

**Static (Predefined)**:
```
Complex task → fixed subtask list
```

**Dynamic (LLM-Generated)**:
```
Complex task → LLM generates subtask list
             → routes each to SubtaskAgent
             → adapts as new info emerges
```

## Benefits

- 📋 Handles open-ended, complex goals
- 🔄 Adapts plan as execution reveals new needs
- ✅ Each subtask is concrete and verifiable
- 🎯 Parallelizable where dependencies allow

</v-clicks>

</div>

</div>

---

# Multi-Agent

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

## Collaborative Specialized Agents

<v-clicks>

Multiple agents with **distinct roles and expertise** collaborate — each handles its domain, with coordination through a central orchestrator or direct handoff.

**Software Team Example**:

```
User Goal: "Ship the feature"
  ↓
[Project Manager Agent]
  Delegates to:
  ├─ [Architect Agent] — Design
  ├─ [Frontend Agent] — UI implementation
  ├─ [Backend Agent]  — API implementation
  ├─ [QA Agent]       — Test suite
  └─ [Reviewer Agent] — Code review
  ↓
[PM Agent] Integrates, resolves conflicts
```

</v-clicks>

</div>

<div>

<v-clicks>

## Coordinator-Delegate in Practice

**Travel Booking System**:
- `TravelCoordinator` receives: *"Plan a trip to Tokyo"*
- Routes to `FlightAgent` → finds flights
- Routes to `HotelAgent` → finds hotels
- Routes to `ActivityAgent` → suggests activities
- Coordinator synthesizes full itinerary

**Communication Patterns**:

| Pattern | Description |
|---------|-------------|
| Central Orchestrator | All agents report to coordinator |
| Peer-to-Peer Handoff | Agent A passes directly to Agent B |
| Shared Message Queue | Agents consume from shared task pool |

## When to Use

When diverse expertise is genuinely needed and tasks benefit from specialization

</v-clicks>

</div>

</div>
