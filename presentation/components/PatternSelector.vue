<template>
  <div class="pattern-selector">
    <div class="selector-header">
      <h3>Explore Agentic Workflow Patterns</h3>
      <p>Select a category to view patterns</p>
    </div>

    <div class="category-tabs">
      <button
        v-for="category in categories"
        :key="category.id"
        @click="selectedCategory = category.id"
        class="category-tab"
        :class="{ active: selectedCategory === category.id }"
      >
        <span class="tab-icon">{{ category.icon }}</span>
        <span class="tab-name">{{ category.name }}</span>
        <span class="tab-count">{{ category.patterns.length }}</span>
      </button>
    </div>

    <div class="patterns-grid">
      <div
        v-for="pattern in currentPatterns"
        :key="pattern.id"
        class="pattern-card"
        @click="selectPattern(pattern)"
        :class="{ selected: selectedPattern?.id === pattern.id }"
      >
        <div class="pattern-icon">{{ pattern.icon }}</div>
        <div class="pattern-name">{{ pattern.name }}</div>
        <div class="pattern-description">{{ pattern.shortDescription }}</div>
        <div class="pattern-use-case">
          <span class="use-case-label">Best for:</span>
          {{ pattern.useCase }}
        </div>
      </div>
    </div>

    <transition name="detail-slide">
      <div v-if="selectedPattern" class="pattern-detail">
        <div class="detail-header">
          <div class="detail-title">
            <span class="detail-icon">{{ selectedPattern.icon }}</span>
            <h4>{{ selectedPattern.name }}</h4>
          </div>
          <button @click="selectedPattern = null" class="close-button">
            <carbon:close />
          </button>
        </div>
        <div class="detail-content">
          <p class="detail-description">{{ selectedPattern.fullDescription }}</p>
          <div class="detail-stats">
            <div class="stat">
              <span class="stat-label">Complexity</span>
              <span class="stat-value">{{ selectedPattern.complexity }}</span>
            </div>
            <div class="stat">
              <span class="stat-label">Performance</span>
              <span class="stat-value">{{ selectedPattern.performance }}</span>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const selectedCategory = ref('core')
const selectedPattern = ref(null)

const categories = [
  {
    id: 'core',
    name: 'Core',
    icon: '🎯',
    patterns: [
      {
        id: 'reflection',
        name: 'Reflection',
        icon: '🔍',
        shortDescription: 'Self-review and improvement',
        fullDescription: 'The agent reviews its own outputs and iteratively improves them based on self-critique.',
        useCase: 'Code quality, content refinement',
        complexity: 'Low',
        performance: 'High'
      },
      {
        id: 'tool-use',
        name: 'Tool Use',
        icon: '🛠️',
        shortDescription: 'External tool integration',
        fullDescription: 'Agent calls external APIs, databases, or shell commands to gather information or execute actions.',
        useCase: 'System integration, data retrieval',
        complexity: 'Medium',
        performance: 'High'
      },
      {
        id: 'planning',
        name: 'Planning',
        icon: '📋',
        shortDescription: 'Task decomposition',
        fullDescription: 'Agent breaks down complex goals into structured sub-tasks before execution.',
        useCase: 'Complex workflows, multi-step tasks',
        complexity: 'Medium',
        performance: 'Medium'
      }
    ]
  },
  {
    id: 'workflow',
    name: 'Workflow',
    icon: '🔄',
    patterns: [
      {
        id: 'sequential',
        name: 'Sequential',
        icon: '➡️',
        shortDescription: 'Step-by-step execution',
        fullDescription: 'Tasks execute in a defined order, with each step depending on the previous completion.',
        useCase: 'Pipelines, linear workflows',
        complexity: 'Low',
        performance: 'Medium'
      },
      {
        id: 'parallel',
        name: 'Parallel',
        icon: '⚡',
        shortDescription: 'Concurrent execution',
        fullDescription: 'Multiple independent tasks run simultaneously to optimize throughput.',
        useCase: 'Batch processing, independent tasks',
        complexity: 'Medium',
        performance: 'High'
      }
    ]
  },
  {
    id: 'coordination',
    name: 'Coordination',
    icon: '🤝',
    patterns: [
      {
        id: 'multi-agent',
        name: 'Multi-Agent',
        icon: '👥',
        shortDescription: 'Collaborative execution',
        fullDescription: 'Multiple agents work together, each contributing specialized capabilities.',
        useCase: 'Complex systems, diverse expertise',
        complexity: 'High',
        performance: 'High'
      },
      {
        id: 'hierarchical',
        name: 'Hierarchical',
        icon: '🏗️',
        shortDescription: 'Parent-child relationships',
        fullDescription: 'A coordinator agent delegates sub-tasks to specialized child agents.',
        useCase: 'Task orchestration, delegation',
        complexity: 'High',
        performance: 'Medium'
      },
      {
        id: 'routing',
        name: 'Routing',
        icon: '🎯',
        shortDescription: 'Specialized delegation',
        fullDescription: 'A router agent analyzes requests and directs them to the most appropriate specialist.',
        useCase: 'Multi-domain systems, expertise routing',
        complexity: 'Medium',
        performance: 'High'
      }
    ]
  },
  {
    id: 'control',
    name: 'Control',
    icon: '🎛️',
    patterns: [
      {
        id: 'human-loop',
        name: 'Human-in-Loop',
        icon: '👤',
        shortDescription: 'Human oversight',
        fullDescription: 'Agent pauses at critical points to request human review and approval.',
        useCase: 'High-stakes decisions, compliance',
        complexity: 'Low',
        performance: 'Low (by design)'
      },
      {
        id: 'feedback',
        name: 'Feedback Loop',
        icon: '🔁',
        shortDescription: 'Iterative refinement',
        fullDescription: 'Agent observes outcomes, learns from results, and adjusts future behavior.',
        useCase: 'Continuous improvement, optimization',
        complexity: 'Medium',
        performance: 'High'
      }
    ]
  }
]

const currentPatterns = computed(() => {
  const category = categories.find(c => c.id === selectedCategory.value)
  return category ? category.patterns : []
})

const selectPattern = (pattern) => {
  selectedPattern.value = pattern
}
</script>

<style scoped>
.pattern-selector {
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 107, 53, 0.3);
  border-radius: 1rem;
  padding: 2rem;
  margin: 1rem 0;
}

.selector-header {
  text-align: center;
  margin-bottom: 2rem;
}

.selector-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #ff6b35;
  margin: 0 0 0.5rem 0;
}

.selector-header p {
  color: #cccccc;
  margin: 0;
}

.category-tabs {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  justify-content: center;
  flex-wrap: wrap;
}

.category-tab {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: rgba(255, 255, 255, 0.05);
  border: 2px solid rgba(255, 107, 53, 0.3);
  border-radius: 0.5rem;
  color: #ffffff;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 0.95rem;
  font-weight: 600;
}

.category-tab:hover {
  background: rgba(255, 107, 53, 0.1);
  border-color: #ff6b35;
}

.category-tab.active {
  background: rgba(255, 107, 53, 0.2);
  border-color: #ff6b35;
  box-shadow: 0 0 10px rgba(255, 107, 53, 0.3);
}

.tab-icon {
  font-size: 1.25rem;
}

.tab-count {
  background: #ff6b35;
  color: #000000;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.125rem 0.5rem;
  border-radius: 0.25rem;
}

.patterns-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.pattern-card {
  background: rgba(255, 255, 255, 0.05);
  border: 2px solid rgba(255, 107, 53, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s;
}

.pattern-card:hover {
  background: rgba(255, 107, 53, 0.1);
  border-color: #ff6b35;
  transform: translateY(-2px);
}

.pattern-card.selected {
  border-color: #ff9f1c;
  background: rgba(255, 159, 28, 0.15);
}

.pattern-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  text-align: center;
}

.pattern-name {
  font-size: 1.125rem;
  font-weight: 700;
  color: #ff6b35;
  margin-bottom: 0.5rem;
  text-align: center;
}

.pattern-description {
  font-size: 0.9rem;
  color: #cccccc;
  margin-bottom: 1rem;
  text-align: center;
}

.pattern-use-case {
  font-size: 0.85rem;
  color: #aaaaaa;
  text-align: center;
  padding-top: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.use-case-label {
  font-weight: 600;
  color: #ff9f1c;
  display: block;
  margin-bottom: 0.25rem;
}

.pattern-detail {
  background: rgba(255, 107, 53, 0.1);
  border: 2px solid #ff6b35;
  border-radius: 0.75rem;
  padding: 1.5rem;
  margin-top: 2rem;
}

.detail-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.detail-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.detail-icon {
  font-size: 2rem;
}

.detail-title h4 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #ff6b35;
  margin: 0;
}

.close-button {
  background: transparent;
  border: none;
  color: #ff6b35;
  cursor: pointer;
  font-size: 1.5rem;
  padding: 0.25rem;
  transition: color 0.2s;
}

.close-button:hover {
  color: #ff9f1c;
}

.detail-content {
  color: #ffffff;
}

.detail-description {
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.detail-stats {
  display: flex;
  gap: 2rem;
}

.stat {
  flex: 1;
  background: rgba(0, 0, 0, 0.3);
  padding: 1rem;
  border-radius: 0.5rem;
  text-align: center;
}

.stat-label {
  display: block;
  font-size: 0.85rem;
  color: #cccccc;
  margin-bottom: 0.5rem;
}

.stat-value {
  display: block;
  font-size: 1.125rem;
  font-weight: 700;
  color: #ff9f1c;
}

.detail-slide-enter-active,
.detail-slide-leave-active {
  transition: all 0.3s ease;
}

.detail-slide-enter-from,
.detail-slide-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
</style>
