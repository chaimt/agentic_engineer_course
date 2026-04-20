# Agentic Engineer Course

A hands-on course on building and understanding AI agentic workflows. The repository contains a full-featured Slidev presentation and companion workshop materials.

## Repository Structure

```
agentic_engineer_course/
├── presentation/   # Slidev slide deck on agentic workflow patterns
└── workshop/       # Hands-on exercises and workshop materials
```

## What's Inside

### `presentation/`

An interactive slide deck built with [Slidev](https://sli.dev/) covering:

- **Foundational Concepts** — the shift from LLMs to agentic systems
- **18 Agentic Workflow Patterns** — 10 core patterns + 8 modern agent architectures
- **Implementation Frameworks** — LangChain, LangGraph, AutoGen, and CrewAI comparison
- **Memory Systems** — simple memory and advanced MemGPT two-tier memory
- **Advanced Techniques** — pattern composition, optimization, and real-world case studies
- **Best Practices** — getting started and avoiding common pitfalls

**Target Audience**: Developers familiar with AI tools (Copilot, ChatGPT) who want to move into structured agentic workflows.  
**Duration**: 60–75 minutes

See [`presentation/README.md`](presentation/README.md) for setup and usage instructions.

### `workshop/`

Companion workshop materials with practical exercises that reinforce the concepts covered in the presentation.

## Quick Start

### Presentation

```bash
cd presentation
npm install
npm run dev
# Open http://localhost:3030
```

Or with [go-task](https://taskfile.dev/):

```bash
cd presentation
task setup
task dev
```

## Technologies

- [Slidev](https://sli.dev/) — presentation framework built on Vue 3 + Vite
- [Vue 3](https://vuejs.org/) — component model for interactive slides
- [Shiki](https://shiki.matsu.io/) — syntax highlighting
- [UnoCSS](https://unocss.dev/) — utility-first CSS

## License

Educational use — check with the repository owner for distribution rights.
