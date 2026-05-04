<script setup lang="ts">
import { computed } from 'vue'
import { useNav } from '@slidev/client'

const { currentPage, slides } = useNav()

const sections = computed(() =>
  slides.value
    .filter(s => s.meta?.slide?.frontmatter?.sectionTitle)
    .map(s => ({
      no: s.no,
      title: s.meta.slide.frontmatter.sectionTitle as string,
    }))
)

const currentSectionIndex = computed(() => {
  let idx = -1
  for (let i = 0; i < sections.value.length; i++) {
    if (currentPage.value >= sections.value[i].no) idx = i
  }
  return idx
})

const isVisible = computed(() => currentPage.value > 2 && sections.value.length > 0)
</script>

<template>
  <div v-if="isVisible" class="section-progress">
    <div
      v-for="(section, i) in sections"
      :key="section.no"
      class="section-item"
      :class="{
        active: i === currentSectionIndex,
        past: i < currentSectionIndex,
      }"
    >
      <span class="section-label">{{ section.title }}</span>
    </div>
  </div>
</template>

<style scoped>
.section-progress {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  height: 32px;
  z-index: 100;
  background: rgba(0, 0, 0, 0.88);
  border-bottom: 1px solid #1a1a1a;
}

.section-item {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  border-right: 1px solid #1a1a1a;
  transition: background 0.25s;
}

.section-item:last-child {
  border-right: none;
}

.section-item::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: transparent;
  transition: background 0.25s;
}

.section-item.past::after {
  background: #555;
}

.section-item.active {
  background: rgba(244, 119, 33, 0.08);
}

.section-item.active::after {
  background: #F47721;
}

.section-label {
  font-size: 9px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #444;
  transition: color 0.25s;
  font-family: 'Roboto', sans-serif;
}

.section-item.past .section-label {
  color: #777;
}

.section-item.active .section-label {
  color: #F47721;
}
</style>
