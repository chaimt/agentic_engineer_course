/**
 * Shiki Syntax Highlighting Configuration
 *
 * Custom configuration for code highlighting in Agentic Workflows presentation
 * Uses dark theme to complement black and orange color scheme
 */

import type { ShikiSetupReturn } from '@slidev/types'

export default function setup(): ShikiSetupReturn {
  return {
    theme: {
      dark: 'github-dark',
      light: 'github-light',
    },
    langs: [
      'javascript',
      'typescript',
      'python',
      'json',
      'yaml',
      'markdown',
      'bash',
      'shell',
    ],
  }
}
