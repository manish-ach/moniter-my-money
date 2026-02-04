<script lang="ts">
	interface Option {
		value: string;
		label: string;
	}

	interface Props {
		label?: string;
		options: Option[];
		value?: string;
		required?: boolean;
		placeholder?: string;
	}

	let {
		label,
		options,
		value = $bindable(''),
		required = false,
		placeholder = 'Select an option'
	}: Props = $props();

	// unique ID for label association (for a11y)[screenreaders]
	const selectID = `select-${Math.random().toString(36).slice(2, 11)}`;
</script>

<div class="select-group">
	{#if label}
		<label for={selectID}>
			{label}
			{#if required}
				<span class="required">*</span>
			{/if}
		</label>
	{/if}
	<select id={selectID} bind:value {required}>
		<option value="" disabled>{placeholder}</option>
		{#each options as opt}
			<option value={opt.value}>{opt.label}</option>
		{/each}
	</select>
</div>

<style>
	.select-group {
		display: flex;
		flex-direction: column;
		gap: 0.25rem;
	}

	label {
		font-size: 0.875rem;
		font-weight: 500;
	}

	.required {
		color: var(--color-danger);
	}

	select {
		padding: 0.5rem 0.75rem;
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
		font-size: 1rem;
		background: white;
		cursor: pointer;
	}

	select:focus {
		outline: none;
		border-color: var(--color-primary);
	}
</style>
