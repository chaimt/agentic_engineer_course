<template>
  <div class="code-demo-layout slidev-layout">
    <!-- Header with pattern name -->
    <div class="demo-header">
      <h1 v-if="$slidev.nav.currentLayout === 'code-demo'">
        <slot name="title">{{ $slidev.nav.currentSlideNo }}</slot>
      </h1>
    </div>

    <!-- Main content area -->
    <div class="demo-content">
      <!-- Left side: Explanation -->
      <div class="explanation">
        <slot />
      </div>

      <!-- Right side: Code display -->
      <div class="code-display">
        <slot name="code">
          <!-- Code blocks will be inserted here -->
        </slot>
      </div>
    </div>

    <!-- Footer with demo controls -->
    <div class="demo-footer">
      <slot name="footer">
        <span class="demo-indicator">
          <carbon:code class="inline"/> Live Code Demo
        </span>
      </slot>
    </div>
  </div>
</template>

<script setup>
// No specific props needed - uses slots for flexibility
</script>

<style scoped>
.code-demo-layout {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  background: #000000;
  color: #ffffff;
  padding: 2rem;
}

.demo-header {
  margin-bottom: 1.5rem;
  border-bottom: 2px solid #ff6b35;
  padding-bottom: 0.75rem;
}

.demo-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #ff6b35;
  margin: 0;
}

.demo-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  flex: 1;
  overflow: hidden;
}

.explanation {
  overflow-y: auto;
  padding-right: 1rem;
}

.explanation::-webkit-scrollbar {
  width: 6px;
}

.explanation::-webkit-scrollbar-track {
  background: #1a1a1a;
}

.explanation::-webkit-scrollbar-thumb {
  background: #ff6b35;
  border-radius: 3px;
}

.code-display {
  background: #1a1a1a;
  border: 2px solid #ff6b35;
  border-radius: 0.5rem;
  padding: 1rem;
  overflow-y: auto;
  font-family: 'Fira Code', monospace;
}

.code-display::-webkit-scrollbar {
  width: 6px;
}

.code-display::-webkit-scrollbar-track {
  background: #0a0a0a;
}

.code-display::-webkit-scrollbar-thumb {
  background: #ff9f1c;
  border-radius: 3px;
}

.demo-footer {
  margin-top: 1.5rem;
  padding-top: 0.75rem;
  border-top: 1px solid rgba(255, 107, 53, 0.3);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.demo-indicator {
  color: #ff9f1c;
  font-size: 0.9rem;
  font-weight: 600;
}

/* Responsive design */
@media (max-width: 1024px) {
  .demo-content {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .code-display {
    max-height: 400px;
  }
}
</style>
