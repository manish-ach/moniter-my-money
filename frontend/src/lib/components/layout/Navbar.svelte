<script lang="ts">
	import { page } from '$app/stores';
</script>

<nav class="navbar">
	<div class="container">
		<a href="/" class="logo">Budget Tracker</a>
		<div class="nav-links">
			<a href="/" class:active={$page.url.pathname === '/'}>Dashboard</a>
			<a href="/transactions" class:active={$page.url.pathname === '/transactions'}>Transactions</a>
		</div>
	</div>
</nav>

<style>
	.navbar {
		background: var(--color-surface);
		border-bottom: 1px solid var(--color-border);
		padding: var(--spacing-md) 0;
		position: sticky;
		top: 0;
		z-index: 50;
	}

	.container {
		max-width: 1200px;
		margin: 0 auto;
		padding: 0 var(--spacing-md);
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.logo {
		font-size: 1.25rem;
		font-weight: 700;
		color: var(--color-text);
		text-decoration: none;
	}

	.nav-links {
		display: flex;
		gap: var(--spacing-lg);
	}

	.nav-links a {
		color: var(--color-text-muted);
		text-decoration: none;
		font-weight: 500;
		padding: var(--spacing-sm) var(--spacing-md);
		border-radius: var(--radius-md);
		transition: all 0.15s ease;
	}

	.nav-links a:hover {
		color: var(--color-text);
		background: var(--color-bg);
	}

	.nav-links a.active {
		color: var(--color-primary);
		background: #eef2ff;
	}
</style>
