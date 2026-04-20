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

## Research Complete

All technical clarifications from plan.md resolved:
- ✅ Slidev theme customization approach
- ✅ Code example implementation patterns
- ✅ Asset management strategy
- ✅ Speckit-Slidev integration workflow
- ✅ Live demo rehearsal and backup procedures

**Next Phase**: Phase 1 - Design & Contracts (data-model.md, contracts/, quickstart.md)
