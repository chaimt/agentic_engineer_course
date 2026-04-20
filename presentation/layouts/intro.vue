<template>
  <div class="slidev-layout intro-layout" :class="$attrs.class">
    <div class="intro-content">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.intro-layout {
  @apply h-full w-full flex items-center justify-center p-16;
  background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
  color: var(--slidev-theme-text, #e2e8f0);
}

.intro-content {
  @apply text-center max-w-4xl;
}

.intro-layout :deep(h1) {
  @apply text-6xl md:text-7xl font-bold mb-8;
  color: var(--slidev-theme-heading, #f1f5f9);
  text-shadow: 0 2px 20px rgba(59, 130, 246, 0.3);
}

.intro-layout :deep(h2) {
  @apply text-3xl md:text-4xl font-medium mb-6;
  color: var(--slidev-theme-primary, #3b82f6);
}

.intro-layout :deep(p) {
  @apply text-xl md:text-2xl leading-relaxed mb-6;
  color: var(--slidev-theme-text-muted, #94a3b8);
}

.intro-layout :deep(.subtitle) {
  @apply text-2xl font-light mt-4;
  color: var(--slidev-theme-text-muted, #94a3b8);
}

.intro-layout :deep(.author) {
  @apply text-lg mt-8;
  color: var(--slidev-theme-text-muted, #94a3b8);
}

.intro-layout :deep(.date) {
  @apply text-base mt-2;
  color: var(--slidev-theme-text-muted, #94a3b8);
}

/* Animated gradient accent */
.intro-layout::before {
  content: '';
  @apply absolute top-0 left-0 w-full h-2;
  background: linear-gradient(90deg,
    var(--slidev-theme-primary, #3b82f6) 0%,
    var(--slidev-theme-secondary, #8b5cf6) 50%,
    var(--slidev-theme-accent, #06b6d4) 100%
  );
}
</style>
