<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		padding?: 'sm' | 'md' | 'lg' | 'none';
		shadow?: boolean;
		children: Snippet;
	}

	let { padding = 'lg', shadow = true, children }: Props = $props();
</script>

<div class="card padding-{padding}" class:shadow>
	{@render children()}
</div>

<style>
	.card {
		background: var(--color-surface);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
	}

	.shadow {
		box-shadow: var(--shadow-sm);
	}

	.padding-none {
		padding: 0;
	}

	.padding-sm {
		padding: var(--spacing-sm);
	}

	.padding-md {
		padding: var(--spacing-md);
	}

	.padding-lg {
		padding: var(--spacing-lg);
	}
</style>
