# Agentic Workflows Presentation

An educational presentation on agentic workflows using the Slidev framework.

## Overview

This presentation teaches developers how to implement AI-assisted development workflows, featuring:
- **Foundational Concepts**: Understanding the shift from LLMs to agentic systems
- **18 Agentic Workflow Patterns**: 10 core patterns + 8 modern agent architectures from the 2025 guide
- **Implementation Frameworks**: LangChain, LangGraph, AutoGen, and CrewAI comparison
- **Memory Systems**: Simple memory and advanced MemGPT two-tier memory
- **Advanced Techniques**: Pattern composition, optimization, and real-world case studies
- **Best Practices**: Getting started and avoiding common pitfalls

**Target Audience**: Developers familiar with AI tools (Copilot, ChatGPT) but new to structured agentic workflows

**Duration**: 60-75 minutes

## Quick Start

### Prerequisites

- Node.js 18+ LTS
- npm or pnpm
- Modern web browser
- [go-task](https://taskfile.dev/) (optional but recommended)

### Installation

#### Using Task (Recommended)

```bash
# Install go-task if not already installed
# macOS: brew install go-task
# Linux/Windows: See https://taskfile.dev/installation/

# Set up project environment
task setup

# Start development server
task dev

# Open presenter mode
# Navigate to http://localhost:3030/presenter
```

#### Using npm directly

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Open presenter mode
# Navigate to http://localhost:3030/presenter
```

### Build and Export

#### Using Task

```bash
# Build static site
task build

# Export to PDF
task export

# Preview built presentation
task preview

# Validate presentation structure
task validate

# Clean build artifacts
task clean
```

#### Using npm directly

```bash
# Build static site
npm run build

# Export to PDF (requires additional setup)
npm run export
```

## Project Structure

```
presentation/
├── slides.md              # Main presentation file
├── layouts/               # Custom Vue slide layouts
│   ├── default.vue       # Standard content layout
│   ├── intro.vue         # Title/intro slides
│   ├── section-header.vue # Section dividers
│   └── pattern-slide.vue # Pattern showcase layout
├── components/            # Reusable Vue components
├── styles/                # Theme and styling
│   ├── theme.css         # Custom theme colors/fonts
│   └── code-highlighting.css # Syntax highlighting
├── examples/              # Executable code examples
│   ├── reflection/       # Reflection pattern examples
│   ├── tool-use/         # Tool use pattern examples
│   ├── planning/         # Planning pattern examples
│   ├── sequential/       # Sequential workflow examples
│   ├── parallel/         # Parallel workflow examples
│   ├── multi-agent/      # Multi-agent collaboration examples
│   ├── hierarchical/     # Hierarchical workflow examples
│   ├── routing/          # Routing pattern examples
│   ├── human-loop/       # Human-in-the-loop examples
│   ├── feedback/         # Feedback loop examples
│   ├── architectures/    # Modern agent architecture examples (2025)
│   └── advanced/         # Advanced pattern combinations
├── public/                # Static assets
│   ├── screenshots/      # Demo screenshots
│   ├── diagrams/         # Architecture diagrams
│   └── demos/            # Video demonstrations
├── resources/             # Additional learning materials
└── specs/                 # Feature specifications
    └── 001-agentic-workflows-presentation/
        ├── spec.md        # Feature specification
        ├── plan.md        # Implementation plan
        ├── tasks.md       # Task breakdown
        ├── research.md    # Technical research
        └── contracts/     # API contracts
```

## Features

### Custom Layouts

- **Default**: Standard content layout with heading and body
- **Intro**: Centered layout for title and opening slides
- **Section Header**: Full-screen section dividers
- **Pattern Slide**: Two-column layout for pattern showcase (description + code)

### Theme

- Black and orange color scheme for professional technical appearance
- High-contrast design with maximum readability
- Material Theme Palenight syntax highlighting
- Accessible color contrast (WCAG AAA)
- Custom fonts: Roboto (sans), Roboto Slab (serif), Fira Code (mono)

### Code Examples

All examples in `examples/` are executable and tested:

**Core Patterns:**
- Reflection pattern
- Tool use pattern
- Planning pattern

**Workflow Patterns:**
- Sequential workflow
- Parallel workflow

**Coordination Patterns:**
- Multi-agent collaboration
- Hierarchical workflows
- Routing pattern

**Control Patterns:**
- Human-in-the-loop
- Feedback loops

**Modern Agent Architectures (2025):**
- Single Agent + Tools (ReAct)
- Sequential Agents
- Single Agent + MCP Servers + Tools
- Agents Hierarchy + Parallel + Shared Tools
- Single Agent + Tools + Router
- Single Agent + Human in Loop + Tools
- Single Agent + Dynamically Call Other Agents
- Agents Hierarchy + Loop + Parallel + Shared RAG

**Advanced:**
- Advanced pattern combinations and hybrid approaches

## Development

### Available Task Commands

The project includes a Taskfile.yml for build automation. See all available tasks:

```bash
task --list
```

**Common tasks:**
- `task setup` - Install all dependencies
- `task dev` - Start development server with hot reload
- `task build` - Build presentation for production
- `task export` - Export presentation to PDF
- `task preview` - Preview built presentation
- `task validate` - Validate presentation structure
- `task lint` - Lint markdown and code files
- `task format` - Format code with Prettier
- `task test:examples` - Test all code examples
- `task clean` - Clean build artifacts
- `task clean:all` - Clean everything including node_modules
- `task ci` - Run all CI checks (validate, lint, build)

### Running the Presentation

#### Using Task

```bash
task dev
```

#### Using npm

```bash
npm run dev
```

The presentation will open automatically at `http://localhost:3030`.

**Presenter Mode**: Navigate to `http://localhost:3030/presenter` for notes and preview.

### Editing Content

Main content is in `slides.md`. Use Slidev markdown syntax:

```markdown
---
layout: default
---

# Slide Title

Content here

<!--
Presenter notes (visible only in presenter mode)
-->
```

### Adding Code Examples

1. Create example file in `examples/[pattern-name]/`
2. Reference in slides:

```markdown
```js
<<< @/examples/reflection/agent.js
```
```

### Adding Assets

Place assets in `public/`:
- Screenshots: `public/screenshots/`
- Diagrams: `public/diagrams/`
- Videos: `public/demos/`

Reference in slides:

```markdown
![Description](/screenshots/demo.png)
```

## Keyboard Shortcuts

### Navigation
- `→` or `Space`: Next slide
- `←`: Previous slide
- `Home`: First slide
- `End`: Last slide

### Features
- `O`: Slide overview
- `D`: Toggle dark mode
- `G`: Go to slide (type number)
- `F`: Fullscreen
- `P`: Toggle presenter mode

## Presenter Notes

For detailed presentation guidance, see:
- `specs/001-agentic-workflows-presentation/quickstart.md` - Complete presenter guide
- `specs/001-agentic-workflows-presentation/research.md` - Content research
- `.specify/theme-notes.md` - Theme customization details

## Technologies

- **Slidev**: Presentation framework
- **Vue 3**: Component framework
- **Vite**: Build tool
- **Shiki**: Syntax highlighting
- **UnoCSS**: Utility-first CSS

## Documentation

- [Slidev Documentation](https://sli.dev/)
- [Vue 3 Documentation](https://vuejs.org/)
- [Shiki Syntax Highlighting](https://shiki.matsu.io/)

## Contributing

This presentation follows the Speckit specification-driven approach:
1. Specifications are in `specs/001-agentic-workflows-presentation/`
2. Content is generated from specifications
3. Implementation follows the task breakdown in `tasks.md`

## License

Educational use - check with repository owner for distribution rights.

## Status

**Implementation Progress**: Phase 4 Partially Complete (Core Patterns Done)

✅ Phase 1: Setup (Complete)
✅ Phase 2: Foundational Infrastructure (Complete)
✅ Phase 3: User Story 1 - Understanding Agentic Concepts (Complete)
🔄 Phase 4: User Story 2 - Practical Implementation Knowledge (In Progress)
  - ✅ Setup and Overview
  - ✅ Core Patterns (Reflection, Tool Use, Planning)
  - ⏳ Workflow Patterns (Sequential, Parallel)
  - ⏳ Coordination Patterns (Multi-Agent, Hierarchical, Routing)
  - ⏳ Control Patterns (Human-in-Loop, Feedback)
  - ⏳ Modern Agent Architectures (8 patterns)
  - ⏳ Implementation Frameworks & Memory Systems
  - ⏳ Pattern Selection & Resources
⏳ Phase 5: User Story 3 - Advanced Workflow Patterns (Pending)
⏳ Phase 6: Polish & Cross-Cutting Concerns (Pending)

See `specs/001-agentic-workflows-presentation/tasks.md` for detailed task list.

## Contact

For questions or feedback about this presentation, refer to the specification documentation in `specs/`.
