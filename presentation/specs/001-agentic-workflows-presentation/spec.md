# Feature Specification: Agentic Workflows Presentation

**Feature Branch**: `001-agentic-workflows-presentation`
**Created**: 2026-04-14
**Status**: Draft
**Input**: User description: "This project will be a presentation agentic workflows, and should use themes like in the presetation: https://docs.google.com/presentation/d/1KEfu6VjQZBZscsg7GodkjttD9GPi3pRvP65boUg7IMY/edit?slide=id.g36c849d51ab_0_1530#slide=id.g36c849d51ab_0_1530"

**Milestone Reference**: M01: Q2 2026
**Feature PDR Reference**: PDR-001

**Goal**: Create an educational presentation that teaches developers how to implement and use agentic workflows in software engineering
**Success Criteria**: Attendees understand agentic concepts, can identify use cases, and have practical implementation knowledge
**Constraints**: Must be delivered using Slidev framework, content-first approach via Speckit, black and orange color theme

## Demo Sentence *(mandatory)*

**After this feature, the user can:** attend a comprehensive presentation on agentic workflows and leave with practical knowledge of how to implement AI-assisted development workflows in their own projects.

## Boundary Map *(mandatory for multi-feature projects)*

### Produces

| Artifact | Type | Exports/Provides |
|----------|------|------------------|
| slides/ | Slidev Presentation | Interactive slides with code examples and demos |
| examples/ | Code Samples | Practical implementation examples |
| resources/ | Documentation | Additional learning materials and references |

### Consumes

| From Feature | Artifact | Imports/Uses |
|--------------|----------|--------------|
| *(none - leaf feature)* | - | - |

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Understanding Agentic Concepts (Priority: P1)

**Presentation attendee** wants to understand what agentic workflows are and how they differ from traditional development approaches.

**Why this priority**: Foundational knowledge required before any practical application

**Independent Test**: Can be fully tested by quiz/assessment after concept introduction and delivers clear understanding of agentic principles

**Acceptance Scenarios**:

1. **Given** a developer with no prior AI-assisted development experience, **When** they attend the concept introduction, **Then** they can define agentic workflows and explain key differences from traditional development
2. **Given** an experienced developer, **When** they see agentic workflow examples, **Then** they can identify specific benefits and potential use cases in their work

---

### User Story 2 - Practical Implementation Knowledge (Priority: P1)

**Developer** wants to see real-world examples of how to implement agentic workflows in their development process.

**Why this priority**: Practical knowledge is essential for applying concepts to real projects

**Independent Test**: Can be tested through hands-on coding exercise or implementation planning activity

**Acceptance Scenarios**:

1. **Given** a specific development task, **When** shown agentic workflow implementation, **Then** the developer can identify the key components and integration points
2. **Given** their current development environment, **When** presented with setup instructions, **Then** they can plan how to integrate agentic tools into their workflow

---

### User Story 3 - Advanced Workflow Patterns (Priority: P2)

**Experienced developer** wants to learn advanced agentic workflow patterns and optimization techniques.

**Why this priority**: Advanced patterns provide additional value but aren't essential for basic understanding

**Independent Test**: Can be tested through pattern recognition exercises and optimization scenarios

**Acceptance Scenarios**:

1. **Given** a complex development scenario, **When** shown advanced workflow patterns, **Then** they can select appropriate patterns for different situations

---

### Edge Cases

- What happens when agentic tools fail or produce incorrect output?
- How does the workflow handle security-sensitive code that shouldn't be shared with AI systems?
- How do teams coordinate when multiple developers use different agentic tools?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Presentation MUST follow a concept-first structure: (1) What are agentic workflows, (2) Why they matter, (3) Live Claude Code demo, (4) Workflow patterns, (5) Practical tips, (6) Q&A
- **FR-002**: Presentation MUST demonstrate practical implementation examples using Claude Code as the primary agentic tool, with brief mentions of alternative tools (e.g., GitHub Copilot, Cursor)
- **FR-003**: Presentation MUST include presenter-driven live coding demos using Claude Code (audience watches, no hands-on exercises)
- **FR-004**: Presentation MUST provide setup instructions for implementing agentic workflows
- **FR-005**: Presentation MUST address common challenges and solutions in agentic development
- **FR-006**: Presentation MUST include assessment mechanisms to validate learning outcomes
- **FR-007**: Presentation MUST be delivered using Slidev framework, with black and orange color theme providing strong contrast and professional appearance
- **FR-008**: Presentation MUST cover the 8 modern agent architecture patterns from the 2025 guide, each with: definition, use cases, performance metrics, and key limitations:
  1. **Single Agent + Tools** (ReAct pattern) — 50% cheaper than complex architectures
  2. **Sequential Agents** — 15-25% higher completion rate on complex tasks
  3. **Single Agent + MCP Servers + Tools** — 37% faster, 93% vs 78% completion rate
  4. **Agents Hierarchy + Parallel Agents + Shared Tools** — 30-60% execution time reduction
  5. **Single Agent + Tools + Router** — 85-95% routing accuracy
  6. **Single Agent + Human in the Loop + Tools** — 50-80% reduction in critical errors
  7. **Single Agent + Dynamically Call Other Agents** — hub-spoke model, 15-25% accuracy improvement
  8. **Agents Hierarchy + Loop + Parallel Agents + Shared RAG** — 40-60% time reduction
- **FR-009**: Presentation MUST include an implementation frameworks comparison covering LangChain, LangGraph, AutoGen, and CrewAI, with guidance on which framework suits which architecture pattern
- **FR-010**: Presentation MUST include an architecture selection guide with 5 decision criteria: (1) task complexity, (2) specialization needs, (3) control and oversight requirements, (4) resource constraints, (5) framework selection

### Key Entities *(include if feature involves data)*

- **Agentic Workflow**: Structured process that integrates AI assistance into software development
- **Development Task**: Specific coding or engineering activities enhanced by agentic tools
- **AI Agent**: Software component that provides intelligent assistance in development workflows (primary reference: Claude Code CLI agent)
- **Code Example**: Practical implementation demonstrations with before/after comparisons

### Non-Functional Requirements

- **NFR-001**: Presentation MUST be delivered within 45-60 minute timeframe
- **NFR-002**: Slides MUST be visually clear and readable for audience of 10-100 people
- **NFR-003**: Code examples MUST be executable and tested for accuracy
- **NFR-004**: Presentation MUST support audience engagement through presenter-driven live demos (no audience hands-on setup required)
- **NFR-005**: Content MUST target developers who are aware of AI tools but not yet practicing structured agentic workflows, while remaining accessible to complete beginners

### Quality Attributes

- **Clarity**: Concepts explained in terms familiar to software developers
- **Practicality**: All examples based on real development scenarios
- **Engagement**: Interactive elements maintain audience attention and participation
- **Accuracy**: Technical content verified and tested for correctness
- **Completeness**: Covers fundamental concepts through practical implementation
- **Accessibility**: Suitable for developers with different experience levels

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 90% of attendees can correctly define agentic workflows in post-presentation assessment
- **SC-002**: 80% of attendees can identify at least 3 practical use cases for agentic workflows in their work
- **SC-003**: 75% of attendees express confidence in implementing basic agentic workflows after the presentation
- **SC-004**: Presentation maintains audience engagement with average attention score above 85%
- **SC-005**: Code examples execute successfully during live demonstration without errors

## Clarifications

### Session 2026-04-16

- Q: Which specific agentic development tools should the presentation feature? → A: Claude Code (Anthropic's CLI agent) as primary tool, with brief mentions of alternatives
- Q: What high-level structure should the presentation follow? → A: Concept-first arc: What are agentic workflows → Why they matter → Live Claude Code demo → Workflow patterns → Practical tips → Q&A
- Q: What is the primary audience experience level with AI-assisted development? → A: Aware but not practicing — developers who've tried Copilot/ChatGPT casually but lack structured agentic workflows
- Q: What type of interactive elements should be included? → A: Presenter-driven live demos only — presenter codes live with Claude Code while audience watches
- Q: What visual style should the Slidev presentation use? → A: Match the referenced Google Slides color scheme and layout as closely as possible in Slidev

### Session 2026-04-20

- Q: What color scheme should the presentation use? → A: Black and orange theme for strong contrast and professional technical appearance

## Assumptions

- Attendees have basic software development experience and casual exposure to AI coding tools (e.g., Copilot, ChatGPT) but lack structured agentic workflow practices
- Presentation will be delivered to technical audience (developers, engineers, technical leads) who are aware of AI-assisted development but not yet practicing structured workflows
- Audience does not need laptops; all demos are presenter-driven
- Presentation environment supports live coding and screen sharing capabilities
- Attendees are interested in improving their development productivity through AI assistance

## Research Sources

| Source | URL | Key Contribution |
|--------|-----|-----------------|
| The Ultimate Guide to AI Agent Architectures in 2025 | https://dev.to/sohail-akbar/the-ultimate-guide-to-ai-agent-architectures-in-2025-2j1c | 8 modern architecture patterns with performance metrics, framework comparisons, and selection guide |
| Anthropic Claude Code | https://docs.anthropic.com/en/docs/claude-code | Primary agentic tool for live demos |
| ByteByteGo | https://bytebytego.com | System design and distributed patterns |
| Philipp Schmid | https://www.philschmid.de | LLM/agent implementation guides |
| Weaviate | https://weaviate.io | RAG and vector store patterns |

## Architecture Reference *(from 2025 Guide)*

Eight major architecture patterns examined as standards in the field:

### Pattern Performance Benchmarks

| Architecture | Key Metric | Notes |
|---|---|---|
| Single Agent + Tools | ~50% cheaper vs complex alternatives | Pass^8 score <50% on τ-bench |
| Sequential Agents | 15-25% higher completion rate | 30-40% higher domain accuracy |
| Single Agent + MCP Servers | 37% faster, 93% success rate | 42% more tokens (caching overhead) |
| Hierarchy + Parallel + Shared Tools | 25-40% higher completion, 30-60% faster | 45% better task adaptation |
| Single Agent + Router | 85-95% routing accuracy | Claude 3.5: 0.91 score |
| Human in the Loop | 50-80% error reduction | 15-25% quality improvement |
| Dynamic Agent Delegation | 15-25% accuracy improvement | 30-40% token reduction |
| Hierarchy + Loop + Parallel + RAG | 40-60% time reduction, 25-35% quality gain | Most sophisticated pattern |

### Implementation Frameworks

| Framework | Best For | Key Strength | Key Limitation |
|---|---|---|---|
| LangChain | Rapid prototyping, tool integration | Extensive integrations, API abstraction | Rapidly evolving API, frequent breaking changes |
| LangGraph | Complex multi-agent workflows | Graph-based state, human-in-the-loop, time-travel debugging | LangChain dependency, steeper learning curve |
| AutoGen | Conversational multi-agent systems | Conversational paradigm, code execution, No-code GUI | Less structured control flow, limited visualization |
| CrewAI | Role-based agent teams | Clean API, role/goal/backstory design, standalone | Less mature ecosystem, fewer advanced features |

### Architecture Selection Decision Framework

1. **Task complexity** → Simple/focused: Single Agent + Tools | Multi-domain: Dynamic Delegation | Multi-stage: Sequential Agents | Complex research: Hierarchy + Parallel
2. **Specialization needs** → General-purpose: Single Agent | Deep expertise: Multi-agent | Standardized tools: MCP Servers
3. **Control and oversight** → High-stakes: Human in the Loop | Predefined flow: Sequential Agents | Adaptive: Hierarchical
4. **Resource constraints** → Limited compute: Simpler architectures | Performance priority: Specialized multi-agent
5. **Framework selection** → Rapid prototyping: CrewAI or LangChain | Complex workflows: LangGraph | Conversational: AutoGen | Enterprise: AutoGen or LangGraph

## Risk Register *(optional)*

- RISK: Technical demonstration failures | Severity: Medium | Impact: Reduced credibility and learning effectiveness | Test: Verify all code examples work in clean environment before presentation
- RISK: Audience overwhelm with complex concepts | Severity: Low | Impact: Reduced comprehension and engagement | Test: Validate content progression through pilot presentation with target audience
- RISK: Slidev framework limitations | Severity: Low | Impact: Presentation features may not work as expected | Test: Create prototype slides and test all interactive features
