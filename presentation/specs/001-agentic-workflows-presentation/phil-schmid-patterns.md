# Phil Schmid's Agentic Workflow Patterns

**Source**: https://www.philschmid.de/agentic-pattern  
**Date Accessed**: 2026-04-20  
**Context**: Authoritative taxonomy of foundational workflow and agentic patterns

## Pattern Organization

Phil Schmid organizes patterns into two categories:

1. **Workflow Patterns** (Non-Agentic): Sequential, deterministic flows without autonomous decision-making
2. **Agentic Patterns**: Autonomous decision-making, tool use, and iterative refinement

---

## Workflow Patterns (Non-Agentic)

### 1. Prompt Chaining

**Definition**: "The output of one LLM call sequentially feeds into the input of the next LLM call"

**Characteristics**:
- Fixed, predictable sequence of steps
- Each step transforms data for the next
- Decomposition of complex tasks into manageable sub-tasks

**Use Cases**:
- Structured document generation (outline → validation → content)
- Multi-step data processing (extract → transform → summarize)
- Newsletter generation from curated inputs

**Example Flow**:
```
Input Text → Summarize → Translate to French → Format as Markdown → Output
```

**Benefits**:
- Clear separation of concerns
- Easier debugging (inspect intermediate outputs)
- Reusable components

---

### 2. Routing (Handoff)

**Definition**: "An initial LLM classifies user input and directs it to specialized downstream handlers based on category"

**Characteristics**:
- Classification at the entry point
- Specialized handlers for different categories
- Separation of concerns through delegation

**Use Cases**:
- Customer support routing (billing vs technical vs product)
- Tiered model selection (simple → cheap, complex → advanced)
- Specialized content generation workflows

**Example Flow**:
```
User Query → Classifier LLM → 
  - Weather query → Weather Handler (specialized model/tools)
  - Science query → Advanced Model Handler
  - Simple query → Basic Model Handler
```

**Benefits**:
- Cost optimization (route simple queries to cheaper models)
- Quality optimization (route complex queries to specialized handlers)
- Reduced latency (smaller models for simple tasks)

---

### 3. Parallelization

**Definition**: "Independent subtasks processed simultaneously by multiple LLMs with aggregated outputs synthesized by a final LLM"

**Characteristics**:
- Concurrent execution of independent tasks
- Aggregation of diverse outputs
- Map-reduce style operations

**Use Cases**:
- RAG with decomposed queries (parallel searches)
- Document analysis (split into sections, analyze in parallel)
- Multiple perspective generation (diverse viewpoints → synthesis)
- Large-scale data operations

**Example Flow**:
```
Task → Split into 3 independent subtasks →
  - Subtask 1 (parallel) → Result 1
  - Subtask 2 (parallel) → Result 2
  - Subtask 3 (parallel) → Result 3
→ Aggregate → Final synthesized output
```

**Benefits**:
- Improved latency (parallel processing)
- Enhanced quality (diverse outputs provide broader coverage)
- Scalability (add more parallel workers as needed)

---

## Agentic Patterns (Autonomous Decision-Making)

### 4. Reflection Pattern

**Definition**: "An agent generates output, evaluates it against criteria, and iteratively refines based on feedback"

**Characteristics**:
- Self-correction loop
- Evaluation against quality criteria
- Iterative refinement
- Also called "Evaluator-Optimizer"

**Use Cases**:
- Code generation with error correction
- Writing refinement (draft → critique → revise)
- Complex problem-solving with feasibility checks
- Information retrieval with validation

**Example Flow**:
```
Generate Initial Output → Evaluate Against Criteria →
  If meets criteria: Done ✓
  If not: Generate Feedback → Refine Output → Repeat (max N iterations)
```

**Implementation Pattern**:
```python
for iteration in range(max_iterations):
    output = generate(prompt)
    evaluation = evaluate(output, criteria)
    if evaluation.passed:
        return output
    feedback = create_feedback(evaluation)
    prompt = augment_prompt_with_feedback(prompt, feedback)
return output  # Return best effort after max iterations
```

**Benefits**:
- Self-correcting behavior
- Higher quality outputs
- Reduced need for human review
- Consistent quality standards

---

### 5. Tool Use Pattern (Function Calling)

**Definition**: "LLM invokes external functions/APIs by generating structured output matching required schemas, receives results, and formulates final response"

**Characteristics**:
- Schema-driven function invocation
- External system integration
- "Vastly extends the LLM's capabilities beyond its training data"

**Use Cases**:
- Appointment booking via calendar APIs
- Real-time data retrieval (stock prices, weather)
- Vector database searches for RAG
- Smart home device control
- Code execution

**Example Flow**:
```
User: "What's the weather in Paris?"
LLM: Determines need for weather API
     Generates: function_call(name="get_weather", args={"location": "Paris"})
System: Executes function → returns {"temp": 18, "condition": "sunny"}
LLM: Formulates response: "It's 18°C and sunny in Paris"
```

**Tool Schema Example**:
```json
{
  "name": "get_weather",
  "description": "Get current weather for a location",
  "parameters": {
    "type": "object",
    "properties": {
      "location": {"type": "string", "description": "City name"}
    },
    "required": ["location"]
  }
}
```

**Benefits**:
- Real-world actionability
- Up-to-date information access
- Integration with existing systems
- Extensibility (add new tools without retraining)

---

### 6. Planning Pattern (Orchestrator-Workers)

**Definition**: "Central planner generates dynamic multi-step task breakdown assigned to specialized workers, with orchestrator synthesizing results and potentially re-planning"

**Characteristics**:
- Dynamic task decomposition
- Specialized worker delegation
- Orchestrator for synthesis and coordination
- Adaptive re-planning based on results

**Use Cases**:
- Complex software development (plan → code → test → document)
- Research reports (search → extract → analyze → write)
- Multi-modal tasks (image + text integration)
- Trip planning (flights + hotels + activities)

**Example Flow**:
```
Goal: "Create a blog post about AI agents"

Planner:
  1. Research current AI agent trends
  2. Write outline
  3. Draft content sections
  4. Review and refine

Workers:
  - Research Worker → executes task 1
  - Writing Worker → executes tasks 2, 3
  - Review Worker → executes task 4

Orchestrator: Synthesizes outputs into final blog post
```

**Benefits**:
- Reduces cognitive load on single LLM
- Improves reasoning quality through specialization
- Enables parallel execution (if no dependencies)
- Dynamic adaptation to intermediate results

---

### 7. Multi-Agent Pattern

**Definition**: "Multiple distinct agents with specific roles/expertise collaborate autonomously or semi-autonomously, coordinated centrally or through handoff logic"

**Characteristics**:
- Each agent has unique role and specialized knowledge
- Autonomous or semi-autonomous operation
- Coordination via central controller or handoff
- Role-based collaboration

**Use Cases**:
- Debates or brainstorming (different personas)
- Complex software creation (PM + coder + tester + critic)
- Virtual experiments (agents as different actors)
- Collaborative content creation

**Example Flow**:
```
Customer Request: "Book a hotel with restaurant"

Coordinator:
  → Hotel Booking Agent: 
    - Searches hotels
    - Books room
    - Checks if restaurant needed
  → Restaurant Booking Agent: (handoff from Hotel Agent)
    - Searches restaurants
    - Books reservation
  
Coordinator: Synthesizes confirmations → Response to customer
```

**Agent Roles Example**:
```python
agents = [
    Agent(role="Product Manager", expertise="requirements, priorities"),
    Agent(role="Developer", expertise="implementation, code"),
    Agent(role="QA Tester", expertise="testing, quality"),
    Agent(role="Critic", expertise="review, feedback")
]
```

**Benefits**:
- Specialization improves output quality
- Parallel collaboration possible
- Mimics human team dynamics
- Scalable (add more agents for new capabilities)

---

## Implementation Best Practices

### 1. Simplicity First
> "Always seek the simplest solution first"

- Use **Workflow Patterns** for well-defined tasks where steps are known
- Use **Agentic Patterns** when flexibility, adaptability, and model-driven decisions are needed
- Don't over-engineer: start simple, add complexity only when needed

### 2. Robust Error Handling
> "Agentic systems must incorporate robust error logging, exception handling, and retry mechanisms"

**Critical considerations**:
- Tool calls can fail (API timeouts, rate limits)
- LLM outputs can be malformed
- External systems can be unavailable
- Agents can get stuck in loops

**Implementation requirements**:
- Comprehensive logging at each step
- Graceful degradation for tool failures
- Retry logic with exponential backoff
- Maximum iteration limits for loops
- Circuit breakers for external dependencies

### 3. Iterative Optimization
> "Define metrics, measure performance, identify bottlenecks...and iterate"

**Optimization cycle**:
1. **Define Metrics**: Latency, cost, quality, success rate
2. **Measure Baseline**: Current performance
3. **Identify Bottlenecks**: Profiling and analysis
4. **Optimize**: Target specific bottlenecks
5. **Re-measure**: Validate improvements
6. **Iterate**: Continuous improvement

**Common optimizations**:
- Caching frequent tool call results
- Parallelizing independent operations
- Using smaller models for simple tasks
- Prompt optimization for clarity/conciseness

### 4. Pattern Composition
> "Patterns aren't mutually exclusive—real systems combine multiple patterns"

**Common compositions**:
- **Planning + Tool Use**: Planner creates tasks, workers use tools to execute
- **Multi-Agent + Routing**: Coordinator routes tasks to specialized agents
- **Reflection + Parallelization**: Generate multiple outputs in parallel, reflect on each
- **Routing + Hierarchical**: Router sends to coordinator, coordinator delegates to workers

**Design principle**: Build complex systems by composing simple, proven patterns

---

## When to Use Each Pattern

| Pattern | Best For | Avoid When |
|---------|----------|------------|
| **Prompt Chaining** | Well-defined sequential transformations | Steps require dynamic decision-making |
| **Routing** | Clear categorization with specialized handlers | Categories overlap or are ambiguous |
| **Parallelization** | Independent subtasks with no dependencies | Subtasks have sequential dependencies |
| **Reflection** | Quality-critical outputs needing refinement | Real-time latency requirements |
| **Tool Use** | Need for external data or actions | Pure text generation suffices |
| **Planning** | Complex multi-step goals with dependencies | Simple, single-step tasks |
| **Multi-Agent** | Diverse expertise needed, collaborative workflows | Single perspective sufficient |

---

## Framework Recommendations

Phil Schmid's article provides pure API implementations but acknowledges these frameworks:

- **LangChain**: Rapid prototyping, extensive integrations
- **LangGraph**: Complex multi-agent workflows, graph-based state
- **LlamaIndex**: RAG and document-centric workflows
- **CrewAI**: Role-based agent teams, clean API

**Note**: The article emphasizes understanding patterns at the API level before adopting frameworks, to avoid framework lock-in and understand underlying mechanics.

---

## Key Takeaways

1. **Taxonomy matters**: Distinguish workflow patterns (deterministic) from agentic patterns (autonomous)
2. **Simplicity first**: Use the simplest pattern that solves the problem
3. **Composition is powerful**: Real systems combine multiple patterns
4. **Robustness is critical**: Error handling, logging, retries are non-negotiable
5. **Measure and iterate**: Define metrics, optimize bottlenecks, repeat
6. **Tool use is transformative**: "Vastly extends LLM capabilities beyond training data"
7. **Reflection improves quality**: Self-correction loop reduces human review burden

---

## Integration with Other Taxonomies

### Overlap with 2025 Architecture Guide

Phil Schmid's foundational patterns map to 2025 guide architectures:

| Phil Schmid Pattern | 2025 Guide Architecture |
|---------------------|------------------------|
| Tool Use | Single Agent + Tools |
| Routing | Single Agent + Router |
| Planning | Hierarchical with delegation |
| Multi-Agent | Dynamic Agent Delegation |
| Parallelization | Parallel Agents execution |
| Reflection | Internal loop mechanism |

**Combined value**: Phil Schmid provides conceptual foundation, 2025 Guide adds performance metrics and modern compositions.
