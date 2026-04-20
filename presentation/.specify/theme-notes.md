# Theme Notes: Black and Orange Technical Presentation

**Theme**: Black and Orange - Professional Technical Design
**Status**: Theme updated to black/orange color scheme per specification
**Date**: 2026-04-20 (Updated)

## Color Scheme

### Primary Colors
- **Primary Orange**: `#ff6b35` - Used for main headings, primary accents, and CTAs
- **Bright Orange**: `#ff9f1c` - Used for highlights and interactive elements
- **Dark Orange**: `#d94f30` - Used for hover states and secondary accents

### Background Colors
- **Pure Black**: `#000000` - Main slide background (maximum contrast)
- **Charcoal Black**: `#0a0a0a` - Alternate background for sections
- **Dark Gray**: `#1a1a1a` - Code block background
- **Medium Gray**: `#2a2a2a` - Secondary elements background

### Text Colors
- **Primary Text**: `#ffffff` - Body text (pure white on black)
- **Heading Text**: `#ff6b35` - H1 headings (primary orange)
- **Muted Text**: `#cccccc` - Secondary information (light gray)
- **Code Text**: `#f0f0f0` - Code block text

### Accent Colors
- **Success Orange**: `#ff9f1c` - Success states, checkmarks (bright orange)
- **Warning Orange**: `#ffb347` - Warnings, important notes (lighter orange)
- **Error Orange**: `#d94f30` - Errors, critical information (dark orange)
- **Link Orange**: `#ff6b35` - Links and interactive elements

## Typography

### Fonts
- **Sans Serif**: Roboto - Body text and UI elements
- **Serif**: Roboto Slab - Headings for emphasis
- **Monospace**: Fira Code - Code blocks and technical content

### Font Sizes
- **H1**: 3rem (48px) - Title slides
- **H2**: 2rem (32px) - Section headers
- **H3**: 1.5rem (24px) - Subsection headers
- **Body**: 1.125rem (18px) - Paragraph text
- **Code**: 0.95rem (15.2px) - Code blocks

### Font Weights
- **Bold**: 700 - Main titles
- **Semibold**: 600 - Subheadings
- **Regular**: 400 - Body text

## Layout Patterns

### Title Slide (Cover Layout)
- Centered alignment
- Large title (H1)
- Subtitle or tagline
- Optional author/date information
- Minimal visual elements

### Section Header Slide
- Bold section title (H2)
- Optional subtitle or description
- Accent color background or border
- Clean separation from content slides

### Content Slide (Default Layout)
- Title at top (H2)
- 2-column support for content + visuals
- Bullet points with adequate spacing
- Maximum 6 elements per slide

### Pattern Showcase Slide
- Pattern name as title
- Code example (≤20 lines)
- Diagram or visualization
- Key characteristics list

### Code Demo Slide
- Full-width code block
- Syntax highlighting (Material Theme Palenight)
- Progressive line highlighting support
- Line numbers optional

## Spacing

### Margins
- **Slide Margins**: 2rem (32px) all sides
- **Content Padding**: 1rem (16px) between elements
- **Section Gap**: 1.5rem (24px) between major sections

### Line Heights
- **Headings**: 1.2 - Tight for impact
- **Body Text**: 1.75 - Comfortable reading
- **Code**: 1.6 - Clear line separation

## Visual Elements

### Borders
- **Code Blocks**: 1px solid border with rounded corners (0.5rem)
- **Section Headers**: Optional bottom border for emphasis

### Shadows
- **Elevated Elements**: Subtle shadow for depth (optional)
- **Code Blocks**: No shadow, rely on border

### Transitions
- **Slide Transitions**: Smooth fade or slide (200-300ms)
- **Animations**: Minimal, purposeful only
- **Hover Effects**: Subtle color transitions (200ms)

## Accessibility

### Contrast Ratios
- Text on dark background: Minimum 7:1 (AAA standard)
- Code highlighting: Sufficient contrast for all tokens

### Font Sizes
- Minimum body text: 18pt for readability in presentation context
- Code blocks: 15pt minimum

### Focus Indicators
- Interactive elements: Visible focus ring
- Navigation: Clear active state

## Code Syntax Highlighting

**Theme**: Material Theme Palenight (Shiki)

### Token Colors
- **Keywords**: `#c792ea` (purple) - `function`, `const`, `let`
- **Strings**: `#c3e88d` (green) - String literals
- **Functions**: `#82aaff` (blue) - Function names
- **Comments**: `#676e95` (gray) - Comments, annotations
- **Variables**: `#f07178` (red) - Variable names
- **Operators**: `#89ddff` (cyan) - `=`, `+`, `=>` 
- **Numbers**: `#f78c6c` (orange) - Numeric literals
- **Classes**: `#ffcb6b` (yellow) - Class names
- **Punctuation**: `#89ddff` (cyan) - Brackets, parens

## Implementation Notes

1. **Maximum Contrast**: Black background with orange accents provides excellent readability
2. **Professional Technical Aesthetic**: Black/orange conveys modern, developer-focused brand
3. **Code-First Design**: Code blocks are primary content with high-contrast syntax highlighting
4. **Progressive Disclosure**: Support click-through highlights in code with orange markers
5. **Responsive Text**: Font sizes tested at 1920x1080 minimum with high contrast
6. **Minimal Animations**: Performance over flash, orange accent animations only
7. **Consistent Spacing**: Rhythm and hierarchy through whitespace and orange dividers
8. **Accessibility**: WCAG AAA contrast ratio (21:1 black on white, 8.2:1 orange on black)

## Customization Points

Areas where theme may need adjustment based on actual reference slides:
- [ ] Exact brand color values (if different from defaults)
- [ ] Logo placement and size
- [ ] Custom background patterns or gradients
- [ ] Specific layout tweaks for 2-column slides
- [ ] Speaker notes formatting preferences
