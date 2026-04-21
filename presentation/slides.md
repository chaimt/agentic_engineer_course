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
mdc: true
---

# Agentic Workflows

From AI Autocomplete to Development Partner

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space to start <mdi:arrow-right class="inline"/>
  </span>
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

Target time: 45-60 minutes total
- Introduction and concepts: 8 min
- Benefits and use cases: 7 min
- Live demonstration: 15 min
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
2. 💡 **Benefits and Use Cases** - Real-world applications and advantages
3. 🎯 **Live Claude Code Demo** - See agentic workflows in action
4. 🔄 **Workflow Patterns** - Core patterns for practical implementation
5. 🛠️ **Practical Tips** - Getting started and best practices
6. ❓ **Q&A** - Your questions and discussion

</v-clicks>

<!--
This is your roadmap for the next 45-60 minutes.

We'll start with foundational concepts, then see a live demonstration, explore practical patterns, and finish with tips for adoption.

Each section builds on the previous one, so we'll progress from theory to practice.
-->

---
layout: section-header
---

# Section 1: Understanding Agentic Concepts

What are agentic workflows and how do they differ from traditional AI tools?

<!--
Section 1 is your foundation. 

We'll define key terms, establish the mental model shift required, and explore what makes agentic workflows fundamentally different from tools like Copilot or ChatGPT.

Duration: 8 minutes
-->

---
layout: default
---

# What is an LLM?

<v-clicks>

## Large Language Model (LLM)

- **Definition**: AI model trained on vast amounts of text to understand and generate human-like text
- **Core Capability**: Pattern recognition and text completion
- **Interaction Model**: Request → Response (stateless)
- **Limitations**: 
  - No ability to take actions in the real world
  - No memory across conversations (without explicit context)
  - No ability to use tools or access external systems

</v-clicks>

<div v-click class="mt-8 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:information class="inline"/> Think of an LLM as a highly sophisticated autocomplete engine.
</div>

<!--
LLMs like GPT-4, Claude, or Llama are powerful text processors.

They excel at understanding context and generating coherent responses, but they're fundamentally reactive and stateless.

Every interaction starts fresh unless you explicitly provide context.

Key limitation: They can suggest code but can't write files, run tests, or execute commands on their own.
-->

---
layout: default
---

# What is an Agent?

<v-clicks>

## AI Agent

- **Definition**: An AI system that can autonomously take actions to achieve goals
- **Core Capability**: Goal-oriented behavior with tool use
- **Interaction Model**: Goal → Plan → Execute → Verify (stateful)
- **Key Characteristics**:
  - **Autonomy**: Can execute multi-step workflows without constant human input
  - **Tool Use**: Can interact with external systems (files, APIs, databases, shell)
  - **Memory**: Maintains context and state across operations
  - **Feedback Loops**: Can observe results and adjust behavior

</v-clicks>

<div v-click class="mt-8 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:robot class="inline"/> Think of an agent as an LLM with hands and memory.
</div>

<!--
Agents are LLMs plus agency - the ability to act.

The critical difference: Agents don't just suggest what to do, they actually do it.

They can read files, write code, run tests, search documentation, call APIs, and chain these actions together.

They maintain state across a session, building up context as they work.
-->

---
layout: default
---

# LLM vs Agent: Key Differences

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

## LLM (Language Model)

<v-clicks>

- 📝 **Reactive**: Responds to prompts
- 🔄 **Stateless**: No memory between requests
- 💬 **Suggests**: Provides recommendations
- 🚫 **Read-only**: Cannot modify systems
- 🎯 **Single-turn**: One question, one answer

</v-clicks>

</div>

<div>

## Agent (AI Agent)

<v-clicks>

- 🤖 **Proactive**: Executes towards goals
- 🧠 **Stateful**: Maintains context
- ⚡ **Acts**: Executes commands
- ✏️ **Read-write**: Can modify files, run tests
- 🔁 **Multi-turn**: Plans and executes workflows

</v-clicks>

</div>

</div>

<div v-click class="mt-8 p-4 bg-orange-900 bg-opacity-30 rounded border-l-4 border-orange-500">
<mdi:arrow-right class="inline"/> <strong>The Shift</strong>: From "AI suggests code" to "AI writes, tests, and deploys code"
</div>

<!--
This comparison highlights the fundamental paradigm shift.

LLMs are consultants - they advise but don't execute.
Agents are teammates - they do the work alongside you.

The key enabler: Tool use. Agents can call functions, run shell commands, read/write files, and chain these actions.

Example:
- LLM: "You should add a user model to models/user.py"
- Agent: *Creates models/user.py, writes the code, runs tests, commits changes*
-->

---
layout: default
---

# LLM vs Agent: Interactive Comparison

<LlmAgentComparison />

<div class="mt-8 p-4 bg-orange-900 bg-opacity-30 rounded text-center">
<mdi:lightbulb class="inline"/> The transformation: From passive advisor to active partner
</div>

<!--
This interactive component visualizes the key differences side-by-side.

Notice the pattern:
- LLMs are fundamentally passive - they wait for input and provide output
- Agents are fundamentally active - they pursue goals through action

The bridge between them: Tool use and memory.

When you give an LLM the ability to call functions and maintain state across calls, it becomes an agent.
-->

---
layout: default
---

# Agentic Workflows Defined

<v-clicks>

## What is an Agentic Workflow?

A **structured process** where AI agents autonomously execute multi-step tasks using:

1. 🎯 **Goal Understanding**: Interpret high-level objectives
2. 📋 **Planning**: Break down goals into executable steps
3. 🛠️ **Tool Use**: Interact with files, APIs, databases, shell commands
4. 🔄 **Execution Loops**: Run actions, observe results, adjust approach
5. ✅ **Verification**: Test outcomes and validate success

</v-clicks>

<div v-click class="mt-8">

## Real-World Example

```mermaid
graph LR
    A[User: Add login] --> B[Agent: Plan steps]
    B --> C[Create auth model]
    C --> D[Write tests]
    D --> E[Implement service]
    E --> F[Run tests]
    F --> G[Verify & commit]
    style A fill:#ff6b35
    style G fill:#ff9f1c
```

</div>

<!--
Agentic workflows transform vague requests into concrete implementations.

Key insight: The workflow is a closed loop - the agent observes outcomes and course-corrects.

Traditional development: Human plans → Human codes → Human tests → Human debugs
Agentic workflow: Human sets goal → Agent plans → Agent codes → Agent tests → Agent debugs → Human reviews

The human role shifts from executor to reviewer and decision-maker.

This is not autopilot - it's co-pilot with agency.
-->

---
layout: default
---

# Benefits of Agentic Workflows

<v-clicks>

## Why Adopt Agentic Workflows?

### 🚀 Productivity Gains
- **Faster iteration**: Agent handles boilerplate and repetitive tasks
- **Parallel exploration**: Test multiple approaches simultaneously
- **24/7 execution**: Agents work while you sleep

### 🎯 Quality Improvements
- **Consistency**: Agents follow patterns and conventions reliably
- **Testing**: Automated test generation and execution
- **Documentation**: Code and docs stay synchronized

### 💡 Cognitive Benefits
- **Focus shift**: From typing to reviewing and decision-making
- **Reduced context switching**: Agent maintains project state
- **Learning amplification**: See expert patterns in action

### 🔧 Practical Advantages
- **Onboarding**: New team members productive faster
- **Legacy codebases**: Navigate unfamiliar code with AI guide
- **Cross-domain work**: Get help in unfamiliar tech stacks

</v-clicks>

<!--
The benefits span multiple dimensions - not just speed, but quality and learning too.

Real stat: Developers report 30-55% time savings on routine tasks when using agentic workflows effectively.

Key insight: The biggest benefit isn't speed - it's the elevation of your work. You move from code monkey to architect and reviewer.

Warning: This requires trust-but-verify mindset. Agents are powerful but not infallible.
-->

---
layout: default
---

# Use Cases: Where Agentic Workflows Shine

<div class="grid grid-cols-2 gap-6 mt-6">

<div v-click>

### 🏗️ **Greenfield Projects**
- Scaffold new projects from specs
- Set up CI/CD pipelines
- Generate boilerplate with tests

</div>

<div v-click>

### 🔧 **Refactoring**
- Rename variables across codebase
- Extract functions and classes
- Update imports and dependencies

</div>

<div v-click>

### 🐛 **Debugging**
- Trace errors through stack traces
- Add logging and instrumentation
- Reproduce and fix bugs

</div>

<div v-click>

### 📚 **Documentation**
- Generate API documentation
- Update README files
- Create usage examples

</div>

<div v-click>

### ✅ **Testing**
- Write unit and integration tests
- Add test coverage
- Generate test fixtures

</div>

<div v-click>

### 🔄 **Migrations**
- Update dependencies
- Migrate to new frameworks
- Refactor deprecated APIs

</div>

</div>

<div v-click class="mt-8 p-4 bg-orange-900 bg-opacity-30 rounded">
<mdi:lightbulb class="inline"/> <strong>Common pattern</strong>: Tasks that are well-defined but tedious are perfect for agentic workflows
</div>

<!--
Agentic workflows excel at tasks with clear success criteria but high execution cost.

Best candidates: Structured, repeatable, verifiable tasks
Poor candidates: Ambiguous requirements, novel algorithms, high-stakes security decisions

The sweet spot: Tasks you understand how to do but don't want to spend time doing manually.

Real example: "Add input validation to all 47 API endpoints" - tedious for humans, perfect for agents.
-->

---
layout: section-header
---

# Section 2: Practical Implementation

How to build and use agentic workflows in real projects

<!--
Section 2 shifts from theory to practice.

We'll explore the toolkit - patterns, frameworks, and techniques for implementing agentic workflows.

This section covers 18 patterns total: 10 foundational workflow patterns + 8 modern agent architectures.

Duration: 25-30 minutes
-->

---
layout: default
---

# Getting Started with Agentic Workflows

<v-clicks>

## Prerequisites

### Development Environment
- Modern IDE (VS Code, Cursor, or similar)
- Git for version control
- Package manager (npm, pip, cargo, etc.)

### AI Development Tools
- **Claude Code** (Primary recommendation) - Anthropic's agentic CLI
- Alternatives: GitHub Copilot, Cursor AI, or other AI-assisted tools
- API access to LLM providers (Anthropic, OpenAI, etc.)

### Conceptual Prerequisites
- Familiarity with command line / terminal
- Basic understanding of AI/LLM capabilities
- Comfort with iterative development

</v-clicks>

<div v-click class="mt-8 p-4 bg-orange-900 bg-opacity-30 rounded">
<mdi:check class="inline"/> You don't need to be an AI expert - these tools are designed for working developers
</div>

<!--
The barrier to entry is lower than you might think.

If you can use Git and run terminal commands, you can start with agentic workflows today.

Claude Code is the recommended starting point - it's specifically designed for software development workflows and has excellent integration with existing tools.

No PhD required - the AI handles the complexity, you guide the direction.
-->

---
layout: default
---

# Pattern Categories Overview

<div class="grid grid-cols-2 gap-6 mt-4">

<div v-click>

### 🎯 Core Patterns
Fundamental building blocks

- **Reflection** - Self-review and improvement
- **Tool Use** - External system integration
- **Planning** - Task decomposition

</div>

<div v-click>

### 🔄 Workflow Patterns
Execution control flow

- **Sequential** - Step-by-step execution
- **Parallel** - Concurrent task handling

</div>

<div v-click>

### 🤝 Coordination Patterns
Multi-agent collaboration

- **Multi-Agent** - Collaborative execution
- **Hierarchical** - Parent-child relationships
- **Routing** - Specialized task delegation

</div>

<div v-click>

### 🎛️ Control Patterns
Oversight and feedback

- **Human-in-the-Loop** - Human oversight
- **Feedback Loop** - Iterative refinement

</div>

</div>

<div v-click class="mt-8 p-4 bg-orange-900 bg-opacity-30 rounded text-center">
<mdi:lightbulb class="inline"/> <strong>Plus 8 Modern Architectures</strong> from the 2025 Architectural Guide
</div>

<!--
These 10 foundational patterns can be combined and composed to build sophisticated agentic workflows.

Think of them as LEGO blocks - each pattern solves a specific problem, and you combine them to build complete systems.

We'll also explore 8 cutting-edge architectural patterns from 2025's definitive guide, showing the latest advances in agent systems.

Pattern selection depends on your specific use case - we'll cover selection criteria at the end.

The beauty: Start simple (single pattern) and grow complexity only as needed.
-->

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

<div v-click>

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

<div v-click>

## Common Tools

- File system (read/write/delete)
- Shell commands
- APIs (REST, GraphQL)
- Databases (SQL, NoSQL)
- Version control (git)
- Package managers (npm, pip)

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

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:sitemap class="inline"/> From "what" to "how" automatically
</div>

</div>

<div v-click>

## Example Decomposition

**Goal**: "Add user authentication"

**Plan**:
1. Create user model
2. Implement password hashing
3. Build login endpoint
4. Add JWT generation
5. Create middleware
6. Write tests

## Benefits

- 📋 Structured approach
- 🎯 Clear progress tracking
- 🔄 Handles complexity
- ✅ Verifiable completion

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

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:pipe class="inline"/> Like a pipeline: each stage transforms the input
</div>

</div>

<div v-click>

## Use Cases

- **Document Generation**: Outline → Validate → Write → Format
- **Data Processing**: Extract → Transform → Summarize
- **Content Creation**: Research → Draft → Edit → Publish

## Benefits

- ✅ Clear separation of concerns
- ✅ Easy to debug (inspect intermediate outputs)
- ✅ Reusable components
- ✅ Predictable behavior

## When to Use

Perfect for well-defined transformations where steps are known upfront

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

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:arrow-left-right class="inline"/> Map-Reduce for LLMs
</div>

</div>

<div v-click>

## Use Cases

- **RAG**: Decompose query → parallel searches → aggregate
- **Document Analysis**: Split sections → analyze each → synthesize
- **Diverse Perspectives**: Generate multiple viewpoints → combine
- **Batch Processing**: Process items concurrently

## Benefits

- ⚡ Improved latency (parallel execution)
- 🎯 Enhanced quality (diverse outputs)
- 📈 Scalability (add more workers)
- 🔄 Better coverage (multiple approaches)

## When to Use

When subtasks are independent with no sequential dependencies

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

# Multi-Agent Collaboration Pattern

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

<v-clicks>

1. **Define Agent Roles**: Each agent has specific expertise
2. **Autonomous Operation**: Agents work independently
3. **Collaboration**: Agents communicate and handoff
4. **Coordination**: Central orchestrator or handoff logic
5. **Synthesis**: Combine outputs from all agents

</v-clicks>

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:account-group class="inline"/> Like a team of specialists working together
</div>

</div>

<div v-click>

## Use Cases

- **Software Development**: PM + Coder + Tester + Reviewer agents
- **Content Creation**: Researcher + Writer + Editor agents
- **Complex Analysis**: Different perspectives/domains
- **Virtual Experiments**: Agents as different actors

## Benefits

- 🎯 Specialization improves quality
- 🤝 Mimics human team dynamics
- 📈 Scalable (add more agents)
- 🔄 Parallel collaboration possible

## When to Use

When diverse expertise is needed and tasks benefit from specialized handling

</div>

</div>

<!--
Multi-Agent is Phil Schmid's most sophisticated agentic pattern.

Key insight: "Multiple distinct agents with specific roles/expertise collaborate autonomously or semi-autonomously"

Example: Customer service system
- Hotel Booking Agent: Searches hotels, books rooms
- Restaurant Booking Agent: Handles restaurant reservations
- Coordinator: Routes requests and synthesizes responses

Each agent has unique role and specialized knowledge. They can work in parallel or hand off to each other.

Real-world analogy: A hospital with specialists (cardiologist, neurologist, etc.) who collaborate on complex cases.

Design consideration: How do agents communicate? Options:
1. Central coordinator (orchestrator pattern)
2. Direct handoff (agent-to-agent)
3. Shared message queue
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

<div v-click>

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

<div v-click>

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

<div v-click>

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

<div v-click>

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

<div class="grid grid-cols-2 gap-6">

<div>

## How It Works

<v-clicks>

1. **Search Agent**: Queries web using SERP API
2. **Scrape Agent**: Extracts content from URLs
3. **Summarize Agent**: Synthesizes information
4. **Sequential Chain**: Each agent has single responsibility
5. **Tool Specialization**: Web-specific capabilities

</v-clicks>

<div v-click class="mt-6 p-4 bg-orange-900 bg-opacity-20 rounded">
<mdi:magnify class="inline"/> Three-stage pipeline for web content processing
</div>

</div>

<div v-click>

## Use Cases

- **Research Automation**: Gather information from web sources
- **Competitive Analysis**: Monitor competitor websites
- **Content Aggregation**: Collect and summarize news/articles
- **Market Intelligence**: Track industry trends from web data

## Benefits

- 🔍 Specialized agents for each step
- 🔗 Clean separation of concerns
- 🛠️ Tool-use best practices
- 📊 Structured information extraction

## When to Use

When you need to systematically gather and process web content with clear stages

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

# Placeholder slides for remaining content

More content will be added for:
- Dynamic Sharding Pattern
- Dynamic Decomposition Pattern
- DAG Orchestration Pattern
- Modern Agent Architectures (8 patterns from 2025 guide)
- Anthropic Best Practices
- Live Demonstrations
- Practical Tips
- Q&A

<!--
This is a work in progress. Additional slides will be added as implementation continues.
-->

---

# References & Further Reading

<div class="two-col">

<div>

## Pattern References

- **[Agentic Workflow Patterns](https://www.philschmid.de/agentic-pattern)**  
  Philipp Schmid — Foundational taxonomy: Prompt Chaining, Routing, Parallelization, Reflection, Tool Use, Planning, Multi-Agent

- **[Agentic Workflow Patterns (GitHub)](https://github.com/arunpshankar/Agentic-Workflow-Patterns)**  
  arunpshankar — Python reference implementations: Reflection, Web Access, Semantic Routing, Parallel Delegation, Dynamic Sharding, Task Decomposition, DAG Orchestration

- **[The Ultimate Guide to AI Agent Architectures in 2025](https://dev.to/sohail-akbar/the-ultimate-guide-to-ai-agent-architectures-in-2025-2j1c)**  
  Dev.to — Modern architectural compositions: MCP Servers, Hierarchy+Parallel, Human-in-Loop, Dynamic Delegation, RAG-augmented agents

</div>

<div>

## Additional Resources

- **Anthropic Claude** — Tool use and multi-agent patterns
- **ByteByteGo** — System design for agentic workflows
- **Weaviate** — RAG and vector search integration
- **LangChain / LangGraph** — Framework implementations
- **AutoGen / CrewAI** — Multi-agent orchestration frameworks

</div>

</div>

<!--
Three primary research sources for this presentation:

1. Philipp Schmid (philschmid.de): The foundational taxonomy used as the pedagogical backbone — 7 core patterns from simple to complex.

2. arunpshankar (GitHub): Python reference implementations demonstrating best practices. Adds Actor-Critic framing to Reflection, coordinator-delegate to Routing, DAG Orchestration as a new pattern.

3. Dev.to 2025 Architecture Guide: Modern real-world architectural compositions — the 8 patterns that show how foundational patterns combine in production systems.
-->
