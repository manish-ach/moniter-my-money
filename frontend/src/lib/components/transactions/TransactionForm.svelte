<script lang="ts">
	import { untrack } from 'svelte';
	import Button from '$lib/components/ui/Button.svelte';
	import Input from '$lib/components/ui/Input.svelte';
	import Select from '$lib/components/ui/Select.svelte';
	import type { Transaction } from '$lib/types/transaction';

	interface Props {
		transaction?: Transaction | null;
		onsubmit: (data: Omit<Transaction, 'id' | 'created_at' | 'updated_at'>) => void;
		oncancel: () => void;
	}

	let { transaction = null, onsubmit, oncancel }: Props = $props();

	let amount = $state('');
	let transaction_type = $state('');
	let category = $state('');
	let description = $state('');
	let date = $state(new Date().toISOString().split('T')[0]);

	$effect(() => {
		if (transaction) {
			untrack(() => {
				amount = transaction.amount;
				transaction_type = transaction.transaction_type;
				category = transaction.category;
				description = transaction.description;
				date = transaction.date;
			});
		}
	});

	const typeOptions = [
		{ value: 'income', label: 'Income' },
		{ value: 'expense', label: 'Expense' }
	];

	const categoryOptions = [
		{ value: 'salary', label: 'Salary' },
		{ value: 'freelance', label: 'Freelance' },
		{ value: 'investments', label: 'Investments' },
		{ value: 'other_income', label: 'Other Income' },
		{ value: 'food', label: 'Food & Dining' },
		{ value: 'transportation', label: 'Transportation' },
		{ value: 'utilities', label: 'Utilities' },
		{ value: 'rent', label: 'Rent/Mortgage' },
		{ value: 'entertainment', label: 'Entertainment' },
		{ value: 'shopping', label: 'Shopping' },
		{ value: 'healthcare', label: 'Healthcare' },
		{ value: 'education', label: 'Education' },
		{ value: 'other_expense', label: 'Other Expense' }
	];

	const handleSubmit = (e: SubmitEvent) => {
		e.preventDefault();
		onsubmit({
			amount,
			transaction_type: transaction_type as 'income' | 'expense',
			category: category as Transaction['category'],
			description,
			date
		});
	};
</script>

<form onsubmit={handleSubmit}>
	<div class="form-grid">
		<Input label="Amount" type="amount" bind:value={amount} required placeholder="0.00" />
		<Input label="Date" type="datetext" bind:value={date} required />

		<Select
			label="Type"
			options={typeOptions}
			bind:value={transaction_type}
			required
			placeholder="Select type"
		/>

		<Select
			label="Category"
			options={categoryOptions}
			bind:value={category}
			required
			placeholder="Select category"
		/>
	</div>

	<div class="mt-md">
		<Input label="Description" type="text" bind:value={description} placeholder="Optional notes" />
	</div>

	<div class="actions">
		<Button variant="ghost" onclick={oncancel}>Cancel</Button>
		<Button type="submit">{transaction ? 'Update' : 'Add'} Transaction</Button>
	</div>
</form>

<style>
	.form-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: var(--spacing-md);
	}

	.actions {
		display: flex;
		justify-content: flex-end;
		gap: var(--spacing-md);
		margin-top: var(--spacing-lg);
		padding-top: var(--spacing-lg);
		border-top: 1px solid var(--color-border);
	}
</style>
