<template>
  <div class="slidev-layout section-header-layout" :class="$attrs.class">
    <div class="section-header-content">
      <div class="section-indicator">
        <slot name="section-number">Section</slot>
      </div>
      <div class="section-title">
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.section-header-layout {
  @apply h-full w-full flex items-center justify-center p-16;
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
  color: var(--slidev-theme-text, #e2e8f0);
  position: relative;
}

.section-header-content {
  @apply text-center max-w-4xl;
}

.section-indicator {
  @apply text-sm uppercase tracking-widest font-semibold mb-6;
  color: var(--slidev-theme-accent, #06b6d4);
}

.section-header-layout :deep(h1) {
  @apply text-5xl md:text-6xl font-bold mb-6;
  color: var(--slidev-theme-heading, #f1f5f9);
  line-height: 1.2;
}

.section-header-layout :deep(h2) {
  @apply text-3xl md:text-4xl font-semibold mb-4;
  color: var(--slidev-theme-primary, #3b82f6);
}

.section-header-layout :deep(p) {
  @apply text-xl md:text-2xl leading-relaxed;
  color: var(--slidev-theme-text-muted, #94a3b8);
}

/* Decorative accent line */
.section-header-layout::after {
  content: '';
  @apply absolute bottom-16 left-1/2 transform -translate-x-1/2 w-32 h-1 rounded-full;
  background: linear-gradient(90deg,
    var(--slidev-theme-primary, #3b82f6) 0%,
    var(--slidev-theme-accent, #06b6d4) 100%
  );
}

/* Animated background accent */
.section-header-layout::before {
  content: '';
  @apply absolute inset-0 opacity-10;
  background: radial-gradient(circle at center,
    var(--slidev-theme-primary, #3b82f6) 0%,
    transparent 70%
  );
}
</style>
