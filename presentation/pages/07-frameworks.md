---
layout: section
---

# Agentic Frameworks
## Choosing the right Python framework for your agent stack

<!--
Now that we've covered the patterns and which models suit each pattern,
the natural next question is: which framework do I reach for when I sit
down to write code? This section compares the four most relevant Python
agent frameworks in 2026 — CrewAI, Pydantic AI, LangGraph, and Agno.
-->

---
layout: default
---

# Framework Landscape

<div class="mt-2 text-sm">

| Framework | Core Abstraction | State Model | Killer Feature | Best For |
|-----------|-----------------|-------------|----------------|----------|
| **CrewAI** | Crew of Agents | Implicit task handoff | Role / goal / backstory framing | Team-style multi-agent simulations |
| **Pydantic AI** | Typed `Agent` | Pydantic deps + output schema | End-to-end type safety | Production pipelines, validated I/O |
| **LangGraph** | `StateGraph` (DAG) | Explicit shared state | Loops, branching, checkpointing | Long-running stateful workflows |
| **Agno** | `Agent` / `Team` | Built-in memory + knowledge base | Speed + multi-modal + RAG batteries | Fast prototypes, voice / vision agents |

</div>

<div class="mt-3 p-3 bg-orange-900 bg-opacity-20 rounded text-sm" v-click>

**Selection rule of thumb**: pick the framework whose **core abstraction** matches how you already think about the problem — *roles* (CrewAI), *types* (Pydantic AI), *graphs* (LangGraph), or *batteries-included agents* (Agno).

</div>

<!--
Each of these frameworks solves the same underlying problem (orchestrate
LLM calls + tools) but they differ sharply in their primary abstraction.

CrewAI thinks in terms of human teams: roles, goals, backstories, tasks.
Pydantic AI thinks in terms of typed contracts at every boundary.
LangGraph thinks in terms of explicit state machines and graphs.
Agno thinks in terms of a single rich Agent object with memory, knowledge,
and tools wired in by default.

The right pick is usually whichever framework's abstraction matches how
you already model the problem mentally.
-->

---
layout: default
---

# Pros & Cons at a Glance (1/2)

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="p-5 bg-orange-950 bg-opacity-40 border border-orange-900 border-opacity-30 rounded-lg dense-col" v-click>

### CrewAI

**Pros**
- Intuitive role-based mental model
- Fast to scaffold a multi-agent workflow
- Strong community + recipes for common crews

**Cons**
- Implicit handoffs harder to debug at scale
- Less control over execution graph

</div>

<div class="p-5 bg-orange-950 bg-opacity-40 border border-orange-900 border-opacity-30 rounded-lg dense-col" v-click>

### Pydantic AI

**Pros**
- Type-safe deps, tools, and outputs
- Excellent IDE / static analysis support
- Clean dependency injection per run

**Cons**
- Smaller ecosystem of pre-built integrations
- Schema-first style adds upfront friction

</div>

</div>

<!--
CrewAI optimises developer ergonomics for team-style problems.
Pydantic AI optimises correctness and refactor-ability.
-->

---
layout: default
---

# Pros & Cons at a Glance (2/2)

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="p-5 bg-orange-950 bg-opacity-40 border border-orange-900 border-opacity-30 rounded-lg dense-col" v-click>

### LangGraph

**Pros**
- Explicit state, loops, and branching
- First-class checkpointing + time-travel
- Production-grade observability via LangSmith

**Cons**
- Steeper learning curve (graph + state design)
- More boilerplate for simple linear flows

</div>

<div class="p-5 bg-orange-950 bg-opacity-40 border border-orange-900 border-opacity-30 rounded-lg dense-col" v-click>

### Agno

**Pros**
- Very fast agent instantiation
- Memory, knowledge, and reasoning built-in
- Multi-modal (text / image / audio) out of the box

**Cons**
- Younger ecosystem, fewer reference architectures
- Opinionated defaults can be hard to override

</div>

</div>

<!--
LangGraph optimises control and observability for complex stateful
workflows. Agno optimises speed-to-running-agent and built-in features.
None of these are "best" in the absolute sense — each excels along a
different axis.
-->

---
layout: default
zoom: 0.85
---

# CrewAI — Role-Based Teams

<div class="grid grid-cols-2 gap-4 mt-2">

<div class="dense-col">

## When to Use

<v-clicks>

- You think of the workflow as a **team of specialists** with distinct roles
- You want **agent-to-agent task delegation** with minimal wiring
- You need **sequential or hierarchical** processes more than arbitrary graphs

## Key Concepts

- **Agent** — `role`, `goal`, `backstory`, `llm`, `tools`
- **Task** — a unit of work assigned to an agent
- **Crew** — orchestrates agents + tasks under a `Process`
- **Process** — `sequential` or `hierarchical` execution

</v-clicks>

</div>

<div class="dense-col">

## Minimal Example

```python
from crewai import Agent, Task, Crew, Process

researcher = Agent(
    role="Senior Researcher",
    goal="Find the latest trends in agentic AI",
    backstory="PhD-level analyst with web access.",
    tools=[search_tool],
)

writer = Agent(
    role="Tech Writer",
    goal="Turn research into a blog post",
    backstory="Crisp, opinionated technical writer.",
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[
        Task(description="Research agentic frameworks",
             agent=researcher),
        Task(description="Write a 500-word summary",
             agent=writer),
    ],
    process=Process.sequential,
)

result = crew.kickoff()
```

</div>

</div>

<!--
CrewAI's superpower is that the code reads like an org chart. You
describe who does what, and the framework figures out the handoffs.
That makes it ideal for prototyping multi-agent systems where the
mental model is genuinely about collaboration between specialists.

Trade-off: the same implicit handoff that makes it easy to write makes
it harder to debug when a long crew misbehaves. You have less direct
control over the execution graph than you do in LangGraph.
-->

---
layout: default
zoom: 0.85
---

# Pydantic AI — Type-Safe Agents

<div class="grid grid-cols-2 gap-4 mt-2">

<div class="dense-col">

## When to Use

<v-clicks>

- You want **structured, validated outputs** instead of free-form strings
- You rely heavily on **IDE autocomplete and type checking**
- You're shipping to production where **schema drift is a real risk**

## Key Concepts

- `Agent[Deps, Output]` — typed in both directions
- `deps_type` — dependency injection per `run`
- `output_type` — Pydantic model the agent must return
- `@agent.tool` — type-checked tool registration
- `agent.run(...)` / `agent.run_sync(...)`

</v-clicks>

</div>

<div class="dense-col">

## Minimal Example

```python
from dataclasses import dataclass
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext

@dataclass
class Deps:
    db: "Database"

class Answer(BaseModel):
    summary: str
    confidence: float

agent = Agent(
    "openai:gpt-4o",
    deps_type=Deps,
    output_type=Answer,
    system_prompt="Answer using the DB tool only.",
)

@agent.tool
async def lookup(ctx: RunContext[Deps], key: str) -> str:
    return await ctx.deps.db.get(key)

result = await agent.run("What is order #42?", deps=Deps(db=db))
print(result.output.summary, result.output.confidence)
```

</div>

</div>

<!--
Pydantic AI brings the same rigor to agents that Pydantic brought to
HTTP APIs. Every boundary — inputs, dependencies, tool args, final
output — is a validated type. That makes refactors safe and turns a
whole class of "the LLM returned weird JSON" bugs into compile-time
errors.

The trade-off is upfront design cost. You have to think about your
schemas before you can run the agent, which slows down the very first
prototype but pays off enormously once the system grows.
-->

---
layout: default
zoom: 0.85
---

# LangGraph — Stateful Graphs

<div class="grid grid-cols-2 gap-4 mt-2">

<div class="dense-col">

## When to Use

<v-clicks>

- Your workflow has **loops, branches, or conditional retries**
- You need **explicit shared state** that multiple nodes mutate
- You require **checkpointing, persistence, or time-travel debugging**
- You're already in the **LangChain / LangSmith** ecosystem

## Key Concepts

- `StateGraph(State)` — typed shared state schema
- `add_node(name, fn)` — pure function over state
- `add_edge` / `add_conditional_edges` — control flow
- `compile(checkpointer=...)` — produces a runnable graph
- Built-in support for **human-in-the-loop** breakpoints

</v-clicks>

</div>

<div class="dense-col">

## Minimal Example

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    question: str
    draft: str
    approved: bool

def draft(state: State) -> State:
    return {"draft": llm.invoke(state["question"])}

def review(state: State) -> State:
    return {"approved": "lgtm" in critic.invoke(state["draft"])}

def route(state: State) -> str:
    return END if state["approved"] else "draft"

g = StateGraph(State)
g.add_node("draft", draft)
g.add_node("review", review)
g.add_edge(START, "draft")
g.add_edge("draft", "review")
g.add_conditional_edges("review", route)

app = g.compile()
result = app.invoke({"question": "Explain agentic loops"})
```

</div>

</div>

<!--
LangGraph is the framework you reach for when "just call the LLM in a
loop" stops being enough. Explicit state means you can reason about
exactly what each node sees and produces. Checkpointing means a long
workflow can pause for a human, resume hours later, or even rewind.

Trade-off: you do have to design the graph and the state schema. For a
linear three-step pipeline, this is overkill — use prompt chaining or
CrewAI instead. For a workflow with retries, branches, and approvals,
the explicit structure pays for itself.
-->

---
layout: default
zoom: 0.85
---

# Agno — High-Performance Lightweight

<div class="grid grid-cols-2 gap-4 mt-2">

<div class="dense-col">

## When to Use

<v-clicks>

- You want a **batteries-included** agent without orchestration boilerplate
- You need **multi-modal** (text / image / audio) in one runtime
- **Memory, knowledge, and reasoning** should be wired in by default
- You care about **instantiation speed** for many short-lived agents

## Key Concepts

- `Agent` — model + tools + memory + knowledge in one object
- `Team` — coordinate multiple agents (route / collaborate / coordinate)
- Built-in **vector knowledge bases** for RAG
- First-class **session memory** and **structured outputs**
- Model-agnostic: OpenAI, Anthropic, Gemini, local, etc.

</v-clicks>

</div>

<div class="dense-col">

## Minimal Example

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.url import UrlKnowledge
from agno.vectordb.lancedb import LanceDb

knowledge = UrlKnowledge(
    urls=["https://docs.agno.com/introduction"],
    vector_db=LanceDb(uri="tmp/lancedb", table_name="docs"),
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    knowledge=knowledge,
    add_history_to_messages=True,
    markdown=True,
)

agent.print_response(
    "Compare Agno and LangGraph for stateful workflows.",
    stream=True,
)
```

</div>

</div>

<!--
Agno (formerly Phidata) optimises for the "I want a capable agent in
ten lines" experience. Memory, knowledge bases, multi-modal input, and
streaming are first-class — you opt out rather than opt in.

Trade-off: it's a younger ecosystem with fewer reference architectures
than LangGraph, and its opinionated defaults occasionally fight you
when you need very fine-grained control.

Final takeaway: there is no universal winner. Match the framework's
core abstraction to your problem's natural shape, and you'll spend
less time fighting the tool and more time shipping the agent.
-->
