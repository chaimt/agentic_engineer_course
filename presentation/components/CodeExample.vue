<template>
  <div class="code-example">
    <div class="example-header">
      <div class="example-title">
        <span class="icon">{{ icon }}</span>
        <span class="title-text">{{ title }}</span>
      </div>
      <div class="example-language">
        <span class="language-badge">{{ language }}</span>
      </div>
    </div>

    <div class="example-description" v-if="description">
      <p>{{ description }}</p>
    </div>

    <div class="code-container">
      <div class="code-header">
        <span class="file-name">{{ filename }}</span>
        <button @click="copyCode" class="copy-button" :class="{ copied: copied }">
          <carbon:copy v-if="!copied" />
          <carbon:checkmark v-else />
          <span class="button-text">{{ copied ? 'Copied!' : 'Copy' }}</span>
        </button>
      </div>
      <div class="code-content">
        <slot>
          <!-- Code will be inserted here via slot -->
        </slot>
      </div>
    </div>

    <div class="example-footer" v-if="highlights && highlights.length > 0">
      <div class="highlights">
        <span class="highlight-label">Key Points:</span>
        <ul class="highlight-list">
          <li v-for="(highlight, index) in highlights" :key="index">
            {{ highlight }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    default: ''
  },
  language: {
    type: String,
    default: 'python'
  },
  filename: {
    type: String,
    default: 'example.py'
  },
  icon: {
    type: String,
    default: '💻'
  },
  highlights: {
    type: Array,
    default: () => []
  }
})

const copied = ref(false)

const copyCode = () => {
  const codeElement = document.querySelector('.code-content pre')
  if (codeElement) {
    const code = codeElement.textContent
    navigator.clipboard.writeText(code)
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  }
}
</script>

<style scoped>
.code-example {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 107, 53, 0.3);
  border-radius: 0.75rem;
  overflow: hidden;
  margin: 1rem 0;
}

.example-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  background: rgba(255, 107, 53, 0.1);
  border-bottom: 1px solid rgba(255, 107, 53, 0.3);
}

.example-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.icon {
  font-size: 1.5rem;
}

.title-text {
  font-size: 1.125rem;
  font-weight: 600;
  color: #ffffff;
}

.language-badge {
  background: #ff6b35;
  color: #000000;
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
}

.example-description {
  padding: 1rem 1.5rem;
  color: #cccccc;
  font-size: 0.95rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.example-description p {
  margin: 0;
}

.code-container {
  background: #1a1a1a;
}

.code-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 1rem;
  background: #0a0a0a;
  border-bottom: 1px solid #ff6b35;
}

.file-name {
  color: #ff9f1c;
  font-family: 'Fira Code', monospace;
  font-size: 0.85rem;
}

.copy-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: transparent;
  border: 1px solid #ff6b35;
  color: #ff6b35;
  padding: 0.375rem 0.75rem;
  border-radius: 0.25rem;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.2s;
}

.copy-button:hover {
  background: rgba(255, 107, 53, 0.2);
}

.copy-button.copied {
  border-color: #ff9f1c;
  color: #ff9f1c;
}

.button-text {
  font-size: 0.8rem;
  font-weight: 600;
}

.code-content {
  padding: 1rem;
  overflow-x: auto;
}

.code-content::-webkit-scrollbar {
  height: 8px;
}

.code-content::-webkit-scrollbar-track {
  background: #0a0a0a;
}

.code-content::-webkit-scrollbar-thumb {
  background: #ff6b35;
  border-radius: 4px;
}

.example-footer {
  padding: 1rem 1.5rem;
  background: rgba(255, 159, 28, 0.05);
  border-top: 1px solid rgba(255, 107, 53, 0.3);
}

.highlights {
  color: #ffffff;
}

.highlight-label {
  font-weight: 600;
  color: #ff9f1c;
  margin-bottom: 0.5rem;
  display: block;
}

.highlight-list {
  margin: 0.5rem 0 0 0;
  padding-left: 1.5rem;
}

.highlight-list li {
  margin-bottom: 0.25rem;
  font-size: 0.9rem;
  color: #cccccc;
}

.highlight-list li::marker {
  color: #ff6b35;
}
</style>
