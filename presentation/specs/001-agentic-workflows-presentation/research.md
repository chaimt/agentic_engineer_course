# Research: Agentic Workflows Presentation

**Date**: 2026-04-16 | **Feature**: 001-agentic-workflows-presentation

## R1: Slidev Framework Setup & Best Practices

**Decision**: Use standard Slidev project structure with custom theme overrides

**Rationale**: Slidev provides a well-documented structure with built-in support for code highlighting, presenter mode, and UnoCSS theming — ideal for a developer-focused technical presentation.

**Key Findings**:
- Project structure: `slides.md` (main), `components/`, `layouts/`, `styles/`, `public/`, `snippets/`, `uno.config.ts`
- Import code snippets via `<<< @/snippets/file.js` syntax; supports VS Code regions for partial includes
- Use frontmatter for slide-level config; first block is deck-level ("headmatter")
- Built-in layouts: `cover`, `default`, `image-left`, `two-cols`; custom layouts override defaults
- Presenter mode shows slide preview + speaker notes; access via built-in UI
- Limitations: broad CSS can break presenter UI; TwoSlash doesn't sync between presenter/viewer modes; speaker notes display space is constrained

**Alternatives Considered**:
- reveal.js: More mature but less developer-friendly markdown workflow
- PowerPoint/Google Slides: No code-first workflow, no git integration

## R2: Google Slides Theme Extraction

**Decision**: NEEDS USER INPUT — Google Slides reference requires authentication

**Rationale**: The referenced presentation (https://docs.google.com/presentation/d/1KEfu6VjQZBZscsg7GodkjttD9GPi3pRvP65boUg7IMY) is not publicly accessible. Theme details (colors, fonts, layout patterns) cannot be programmatically extracted.

**Resolution Path**: User must either:
1. Export the Google Slides as PDF/images and share locally, OR
2. Provide a written description of the theme (background color, accent colors, fonts, logo), OR
3. Grant public access to the presentation

**Fallback**: If theme details unavailable by implementation time, use a clean dark developer theme (dark background, light text, syntax-highlighted code) as default, adjustable later.

**Alternatives Considered**:
- Programmatic Google Slides API export: Requires OAuth credentials not available
- Screenshot analysis: Requires manual export step from user

## R3: Agentic Workflow Core Concepts

**Decision**: Structure concepts around the shift from "AI as autocomplete" to "AI as development partner"

**Rationale**: Target audience has casual AI tool experience (Copilot/ChatGPT). The presentation must bridge from their current mental model (AI completes code snippets) to the agentic paradigm (AI executes multi-step workflows with tools).

**Key Concepts to Cover**:
- **Definition**: Agentic workflows chain AI capabilities across multiple steps, with each step building on the last using tools (file reads, shell commands, API calls, web searches)
- **Key Shift**: Engineers focus on architecture, specifications, and review rather than line-by-line implementation
- **Trust Model**: Trust grows with usage — new users auto-approve ~20% of actions, experienced users reach 40%+
- **Adoption Signal**: At Anthropic, majority of code is now written by Claude Code

**Alternatives Considered**:
- Starting with academic AI agent taxonomy: Too theoretical for practitioner audience
- Multi-vendor comparison approach: Dilutes focus; spec clarification chose Claude Code as primary

## R4: Claude Code Features for Demo

**Decision**: Demo the following Claude Code features in order of audience impact

**Rationale**: Selected features that show the broadest value proposition and are visually impressive in a live demo context.

**Demo Features (ordered)**:
1. **CLAUDE.md** — Project guidelines file; show how it shapes agent behavior (keep under 200 lines)
2. **Interactive CLI workflow** — Show Claude Code reading code, making edits, running tests in a real project
3. **Hooks** — User-defined commands at lifecycle points; demo linting/formatting on commit
4. **MCP (Model Context Protocol)** — Universal adapter connecting Claude to external tools (GitHub, databases, Sentry)
5. **Sub-agents** — Orchestrated specialized agents for complex tasks (if time permits — P2 content)

**Alternatives Considered**:
- Showing API-level agent building: Too low-level for target audience
- Multi-agent orchestration deep-dive: Better suited for advanced workshop, not 45-60 min talk

## R5: Agentic Workflow Patterns

**Decision**: Present 4 core patterns with practical examples

**Rationale**: These patterns cover the spectrum from simple to advanced, matching the presentation's concept-first arc.

**Patterns**:
1. **Prompt-Driven Development**: Structured prompts turning vague intent into reliable agent execution
2. **Spec-Driven Development (SDD)**: Write formal Markdown specifications first; becomes single source of truth for AI execution
3. **Test-Driven Development with AI**: AI writes both code and tests; test suite gives agents concrete iteration targets
4. **Multi-Agent Collaboration**: Specialized agents coordinated by an orchestrator (mention briefly as advanced pattern)

**Alternatives Considered**:
- Sequential/split-and-merge/headless patterns: Too architectural for target audience level
- Tool-specific patterns: Less transferable knowledge

## R6: Challenges & Practical Tips Content

**Decision**: Frame challenges as "things to know" rather than blockers; pair each with a practical tip

**Rationale**: Target audience is evaluating adoption. Presenting challenges without solutions creates anxiety rather than confidence.

**Challenge → Tip Pairings**:
1. Inconsistent output quality → Use CLAUDE.md to encode project standards and reduce variability
2. Trust and verification → Start with bounded tasks; implement hooks for quality gates (linting, security)
3. Context loss across sessions → Write specifications that preserve decision rationale
4. Security concerns → Understand what code/data the agent can access; configure permissions appropriately
5. Team coordination → Establish shared CLAUDE.md standards; use spec-driven workflows for alignment

**Alternatives Considered**:
- Deep-dive into enterprise governance: Too heavy for a 45-60 min talk
- Ignoring challenges entirely: Would reduce credibility with experienced developers

## R7: Presentation Section Breakdown

**Decision**: 6-section concept-first arc with approximate timing

**Rationale**: Aligns with FR-001 clarification and constitution's progressive skill building principle.

| Section | Duration | Slides | Content |
|---------|----------|--------|---------|
| 1. What Are Agentic Workflows | 8 min | 5-7 | Definition, key concepts, mental model shift |
| 2. Why They Matter | 7 min | 4-5 | Benefits, adoption signals, industry trends |
| 3. Live Claude Code Demo | 15 min | 3-5 | CLAUDE.md setup, interactive CLI workflow, hooks |
| 4. Workflow Patterns | 10 min | 6-8 | Prompt-driven, spec-driven, TDD with AI, multi-agent |
| 5. Practical Tips | 8 min | 5-6 | Getting started, challenges & solutions, best practices |
| 6. Q&A | 7 min | 1-2 | Questions, resources, next steps |
| **Total** | **~55 min** | **~30-35** | |

**Alternatives Considered**:
- 45 min compressed version: Drops patterns section to P2; viable for shorter slots
- 60 min extended version: Adds audience polling/interactive elements between sections

---

## Technical Implementation Research

The following research findings resolve technical clarifications from plan.md.

## R8: Slidev Theme Customization Implementation

**Decision**: Extend an existing Slidev theme using local customization with UnoCSS configuration and custom Vue layouts

**Rationale**: Building from scratch requires excessive effort for brand matching. Slidev's theme system is designed for extension, not reinvention. UnoCSS theme config provides granular color/spacing control while custom layouts enable precise visual matching.

**Implementation Structure**:
```
slides/
├── uno.config.ts         # Color scheme, spacing, typography
├── theme/
│   ├── layouts/          # Custom .vue slide layouts
│   ├── components/       # Reusable Vue components
│   └── styles/           # Global CSS overrides
└── slides.md             # Frontmatter specifies theme
```

**Key Steps**:
1. Select base theme from [Slidev Theme Gallery](https://sli.dev/resources/theme-gallery)
2. Configure colors via `uno.config.ts` theme section
3. Create custom layouts in `theme/layouts/` for brand-specific slides
4. Add global style overrides in `theme/styles/`

**Alternatives Considered**:
- Build custom theme from scratch: Rejected due to time investment
- Fork published theme: Rejected to avoid divergence from upstream

## R9: Code Example Best Practices

**Decision**: Use Shiki syntax highlighting with progressive line highlighting and Monaco Editor for interactive examples

**Rationale**: Shiki provides superior syntax highlighting. Progressive highlighting enables step-by-step code walkthroughs. Monaco Editor gives audience familiar VS Code experience.

**Implementation Patterns**:

Progressive highlighting (click-through):
````markdown
```js{1|3-5|7}
// Step 1: Setup
const agent = new Agent();
// Step 2: Configure
agent.loadConfig();
agent.setContext();
// Step 3: Execute
agent.run();
```
````

Interactive Monaco Editor:
````markdown
```js{monaco}
// Editable code
const demo = () => console.log("Try editing!");
```
````

Magic Move (animated transitions):
`````markdown
````magic-move{lines: true}
```js
const x = 1;
```
```js
const x = 2;
const y = 3;
```
````
`````

**Best Practices**:
- Limit to ≤20 lines per code block
- Use line highlighting to focus attention
- Test all code snippets for syntax correctness
- Maintain examples in `/examples/` directory

**Alternatives Considered**:
- Plain code blocks: Insufficient for educational clarity
- External playground embeds: Network dependency risk
- TwoSlash integration: Rejected due to sync issues in presenter mode

## R10: Asset Management Strategy

**Decision**: Organize assets in `public/` directory with absolute path referencing and format-specific subdirectories

**Rationale**: `public/` assets are served at root `/`, ensuring consistent paths. Absolute paths work reliably in both markdown and frontmatter. Format-based organization improves maintainability.

**Directory Structure**:
```
public/
├── screenshots/      # PNG workflow captures (<200KB each)
├── diagrams/         # SVG concept diagrams
└── demos/            # MP4 demo videos (H.264, 720p-1080p)
```

**Optimization Guidelines**:
- Screenshots: PNG, compress to <200KB
- Diagrams: SVG preferred for scaling
- Videos: MP4 with H.264, 2-5 Mbps, <60 seconds
- Limit: Maximum 5 assets per slide

**Alternatives Considered**:
- Relative paths: Rejected due to inconsistency
- GIF animations: Rejected due to file size; MP4 preferred

## R11: Speckit-Slidev Integration

**Decision**: Specification-driven architecture with automated generation from `specs/` to `slides/`

**Rationale**: Aligns with Constitutional Principle IV: "Specification-Driven Slides". Maintains single source of truth. Prevents content duplication.

**Integration Architecture**:
```
specs/001-agentic-workflows-presentation/
├── sections/
│   ├── 01-concepts.spec.md        # Learning objectives, key concepts
│   ├── 02-benefits.spec.md
│   └── ...
└── code-examples/                  # Executable code

slides/sections/                    # Generated (read-only)
├── 01-concepts.md
└── ...
```

**Workflow**:
1. Author content specifications in `specs/sections/*.spec.md`
2. Generate Slidev markdown via build script
3. Render presentation with Slidev

**Alternatives Considered**:
- Manual sync: Rejected due to drift risk
- Slides as source of truth: Violates Content-First Development principle

## R12: Live Demo Workflow

**Decision**: Structured rehearsal process with pre-tested scripts, terminal setup, and multi-layered backup strategy

**Rationale**: Live demos are critical success factor (SC-005). Rehearsal reduces failure probability. Backup recordings provide fail-safe.

**Rehearsal Schedule**:
- Full run-through #1 (3 days before): Identify issues
- Full run-through #2 (1 day before): Validate fixes
- Abbreviated run-through #3 (1 hour before): Final verification

**Demo Timing**: 15 minutes total
- 3 min: Introduction
- 9 min: Active demo (3 segments × 3 min each)
- 3 min: Wrap-up and Q&A

**Backup Strategy**:
- Layer 1: Screen recordings (primary backup)
- Layer 2: Screenshot fallbacks (partial failures)
- Layer 3: Presenter notes (narration guide)

**Terminal Configuration**:
- Theme: High contrast (dark background, light text)
- Font: Menlo/Monaco 16pt minimum
- Clear command history before start

**Recovery Protocol**:
- If fails within 30 seconds → attempt recovery
- If fails beyond 30 seconds → switch to recording
- Maximum 2 minutes for recovery attempt

**Alternatives Considered**:
- Fully live, no backups: Too risky
- Fully pre-recorded: Less engaging
- Audience hands-on: Rejected per spec (presenter-driven only)

---

## R13: arunpshankar/Agentic-Workflow-Patterns GitHub Repository

**Source**: https://github.com/arunpshankar/Agentic-Workflow-Patterns  
**Companion Article**: https://medium.com/google-cloud/designing-cognitive-architectures-agentic-workflow-patterns-from-scratch-63baa74c54bc  
**Decision**: Incorporate 4 unique patterns from this repo not yet covered in the spec, and enrich existing pattern descriptions with concrete implementation details.

**Rationale**: This is one of the most cited Python pattern libraries for agentic workflows, implemented against Google Cloud / Vertex AI. The patterns are concrete, runnable, and represent well-named architectural conventions. Four patterns (Web Access, Dynamic Sharding, Dynamic Decomposition, DAG Orchestration) provide significant coverage gaps in the current spec.

**Repository Overview**:
- Language: Python 94.4%, Mermaid 5.6%
- Platform: Google Cloud Platform / Vertex AI + SERP API
- Structure: `src/patterns/<name>/pipeline.py` as the main entry point per pattern
- Data: `data/patterns/<name>/` holds prompt templates, JSON schemas, and outputs
- Credentials: GCP service account key (`credentials/key.json`) + SERP API key (`credentials/key.yml`)

**All 8 Patterns with Implementation Details**:

### Pattern 1 — Reflection (Actor-Critic Framework)
- **Implementation**: Two-agent loop — Actor generates content, Critic reviews it, loop continues until quality threshold
- **Key Mechanics**: Iterative refinement via continuous feedback; Actor and Critic are separate LLM calls with different system prompts
- **Maps to**: T034-T036 (Reflection Pattern) — already covered; enrich slide with Actor-Critic framing
- **Code Path**: `src/patterns/reflection/pipeline.py`

### Pattern 2 — Web Access (Search → Scrape → Summarize Pipeline)
- **Implementation**: Three specialized agents in pipeline: SearchAgent (SERP API), ScrapeAgent (HTML extraction), SummarizeAgent (content distillation)
- **Key Mechanics**: Each agent is single-responsibility; chained sequentially with handoff data
- **Use Case**: Information retrieval workflows, research automation
- **Maps to**: NEW — not currently in spec; complements Tool Use pattern with web-specific specialization
- **Code Path**: `src/patterns/web_access/pipeline.py`

### Pattern 3 — Semantic Routing (Coordinator-Delegate Architecture)
- **Implementation**: TravelPlannerAgent acts as coordinator; routes to FlightAgent, HotelAgent, CarRentalAgent based on semantic intent classification
- **Key Mechanics**: Intent classification via LLM → deterministic routing to domain specialists
- **Maps to**: T057-T059 (Routing Pattern) — already covered; enrich with "coordinator-delegate" terminology and travel planning example

### Pattern 4 — Parallel Delegation (NER-Based Entity Extraction)
- **Implementation**: Named Entity Recognition (NER) identifies distinct entities in a query; each entity delegated to a specialized agent running concurrently
- **Key Mechanics**: Entity extraction → parallel fan-out → result aggregation
- **Maps to**: T047-T049 (Parallel Workflow) — already covered; enrich with NER-based delegation framing
- **Code Path**: `src/patterns/parallel_delegation/pipeline.py`

### Pattern 5 — Dynamic Sharding (Large Dataset Parallel Processing)
- **Implementation**: Input dataset dynamically split into N shards based on size/complexity; each shard processed by a worker agent in parallel; results merged
- **Key Mechanics**: Adaptive sharding strategy (not fixed-size); demonstrated with celebrity biography fetching via web search
- **Use Case**: Large-scale data processing, batch enrichment pipelines
- **Maps to**: NEW — distinct from parallel delegation (data-driven vs entity-driven); add as standalone pattern
- **Code Path**: `src/patterns/dynamic_sharding/pipeline.py`

### Pattern 6 — Task Decomposition (Predefined Sub-Task Agents)
- **Implementation**: Complex task broken into predefined independent subtasks; each managed by a dedicated Sub-Task Agent with its own context and tools
- **Key Mechanics**: Static decomposition (human-defined subtask list); parallel or sequential Sub-Task Agents
- **Maps to**: T040-T042 (Planning Pattern) — closely related; enrich slide with Sub-Task Agent framing and distinction from dynamic decomposition

### Pattern 7 — Dynamic Decomposition (LLM-Generated Subtasks)
- **Implementation**: An orchestrator LLM receives the complex task and autonomously generates a list of subtasks (no predefined decomposition); each subtask routed to a SubtaskAgent
- **Key Mechanics**: Decomposition itself is AI-generated — enables open-ended task handling; subtask list is dynamic and context-dependent
- **Use Case**: Open-ended research, complex content generation, adaptive workflows
- **Maps to**: NEW — distinct from static Task Decomposition; the LLM designs its own plan
- **Code Path**: `src/patterns/dynamic_decomposition/pipeline.py`

### Pattern 8 — DAG Orchestration (YAML-Defined Directed Acyclic Graph)
- **Implementation**: Workflow structure defined in YAML as a DAG; orchestrator reads DAG, resolves dependencies, executes nodes in topological order; supports parallel branches
- **Key Mechanics**: Declarative workflow definition; dependency graph determines execution order; non-blocking parallel branches execute concurrently
- **Use Case**: Complex multi-step workflows with interdependencies, ETL pipelines, build systems
- **Maps to**: NEW — most sophisticated orchestration pattern; enables declarative multi-agent orchestration
- **Code Path**: `src/patterns/dag_orchestration/pipeline.py`

**Key Implementation Insights for Slides**:
- All patterns follow a `pipeline.py` entry point convention — good for showing "how to run" in demos
- Credential setup is two-step: GCP service account + SERP API key — relevant for "Getting Started" slide
- Patterns use modular agent classes with clear single responsibilities — validates separation of concerns principle
- Actor-Critic is the canonical Reflection implementation — use this framing in the Reflection slide

**New Patterns to Add to Spec** (4 gaps identified):
1. **Web Access** — Search/Scrape/Summarize pipeline (specialized tool-use chain)
2. **Dynamic Sharding** — Data-volume-driven parallel processing (distinct from entity-driven parallel delegation)
3. **Dynamic Decomposition** — LLM-autonomously-generated subtask planning (distinct from predefined task decomposition)
4. **DAG Orchestration** — YAML-declarative dependency-aware workflow execution (most advanced orchestration pattern)

---

## R14: Tools and Memory Fundamentals (NEW REQUIREMENT 2026-04-24)

**Decision**: Add comprehensive Tools and Memory section before agent architectures, with practical RAG system example

**Rationale**: User explicitly requested: "before describing agents add a slide about tools and memory and how they work. in addition bring an example of a rag system that uses tools and memory"

**Pedagogical Benefit**: Understanding tools and memory as building blocks helps audience comprehend how patterns and architectures combine these primitives.

### Tools: Agent-Computer Interface (ACI)

**Definition**: Structured interfaces that extend LLM capabilities beyond text generation by enabling interaction with external systems, APIs, databases, and computational resources.

**Key Concepts**:
1. **Tool Structure** (Anthropic API format):
   - Name and description (agent decides when to use)
   - Input schema (typed parameters with validation)
   - Execution logic (actual functionality)
   - Output format (structured response)

2. **Tool Categories**:
   - Information Retrieval: Search, database queries, API calls
   - Computation: Math operations, data processing, code execution
   - Action Execution: File operations, system commands, external service integration
   - Memory Access: Vector store queries, context retrieval, conversation history

3. **Implementation Example**:
```python
{
  "name": "search_codebase",
  "description": "Search code repository for function definitions, class names, or keywords",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {"type": "string", "description": "Search query or keyword"},
      "file_types": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["query"]
  }
}
```

**Best Practices** (from Anthropic's Building Effective Agents):
- Detailed descriptions help agent decide when to call
- Clear input schemas prevent malformed requests
- Structured outputs enable agent parsing and use
- Error handling helps agent recover from failures

### Memory: Stateful Context Management

**Definition**: Memory systems enable agents to maintain context across interactions, store learned information, and retrieve relevant historical data to inform current decisions.

**Key Concepts**:
1. **Memory Types**:
   - **Short-term Memory**: Conversation context within token limits (~200K tokens for Claude 3.5)
   - **Long-term Memory**: Persistent storage (vector databases, traditional databases, file systems)
   - **Semantic Memory**: Embeddings-based retrieval (RAG pattern)
   - **Episodic Memory**: Structured records of past interactions, decisions, outcomes

2. **Memory Operations**:
   - Storage: Save information for future retrieval
   - Retrieval: Query relevant information based on current context
   - Update: Modify existing memories as understanding evolves
   - Pruning: Remove outdated or irrelevant information

3. **Memory Architecture Patterns**:
   - Context Window Management: Fit recent context within token limits
   - Retrieval-Augmented Generation (RAG): Query external knowledge on-demand
   - Hybrid Memory: Combine context window + vector store + structured DB
   - Shared Memory: Multiple agents access common knowledge base

4. **Implementation Approaches**:
```python
# Vector Store (Semantic Memory)
vector_store = WeaviateClient(
    collection="documentation",
    embedding_model="text-embedding-3-large"
)

# Structured Memory (Episodic)
db.query(
    "SELECT solution, resolution_time FROM tickets "
    "WHERE error_code = '429' AND status = 'resolved'"
)
```

### RAG Example: API Support Agent with Tools + Memory

**Use Case**: Customer support agent helping developers troubleshoot API integration issues

**Architecture Demonstration**:

```
User Query: "My API calls are returning 429 errors"
       ↓
[Agent receives query + conversation history]
       ↓
┌──────────────────────────────────────────┐
│  TOOLS (Action Execution)                │
│  ✓ search_issue_tracker("429 errors")   │
│  ✓ check_api_rate_limits(user_id)       │
│  ✓ fetch_recent_logs(last_hour)         │
└──────────────────────────────────────────┘
       ↓
┌──────────────────────────────────────────┐
│  MEMORY (RAG - Knowledge Retrieval)      │
│  ✓ Vector search: "rate limiting best   │
│    practices" in documentation           │
│  ✓ Retrieve: Past solutions for 429s    │
│  ✓ Find: API quota upgrade procedures   │
└──────────────────────────────────────────┘
       ↓
[Agent synthesizes: Logs show 1000 req/min,
 limit is 100/min. Documentation recommends
 exponential backoff. Past solutions suggest
 upgrading to Enterprise tier.]
       ↓
Response: "You're hitting rate limits (100/min).
Implement exponential backoff (code example from
docs). For higher limits, upgrade to Enterprise."
```

**Implementation Details**:

1. **Tools Used**:
```python
tools = [
    {
        "name": "search_issue_tracker",
        "description": "Search past support tickets and issues",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "status": {"type": "string", "enum": ["open", "closed", "all"]}
            }
        }
    },
    {
        "name": "check_rate_limits",
        "description": "Get current API usage and limits for a user",
        "input_schema": {
            "type": "object",
            "properties": {
                "user_id": {"type": "string"}
            }
        }
    },
    {
        "name": "fetch_logs",
        "description": "Retrieve API request logs for debugging",
        "input_schema": {
            "type": "object",
            "properties": {
                "time_range": {"type": "string"},
                "filter": {"type": "string"}
            }
        }
    }
]
```

2. **Memory (RAG) Retrieval**:
```python
# Vector Store Setup
vector_store = WeaviateClient(
    collection="api_documentation",
    embedding_model="text-embedding-3-large"
)

# Semantic Search
def retrieve_relevant_docs(query: str, k: int = 5):
    embedding = get_embedding(query)
    results = vector_store.similarity_search(
        embedding=embedding,
        limit=k,
        filters={"category": ["troubleshooting", "rate-limits"]}
    )
    return results

# Hybrid Memory: Vector + Structured
past_solutions = db.query(
    "SELECT solution, resolution_time FROM tickets "
    "WHERE error_code = '429' AND status = 'resolved' "
    "ORDER BY created_at DESC LIMIT 10"
)
```

3. **Complete Workflow**:
```python
# Agent receives query
user_query = "My API calls are returning 429 errors"

# Execute tools in parallel
tool_results = await execute_parallel([
    search_issue_tracker("429 errors"),
    check_rate_limits(user_id),
    fetch_logs(last_hour)
])

# Query memory (RAG)
relevant_docs = retrieve_relevant_docs(
    query="API rate limiting troubleshooting",
    k=3
)
past_solutions = get_similar_resolutions(error_code="429")

# Synthesize with full context
context = {
    "user_query": user_query,
    "tool_results": tool_results,
    "documentation": relevant_docs,
    "past_solutions": past_solutions
}

response = agent.generate_response(context)
```

**Performance Benefits**:
- **Tool Use**: Real-time data access (current limits, logs) vs outdated knowledge
- **RAG Memory**: 37% faster resolution (from Pattern #3: MCP + Tools benchmark in spec)
- **Combined**: Reduced back-and-forth (agent has full context immediately)

**Slide Structure** (4 slides total):

1. **"What are Tools?"**
   - Definition: Structured interfaces for agent-external system interaction
   - Categories: Information, Computation, Action, Memory Access
   - Code example: Tool definition structure
   - Key point: Tools transform LLMs into agents

2. **"What is Memory?"**
   - Definition: Stateful context management across interactions
   - Types: Short-term (context window) vs Long-term (vector stores, DBs)
   - Memory operations: Store, Retrieve, Update, Prune
   - Key point: Memory enables learning and context-aware responses

3. **"Tools + Memory in Action: RAG Support Agent"**
   - Use case: API troubleshooting support
   - Architecture diagram showing query → tools → memory → synthesis
   - Code walkthrough: Tool calls + RAG retrieval
   - Results: Faster resolution, better accuracy, learned from past issues

4. **"Why This Matters"**
   - Without tools: Agent can only generate text from training knowledge
   - Without memory: Agent repeats same mistakes, lacks personalization
   - Together: Powerful, context-aware, action-capable agents
   - Transition: "Now let's see how to architect these into complete systems..."

**Integration into Presentation Flow**:

Updated Section Order (inserted after live demo, before patterns):
1. Introduction: What are agentic workflows
2. Why they matter
3. Live Claude Code demo
4. **NEW: Fundamentals - Tools and Memory** (18 minutes: 5 min tools + 5 min memory + 8 min RAG example)
5. Foundational Workflow Patterns (Phil Schmid's 7 patterns)
6. Modern Architecture Patterns (2025 guide's 8 patterns)
7. Anthropic Building Effective Agents principles
8. Practical implementation tips
9. Q&A

**Time Budget Impact**:
- Tools + Memory section: 18 minutes
- Remaining for patterns/principles/Q&A: 42 minutes (within 60-minute constraint)

**Alternatives Considered**:
- Integrate tools/memory into pattern sections - rejected because it dilutes focus and loses coherent narrative
- Add at beginning before demo - rejected because lacks context, audience won't appreciate importance
- Add at end after patterns - rejected because too late, patterns already introduced concepts

---

## Research Complete

All technical clarifications from plan.md resolved:
- ✅ Slidev theme customization approach
- ✅ Code example implementation patterns
- ✅ Asset management strategy
- ✅ Speckit-Slidev integration workflow
- ✅ Live demo rehearsal and backup procedures
- ✅ **NEW: Tools and Memory fundamentals with RAG system example**

**Next Phase**: Phase 1 - Design & Contracts (data-model.md, contracts/, quickstart.md)
