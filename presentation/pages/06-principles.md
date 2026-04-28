# Building Effective Agents

---
layout: section
---

# Anthropic's Agent Principles
## Building Effective Agents Guidance

---

# Simplicity Over Complexity

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

## Start With the Simplest Thing That Works

Anthropic's core recommendation: **don't build multi-agent systems until a single agent demonstrably fails at your task.**

**Complexity Ladder** — stop as soon as your task is solved:

1. Plain LLM call (no tools)
2. Single agent + tools
3. Single agent + MCP + tools
4. Sequential agents
5. Hierarchical multi-agent
6. Hierarchy + parallel + RAG

</v-clicks>

</div>

<div>

<v-clicks>

## Why Simplicity Wins

Each layer of added complexity:
- Increases latency (coordination overhead)
- Increases cost (more tokens, more calls)
- Increases failure surface (more moving parts)
- Decreases debuggability

## Measured Improvements from Anthropic

- Adding MCP: **37% speed improvement** → justified
- Adding parallelism: **30-60% time reduction** → justified for large tasks
- Adding reflection: **Measurably higher quality** → justified when quality is critical

**Only add a pattern when you have a number that justifies the tradeoff.**

</v-clicks>

<div v-click class="mt-4 p-3 bg-orange-900 bg-opacity-30 rounded">

*"The best agent architecture is the simplest one that solves your problem reliably."*

</div>

</div>

</div>

---

# Transparent Planning

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

## Show the Agent's Reasoning

**Extended Thinking** allows agents to reason through problems before acting — and exposing that reasoning builds trust and enables debugging.

```python
response = client.messages.create(
    model="claude-opus-4-5",
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    messages=[{
        "role": "user",
        "content": "Refactor this module for testability"
    }]
)

# Agent shows reasoning before acting:
# "I need to identify dependencies, extract
#  interfaces, apply dependency injection..."
```

</v-clicks>

</div>

<div>

<v-clicks>

## ACI Best Practices

**Tool Descriptions Matter**:

```python
# Bad — agent guesses when to use it
{"name": "search", "description": "Search things"}

# Good — agent knows exactly when to call it
{
  "name": "search_codebase",
  "description":
    "Search the repository for function definitions,
     class declarations, or import statements.
     Use when you need to locate where a symbol
     is defined or find all usages of a pattern.
     Returns: file paths and line numbers.",
}
```

**Structured Outputs**: Return JSON with typed fields so the agent can reliably parse and use results

**Error Messages**: Include context — `"File not found: auth/jwt.ts"` not just `"Error 404"`

</v-clicks>

</div>

</div>

---

# When to Build Agents

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

## Good Candidates for Agents

Tasks that are genuinely hard to automate with simple scripts but **well-suited for agentic execution**:

- **Predictable subtasks** — goal can be decomposed into concrete, verifiable steps
- **Parallel opportunities** — independent subtasks exist and speed matters
- **Multiple domains** — task spans frontend, backend, infra, testing simultaneously
- **Iteration required** — output quality can be measured and needs refinement
- **Tedious but well-defined** — tasks you understand but don't want to execute manually

</v-clicks>

</div>

<div>

<v-clicks>

## Poor Candidates

Tasks where agents underperform simple alternatives:

| Avoid Agents When... | Use Instead |
|---------------------|-------------|
| Single-step, no tool use needed | Direct LLM call |
| Fully deterministic, no judgment | Conventional script |
| Novel algorithm invention required | Human expert |
| Requirements are deeply ambiguous | Clarify first, then agent |
| High-security, no room for error | Human with AI assist |

</v-clicks>

<div v-click class="mt-4 p-3 bg-blue-900 bg-opacity-30 rounded">

**Decision heuristic**: If you can write a script for it, write the script. If the script would require too much conditional logic and judgment, use an agent.

</div>

</div>

</div>

---
layout: section
---

# Practical Tips

---

# Getting Started

<div class="mt-4">

## 5-Step Adoption Path

</div>

<div class="grid grid-cols-5 gap-2 mt-3 text-xs">

<div class="p-2 bg-gray-800 rounded-lg text-center" v-click>

**Step 1**

Install Claude Code

```bash
npm install -g \
  @anthropic-ai/claude-code
```

</div>

<div class="p-2 bg-gray-800 rounded-lg text-center" v-click>

**Step 2**

Add `CLAUDE.md` to your project

Stack, commands, conventions, constraints

</div>

<div class="p-2 bg-gray-800 rounded-lg text-center" v-click>

**Step 3**

Run a **bounded task**

Concrete with clear success criteria

</div>

<div class="p-2 bg-gray-800 rounded-lg text-center" v-click>

**Step 4**

**Review** the output

Build intuition for what the agent does well

</div>

<div class="p-2 bg-gray-800 rounded-lg text-center" v-click>

**Step 5**

**Expand scope** gradually

Add hooks, MCP servers, larger tasks

</div>

</div>

<div class="mt-3 text-sm" v-click>

**Good first tasks**: Add tests to existing functions · Rename a symbol across the codebase · Generate API docs · Fix a linting category

</div>

<div class="mt-2 p-2 bg-orange-900 bg-opacity-30 rounded text-sm" v-click>

**The trust curve**: New users auto-approve ~20% of actions. Experienced users reach 40%+. Trust is earned through experience.

</div>

---

# Common Challenges & Solutions

<div class="mt-2 text-sm">

| Challenge | Solution |
|-----------|----------|
| **Inconsistent output quality** — varying results across runs | Add `CLAUDE.md` with explicit coding standards and patterns. Encode what "good" looks like. |
| **Trust and verification** — hard to know when to trust output | Start with bounded tasks with automated tests. Use hooks for quality gates (lint, security scan). |
| **Context loss between sessions** — agent forgets decisions | Write specs before running the agent. Specs preserve rationale and become persistent memory. |
| **Security concerns** — unsure what the agent can access | Review tool permissions explicitly. Start read-only, add writes incrementally. |
| **Team coordination** — different engineers get different results | Check `CLAUDE.md` into the repo. Use spec-driven workflows so all agents share the same context. |

</div>

---

# Best Practices

<div class="grid grid-cols-3 gap-4 mt-6">

<div class="p-4 bg-gray-800 rounded-lg" v-click>

### CLAUDE.md

Your project's contract with the agent

- Tech stack and versions
- Test and lint commands
- Coding conventions
- Explicit "Do NOT" list
- Keep under 200 lines

</div>

<div class="p-4 bg-gray-800 rounded-lg" v-click>

### Hooks

Automated quality gates

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "npm run lint -- $FILE"
      }]
    }]
  }
}
```

Every file edit → auto-linted

</div>

<div class="p-4 bg-gray-800 rounded-lg" v-click>

### Spec-Driven Workflows

Write the spec first

```
specs/feature-name/
  ├── plan.md      ← architecture
  ├── tasks.md     ← task breakdown
  └── research.md  ← decisions + rationale
```

The spec becomes the agent's persistent memory and the team's shared understanding

</div>

</div>

<div class="mt-4 p-3 bg-green-900 bg-opacity-30 rounded" v-click>

**Core discipline**: The agent executes — you design. Your job shifts from writing code to writing clear specifications and reviewing outcomes.

</div>

---

# Team Coordination

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

## Shared Standards

**CLAUDE.md as Team Contract**

Check `CLAUDE.md` into version control. Every team member's agent sessions run with the same context — consistent output across the team.

```bash
# Everyone gets the same agent behavior
git clone repo
cd repo
claude  # reads shared CLAUDE.md automatically
```

**Spec-Driven Alignment**

Tasks defined in `specs/` before execution means all agents work from the same source of truth — no "it worked on my machine" for agent output.

</v-clicks>

</div>

<div>

<v-clicks>

## Shifting Human Roles

| Old Role | New Role |
|----------|----------|
| Writing boilerplate code | Writing clear specifications |
| Implementing features line-by-line | Reviewing agent-generated implementations |
| Running tests manually | Designing test strategies |
| Fixing linting errors | Configuring hooks to auto-fix |
| Explaining codebase to new hires | Maintaining CLAUDE.md as living documentation |

## The Review Mindset

The most important skill shift: **from author to reviewer**

Review agent output like a PR — check logic, check edge cases, check security — but you didn't have to write the first draft.

</v-clicks>

</div>

</div>

---
layout: section
---

# Q&A and Resources

---

# Questions?

<div class="mt-12 text-center">

## What would you like to explore further?

</div>

<div class="grid grid-cols-3 gap-4 mt-8">

<div class="p-4 bg-gray-800 rounded-lg text-center" v-click>

### Concepts
Agentic workflows, tools, memory, mental model shifts

</div>

<div class="p-4 bg-gray-800 rounded-lg text-center" v-click>

### Patterns
Specific workflow patterns, architecture selection, framework choices

</div>

<div class="p-4 bg-gray-800 rounded-lg text-center" v-click>

### Adoption
Getting started, team rollout, security, measuring impact

</div>

</div>

---

# Resources

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

## Primary References

- **[Agentic Workflow Patterns](https://www.philschmid.de/agentic-pattern)**  
  Philipp Schmid — foundational taxonomy (Prompt Chaining, Routing, Parallelization, Reflection, Tool Use, Planning, Multi-Agent)

- **[Agentic Workflow Patterns — GitHub](https://github.com/arunpshankar/Agentic-Workflow-Patterns)**  
  arunpshankar — Python reference implementations (Reflection, Web Access, Semantic Routing, Parallel Delegation, Dynamic Sharding, DAG Orchestration)

- **[The Ultimate Guide to AI Agent Architectures in 2025](https://dev.to/sohail-akbar/the-ultimate-guide-to-ai-agent-architectures-in-2025-2j1c)**  
  Dev.to — 8 modern architectural compositions with performance benchmarks

</div>

<div>

## Tools & Docs

- **[Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code)** — CLAUDE.md, hooks, MCP setup
- **[Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)** — Core principles
- **[LangGraph Docs](https://langchain-ai.github.io/langgraph/)** — Stateful multi-agent workflows
- **[AutoGen](https://microsoft.github.io/autogen/)** — Microsoft's multi-agent framework
- **[CrewAI](https://www.crewai.com/)** — Role-based agent teams
- **[MCP Protocol](https://modelcontextprotocol.io/)** — Universal tool adapter standard

## Start Here

```bash
npm install -g @anthropic-ai/claude-code
claude  # in your project directory
```

</div>

</div>

---
layout: end
---

# Thank You!
## Let's Build Agentic Workflows Together
