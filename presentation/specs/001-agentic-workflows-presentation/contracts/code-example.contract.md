# Code Example Contract

**Feature**: 001-agentic-workflows-presentation  
**Version**: 1.0.0  
**Purpose**: Define the contract for embedding and referencing code examples in slides

## Contract Overview

Code examples provide practical demonstrations of agentic workflow concepts. They must be executable, tested, and properly formatted for slide display.

---

## Example Reference Format

### In Section Specifications

```yaml
code_examples:
  - id: "basic-workflow-agent"
    file_path: "basic-workflow/agent.js"
    language: javascript
    line_range: [1, 10]
    highlight_lines: "3,5-7"
    description: "Agent initialization with tool usage"
    is_live_demo: false
```

### In Slide Content (Markdown)

**External File Import**:
```markdown
<<< @/examples/basic-workflow/agent.js{1-10}{3,5-7}
```

**Inline Code Block**:
````markdown
```js{1,3-5|7}
// Progressive highlighting: click reveals
const agent = new Agent();      // Click 1
agent.loadTools();              // Click 1
agent.setContext(projectInfo);  // Click 1
agent.run();                    // Click 2
```
````

**Monaco Editor (Interactive)**:
````markdown
```js{monaco}
// Editable code example
const demo = () => console.log("Editable!");
```
````

**Magic Move (Animated Transitions)**:
`````markdown
````magic-move{lines: true}
```js
// Before
const x = 1;
```
```js
// After - smooth animation
const x = 2;
const y = 3;
```
````
`````

---

## File Organization

```
examples/
├── basic-workflow/
│   ├── agent.js                # Simple agent initialization
│   ├── tools.js                # Tool definitions
│   └── package.json
│
├── advanced-patterns/
│   ├── spec-driven.js          # Spec-driven development example
│   ├── multi-agent.js          # Multi-agent collaboration
│   └── prompt-engineering.js   # Prompt structure patterns
│
└── claude-code-demo/
    ├── 01-init.sh              # Demo segment 1: initialization
    ├── 02-hooks.sh             # Demo segment 2: hooks
    ├── 03-mcp.sh               # Demo segment 3: MCP (optional)
    ├── sample-project/         # Demo project files
    └── README.md               # Demo execution guide
```

---

## Code Example Requirements

### 1. Executability

**Contract**: All code examples with `is_live_demo: true` MUST be executable and tested.

**Validation**:
```bash
# Each example directory must have test script
cd examples/basic-workflow
npm test  # or python test.py, etc.
```

**Status Tracking**:
- `untested` → has not been executed
- `passing` → executes successfully
- `failing` → has errors (BLOCKS section approval)

### 2. Display Formatting

**Contract**: Code blocks in slides MUST be ≤20 lines for readability.

**Best Practices**:
- Use `line_range` to show relevant subset
- Use `highlight_lines` to focus attention
- Split long examples across multiple slides with Magic Move

### 3. Syntax Highlighting

**Contract**: All code blocks MUST specify language for proper highlighting.

**Supported Languages**:
```
js, javascript, ts, typescript, python, py, bash, sh, yaml, yml, json, markdown, md, html, css, sql
```

**Configuration** (in `slidev.config.ts`):
```ts
export default {
  highlighter: 'shiki',
  shikiTheme: 'material-theme-palenight',
}
```

### 4. Progressive Highlighting

**Contract**: Use progressive highlighting for step-by-step explanations.

**Syntax**:
- **Static highlighting**: `{1,3,5-7}` - lines 1, 3, and 5 through 7
- **Progressive highlighting**: `{1|3-5|7}` - click reveals each group
- **Magic Move**: Animate transitions between code versions

**Example**:
````markdown
```js{1-2|4-6|8}
// Step 1: Setup
const agent = new Agent();
// Step 2: Configure
agent.loadTools();
agent.setContext();
// Step 3: Execute
agent.run();
```
````

---

## Demo Segment Contract

### Structure

Demo segments combine multiple code examples into a coherent live demonstration.

```yaml
demo_segments:
  - id: "demo-01-basics"
    title: "Claude Code Basics"
    order: 1
    duration_min: 3
    script: |
      1. cd examples/claude-code-demo
      2. claude init
      3. Show generated CLAUDE.md
      4. Run: "add a hello function to greet.js"
      5. Observe: file read → edit → test execution

    code_examples:
      - "demo-init-output"
      - "claude-md-template"
      - "hello-function-result"

    validation_checkpoints:
      - "CLAUDE.md file exists"
      - "greet.js contains hello function"
      - "Tests pass"

    backup_recording: "/demos/01-basics-demo.mp4"
    rehearsal_status: "validated"
```

### Rehearsal Workflow

```
scripted → (practice run) → rehearsed → (successful execution) → validated
```

**Requirements for "validated" status**:
1. All validation checkpoints pass
2. Demo completes within time budget (duration_min ± 30 seconds)
3. Backup recording MP4 exists in `/public/demos/`
4. Presenter can execute without script reference

---

## Asset Integration

### Code Screenshots

For static code displays (alternative to live code blocks):

```markdown
![Agent initialization code](./screenshots/agent-init.png)
```

**Requirements**:
- High resolution (2x retina: 3840x2160 for full-slide code)
- Dark theme with high contrast
- Font: Menlo/Monaco 16pt minimum
- Syntax highlighting colors matching slide theme

### Terminal Recordings

For demo backup or reference:

```html
<video controls width="100%" src="/demos/01-basics-demo.mp4" preload="none"></video>
```

**Requirements**:
- MP4 format, H.264 codec
- 1920x1080 or 2560x1440 resolution
- 2-5 Mbps bitrate
- ≤60 seconds duration
- Clear terminal output (dark background, light text, 16pt+ font)

---

## Validation Checklist

Before section reaches "approved" status:

- [ ] All code examples exist at specified `file_path`
- [ ] All code examples with `is_live_demo: true` have `test_status: passing`
- [ ] No code blocks exceed 20 lines when displayed
- [ ] All code blocks specify correct `language`
- [ ] Progressive highlighting syntax is valid (`{1,3|5-7}` not `{1,3-5-7}`)
- [ ] Demo segments have `rehearsal_status: validated`
- [ ] All demo segments have backup recordings in `/public/demos/`
- [ ] Total demo duration ≤15 minutes

---

## Example: Complete Code Example Lifecycle

### 1. Specification

```yaml
# In specs/sections/01-concepts.spec.md
code_examples:
  - id: "basic-workflow-agent"
    file_path: "basic-workflow/agent.js"
    language: javascript
    line_range: [1, 15]
    highlight_lines: "3,7-9"
    description: "Simple agentic workflow showing tool initialization and execution"
    is_live_demo: false
```

### 2. Implementation

```js
// examples/basic-workflow/agent.js
import { Agent } from 'agentic-sdk';

const agent = new Agent({
  name: 'demo-agent',
  tools: ['file-reader', 'code-editor', 'test-runner']
});

agent.setContext({
  projectPath: './sample-project'
});

agent.run('Add a greeting function');
```

### 3. Testing

```bash
cd examples/basic-workflow
npm install
npm test
# ✓ All tests pass
# test_status: passing
```

### 4. Embedding in Slide

````markdown
---
layout: default
section_id: "01-concepts"
---

# Tool-Enabled Execution

Agentic workflows use tools to interact with the environment:

```js{1-2|4-6|8-10|12}
import { Agent } from 'agentic-sdk';

const agent = new Agent({
  name: 'demo-agent',
  tools: ['file-reader', 'code-editor', 'test-runner']
});

agent.setContext({
  projectPath: './sample-project'
});

agent.run('Add a greeting function');
```

<v-click at="1">Agent initialization with tool registry</v-click>
<v-click at="2">Context setup (project location)</v-click>
<v-click at="3">Natural language instruction → tool orchestration</v-click>
````

### 5. Presenter Notes

```yaml
notes: |
  **Code Walkthrough** (90 seconds):
  - Click 1: Import and setup (10s)
  - Click 2: Tool registration - explain each tool (25s)
  - Click 3: Context provides project awareness (20s)
  - Click 4: Run command - agent orchestrates tools (35s)

  **Key Message**: Tools transform AI from text generator to development partner

  **Audience Check**: "How many use autocomplete daily? This is the next step."
```

---

## Contract Versioning

**Version**: 1.0.0  
**Last Updated**: 2026-04-16  
**Breaking Changes**: None

**Change Log**:
- 2026-04-16: Initial contract definition
