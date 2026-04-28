<template>
  <div class="architecture-diagram">
    <div class="diagram-title" v-if="title">
      <h3>{{ title }}</h3>
      <span v-if="subtitle" class="subtitle">{{ subtitle }}</span>
    </div>

    <div class="diagram-container">
      <!-- SVG-based architecture visualization -->
      <svg
        :viewBox="`0 0 ${width} ${height}`"
        :width="width"
        :height="height"
        class="diagram-svg"
      >
        <!-- Connections/Arrows -->
        <g class="connections">
          <path
            v-for="(connection, index) in connections"
            :key="`conn-${index}`"
            :d="connection.path"
            :class="['connection-line', connection.type]"
            :marker-end="`url(#arrow-${connection.type || 'default'})`"
          />
        </g>

        <!-- Nodes/Components -->
        <g class="nodes">
          <g
            v-for="node in nodes"
            :key="node.id"
            :transform="`translate(${node.x}, ${node.y})`"
            class="node"
            :class="node.type"
          >
            <rect
              :width="node.width || 120"
              :height="node.height || 60"
              :rx="8"
              class="node-box"
            />
            <text
              :x="(node.width || 120) / 2"
              :y="(node.height || 60) / 2"
              text-anchor="middle"
              dominant-baseline="middle"
              class="node-label"
            >
              {{ node.label }}
            </text>
            <text
              v-if="node.sublabel"
              :x="(node.width || 120) / 2"
              :y="(node.height || 60) / 2 + 15"
              text-anchor="middle"
              class="node-sublabel"
            >
              {{ node.sublabel }}
            </text>
          </g>
        </g>

        <!-- Arrow markers -->
        <defs>
          <marker
            id="arrow-default"
            markerWidth="10"
            markerHeight="10"
            refX="9"
            refY="3"
            orient="auto"
            markerUnits="strokeWidth"
          >
            <path d="M0,0 L0,6 L9,3 z" fill="var(--slidev-theme-primary)" />
          </marker>
          <marker
            id="arrow-data"
            markerWidth="10"
            markerHeight="10"
            refX="9"
            refY="3"
            orient="auto"
            markerUnits="strokeWidth"
          >
            <path d="M0,0 L0,6 L9,3 z" fill="var(--slidev-theme-secondary)" />
          </marker>
          <marker
            id="arrow-control"
            markerWidth="10"
            markerHeight="10"
            refX="9"
            refY="3"
            orient="auto"
            markerUnits="strokeWidth"
          >
            <path d="M0,0 L0,6 L9,3 z" fill="var(--slidev-theme-accent)" />
          </marker>
        </defs>
      </svg>
    </div>

    <div class="legend" v-if="legend">
      <div
        v-for="item in legend"
        :key="item.label"
        class="legend-item"
        :class="item.type"
      >
        <span class="legend-marker"></span>
        <span class="legend-label">{{ item.label }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Node {
  id: string
  label: string
  sublabel?: string
  x: number
  y: number
  width?: number
  height?: number
  type?: 'agent' | 'tool' | 'memory' | 'user' | 'system'
}

interface Connection {
  path: string
  type?: 'default' | 'data' | 'control'
}

interface LegendItem {
  label: string
  type: string
}

defineProps<{
  title?: string
  subtitle?: string
  width?: number
  height?: number
  nodes: Node[]
  connections?: Connection[]
  legend?: LegendItem[]
}>()
</script>

<style scoped>
.architecture-diagram {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem;
  background: var(--slidev-theme-background-alt, #0a0a0a);
  border-radius: 0.5rem;
  border: 1px solid var(--slidev-theme-primary, #F47721);
}

.diagram-title h3 {
  margin: 0 0 0.25rem 0;
  font-size: 1.5rem;
  color: var(--slidev-theme-primary, #F47721);
}

.subtitle {
  font-size: 0.9rem;
  color: var(--slidev-theme-text-muted, #cccccc);
}

.diagram-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;
}

.diagram-svg {
  max-width: 100%;
  height: auto;
}

.connection-line {
  fill: none;
  stroke-width: 2;
  stroke: var(--slidev-theme-primary, #F47721);
}

.connection-line.data {
  stroke: var(--slidev-theme-secondary, #FF9A3C);
  stroke-dasharray: 5, 5;
}

.connection-line.control {
  stroke: var(--slidev-theme-accent, #F47721);
  stroke-width: 3;
}

.node-box {
  fill: var(--slidev-theme-background, #000000);
  stroke: var(--slidev-theme-primary, #F47721);
  stroke-width: 2;
}

.node.agent .node-box {
  fill: rgba(244, 119, 33, 0.1);
  stroke: var(--slidev-theme-primary, #F47721);
}

.node.tool .node-box {
  fill: rgba(255, 154, 60, 0.1);
  stroke: var(--slidev-theme-secondary, #FF9A3C);
}

.node.memory .node-box {
  fill: rgba(193, 52, 41, 0.1);
  stroke: var(--slidev-theme-tertiary, #C13429);
}

.node.user .node-box {
  fill: rgba(255, 255, 255, 0.05);
  stroke: var(--slidev-theme-text-muted, #cccccc);
}

.node-label {
  fill: var(--slidev-theme-text, #ffffff);
  font-size: 14px;
  font-weight: 600;
}

.node-sublabel {
  fill: var(--slidev-theme-text-muted, #cccccc);
  font-size: 11px;
}

.legend {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  padding-top: 1rem;
  border-top: 1px solid rgba(244, 119, 33, 0.3);
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  color: var(--slidev-theme-text, #ffffff);
}

.legend-marker {
  width: 20px;
  height: 12px;
  border-radius: 2px;
  border: 2px solid var(--slidev-theme-primary, #F47721);
}

.legend-item.agent .legend-marker {
  background: rgba(244, 119, 33, 0.2);
  border-color: var(--slidev-theme-primary, #F47721);
}

.legend-item.tool .legend-marker {
  background: rgba(255, 154, 60, 0.2);
  border-color: var(--slidev-theme-secondary, #FF9A3C);
}

.legend-item.memory .legend-marker {
  background: rgba(193, 52, 41, 0.2);
  border-color: var(--slidev-theme-tertiary, #C13429);
}
</style>
