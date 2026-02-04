export type TransactionType = 'income' | 'expense';

export type Category =
	| 'salary'
	| 'freelance'
	| 'investement'
	| 'other_income'
	| 'food'
	| 'transportation'
	| 'utilities'
	| 'rent'
	| 'entertainment'
	| 'shopping'
	| 'healthcare'
	| 'education'
	| 'other_expense';

export interface Transaction {
	id: number;
	amount: string;
	transaction_type: TransactionType;
	category: Category;
	description: string;
	date: string;
	created_at: string;
	updated_at: string;
}
