<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		open: boolean;
		title: string;
		onclose: () => void;
		children: Snippet;
	}

	let { open = $bindable(false), title, onclose, children }: Props = $props();

	const handleKeydown = (e: KeyboardEvent) => {
		if (e.key === 'Escape') onclose();
	};
</script>

<svelte:window onkeydown={handleKeydown} />

{#if open}
	<!-- svelte-ignore a11y_click_events_have_key_events -->
	<div class="overlay" onclick={onclose} role="button" tabindex="-1"></div>
	<div class="modal" role="dialog" aria-modal="true">
		<div class="header">
			<h2>{title}</h2>
			<button class="close-btn" onclick={onclose}>✕</button>
		</div>
		<div class="content">
			{@render children()}
		</div>
	</div>
{/if}

<style>
	.overlay {
		position: fixed;
		inset: 0;
		background: rgba(0, 0, 0, 0.5);
		z-index: 100;
	}

	.modal {
		position: fixed;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		background: var(--color-surface);
		border-radius: var(--radius-lg);
		box-shadow: var(--shadow-md);
		z-index: 101;
		min-width: 400px;
		max-width: 90vw;
		max-height: 90vh;
		overflow: auto;
	}

	.header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: var(--spacing-md) var(--spacing-lg);
		border-bottom: 1px solid var(--color-border);
	}

	h2 {
		font-size: 1.25rem;
	}

	.close-btn {
		background: none;
		border: none;
		font-size: 1.25rem;
		cursor: pointer;
		color: var(--color-text-muted);
	}

	.content {
		padding: var(--spacing-lg);
	}
</style>
