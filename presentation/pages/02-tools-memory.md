---
layout: section-header
---

# Tools & Memory Fundamentals

The building blocks that transform LLMs into agents

<!--
Before diving into patterns, we need to understand the two primitives that make agentic workflows possible.

Tools give agents the ability to interact with the world — file systems, APIs, databases, shell commands.
Memory gives agents persistence and context — short-term in-context, long-term via vector stores and databases.

Together, they're what separates an LLM from an agent.

Duration: 5-7 minutes
-->

---

# What are Tools?

<div class="mt-4 text-sm">

## Tool Categories

<v-clicks>

**Information Retrieval** — Search, database queries, API calls

**Computation** — Math operations, data processing, code execution

**Action Execution** — File operations, shell commands, external services

**Memory Access** — Vector store queries, context retrieval, history

</v-clicks>

<div v-click class="mt-4 p-2 bg-orange-900 bg-opacity-30 rounded">

**Key Insight**: Tools transform LLMs into agents — from advisors into actors

</div>

</div>

<!--
## Agent-Computer Interface (ACI)

**Definition**: Structured interfaces that extend LLM capabilities beyond text generation by enabling interaction with external systems, APIs, databases, and computational resources.

Tools are the ACI — the layer through which an agent perceives and acts on the world. Just as a GUI is a Human-Computer Interface, the ACI defines how an agent reads inputs (tool results) and writes outputs (tool calls).

The agent sends a structured tool call → the environment executes it → the result is returned as an observation → the agent decides the next action.
-->

---

# What is Memory? — Types

<div class="mt-4 text-sm">

<v-clicks>

## Memory Types

**Short-term** — Conversation context within token limits (~200K tokens), ephemeral and fast

**Long-term** — Persistent storage across sessions via vector DBs, SQL, file systems

**Semantic** — Embeddings-based retrieval (RAG); query by meaning, not exact match

**Episodic** — Structured records of past interactions, decisions, and outcomes

</v-clicks>

</div>

---

# What is Memory? — Operations

<div class="mt-4 text-sm">

<v-clicks>

## Memory Operations

- **Store** — Save information for future retrieval
- **Retrieve** — Query relevant info based on current context
- **Update** — Modify memories as understanding evolves
- **Prune** — Remove outdated or irrelevant information

</v-clicks>

</div>

---

# Tools + Memory in Action

<div class="grid grid-cols-2 gap-4 mt-1 text-sm">

<div>

<div v-click class="mb-2">

**User**: *"My API calls are returning 429 errors"*

</div>

<div v-click>

**Step 1 — Tools (Real-time Data)**

```python
await asyncio.gather(
    search_issue_tracker("429 errors"),
    check_rate_limits(user_id),
    fetch_logs(last_hour))
```

</div>

<div v-click class="mt-2">

**Step 2 — Memory (RAG)**

```python
docs = vector_store.search(
    "rate limit troubleshooting", k=3)
past = db.query(
    "WHERE error_code = '429'")
```

</div>

</div>

<div v-click>

**Step 3 — Synthesis**

```
Logs:    1,000 req/min (limit: 100/min)
Docs:    Exponential backoff recommended
History: Enterprise tier resolved 429s
```

**Response**: *"You're hitting rate limits. Implement exponential backoff — or upgrade to Enterprise for higher limits."*

<div class="mt-2 p-2 bg-green-900 bg-opacity-30 rounded">

**Result**: Full context in one turn — no back-and-forth, faster resolution

</div>

</div>

</div>

---

# Why This Matters

<div class="grid grid-cols-3 gap-4 mt-6">

<div class="p-4 bg-gray-800 rounded-lg text-center" v-click>

### Without Tools
LLM can only generate text from **training knowledge**

Static, outdated, unable to act on real systems

</div>

<div class="p-4 bg-gray-800 rounded-lg text-center" v-click>

### Without Memory
Agent repeats the same mistakes, lacks personalization, loses context between sessions

</div>

<div class="p-4 bg-orange-900 bg-opacity-40 rounded-lg text-center" v-click>

### Tools + Memory
Powerful, context-aware, action-capable agents that **learn** and **act**

</div>

</div>

<div class="mt-8" v-click>

## The Building Block Principle

> *Tools give agents **hands**. Memory gives agents **experience**. Together they enable agents to tackle real-world complexity.*

</div>

<div class="mt-4 p-3 bg-blue-900 bg-opacity-30 rounded" v-click>

**Up next**: How these primitives combine into **workflow patterns** and **multi-agent architectures**

</div>
