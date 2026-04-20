# Quickstart Guide: Agentic Workflows Presentation

**Feature**: 001-agentic-workflows-presentation  
**Audience**: Presenters delivering the Agentic Workflows presentation  
**Time to Setup**: ~30 minutes first time, ~10 minutes for rehearsal resets

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Initial Setup](#initial-setup)
3. [Content Workflow](#content-workflow)
4. [Rehearsal Process](#rehearsal-process)
5. [Presentation Delivery](#presentation-delivery)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software

- **Node.js**: 18+ LTS
- **npm** or **pnpm**: Latest version
- **Git**: For version control and demo baseline
- **Claude API Key**: For live Claude Code demonstrations
- **Terminal**: iTerm2, Hyper, or native terminal with theme support

### Required Knowledge

- Familiarity with Slidev (or willingness to learn basics)
- Understanding of agentic workflows concepts (read `research.md`)
- Comfort with live coding demonstrations

### System Requirements

- **OS**: macOS, Linux, or Windows with WSL
- **Display**: Supports 1920x1080 minimum (presenter + audience screens)
- **Network**: Stable internet for Claude API calls during demo
- **Storage**: ~500 MB for project + recordings

---

## Initial Setup

### Step 1: Clone and Install

```bash
# Navigate to presentation directory
cd presentation

# Install dependencies
npm install

# Verify Slidev installation
npx slidev --version
```

**Expected Output**:
```
@slidev/cli/0.x.x
```

### Step 2: Configure Environment

```bash
# Set Claude API key (for live demos)
export ANTHROPIC_API_KEY="your-api-key-here"

# Verify API access
claude --version  # or appropriate test command
```

**Add to your shell profile** (`.zshrc`, `.bashrc`):
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### Step 3: Verify Project Structure

```bash
tree -L 2 -I 'node_modules'
```

**Expected Structure**:
```
presentation/
├── slides/                   # Slidev presentation
├── examples/                 # Code examples and demos
├── assets/ or public/        # Presentation assets
├── specs/                    # Feature specifications
│   └── 001-agentic-workflows-presentation/
├── package.json
└── slidev.config.ts (if exists)
```

### Step 4: Generate Slides (if using spec-driven workflow)

```bash
# Generate Slidev markdown from specifications
.specify/scripts/generate-slides.sh

# Or manually ensure slides exist in slides/ directory
```

### Step 5: Test Presentation

```bash
# Start Slidev development server
npm run dev

# Or
npx slidev slides.md
```

**Access**:
- **Main presentation**: http://localhost:3030
- **Presenter mode**: http://localhost:3030/presenter
- **Overview**: http://localhost:3030/overview

**Verify**:
- [ ] All slides load without errors
- [ ] Code syntax highlighting works
- [ ] Images and assets display correctly
- [ ] Presenter notes appear in presenter mode

---

## Content Workflow

### Understanding the Spec-Driven Approach

This presentation follows Constitutional Principle IV: **Specification-Driven Slides**. Content is authored in `specs/`, then generated into `slides/`.

```
specs/sections/*.spec.md  →  [generation]  →  slides/sections/*.md
         (source of truth)                      (generated, read-only)
```

### Editing Content

**❌ DO NOT** edit files in `slides/sections/` directly - changes will be overwritten.

**✅ DO** edit section specifications in `specs/001-agentic-workflows-presentation/sections/`:

```bash
# Edit a section specification
vim specs/001-agentic-workflows-presentation/sections/01-concepts.spec.md
```

**Section Spec Format** (see `contracts/section-spec.schema.yaml`):
```yaml
---
section_id: "01-concepts"
title: "What are Agentic Workflows"
order: 1
duration_min: 8
slide_count_range: [5, 7]
---

## Learning Objectives
- Define agentic workflows (understand, quiz, SC-001)
- Explain mental model shift (analyze, observation, SC-002)

## Slides

### Slide 1: Cover
Layout: cover
Content: [markdown content here]
Notes: [presenter notes here]

### Slide 2: Definition
Layout: default
Content: [markdown content with code references]
Code: @basic-workflow-agent{1-10}{highlight:3-5}
Notes: [presenter notes with timing and talking points]

## Code Examples
- basic-workflow-agent: examples/basic-workflow/agent.js (lines 1-10)

## Assessment
- Quiz: "What distinguishes agentic workflows?" (multiple_choice, 90%)
```

### Regenerating Slides

```bash
# After editing specs, regenerate Slidev markdown
.specify/scripts/generate-slides.sh

# Verify changes
npm run dev
```

### Adding Code Examples

1. **Create example file**:
```bash
# Create example in examples/ directory
mkdir -p examples/my-feature
vim examples/my-feature/agent.js
```

2. **Add to section spec**:
```yaml
code_examples:
  - id: "my-feature-agent"
    file_path: "my-feature/agent.js"
    language: javascript
    line_range: [1, 15]
    highlight_lines: "3,7-9"
    description: "Demonstrates my feature"
    is_live_demo: false
```

3. **Reference in slide content**:
```markdown
<<< @/examples/my-feature/agent.js{1-15}{3,7-9}
```

4. **Test the code**:
```bash
cd examples/my-feature
npm install  # if needed
node agent.js
# Verify it works
```

### Adding Assets

1. **Add file to public/** (or assets/):
```bash
# Screenshots
cp screenshot.png public/screenshots/feature-demo.png

# Diagrams
cp diagram.svg public/diagrams/workflow-architecture.svg

# Videos
cp demo.mp4 public/demos/01-feature-demo.mp4
```

2. **Optimize** (if needed):
```bash
# Compress PNG
pngquant public/screenshots/feature-demo.png --output public/screenshots/feature-demo.png --force

# Check video codec
ffprobe public/demos/01-feature-demo.mp4
# Should be: H.264, 720p-1080p, 2-5 Mbps
```

3. **Reference in slide**:
```markdown
![Feature demonstration](./screenshots/feature-demo.png)

<!-- or in frontmatter -->
---
background: /diagrams/workflow-architecture.svg
---
```

---

## Rehearsal Process

### Rehearsal Schedule

**3 Days Before Presentation**: Full Run-Through #1  
**1 Day Before Presentation**: Full Run-Through #2  
**1 Hour Before Presentation**: Abbreviated Check

### Pre-Rehearsal Setup

```bash
# Reset demo environments to baseline
cd examples/claude-code-demo
git clean -fd
rm -rf .claude node_modules/.cache
git checkout .

# Verify demo prerequisites
cd sample-project
npm install
npm test  # Should pass
cd ../..

# Verify Claude API access
export ANTHROPIC_API_KEY="your-key"
claude --version  # Or test command
```

### Full Run-Through Procedure

1. **Start presentation**:
```bash
npm run dev
# Open http://localhost:3030/presenter
```

2. **Start timer**: Note start time

3. **Present all sections**:
   - Narrate talking points from presenter notes
   - Execute live demos according to demo scripts
   - Track actual timing vs. target timing
   - Note any issues or improvements

4. **Record outcomes**:
```markdown
## Rehearsal Log: [Date]

**Total Duration**: X minutes (target: 55-60)

**Section Timing**:
- 01-concepts: X min (target: 8)
- 02-benefits: X min (target: 7)
- 03-demo: X min (target: 15)
- 04-patterns: X min (target: 10)
- 05-tips: X min (target: 8)
- 06-qa: X min (target: 7)

**Issues**:
- [ ] Demo segment 2 failed at step 3 (hook didn't trigger)
- [ ] Slide timing too fast in section 04
- [ ] Code example on slide 12 has syntax error

**Action Items**:
- Fix hook configuration in .clauderc
- Add pauses in section 04 narration
- Correct code example and regenerate
```

### Demo Segment Rehearsal

**For each demo segment** (e.g., `demo-01-basics`):

1. **Reset environment**:
```bash
cd examples/claude-code-demo
./reset-demo.sh  # or manual reset commands
```

2. **Follow demo script** (`examples/claude-code-demo/01-basics.md`):
   - Execute each command
   - Verify validation checkpoints
   - Time the segment (target: 3 minutes ±30s)

3. **Record backup** (if not already done):
```bash
# Use OBS, QuickTime, or ScreenFlow
# Record: Terminal + narration
# Export: MP4, H.264, 1920x1080, 2-5 Mbps
# Save to: public/demos/01-basics-demo.mp4
```

4. **Update rehearsal status**:
```yaml
# In specs/sections/03-demo.spec.md
demo_segments:
  - id: "demo-01-basics"
    rehearsal_status: validated  # Change from rehearsed
```

### Validation Checklist (Before Presentation)

- [ ] All 3 demo segments have `rehearsal_status: validated`
- [ ] Total presentation duration is 55-60 minutes
- [ ] All demo validation checkpoints pass
- [ ] All backup recordings exist and play correctly
- [ ] Failover procedures tested and documented
- [ ] Presenter can execute demos without script reference
- [ ] No code examples have syntax errors
- [ ] All assets load correctly in slides

---

## Presentation Delivery

### Day-of Setup (1 Hour Before)

**1. Environment Check**:
```bash
# Verify system
node --version  # 18+
npm --version
claude --version

# Verify API key
echo $ANTHROPIC_API_KEY
# Should output your key
```

**2. Reset Demo Environments**:
```bash
cd examples/claude-code-demo
./reset-demo.sh
cd ../..
```

**3. Configure Terminal**:
- **Theme**: High contrast (dark background, light text)
- **Font**: Menlo/Monaco, 16pt minimum
- **Window**: Full screen, hide menu bar, no notifications
- **Layout**: If using tmux/splits, configure now

**4. Start Presentation**:
```bash
npm run dev

# Open presenter mode in separate window/screen
open http://localhost:3030/presenter

# Main screen shows audience view
```

**5. Verify Technical**:
- [ ] Presenter mode shows notes and next slide
- [ ] All slides load (click through quickly)
- [ ] Code highlighting works
- [ ] Assets display
- [ ] Demo terminals ready

### During Presentation

**Presenter Mode Features**:
- **Left**: Current slide
- **Right**: Next slide preview
- **Bottom**: Presenter notes (from frontmatter)
- **Top**: Timer and slide number

**Navigation**:
- `→` or `Space`: Next slide
- `←`: Previous slide
- `Home`: First slide
- `End`: Last slide
- `O`: Slide overview
- `D`: Toggle dark mode
- `G`: Go to slide (type number)

**Demo Execution**:

Follow demo scripts exactly:
1. Read presenter notes before each demo segment
2. Execute commands from script
3. Validate checkpoints as you go
4. Watch for timing (stay within budget ±30s)
5. If failure >30s, switch to backup recording

**Failover to Backup**:
```html
<!-- In slide, pre-loaded video -->
<video controls width="100%" src="/demos/01-basics-demo.mp4"></video>

<!-- Say: "Let me show you a prepared example..." -->
<!-- Play video, narrate over it -->
```

**Time Management**:

Check timer at these checkpoints:
- End of Section 01: 8 min elapsed
- Start of Demo: 15 min elapsed
- End of Patterns: 40 min elapsed

If running late:
- Reduce Section 02 buffer (skip one benefit example)
- Skip demo segment #3 (advanced)
- Shorten tips section (5 min instead of 8)
- Reduce Q&A to 5 min

### Audience Engagement

**Allowed**:
- Show of hands questions: "Who has used Copilot?"
- Rhetorical questions: "What would this mean for your workflow?"
- Brief inline Q&A: "Good question - here's the key difference..."
- Observational pauses: Let audience watch demo execute (10-15s)

**Not Allowed** (per spec):
- Hands-on coding exercises
- Audience screen sharing
- Setup/installation activities

**Q&A Section**:
- Reserve 7 minutes at end
- If questions come up earlier, answer briefly or defer to Q&A
- Use extra Q&A time if presentation finishes early

---

## Troubleshooting

### Issue: Slides Don't Load

**Symptoms**: Blank screen, error in console

**Solutions**:
1. Check for syntax errors in markdown:
```bash
# Lint slides
npx markdownlint slides/*.md
```

2. Verify frontmatter syntax:
```yaml
---
layout: default  # No quotes if simple value
title: "Title"   # Quotes if contains special chars
---
```

3. Check file paths:
```markdown
# Absolute paths for public/ assets
![Image](/screenshots/demo.png)

# Relative paths for code imports
<<< @/examples/code.js
```

4. Clear cache:
```bash
rm -rf node_modules/.cache
npm run dev
```

### Issue: Code Highlighting Broken

**Symptoms**: Code blocks show plain text, no colors

**Solutions**:
1. Verify language is supported:
```markdown
```js  <!-- Good -->
```javascript  <!-- Also good -->
```jsx  <!-- If configured -->
```

2. Check Shiki configuration in `slidev.config.ts`:
```ts
export default {
  highlighter: 'shiki',
  shikiTheme: 'material-theme-palenight',
}
```

3. Verify line highlighting syntax:
```markdown
```js{1,3-5}  <!-- Good -->
```js{1,3,5-7}  <!-- Good -->
```js{1|3-5|7}  <!-- Good (progressive) -->
```js{1-3-5}  <!-- BAD - use commas or pipes -->
```

### Issue: Demo Fails During Presentation

**Symptoms**: Command doesn't execute, validation checkpoint fails

**Solutions**:

**Immediate** (< 30s):
1. Re-run command once
2. Check validation checkpoint again

**If still fails** (>30s):
1. Verbalize: "Let me show you a prepared example of this..."
2. Switch to backup recording:
```markdown
<!-- Slide should have pre-loaded video -->
<video controls src="/demos/01-basics-demo.mp4"></video>
```

3. Play recording, narrate over it
4. Resume next slide after recording

**Alternative** (if video fails):
1. Show screenshot fallback
2. Narrate expected behavior from presenter notes
3. Emphasize concept over execution: "The key idea is..."

### Issue: Presenter Mode Not Showing Notes

**Symptoms**: Presenter view shows slide but no notes

**Solutions**:
1. Verify frontmatter has `notes:` field:
```yaml
---
layout: default
notes: |
  Your notes here
  Multiple lines supported
---
```

2. Check for YAML syntax errors:
```yaml
---
notes: |  # Pipe for multiline
  Content
---

# OR

---
notes: "Single line"
---
```

3. Restart Slidev:
```bash
# Kill server (Ctrl+C)
npm run dev
# Reopen presenter mode
```

### Issue: Running Out of Time

**Symptoms**: Already at 50 minutes, still 2 sections left

**Solutions**:

**Immediate adjustments**:
- Skip demo segment #3 (advanced) - saves 3 min
- Reduce patterns section: skip multi-agent pattern (P2) - saves 3 min
- Shorten tips section: cover 3 tips instead of 5 - saves 3 min
- Reduce Q&A to 5 min instead of 7 - saves 2 min

**Communication**:
- "In the interest of time, I'll skip the advanced demo and focus on core patterns..."
- "For additional patterns, see the resources slide at the end"

**Never**:
- Rush through demo (reduces effectiveness)
- Skip Q&A entirely (violates FR-001 requirement)
- Extend beyond 65 minutes (respect audience time)

### Issue: Audience Question Derails Timing

**Symptoms**: Great question but requires 5-minute deep dive

**Solutions**:

**During presentation**:
- "Excellent question - let me give a brief answer now..."
- Provide 60-second response
- "We can dive deeper in Q&A or offline after the presentation"

**Defer to Q&A**:
- "I'll add that to my list for Q&A - remind me if I forget"
- Write question on notepad/slide
- Address in Q&A section

**Offline**:
- "That's worth a dedicated conversation - can we connect after?"
- Collect contact info or point to resources

---

## Additional Resources

### Files to Read Before Presenting

1. **research.md** - Content research (R1-R7) for subject matter understanding
2. **data-model.md** - Content structure and relationships
3. **contracts/** - Detailed specifications for all content types
4. **plan.md** - Technical context and architectural decisions

### Slidev Documentation

- [Official Slidev Docs](https://sli.dev/)
- [Syntax Guide](https://sli.dev/guide/syntax)
- [Presenter Mode](https://sli.dev/guide/presenter-mode)
- [Animations](https://sli.dev/guide/animations)

### Demo Resources

- `examples/claude-code-demo/README.md` - Demo execution guide
- `examples/claude-code-demo/01-basics.md` - Demo segment 1 script
- `examples/claude-code-demo/02-hooks.md` - Demo segment 2 script
- `examples/claude-code-demo/03-advanced.md` - Demo segment 3 script

### Support

- **Issues**: Report at project repository
- **Questions**: Contact feature owner or technical lead
- **Improvements**: Submit feedback via `.specify/memory/` or pull request

---

## Quick Reference

### Common Commands

```bash
# Start presentation
npm run dev

# Build static version
npm run build

# Export PDF (if configured)
npm run export

# Reset demo environment
cd examples/claude-code-demo && ./reset-demo.sh

# Regenerate slides from specs
.specify/scripts/generate-slides.sh

# Validate section specs against schema
.specify/scripts/validate-specs.sh  # (if exists)
```

### Keyboard Shortcuts (Presenter Mode)

| Key | Action |
|-----|--------|
| `→` or `Space` | Next slide |
| `←` | Previous slide |
| `Home` | First slide |
| `End` | Last slide |
| `O` | Slide overview |
| `G` | Go to slide (type number) |
| `D` | Toggle dark mode |
| `P` | Toggle presenter mode |
| `F` | Toggle fullscreen |

### Timing Quick Reference

| Section | Target (min) | Slides | Notes |
|---------|--------------|--------|-------|
| 01-Concepts | 8 | 5-7 | Foundation - don't rush |
| 02-Benefits | 7 | 4-5 | Can reduce if running late |
| 03-Demo | 15 | 3-5 | Critical - maintain quality |
| 04-Patterns | 10 | 6-8 | Can skip pattern #4 if late |
| 05-Tips | 8 | 5-6 | Can shorten to 5 min |
| 06-Q&A | 7 | 1-2 | Flexible buffer |
| **Total** | **55** | **30-35** | Target: 55-60 min |

---

**Version**: 1.0.0  
**Last Updated**: 2026-04-19  
**Maintainer**: Feature Owner (001-agentic-workflows-presentation)
