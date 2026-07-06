<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';
	import { onMount } from 'svelte';

	let { children } = $props();

	// Active theme options: 'system', 'light', 'dark'
	let theme = $state('system');
	let resolvedTheme = $state('dark');

	function applyTheme() {
		if (theme === 'system') {
			if (typeof window !== 'undefined') {
				const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
				resolvedTheme = systemPrefersDark ? 'dark' : 'light';
			}
		} else {
			resolvedTheme = theme;
		}

		if (typeof document !== 'undefined') {
			const root = document.documentElement;
			root.classList.remove('light', 'dark');
			root.classList.add(resolvedTheme);
			root.setAttribute('data-theme', resolvedTheme);
		}
	}

	onMount(() => {
		// Read theme from localStorage if saved
		const savedTheme = localStorage.getItem('stereoit-theme') || 'system';
		theme = savedTheme;
		applyTheme();

		// Listen for system theme changes
		const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
		const handleChange = () => {
			if (theme === 'system') applyTheme();
		};
		mediaQuery.addEventListener('change', handleChange);

		// Expose a global theme switcher function on the window for child page overrides
		(window as any).setStereoitTheme = (newTheme: string) => {
			theme = newTheme;
		};
		(window as any).getStereoitTheme = () => theme;

		return () => {
			mediaQuery.removeEventListener('change', handleChange);
		};
	});

	// Reactivity loop to sync selection
	$effect(() => {
		applyTheme();
		if (typeof window !== 'undefined') {
			localStorage.setItem('stereoit-theme', theme);
			// Fire a custom event so child pages or other components (like Storybook) can sync
			window.dispatchEvent(new CustomEvent('theme-changed', { detail: { theme, resolvedTheme } }));
		}
	});
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{@render children()}
