---

description: "Task list for Agentic Workflows Presentation feature implementation - Pedagogically Ordered"
---

# Tasks: Agentic Workflows Presentation

**Input**: Design documents from `/specs/001-agentic-workflows-presentation/`
**Prerequisites**: plan.md (tech stack, project structure), spec.md (user stories with priorities), context.md (research sources)
**Context**: Presentation explaining the difference between LLMs and agents, with detailed coverage of agentic workflow patterns

**Research Sources**: ByteByteGo, Anthropic, Dev.to, Philipp Schmid, GitHub repositories, Weaviate
**Patterns Coverage**: Each major agentic workflow pattern gets a dedicated slide with code examples
**Theme Reference**: https://docs.google.com/presentation/d/1KEfu6VjQZBZscsg7GodkjttD9GPi3pRvP65boUg7IMY/edit?slide=id.g36c849d51ab_0_1530 - Slidev theme MUST match the visual style of this presentation

**Tests**: Tests are NOT explicitly requested in the specification - test tasks are excluded per requirements.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.
**Pedagogical Order**: Slides are sequenced for optimal learning progression: concepts → setup → basic patterns → complex patterns → advanced topics → practice

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Repository root for Slidev project structure
- `slides.md` at root for main presentation
- `public/` for static assets
- `components/` for custom Vue components
- `layouts/` for custom slide layouts
- `examples/` for executable code examples organized by pattern

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic Slidev structure

- [ ] T001 Create project structure per implementation plan at repository root
- [ ] T002 Initialize Node.js project with package.json including Slidev, Vue.js 3, Vite dependencies
- [ ] T003 [P] Create slidev.config.ts with presentation configuration
- [ ] T004 [P] Create public/ directory structure for images/, diagrams/, and patterns/
- [ ] T005 [P] Create components/ directory for custom Vue components
- [ ] T006 [P] Create layouts/ directory for custom slide layouts
- [ ] T007 [P] Create styles/ directory with theme.css (matching reference presentation colors/fonts) and code-highlighting.css
- [ ] T008 [P] Create examples/ directory with subdirectories for each pattern (reflection/, tool-use/, planning/, multi-agent/, sequential/, parallel/, hierarchical/, routing/, human-loop/, feedback/)
- [ ] T009 [P] Create resources/ directory for additional learning materials

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

**Theme Reference**: https://docs.google.com/presentation/d/1KEfu6VjQZBZscsg7GodkjttD9GPi3pRvP65boUg7IMY/edit?slide=id.g36c849d51ab_0_1530

- [ ] T010 Review reference Google Slides presentation and document theme elements (colors, fonts, layouts, spacing) in .specify/theme-notes.md
- [ ] T011 Create main slides.md file with basic Slidev frontmatter and structure
- [ ] T012 [P] Implement base slide layout in layouts/default.vue matching reference presentation style
- [ ] T013 [P] Configure Slidev theme in slidev.config.ts to match reference presentation (colors, fonts, transitions)
- [ ] T014 [P] Create styles/theme.css with color scheme and typography matching reference presentation
- [ ] T015 [P] Setup Prism.js syntax highlighting configuration in styles/code-highlighting.css with theme-matching colors
- [ ] T016 [P] Create intro slide layout in layouts/intro.vue matching reference presentation intro style
- [ ] T017 [P] Create section header layout in layouts/section-header.vue matching reference presentation section headers
- [ ] T018 [P] Create pattern showcase layout in layouts/pattern-slide.vue for consistent pattern presentation
- [ ] T019 [P] Setup presentation navigation and structure in slides.md

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Understanding Agentic Concepts (Priority: P1) 🎯 MVP

**Goal**: Deliver foundational knowledge explaining what agentic workflows are and how they differ from LLMs and traditional development

**Independent Test**: Attendee can define agentic workflows, explain differences from LLMs, and identify key benefits after viewing this section

**Slide Order**: Title → LLM Definition → Agent Definition → Comparison → Workflows → Benefits → Use Cases

### Implementation for User Story 1

- [ ] T020 [P] [US1] Create title slide content in slides.md explaining presentation goals using reference theme style
- [ ] T021 [P] [US1] Create "What is an LLM?" slide section in slides.md with definition and characteristics
- [ ] T022 [P] [US1] Create "What is an Agent?" slide section in slides.md with definition and characteristics
- [ ] T023 [US1] Create "LLM vs Agent" comparison slide in slides.md highlighting key differences
- [ ] T024 [US1] Create "Agentic Workflows Defined" slide section in slides.md with core concepts
- [ ] T025 [P] [US1] Add diagram comparing LLM request-response vs agent autonomous behavior in public/diagrams/llm-vs-agent.svg
- [ ] T026 [P] [US1] Create "Benefits of Agentic Workflows" slide in slides.md
- [ ] T027 [P] [US1] Create "Use Cases" slide section in slides.md identifying practical applications
- [ ] T028 [US1] Create interactive comparison component in components/LlmAgentComparison.vue
- [ ] T029 [US1] Integrate LlmAgentComparison component into slides.md for concept demonstration

**Checkpoint**: At this point, User Story 1 should be fully functional - attendees can understand core concepts

---

## Phase 4: User Story 2 - Practical Implementation Knowledge (Priority: P1)

**Goal**: Provide real-world examples with ONE SLIDE PER PATTERN showing implementation details

**Independent Test**: Attendee can identify key components of each pattern, understand setup requirements, and select appropriate patterns

**Slide Order**: Getting Started → Pattern Overview → Core Patterns (3) → Workflow Patterns (2) → Coordination Patterns (3) → Control Patterns (2) → Selection Guide → Comparison Table → Tools

### Setup and Overview

- [ ] T028 [US2] Create "Getting Started" slide section in slides.md with setup overview and prerequisites
- [ ] T029 [US2] Create "Pattern Categories Overview" slide in slides.md introducing the 4 pattern types (Core, Workflow, Coordination, Control)
- [ ] T030 [US2] Create code demo layout in layouts/code-demo.vue for live coding display
- [ ] T031 [US2] Create interactive code example component in components/CodeExample.vue
- [ ] T032 [US2] Create pattern selector component in components/PatternSelector.vue for interactive exploration

### Core Patterns (Fundamental Building Blocks)

**Slide Sequence**: Section Header → Reflection → Tool Use → Planning

- [ ] T033 [P] [US2] Create "Core Patterns" section header slide in slides.md
- [ ] T034 [P] [US2] Create "Reflection Pattern" slide in slides.md explaining self-review and improvement
- [ ] T035 [P] [US2] Create reflection pattern example in examples/reflection/reflection_agent.py
- [ ] T036 [P] [US2] Add reflection pattern diagram in public/diagrams/reflection-pattern.svg
- [ ] T037 [P] [US2] Create "Tool Use Pattern" slide in slides.md explaining external tool integration
- [ ] T038 [P] [US2] Create tool use pattern example in examples/tool-use/tool_agent.py
- [ ] T039 [P] [US2] Add tool use pattern diagram in public/diagrams/tool-use-pattern.svg
- [ ] T040 [P] [US2] Create "Planning Pattern" slide in slides.md explaining task decomposition
- [ ] T041 [P] [US2] Create planning pattern example in examples/planning/planning_agent.py
- [ ] T042 [P] [US2] Add planning pattern diagram in public/diagrams/planning-pattern.svg

### Workflow Patterns (Execution Flow)

**Slide Sequence**: Section Header → Sequential → Parallel

- [ ] T043 [P] [US2] Create "Workflow Patterns" section header slide in slides.md
- [ ] T044 [P] [US2] Create "Sequential Workflow Pattern" slide in slides.md explaining step-by-step execution
- [ ] T045 [P] [US2] Create sequential workflow example in examples/sequential/sequential_workflow.py
- [ ] T046 [P] [US2] Add sequential workflow diagram in public/diagrams/sequential-pattern.svg
- [ ] T047 [P] [US2] Create "Parallel Workflow Pattern" slide in slides.md explaining concurrent execution
- [ ] T048 [P] [US2] Create parallel workflow example in examples/parallel/parallel_workflow.py
- [ ] T049 [P] [US2] Add parallel workflow diagram in public/diagrams/parallel-pattern.svg

### Coordination Patterns (Multi-Agent Systems)

**Slide Sequence**: Section Header → Multi-Agent → Hierarchical → Routing

- [ ] T050 [P] [US2] Create "Coordination Patterns" section header slide in slides.md
- [ ] T051 [P] [US2] Create "Multi-Agent Collaboration" slide in slides.md explaining agent coordination
- [ ] T052 [P] [US2] Create multi-agent example in examples/multi-agent/collaborative_agents.py
- [ ] T053 [P] [US2] Add multi-agent pattern diagram in public/diagrams/multi-agent-pattern.svg
- [ ] T054 [P] [US2] Create "Hierarchical Workflow Pattern" slide in slides.md explaining parent-child relationships
- [ ] T055 [P] [US2] Create hierarchical workflow example in examples/hierarchical/hierarchical_agents.py
- [ ] T056 [P] [US2] Add hierarchical workflow diagram in public/diagrams/hierarchical-pattern.svg
- [ ] T057 [P] [US2] Create "Routing Pattern" slide in slides.md explaining task delegation to specialized agents
- [ ] T058 [P] [US2] Create routing pattern example in examples/routing/routing_agent.py
- [ ] T059 [P] [US2] Add routing pattern diagram in public/diagrams/routing-pattern.svg

### Control Patterns (Oversight and Improvement)

**Slide Sequence**: Section Header → Human-in-Loop → Feedback

- [ ] T060 [P] [US2] Create "Control Patterns" section header slide in slides.md
- [ ] T061 [P] [US2] Create "Human-in-the-Loop Pattern" slide in slides.md explaining human oversight
- [ ] T062 [P] [US2] Create human-in-the-loop example in examples/human-loop/human_oversight_agent.py
- [ ] T063 [P] [US2] Add human-in-the-loop diagram in public/diagrams/human-loop-pattern.svg
- [ ] T064 [P] [US2] Create "Feedback Loop Pattern" slide in slides.md explaining iterative improvement
- [ ] T065 [P] [US2] Create feedback loop example in examples/feedback/feedback_loop_agent.py
- [ ] T066 [P] [US2] Add feedback loop diagram in public/diagrams/feedback-pattern.svg

### Pattern Selection and Resources

**Slide Sequence**: Selection Guide → Comparison Table → Tools and Libraries

- [ ] T067 [US2] Create "Pattern Selection Guide" slide in slides.md with decision criteria for choosing patterns
- [ ] T068 [US2] Create "Pattern Comparison Table" slide in slides.md summarizing all 10 patterns with use cases
- [ ] T069 [US2] Create "Tools and Libraries" slide in slides.md listing LangChain, LlamaIndex, AutoGen, CrewAI, etc.
- [ ] T070 [US2] Integrate CodeExample component into slides.md with pattern examples
- [ ] T071 [US2] Integrate PatternSelector component into slides.md for interactive pattern exploration

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - attendees understand concepts and all 10 patterns

---

## Phase 5: User Story 3 - Advanced Workflow Patterns (Priority: P2)

**Goal**: Teach advanced pattern combinations and optimization techniques for experienced developers

**Independent Test**: Attendee can combine patterns, identify optimization opportunities, and understand trade-offs

**Slide Order**: Section Header → Combining Patterns → Pattern Composition Example → Optimization → Trade-offs → Decision Framework → Case Studies

### Implementation for User Story 3

- [ ] T072 [P] [US3] Create "Advanced Patterns" section header slide in slides.md
- [ ] T073 [P] [US3] Create "Combining Patterns" slide in slides.md showing pattern composition strategies
- [ ] T074 [P] [US3] Create hybrid pattern example combining reflection + tool use in examples/advanced/hybrid_reflection_tools.py
- [ ] T075 [P] [US3] Create advanced multi-agent system in examples/advanced/advanced_multi_agent.py
- [ ] T076 [P] [US3] Create pattern composition diagram in public/diagrams/pattern-composition.svg
- [ ] T077 [US3] Create "Optimization Techniques" slide section in slides.md covering performance and efficiency
- [ ] T078 [P] [US3] Create optimized agent example in examples/advanced/optimized_agent.py
- [ ] T079 [P] [US3] Create "Pattern Trade-offs" slide in slides.md comparing complexity vs capability
- [ ] T080 [US3] Create "Decision Framework: Choosing the Right Pattern" slide in slides.md with flowchart
- [ ] T081 [P] [US3] Create advanced workflow diagram in public/diagrams/advanced-workflows.svg
- [ ] T082 [US3] Create "Real-World Case Studies" slide section in slides.md with production examples
- [ ] T083 [US3] Integrate PatternSelector component into advanced patterns section of slides.md

**Checkpoint**: All user stories should now be independently functional - complete learning journey from concepts through advanced implementation

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final presentation quality

**Slide Order**: Common Challenges → Security → Team Coordination → Debugging → Quiz → Closing

### Resources and Documentation

- [ ] T084 [P] Create resources/references.md with links to all research sources (ByteByteGo, Anthropic, Dev.to, etc.)
- [ ] T085 [P] Create resources/further-reading.md with additional learning materials
- [ ] T086 [P] Create resources/tools-and-libraries.md listing LangChain, LlamaIndex, AutoGen, CrewAI, etc.
- [ ] T087 [P] Create resources/pattern-catalog.md with comprehensive pattern reference guide

### Practical Guidance Slides

- [ ] T088 Create "Common Challenges" slide section in slides.md addressing edge cases and troubleshooting
- [ ] T089 Create "Security Considerations" slide in slides.md for AI-assisted development
- [ ] T090 Create "Team Coordination" slide in slides.md for multi-developer scenarios
- [ ] T091 Create "Debugging Agentic Workflows" slide in slides.md with troubleshooting techniques

### Assessment and Closing

- [ ] T092 [P] Create assessment quiz component in components/QuizComponent.vue
- [ ] T093 Add quiz slides to slides.md for learning validation covering all 10 patterns and concepts
- [ ] T094 Create closing slide with key takeaways, next steps, and resources in slides.md

### Quality Assurance

- [ ] T095 [P] Add speaker notes throughout slides.md for presentation delivery
- [ ] T096 [P] Optimize all diagrams for presentation clarity in public/diagrams/
- [ ] T097 Verify all code examples execute successfully in examples/ for all 10 patterns
- [ ] T098 Test presentation flow and timing (45-60 minute target)
- [ ] T099 Review slide transitions and animations for smooth delivery
- [ ] T100 [P] Add README.md with setup and delivery instructions at repository root

---

## Presentation Slide Flow Summary

**Complete slide sequence in presentation order:**

### Section 1: Introduction and Concepts (US1)
1. Title and Goals
2. What is an LLM?
3. What is an Agent?
4. LLM vs Agent Comparison
5. Agentic Workflows Defined
6. Benefits of Agentic Workflows
7. Use Cases

### Section 2: Getting Started (US2)
8. Getting Started and Prerequisites
9. Pattern Categories Overview (Core, Workflow, Coordination, Control)

### Section 3: Core Patterns (US2)
10. Core Patterns Section Header
11. Reflection Pattern
12. Tool Use Pattern
13. Planning Pattern

### Section 4: Workflow Patterns (US2)
14. Workflow Patterns Section Header
15. Sequential Workflow Pattern
16. Parallel Workflow Pattern

### Section 5: Coordination Patterns (US2)
17. Coordination Patterns Section Header
18. Multi-Agent Collaboration Pattern
19. Hierarchical Workflow Pattern
20. Routing Pattern

### Section 6: Control Patterns (US2)
21. Control Patterns Section Header
22. Human-in-the-Loop Pattern
23. Feedback Loop Pattern

### Section 7: Pattern Selection (US2)
24. Pattern Selection Guide
25. Pattern Comparison Table
26. Tools and Libraries

### Section 8: Advanced Topics (US3)
27. Advanced Patterns Section Header
28. Combining Patterns
29. Optimization Techniques
30. Pattern Trade-offs
31. Decision Framework
32. Real-World Case Studies

### Section 9: Practical Guidance (Polish)
33. Common Challenges
34. Security Considerations
35. Team Coordination
36. Debugging Agentic Workflows

### Section 10: Closing (Polish)
37. Assessment Quiz
38. Key Takeaways and Next Steps

**Total: ~38 slide topics with clear pedagogical progression**

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User Story 1 (P1) - Concepts: Can start after Foundational
  - User Story 2 (P1) - Patterns: Can start after Foundational (independent of US1)
  - User Story 3 (P2) - Advanced: Can start after Foundational (independent of US1/US2)
- **Polish (Phase 6)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Independent of US1, though logically builds on concepts
  - Setup slides (T028-T032) must complete before pattern slides
  - Pattern categories are independent and can be developed in parallel
  - Selection/comparison slides (T067-T071) should come after pattern slides
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Independent of US1/US2, though requires pattern knowledge

### Within Each User Story

- **User Story 2 Pattern Organization**:
  - Setup slides (T028-T032) first
  - Each pattern category can be developed in parallel:
    - Core Patterns (T033-T042): 10 tasks
    - Workflow Patterns (T043-T049): 7 tasks
    - Coordination Patterns (T050-T059): 10 tasks
    - Control Patterns (T060-T066): 7 tasks
  - Selection/Resources (T067-T071) after patterns complete

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T003-T009)
- All Foundational tasks marked [P] can run in parallel within Phase 2 (T011-T017)
- Once Foundational phase completes, all user stories can start in parallel
- **Pattern categories in User Story 2 can be developed in parallel**:
  - Core Patterns team: T034-T042 (9 tasks)
  - Workflow Patterns team: T044-T049 (6 tasks)
  - Coordination Patterns team: T051-T059 (9 tasks)
  - Control Patterns team: T061-T066 (6 tasks)
  - Each category includes: section header + patterns (each with slide + code + diagram)
- Different user stories can be worked on in parallel by different team members
- Polish tasks marked [P] can run in parallel (T084-T087, T092, T096, T100)

---

## Parallel Example: User Story 2 - Pattern Development by Category

```bash
# Team A: Core Patterns
Task: "Create 'Core Patterns' section header"
Task: "Create 'Reflection Pattern' slide"
Task: "Create reflection pattern example in examples/reflection/reflection_agent.py"
Task: "Add reflection diagram in public/diagrams/reflection-pattern.svg"
Task: "Create 'Tool Use Pattern' slide"
Task: "Create tool use pattern example"
Task: "Add tool use diagram"
Task: "Create 'Planning Pattern' slide"
Task: "Create planning pattern example"
Task: "Add planning diagram"

# Team B: Workflow Patterns (parallel to Team A)
Task: "Create 'Workflow Patterns' section header"
Task: "Create 'Sequential Workflow' slide"
Task: "Create sequential workflow example"
...

# Team C: Coordination Patterns (parallel to A and B)
Task: "Create 'Coordination Patterns' section header"
Task: "Create 'Multi-Agent Collaboration' slide"
...

# Team D: Control Patterns (parallel to A, B, and C)
Task: "Create 'Control Patterns' section header"
Task: "Create 'Human-in-the-Loop' slide"
...
```

---

## Implementation Strategy

### MVP First (User Story 1 + Core Patterns)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 - Understanding Agentic Concepts
4. Complete US2 Setup + Core Patterns only (T028-T042)
5. **STOP and VALIDATE**: Test presentation flow for concepts + 3 core patterns
6. Demo if ready - foundational presentation complete

### Incremental Delivery - Pattern Category by Category

1. Complete Setup + Foundational → Presentation framework ready
2. Add User Story 1 → Test independently → Demo concepts section (MVP!)
3. Add User Story 2 incrementally by pattern category:
   - Add Setup + Core Patterns (Reflection, Tool Use, Planning)
   - Add Workflow Patterns (Sequential, Parallel)
   - Add Coordination Patterns (Multi-Agent, Hierarchical, Routing)
   - Add Control Patterns (Human-Loop, Feedback)
   - Add Selection Guide and Resources
4. Add User Story 3 → Test independently → Demo advanced techniques
5. Add Polish → Complete presentation

### Parallel Team Strategy

With multiple developers (organized by pattern category):

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Concepts slides + components)
   - Developer B: US2 Setup + Core Patterns (T028-T042)
   - Developer C: US2 Workflow Patterns (T043-T049)
   - Developer D: US2 Coordination Patterns (T050-T059)
   - Developer E: US2 Control Patterns + Selection (T060-T071)
   - Developer F: User Story 3 (Advanced patterns)
3. Each developer creates: slides + code examples + diagrams for their patterns
4. Stories and patterns integrate sequentially into slides.md for proper flow

---

## Pattern Coverage Summary

**10 Agentic Workflow Patterns - Organized by Category:**

### Core Patterns (Fundamental Building Blocks)
1. **Reflection Pattern** (T034-T036): Self-review and improvement
2. **Tool Use Pattern** (T037-T039): External tool integration
3. **Planning Pattern** (T040-T042): Task decomposition and planning

### Workflow Patterns (Execution Flow)
4. **Sequential Workflow** (T044-T046): Step-by-step execution
5. **Parallel Workflow** (T047-T049): Concurrent execution

### Coordination Patterns (Multi-Agent Systems)
6. **Multi-Agent Collaboration** (T051-T053): Agent coordination
7. **Hierarchical Workflow** (T054-T056): Parent-child relationships
8. **Routing Pattern** (T057-T059): Task delegation to specialists

### Control Patterns (Oversight and Improvement)
9. **Human-in-the-Loop** (T061-T063): Human oversight integration
10. **Feedback Loop Pattern** (T064-T066): Iterative improvement cycles

Each pattern includes:
- Dedicated slide explaining the pattern
- Executable code example
- Visual diagram illustrating the pattern

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Slides are ordered for optimal learning: simple → complex, concepts → practice
- Pattern categories provide clear organization and enable parallel development
- Each user story should be independently completable and testable
- All code examples must be executable and tested (T097)
- All 10 patterns should be validated in assessment quiz (T093)
- Presentation timing target: 45-60 minutes (T098)
- Pattern catalog resource provides quick reference (T087)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Educational effectiveness is the primary success metric
