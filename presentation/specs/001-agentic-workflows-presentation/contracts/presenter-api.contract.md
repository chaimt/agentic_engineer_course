# Presenter API Contract

**Feature**: 001-agentic-workflows-presentation  
**Version**: 1.0.0  
**Purpose**: Define the interface for presenter notes, demo scripts, and rehearsal workflow

## Contract Overview

The Presenter API provides structured guidance for presentation delivery, including speaker notes, demo scripts, timing checkpoints, and backup strategies.

---

## Presenter Notes Format

### In Slide Frontmatter

```yaml
---
layout: default
notes: |
  **Talking Points** (60 seconds):
  - Introduce mental model shift: autocomplete → workflow partner
  - Use analogy: autocomplete is calculator, agent is spreadsheet
  - Reference target audience: "Who has used Copilot? This builds on that."

  **Audience Engagement**:
  - Pause for hands raised (10s)
  - Acknowledge experience levels

  **Transition**: "Now let's see what makes this shift possible..."
---
```

### Presenter Notes Structure

**Required Sections**:

1. **Talking Points** - Bullet list of key messages
2. **Timing** - Expected duration for this slide
3. **Audience Engagement** - Interactive elements (questions, polls, acknowledgments)
4. **Transitions** - Link to next slide/section

**Optional Sections**:

5. **Demo Checkpoints** - Validation steps for live demos
6. **Backup Plan** - Failover if demo/tech fails
7. **Deep Dive** - Additional context if audience asks questions

### Example: Concept Slide

```yaml
notes: |
  **Talking Points** (90 seconds):
  - Definition: Agentic workflows chain AI capabilities across multiple steps
  - Each step uses tools: file reads, shell commands, API calls
  - Contrast: autocomplete gives you one completion, agent completes entire task

  **Visual Cue**: Point to code example, highlight line 5 (tool registry)

  **Audience Check**: "How would this change your code review workflow?"
  Wait 5-10 seconds for mental processing.

  **Timing**: This slide is critical for mental model shift. Don't rush.

  **Transition**: "So why does this matter? Let's look at real adoption signals..."
```

### Example: Demo Slide

```yaml
notes: |
  **LIVE DEMO SEGMENT 2: Hooks** (3 minutes)

  **Pre-Demo Check** (30 seconds before):
  - Terminal in correct directory: cd examples/claude-code-demo
  - .clauderc configured with hooks
  - Git status clean

  **Script**:
  1. Open .clauderc, show hook definitions (20s)
  2. Make intentional style violation in code.js (15s)
  3. Run: git add && git commit -m "demo" (30s)
  4. Observe: pre-commit hook triggers, Claude auto-fixes style (45s)
  5. Show: corrected code.js (20s)
  6. Complete commit (10s)

  **Narration**:
  "Hooks let you embed quality gates directly in the workflow. Watch what happens
  when I try to commit code that violates our style guide..."

  **Validation Checkpoints**:
  - Hook triggers on commit
  - Style violation detected
  - Auto-fix applied
  - Commit succeeds with corrected code

  **Backup Plan**:
  - If hook fails to trigger: switch to /demos/02-hooks-demo.mp4
  - If auto-fix fails: show screenshot /screenshots/hooks-before-after.png

  **Time Budget**: 3 min (±30s). If over 3:30, skip "show corrected code" step.

  **Transition**: "Hooks are one pattern. Let's explore others..."
```

---

## Demo Script Contract

### Structure

Demo scripts live in `examples/claude-code-demo/` and follow this format:

```markdown
# Demo Segment 1: Claude Code Basics

**Duration**: 3 minutes  
**Order**: 1 of 3  
**Prerequisite**: Claude API key configured

## Setup

```bash
cd examples/claude-code-demo/sample-project
rm -rf .claude  # Clear previous state
git clean -fd   # Reset to baseline
```

## Script

### Step 1: Initialize Claude (30s)

**Command**:
```bash
claude init
```

**Expected Output**:
```
Initializing Claude Code in /Users/presenter/examples/claude-code-demo/sample-project
✓ Created CLAUDE.md
✓ Detected project type: Node.js
```

**Narration**:
"Claude Code detects the project type and generates a configuration file. Let's look at what it created..."

**Validation**: `CLAUDE.md` file exists

**Failover**: If init fails, switch to `/demos/01-basics-demo.mp4`

### Step 2: Show CLAUDE.md (45s)

**Command**:
```bash
cat CLAUDE.md
```

**Narration**:
"This file guides Claude's behavior. Notice the project description, coding standards, and architectural constraints. These become the agent's context."

**Pause**: 10 seconds for audience to read key sections

**Highlight**: Point to "Keep functions pure" guideline

### Step 3: Interactive Command (90s)

**Command**:
```bash
claude "add a hello function to greet.js that takes a name parameter"
```

**Expected Behavior**:
- Claude reads project files
- Edits greet.js
- Runs tests
- Reports success

**Narration**:
"Watch the tool usage. Claude reads the existing code, makes the edit, and validates with tests. All from one natural language instruction."

**Validation Checkpoints**:
- `greet.js` contains `hello` function
- Function signature: `hello(name)`
- Tests pass

**Failover**: If any step fails >30s, switch to recording

## Backup Assets

- **Recording**: `/public/demos/01-basics-demo.mp4`
- **Screenshots**: `/public/screenshots/demo-01-*.png`
- **Code State**: `examples/claude-code-demo/sample-project-expected/` (expected end state)

## Rehearsal Checklist

- [ ] All commands execute successfully
- [ ] Timing fits within 3 minutes (±30s)
- [ ] Validation checkpoints pass
- [ ] Backup recording exists
- [ ] Narration feels natural (not scripted)
- [ ] Transitions to next segment are smooth
```

---

## Rehearsal Workflow Contract

### Status Progression

```
scripted → rehearsed → validated
```

**Scripted**: Demo script written, not yet practiced  
**Rehearsed**: Full run-through completed, issues identified  
**Validated**: Successful execution, ready for presentation

### Rehearsal Schedule

```yaml
rehearsals:
  - date: "3 days before presentation"
    type: "Full run-through #1"
    focus: "Identify technical issues, timing problems"
    outcome: "Issue list"

  - date: "1 day before presentation"
    type: "Full run-through #2"
    focus: "Validate fixes, finalize narration"
    outcome: "rehearsal_status: rehearsed"

  - date: "1 hour before presentation"
    type: "Abbreviated check"
    focus: "Final system validation"
    outcome: "rehearsal_status: validated"
```

### Rehearsal Validation Criteria

**Technical Validation**:
- [ ] All demo commands execute successfully
- [ ] Validation checkpoints pass
- [ ] No unexpected errors or warnings
- [ ] Timing fits within budget (±10%)

**Delivery Validation**:
- [ ] Narration flows naturally
- [ ] Transitions are smooth
- [ ] Audience engagement points are effective
- [ ] Presenter can execute without script reference

**Backup Validation**:
- [ ] Backup recordings exist and play correctly
- [ ] Screenshot fallbacks cover all critical states
- [ ] Failover procedure is clear and fast (<10s to switch)

---

## Timing Contract

### Section Timing

Total presentation: 55 minutes (±5 minutes)

```yaml
sections:
  - id: "01-concepts"
    duration_min: 8
    slides: [5, 7]
    avg_per_slide: 68  # seconds

  - id: "02-benefits"
    duration_min: 7
    slides: [4, 5]
    avg_per_slide: 84

  - id: "03-demo"
    duration_min: 15
    slides: [3, 5]
    demo_segments: 3
    avg_per_segment: 300  # 5 minutes per demo segment

  - id: "04-patterns"
    duration_min: 10
    slides: [6, 8]
    avg_per_slide: 75

  - id: "05-tips"
    duration_min: 8
    slides: [5, 6]
    avg_per_slide: 80

  - id: "06-qa"
    duration_min: 7
    slides: [1, 2]
    buffer: "Flexible time for questions"
```

### Slide Timing Guidelines

**Concept Slides**: 60-90 seconds  
**Code Slides**: 90-120 seconds (includes click-through)  
**Demo Slides**: 180-300 seconds (includes live execution)  
**Section Dividers**: 10-15 seconds

### Time Management

**Buffer Strategy**:
- Q&A section (7 min) is flexible buffer
- Pattern #4 (Multi-Agent) is marked optional if running late
- Demo segment #3 (Advanced) can be skipped

**Time Checkpoints**:
```yaml
checkpoints:
  - slide: "End of Section 01"
    elapsed_min: 8
    action_if_late: "Reduce Section 02 buffer (benefits)"

  - slide: "Start of Demo"
    elapsed_min: 15
    action_if_late: "Skip demo segment #3 (advanced)"

  - slide: "End of Patterns"
    elapsed_min: 40
    action_if_late: "Shorten tips section, reduce Q&A to 5 min"
```

---

## Backup Strategy Contract

### Multi-Layer Failover

**Layer 1: Screen Recordings** (Primary Backup)

```yaml
backup_recordings:
  - segment: "demo-01-basics"
    path: "/public/demos/01-basics-demo.mp4"
    duration: "3:15"
    trigger: "If live demo fails >30s into execution"

  - segment: "demo-02-hooks"
    path: "/public/demos/02-hooks-demo.mp4"
    duration: "3:00"
    trigger: "If hooks don't trigger within 45s"

  - segment: "demo-03-advanced"
    path: "/public/demos/03-advanced-demo.mp4"
    duration: "2:45"
    trigger: "If MCP connection fails"
```

**Failover Procedure**:
1. Recognize failure (validation checkpoint fails)
2. Verbalize: "Let me show you a prepared example of this workflow..."
3. Switch to recording (HTML video player, pre-loaded)
4. Narrate over recording
5. Resume live presentation after recording ends

**Layer 2: Screenshot Fallbacks**

```yaml
screenshot_fallbacks:
  - state: "CLAUDE.md generated"
    path: "/public/screenshots/claude-md-example.png"
    use_case: "If init fails completely"

  - state: "Hooks auto-fix result"
    path: "/public/screenshots/hooks-before-after.png"
    use_case: "If hook demo fails but need to show concept"
```

**Failover Procedure**:
1. Show screenshot: "Here's what this typically produces..."
2. Walk through static image
3. Resume next slide

**Layer 3: Presenter Notes Narration**

```yaml
notes: |
  **If All Tech Fails**:
  Narrate the workflow from presenter notes without showing execution:
  "In a typical workflow, you'd run 'claude init', which generates a CLAUDE.md
  file with project context. Then you issue natural language commands like
  'add a hello function', and Claude reads your code, makes edits, runs tests..."

  **Key Point**: Emphasize the concept even if demo fails. The idea is more
  important than perfect execution.
```

---

## Presenter Mode Features

### Slidev Presenter View

Access via built-in presenter mode (separate window):

```yaml
presenter_view:
  layout:
    - slide_preview: "Next slide preview"
    - speaker_notes: "Markdown notes from frontmatter"
    - timer: "Elapsed time + slide timing"
    - controls: "Navigation, drawing tools"

  keyboard_shortcuts:
    - "p": "Toggle presenter mode"
    - "o": "Toggle slide overview"
    - "d": "Toggle dark mode"
    - "g": "Go to slide (type number)"
```

### Custom Presenter Tools

```yaml
custom_tools:
  - timer_display: "Visible elapsed time"
  - checkpoint_alerts: "Visual alert at time checkpoints"
  - demo_status: "Indicator for rehearsal_status of upcoming demos"
  - backup_quick_access: "Hotkeys for failover to recordings"
```

---

## Audience Engagement Contract

### Interactive Elements

**Allowed in Presenter-Driven Format**:
- ✅ Show of hands questions ("Who has used Copilot?")
- ✅ Rhetorical questions for mental processing
- ✅ Observational pauses (watch live demo execute)
- ✅ Q&A throughout presentation (brief answers inline)
- ✅ Q&A section at end (7 minutes dedicated time)

**Not Allowed (per spec FR-004)**:
- ❌ Audience hands-on coding exercises
- ❌ Pair programming activities
- ❌ Setup/installation during presentation
- ❌ Audience screen sharing

### Engagement Tracking

```yaml
engagement_checkpoints:
  - slide: "01-concepts-slide-02"
    type: "show_of_hands"
    question: "Who has used GitHub Copilot or similar AI tools?"
    purpose: "Gauge experience level, tailor explanation depth"

  - slide: "03-demo-slide-01"
    type: "rhetorical"
    question: "What would this mean for your code review time?"
    purpose: "Mental processing of benefits, personal relevance"

  - slide: "05-tips-slide-04"
    type: "pause"
    duration: 10s
    purpose: "Let attendees absorb challenge/solution pairings"
```

---

## Validation Checklist

Before presentation day:

**Content**:
- [ ] All presenter notes follow structured format
- [ ] All demo scripts have narration guidance
- [ ] All slides have timing estimates
- [ ] Total presentation duration is 55-60 minutes

**Rehearsal**:
- [ ] Full run-through #1 completed (3 days before)
- [ ] Full run-through #2 completed (1 day before)
- [ ] All demo segments have `rehearsal_status: validated`
- [ ] Timing fits within budget (±5 minutes)

**Backups**:
- [ ] All demo recordings exist and play correctly
- [ ] All screenshot fallbacks exist and are high quality
- [ ] Failover procedures are documented and tested
- [ ] Presenter knows how to switch to backups quickly

**Technical**:
- [ ] Claude API key configured and tested
- [ ] Demo environments reset to baseline state
- [ ] Terminal theme/font configured for visibility
- [ ] Presentation environment supports screen sharing

---

## Contract Versioning

**Version**: 1.0.0  
**Last Updated**: 2026-04-16  
**Breaking Changes**: None

**Change Log**:
- 2026-04-16: Initial presenter API contract definition
