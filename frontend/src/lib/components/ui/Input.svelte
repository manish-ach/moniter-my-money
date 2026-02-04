<script lang="ts">
	interface Props {
		label?: string;
		type?: 'text' | 'number' | 'date' | 'email' | 'password' | 'amount' | 'datetext';
		placeholder?: string;
		value?: string | number;
		required?: boolean;
		error?: string;
		oninput?: (e: Event) => void;
	}

	let {
		label,
		type = 'text',
		placeholder = '',
		value = $bindable(''),
		required = false,
		error,
		oninput
	}: Props = $props();

	// unique ID for label association (for a11y)[screenreaders]
	const inputId = `input-${Math.random().toString(36).slice(2, 11)}`;

	const handleAmountInput = (e: Event) => {
		const input = e.target as HTMLInputElement;
		let val = input.value;

		// remove non digit or . characters
		val = val.replace(/[^\d.]/g, '');

		// ensure only one decimal point
		const parts = val.split('.');
		if (parts.length > 2) {
			val = parts[0] + '.' + parts.slice(1).join('');
		}

		input.value = val;
		value = val;
		oninput?.(e);
	};

	const handleDateTextInput = (e: Event) => {
		const input = e.target as HTMLInputElement;
		let val = input.value;

		// remove non-digit character
		val = val.replace(/\D/g, '');

		// auto insert dashes: YYYY-MM-DD
		if (val.length > 4) {
			val = val.slice(0, 4) + '-' + val.slice(4);
		}
		if (val.length > 7) {
			val = val.slice(0, 7) + '-' + val.slice(7);
		}

		// Limit to 10 characters (YYYY-MM-DD)
		val = val.slice(0, 10);

		input.value = val;
		value = val;
		oninput?.(e);
	};

	const getInputType = () => {
		if (type === 'amount' || type === 'datetext') return 'text';
		return type;
	};

	const getInputMode = () => {
		if (type === 'amount') return 'decimal';
		if (type === 'datetext') return 'numeric';
		return undefined;
	};

	const handleInput = (e: Event) => {
		if (type === 'amount') {
			handleAmountInput(e);
		} else if (type === 'datetext') {
			handleDateTextInput(e);
		} else {
			oninput?.(e);
		}
	};
</script>

<div class="input-group">
	{#if label}
		<label for={inputId}>
			{label}{#if required}<span class="required">*</span>{/if}
		</label>
	{/if}
	<input
		id={inputId}
		type={getInputType()}
		inputmode={getInputMode()}
		{placeholder}
		bind:value
		{required}
		oninput={handleInput}
		class:has-error={error}
		aria-invalid={error ? 'true' : 'false'}
		aria-describedby={error ? '${inputId}-error' : undefined}
	/>
	{#if error}
		<span class="error">{error}</span>
	{/if}
</div>

<style>
	.input-group {
		display: flex;
		flex-direction: column;
		gap: 0.25rem;
	}

	label {
		font-size: 0.875rem;
		font-weight: 500;
		color: var(--color-text);
	}

	.required {
		color: var(--color-danger);
	}

	input {
		padding: 0.5rem 0.75rem;
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
		font-size: 1rem;
		transition: border-color 0.15s ease;
	}

	input:focus {
		outline: none;
		border-color: var(--color-primary);
	}

	input.has-error {
		border-color: var(--color-danger);
	}

	.error {
		font-size: 0.75rem;
		color: var(--color-danger);
	}
</style>
