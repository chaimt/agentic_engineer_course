# Implementation Plan: Agentic Workflows Presentation

**Branch**: `001-agentic-workflows-presentation` | **Date**: 2026-04-24 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-agentic-workflows-presentation/spec.md`

**Note**: This template is filled in by the `/speckit-plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Create a comprehensive educational presentation on agentic workflows using Slidev framework. The presentation teaches developers how to implement AI-assisted development workflows, covering foundational patterns from Phil Schmid's taxonomy (7 patterns: Prompt Chaining, Routing, Parallelization, Reflection, Tool Use, Planning, Multi-Agent) — organized in `pages/04-patterns.md` into 4 thematic categories preceded by a "Why Multi-Agent?" intro — modern architecture patterns from the 2025 guide (8 patterns with performance metrics), and Anthropic's "Building Effective Agents" principles. Claude Code is the canonical reference tool, illustrated through static slides (CLAUDE.md, hooks JSON, MCP config). Black and orange color theme for professional technical appearance.

**NEW REQUIREMENT (2026-04-24)**: Comprehensive slide section covering Tools and Memory concepts with practical RAG system example demonstrating both — added as Section 2 of the deck (immediately after Concepts, before Patterns).

**SLIDE RESTRUCTURE (2026-04-28)**: After several "fix slides" iterations, the active deck (`presentation/slides.md`) was reorganized as follows. This plan now reflects that final structure:

- **Live Claude Code Demo section removed** from the active deck. The orphaned `pages/03-demo.md` is retained in the repo as an opt-in module not imported by `slides.md`.
- **Patterns moved to `pages/04-patterns.md` (imported by `slides.md`)** and grouped into 4 thematic categories (Core / Workflow / Coordination / Control) preceded by a "Why Multi-Agent?" intro section. The `arunpshankar Reference Patterns` group (Web Access) was included initially but has since been removed (see Phase 3 Reconciliation Summary 2026-04-30).
- **Tools & Memory promoted to Section 2** (after Concepts, before Patterns) with its own section-header slide and hero image.
- **Hero/branding visuals added**: `public/images/agentic-hero.png` (title slide) and `public/images/tools-memory-hero.png` (section header), plus per-pattern SVG diagrams in `public/diagrams/`.
- **Closing References slide added** listing the three primary research sources.

## Technical Context

**Language/Version**: JavaScript/TypeScript with Node.js (Slidev requirement)
**Primary Dependencies**: Slidev (Vue 3 + Vite), TailwindCSS or custom CSS for black/orange theming, Shiki for syntax highlighting, Mermaid for diagrams
**Storage**: Markdown files (slides.md), static assets (images, code examples), theme configuration
**Testing**: Manual presentation testing, code example validation (ensuring all demos execute successfully), content accuracy review
**Target Platform**: Modern web browsers (Chrome, Firefox, Safari), presentation mode with speaker notes
**Project Type**: Interactive web-based presentation application
**Performance Goals**: Instant slide transitions (<100ms), smooth animations (60fps), fast initial load (<2s)
**Constraints**: 55-65 minute delivery window, readable text for audiences 10-100 people, all on-slide code examples must be syntactically valid and conceptually accurate, presenter-narrated (no live coding required in the active deck)
**Scale/Scope**: ~35-45 slides covering 7 foundational patterns (in 4 thematic groups, preceded by "Why Multi-Agent?" intro) + 8 architecture patterns + tools/memory section with RAG example + Anthropic principles + practical tips + assessment + closing references

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
- All on-slide code examples required to be syntactically valid and conceptually accurate (NFR-003, SC-005 as updated 2026-04-28)
- Claude Code referenced throughout the deck via static examples (CLAUDE.md, hooks JSON, MCP config, 5-step adoption path) — see FR-002 / FR-003
- Practical methodology grounded in working code patterns (FR-002, FR-004, FR-014)

### Specification-Driven Slides ✅ PASS
- Learning objectives defined per user story (Priority P1, P2)
- On-slide code examples and content specified (FR-008, FR-009, FR-014)
- Assessment criteria included (FR-006, SC-001 through SC-005)
- Technical examples derived from approved research sources

### Modular Content Architecture ✅ PASS
- Content organized into independent educational modules (active deck, post 2026-04-28 restructure):
  1. **Concepts** — `pages/01-concepts.md` (definition, mental model shift, key characteristics, why they matter, industry adoption, productivity gains)
  2. **Tools & Memory Fundamentals** — `pages/02-tools-memory.md` (Tools/ACI, Memory types, RAG support agent example, "Why this matters")
  3. **Workflow Patterns** — `pages/04-patterns.md` (imported by `slides.md`), organized into:
     - Why Multi-Agent? (Single Agent Limitations, Benefits, Pitfalls) — precedes all pattern groups
     - Core Patterns (Reflection, Tool Use, Planning)
     - Workflow Patterns (Sequential / Prompt Chaining, Parallel / Parallelization)
     - Coordination Patterns (Multi-Agent, Hierarchical, Routing)
     - Control Patterns (Human-in-the-Loop, Feedback Loop)
     - ~~arunpshankar Reference Patterns (Web Access)~~ — removed 2026-04-30
  4. **Modern Architecture Patterns** — `pages/05-architectures.md` (8 architectures with performance metrics, framework comparison, selection guide)
  5. **Anthropic Building Effective Agents + Practical Tips** — `pages/06-principles.md` (simplicity, transparent planning, when to build agents, getting started, challenges, best practices, team coordination)
  6. **Q&A and References** — closing slides in `slides.md` (questions, resources, references)
- Orphaned (retained, not imported): `pages/03-demo.md` (live Claude Code demo)
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
├── slides.md                 # Main Slidev presentation entry point
│                             # — Title + overview slides (inline)
│                             # — Imports pages/01-concepts.md
│                             # — Tools & Memory section header (inline) + imports pages/02-tools-memory.md
│                             # — Imports pages/04-patterns.md (Why Multi-Agent + Core / Workflow / Coordination / Control pattern groups)
│                             # — Imports pages/05-architectures.md and pages/06-principles.md
│                             # — Closing References slide (inline)
├── pages/                    # Modular slide pages
│   ├── 01-concepts.md       # IMPORTED — Agentic concepts (definition, mental model, benefits, adoption, productivity)
│   ├── 02-tools-memory.md   # IMPORTED — Tools and Memory fundamentals + RAG example + Why This Matters
│   ├── 03-demo.md           # ORPHANED (retained, not imported) — Live Claude Code demo, opt-in module
│   ├── 04-patterns.md       # IMPORTED — Why Multi-Agent? intro + Core / Workflow / Coordination / Control patterns (arunpshankar section removed 2026-04-30)
│   ├── 05-architectures.md  # IMPORTED — 8 modern architecture patterns + framework comparison + selection guide
│   └── 06-principles.md     # IMPORTED — Anthropic principles + Practical tips + Team coordination + Q&A
├── components/               # Custom Vue components for interactive elements
│   ├── CodeExample.vue      # Syntax-highlighted code with copy button
│   ├── PatternComparison.vue # Side-by-side pattern comparison
│   └── ArchitectureDiagram.vue # Interactive architecture diagrams
├── public/                   # Static assets
│   ├── images/              # Hero images: agentic-hero.png (title), tools-memory-hero.png (Tools & Memory section)
│   ├── diagrams/            # Per-pattern SVGs (reflection-pattern.svg, tool-use-pattern.svg, planning-pattern.svg,
│   │                        # sequential-pattern.svg, parallel-pattern.svg, multi-agent-pattern.svg,
│   │                        # hierarchical-pattern.svg, routing-pattern.svg, human-loop-pattern.svg,
│   │                        # feedback-pattern.svg, web-access-pattern.svg, memory-types.svg,
│   │                        # llm-vs-agent.svg, plan-execute-flow.svg, hero-agentic.svg)
│   └── examples/            # (Optional) executable companion code for static slide examples
├── styles/                   # Custom CSS/SCSS
│   ├── theme.css           # Black and orange color theme
│   ├── code-highlighting.css # Custom syntax theme
│   └── layouts.css         # Custom slide layouts (e.g. section-header, dense-col)
├── setup/                    # Slidev setup scripts
│   └── shiki.ts            # Code highlighting configuration
├── slidev.config.ts         # Slidev configuration
├── package.json             # Node dependencies
└── vite.config.ts          # Vite build configuration
```

**Structure Decision**: Slidev presentation with hybrid organization — `slides.md` serves as the entry point and contains the title, overview, Tools & Memory section header, and the closing references slide. All pattern slides (Why Multi-Agent intro + 4 thematic groups) live in `pages/04-patterns.md` and are imported via `src:` frontmatter. Larger content modules (Concepts, Tools & Memory, Modern Architectures, Principles & Tips) also live in `pages/` and are imported similarly. The orphaned `pages/03-demo.md` is retained in the repo as an opt-in module for presenters who want to extend the deck with a live demo. Custom Vue components enable interactive elements (code examples, diagrams, comparisons). Black and orange theme implemented via custom CSS. On-slide code examples are statically validated; any companion executable code lives in `public/examples/`.

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

## Phase 2 Reconciliation Summary (2026-04-28)

✅ **Slide Restructure Reconciled with Specifications**

After multiple "fix slides" iterations on the active branch, the deck (`presentation/slides.md`) diverged from the original 9-section plan. This phase reconciles the spec, plan, data model, tasks, research, and quickstart with the deck's actual structure.

**Reconciliation Outcomes**:
- Active deck has 6 audience-facing sections (Concepts, Tools & Memory, Patterns, Modern Architectures, Principles & Tips, Q&A) — down from 9 — and total runtime ≈55–65 minutes.
- Patterns are presented via `pages/04-patterns.md` (imported by `slides.md`) and grouped into 4 thematic categories (Core, Workflow, Coordination, Control) preceded by a "Why Multi-Agent?" intro. An arunpshankar Reference Patterns group (Web Access) was initially included and later removed.
- Live Claude Code Demo section removed from imports; `pages/03-demo.md` retained as opt-in module.
- Tools & Memory promoted to Section 2 with hero image (`tools-memory-hero.png`).
- Hero/branding visuals added: `agentic-hero.png`, `tools-memory-hero.png`, plus per-pattern SVG diagrams in `public/diagrams/`.
- Closing References slide added.
- New requirements captured: FR-014 (Tools & Memory section), FR-015 (hero/branding visuals), FR-016 (closing references slide).
- SC-005 reframed: code accuracy validated statically (no live demo to validate against).

## Phase 3 Reconciliation Summary (2026-04-30)

✅ **Patterns Page Refactored**

Changes on the `update-patterns-slides` branch to `pages/04-patterns.md`:

**Reconciliation Outcomes**:
- `pages/04-patterns.md` is confirmed as **ACTIVE** — imported by `slides.md` via `src: ./pages/04-patterns.md`. The prior spec description of this file as "orphaned" is corrected here.
- **arunpshankar Reference Patterns section removed**: The entire "arunpshankar Reference Patterns" group (Web Access / Search→Scrape→Summarize) was removed from `pages/04-patterns.md`. The pattern documentation remains in `research.md` for future opt-in use.
- **"Why Multi-Agent?" section repositioned**: Moved from after the Control Patterns section to before the Workflow Patterns section, providing a more natural instructional flow (Core Patterns → motivation for multi-agent → Workflow → Coordination → Control).
- `web-access-pattern.svg` in `public/diagrams/` is no longer referenced in the active deck.

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
