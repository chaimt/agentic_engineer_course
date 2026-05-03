---

# Transparent Planning

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="dense-col">

<v-clicks>

## Show the Agent's Reasoning

**Extended Thinking** lets agents reason through problems before acting — exposing that reasoning builds trust and enables debugging.

```python
response = client.messages.create(
    model="claude-opus-4-5",
    thinking={"type": "enabled",
              "budget_tokens": 10000},
    messages=[{"role": "user",
        "content": "Refactor for testability"}]
)
# Agent thinks before acting...
```

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## ACI Best Practices

**Tool Descriptions Matter**:

```python
# Bad: agent guesses when to use it
{"name": "search", "description": "Search things"}

# Good: agent knows exactly when to call it
{"name": "search_codebase",
 "description": "Find function/class definitions.
   Use to locate symbols or find usages.
   Returns: file paths and line numbers."}
```

**Structured Outputs**: Return JSON with typed fields so the agent can reliably parse results

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

<div class="dense-col">

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

<div class="grid grid-cols-3 gap-4 mt-3">

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
      "hooks": [{"type": "command",
        "command": "npm run lint -- $FILE"}]
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

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

<v-clicks>

## Shared Standards

**CLAUDE.md as Team Contract**

Check `CLAUDE.md` into version control. Every team member's agent sessions run with the same context — consistent output across the team.

```bash
# Everyone gets the same agent behavior
git clone repo && cd repo
claude  # reads shared CLAUDE.md automatically
```

**Spec-Driven Alignment**

Tasks defined in `specs/` before execution means all agents work from the same source of truth.

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## Shifting Human Roles

| Old Role | New Role |
|----------|----------|
| Writing boilerplate code | Writing clear specifications |
| Implementing features line-by-line | Reviewing agent-generated implementations |
| Running tests manually | Designing test strategies |
| Fixing linting errors | Configuring hooks to auto-fix |
| Explaining codebase to new hires | Maintaining CLAUDE.md as living docs |

## The Review Mindset

The most important skill shift: **from author to reviewer**

Review agent output like a PR — check logic, edge cases, security — but you didn't write the first draft.

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

<div class="dense-col">

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
