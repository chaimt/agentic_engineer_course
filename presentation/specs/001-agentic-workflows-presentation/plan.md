# Implementation Plan: Agentic Workflows Presentation

**Branch**: `001-agentic-workflows-presentation` | **Date**: 2026-04-24 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-agentic-workflows-presentation/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Create a comprehensive educational presentation on agentic workflows using Slidev framework. The presentation will teach developers how to implement AI-assisted development workflows, covering foundational patterns from Phil Schmid's taxonomy (7 patterns: Prompt Chaining, Routing, Parallelization, Reflection, Tool Use, Planning, Multi-Agent), modern architecture patterns from 2025 guide (8 patterns with performance metrics), and Anthropic's Building Effective Agents principles. Primary tool demonstration will be Claude Code CLI with live presenter-driven demos. Black and orange color theme for professional technical appearance.

**NEW REQUIREMENT**: Before describing agent architectures, add comprehensive slide section covering Tools and Memory concepts with practical RAG system example demonstrating both.

## Technical Context

**Language/Version**: JavaScript/TypeScript with Node.js (Slidev requirement)
**Primary Dependencies**: Slidev (Vue 3 + Vite), TailwindCSS or custom CSS for black/orange theming, Shiki for syntax highlighting, Mermaid for diagrams
**Storage**: Markdown files (slides.md), static assets (images, code examples), theme configuration
**Testing**: Manual presentation testing, code example validation (ensuring all demos execute successfully), content accuracy review
**Target Platform**: Modern web browsers (Chrome, Firefox, Safari), presentation mode with speaker notes
**Project Type**: Interactive web-based presentation application
**Performance Goals**: Instant slide transitions (<100ms), smooth animations (60fps), fast initial load (<2s)
**Constraints**: 45-60 minute delivery window, readable text for audiences 10-100 people, all code examples must be executable and tested, presenter-driven demos only
**Scale/Scope**: ~60-80 slides covering 7 foundational patterns + 8 architecture patterns + tools/memory section + Anthropic principles + live demos + assessment

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Content-First Development ✅ PASS
- Feature spec defines complete learning objectives, slide narratives, and success criteria
- Educational outcomes are measurable (SC-001 through SC-005)
- No implementation started without approved content specification

### Speckit-Slidev Integration ✅ PASS
- Content managed through Speckit framework (.specify/ directory structure)
- Presentation delivery via Slidev framework (NFR-007 requirement)
- Specification-driven slide generation planned

### Developer-Focused Pedagogy (NON-NEGOTIABLE) ✅ PASS
- Target audience: developers aware of AI tools but not practicing structured workflows (NFR-005)
- All code examples required to be executable and tested (NFR-003)
- Presenter-driven live demos with Claude Code (FR-003)
- Hands-on methodology with practical implementations (FR-002, FR-004)

### Specification-Driven Slides ✅ PASS
- Learning objectives defined per user story (Priority P1, P2)
- Code examples and demos specified (FR-003, FR-008, FR-009)
- Assessment criteria included (FR-006, SC-001 through SC-005)
- Technical examples derived from approved research sources

### Modular Content Architecture ✅ PASS
- Content organized into independent educational modules:
  1. Agentic concepts introduction
  2. Live Claude Code demo
  3. Foundational workflow patterns (7 patterns)
  4. **NEW: Tools and Memory fundamentals with RAG example**
  5. Modern architecture patterns (8 patterns)
  6. Anthropic Building Effective Agents principles
  7. Practical implementation and Q&A
- Each module delivers standalone value
- Clear dependencies documented in presentation flow

**GATE STATUS**: ✅ ALL GATES PASS - Proceed to Phase 0 research

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/spec.plan command output)
├── research.md          # Phase 0 output (/spec.plan command)
├── data-model.md        # Phase 1 output (/spec.plan command)
├── quickstart.md        # Phase 1 output (/spec.plan command)
├── contracts/           # Phase 1 output (/spec.plan command)
└── tasks.md             # Phase 2 output (/spec.tasks command - NOT created by /spec.plan)
```

### Source Code (repository root)

```text
presentation/
├── slides.md                 # Main Slidev presentation file (markdown-based slides)
├── pages/                    # Additional slide pages (if splitting content)
│   ├── 01-concepts.md       # Agentic concepts introduction
│   ├── 02-tools-memory.md   # NEW: Tools and Memory fundamentals + RAG example
│   ├── 03-demo.md           # Live Claude Code demo
│   ├── 04-patterns.md       # Foundational workflow patterns
│   ├── 05-architectures.md  # Modern architecture patterns
│   └── 06-principles.md     # Anthropic Building Effective Agents
├── components/               # Custom Vue components for interactive elements
│   ├── CodeExample.vue      # Syntax-highlighted code with copy button
│   ├── PatternComparison.vue # Side-by-side pattern comparison
│   └── ArchitectureDiagram.vue # Interactive architecture diagrams
├── public/                   # Static assets
│   ├── images/              # Diagrams, screenshots, logos
│   ├── examples/            # Code example files for demos
│   └── fonts/               # Custom fonts if needed
├── styles/                   # Custom CSS/SCSS
│   ├── theme.css           # Black and orange color theme
│   ├── code-highlighting.css # Custom syntax theme
│   └── layouts.css         # Custom slide layouts
├── setup/                    # Slidev setup scripts
│   └── shiki.ts            # Code highlighting configuration
├── slidev.config.ts         # Slidev configuration
├── package.json             # Node dependencies
└── vite.config.ts          # Vite build configuration
```

**Structure Decision**: Slidev presentation with modular page organization. Main slides.md serves as entry point with imports from pages/ directory for each major section. Custom Vue components enable interactive elements (code examples, diagrams, comparisons). Black and orange theme implemented via custom CSS. All code examples stored as executable files in public/examples/ for validation and live demo use.

## Triage Framework: [SYNC] vs [ASYNC] Classification

**Execution Strategy**: This feature uses primarily [SYNC] (human-authored) approach due to the nature of educational content creation requiring pedagogical expertise and narrative coherence.

### Preliminary Task Classification

| Task Category | Estimated [SYNC] Tasks | Estimated [ASYNC] Tasks | Rationale |
|---------------|----------------------|----------------------|-----------|
| Content Writing | 10 | 0 | Educational content requires pedagogical expertise, narrative flow, and learning outcome alignment |
| Slide Design | 8 | 2 | Custom layouts and theming require design decisions; standard slides can be templated |
| Code Examples | 0 | 6 | Executable code examples (tools, memory, RAG) can be generated and validated automatically |
| Technical Setup | 0 | 4 | Slidev configuration, build setup, dependency management are automatable |
| Testing/Validation | 2 | 4 | Content review requires human judgment; code execution testing can be automated |

### Triage Decision Criteria Applied

**High-Risk [SYNC] Classifications:**

- All section narrative content (learning objectives, concept explanations, transitions)
- Tools and Memory conceptual explanations
- RAG example architecture design and walkthrough narrative
- Live demo script and presenter notes
- Assessment questions and success criteria alignment
- Slide layout decisions affecting pedagogical flow

**Agent-Delegated [ASYNC] Classifications:**

- Code example implementations (tools definition, RAG retrieval, vector store setup)
- Slidev configuration and theme setup
- Test harness for code examples
- Asset optimization (image compression, syntax highlighting config)
- Build and deployment scripts
- Documentation generation (API docs from code)

### Triage Audit Trail

| Task | Classification | Primary Criteria | Risk Level | Rationale |
|------|----------------|------------------|------------|-----------|
| Tools slide narrative | [SYNC] | Educational quality | High | Requires pedagogical framing for developer audience |
| Memory slide narrative | [SYNC] | Educational quality | High | Complex concepts need expert explanation |
| RAG example code | [ASYNC] | Technical implementation | Low | Standard Python patterns with clear spec |
| RAG architecture diagram | [SYNC] | Pedagogical design | Medium | Visual communication requires design judgment |
| Code validation tests | [ASYNC] | Automation-friendly | Low | Standard pytest patterns |
| Slidev theme config | [ASYNC] | Configuration | Low | Black/orange theme specs are clear |
| Slide transitions | [SYNC] | User experience | Medium | Affects presentation pacing and flow |

## Complexity Tracking

> **No violations detected** - Constitution Check passed all gates

## Phase 0 Completion Summary

✅ **Research Phase Complete** (2026-04-24)

**Deliverables**:
- research.md updated with R14: Tools and Memory Fundamentals
- Tools definition and categorization (Agent-Computer Interface)
- Memory types and architecture patterns (short-term, long-term, semantic, episodic)
- RAG example specification (API Support Agent with tools + memory)
- Slide structure planned (4 slides: Tools, Memory, RAG Example, Why This Matters)
- Presentation flow integration confirmed (inserted as Section 4, after demo, before patterns)
- Time budget validated (18 minutes for tools/memory, 42 minutes remaining, within 60-minute constraint)

## Phase 1 Completion Summary

✅ **Design & Contracts Phase Complete** (2026-04-24)

**Deliverables**:
- data-model.md updated with new Section 4 (Tools and Memory)
- Presentation flow restructured (9 sections total, previously 6)
- Duration allocations updated (60-minute total confirmed)
- contracts/ directory reviewed (existing contracts apply to new section)
- quickstart.md reviewed (setup process unchanged)
- Agent context updated (CLAUDE.md refreshed with current technologies)

## Constitution Re-Check (Post Phase 1)

*GATE: Re-evaluate after design phase*

### Content-First Development ✅ PASS (CONFIRMED)
- Tools and Memory section fully specified in research.md before implementation
- Learning objectives defined: Understand tools (5 min), memory (5 min), practical integration (8 min)
- RAG example architecture designed with clear pedagogical goals
- Implementation will follow approved specification

### Speckit-Slidev Integration ✅ PASS (CONFIRMED)
- New section managed through Speckit framework (research.md, data-model.md)
- Slidev delivery planned with standard section structure
- Specification-driven: Code examples specified before implementation
- Single source of truth maintained

### Developer-Focused Pedagogy (NON-NEGOTIABLE) ✅ PASS (CONFIRMED)
- RAG example chosen for high developer relevance (API troubleshooting)
- Code examples designed to be executable and tested
- Concrete implementations shown (tool definitions, vector store setup, hybrid memory)
- Hands-on methodology: Working code + architecture diagrams + walkthrough

### Specification-Driven Slides ✅ PASS (CONFIRMED)
- 4-slide structure documented with clear content per slide
- Learning objectives: Define tools, define memory, demonstrate integration, explain value
- Code examples specified in research.md with implementation details
- Assessment implicit: Audience should understand tools/memory as building blocks after this section

### Modular Content Architecture ✅ PASS (CONFIRMED)
- Section 4 is self-contained: Can present tools/memory independently if needed
- Clear dependencies: Follows demo (provides context), precedes patterns (provides building blocks)
- Standalone educational value: Understanding tools and memory is foundational for any agentic system
- No coupling: Other sections don't require modification for this addition

**GATE STATUS**: ✅ ALL GATES PASS (RECONFIRMED) - Constitution compliance maintained after design phase

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

N/A - No violations detected
