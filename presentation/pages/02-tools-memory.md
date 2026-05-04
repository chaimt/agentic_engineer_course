---
layout: section-header
sectionTitle: "Tools & Memory"
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

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🔍</div>
<div class="text-lg font-bold text-orange-300">Information Retrieval</div>
<div class="text-sm mt-1 opacity-80">Search, database queries, API calls</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">⚡</div>
<div class="text-lg font-bold text-orange-300">Computation</div>
<div class="text-sm mt-1 opacity-80">Math operations, data processing, code execution</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🚀</div>
<div class="text-lg font-bold text-orange-300">Action Execution</div>
<div class="text-sm mt-1 opacity-80">File operations, shell commands, external services</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🗄️</div>
<div class="text-lg font-bold text-orange-300">Memory Access</div>
<div class="text-sm mt-1 opacity-80">Vector store queries, context retrieval, history</div>
</div>

</div>

<div v-click class="mt-4 p-4 bg-orange-900 bg-opacity-50 rounded-xl border border-orange-500 text-center">
<div class="text-base font-bold text-orange-200">Tools transform LLMs into agents — from advisors into actors</div>
</div>

<!--
## Agent-Computer Interface (ACI)

**Definition**: Structured interfaces that extend LLM capabilities beyond text generation by enabling interaction with external systems, APIs, databases, and computational resources.

Tools are the ACI — the layer through which an agent perceives and acts on the world. Just as a GUI is a Human-Computer Interface, the ACI defines how an agent reads inputs (tool results) and writes outputs (tool calls).

The agent sends a structured tool call → the environment executes it → the result is returned as an observation → the agent decides the next action.
-->

---

# What is Memory? — Types

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">⚡</div>
<div class="text-lg font-bold text-orange-300">Short-term</div>
<div class="text-sm mt-1 opacity-80">Conversation context within token limits (~200K tokens), ephemeral and fast</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">📚</div>
<div class="text-lg font-bold text-orange-300">Long-term</div>
<div class="text-sm mt-1 opacity-80">Persistent storage across sessions via vector DBs, SQL, file systems</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🔍</div>
<div class="text-lg font-bold text-orange-300">Semantic</div>
<div class="text-sm mt-1 opacity-80">Embeddings-based retrieval (RAG); query by meaning, not exact match</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">📋</div>
<div class="text-lg font-bold text-orange-300">Episodic</div>
<div class="text-sm mt-1 opacity-80">Structured records of past interactions, decisions, and outcomes</div>
</div>

</div>

---

# What is Memory? — Operations

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">💾</div>
<div class="text-lg font-bold text-orange-300">Store</div>
<div class="text-sm mt-1 opacity-80">Save information for future retrieval</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🔍</div>
<div class="text-lg font-bold text-orange-300">Retrieve</div>
<div class="text-sm mt-1 opacity-80">Query relevant info based on current context</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🔄</div>
<div class="text-lg font-bold text-orange-300">Update</div>
<div class="text-sm mt-1 opacity-80">Modify memories as understanding evolves</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">✂️</div>
<div class="text-lg font-bold text-orange-300">Prune</div>
<div class="text-sm mt-1 opacity-80">Remove outdated or irrelevant information</div>
</div>

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

<div class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center" v-click>
<div class="text-3xl mb-2">📝</div>
<div class="text-lg font-bold text-orange-300 mb-2">Without Tools</div>
LLM can only generate text from **training knowledge**

Static, outdated, unable to act on real systems

</div>

<div class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center" v-click>
<div class="text-3xl mb-2">🌪️</div>
<div class="text-lg font-bold text-orange-300 mb-2">Without Memory</div>
Agent repeats the same mistakes, lacks personalization, loses context between sessions

</div>

<div class="p-4 bg-orange-900 bg-opacity-50 rounded-xl border border-orange-500 text-center" v-click>
<div class="text-3xl mb-2">🤖</div>
<div class="text-lg font-bold text-orange-200 mb-2">Tools + Memory</div>
Powerful, context-aware, action-capable agents that **learn** and **act**

</div>

</div>

<div class="mt-8" v-click>

## The Building Block Principle

> *Tools give agents **hands**. Memory gives agents **experience**. Together they enable agents to tackle real-world complexity.*

</div>

<div class="mt-4 p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-700" v-click>

**Up next**: How these primitives combine into **workflow patterns** and **multi-agent architectures**

</div>
