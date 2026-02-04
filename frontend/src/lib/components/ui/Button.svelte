<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		variant?: 'primary' | 'secondary' | 'danger' | 'ghost';
		size?: 'sm' | 'md' | 'lg';
		disabled?: boolean;
		type?: 'button' | 'submit';
		onclick?: () => void;
		children: Snippet;
	}

	let {
		variant = 'primary',
		size = 'md',
		disabled = false,
		type = 'button',
		onclick,
		children
	}: Props = $props();
</script>

<button class="btn {variant} {size}" {disabled} {type} {onclick}>
	{@render children()}
</button>

<style>
	.btn {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		gap: 0.5rem;
		border: none;
		border-radius: var(--radius-md);
		font-weight: 500;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.btn:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	/* Sizes */
	.sm {
		padding: 0.375rem 0.75rem;
		font-size: 0.875rem;
	}
	.md {
		padding: 0.5rem 1rem;
		font-size: 1rem;
	}
	.lg {
		padding: 0.75rem 1.5rem;
		font-size: 1.125rem;
	}

	/* Variants */
	.primary {
		background: var(--color-primary);
		color: white;
	}
	.primary:hover:not(:disabled) {
		background: var(--color-primary-hover);
	}

	.secondary {
		background: var(--color-border);
		color: var(--color-text);
	}
	.secondary:hover:not(:disabled) {
		background: #cbd5e1;
	}

	.danger {
		background: var(--color-danger);
		color: white;
	}
	.danger:hover:not(:disabled) {
		background: #dc2626;
	}

	.ghost {
		background: transparent;
		color: var(--color-text);
	}
	.ghost:hover:not(:disabled) {
		background: var(--color-border);
	}
</style>
