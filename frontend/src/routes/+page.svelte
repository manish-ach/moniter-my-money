<script lang="ts">
	import { onMount } from 'svelte';
	import { resolve } from '$app/paths';
	import { getTransactions } from '$lib/api/budget';
	import type { Transaction } from '$lib/types/transaction';
	import Card from '$lib/components/ui/Card.svelte';

	let transactions: Transaction[] = $state([]);
	let loading = $state(true);

	let totalIncome = $derived(
		transactions
			.filter((t) => t.transaction_type === 'income')
			.reduce((sum, t) => sum + parseFloat(t.amount), 0)
	);

	let totalExpense = $derived(
		transactions
			.filter((t) => t.transaction_type === 'expense')
			.reduce((sum, t) => sum + parseFloat(t.amount), 0)
	);

	let balance = $derived(totalIncome - totalExpense);
	let recentTransactions = $derived(transactions.slice(0, 5));

	onMount(async () => {
		try {
			transactions = await getTransactions();
		} finally {
			loading = false;
		}
	});

	const formatCategory = (category: string): string =>
		category.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());
</script>

<h1>Dashboard</h1>
{#if loading}
	<p>Loading...</p>
{:else}
	<div class="stats-grid">
		<!-- <div class="card stat-card">
			<span class="stat-label">Total Balance</span>
			<span class="stat-value" class:text-success={balance >= 0} class:text-danger={balance < 0}
				>${balance.toFixed(2)}</span
			>
		</div>
		<div class="card stat-card">
			<span class="stat-label">Income</span>
			<span class="stat-value text-success">+${totalIncome.toFixed(2)}</span>
		</div>
	 -->

		<Card>
			<span class="stat-label">Total Balance</span>
			<span class="stat-value" class:text-success={balance >= 0} class:text-danger={balance < 0}>
				${balance.toFixed(2)}
			</span>
		</Card>

		<Card>
			<span class="stat-label">Income</span>
			<span class="stat-value text-success">+${totalIncome.toFixed(2)}</span>
		</Card>
	</div>

	<div class="mt-lg">
		<div class="section-header">
			<h2>Recent Transactions</h2>
			<a href={resolve('/transactions')}>View all →</a>
		</div>

		{#if recentTransactions.length === 0}
			<Card>
				<p class="text-muted">
					No transactions yet. <a href={resolve('/transactions')}>Add one!</a>
				</p>
			</Card>
		{:else}
			<Card>
				{#each recentTransactions as t (t.id)}
					<div class="transaction-row">
						<div>
							<strong>{formatCategory(t.category)}</strong>
							<span class="text-muted">{t.date}</span>
						</div>
						<span class={t.transaction_type === 'income' ? 'text-success' : 'text-danger'}>
							{t.transaction_type === 'income' ? '+' : '-'}${t.amount}
						</span>
					</div>
				{/each}
			</Card>
		{/if}
	</div>
{/if}

<style>
	.stats-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: var(--spacing-md);
		margin-top: var(--spacing-lg);
	}

	.stat-label {
		display: block;
		font-size: 0.875rem;
		color: var(--color-text-muted);
		margin-bottom: var(--spacing-xs);
	}

	.stat-value {
		font-size: 1.75rem;
		font-weight: 700;
	}

	.section-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: var(--spacing-md);
	}

	.section-header h2 {
		font-size: 1.25rem;
	}

	.transaction-row {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: var(--spacing-sm) 0;
		border-bottom: 1px solid var(--color-border);
	}

	.transaction-row:last-child {
		border-bottom: none;
	}

	.transaction-row div {
		display: flex;
		flex-direction: column;
		gap: 0.125rem;
	}
</style>
