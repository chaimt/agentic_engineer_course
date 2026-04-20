import { defineConfig } from '@slidev/cli'

export default defineConfig({
  // Basic presentation configuration
  title: 'Agentic Workflows',
  theme: 'default',

  // Syntax highlighting - using dark theme to complement black/orange
  highlighter: 'shiki',
  shikiTheme: 'github-dark',

  // Monaco editor for interactive code examples
  monaco: 'dev',

  // Layout and rendering
  layout: 'default',
  aspectRatio: '16/9',
  canvasWidth: 980,

  // Export configuration
  exportFilename: 'agentic-workflows-presentation',

  // Download configuration
  download: true,

  // Enable presenter mode
  presenter: true,

  // Color scheme
  colorSchema: 'auto',

  // Fonts
  fonts: {
    sans: 'Roboto',
    serif: 'Roboto Slab',
    mono: 'Fira Code',
  },

  // Enable drawings
  drawings: {
    enabled: true,
    persist: false,
  },

  // Navigation
  controls: true,

  // UnoCSS configuration
  css: 'unocss',
})
