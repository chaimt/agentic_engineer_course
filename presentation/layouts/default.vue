<template>
  <div class="slidev-layout default-layout" :class="$attrs.class">
    <div class="slide-content">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.default-layout {
  @apply h-full w-full p-12;
  background: var(--slidev-theme-background, #1e293b);
  color: var(--slidev-theme-text, #e2e8f0);
}

.slide-content {
  @apply h-full flex flex-col;
}

/* Typography overrides */
.default-layout :deep(h1) {
  @apply text-5xl font-bold mb-6;
  color: var(--slidev-theme-heading, #f1f5f9);
}

.default-layout :deep(h2) {
  @apply text-3xl font-semibold mb-4;
  color: var(--slidev-theme-primary, #3b82f6);
}

.default-layout :deep(h3) {
  @apply text-2xl font-semibold mb-3;
  color: var(--slidev-theme-secondary, #8b5cf6);
}

.default-layout :deep(p) {
  @apply text-lg leading-relaxed mb-4;
}

.default-layout :deep(ul) {
  @apply list-disc pl-8 space-y-2;
}

.default-layout :deep(li) {
  @apply text-lg;
}

.default-layout :deep(code) {
  @apply bg-slate-800 px-2 py-1 rounded text-sm;
  font-family: 'Fira Code', monospace;
}

.default-layout :deep(pre) {
  @apply rounded-lg p-4 my-4 overflow-x-auto;
  background: var(--slidev-code-background, #0f172a);
  border: 1px solid var(--slidev-code-border, #334155);
}

.default-layout :deep(a) {
  @apply underline;
  color: var(--slidev-theme-accent, #06b6d4);
}

.default-layout :deep(a:hover) {
  @apply opacity-80;
}

.default-layout :deep(strong) {
  @apply font-semibold;
  color: var(--slidev-theme-accent, #06b6d4);
}

.default-layout :deep(em) {
  @apply italic;
  color: var(--slidev-theme-primary, #3b82f6);
}
</style>
