import type { Transaction } from '$lib/types/transaction';

const API_BASE = import.meta.env.PUBLIC_API_URL || 'http://127.0.0.1:8000/api';

// GET all transactions
export async function getTransactions(): Promise<Transaction[]> {
	const response = await fetch(`${API_BASE}/transactions/`);

	if (!response.ok) {
		throw new Error('Failed to fetch transactions');
	}

	return response.json();
}

// Get single transaction
export async function getTransaction(id: number): Promise<Transaction> {
	const response = await fetch(`${API_BASE}/transactions/${id}/`);

	if (!response.ok) {
		throw new Error('Failed to fetch transactions');
	}

	return response.json();
}

// POST create transaction
export async function createTransaction(
	data: Omit<Transaction, 'id' | 'created_at' | 'updated_at'>
): Promise<Transaction> {
	const response = await fetch(`${API_BASE}/transactions/`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(data)
	});

	if (!response.ok) {
		throw new Error('Failed to create transaction');
	}

	return response.json();
}

// PUT update transaction
export async function updateTransaction(
	id: number,
	data: Omit<Transaction, 'id' | 'created_at' | 'updated_at'>
): Promise<Transaction> {
	const response = await fetch(`${API_BASE}/transactions/${id}/`, {
		method: 'PUT',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(data)
	});

	if (!response.ok) throw new Error('Failed to update transaction');
	return response.json();
}

//DELETE transaction
export async function deleteTransaction(id: number): Promise<void> {
	const response = await fetch(`${API_BASE}/transactions/${id}/`, {
		method: 'DELETE'
	});
	if (!response.ok) throw new Error('Failed to delete transaction');
}
