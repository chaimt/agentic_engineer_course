---
theme: default
background: '#000000'
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Agentic Workflows
  
  Educational presentation on agentic workflows - understanding the shift from AI as autocomplete to AI as development partner.
  
  Learn about:
  - What agentic workflows are and how they differ from LLMs
  - Practical implementation patterns
  - Advanced workflow techniques
  - Real-world applications
drawings:
  persist: false
transition: slide-left
title: Agentic Workflows
controls: false
hideInToc: True
mdc: true
---

<div class="flex flex-col items-center justify-center h-full gap-4">



<h1 class="text-6xl font-extrabold tracking-tight" style="color:#ff8c00;text-shadow:0 0 40px #ff6b0066,0 2px 8px #0008;">
  Agentic Workflows
</h1>

<p class="text-2xl font-light mt-1" style="color:#ffb86090;">
  From AI Autocomplete to Development Partner
</p>

<div class="pt-4 cursor-pointer" @click="$slidev.nav.next">
  <img src="/images/agentic-hero.png" alt="Agentic Hero" class="w-128 opacity-95 rounded-xl shadow-lg"/>
</div>

</div>

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <mdi:pencil />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <mdi:github />
  </a>
</div>

<!--
Welcome to the Agentic Workflows presentation!

This presentation will take you on a journey from understanding basic LLM capabilities to implementing sophisticated agentic workflows in your development practice.

Target time: 30-45 minutes total
- Introduction and concepts: 8 min
- Benefits and use cases: 7 min
- Workflow patterns: 10 min
- Practical tips: 8 min
- Q&A: 7 min
-->

---
layout: default
---

# Presentation Overview

<v-clicks>

## What We'll Cover

1. 🤖 **Understanding Agentic Workflows** - What they are and why they matter
2. 🔧 **Tools & Memory Fundamentals** - The building blocks of agentic systems
3. 💡 **Benefits** - Real-world productivity gains and industry adoption
4. 🔄 **Workflow Patterns** - Core patterns for practical implementation
5. 🛠️ **Practical Tips** - Getting started and best practices
6. ❓ **Q&A** - Your questions and discussion

</v-clicks>

<!--
This is your roadmap for the next 30-45 minutes.

We'll start with foundational concepts, explore practical patterns, and finish with tips for adoption.

Each section builds on the previous one, so we'll progress from theory to practice.
-->

---
src: ./pages/01-concepts.md
---

---
layout: default
zoom: 0.85
---

# Prompt Engineering Techniques

<div class="grid grid-cols-3 gap-3 mt-1" style="font-size:0.78rem;">

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**🎯 Zero-Shot**

No examples — rely on the model's training knowledge alone.

<p class="mt-1 text-orange-300 italic">"Classify as positive / negative / neutral: 'The flight was okay.'"<br/>→ <strong>Neutral</strong></p>

</div>

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**📚 Few-Shot**

Provide example pairs to guide in-context learning.

<p class="mt-1 text-orange-300 italic">"A baku is a large blue bird. 'We saw bakus in Maui.' → Now write a story about a baku on a ship."</p>

</div>

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**🔗 Chain-of-Thought**

Break complex tasks into explicit reasoning steps.

<p class="mt-1 text-orange-300 italic">"I had 8, gave 3, found 4. <em>Think step by step.</em>"<br/>→ 8−3=5, 5+4=<strong>9</strong></p>

</div>

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**🏗️ Meta Prompting**

Define structure and format, not specific content.

<p class="mt-1 text-orange-300 italic">Step 1: Define variables.<br/>Step 2: Apply formula.<br/>Step 3: Simplify & solve.</p>

</div>

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**♻️ Self-Consistency**

Sample multiple reasoning paths, pick the most consistent answer.

<p class="mt-1 text-orange-300 italic">"At 6 my sister was 3, gap = 3 yrs always."<br/>→ At 70, sister is <strong>67</strong></p>

</div>

<div v-click class="p-3 bg-orange-900 bg-opacity-20 rounded border border-orange-800">

**🎭 Role Prompting**

Assign a persona to shape tone, priorities and domain focus.

<p class="mt-1 text-orange-300 italic">"You are a skeptical VC. List top 3 pros and cons of this pitch."</p>

</div>

</div>

<!--
Prompt engineering is the foundation before agents even enter the picture.

Six key techniques from simple to advanced:

1. Zero-Shot — no examples, just clear instructions. Works well for tasks the model was trained on.

2. Few-Shot — show don't just tell. Examples dramatically improve performance on novel or ambiguous tasks.

3. Chain-of-Thought — "think step by step" unlocks multi-step reasoning. Critical for math, logic, and planning tasks.

4. Meta Prompting — define structure abstractly, not with specific content. Excellent for token efficiency and generalization.

5. Self-Consistency — sample multiple reasoning paths and vote for the most consistent answer. Great for arithmetic and commonsense tasks.

6. Role Prompting — "You are a security auditor" changes what the model prioritizes. Aligns model behavior with domain expectations.

These techniques compose with each other — e.g., Few-Shot + Chain-of-Thought is especially powerful for complex reasoning.

Source: k2view.com/blog/prompt-engineering-techniques/
-->

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
src: ./pages/02-tools-memory.md
---

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
---

<div class="flex items-center justify-center h-full">
  <img src="/images/feedback-loop-diagram.png" class="max-h-full max-w-full object-contain rounded-xl" />
</div>

---
layout: section-header
---

# arunpshankar Reference Patterns

Advanced implementations from production use cases

<!--
These patterns come from arunpshankar's GitHub reference implementation repository.

Four unique patterns beyond what we've covered:
1. Web Access - Specialized agent pipeline for web content
2. Dynamic Sharding - Adaptive parallel processing for large datasets
3. Dynamic Decomposition - AI-generated task breakdown
4. DAG Orchestration - Declarative workflow dependencies

Each demonstrates sophisticated real-world agent architectures.

Duration: 8-10 minutes for all four patterns
-->

---
layout: default
---

# Web Access Pattern

<div class="grid grid-cols-2 gap-4 text-sm">

<div>

## How It Works

<v-clicks>

1. **Search Agent**: Queries web using SERP API
2. **Scrape Agent**: Extracts content from URLs
3. **Summarize Agent**: Synthesizes information
4. **Sequential Chain**: Single responsibility per agent
5. **Tool Specialization**: Web-specific capabilities

</v-clicks>

<div v-click class="mt-3 p-3 bg-orange-900 bg-opacity-20 rounded text-xs">
<mdi:magnify class="inline"/> Three-stage pipeline for web content processing
</div>

</div>

<div v-click>

## Use Cases

- **Research Automation**: Gather info from web sources
- **Competitive Analysis**: Monitor competitor websites
- **Content Aggregation**: Summarize news/articles
- **Market Intelligence**: Track industry trends

## Benefits

- Specialized agents for each step
- Clean separation of concerns
- Tool-use best practices
- Structured information extraction

## When to Use

Systematically gather and process web content with clear stages

</div>

</div>

<!--
Web Access Pattern is a practical application of sequential workflow with tool use.

Three specialized agents:
1. Search Agent: Uses SERP API to find relevant URLs
2. Scrape Agent: Extracts content from each URL  
3. Summarize Agent: Synthesizes information across sources

Key insight: Single-responsibility principle for agents. Each agent does one thing well.

Example workflow:
User: "Research latest trends in agentic AI"
→ Search Agent: Finds 10 relevant articles
→ Scrape Agent: Extracts content from each
→ Summarize Agent: Creates comprehensive summary

Tool specialization: Each agent uses domain-specific tools (SERP API, web scraping libraries, summarization prompts).

Design consideration: Error handling at each stage (failed searches, inaccessible URLs, parsing errors).

Real-world application: Automated research assistants, competitive intelligence gathering, content curation pipelines.
-->

---
layout: image
image: /images/parallel-workflow.png
backgroundSize: contain
---

---
src: ./pages/05-architectures.md
---

---
src: ./pages/06-principles.md
---

---

# References & Further Reading

<div class="grid grid-cols-2 gap-4 mt-2 text-sm">

<div>

## Pattern References

- **[Agentic Workflow Patterns](https://www.philschmid.de/agentic-pattern)**  
  Philipp Schmid — Prompt Chaining, Routing, Parallelization, Reflection, Tool Use, Planning, Multi-Agent

- **[Agentic Workflow Patterns (GitHub)](https://github.com/arunpshankar/Agentic-Workflow-Patterns)**  
  arunpshankar — Python implementations: Reflection, Web Access, Routing, Sharding, Task Decomposition, DAG Orchestration

- **[The Ultimate Guide to AI Agent Architectures in 2025](https://dev.to/sohail-akbar/the-ultimate-guide-to-ai-agent-architectures-in-2025-2j1c)**  
  Dev.to — 8 modern architectural compositions with performance benchmarks

</div>

<div>

## Additional Resources

- **[Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code)** — CLAUDE.md, hooks, MCP setup
- **[Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)** — Core principles
- **[LangGraph](https://langchain-ai.github.io/langgraph/)** — Stateful multi-agent workflows
- **[AutoGen](https://microsoft.github.io/autogen/)** — Microsoft's multi-agent framework
- **[CrewAI](https://www.crewai.com/)** — Role-based agent teams
- **[MCP Protocol](https://modelcontextprotocol.io/)** — Universal tool adapter standard

</div>

</div>

<!--
Three primary research sources for this presentation:

1. Philipp Schmid (philschmid.de): The foundational taxonomy used as the pedagogical backbone — 7 core patterns from simple to complex.

2. arunpshankar (GitHub): Python reference implementations demonstrating best practices. Adds Actor-Critic framing to Reflection, coordinator-delegate to Routing, DAG Orchestration as a new pattern.

3. Dev.to 2025 Architecture Guide: Modern real-world architectural compositions — the 8 patterns that show how foundational patterns combine in production systems.
-->
