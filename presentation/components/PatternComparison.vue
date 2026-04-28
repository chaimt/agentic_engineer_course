<template>
  <div class="pattern-comparison">
    <div class="pattern-card" v-for="pattern in patterns" :key="pattern.name">
      <div class="pattern-header">
        <h3>{{ pattern.name }}</h3>
        <span class="pattern-type" :class="pattern.type">{{ pattern.type }}</span>
      </div>

      <div class="pattern-body">
        <div class="section">
          <h4>Use Cases</h4>
          <ul>
            <li v-for="useCase in pattern.useCases" :key="useCase">{{ useCase }}</li>
          </ul>
        </div>

        <div class="section" v-if="pattern.benefits">
          <h4>Benefits</h4>
          <ul>
            <li v-for="benefit in pattern.benefits" :key="benefit">{{ benefit }}</li>
          </ul>
        </div>

        <div class="section" v-if="pattern.metrics">
          <h4>Performance</h4>
          <div class="metrics">
            <span v-for="(value, key) in pattern.metrics" :key="key" class="metric">
              <strong>{{ key }}:</strong> {{ value }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface PatternMetrics {
  [key: string]: string
}

interface Pattern {
  name: string
  type: 'workflow' | 'agentic' | 'architecture'
  useCases: string[]
  benefits?: string[]
  metrics?: PatternMetrics
}

defineProps<{
  patterns: Pattern[]
}>()
</script>

<style scoped>
.pattern-comparison {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  padding: 1rem;
}

.pattern-card {
  background: var(--slidev-theme-background-alt, #0a0a0a);
  border: 2px solid var(--slidev-theme-primary, #F47721);
  border-radius: 0.5rem;
  padding: 1.5rem;
  transition: transform 0.2s, box-shadow 0.2s;
}

.pattern-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(244, 119, 33, 0.3);
}

.pattern-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid var(--slidev-theme-primary, #F47721);
}

.pattern-header h3 {
  margin: 0;
  font-size: 1.25rem;
  color: var(--slidev-theme-primary, #F47721);
}

.pattern-type {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

.pattern-type.workflow {
  background: rgba(255, 154, 60, 0.2);
  color: #FF9A3C;
}

.pattern-type.agentic {
  background: rgba(244, 119, 33, 0.2);
  color: #F47721;
}

.pattern-type.architecture {
  background: rgba(193, 52, 41, 0.2);
  color: #C13429;
}

.pattern-body {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.section h4 {
  margin: 0 0 0.5rem 0;
  font-size: 0.95rem;
  color: var(--slidev-theme-secondary, #FF9A3C);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.section ul {
  margin: 0;
  padding-left: 1.25rem;
  list-style-type: disc;
}

.section li {
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--slidev-theme-text, #ffffff);
  margin-bottom: 0.25rem;
}

.metrics {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.metric {
  font-size: 0.9rem;
  color: var(--slidev-theme-text, #ffffff);
}

.metric strong {
  color: var(--slidev-theme-accent, #F47721);
}
</style>
