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

# Reflection Pattern: Self-Improvement

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

<v-clicks>

1. **Generate**: Agent produces initial output
2. **Critique**: Agent reviews its own work
3. **Refine**: Agent improves based on critique
4. **Repeat**: Iterate until quality threshold met

</v-clicks>

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:lightbulb class="inline"/> The agent becomes its own code reviewer
</div>

</div>

<div v-click class="dense-col">

## Use Cases

- Code quality improvement
- Documentation refinement
- Test case generation
- Error message clarity
- Architecture review

## Benefits

- ✅ Higher quality outputs
- ✅ Reduced human review time
- ✅ Consistent standards
- ✅ Self-correcting behavior

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

# Tool Use Pattern: System Integration

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

<v-clicks>

1. **Define Tools**: Register available functions/APIs
2. **Plan**: Agent determines which tools to use
3. **Execute**: Agent calls tools with parameters
4. **Observe**: Agent reads tool results
5. **Act**: Agent adjusts based on outcomes

</v-clicks>

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:tools class="inline"/> Transforms suggestions into actions
</div>

</div>

<div v-click class="dense-col">

## Common Tools

- File system & shell commands
- APIs (REST, GraphQL)
- Databases (SQL, NoSQL)
- Version control & package managers

## Benefits

- ⚡ Autonomous execution
- 🔧 Real-world impact
- 🔄 Feedback loops enabled
- 🎯 Goal-oriented behavior

</div>

</div>

<!--
Tool use is what makes an agent actually DO things instead of just suggesting things.

Think of tools as the agent's hands - ways to manipulate the world.

The pattern: Agent decides "I need to check if this file exists" → Calls file.exists(path) → Gets true/false → Makes next decision based on result.

This is the CORE difference between LLM and Agent - the ability to take action.

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

# Planning Pattern: Task Decomposition

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

<v-clicks>

1. **Understand Goal**: Parse high-level objective
2. **Decompose**: Break into sub-tasks
3. **Order**: Determine dependencies
4. **Execute**: Run tasks in sequence/parallel
5. **Verify**: Check overall goal achieved

</v-clicks>

<div v-click class="mt-3 p-3 bg-orange-900 bg-opacity-20 rounded">
<mdi:sitemap class="inline"/> From "what" to "how" automatically
</div>

</div>

<div v-click class="dense-col">

## Example Decomposition

**Goal**: "Add user authentication"

**Plan**:
1. Create user model
2. Implement password hashing
3. Build login endpoint
4. Add JWT generation
5. Create middleware
6. Write tests

**Benefits**: Structured approach · Clear progress tracking · Handles complexity · Verifiable completion

</div>

</div>

<!--
Planning is where the agent thinks before acting.

Instead of rushing straight to code, the agent creates a roadmap.

The beauty: Complex requests become manageable sequences of simple tasks.

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
zoom: 0.85
---

# Multi-Agent Pattern: Specialization at Scale

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

<v-clicks>

1. **Specialist Agents**: Each agent has a specific domain or capability
2. **Critic/Review Agents**: Dedicated agents that evaluate others' outputs
3. **Orchestrator**: Coordinator manages workflow and routes tasks
4. **Collaboration**: Agents communicate via handoffs or shared queues
5. **Synthesis**: Combine diverse outputs into a unified result

</v-clicks>

<div v-click class="mt-4 p-3 bg-orange-900 bg-opacity-20 rounded">
<mdi:account-group class="inline"/> Specialization leads to better performance than generalization
</div>

</div>

<div v-click class="dense-col">

## Agent Roles

- **Researcher**: Finds and synthesizes information
- **Coder**: Writes and debugs code
- **Analyst**: Statistical analysis & visualization
- **Critic**: Reviews and validates outputs
- **Orchestrator**: Routes tasks and synthesizes results

## Trade-offs

- ✅ Higher quality through specialization
- ✅ Diverse expert perspectives
- ✅ Scalable — add more agents as needed
- ⚠️ Coordination overhead increases
- ⚠️ Debugging across agents is harder

</div>

</div>

<!--
Multi-Agent pattern is about specialization — the core insight is that a single agent trying to be excellent at everything faces fundamental trade-offs.

From ByteByteGo: "A single agent trying to be excellent at everything faces challenges. By dividing responsibilities among multiple agents, each can be optimized for its specific role."

Three types of agents:
1. Specialist agents: research, coding, data analysis — each optimized for their domain
2. Critic/review agents: dedicated to finding flaws and improving quality
3. Coordinator/orchestrator: manages the overall workflow and integration

Communication patterns:
- Central coordinator (star topology)
- Direct agent-to-agent handoff (mesh topology)
- Shared message queue (pub-sub)

Key insight: For simple tasks, a single agent wins. For tasks requiring diverse expertise — software development teams, research pipelines, complex analysis — multi-agent systems produce superior results.

Real example: Software dev team — PM agent (requirements), Coder agent (implementation), Tester agent (QA), Reviewer agent (code review), Coordinator (integration).
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

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

### Context Window Constraints
Every token costs — long tasks overflow the window, losing earlier context and decisions

### Specialization vs Generalization
A generalist agent is mediocre at everything; deep expertise in one domain requires a specialist

### Sequential Processing Bottlenecks
One agent can only do one thing at a time — independent subtasks queue up unnecessarily

</v-clicks>

</div>

<div>

<v-clicks>

### Error Propagation
A mistake in step 3 of a 10-step chain corrupts all downstream work with no isolation

### Multi-Domain Complexity
Tasks spanning frontend, backend, infrastructure, and security require too many context switches for one agent to handle well

</v-clicks>

<div v-click class="mt-6 p-4 bg-red-900 bg-opacity-30 rounded">

**The ceiling**: A single agent handling complex, multi-domain tasks is like asking one developer to simultaneously write React, design SQL schemas, and configure Kubernetes — context degrades fast

</div>

</div>

</div>

---

# Multi-Agent Benefits

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<v-clicks>

### Parallel Processing
Independent subtasks execute simultaneously — what takes hours sequentially takes minutes in parallel

### Domain Specialization
Each agent is an expert in one area — a dedicated test agent outperforms a generalist on testing tasks

### Fault Isolation
A failure in one agent is contained — the rest of the system continues; failed tasks can be retried without restarting everything

</v-clicks>

</div>

<div>

<v-clicks>

### Horizontal Scalability
Add more agents to handle more work — throughput scales linearly with agent count for parallelizable tasks

### Compositional Flexibility
Combine agents like LEGO blocks — reuse a "code review" agent across multiple workflows without modification

</v-clicks>

<div v-click class="mt-6 p-4 bg-green-900 bg-opacity-30 rounded">

**The result**: Multi-agent systems match how expert human teams work — specialists collaborating in parallel, each handling their domain, coordinated by a shared goal

</div>

</div>

</div>

---
layout: default
zoom: 0.85
---

# Multi-Agent Pitfalls & Failure Modes

<div class="grid grid-cols-2 gap-4 mt-1 text-sm">

<div>

<v-clicks>

**Complexity Explosion** — Each agent added multiplies coordination surface area; debugging a 5-agent system is exponentially harder

**Cascading Failures** — One agent's bad output silently poisons downstream agents; errors compound before anything raises an alarm

**Context Fragmentation** — Agents have partial world views; critical information may not be passed, leading to contradictory decisions

**Runaway Costs** — Every agent hop burns tokens; a 6-agent pipeline can cost 10× more than a well-prompted single agent

</v-clicks>

</div>

<div>

<v-clicks>

**Non-Determinism** — Parallel agents + async handoffs = results that change between runs; nearly impossible to reproduce bugs

**Latency Chains** — Sequential agent dependencies stack latency; 5 agents × 3s each = 15s minimum, with no easy short-circuit

**Orchestration Deadlocks** — Agents waiting on each other, circular dependencies, or resource contention can silently stall everything

</v-clicks>

<div v-click class="mt-3 p-3 bg-orange-900 bg-opacity-40 rounded border border-orange-500">

**Golden Rule:** Start with the simplest architecture that could work.
Multi-agent adds real overhead — only reach for it when a single agent genuinely can't do the job.

</div>

</div>

</div>

<!--
Multi-agent is powerful but not free — every benefit has a corresponding cost.

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

# Sequential Workflow Pattern (Prompt Chaining)

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

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

<div v-click class="dense-col">

## Use Cases

- **Document Generation**: Outline → Validate → Write → Format
- **Data Processing**: Extract → Transform → Summarize
- **Content Creation**: Research → Draft → Edit → Publish

**Benefits**: Clear separation of concerns · Easy to debug · Reusable components · Predictable behavior

<p class="mt-2 text-orange-300 text-xs">Best for well-defined transformations where steps are known upfront</p>

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

Key limitation: No decision-making. If you need branching logic, you need routing or agentic patterns.
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

# Hierarchical Workflow Pattern

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

<v-clicks>

1. **Coordinator Agent**: High-level planning and delegation
2. **Worker Agents**: Specialized execution
3. **Task Breakdown**: Coordinator decomposes goals
4. **Assignment**: Delegate to appropriate workers
5. **Collection**: Gather and synthesize results

</v-clicks>

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:file-tree class="inline"/> Parent-child relationship for delegation
</div>

</div>

<div v-click class="dense-col">

## Use Cases

- **Complex Projects**: Break into sub-projects with specialists
- **Task Orchestration**: Coordinator manages workflow
- **Resource Management**: Allocate workers efficiently
- **Phased Execution**: Sequential delegation with dependencies

## Benefits

- 📋 Clear responsibility hierarchy
- 🎯 Specialized worker expertise
- 🔄 Coordinator handles complexity
- ✅ Centralized monitoring

## When to Use

When tasks have clear hierarchy and need central coordination

</div>

</div>

<!--
Hierarchical pattern is closely related to the Planning pattern, but with multiple specialized workers.

The coordinator is like a project manager who:
1. Understands the goal
2. Breaks it into tasks
3. Assigns tasks to specialized workers
4. Monitors progress
5. Synthesizes final deliverable

Example: Building a web application
- Coordinator: Understands "build todo app"
- Frontend Worker: Builds UI
- Backend Worker: Builds API
- Database Worker: Designs schema
- Test Worker: Writes tests

Coordinator collects outputs and ensures they integrate correctly.

Key difference from Multi-Agent: Hierarchical has clear parent-child relationships. Multi-Agent can be peer-to-peer.
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

# Routing Pattern (Handoff)

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

<v-clicks>

1. **Classifier LLM**: Analyzes incoming request
2. **Categorization**: Determines type/complexity
3. **Route Decision**: Select appropriate handler
4. **Delegation**: Send to specialized agent/model
5. **Response**: Handler provides result

</v-clicks>

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:graph class="inline"/> Smart dispatch to specialists
</div>

</div>

<div v-click class="dense-col">

## Use Cases

- **Customer Support**: Route by category (billing, technical, product)
- **Model Selection**: Simple → cheap model, Complex → advanced
- **Domain Routing**: Weather, Science, Finance specialists
- **Load Balancing**: Distribute across available handlers

## Benefits

- 💰 Cost optimization (use right-sized models)
- ⚡ Latency optimization (fast models for simple)
- 🎯 Quality optimization (specialists for domains)
- 📊 Separation of concerns

## When to Use

When requests have clear categories with specialized handlers

</div>

</div>

<!--
Routing is Phil Schmid's workflow pattern for intelligent delegation.

Phil Schmid's definition: "An initial LLM classifies user input and directs it to specialized downstream handlers based on category"

Classic example: Customer support triage
User: "I can't log in"
Router: Classifies as "Technical Support"
→ Routes to Technical Support Agent (specialized for auth issues)

User: "Why was I charged twice?"
Router: Classifies as "Billing"
→ Routes to Billing Agent (has access to payment systems)

Performance benefit: Simple queries can go to smaller/cheaper models, complex queries to advanced models.

Implementation: Router LLM generates classification, system routes based on that classification.

85-95% routing accuracy is achievable (from 2025 architecture guide).
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

# Human-in-the-Loop Pattern

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

<v-clicks>

1. **Agent Execution**: Agent performs initial task
2. **Pause Point**: System stops for human review
3. **Human Decision**: Approve, reject, or modify
4. **Incorporation**: Human feedback guides next steps
5. **Resume**: Continue with human-guided direction

</v-clicks>

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:account class="inline"/> Critical checkpoints for human wisdom
</div>

</div>

<div v-click class="dense-col">

## Use Cases

- **High-Stakes Decisions**: Legal, medical, financial domains
- **Content Moderation**: Human review of sensitive content
- **Approval Workflows**: Multi-stage business processes
- **Safety-Critical**: Systems where errors are unacceptable

## Benefits

- 🛡️ Risk mitigation (human oversight)
- ✅ Quality assurance (expert review)
- ⚖️ Compliance (regulatory requirements)
- 🎯 Trust building (human accountability)

## When to Use

When decisions are too critical for full automation or require domain expertise

</div>

</div>

<!--
Human-in-the-Loop (HITL) is essential for high-stakes scenarios.

Key principle: Agents handle routine work, humans make critical decisions.

Example: Document generation workflow
1. Agent drafts contract
2. HITL: Lawyer reviews critical terms
3. Agent incorporates lawyer's edits
4. HITL: Client approves final version
5. Agent processes finalized contract

Balance: Too many HITL checkpoints slow workflow, too few reduce quality/safety.

Design consideration: Where to place HITL checkpoints?
- Before irreversible actions
- After complex decisions
- When confidence is low
- When regulations require it

Real-world analogy: Manufacturing assembly line with quality control stations.
-->

---
layout: default
background: '#000000'
title: Human-in-the-Loop Diagram
---

<div class="flex items-center justify-center h-full">
  <img src="/images/human-in-the-loop.png" class="max-h-full max-w-full object-contain rounded-xl" />
</div>

---
layout: default
zoom: 0.85
---

# Feedback Loop Pattern

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

<v-clicks>

1. **Initial Output**: Agent generates first attempt
2. **Evaluation**: System or agent evaluates quality
3. **Feedback Generation**: Identify improvements needed
4. **Refinement**: Agent incorporates feedback
5. **Iterate**: Repeat until quality threshold met

</v-clicks>

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:refresh class="inline"/> Self-improvement through iteration
</div>

</div>

<div v-click class="dense-col">

## Use Cases

- **Code Generation**: Write → Test → Fix → Repeat
- **Content Refinement**: Draft → Critique → Revise
- **Optimization**: Propose → Evaluate → Improve
- **Conversation**: Respond → Assess → Refine

## Benefits

- 🎯 Quality improvement (iterative refinement)
- 📈 Adaptive behavior (learn from mistakes)
- 🔄 Self-correction (automatic refinement)
- ⚡ Efficiency (fewer manual interventions)

## When to Use

When output quality can be measured and iterative refinement is beneficial

</div>

</div>

<!--
Feedback Loop pattern enables autonomous quality improvement.

Key insight: If you can evaluate output, you can iteratively improve it.

Example: Code generation with tests
1. Agent writes function
2. Run tests → 2 failures
3. Agent analyzes failures, updates code
4. Run tests → all pass
5. Success!

Feedback sources:
- Automated tests (code generation)
- Quality metrics (content generation)
- User feedback (conversational agents)
- Self-evaluation (reflection-style)

Design considerations:
- Maximum iterations (prevent infinite loops)
- Convergence criteria (when to stop)
- Feedback quality (garbage in, garbage out)
- Cost vs. benefit (each iteration costs tokens)

Synergy: Combine with Reflection pattern for self-evaluation feedback loop.

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
zoom: 0.78
---

# Models by Agentic Pattern

<div class="mt-2">

| Pattern | Best Model Type | Recommended Models | Key Reason |
|---------|----------------|-------------------|------------|
| **Reflection** | Reasoning / thinking | o3, Claude (extended thinking) | Deep self-critique requires extended reasoning |
| **Feedback Loop** | Reasoning / thinking | o3, Claude (extended thinking) | Evaluate + regenerate demands analytical depth |
| **Planning** | Reasoning / thinking | o3, Gemini 2.5 Pro, Claude thinking | Multi-step decomposition benefits from long-horizon reasoning |
| **Tool Use** | Function-calling specialists | Claude 3.7 Sonnet, GPT-4o, Gemini 2.5 | Reliable structured outputs and tool invocations |
| **Multi-Agent** | Tiered | Sonnet/GPT-4o (orchestrator) + Haiku/Flash (workers) | Strong orchestration, cheap parallel workers |
| **Hierarchical** | Tiered | o3 / Sonnet (planner) + Haiku / Flash (executors) | Quality planning + high-throughput execution |
| **Human-in-the-Loop** | Any capable | Claude Sonnet, GPT-4o | Human handles critical decisions; model handles drafts |
| **Routing** | Fast classifiers | Claude Haiku, GPT-4o-mini, Gemini Flash | Low-latency, low-cost intent classification |
| **Prompt Chaining** | Efficient per-step | Haiku, GPT-4o-mini, Llama 4 Scout | Simple transforms; cost compounds across steps |
| **Parallelization** | Fast parallel | Haiku, Flash, Llama 4 Scout | High throughput; per-call cost dominates |

</div>

<div class="mt-3 p-3 bg-orange-900 bg-opacity-20 rounded text-sm" v-click>

**Rule of thumb**: Use reasoning models for *cognitive* patterns (reflection, planning, feedback). Use fast/cheap models for *throughput* patterns (routing, chaining, parallelization). Use tiered mixes for *coordination* patterns.

</div>

<!--
Key insight: model selection is not one-size-fits-all — it follows the cognitive demand of the pattern.

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
-->


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

<div class="mt-6 p-3 bg-blue-900 bg-opacity-30 rounded" v-click>

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
