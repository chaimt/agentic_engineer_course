<template>
  <div class="slidev-layout pattern-slide-layout" :class="$attrs.class">
    <div class="pattern-header">
      <slot name="pattern-name" />
    </div>
    <div class="pattern-content grid grid-cols-2 gap-8">
      <div class="pattern-description">
        <slot name="description" />
      </div>
      <div class="pattern-example">
        <slot name="example" />
      </div>
    </div>
    <div class="pattern-footer">
      <slot name="footer" />
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.pattern-slide-layout {
  @apply h-full w-full p-12 flex flex-col;
  background: var(--slidev-theme-background, #1e293b);
  color: var(--slidev-theme-text, #e2e8f0);
}

.pattern-header {
  @apply mb-8;
}

.pattern-header :deep(h1) {
  @apply text-4xl font-bold mb-2;
  color: var(--slidev-theme-heading, #f1f5f9);
}

.pattern-header :deep(h2) {
  @apply text-2xl font-semibold;
  color: var(--slidev-theme-primary, #3b82f6);
}

.pattern-header :deep(.pattern-tag) {
  @apply inline-block px-3 py-1 rounded text-sm font-semibold mt-2;
  background: var(--slidev-theme-accent, #06b6d4);
  color: var(--slidev-theme-background, #1e293b);
}

.pattern-content {
  @apply flex-1 overflow-hidden;
}

.pattern-description {
  @apply flex flex-col justify-start;
}

.pattern-description :deep(h3) {
  @apply text-xl font-semibold mb-3;
  color: var(--slidev-theme-secondary, #8b5cf6);
}

.pattern-description :deep(ul) {
  @apply list-disc pl-6 space-y-2;
}

.pattern-description :deep(li) {
  @apply text-base leading-relaxed;
}

.pattern-description :deep(p) {
  @apply text-base leading-relaxed mb-3;
}

.pattern-example {
  @apply flex flex-col;
}

.pattern-example :deep(pre) {
  @apply rounded-lg p-4 overflow-auto flex-1;
  background: var(--slidev-code-background, #0f172a);
  border: 1px solid var(--slidev-code-border, #334155);
  font-size: 0.85rem;
  line-height: 1.5;
}

.pattern-example :deep(img) {
  @apply rounded-lg w-full h-auto object-contain;
  border: 1px solid var(--slidev-code-border, #334155);
}

.pattern-footer {
  @apply mt-6 pt-4 border-t;
  border-color: var(--slidev-code-border, #334155);
}

.pattern-footer :deep(.pattern-characteristics) {
  @apply flex flex-wrap gap-2;
}

.pattern-footer :deep(.characteristic-badge) {
  @apply px-3 py-1 rounded text-sm;
  background: rgba(59, 130, 246, 0.1);
  color: var(--slidev-theme-primary, #3b82f6);
  border: 1px solid var(--slidev-theme-primary, #3b82f6);
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .pattern-content {
    @apply grid-cols-1;
  }

  .pattern-example :deep(pre) {
    @apply max-h-64;
  }
}
</style>
