# Live Claude Code Demo

---
layout: section
---

# Live Demo
## Claude Code in Action

---

# Demo: CLAUDE.md Setup

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

## What is CLAUDE.md?

<v-clicks>

A **project guidelines file** that shapes how Claude Code behaves in your repository — encoding your team's standards, conventions, and commands so the agent never has to guess.

**Placement**: Root of your project (`./CLAUDE.md`)

**Key Rule**: Keep it **under 200 lines** — focused, not exhaustive

</v-clicks>

</div>

<div v-click>

## Sample Structure

```markdown
# Project: My API Service

## Tech Stack
- Node.js 20, TypeScript, Postgres
- Jest for testing, ESLint + Prettier

## Commands
- `npm test` — run test suite
- `npm run lint` — lint and format
- `npm run build` — compile TypeScript

## Conventions
- Use async/await, not .then() chains
- All functions must have JSDoc comments
- Tests live next to source: foo.test.ts

## Do NOT
- Commit directly to main
- Use `any` types in TypeScript
- Skip error handling in async functions
```

</div>

</div>

<div class="mt-4 p-3 bg-orange-900 bg-opacity-30 rounded" v-click>

**What you'll see**: CLAUDE.md created → Claude reads it → agent behavior changes immediately (follows conventions, uses correct test commands)

</div>

---

# Demo: Interactive CLI Workflow

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

## Starting Claude Code

<v-clicks>

```bash
# Install once
npm install -g @anthropic-ai/claude-code

# Start in your project
cd my-project
claude
```

**The Loop**: Claude reads → edits → runs → observes → iterates — all in one session

</v-clicks>

<div v-click class="mt-4 p-3 bg-gray-800 rounded">

**Prompt Example**:

> *"Add input validation to all POST endpoints. Run tests after each endpoint and fix any failures before moving to the next."*

</div>

</div>

<div v-click>

## What Happens

```
> Reading routes/users.ts...
> Reading routes/posts.ts...
> Planning: 3 endpoints identified

[users.ts] Adding Zod validation schema
[users.ts] Running tests... ✓ 12 passed

[posts.ts] Adding validation schema
[posts.ts] Running tests... ✗ 2 failed
[posts.ts] Fixing: title field required
[posts.ts] Running tests... ✓ 14 passed

[comments.ts] Adding validation schema
[comments.ts] Running tests... ✓ 8 passed

Done. 3 endpoints validated, all tests passing.
```

<div class="mt-4 p-3 bg-green-900 bg-opacity-30 rounded">

**Key**: Agent sees test output and self-corrects without human intervention

</div>

</div>

</div>

---

# Demo: Hooks and MCP

<div class="grid grid-cols-2 gap-6 mt-2">

<div>

## Hooks: Lifecycle Commands

<v-clicks>

User-defined commands that run at **agent lifecycle events** — quality gates you never have to ask the agent to run.

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "npm run lint -- $FILE"
      }]
    }],
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "echo 'Running command: $CMD'"
      }]
    }]
  }
}
```

**Result**: Every file edit auto-linted — no manual quality checks needed

</v-clicks>

</div>

<div>

<v-clicks>

## MCP: Universal Tool Adapter

**Model Context Protocol** — a standard interface connecting Claude to any external service without custom integration code.

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    },
    "sentry": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sentry"]
    }
  }
}
```

**What Claude can now do**:
- Read GitHub PRs and issues directly
- Fetch Sentry errors and stack traces
- Query databases, Slack, Jira, and more

</v-clicks>

<div v-click class="mt-4 p-3 bg-orange-900 bg-opacity-30 rounded">

**Together**: Hooks enforce your standards automatically; MCP brings your entire toolchain into the agent's reach

</div>

</div>

</div>
