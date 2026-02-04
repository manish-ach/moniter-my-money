<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import '$lib/styles/global.css';
	import Navbar from '$lib/components/layout/Navbar.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>Budget Tracker</title>
</svelte:head>

<Navbar />

<main
	class="container"
	style="padding-top: var(--spacing-2x1); padding-bottom: var(--spacing-2x1);"
>
	{@render children()}
</main>
