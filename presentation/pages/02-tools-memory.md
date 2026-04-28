# Tools and Memory Fundamentals

---

# What are Tools?

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="dense-col">

<v-clicks>

## Agent-Computer Interface (ACI)

**Definition**: Structured interfaces that extend LLM capabilities beyond text generation by enabling interaction with external systems, APIs, databases, and computational resources.

**How Agents Use Tools**:

<img src="/diagrams/tool-use-pattern.svg" class="w-full mt-2 rounded max-h-40 object-contain" />

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## Tool Categories

**Information Retrieval**
- Search, database queries, API calls

**Computation**
- Math operations, data processing, code execution

**Action Execution**
- File operations, shell commands, external services

**Memory Access**
- Vector store queries, context retrieval, history

</v-clicks>

<div v-click class="mt-4 p-3 bg-orange-900 bg-opacity-30 rounded">

**Key Insight**: Tools transform LLMs into agents — from advisors into actors

</div>

</div>

</div>

---

# What is Memory?

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="dense-col">

<v-clicks>

## Memory Types

**Short-term Memory**
- Conversation context within token limits (~200K tokens for Claude)
- In-context, ephemeral, fast

**Long-term Memory**
- Persistent storage across sessions
- Vector databases, SQL, file systems

**Semantic Memory**
- Embeddings-based retrieval (RAG)
- Query by meaning, not exact match

**Episodic Memory**
- Structured records of past interactions, decisions, outcomes

</v-clicks>

</div>

<div class="dense-col">

<v-clicks>

## Memory Operations

- **Store** — Save information for future retrieval
- **Retrieve** — Query relevant info based on current context
- **Update** — Modify memories as understanding evolves
- **Prune** — Remove outdated or irrelevant information

## Implementation

```python
# Vector (semantic) search
results = vector_store.search(query, k=5)

# SQL (episodic) search
past = db.query(
    "WHERE error_code = '429'")
```

</v-clicks>

</div>

</div>

---

# Tools + Memory in Action

<div class="grid grid-cols-2 gap-6 mt-2 text-sm">

<div>

<v-clicks>

**User**: *"My API calls are returning 429 errors"*

**Step 1 — Tools (Real-time Data)**

```python
await asyncio.gather(
    search_issue_tracker("429 errors"),
    check_rate_limits(user_id),
    fetch_logs(last_hour))
```

**Step 2 — Memory (RAG)**

```python
docs = vector_store.search(
    "rate limit troubleshooting", k=3)
past = db.query(
    "WHERE error_code = '429'")
```

</v-clicks>

</div>

<div v-click>

**Step 3 — Synthesis**

```
Logs:    1,000 req/min (limit: 100/min)
Docs:    Exponential backoff recommended
History: Enterprise tier resolved 429s
```

**Response**: *"You're hitting rate limits. Implement exponential backoff — or upgrade to Enterprise for higher limits."*

<div class="mt-3 p-3 bg-green-900 bg-opacity-30 rounded">

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
