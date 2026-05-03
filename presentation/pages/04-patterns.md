---
layout: section-header
---

# Core Patterns

Fundamental building blocks for agentic workflows

<!--
Core patterns are the foundation - every agentic system uses at least one of these.

Three essential patterns:
1. Reflection - Self-improvement through critique
2. Tool Use - Interaction with external systems
3. Planning - Task decomposition and strategy

These are universally applicable and form the basis for more complex patterns.

Duration: 8-10 minutes for all three
-->

---
layout: default
---

# Reflection Pattern: How It Works

<div class="flex flex-col gap-6 mt-4">

<div>

<v-clicks>

1. **Generate** — Agent produces an initial output (code, text, plan, etc.)
2. **Critique** — Agent reviews its own work as if seeing it for the first time
3. **Refine** — Agent improves the output based on the critique
4. **Repeat** — Iterate until a quality threshold is met or max cycles reached

</v-clicks>

</div>

<div v-click class="p-5 bg-orange-900 bg-opacity-20 rounded-xl border border-orange-700">
<mdi:lightbulb class="inline text-orange-400 mr-2"/> <strong>Key Insight:</strong> The agent becomes its own pair programmer — write, review, fix — without human intervention. Each cycle brings the output closer to production quality.
</div>

</div>

<!--
Reflection is like having the AI be its own pair programmer.

It writes code, then reviews it with fresh eyes (fresh tokens?), identifies issues, and fixes them.

The magic: Each critique-refine cycle improves quality without human intervention.

Real example: "Write a user authentication function" → Agent writes code → Agent reviews for security issues → Agent fixes vulnerabilities → Final code is production-ready.

Limitation: Not good for novel problems where the agent doesn't know what "good" looks like.
-->

---
layout: default
---

# Reflection Pattern: Use Cases & Benefits

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

## Where It Shines

<v-clicks>

- **Code quality** — spot bugs, edge cases, and style issues before humans do
- **Documentation** — refine clarity, completeness, and accuracy iteratively
- **Test generation** — critique coverage gaps and add missing scenarios
- **Error messages** — improve user-facing clarity through critique cycles
- **Architecture review** — self-audit design decisions for consistency

</v-clicks>

</div>

<div v-click class="dense-col">

## Benefits

- ✅ Higher quality outputs with fewer human review cycles
- ✅ Consistent standards applied on every run
- ✅ Self-correcting — catches its own mistakes
- ✅ Scales review effort without scaling headcount

## Limitation

<div class="mt-2 p-3 bg-red-900 bg-opacity-20 rounded border border-red-700 text-sm">
<mdi:alert class="inline text-red-400 mr-1"/> Not effective when the agent lacks domain knowledge to judge "good" — garbage criteria in, garbage critique out.
</div>

</div>

</div>

<!--
The use cases all share a common trait: there's a measurable quality bar the agent can check against.

Code: does it pass tests? does it follow conventions?
Docs: is every parameter described? are examples correct?
Tests: does coverage reach critical paths?

The limitation is important: reflection is only as good as the agent's ability to self-evaluate. For genuinely novel problems or domains outside training, the critique step may not catch real issues.
-->

---
layout: default
---

# Reflection Pattern: Actor-Critic Architecture

<div class="flex justify-center items-center" style="height: calc(100% - 4rem);">
  <img src="/images/reflection-pattern.png" alt="Reflection Pattern" class="rounded-xl shadow-lg" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
</div>

<!--
The Actor-Critic architecture shows the two agents working in tandem.

The Actor generates and improves responses (blue cycle on the right).
The Critic reviews and provides feedback (yellow cycle on the left).

Flow: LLM spawns both agents → Actor generates response → Critic reviews it → Critic provides feedback → Actor improves → cycle repeats until quality is met.

Numbers 0–6 show the message flow order between the agents.
-->

---
layout: default
---

# Tool Use Pattern: How It Works

<div class="flex flex-col gap-6 mt-4">

<div>

<v-clicks>

1. **Define Tools**: Register available functions/APIs
2. **Plan**: Agent determines which tools to use
3. **Execute**: Agent calls tools with parameters
4. **Observe**: Agent reads tool results
5. **Act**: Agent adjusts based on outcomes

</v-clicks>

</div>

<div v-click class="p-5 bg-orange-900 bg-opacity-20 rounded-xl border border-orange-700">
<mdi:tools class="inline text-orange-400 mr-2"/> <strong>Key Insight:</strong> Tool use is what makes an agent actually <em>do</em> things instead of just suggesting them — think of tools as the agent's hands.
</div>

</div>

<!--
Tool use is what makes an agent actually DO things instead of just suggesting things.

Think of tools as the agent's hands - ways to manipulate the world.

The pattern: Agent decides "I need to check if this file exists" → Calls file.exists(path) → Gets true/false → Makes next decision based on result.

This is the CORE difference between LLM and Agent - the ability to take action.
-->

---
layout: default
---

# Tool Use Pattern: Tools & Benefits

<div class="grid grid-cols-2 gap-8 mt-4">

<div>

## Common Tools

<v-clicks>

- File system & shell commands
- APIs (REST, GraphQL)
- Databases (SQL, NoSQL)
- Version control & package managers

</v-clicks>

</div>

<div>

## Benefits

<v-clicks>

- ⚡ Autonomous execution
- 🔧 Real-world impact
- 🔄 Feedback loops enabled
- 🎯 Goal-oriented behavior

</v-clicks>

</div>

</div>

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded-xl border border-orange-700">
<mdi:shield-check class="inline text-orange-400 mr-2"/> <strong>Security note:</strong> Tool access must be carefully controlled — agents should only have tools appropriate for their task.
</div>

<!--
Two sides of tool use: what tools exist and why they matter.

Security note: Tool access must be carefully controlled - agents should only have tools appropriate for their task.
-->

---
layout: default
---

# Tool Use Pattern

<div class="flex justify-center items-center" style="height: calc(100% - 4rem);">
  <img src="/images/tool-use-pattern.png" alt="Tool Use Pattern" class="rounded-xl shadow-lg" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
</div>

<!--
The Tool Use Pattern flow:
1. User sends a query to the LLM
2. LLM accesses tools (Web Search, Vector DB, APIs)
3. Tools return results to LLM
4. LLM generates final response back to the user

This cycle is what transforms a static language model into an active agent that can interact with real-world systems.
-->

---
layout: default
---

# Planning Pattern: How It Works

<div class="flex flex-col gap-6 mt-4">

<div>

<v-clicks>

1. **Understand Goal**: Parse high-level objective
2. **Decompose**: Break into sub-tasks
3. **Order**: Determine dependencies
4. **Execute**: Run tasks in sequence/parallel
5. **Verify**: Check overall goal achieved

</v-clicks>

</div>

<div v-click class="p-5 bg-orange-900 bg-opacity-20 rounded-xl border border-orange-700">
<mdi:sitemap class="inline text-orange-400 mr-2"/> <strong>Key Insight:</strong> Planning separates "what to do" from "how to do it" — the agent builds a strategy first, then executes with the ability to replan based on results.
</div>

</div>

<!--
Planning is where the agent thinks before acting.

Instead of rushing straight to code, the agent creates a roadmap.

The beauty: Complex requests become manageable sequences of simple tasks.
-->

---
layout: default
---

# Planning Pattern: Example Decomposition

<div class="flex flex-col gap-4 mt-4">

<div class="p-4 bg-gray-900 bg-opacity-60 rounded-xl border border-gray-700">

**Goal**: "Add user authentication"

</div>

<div>

**Plan**:

<v-clicks>

1. Create user model
2. Implement password hashing
3. Build login endpoint
4. Add JWT generation
5. Create middleware
6. Write tests

</v-clicks>

</div>

<div v-after class="p-4 bg-orange-900 bg-opacity-20 rounded-xl border border-orange-700">

**Benefits**: Structured approach · Clear progress tracking · Handles complexity · Verifiable completion

</div>

</div>

<!--
Real workflow:
User: "Build a REST API for todo items"
Agent Plan:
  1. Define data model (Task, User)
  2. Create database schema
  3. Implement CRUD operations
  4. Add validation
  5. Write API routes
  6. Add authentication
  7. Write tests
  8. Document endpoints

Each step is concrete and testable.

Limitation: Requires the agent to have domain knowledge to create good plans.
-->

---
layout: default
---

# Planning Pattern: Flow Diagram

<div class="flex justify-center items-center" style="height: calc(100% - 4rem);">
  <img src="/images/planning-pattern.png" alt="Planning Pattern" class="rounded-xl shadow-lg" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
</div>

<!--
The Planning Pattern flow:
1. User sends a Prompt to the Planning agent
2. Planning generates a Task list (Task Generation)
3. The Task is executed by the Task Agent
4. Task Agent returns the Task Result
5. If needed, Replan adjusts the task list based on results
6. Final Response is returned to the user

Key insight: Planning separates "what to do" from "how to do it" — the agent builds a strategy first, then executes with the ability to replan based on results.
-->

---
layout: default
---

# Multi-Agent Pattern: How It Works

<div class="flex flex-col gap-6 mt-4">

<div>

<v-clicks>

1. **Specialist Agents**: Each agent has a specific domain or capability
2. **Critic/Review Agents**: Dedicated agents that evaluate others' outputs
3. **Orchestrator**: Coordinator manages workflow and routes tasks
4. **Collaboration**: Agents communicate via handoffs or shared queues
5. **Synthesis**: Combine diverse outputs into a unified result

</v-clicks>

</div>

<div v-click class="p-5 bg-orange-900 bg-opacity-20 rounded-xl border border-orange-700">
<mdi:account-group class="inline text-orange-400 mr-2"/> <strong>Key Insight:</strong> Specialization leads to better performance — a single agent trying to be excellent at everything faces fundamental trade-offs.
</div>

</div>

<!--
Multi-Agent pattern is about specialization — from ByteByteGo: "A single agent trying to be excellent at everything faces challenges. By dividing responsibilities among multiple agents, each can be optimized for its specific role."

Communication patterns:
- Central coordinator (star topology)
- Direct agent-to-agent handoff (mesh topology)
- Shared message queue (pub-sub)
-->

---
layout: default
---

# Multi-Agent Pattern: Roles & Trade-offs

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

## Agent Roles

<v-clicks>

- **Researcher**: Finds and synthesizes information
- **Coder**: Writes and debugs code
- **Analyst**: Statistical analysis & visualization
- **Critic**: Reviews and validates outputs
- **Orchestrator**: Routes tasks and synthesizes results

</v-clicks>

</div>

<div v-click class="dense-col">

## Trade-offs

- ✅ Higher quality through specialization
- ✅ Diverse expert perspectives
- ✅ Scalable — add more agents as needed
- ⚠️ Coordination overhead increases
- ⚠️ Debugging across agents is harder

<div class="mt-4 p-3 bg-blue-900 bg-opacity-30 rounded">

**Best for**: tasks requiring diverse expertise — dev teams, research pipelines, complex multi-domain analysis

</div>

</div>

</div>

<!--
Real example: Software dev team — PM agent (requirements), Coder agent (implementation), Tester agent (QA), Reviewer agent (code review), Coordinator (integration).

Key insight: For simple tasks, a single agent wins. For tasks requiring diverse expertise, multi-agent systems produce superior results.
-->

---
layout: default
---

# Multi-Agent Pattern: Flow Diagram

<div class="flex justify-center items-center" style="height: calc(100% - 4rem);">
  <img src="/images/multi-agent-pattern-animated.gif" alt="Multi-Agent Pattern" class="rounded-xl shadow-lg" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
</div>

<!--
The Planning Pattern flow from ByteByteGo illustrates how a coordinator-based multi-agent system works:

1. User sends a Prompt to the Planning/Orchestrator agent
2. Planning generates a Task list (Task Generation)
3. The Task is dispatched to a specialist Task Agent
4. Task Agent returns the Task Result
5. If needed, a Replan cycle adjusts the task list based on the result
6. Final Response is returned to the user

Key insight: The Replan step is what makes this adaptive — the orchestrator can adjust strategy mid-execution based on what agents discover, making the system resilient to unexpected results.

Source: ByteByteGo — Top AI Agentic Workflow Patterns
-->

---
layout: section-header
---

# Why Multi-Agent?
## Single Agent Limitations and Multi-Agent Benefits

---

# Single Agent Limitations

<div class="grid grid-cols-3 gap-5 mt-6">

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">📊</div>
<div class="text-lg font-bold text-orange-300">Context Window Limits</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🎯</div>
<div class="text-lg font-bold text-orange-300">Specialization Ceiling</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">⏳</div>
<div class="text-lg font-bold text-orange-300">Sequential Bottlenecks</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🌊</div>
<div class="text-lg font-bold text-orange-300">Error Propagation</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🧩</div>
<div class="text-lg font-bold text-orange-300">Multi-Domain Complexity</div>
</div>

<div v-click class="p-4 bg-red-900 bg-opacity-50 rounded-xl border border-red-500 text-center flex items-center justify-center">
<div class="text-base font-bold text-red-200">One agent + complex multi-domain tasks = context degrades fast</div>
</div>

</div>

---

# Multi-Agent Benefits

<div class="grid grid-cols-3 gap-5 mt-6">

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">⚡</div>
<div class="text-lg font-bold text-orange-300">Parallel Processing</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🎯</div>
<div class="text-lg font-bold text-orange-300">Domain Specialization</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🛡️</div>
<div class="text-lg font-bold text-orange-300">Fault Isolation</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">📈</div>
<div class="text-lg font-bold text-orange-300">Horizontal Scalability</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🧩</div>
<div class="text-lg font-bold text-orange-300">Compositional Flexibility</div>
</div>

<div v-click class="p-4 bg-green-900 bg-opacity-50 rounded-xl border border-green-500 text-center flex items-center justify-center">
<div class="text-base font-bold text-green-200">Specialists collaborating in parallel — each handling their domain</div>
</div>

</div>

---
layout: default
---

# Multi-Agent Pitfalls & Failure Modes

<div class="grid grid-cols-4 gap-5 mt-6">

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">💥</div>
<div class="text-lg font-bold text-orange-300">Complexity Explosion</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🌊</div>
<div class="text-lg font-bold text-orange-300">Cascading Failures</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🧩</div>
<div class="text-lg font-bold text-orange-300">Context Fragmentation</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">💸</div>
<div class="text-lg font-bold text-orange-300">Runaway Costs</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🎲</div>
<div class="text-lg font-bold text-orange-300">Non-Determinism</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">⏳</div>
<div class="text-lg font-bold text-orange-300">Latency Chains</div>
</div>

<div v-click class="p-4 bg-gray-800 bg-opacity-60 rounded-xl border border-gray-600 text-center">
<div class="text-3xl mb-2">🔒</div>
<div class="text-lg font-bold text-orange-300">Orchestration Deadlocks</div>
</div>

<div v-click class="p-4 bg-orange-900 bg-opacity-50 rounded-xl border border-orange-500 text-center flex items-center justify-center">
<div class="text-base font-bold text-orange-200">Start with the simplest architecture that could work</div>
</div>

</div>

<!--
Multi-agent is powerful but not free — every benefit has a corresponding cost.

**Complexity Explosion** — Each agent added multiplies coordination surface area; debugging a 5-agent system is exponentially harder.

**Cascading Failures** — One agent's bad output silently poisons downstream agents; errors compound before anything raises an alarm.

**Context Fragmentation** — Agents have partial world views; critical information may not be passed, leading to contradictory decisions.

**Runaway Costs** — Every agent hop burns tokens; a 6-agent pipeline can cost 10× more than a well-prompted single agent.

**Non-Determinism** — Parallel agents + async handoffs = results that change between runs; nearly impossible to reproduce bugs.

**Latency Chains** — Sequential agent dependencies stack latency; 5 agents × 3s each = 15s minimum, with no easy short-circuit.

**Orchestration Deadlocks** — Agents waiting on each other, circular dependencies, or resource contention can silently stall everything.

Golden Rule: Multi-agent adds real overhead — only reach for it when a single agent genuinely can't do the job.

Key questions before choosing multi-agent:
- Can a well-prompted single agent with tools do this?
- Do we genuinely need parallel specialization, or is that premature optimization?
- Do we have observability infrastructure to debug agent interactions?
- Is the added latency and cost acceptable for this use case?

Common anti-pattern: teams reach for multi-agent because it "sounds cool" or seems more sophisticated — then spend weeks debugging coordination issues that a single agent would never have had.
-->

---
layout: section-header
---

# Workflow Patterns

Execution flow control for non-agentic sequences

<!--
Workflow patterns are simpler than agentic patterns - they're deterministic, predictable flows.

Two fundamental patterns:
1. Sequential - Step-by-step execution where each step depends on the previous
2. Parallel - Concurrent execution of independent tasks

These are based on Phil Schmid's taxonomy - workflow patterns are non-agentic (no autonomous decision-making), but form the foundation for more complex agentic systems.

Duration: 5-7 minutes for both
-->

---
layout: default
---

# Sequential Agent: Visual Examples

<div class="flex flex-col gap-4 h-4/5 justify-center">

<div class="flex flex-col items-center gap-1">
  <p class="text-sm text-orange-300 font-semibold uppercase tracking-wide">Simple Sequential Flow</p>
  <img src="/images/sequential-agent-simple.png" alt="Sequential Agent - Simple Flow" class="rounded-xl shadow-lg object-contain max-h-36" />
</div>

<div class="flex flex-col items-center gap-1">
  <p class="text-sm text-orange-300 font-semibold uppercase tracking-wide">Sequential with Loop Agent</p>
  <img src="/images/sequential-agent-loop.png" alt="Sequential Agent - Loop" class="rounded-xl shadow-lg object-contain max-h-36" />
</div>

</div>

<!--
Two real-world examples of sequential agents in action.

Left: A simple three-step sequential agent — Check Positive Aspect → Check Negative Aspect → Generate Final Confirm. Each step receives the output of the previous step and adds its own analysis before passing forward.

Right: A more advanced sequential pattern where one of the steps is itself a loop agent — Research Agent → Loop Agent (Critic + Review) → Conclusion Agent. This nests an inner feedback loop inside the outer sequential chain, enabling iterative quality improvement in the middle of the pipeline.

Key takeaway: Sequential agents can be composed — steps can themselves be agents with their own internal patterns.
-->

---
layout: default
---

# Sequential Workflow Pattern: How It Works

<div class="flex flex-col gap-6 mt-4">

<v-clicks>

1. **Chain LLM Calls**: Output of one feeds into next
2. **Fixed Sequence**: Predefined order of operations
3. **Transform Data**: Each step processes and passes on
4. **No Branching**: Linear, deterministic flow

</v-clicks>

<div v-click class="mt-3 p-3 bg-orange-900 bg-opacity-20 rounded">
<mdi:pipe class="inline"/> Like a pipeline: each stage transforms the input
</div>

</div>

<!--
Sequential/Prompt Chaining is the simplest workflow pattern.

Think of it as a Unix pipeline: `cat file.txt | grep pattern | sort | uniq`

Each LLM call is a stage in the pipeline. The output of one becomes the input of the next.

Phil Schmid's key insight: "The output of one LLM call sequentially feeds into the input of the next"

Example workflow:
1. User provides text
2. LLM summarizes text
3. LLM translates summary to French
4. LLM formats as markdown
→ Final output: French markdown summary
-->

---
layout: default
---

# Sequential Workflow Pattern: Use Cases

<div class="flex flex-col gap-6 mt-4">

<div>

- **Document Generation**: Outline → Validate → Write → Format
- **Data Processing**: Extract → Transform → Summarize
- **Content Creation**: Research → Draft → Edit → Publish

</div>

<div class="p-4 bg-orange-900 bg-opacity-20 rounded-xl border border-orange-700">
<strong>Benefits</strong>: Clear separation of concerns · Easy to debug · Reusable components · Predictable behavior
</div>

<p class="text-orange-300 text-sm">Best for well-defined transformations where steps are known upfront</p>

</div>

<!--
Key limitation: No decision-making. If you need branching logic, you need routing or agentic patterns.
-->

---
layout: default
zoom: 0.85
---

# Parallel Workflow Pattern (Parallelization)

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

<v-clicks>

1. **Decompose Task**: Split into independent subtasks
2. **Execute Concurrently**: Multiple LLMs process simultaneously
3. **Collect Results**: Gather all outputs
4. **Aggregate**: Final LLM synthesizes combined result

</v-clicks>

<div v-click class="mt-3 p-3 bg-orange-900 bg-opacity-20 rounded">
<mdi:arrow-left-right class="inline"/> Map-Reduce for LLMs
</div>

</div>

<div v-click class="dense-col">

## Use Cases

- **RAG**: Decompose query → parallel searches → aggregate
- **Document Analysis**: Split sections → analyze → synthesize
- **Diverse Perspectives**: Multiple viewpoints → combine

## Benefits

- ⚡ Improved latency (parallel execution)
- 🎯 Enhanced quality (diverse outputs)
- 📈 Scalability (add more workers)
- 🔄 Better coverage (multiple approaches)

<p class="mt-2 text-orange-300 text-xs">Best when subtasks are independent with no sequential dependencies</p>

</div>

</div>

<!--
Parallelization is the workflow equivalent of map-reduce.

The key requirement: subtasks must be independent. If task B needs the output of task A, they can't run in parallel.

Phil Schmid's definition: "Independent subtasks processed simultaneously by multiple LLMs with aggregated outputs synthesized by a final LLM"

Classic example: RAG with decomposed query
1. User asks complex question
2. Decompose into 3 simpler queries
3. Execute all 3 searches in parallel
4. Aggregate results into comprehensive answer

Performance benefit: If each query takes 2 seconds, sequential = 6 seconds, parallel = 2 seconds (plus aggregation time).

Quality benefit: Parallel approaches can explore different angles simultaneously, then synthesis picks the best insights from each.

Real-world analogy: Divide-and-conquer algorithms in computer science.
-->

---
layout: default
---

# Parallel Workflow Pattern

<div class="flex items-center justify-center h-4/5">
  <img src="/images/parallel-workflow-pattern.png" alt="Parallel Workflow Pattern" class="max-h-full max-w-full rounded-xl shadow-lg" />
</div>

<!--
Visual diagram of the parallel workflow pattern.
-->

---
layout: section-header
---

# Coordination Patterns

Multi-agent collaboration and task delegation

<!--
Coordination patterns are for situations where multiple agents need to work together.

Three key patterns:
1. Multi-Agent - Collaborative execution with specialized roles
2. Hierarchical - Parent-child delegation
3. Routing - Classification and specialized handling

These patterns enable complex workflows that require diverse expertise or task decomposition.

Duration: 8-10 minutes for all three
-->

---
layout: default
---

# Hierarchical Workflow Pattern: How It Works

<div class="flex flex-col gap-6 mt-4">

<div>

<v-clicks>

1. **Coordinator Agent**: High-level planning and delegation
2. **Worker Agents**: Specialized execution
3. **Task Breakdown**: Coordinator decomposes goals
4. **Assignment**: Delegate to appropriate workers
5. **Collection**: Gather and synthesize results

</v-clicks>

</div>

<div v-click class="p-5 bg-orange-900 bg-opacity-20 rounded-xl border border-orange-700">
<mdi:file-tree class="inline text-orange-400 mr-2"/> <strong>Key Insight:</strong> Parent-child delegation — the coordinator is like a project manager who understands the goal, breaks it into tasks, and assigns them to specialists.
</div>

</div>

<!--
Hierarchical pattern is closely related to the Planning pattern, but with multiple specialized workers.

Key difference from Multi-Agent: Hierarchical has clear parent-child relationships. Multi-Agent can be peer-to-peer.
-->

---
layout: default
---

# Hierarchical Workflow Pattern: Use Cases & Benefits

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

## Use Cases

<v-clicks>

- **Complex Projects**: Break into sub-projects with specialists
- **Task Orchestration**: Coordinator manages workflow
- **Resource Management**: Allocate workers efficiently
- **Phased Execution**: Sequential delegation with dependencies

</v-clicks>

</div>

<div v-click class="dense-col">

## Benefits

- 📋 Clear responsibility hierarchy
- 🎯 Specialized worker expertise
- 🔄 Coordinator handles complexity
- ✅ Centralized monitoring

<div class="mt-4 p-3 bg-blue-900 bg-opacity-30 rounded">

**When to Use**: When tasks have clear hierarchy and need central coordination

</div>

</div>

</div>

<!--
Example: Building a web application
- Coordinator: Understands "build todo app"
- Frontend Worker: Builds UI
- Backend Worker: Builds API
- Database Worker: Designs schema
- Test Worker: Writes tests

Coordinator collects outputs and ensures they integrate correctly.
-->

---
layout: default
---

# Hierarchical Pattern: Example

<div class="flex justify-center items-center" style="height: calc(100% - 4rem);">
  <img src="/images/hierarchical-task-decomposition.png" alt="Hierarchical Task Decomposition Agent Pattern" class="rounded-xl shadow-lg" style="max-height: 100%; max-width: 100%; object-fit: contain;" />
</div>

<!--
The diagram illustrates the Hierarchical Task Decomposition Agent Pattern — "agents within agents within agents" — the Russian Doll approach.

Architecture (left):
- User sends: "Write report on AI trends"
- ReportWriter Agent is the top-level orchestrator
  - Writes comprehensive reports
  - Delegates research via AgentTool call "Research AI trends"

Agent Hierarchy (right):
- Level 1 — Top-Level Agent: ReportWriter Agent (orchestrator)
- Level 2 — Coordinator Agents: ResearchAssistant Agent
  - Finds & summarizes info
  - Tools: [WebSearch, Summarizer]
- Level 3 — Tool Agents:
  - WebSearch Agent: searches web for facts, returns raw data
  - Summarizer Agent: condenses text, extracts key points

Flow:
1. User request → ReportWriter
2. AgentTool call "Research AI trends" → ResearchAssistant
3. AgentTool call "Search web" → WebSearch Agent
4. AgentTool call "Summarize findings" → Summarizer Agent
5. Final response back to user: "Complete AI trends report with research and analysis"

Key insight: Each level delegates to the next, enabling complex multi-step tasks through clean separation of concerns.
-->

---
layout: default
---

# Routing Pattern (Handoff): How It Works

<div class="flex flex-col gap-6 mt-4">

<div>

<v-clicks>

1. **Classifier LLM**: Analyzes incoming request
2. **Categorization**: Determines type/complexity
3. **Route Decision**: Select appropriate handler
4. **Delegation**: Send to specialized agent/model
5. **Response**: Handler provides result

</v-clicks>

</div>

<div v-click class="p-5 bg-orange-900 bg-opacity-20 rounded-xl border border-orange-700">
<mdi:graph class="inline text-orange-400 mr-2"/> <strong>Key Insight:</strong> Smart dispatch to specialists — an initial LLM classifies user input and directs it to specialized downstream handlers based on category.
</div>

</div>

<!--
Phil Schmid's definition: "An initial LLM classifies user input and directs it to specialized downstream handlers based on category"

Classic example: Customer support triage
User: "I can't log in" → Routes to Technical Support Agent
User: "Why was I charged twice?" → Routes to Billing Agent

85-95% routing accuracy is achievable.
-->

---
layout: default
---

# Routing Pattern: Use Cases & Benefits

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

## Use Cases

<v-clicks>

- **Customer Support**: Route by category (billing, technical, product)
- **Model Selection**: Simple → cheap model, Complex → advanced
- **Domain Routing**: Weather, Science, Finance specialists
- **Load Balancing**: Distribute across available handlers

</v-clicks>

</div>

<div v-click class="dense-col">

## Benefits

- 💰 Cost optimization (use right-sized models)
- ⚡ Latency optimization (fast models for simple)
- 🎯 Quality optimization (specialists for domains)
- 📊 Separation of concerns

<div class="mt-4 p-3 bg-blue-900 bg-opacity-30 rounded">

**When to Use**: When requests have clear categories with specialized handlers

</div>

</div>

</div>

<!--
Performance benefit: Simple queries can go to smaller/cheaper models, complex queries to advanced models.

Implementation: Router LLM generates classification, system routes based on that classification.
-->

---
layout: default
---

# Routing Pattern: Visual Overview

<div class="flex items-center justify-center h-4/5">
  <img src="/images/routing-pattern.png" alt="Routing Pattern - Router Agent dispatching to specialized experts" class="max-h-full max-w-full rounded-xl shadow-lg object-contain" />
</div>

<!--
The diagram shows a Router Agent receiving a Question and routing it to one of three specialized experts: Legal, Medical, or Technical. Each expert returns a Response back through the router.

Key insight: The Router Agent uses an LLM (the brain icon) to classify the incoming question and determine which specialist to dispatch to — enabling smart, cost-effective delegation.
-->

---
layout: section-header
---

# Control Patterns

Oversight and feedback mechanisms

<!--
Control patterns add human oversight and iterative improvement to agentic workflows.

Two key patterns:
1. Human-in-the-Loop - Critical checkpoints for human decisions
2. Feedback Loop - Iterative refinement based on evaluation

These patterns ensure quality and safety in autonomous systems.

Duration: 5-6 minutes for both
-->

---
layout: default
---

# Human-in-the-Loop Pattern: How It Works

<div class="flex flex-col gap-6 mt-4">

<div>

<v-clicks>

1. **Agent Execution**: Agent performs initial task
2. **Pause Point**: System stops for human review
3. **Human Decision**: Approve, reject, or modify
4. **Incorporation**: Human feedback guides next steps
5. **Resume**: Continue with human-guided direction

</v-clicks>

</div>

<div v-click class="p-5 bg-orange-900 bg-opacity-20 rounded-xl border border-orange-700">
<mdi:account class="inline text-orange-400 mr-2"/> <strong>Key Insight:</strong> Critical checkpoints for human wisdom — agents handle routine work, humans make critical decisions.
</div>

</div>

<!--
Key principle: Agents handle routine work, humans make critical decisions.

Design consideration: Where to place HITL checkpoints?
- Before irreversible actions
- After complex decisions
- When confidence is low
- When regulations require it
-->

---
layout: default
---

# Human-in-the-Loop Pattern: Use Cases & Benefits

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

## Use Cases

<v-clicks>

- **High-Stakes Decisions**: Legal, medical, financial domains
- **Content Moderation**: Human review of sensitive content
- **Approval Workflows**: Multi-stage business processes
- **Safety-Critical**: Systems where errors are unacceptable

</v-clicks>

</div>

<div v-click class="dense-col">

## Benefits

- 🛡️ Risk mitigation (human oversight)
- ✅ Quality assurance (expert review)
- ⚖️ Compliance (regulatory requirements)
- 🎯 Trust building (human accountability)

<div class="mt-4 p-3 bg-blue-900 bg-opacity-30 rounded">

**When to Use**: When decisions are too critical for full automation or require domain expertise

</div>

</div>

</div>

<!--
Human-in-the-Loop (HITL) is essential for high-stakes scenarios.

Example: Document generation workflow
1. Agent drafts contract
2. HITL: Lawyer reviews critical terms
3. Agent incorporates lawyer's edits
4. HITL: Client approves final version
5. Agent processes finalized contract

Balance: Too many HITL checkpoints slow workflow, too few reduce quality/safety.
-->

---
layout: default
background: '#000000'
title: Human-in-the-Loop Diagram
---

<div class="flex items-center justify-center h-full">
  <img src="/images/human-in-the-loop.png" class="object-contain rounded-xl" style="width: 100%; height: 100%;" />
</div>

---
layout: default
---

# Feedback Loop Pattern: How It Works

<div class="flex flex-col gap-6 mt-4">

<div>

<v-clicks>

1. **Initial Output**: Agent generates first attempt
2. **Evaluation**: System or agent evaluates quality
3. **Feedback Generation**: Identify improvements needed
4. **Refinement**: Agent incorporates feedback
5. **Iterate**: Repeat until quality threshold met

</v-clicks>

</div>

<div v-click class="p-5 bg-orange-900 bg-opacity-20 rounded-xl border border-orange-700">
<mdi:refresh class="inline text-orange-400 mr-2"/> <strong>Key Insight:</strong> If you can evaluate output, you can iteratively improve it — self-improvement through iteration.
</div>

</div>

<!--
Feedback Loop pattern enables autonomous quality improvement.

Design considerations:
- Maximum iterations (prevent infinite loops)
- Convergence criteria (when to stop)
- Feedback quality (garbage in, garbage out)
- Cost vs. benefit (each iteration costs tokens)

Synergy: Combine with Reflection pattern for self-evaluation feedback loop.
-->

---
layout: default
---

# Feedback Loop Pattern: Use Cases & Benefits

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

## Use Cases

<v-clicks>

- **Code Generation**: Write → Test → Fix → Repeat
- **Content Refinement**: Draft → Critique → Revise
- **Optimization**: Propose → Evaluate → Improve
- **Conversation**: Respond → Assess → Refine

</v-clicks>

</div>

<div v-click class="dense-col">

## Benefits

- 🎯 Quality improvement (iterative refinement)
- 📈 Adaptive behavior (learn from mistakes)
- 🔄 Self-correction (automatic refinement)
- ⚡ Efficiency (fewer manual interventions)

<div class="mt-4 p-3 bg-blue-900 bg-opacity-30 rounded">

**When to Use**: When output quality can be measured and iterative refinement is beneficial

</div>

</div>

</div>

<!--
Example: Code generation with tests
1. Agent writes function
2. Run tests → 2 failures
3. Agent analyzes failures, updates code
4. Run tests → all pass
5. Success!

Real-world analogy: Scientific method (hypothesis → experiment → analysis → revision).
-->

---
background: '#000000'
title: Feedback Loop Diagram
---

<div class="flex items-center justify-center h-full">
  <img src="/images/feedback-loop-diagram.png" class="max-h-full max-w-full object-contain rounded-xl" />
</div>

---
layout: default
---

# Models by Agentic Pattern

<div class="grid grid-cols-2 gap-4 mt-6">

<div class="p-4 rounded-xl border border-orange-500/40 bg-orange-900/10">
  <div class="text-3xl">🧠</div>
  <div class="text-orange-400 font-bold text-lg mt-1">Reasoning Models</div>
  <div class="text-xs opacity-70 italic">o3 · Claude thinking · Gemini 2.5 Pro</div>
  <div class="mt-3 flex flex-wrap gap-2 text-xs">
    <span class="px-2 py-1 rounded bg-orange-500/20">Reflection</span>
    <span class="px-2 py-1 rounded bg-orange-500/20">Feedback Loop</span>
    <span class="px-2 py-1 rounded bg-orange-500/20">Planning</span>
  </div>
</div>

<div class="p-4 rounded-xl border border-orange-500/40 bg-orange-900/10">
  <div class="text-3xl">🔧</div>
  <div class="text-orange-400 font-bold text-lg mt-1">Function-Calling Specialists</div>
  <div class="text-xs opacity-70 italic">Claude 3.7 Sonnet · GPT-4o · Gemini 2.5</div>
  <div class="mt-3 flex flex-wrap gap-2 text-xs">
    <span class="px-2 py-1 rounded bg-orange-500/20">Tool Use</span>
    <span class="px-2 py-1 rounded bg-orange-500/20">Human-in-the-Loop</span>
  </div>
</div>

<div class="p-4 rounded-xl border border-orange-500/40 bg-orange-900/10">
  <div class="text-3xl">🤝</div>
  <div class="text-orange-400 font-bold text-lg mt-1">Tiered Mixes</div>
  <div class="text-xs opacity-70 italic">Sonnet/o3 orchestrator + Haiku/Flash workers</div>
  <div class="mt-3 flex flex-wrap gap-2 text-xs">
    <span class="px-2 py-1 rounded bg-orange-500/20">Multi-Agent</span>
    <span class="px-2 py-1 rounded bg-orange-500/20">Hierarchical</span>
  </div>
</div>

<div class="p-4 rounded-xl border border-orange-500/40 bg-orange-900/10">
  <div class="text-3xl">⚡</div>
  <div class="text-orange-400 font-bold text-lg mt-1">Fast / Cheap Models</div>
  <div class="text-xs opacity-70 italic">Haiku · GPT-4o-mini · Gemini Flash · Llama 4 Scout</div>
  <div class="mt-3 flex flex-wrap gap-2 text-xs">
    <span class="px-2 py-1 rounded bg-orange-500/20">Routing</span>
    <span class="px-2 py-1 rounded bg-orange-500/20">Prompt Chaining</span>
    <span class="px-2 py-1 rounded bg-orange-500/20">Parallelization</span>
  </div>
</div>

</div>

<div class="mt-6 text-center text-sm text-orange-300" v-click>
  Match the model to the <strong>cognitive demand</strong> of the pattern
</div>

<!--
Key insight: model selection is not one-size-fits-all — it follows the cognitive demand of the pattern.

Full mapping (pattern → model type → recommended models → reason):

Reasoning / thinking models:
- Reflection → o3, Claude (extended thinking) — Deep self-critique requires extended reasoning
- Feedback Loop → o3, Claude (extended thinking) — Evaluate + regenerate demands analytical depth
- Planning → o3, Gemini 2.5 Pro, Claude thinking — Multi-step decomposition benefits from long-horizon reasoning

Function-calling specialists:
- Tool Use → Claude 3.7 Sonnet, GPT-4o, Gemini 2.5 — Reliable structured outputs and tool invocations
- Human-in-the-Loop → Claude Sonnet, GPT-4o — Human handles critical decisions; model handles drafts

Tiered mixes:
- Multi-Agent → Sonnet/GPT-4o (orchestrator) + Haiku/Flash (workers) — Strong orchestration, cheap parallel workers
- Hierarchical → o3 / Sonnet (planner) + Haiku / Flash (executors) — Quality planning + high-throughput execution

Fast classifiers / efficient per-step:
- Routing → Claude Haiku, GPT-4o-mini, Gemini Flash — Low-latency, low-cost intent classification
- Prompt Chaining → Haiku, GPT-4o-mini, Llama 4 Scout — Simple transforms; cost compounds across steps
- Parallelization → Haiku, Flash, Llama 4 Scout — High throughput; per-call cost dominates

Why this grouping works:

Reasoning patterns (reflection, planning, feedback loop):
- These require the model to evaluate its own output or plan many steps ahead
- o1/o3 and "extended thinking" models excel here because they spend more compute per token

Tool Use:
- Needs reliable function-calling / structured output
- Claude 3.7 Sonnet, GPT-4o, and Gemini 2.5 Pro have the most mature tool-use capabilities

Coordination patterns (multi-agent, hierarchical):
- The orchestrator faces the hardest reasoning task — use a strong model there
- Workers execute bounded, well-defined tasks — use the fastest cheapest model that meets quality bar
- This tiered approach can cut costs 3–5× vs. using a frontier model for every step

Efficiency patterns (routing, chaining, parallelization):
- Cost compounds: 100 parallel calls × premium model = expensive
- These patterns benefit most from model down-tiering

Human-in-the-Loop:
- The human IS the reasoning step for high-stakes decisions
- Model just needs to generate drafts and incorporate feedback well

Real-world example (Anthropic's research):
Claude Haiku for routing + Claude Sonnet for generation + human review = 70% cost reduction vs. all-Sonnet while maintaining quality.

Rule of thumb: reasoning models for *cognitive* patterns (reflection, planning, feedback); fast/cheap models for *throughput* patterns (routing, chaining, parallelization); tiered mixes for *coordination* patterns.
-->
