<script lang="ts">
	import { onMount } from 'svelte';
	import { getTransactions, createTransaction, deleteTransaction } from '$lib/api/budget';
	import type { Transaction } from '$lib/types/transaction';
	import Button from '$lib/components/ui/Button.svelte';
	import Modal from '$lib/components/ui/Modal.svelte';
	import TransactionForm from '$lib/components/transactions/TransactionForm.svelte';
	import Card from '$lib/components/ui/Card.svelte';

	let transactions: Transaction[] = $state([]);
	let loading = $state(true);
	let error: string | null = $state(null);
	let showModal = $state(false);
	let showDeleteConfirm = $state(false);
	let deleteTargetId: number | null = $state(null);

	onMount(loadTransactions);

	const promptDelete = (id: number) => {
		deleteTargetId = id;
		showDeleteConfirm = true;
	};

	async function loadTransactions() {
		try {
			loading = true;
			transactions = await getTransactions();
		} catch (e) {
			error = e instanceof Error ? e.message : 'Unknown error';
		} finally {
			loading = false;
		}
	}

	async function handleCreate(data: Omit<Transaction, 'id' | 'created_at' | 'updated_at'>) {
		try {
			await createTransaction(data);
			showModal = false;
			await loadTransactions();
		} catch (e) {
			alert('Failed to create transaction');
		}
	}

	async function handleDelete(id: number) {
		if (deleteTargetId === null) return;
		try {
			await deleteTransaction(deleteTargetId);
			showDeleteConfirm = false;
			deleteTargetId = null;
			await loadTransactions();
		} catch (e) {
			alert('Failed to delete transaction');
		}
	}

	const cancelDelete = () => {
		showDeleteConfirm = false;
		deleteTargetId = null;
	};

	const formatCategory = (category: string): string => {
		return category.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());
	};
</script>

<div class="page-header">
	<h1>Transactions</h1>
	<Button onclick={() => (showModal = true)}>+ Add Transaction</Button>
</div>

{#if loading}
	<p>Loading...</p>
{:else if error}
	<p class="text-danger">Error: {error}</p>
{:else if transactions.length === 0}
	<div class="card empty-state">
		<p>No transactions yet.</p>
		<Button onclick={() => (showModal = true)}>Add your first Transaction</Button>
	</div>
{:else}
	<div class="card">
		<table>
			<thead>
				<tr>
					<th>Date</th>
					<th>Type</th>
					<th>Category</th>
					<th>Amount</th>
					<th>Description</th>
					<th>Actions</th>
				</tr>
			</thead>
			<tbody>
				{#each transactions as t}
					<tr>
						<td>{t.date}</td>
						<td>
							<span class="badge {t.transaction_type}">{t.transaction_type}</span>
						</td>
						<td>{formatCategory(t.category)}</td>
						<td class={t.transaction_type === 'income' ? 'text-success' : 'text-danger'}>
							{t.transaction_type === 'income' ? '+' : '-'}${t.amount}
						</td>
						<td class="text-muted">{t.description || '-'}</td>
						<td>
							<Button variant="danger" size="sm" onclick={() => promptDelete(t.id)}>Delete</Button>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
{/if}

<!-- Add Transaction Modal -->
<Modal open={showModal} title="Add Transaction" onclose={() => (showModal = false)}>
	<TransactionForm onsubmit={handleCreate} oncancel={() => (showModal = false)} />
</Modal>

<!-- Delete Confirmation Modal -->
<Modal open={showDeleteConfirm} title="Delete Transaction" onclose={cancelDelete}>
	<p class="confirm-message">
		Are you sure you want to delete this transaction? This actions cannot be undone
	</p>
	<div class="confirm-actions">
		<Button variant="secondary" onclick={cancelDelete}>Cancel</Button>
		<Button variant="danger" onclick={() => handleDelete(deleteTargetId!)}>Delete</Button>
	</div>
</Modal>

<style>
	.page-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: var(--spacing-lg);
	}

	table {
		width: 100%;
		border-collapse: collapse;
	}

	th,
	td {
		padding: var(--spacing-sm) var(--spacing-md);
		text-align: left;
		border-bottom: 1px solid var(--color-border);
	}

	th {
		font-weight: 600;
		color: var(--color-text-muted);
		font-size: 0.875rem;
	}

	.badge {
		padding: 0.25rem 0.5rem;
		border-radius: var(--radius-sm);
		font-size: 0.75rem;
		font-weight: 500;
		text-transform: capitalize;
	}

	.badge.income {
		background: #dcfce7;
		color: #166534;
	}
	.badge.expense {
		background: #fee2e2;
		color: #991b1b;
	}

	.empty-state {
		text-align: center;
		padding: var(--spacing-xl);
	}

	.empty-state p {
		margin-bottom: var(--spacing-md);
	}

	.confirm-message {
		color: var(--color-text-muted);
		margin-bottom: var(--spacing-lg);
	}

	.confirm-actions {
		display: flex;
		justify-content: flex-end;
		gap: var(--spacing-sm);
	}
</style>
