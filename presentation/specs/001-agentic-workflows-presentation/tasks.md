# Tasks: Agentic Workflows Presentation

**Input**: Design documents from `/specs/001-agentic-workflows-presentation/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**NEW REQUIREMENTS** (2026-04-24):
1. Tools and Memory fundamentals section with RAG example
2. **Single vs Multi-Agent limitations slide before workflow patterns**

**SLIDE RESTRUCTURE (2026-04-28)** — Reconciliation of tasks with the active deck `presentation/slides.md`:
- The Live Claude Code Demo section was removed from imports. Tasks T031–T039 (Section 3 demo) are now **OPT-IN** — `pages/03-demo.md` is retained but not part of the active deck.
- Patterns are now **inline in `slides.md`** organized into 4 thematic groups + arunpshankar reference. Tasks T061–T075 (Phil Schmid foundational patterns) and T054–T060 (Why Multi-Agent in `pages/04-patterns.md`) are now **OPT-IN** — `pages/04-patterns.md` is retained but not imported.
- Tools & Memory is now Section 2 of the deck (after Concepts, before Patterns), not Section 4.
- New requirements added: hero/branding visuals, closing References slide, inline section-header slides for the 4 pattern groups + arunpshankar reference.
- New tasks T130–T148 added at the bottom to capture the restructure work.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [SYNC/ASYNC] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[SYNC]**: Requires human review (complex logic, security-critical, ambiguous requirements)
- **[ASYNC]**: Can be delegated to async agents (well-defined CRUD, repetitive tasks, clear specs)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

All paths relative to `presentation/` directory:
- Slide content: `pages/*.md`, `slides.md`
- Components: `components/*.vue`
- Styles: `styles/*.css`
- Examples: `public/examples/*.py`, `public/examples/*.js`
- Assets: `public/images/`, `public/diagrams/`
- Config: `slidev.config.ts`, `vite.config.ts`, `package.json`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and Slidev framework setup

- [x] T001 [ASYNC] Initialize Node.js project with package.json in presentation/
- [x] T002 [ASYNC] Install Slidev dependencies (slidev, vue, vite) via npm/pnpm
- [x] T003 [P] [ASYNC] Install additional dependencies (UnoCSS, Shiki, Mermaid) in package.json
- [x] T004 [P] [ASYNC] Create basic Slidev configuration in slidev.config.ts
- [x] T005 [P] [ASYNC] Create Vite build configuration in vite.config.ts (integrated in slidev.config.ts)
- [x] T006 [ASYNC] Create directory structure (pages/, components/, styles/, public/, setup/)
- [x] T007 [ASYNC] Create main slides.md entry point with frontmatter configuration
- [x] T008 [P] [ASYNC] Setup Shiki syntax highlighting config in setup/shiki.ts

**Checkpoint**: ✅ COMPLETE - Slidev project initialized and ready for content creation

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core theme, layouts, and components that ALL sections depend on

**⚠️ CRITICAL**: No content sections can begin until this phase is complete

- [x] T009 [SYNC] Design black and orange color theme in styles/theme.css
- [x] T010 [P] [ASYNC] Implement custom code highlighting theme in styles/code-highlighting.css
- [x] T011 [P] [ASYNC] Create custom slide layouts in styles/layouts.css
- [x] T012 [P] [SYNC] Create CodeExample.vue component for syntax-highlighted code with copy button
- [x] T013 [P] [SYNC] Create PatternComparison.vue component for side-by-side pattern comparison
- [x] T014 [P] [SYNC] Create ArchitectureDiagram.vue component for interactive architecture diagrams
- [x] T015 [ASYNC] Configure UnoCSS/TailwindCSS theme colors (black: #0a0a0a, orange: #ff6b00)
- [x] T016 [ASYNC] Setup presenter mode configuration in slidev.config.ts
- [x] T017 [ASYNC] Create template slide pages structure (01-concepts.md through 06-principles.md)

**Checkpoint**: ✅ COMPLETE - Foundation ready, all sections can now be developed in parallel

---

## Phase 3: User Story 1 - Understanding Agentic Concepts (Priority: P1) 🎯 MVP

**Goal**: Attendees can define agentic workflows and explain key differences from traditional development (SC-001)

**Independent Test**: Quiz assessment validates 90% of attendees can correctly define agentic workflows

### Section 1: What Are Agentic Workflows (8 min, 5-7 slides)

- [ ] T018 [SYNC] [US1] Write cover slide content in pages/01-concepts.md (title, subtitle, presenter info)
- [ ] T019 [SYNC] [US1] Write "What are Agentic Workflows" definition slide in pages/01-concepts.md
- [ ] T020 [SYNC] [US1] Write "Mental Model Shift" comparison slide (AI as autocomplete → AI as dev partner)
- [ ] T021 [SYNC] [US1] Write "Key Characteristics" slide covering multi-step workflows with tools
- [ ] T022 [P] [ASYNC] [US1] Create basic workflow diagram in public/diagrams/agentic-workflow.svg
- [ ] T023 [SYNC] [US1] Write presenter notes for all Section 1 slides
- [ ] T024 [P] [ASYNC] [US1] Create simple code example showing agentic workflow in public/examples/basic-agent.js

### Section 2: Why They Matter (7 min, 4-5 slides)

- [ ] T025 [SYNC] [US1] Write "Benefits of Agentic Workflows" slide in pages/01-concepts.md
- [ ] T026 [SYNC] [US1] Write "Industry Adoption Signals" slide (Anthropic usage stats, trust model)
- [ ] T027 [SYNC] [US1] Write "Developer Productivity Gains" slide with metrics
- [ ] T028 [SYNC] [US1] Write "Use Cases" slide covering practical applications
- [ ] T029 [P] [ASYNC] [US1] Create productivity comparison diagram in public/diagrams/productivity-gains.svg
- [ ] T030 [SYNC] [US1] Write presenter notes for all Section 2 slides

**Checkpoint**: US1 complete - attendees understand agentic concepts fundamentals

---

## Phase 4: User Story 2 - Practical Implementation Knowledge (Priority: P1)

**Goal**: Developers can identify key components and integration points, plan how to integrate agentic tools (SC-002)

**Independent Test**: 80% of attendees can identify at least 3 practical use cases for agentic workflows

### Section 3 (OPT-IN, removed from active deck per 2026-04-28): Live Claude Code Demo (15 min, 3-5 slides)

> **Status**: `pages/03-demo.md` exists in the repo but is NOT imported by `slides.md`. These tasks are retained for presenters who want to opt into a live demo extension. Skip unless re-enabling.

- [x] T031 [SYNC] [US2] Write demo introduction slide in pages/03-demo.md
- [x] T032 [SYNC] [US2] Create demo script for CLAUDE.md setup (Segment 1: 3 min) in pages/03-demo.md
- [x] T033 [SYNC] [US2] Create demo script for interactive CLI workflow (Segment 2: 6 min)
- [x] T034 [SYNC] [US2] Create demo script for hooks and MCP demo (Segment 3: 6 min)
- [ ] T035 [P] [ASYNC] [US2] Setup demo project files in public/examples/demo-project/ — opt-in
- [ ] T036 [P] [ASYNC] [US2] Test all demo code examples for execution validity — opt-in
- [ ] T037 [P] [ASYNC] [US2] Record backup demo video in public/demos/claude-code-demo.mp4 — opt-in
- [ ] T038 [P] [ASYNC] [US2] Create demo fallback screenshots in public/screenshots/demo-*.png — opt-in
- [ ] T039 [SYNC] [US2] Write detailed presenter notes with timing and recovery protocol — opt-in

### Section 2 (active deck): Fundamentals - Tools and Memory (≈12 min, 4 slides) **NEW REQUIREMENT**

> **Note**: After the 2026-04-28 restructure this section is now Section 2 of the audience-facing deck (was Section 4 in the prior 9-section plan), placed immediately after Concepts and before Patterns. Section header slide added inline in `slides.md` with hero image `public/images/tools-memory-hero.png`.

- [x] T040 [SYNC] [US2] Write "What are Tools?" slide in pages/02-tools-memory.md (definition, categories, ACI)
- [ ] T041 [P] [ASYNC] [US2] Create tool definition code example in public/examples/tool-definition.py
- [x] T042 [SYNC] [US2] Write "What is Memory?" slide in pages/02-tools-memory.md (types, operations, architecture)
- [x] T043 [P] [ASYNC] [US2] Create memory architecture diagram in public/diagrams/memory-types.svg
- [ ] T044 [P] [ASYNC] [US2] Implement vector store example code in public/examples/vector-store-setup.py
- [x] T045 [SYNC] [US2] Write "Tools + Memory in Action: RAG Example" slide with architecture walkthrough
- [ ] T046 [ASYNC] [US2] Create RAG architecture diagram in public/diagrams/rag-architecture.svg
- [ ] T047 [P] [ASYNC] [US2] Implement complete RAG support agent example in public/examples/rag-support-agent.py
- [ ] T048 [P] [ASYNC] [US2] Implement tool definitions for RAG example in public/examples/rag-tools.py
- [ ] T049 [P] [ASYNC] [US2] Implement memory retrieval functions in public/examples/rag-memory.py
- [ ] T050 [P] [ASYNC] [US2] Create test harness for all code examples in public/examples/test_examples.py
- [ ] T051 [ASYNC] [US2] Test all code examples execute successfully (validates SC-005, static validation)
- [x] T052 [SYNC] [US2] Write "Why This Matters" transition slide explaining value of tools+memory
- [ ] T053 [SYNC] [US2] Write presenter notes for all Section 2 slides with timing

**Checkpoint**: US2 complete - developers understand practical implementation with working examples

---

## Phase 5 (OPT-IN, deferred per 2026-04-28): Single vs Multi-Agent (Before Patterns)

> **Status**: Authored in `pages/04-patterns.md` but that file is NOT imported by `slides.md`. The active deck transitions directly from Tools & Memory into the Core Patterns section header. Tasks retained for opt-in re-enablement.

**Purpose**: Explain limitations of single-agent systems and benefits of multi-agent architectures

**Goal**: Establish foundation for understanding why complex patterns and multi-agent systems are needed

- [x] T054 [SYNC] Write "Why Multi-Agent?" slide in pages/04-patterns.md (before pattern content) — opt-in
- [x] T055 [SYNC] Write "Single Agent Limitations" section covering:
  - Context window constraints
  - Specialization vs generalization tradeoff
  - Sequential processing bottlenecks
  - Error propagation in long chains
  - Difficulty handling complex multi-domain tasks
- [x] T056 [SYNC] Write "Multi-Agent Benefits" section covering:
  - Parallel processing capabilities
  - Domain specialization (each agent expert in one area)
  - Fault isolation (failure in one agent doesn't break entire system)
  - Scalability through horizontal agent addition
  - Compositional flexibility
- [ ] T057 [P] [ASYNC] Create comparison diagram in public/diagrams/single-vs-multi-agent.svg — opt-in
- [ ] T058 [P] [ASYNC] Create example showing single agent struggling with complex task in public/examples/single-agent-limitation.py — opt-in
- [ ] T059 [P] [ASYNC] Create example showing multi-agent handling same task successfully in public/examples/multi-agent-solution.py — opt-in
- [ ] T060 [SYNC] Write presenter notes explaining transition from fundamentals to patterns — opt-in

**Checkpoint**: Clear foundation for why patterns and architectures are needed

---

## Phase 6: User Story 3 - Advanced Workflow Patterns (Priority: P2)

**Goal**: Experienced developers can select appropriate patterns for different situations (SC-003)

**Independent Test**: Pattern recognition exercises and optimization scenarios validate understanding

### Section 5 (OPT-IN, in `pages/04-patterns.md`, NOT in active deck): Foundational Workflow Patterns

> **Status (2026-04-28)**: The pattern slides authored in `pages/04-patterns.md` are NOT imported by `slides.md`. The active deck presents patterns inline in `slides.md`, organized into 4 thematic groups (see new tasks T130–T148 below). Tasks here remain marked done where authored, but their output is not part of the active deck.

- [x] T061 [SYNC] [US3] Write "7 Foundational Patterns Overview" intro slide in pages/04-patterns.md
- [x] T062 [SYNC] [US3] Write Prompt Chaining pattern slide (definition, use cases, example)
- [ ] T063 [P] [ASYNC] [US3] Create prompt chaining code example in public/examples/prompt-chaining.py
- [x] T064 [SYNC] [US3] Write Routing pattern slide (coordinator-delegate architecture)
- [ ] T065 [P] [ASYNC] [US3] Create routing example in public/examples/routing-pattern.py
- [x] T066 [SYNC] [US3] Write Parallelization pattern slide (fan-out/aggregate)
- [ ] T067 [P] [ASYNC] [US3] Create parallelization example in public/examples/parallel-pattern.py
- [x] T068 [SYNC] [US3] Write Reflection pattern slide (actor-critic framework)
- [ ] T069 [P] [ASYNC] [US3] Create reflection example in public/examples/reflection-pattern.py
- [x] T070 [SYNC] [US3] Write Tool Use pattern slide (function calling, ACI)
- [x] T071 [SYNC] [US3] Write Planning pattern slide (orchestrator-workers)
- [ ] T072 [P] [ASYNC] [US3] Create planning example in public/examples/planning-pattern.py
- [x] T073 [SYNC] [US3] Write Multi-Agent pattern slide (collaborative agents)
- [ ] T074 [P] [ASYNC] [US3] Create multi-agent example in public/examples/multi-agent-pattern.py
- [x] T075 [SYNC] [US3] Write presenter notes for all pattern slides

### Section 6: Modern Architecture Patterns (10 min, 6-8 slides)

- [ ] T076 [SYNC] [US3] Write "8 Modern Architectures" intro slide in pages/05-architectures.md
- [ ] T077 [SYNC] [US3] Write "Single Agent + Tools (ReAct)" slide with performance metrics
- [ ] T078 [SYNC] [US3] Write "Sequential Agents" slide (15-25% higher completion rate)
- [ ] T079 [SYNC] [US3] Write "Single Agent + MCP + Tools" slide (37% faster, 93% completion)
- [ ] T080 [SYNC] [US3] Write "Hierarchy + Parallel + Shared Tools" slide (30-60% time reduction)
- [ ] T081 [SYNC] [US3] Write "Single Agent + Router" slide (85-95% routing accuracy)
- [ ] T082 [SYNC] [US3] Write "Human in the Loop" slide (50-80% error reduction)
- [ ] T083 [SYNC] [US3] Write "Dynamic Agent Delegation" slide (hub-spoke model)
- [ ] T084 [SYNC] [US3] Write "Hierarchy + Loop + Parallel + RAG" slide (most sophisticated)
- [ ] T085 [P] [ASYNC] [US3] Create architecture comparison diagrams in public/diagrams/architectures/
- [ ] T086 [SYNC] [US3] Write "Framework Comparison" slide (LangChain, LangGraph, AutoGen, CrewAI)
- [ ] T087 [SYNC] [US3] Write "Architecture Selection Guide" slide (5 decision criteria)
- [ ] T088 [SYNC] [US3] Write presenter notes for all architecture slides

### Section 7: Anthropic Building Effective Agents (5 min, 3-4 slides)

- [ ] T089 [SYNC] [US3] Write "Anthropic's Agent Principles" intro slide in pages/06-principles.md
- [ ] T090 [SYNC] [US3] Write "Simplicity Over Complexity" slide (measured improvements)
- [ ] T091 [SYNC] [US3] Write "Transparent Planning" slide (reasoning display, ACI best practices)
- [ ] T092 [SYNC] [US3] Write "When to Build Agents" slide (decision criteria, workflow comparisons)
- [ ] T093 [P] [ASYNC] [US3] Create decision tree diagram in public/diagrams/agent-decision-tree.svg
- [ ] T094 [SYNC] [US3] Write presenter notes for all principles slides

**Checkpoint**: US3 complete - advanced patterns and selection guidance delivered

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final sections, assessment, and presentation quality

### Section 8: Practical Tips (5 min, 5-6 slides)

- [ ] T095 [SYNC] Write "Getting Started" slide in pages/06-principles.md
- [ ] T096 [SYNC] Write "Common Challenges & Solutions" slide (paired challenge→tip format)
- [ ] T097 [SYNC] Write "Best Practices" slide (CLAUDE.md, hooks, spec-driven workflows)
- [ ] T098 [SYNC] Write "Team Coordination" slide (shared standards, alignment)
- [ ] T099 [SYNC] Write presenter notes for practical tips section

### Section 9: Q&A (7 min, 1-2 slides)

- [ ] T100 [SYNC] Write Q&A slide with resources and next steps
- [ ] T101 [SYNC] Write "Resources" slide (links, documentation, learning materials)
- [ ] T102 [P] [ASYNC] Compile additional learning materials in public/resources/

### Assessment & Validation

- [ ] T103 [SYNC] Create quiz questions for SC-001 validation (90% threshold: define agentic workflows)
- [ ] T104 [SYNC] Create quiz questions for SC-002 validation (80% threshold: identify 3+ use cases)
- [ ] T105 [SYNC] Create assessment for SC-003 validation (75% threshold: confidence implementing)
- [ ] T106 [P] [ASYNC] Create audience engagement tracking mechanism (SC-004: 85% attention score)
- [ ] T107 [ASYNC] Validate all code examples execute successfully (SC-005)

### Final Polish

- [ ] T108 [SYNC] Review all slides for pedagogical flow and narrative coherence
- [ ] T109 [SYNC] Verify time allocations match section durations (total 55-60 min)
- [ ] T110 [P] [ASYNC] Optimize all assets (compress images <200KB, videos <60s)
- [ ] T111 [P] [ASYNC] Add alt text to all images and diagrams for accessibility
- [ ] T112 [ASYNC] Test presentation build and preview in Slidev
- [ ] T113 [ASYNC] Test presenter mode with speaker notes and slide previews
- [ ] T114 [ASYNC] Validate all slide transitions and click-through animations
- [ ] T115 [SYNC] Conduct full rehearsal #1 (3 days before): identify issues
- [ ] T116 [SYNC] Conduct full rehearsal #2 (1 day before): validate fixes
- [ ] T117 [SYNC] Conduct abbreviated rehearsal #3 (1 hour before): final verification
- [ ] T118 [P] [ASYNC] Export backup recordings for all demo segments
- [ ] T119 [P] [ASYNC] Create high-contrast terminal theme configuration for demos
- [ ] T120 [ASYNC] Final build and deployment test

**Checkpoint**: Presentation ready for delivery

---

## Task Dependencies

### Critical Path (Blocking Tasks)
```
T001-T008 (Setup) → T009-T017 (Foundation) → Content Sections can proceed in parallel
```

### Section Dependencies
```
Section 1-2 (US1: Concepts) → Independent, can be first MVP
Section 3 (US2: Demo) → Depends on foundation (T009-T017)
Section 4 (US2: Tools/Memory) → Independent from demo, can run parallel
Section 4.5 (Multi-Agent Why) → NEW, depends on Section 4 complete
Section 5-7 (US3: Patterns) → Should follow Section 4.5 for logical flow
Section 8-9 (Polish) → Can run parallel with US3
```

### User Story Completion Order
```
Phase 1 (Setup) → Phase 2 (Foundation) → Phase 3 (US1) ✓
                                       → Phase 4 (US2) ✓
                                       → Phase 5 (Multi-Agent) ✓
                                       → Phase 6 (US3) ✓
                                       → Phase 7 (Polish) ✓
```

---

## Parallel Execution Opportunities

### Within Phase 2 (Foundation)
```
T009 (theme design) — blocking for visual consistency
T010-T011 (additional styles) [P] — parallel after T009
T012-T014 (Vue components) [P] — parallel with styles
T015-T017 (config) [P] — parallel with components
```

### Within Phase 3 (US1 - Section 1)
```
T018-T021 (slide content) — sequential (narrative flow)
T022 (diagram) [P] — parallel with slide content
T024 (code example) [P] — parallel with slide content
T023 (presenter notes) — after slide content complete
```

### Within Phase 4 (US2 - Section 4: Tools/Memory)
```
T040, T042, T045, T052 (slide content) — sequential (narrative flow)
T041, T044, T047-T049 (code examples) [P] — parallel with slide content
T043, T046 (diagrams) [P] — parallel with slide content
T050-T051 (testing) — after all code examples complete
```

### Within Phase 5 (Multi-Agent Slide)
```
T054-T056 (slide content) — sequential
T057-T059 (diagrams & examples) [P] — parallel with content
```

### Within Phase 6 (US3 - Patterns & Architectures)
```
Pattern slides (T062, T064, T066, T068, T070, T071, T073) — sequential (narrative)
Pattern code examples (T063, T065, T067, T069, T071, T072, T074) [P] — parallel
Architecture slides (T077-T084, T086-T087) — sequential
Architecture diagrams (T085, T093) [P] — parallel
```

---

## Implementation Strategy

### MVP Scope (Minimum Viable Presentation)
**Deliver US1 first for early feedback**:
- Phase 1: Setup ✓
- Phase 2: Foundation ✓
- Phase 3: US1 (Sections 1-2) ✓ **← FIRST DELIVERY**
- Test with pilot audience, gather feedback
- Iterate on US1 before proceeding

### Incremental Delivery
1. **Week 1**: Setup + Foundation + US1 (Concepts) — validate pedagogical approach
2. **Week 2**: US2 (Demo + Tools/Memory) — validate technical examples
3. **Week 3**: Multi-Agent slide + US3 (Patterns) — validate advanced content
4. **Week 4**: Polish + Rehearsals — validate delivery readiness

### Execution Mode Distribution
- **[SYNC] tasks**: 67 (56%) — content writing, pedagogical design, presenter notes
- **[ASYNC] tasks**: 53 (44%) — code examples, diagrams, configuration, testing

**Rationale**: Educational content requires human expertise for narrative coherence and learning outcomes; technical implementation can be delegated to async agents with clear specifications.

---

## Validation Checklist

Before marking presentation complete, verify:

### Content Quality
- [ ] All 9 sections have complete slide content
- [ ] All slides follow pedagogical best practices (≤50 words, ≤6 elements)
- [ ] Presenter notes written for every section
- [ ] Time allocations sum to 55-60 minutes total

### Technical Quality
- [ ] All code examples execute successfully (SC-005)
- [ ] All diagrams created and optimized (<200KB)
- [ ] All assets have alt text for accessibility
- [ ] Slidev builds without errors
- [ ] Presenter mode works correctly

### Educational Quality
- [ ] Each section has clear learning objectives
- [ ] Assessment mechanisms in place (SC-001 through SC-005)
- [ ] User stories map to presentation sections
- [ ] Independent test criteria validated for each story

### Demo Readiness
- [ ] All 3 demo segments rehearsed and validated
- [ ] Backup recordings created for all segments
- [ ] Demo recovery protocol documented
- [ ] Terminal theme configured for readability

### Constitution Compliance
- [ ] Content-First Development: All specs complete before implementation ✓
- [ ] Speckit-Slidev Integration: Single source of truth maintained ✓
- [ ] Developer-Focused Pedagogy: Executable examples, practical methodology ✓
- [ ] Specification-Driven Slides: Learning objectives and assessments defined ✓
- [ ] Modular Content Architecture: Each section delivers standalone value ✓

---

## Risk Mitigation Tasks (from Spec Risk Register)

### Risk: Technical demonstration failures (Severity: Medium)
- [ ] T121 [ASYNC] Test all code examples in clean environment (isolated from presenter's setup)
- [ ] T122 [ASYNC] Create containerized demo environment for consistent execution
- [ ] T123 [SYNC] Develop demo failure recovery checklist (30-second rule, recording fallback)

### Risk: Audience overwhelm with complex concepts (Severity: Low)
- [ ] T124 [SYNC] Conduct pilot presentation with target audience (developers aware but not practicing)
- [ ] T125 [SYNC] Gather feedback on content progression and complexity
- [ ] T126 [SYNC] Adjust narrative flow based on pilot feedback

### Risk: Slidev framework limitations (Severity: Low)
- [ ] T127 [ASYNC] Create prototype slides testing all interactive features (click-through, Monaco editor, Mermaid diagrams)
- [ ] T128 [ASYNC] Test presenter mode functionality (notes, preview, timer)
- [ ] T129 [ASYNC] Validate export formats (PDF, static site) maintain quality

---

## Phase 8 (NEW 2026-04-28): Slide Restructure Reconciliation

**Purpose**: Capture the work performed on the active deck (`presentation/slides.md`) during the "fix slides" iterations and reconcile with the new modular structure.

**Goal**: All restructure work is tracked, the active deck matches the spec, and orphaned modules are clearly marked as opt-in.

### Hero & Branding Visuals (FR-015)

- [x] T130 [SYNC] Add title-slide hero image `public/images/agentic-hero.png` and reference it in `slides.md` cover slide
- [x] T131 [SYNC] Add Tools & Memory section-header hero image `public/images/tools-memory-hero.png` and reference it in `slides.md`
- [x] T132 [P] [ASYNC] Create per-pattern SVG diagrams in `public/diagrams/` (reflection, tool-use, planning, sequential, parallel, multi-agent, hierarchical, routing, human-loop, feedback, web-access, memory-types, llm-vs-agent, plan-execute-flow, hero-agentic)

### Pattern Slides Inline (FR-008 reorganized)

> All pattern slides moved from `pages/04-patterns.md` (orphaned) to inline sections in `slides.md`, grouped into 4 thematic categories + arunpshankar reference.

- [x] T133 [SYNC] Add "Core Patterns" section-header slide in `slides.md`
- [x] T134 [SYNC] Author inline Reflection Pattern slide in `slides.md` (how it works, use cases, benefits)
- [x] T135 [SYNC] Author inline Tool Use Pattern slide in `slides.md`
- [x] T136 [SYNC] Author inline Planning Pattern slide in `slides.md`
- [x] T137 [SYNC] Add "Workflow Patterns" section-header slide in `slides.md`
- [x] T138 [SYNC] Author inline Sequential Workflow Pattern (Prompt Chaining) slide in `slides.md`
- [x] T139 [SYNC] Author inline Parallel Workflow Pattern (Parallelization) slide in `slides.md`
- [x] T140 [SYNC] Add "Coordination Patterns" section-header slide in `slides.md`
- [x] T141 [SYNC] Author inline Multi-Agent Collaboration Pattern slide in `slides.md`
- [x] T142 [SYNC] Author inline Hierarchical Workflow Pattern slide in `slides.md`
- [x] T143 [SYNC] Author inline Routing Pattern (Handoff) slide in `slides.md`
- [x] T144 [SYNC] Add "Control Patterns" section-header slide in `slides.md`
- [x] T145 [SYNC] Author inline Human-in-the-Loop Pattern slide in `slides.md`
- [x] T146 [SYNC] Author inline Feedback Loop Pattern slide in `slides.md`
- [x] T147 [SYNC] Add "arunpshankar Reference Patterns" section-header slide in `slides.md` and author Web Access Pattern slide
- [ ] T148 [SYNC] (Optional) Add additional arunpshankar reference patterns (Dynamic Sharding, Dynamic Decomposition, DAG Orchestration) — currently documented in research.md only

### Closing References (FR-016)

- [x] T149 [SYNC] Author "References & Further Reading" closing slide in `slides.md` with Phil Schmid, arunpshankar, 2025 Architecture Guide, and tool/framework links

### Reconciliation Bookkeeping

- [x] T150 [SYNC] Update `spec.md` with FR-014/FR-015/FR-016 and Clarifications session 2026-04-28
- [x] T151 [SYNC] Update `plan.md` with Phase 2 reconciliation summary, restructured Modular Content Architecture, and updated source tree
- [x] T152 [SYNC] Update `data-model.md` Sections table to reflect 6-section audience-facing deck and orphaned modules
- [x] T153 [SYNC] Update `tasks.md` to mark Section 3 (demo) and Section 5 (`pages/04-patterns.md`) tasks as opt-in, and add this Phase 8
- [x] T154 [SYNC] Update `research.md` with R15 documenting the slide restructure rationale
- [x] T155 [SYNC] Update `quickstart.md` timing reference and section listing

**Checkpoint**: Specs, plan, data model, tasks, research, and quickstart all match the active deck

---

## Summary

**Total Tasks**: 155 (after 2026-04-28 restructure additions)
- Setup: 8 tasks
- Foundation: 9 tasks
- US1 (Concepts + Benefits): 13 tasks
- US2 (Demo opt-in + Tools/Memory): 23 tasks
- Multi-Agent Slide (opt-in): 7 tasks
- US3 (Foundational Patterns opt-in + Architectures + Principles): 34 tasks
- Polish (Sections 8-9): 26 tasks
- Risk Mitigation: 9 tasks
- **Slide Restructure Reconciliation (NEW 2026-04-28)**: 26 tasks (T130–T155)

**Active Deck Sections** (post 2026-04-28 restructure):
1. Concepts — `pages/01-concepts.md`
2. Tools & Memory — `pages/02-tools-memory.md`
3. Workflow Patterns (4 thematic groups + arunpshankar reference) — inline in `slides.md`
4. Modern Architectures — `pages/05-architectures.md`
5. Principles & Practical Tips — `pages/06-principles.md`
6. Q&A + References — `pages/06-principles.md` + inline closing slides

**Orphaned Modules** (retained, not imported): `pages/03-demo.md`, `pages/04-patterns.md`

**Critical Requirements Status**:
1. ✅ Section 2: Tools and Memory with RAG example (T040-T053)
2. ◯ Multi-Agent limitations slide (T054-T060) — opt-in, not in active deck
3. ✅ Slide restructure reconciliation (T130-T155 NEW)
4. ✅ Hero/branding visuals (T130-T132)
5. ✅ Closing References slide (T149)
