<template>
  <div class="llm-agent-comparison">
    <div class="comparison-container">
      <div class="side llm-side">
        <div class="header">
          <h3>💬 LLM</h3>
          <p>Language Model</p>
        </div>
        <div class="content">
          <div class="feature" v-for="(feature, index) in llmFeatures" :key="index">
            <span class="icon">{{ feature.icon }}</span>
            <span class="text">{{ feature.text }}</span>
          </div>
        </div>
      </div>

      <div class="divider">
        <div class="arrow">→</div>
      </div>

      <div class="side agent-side">
        <div class="header">
          <h3>🤖 Agent</h3>
          <p>AI Agent</p>
        </div>
        <div class="content">
          <div class="feature" v-for="(feature, index) in agentFeatures" :key="index">
            <span class="icon">{{ feature.icon }}</span>
            <span class="text">{{ feature.text }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const llmFeatures = ref([
  { icon: '📝', text: 'Reactive - responds to prompts' },
  { icon: '🔄', text: 'Stateless - no memory' },
  { icon: '💬', text: 'Suggests - provides advice' },
  { icon: '🚫', text: 'Read-only - cannot modify' },
  { icon: '🎯', text: 'Single-turn - one Q&A' }
])

const agentFeatures = ref([
  { icon: '🤖', text: 'Proactive - executes goals' },
  { icon: '🧠', text: 'Stateful - maintains context' },
  { icon: '⚡', text: 'Acts - executes commands' },
  { icon: '✏️', text: 'Read-write - modifies systems' },
  { icon: '🔁', text: 'Multi-turn - workflows' }
])
</script>

<style scoped>
.llm-agent-comparison {
  width: 100%;
  padding: 2rem 0;
}

.comparison-container {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 2rem;
  align-items: stretch;
}

.side {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 1rem;
  padding: 1.5rem;
  border: 2px solid;
}

.llm-side {
  border-color: #60a5fa;
}

.agent-side {
  border-color: #ff6b35;
}

.header {
  text-align: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
  color: #ffffff;
}

.header p {
  font-size: 0.9rem;
  color: #cccccc;
  margin: 0.25rem 0 0 0;
}

.content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.feature {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 0.5rem;
}

.feature .icon {
  font-size: 1.25rem;
  flex-shrink: 0;
}

.feature .text {
  font-size: 0.95rem;
  color: #ffffff;
}

.divider {
  display: flex;
  align-items: center;
  justify-content: center;
}

.arrow {
  font-size: 3rem;
  color: #ff9f1c;
  font-weight: bold;
}

@media (max-width: 768px) {
  .comparison-container {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .divider {
    display: none;
  }
}
</style>
