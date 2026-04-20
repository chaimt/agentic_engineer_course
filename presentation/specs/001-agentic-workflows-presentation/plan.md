# Implementation Plan: Agentic Workflows Presentation

**Branch**: `001-agentic-workflows-presentation` | **Date**: 2026-04-16 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-agentic-workflows-presentation/spec.md`

**Note**: This template is filled in by the `/spec.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Create an educational presentation on agentic workflows using Slidev framework with Speckit content management. The presentation teaches developers how to implement AI-assisted development workflows, featuring live Claude Code demonstrations and practical implementation examples. Content follows a concept-first arc from fundamentals through advanced patterns, covering 15 core patterns: Phil Schmid's 7 foundational workflow patterns (Prompt Chaining, Routing, Parallelization, Reflection, Tool Use, Planning, Multi-Agent) and 8 modern agent architectures from the 2025 guide. Delivered in 45-60 minutes to developers familiar with AI tools but not yet practicing structured agentic workflows, using black and orange color theme for maximum contrast.

## Technical Context

**Language/Version**: JavaScript/TypeScript with Node.js (NEEDS CLARIFICATION: specific Node version)  
**Primary Dependencies**: Slidev (NEEDS CLARIFICATION: version and theme customization approach), Vue 3, Vite, Markdown processors  
**Storage**: N/A (static presentation content in markdown, assets in filesystem)  
**Testing**: Manual presentation rehearsal, code examples validation (NEEDS CLARIFICATION: testing framework for embedded code snippets)  
**Target Platform**: Modern web browsers (Chrome, Firefox, Safari) for presentation delivery and export to PDF  
**Project Type**: Interactive developer presentation with live coding demonstrations  
**Performance Goals**: Smooth slide transitions (<100ms), fast initial load (<3s), responsive navigation  
**Constraints**: 45-60 minute delivery time, must match referenced Google Slides visual theme, presenter-driven demos only  
**Scale/Scope**: ~50-80 slides covering 6 main sections (concepts, benefits, demo, patterns, tips, Q&A), 3-5 code examples with live demos

**Clarifications Needed (Phase 0 Research)**:
1. How to customize Slidev theme to match Google Slides color scheme and layout
2. Best practices for embedding executable code examples in Slidev
3. Recommended approach for managing presentation assets (screenshots, diagrams, demo recordings)
4. Integration strategy between Speckit content specifications and Slidev markdown structure
5. Setup and rehearsal workflow for live Claude Code demonstrations

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Pre-Design Evaluation (before Phase 0)

| Principle | Status | Evidence |
|-----------|--------|----------|
| **I. Content-First Development** | ✅ PASS | Feature spec defines learning objectives, audience, and success criteria before technical implementation |
| **II. Speckit-Slidev Integration** | ✅ PASS | Project uses Speckit for content management (.specify/ structure) and targets Slidev for delivery |
| **III. Developer-Focused Pedagogy** | ⚠️ PENDING | Requires executable code examples and live demos - will validate in Phase 1 design |
| **IV. Specification-Driven Slides** | ⚠️ PENDING | Requires structured documentation for each slide - will create in Phase 1 (data-model.md, contracts/) |
| **V. Modular Content Architecture** | ✅ PASS | Feature spec defines 6 independent modules: concepts, benefits, demo, patterns, tips, Q&A |

### Workflow Gates

| Phase | Status | Notes |
|-------|--------|-------|
| 1. Content Specification | ✅ COMPLETE | spec.md defines learning objectives, target audience, key concepts |
| 2. Technical Planning | 🔄 IN PROGRESS | This plan.md - completing Technical Context |
| 3. Slide Design | ⏸️ BLOCKED | Awaits Phase 0 research and Phase 1 data-model |
| 4. Content Integration | ⏸️ BLOCKED | Awaits slide design completion |
| 5. Review Phase | ⏸️ BLOCKED | Awaits content integration |
| 6. Delivery Preparation | ⏸️ BLOCKED | Awaits review completion |

### Gate Violations

None identified. The feature spec aligns with all constitutional principles. Two principles (III, IV) require validation during Phase 1 design to ensure technical implementation meets educational standards.

### Post-Design Re-Evaluation

*Will be completed after Phase 1 (data-model.md, contracts/, quickstart.md generation)*

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
presentation/                    # Repository root
├── slides/                      # Slidev presentation content
│   ├── slides.md               # Main presentation file (Slidev markdown)
│   ├── sections/               # Modular slide sections
│   │   ├── 01-concepts.md      # What are agentic workflows
│   │   ├── 02-benefits.md      # Why they matter
│   │   ├── 03-demo.md          # Live Claude Code demonstration
│   │   ├── 04-patterns.md      # Workflow patterns
│   │   ├── 05-tips.md          # Practical tips
│   │   └── 06-qa.md            # Q&A section
│   ├── theme/                  # Custom Slidev theme
│   │   ├── styles/             # CSS matching Google Slides theme
│   │   └── layouts/            # Custom slide layouts
│   └── components/             # Vue components for interactive elements
│
├── examples/                    # Code examples and demos
│   ├── basic-workflow/         # Simple agentic workflow example
│   ├── advanced-patterns/      # Advanced workflow patterns
│   └── claude-code-demo/       # Live demo scripts and setup
│
├── assets/                      # Presentation assets
│   ├── images/                 # Screenshots, diagrams
│   ├── videos/                 # Demo recordings (backup)
│   └── references/             # Additional learning materials
│
├── .specify/                    # Speckit framework (content specs)
│   ├── memory/
│   │   └── constitution.md     # Presentation principles
│   └── scripts/
│
└── specs/                       # Feature specifications
    └── 001-agentic-workflows-presentation/
        ├── spec.md             # Feature specification
        ├── plan.md             # This file
        ├── research.md         # Phase 0 output
        ├── data-model.md       # Phase 1: Content structure
        ├── quickstart.md       # Phase 1: Presenter guide
        └── contracts/          # Phase 1: Slide content contracts
```

**Structure Decision**: Slidev presentation with modular content architecture. The `slides/` directory contains all presentation content organized by section for maintainability. Code examples are separated into `examples/` for testing and reuse. Speckit specifications in `specs/` drive content creation, ensuring alignment with constitution principles. Custom theme in `slides/theme/` matches referenced Google Slides visual style.

## Triage Framework: [SYNC] vs [ASYNC] Classification

**Execution Strategy**: This presentation project uses a hybrid model combining human creativity and pedagogical expertise ([SYNC]) with automated setup and scaffolding ([ASYNC]).

### Preliminary Task Classification

Complete during planning phase - will be validated and refined during task generation

| Task Category | Estimated [SYNC] Tasks | Estimated [ASYNC] Tasks | Rationale |
|---------------|----------------------|----------------------|-----------|
| Content Narrative | 6 | 0 | Learning objectives and story flow require pedagogical expertise |
| Slide Design | 4 | 3 | Visual layouts can be automated, but educational flow needs human review |
| Code Examples | 3 | 2 | Example selection requires context, but scaffolding can be automated |
| Theme Customization | 2 | 1 | Design decisions are human-driven, but CSS implementation can be delegated |
| Infrastructure Setup | 0 | 4 | Slidev configuration and project setup are fully automatable |

### Triage Decision Criteria Applied

**High-Risk [SYNC] Classifications:**

- Learning objective definition for each module (educational effectiveness)
- Content narrative and story flow (pedagogical coherence)
- Live demo script creation (presentation success critical)
- Educational assessment design (learning validation)
- Audience engagement strategy (presentation effectiveness)
- Visual theme design decisions (brand and accessibility compliance)

**Agent-Delegated [ASYNC] Classifications:**

- Slidev project initialization and configuration
- File structure and asset organization
- Slide template scaffolding
- Code example file structure setup
- Documentation generation (quickstart, presenter notes)
- Research on Slidev theming best practices

### Triage Audit Trail

| Task | Classification | Primary Criteria | Risk Level | Rationale |
|------|----------------|------------------|------------|-----------|
| Define learning objectives | [SYNC] | Educational effectiveness | High | Requires pedagogical expertise and domain knowledge |
| Design content narrative | [SYNC] | Pedagogical coherence | High | Story flow impacts learning outcomes |
| Create live demo scripts | [SYNC] | Presentation success | High | Demo failures reduce credibility and engagement |
| Initialize Slidev project | [ASYNC] | Technical setup | Low | Standard configuration, well-documented process |
| Setup file structure | [ASYNC] | Organization | Low | Follows established patterns from project structure |
| Research Slidev theming | [ASYNC] | Knowledge gathering | Low | Information retrieval and synthesis |
| Create slide templates | [ASYNC] | Scaffolding | Low | Based on defined content structure |
| Design visual theme | [SYNC] | Design decisions | Medium | Must match brand and ensure accessibility |

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations identified. Feature aligns with all constitutional principles:
- Content-First Development satisfied by spec.md
- Speckit-Slidev Integration achieved through project structure
- Developer-Focused Pedagogy enforced through executable examples and live demos
- Specification-Driven Slides ensured by Phase 1 contracts generation
- Modular Content Architecture implemented via 6 independent sections

No complexity justification required.
