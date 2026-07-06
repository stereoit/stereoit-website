<script lang="ts">
	import { onMount } from 'svelte';

	// Component preview wrapper theme states
	let sandboxTheme = $state<'dark' | 'light'>('dark');

	// Active tab inside Storybook (Components vs Tokens)
	let activeTab = $state<'components' | 'tokens'>('components');

	// Interactive states for button demo
	let buttonCount = $state(0);
	let disabledDemo = $state(false);

	// Terminal log demo state
	let terminalLogs = $state([
		{ time: '12:00:01', type: 'SYS', msg: 'Storybook sandbox online.' },
		{ time: '12:00:02', type: 'COMP', msg: 'Core visual tokens registered successfully.' }
	]);

	function addLog() {
		const types = ['SYS', 'NET', 'SEC', 'DB', 'DDD'];
		const randomType = types[Math.floor(Math.random() * types.length)];
		const now = new Date().toTimeString().split(' ')[0];
		terminalLogs = [
			...terminalLogs,
			{ time: now, type: randomType, msg: `User interaction detected. Log index: ${terminalLogs.length + 1}` }
		];
	}

	function resetLogs() {
		terminalLogs = [
			{ time: '12:00:01', type: 'SYS', msg: 'Logs re-initialized.' }
		];
	}
</script>

<div class="min-h-screen bg-bg-primary bg-grid-blueprint text-text-main p-6 md:p-12 transition-colors duration-300">
	<!-- Main Header -->
	<header class="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between border-b border-border-grid pb-8 mb-12 gap-4">
		<div class="text-left">
			<div class="flex items-center gap-3 font-mono text-xs text-cyber-mint tracking-widest uppercase mb-2">
				<span class="px-2 py-0.5 rounded border border-cyber-mint/20 bg-cyber-mint/10">STITCH_SYNC_OK</span>
				<span>[ LOCAL // WORKSHOP ]</span>
			</div>
			<h1 class="text-3xl sm:text-4xl font-bold tracking-tight text-white font-heading">
				stereo<span class="text-cyber-mint">IT</span> Component Storybook
			</h1>
			<p class="text-text-body text-sm font-light mt-2 max-w-2xl">
				A local visual playground showcasing Svelte 5 + Tailwind v4 components mapped to our custom design tokens. Use this dashboard to audit spacing, transitions, accessibility, and themes.
			</p>
		</div>

		<!-- Global Storybook actions -->
		<div class="flex flex-wrap items-center gap-4">
			<!-- Tab Switcher -->
			<div class="flex rounded border border-border-grid bg-bg-secondary p-0.5">
				<button 
					onclick={() => activeTab = 'components'}
					class="px-4 py-1.5 rounded font-mono text-[10px] tracking-wider transition-all duration-300 {activeTab === 'components' ? 'bg-cyber-mint text-obsidian font-bold' : 'text-text-body hover:text-white'}"
				>
					COMPONENTS
				</button>
				<button 
					onclick={() => activeTab = 'tokens'}
					class="px-4 py-1.5 rounded font-mono text-[10px] tracking-wider transition-all duration-300 {activeTab === 'tokens' ? 'bg-cyber-mint text-obsidian font-bold' : 'text-text-body hover:text-white'}"
				>
					DESIGN TOKENS
				</button>
			</div>

			<a 
				href="/" 
				class="px-4 py-1.5 rounded border border-border-grid text-[10px] font-mono hover:border-cyber-mint hover:text-cyber-mint transition-colors duration-300"
			>
				&larr; BACK TO WEBSITE
			</a>
		</div>
	</header>

	<main class="max-w-7xl mx-auto">
		{#if activeTab === 'components'}
			<!-- Component Sandbox Controls -->
			<div class="flex items-center justify-between bg-bg-secondary/60 border border-border-grid p-4 rounded-lg mb-8 backdrop-blur-sm">
				<div class="text-left">
					<span class="text-[10px] font-mono text-cyber-mint uppercase tracking-wider block mb-0.5">Sandbox Config</span>
					<span class="text-xs text-text-body">Override theme of preview containers individually to audit contrast ratios.</span>
				</div>

				<div class="flex items-center gap-3">
					<span class="text-[10px] font-mono text-text-body/60 uppercase">SANDBOX_THEME:</span>
					<div class="flex rounded border border-border-grid bg-bg-primary p-0.5">
						<button 
							onclick={() => sandboxTheme = 'dark'}
							class="px-3 py-1 rounded text-[10px] font-mono transition-all duration-300 {sandboxTheme === 'dark' ? 'bg-slate-dark text-white font-bold' : 'text-text-body'}"
						>
							DARK
						</button>
						<button 
							onclick={() => sandboxTheme = 'light'}
							class="px-3 py-1 rounded text-[10px] font-mono transition-all duration-300 {sandboxTheme === 'light' ? 'bg-white text-obsidian font-bold' : 'text-text-body'}"
						>
							LIGHT
						</button>
					</div>
				</div>
			</div>

			<!-- Grid of Components -->
			<div class="flex flex-col gap-12 text-left">
				
				<!-- 1. BUTTONS CATEGORY -->
				<section class="border border-border-grid bg-bg-secondary/20 rounded-lg p-6 md:p-8">
					<div class="border-b border-border-grid pb-4 mb-6">
						<span class="text-[10px] font-mono text-cyber-mint tracking-wider uppercase">[ COMP_01 // INTERACTIVES ]</span>
						<h2 class="text-2xl font-bold text-white">Action Buttons & Controls</h2>
					</div>

					<div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
						<!-- Sandbox Previews -->
						<div class="lg:col-span-6 flex flex-col gap-6 p-6 rounded-lg transition-colors duration-300" class:bg-obsidian={sandboxTheme === 'dark'} class:bg-white={sandboxTheme === 'light'} class:border={sandboxTheme === 'light'} class:border-slate-200={sandboxTheme === 'light'}>
							<div class="text-[10px] font-mono text-text-body/50 mb-2 uppercase">PREVIEW</div>
							
							<div class="flex flex-wrap gap-4 items-center">
								<!-- Primary CTA Button -->
								<button 
									onclick={() => buttonCount++}
									disabled={disabledDemo}
									class="px-6 py-3 bg-cyber-mint text-obsidian font-bold tracking-wide rounded hover:bg-obsidian hover:text-white hover:border hover:border-cyber-mint hover:shadow-[0_0_20px_rgba(0,245,160,0.4)] disabled:opacity-40 disabled:pointer-events-none transition-all duration-300"
								>
									Primary CTA ({buttonCount})
								</button>

								<!-- Secondary/Ghost Button -->
								<button 
									disabled={disabledDemo}
									class="px-6 py-3 border border-border-grid bg-bg-secondary/40 text-text-main font-semibold tracking-wide rounded hover:bg-bg-secondary/80 disabled:opacity-40 disabled:pointer-events-none transition-all duration-300"
								>
									Secondary Button
								</button>

								<!-- Small Mono Icon Button -->
								<button 
									disabled={disabledDemo}
									class="px-4 py-2 border border-cyber-mint/30 bg-cyber-mint/5 text-cyber-mint text-xs font-mono tracking-wider hover:bg-cyber-mint hover:text-obsidian hover:border-cyber-mint transition-all duration-300"
								>
									BUILD WITH US
								</button>
							</div>

							<!-- Interaction Controls -->
							<div class="border-t border-border-grid pt-4 mt-4 flex items-center gap-4">
								<label class="flex items-center gap-2 font-mono text-xs text-text-body cursor-pointer select-none">
									<input 
										type="checkbox" 
										bind:checked={disabledDemo}
										class="rounded bg-bg-primary border-border-grid text-cyber-mint focus:ring-0 cursor-pointer"
									/>
									SIMULATE_DISABLED_STATE
								</label>
							</div>
						</div>

						<!-- Copy Code Segment -->
						<div class="lg:col-span-6 bg-charcoal rounded-lg p-5 font-mono text-xs relative border border-slate-dark overflow-x-auto text-left">
							<span class="absolute top-3 right-3 text-[10px] text-slate-light/30 uppercase">SVELTE 5</span>
							<pre class="text-slate-light"><code class="text-cyber-mint">&lt;!-- Primary Button --&gt;</code>
&lt;button 
  class="px-8 py-4 bg-cyber-mint text-obsidian font-bold 
         rounded hover:bg-white hover:shadow-[0_0_25px_rgba(0,245,160,0.5)] 
         transition-all duration-300"
&gt;
  Connect with Our Team
&lt;/button&gt;

<code class="text-cyber-mint">&lt;!-- Secondary Ghost Button --&gt;</code>
&lt;button 
  class="px-8 py-4 border border-border-grid bg-bg-secondary/40 
         text-text-main font-semibold rounded hover:bg-bg-secondary/80 
         transition-all duration-300"
&gt;
  Our Story
&lt;/button&gt;</pre>
						</div>
					</div>
				</section>

				<!-- 2. TECH TERMINAL CATEGORY -->
				<section class="border border-border-grid bg-bg-secondary/20 rounded-lg p-6 md:p-8">
					<div class="border-b border-border-grid pb-4 mb-6">
						<span class="text-[10px] font-mono text-cyber-mint tracking-wider uppercase">[ COMP_02 // SYSTEM_MONITORS ]</span>
						<h2 class="text-2xl font-bold text-white">System Logs Console / Terminal</h2>
					</div>

					<div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
						<!-- Sandbox Previews -->
						<div class="lg:col-span-6 flex flex-col gap-4 p-6 rounded-lg transition-colors duration-300" class:bg-obsidian={sandboxTheme === 'dark'} class:bg-white={sandboxTheme === 'light'} class:border={sandboxTheme === 'light'} class:border-slate-200={sandboxTheme === 'light'}>
							<div class="text-[10px] font-mono text-text-body/50 mb-2 uppercase">PREVIEW</div>

							<div class="border border-border-grid bg-charcoal rounded-lg p-5 font-mono text-xs shadow-2xl relative overflow-hidden backdrop-blur-sm w-full text-left">
								<!-- Terminal header -->
								<div class="flex items-center justify-between border-b border-slate-dark/40 pb-3 mb-3">
									<div class="flex items-center gap-2">
										<span class="w-3 h-3 rounded-full bg-red-500/80"></span>
										<span class="w-3 h-3 rounded-full bg-yellow-500/80"></span>
										<span class="w-3 h-3 rounded-full bg-green-500/80"></span>
									</div>
									<div class="text-[10px] text-slate-light tracking-widest">CONSOLE // stereoIT.core</div>
								</div>

								<!-- Logs -->
								<div class="flex flex-col gap-2 min-h-[140px] max-h-[220px] overflow-y-auto">
									{#each terminalLogs as log}
										<div class="leading-relaxed">
											<span class="text-slate-light/60">[{log.time}]</span> 
											<span class="text-laser-cyan">[{log.type}]</span> 
											<span class="text-white">{log.msg}</span>
										</div>
									{/each}
								</div>

								<!-- Blinking cursor -->
								<div class="mt-3 flex items-center gap-1.5 text-cyber-mint">
									<span>$ cd /stereoit/architecture</span>
									<span class="w-1.5 h-3 bg-cyber-mint animate-pulse"></span>
								</div>
							</div>

							<!-- Interaction Controls -->
							<div class="flex gap-3">
								<button 
									onclick={addLog}
									class="px-4 py-2 border border-cyber-mint/30 bg-cyber-mint/5 text-cyber-mint text-xs font-mono hover:bg-cyber-mint hover:text-obsidian transition-all duration-300"
								>
									➕ APPEND_LOG_EVENT
								</button>
								<button 
									onclick={resetLogs}
									class="px-4 py-2 border border-border-grid text-text-body text-xs font-mono hover:border-white hover:text-white transition-all duration-300"
								>
									🔄 RESET_CONSOLE
								</button>
							</div>
						</div>

						<!-- Copy Code Segment -->
						<div class="lg:col-span-6 bg-charcoal rounded-lg p-5 font-mono text-xs relative border border-slate-dark overflow-x-auto text-left">
							<span class="absolute top-3 right-3 text-[10px] text-slate-light/30 uppercase">SVELTE 5</span>
							<pre class="text-slate-light"><code class="text-cyber-mint">&lt;!-- Technical Console --&gt;</code>
&lt;div class="border border-border-grid bg-charcoal rounded-lg p-5 font-mono text-xs"&gt;
  &lt;div class="flex items-center justify-between border-b pb-3 mb-3"&gt;
    &lt;div class="flex items-center gap-2"&gt;
      &lt;span class="w-3 h-3 rounded-full bg-red-500/80"&gt;&lt;/span&gt;
      &lt;span class="w-3 h-3 rounded-full bg-yellow-500/80"&gt;&lt;/span&gt;
      &lt;span class="w-3 h-3 rounded-full bg-green-500/80"&gt;&lt;/span&gt;
    &lt;/div&gt;
  &lt;/div&gt;

  &lt;!-- Svelte Runes Loop --&gt;
  &lt;div class="flex flex-col gap-2"&gt;
    &#123;#each terminalLogs as log&#125;
      &lt;div&gt;
        &lt;span class="text-slate-light"&gt;[&#123;log.time&#125;]&lt;/span&gt;
        &lt;span class="text-laser-cyan"&gt;[&#123;log.type&#125;]&lt;/span&gt;
        &lt;span class="text-white"&gt;&#123;log.msg&#125;&lt;/span&gt;
      &lt;/div&gt;
    &#123;/each&#125;
  &lt;/div&gt;
&lt;/div&gt;</pre>
						</div>
					</div>
				</section>

				<!-- 3. CARDS CATEGORY -->
				<section class="border border-border-grid bg-bg-secondary/20 rounded-lg p-6 md:p-8">
					<div class="border-b border-border-grid pb-4 mb-6">
						<span class="text-[10px] font-mono text-cyber-mint tracking-wider uppercase">[ COMP_03 // DISPLAYS ]</span>
						<h2 class="text-2xl font-bold text-white">Philosophy & Capabilities Cards</h2>
					</div>

					<div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
						<!-- Sandbox Previews -->
						<div class="lg:col-span-6 flex flex-col gap-6 p-6 rounded-lg transition-colors duration-300" class:bg-obsidian={sandboxTheme === 'dark'} class:bg-white={sandboxTheme === 'light'} class:border={sandboxTheme === 'light'} class:border-slate-200={sandboxTheme === 'light'}>
							<div class="text-[10px] font-mono text-text-body/50 mb-2 uppercase">PREVIEW</div>

							<div class="grid grid-cols-1 gap-6 w-full text-left">
								<!-- Philosophy Card -->
								<div class="group border border-border-grid bg-card-bg rounded-lg p-6 relative overflow-hidden backdrop-blur-sm transition-colors duration-300">
									<div class="absolute inset-0 bg-gradient-to-tr from-cyber-mint/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
									<div class="flex items-center justify-between mb-4">
										<span class="font-mono text-xs text-cyber-mint tracking-wider">SYNERGY BY DESIGN</span>
										<span class="font-mono text-lg font-bold text-slate-light/30">//01</span>
									</div>
									<h3 class="text-lg font-bold text-text-main mb-2">Cohesive Team > Solo Genius</h3>
									<p class="text-text-body text-xs font-light leading-relaxed">
										A synchronized, battle-tested team always out-performs a collection of isolated specialists.
									</p>
								</div>
							</div>
						</div>

						<!-- Copy Code Segment -->
						<div class="lg:col-span-6 bg-charcoal rounded-lg p-5 font-mono text-xs relative border border-slate-dark overflow-x-auto text-left">
							<span class="absolute top-3 right-3 text-[10px] text-slate-light/30 uppercase">SVELTE 5</span>
							<pre class="text-slate-light"><code class="text-cyber-mint">&lt;!-- Philosophy / Capability Panel --&gt;</code>
&lt;div class="group border border-border-grid bg-card-bg rounded-lg p-8 
            relative overflow-hidden backdrop-blur-sm hover:border-cyber-mint/30 
            hover:bg-bg-secondary/30 transition-all duration-300"&gt;
  &lt;div class="absolute inset-0 bg-gradient-to-tr from-cyber-mint/5 to-transparent 
              opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"&gt;&lt;/div&gt;

  &lt;div class="flex items-center justify-between mb-8"&gt;
    &lt;span class="font-mono text-sm text-cyber-mint border-b border-cyber-mint/20 pb-1 tracking-wider"&gt;
      SYNERGY BY DESIGN
    &lt;/span&gt;
    &lt;span class="font-mono text-2xl font-bold text-slate-light/30 group-hover:text-cyber-mint/30"&gt;
      //01
    &lt;/span&gt;
  &lt;/div&gt;

  &lt;h3 class="text-2xl font-bold text-text-main mb-4 group-hover:text-cyber-mint transition-colors"&gt;
    Cohesive Team &gt; Solo Genius
  &lt;/h3&gt;
  &lt;p class="text-text-body leading-relaxed text-sm font-light"&gt;
    A synchronized, battle-tested team always out-performs a collection of isolated specialists.
  &lt;/p&gt;
&lt;/div&gt;</pre>
						</div>
					</div>
				</section>
			</div>
		{:else if activeTab === 'tokens'}
			<!-- Theme Mappings & Values Sheet -->
			<div class="grid grid-cols-1 md:grid-cols-2 gap-8 text-left animate-fadeIn">
				<!-- Color Values -->
				<div class="border border-border-grid bg-bg-secondary/20 rounded-lg p-6 md:p-8">
					<div class="border-b border-border-grid pb-4 mb-6">
						<span class="text-[10px] font-mono text-cyber-mint tracking-wider uppercase">[ TKN_01 // THEME_COLORS ]</span>
						<h2 class="text-xl font-bold text-white">Color Mappings Matrix</h2>
					</div>

					<div class="flex flex-col gap-4 text-sm font-mono">
						<!-- Obsidian bg -->
						<div class="flex items-center justify-between p-3 border border-border-grid bg-bg-primary rounded">
							<div class="flex items-center gap-3">
								<span class="w-6 h-6 rounded border border-white/20 bg-bg-primary"></span>
								<span>bg-bg-primary</span>
							</div>
							<div class="text-right text-xs text-text-body">
								<span class="block">Dark: #080809</span>
								<span class="block">Light: #f8f9fa</span>
							</div>
						</div>

						<!-- Charcoal bg -->
						<div class="flex items-center justify-between p-3 border border-border-grid bg-bg-secondary rounded">
							<div class="flex items-center gap-3">
								<span class="w-6 h-6 rounded border border-white/20 bg-bg-secondary"></span>
								<span>bg-bg-secondary</span>
							</div>
							<div class="text-right text-xs text-text-body">
								<span class="block">Dark: #121214</span>
								<span class="block">Light: #ffffff</span>
							</div>
						</div>

						<!-- Main Text -->
						<div class="flex items-center justify-between p-3 border border-border-grid bg-bg-secondary rounded">
							<div class="flex items-center gap-3">
								<span class="w-6 h-6 rounded border border-white/20 bg-text-main"></span>
								<span>text-text-main</span>
							</div>
							<div class="text-right text-xs text-text-body">
								<span class="block">Dark: #ffffff</span>
								<span class="block">Light: #0f172a</span>
							</div>
						</div>

						<!-- Cyber Mint constant -->
						<div class="flex items-center justify-between p-3 border border-border-grid bg-bg-secondary rounded">
							<div class="flex items-center gap-3">
								<span class="w-6 h-6 rounded border border-white/20 bg-cyber-mint"></span>
								<span>cyber-mint</span>
							</div>
							<div class="text-right text-xs text-text-body">
								<span class="block">Constant: #00F5A0</span>
							</div>
						</div>

						<!-- Laser Cyan constant -->
						<div class="flex items-center justify-between p-3 border border-border-grid bg-bg-secondary rounded">
							<div class="flex items-center gap-3">
								<span class="w-6 h-6 rounded border border-white/20 bg-laser-cyan"></span>
								<span>laser-cyan</span>
							</div>
							<div class="text-right text-xs text-text-body">
								<span class="block">Constant: #00E5FF</span>
							</div>
						</div>
					</div>
				</div>

				<!-- Typography Scale -->
				<div class="border border-border-grid bg-bg-secondary/20 rounded-lg p-6 md:p-8">
					<div class="border-b border-border-grid pb-4 mb-6">
						<span class="text-[10px] font-mono text-cyber-mint tracking-wider uppercase">[ TKN_02 // DISPLAY_SCALES ]</span>
						<h2 class="text-xl font-bold text-white">Typography Specifications</h2>
					</div>

					<div class="flex flex-col gap-6 font-sans">
						<!-- Display H1 -->
						<div class="border-b border-border-grid pb-4">
							<div class="text-[10px] font-mono text-text-body/50 mb-1">font-heading (72px / Bold / Tracking-Tight)</div>
							<h3 class="text-3xl sm:text-4xl font-bold tracking-tight text-white font-heading leading-tight">Heading XL</h3>
						</div>

						<!-- Headline H2 -->
						<div class="border-b border-border-grid pb-4">
							<div class="text-[10px] font-mono text-text-body/50 mb-1">font-heading (32px / Semi-Bold)</div>
							<h3 class="text-2xl font-semibold text-white font-heading">Heading LG</h3>
						</div>

						<!-- Body -->
						<div class="border-b border-border-grid pb-4">
							<div class="text-[10px] font-mono text-text-body/50 mb-1">font-sans (16px / Regular / Leading-Relaxed)</div>
							<p class="text-text-body text-sm font-light leading-relaxed">
								Body copy optimized for maximum compliance on digital screens in dark/light modes.
							</p>
						</div>

						<!-- Tech Label -->
						<div>
							<div class="text-[10px] font-mono text-text-body/50 mb-1">font-mono (13px / Medium / Tracking-Widest / Uppercase)</div>
							<p class="text-cyber-mint font-mono text-sm tracking-widest uppercase">
								[ 01 // HIGH_FREQUENCY_ACCENT ]
							</p>
						</div>
					</div>
				</div>
			</div>
		{/if}
	</main>
</div>
