<script lang="ts">
	import { onMount } from 'svelte';

	// Storybook state management
	let globalTheme = $state<'option-a' | 'option-b' | 'option-c' | 'option-d'>('option-a');
	let activeTab = $state<'colors' | 'typography' | 'components'>('colors');

	// Font choice toggles for testing
	let fontChoice = $state<'serif' | 'sans'>('serif');

	// Svelte 5 interactive counters / parameters
	let sampleCounter = $state(0);
	let isSimulatingHover = $state(false);

	onMount(() => {
		// Read theme from layout if possible
		if ((window as any).getStereoitTheme) {
			const saved = (window as any).getStereoitTheme();
			if (saved === 'option-b') globalTheme = 'option-b';
			else if (saved === 'option-c') globalTheme = 'option-c';
			else if (saved === 'option-d') globalTheme = 'option-d';
			else globalTheme = 'option-a';
		}

		// Sync with layout theme changes
		window.addEventListener('theme-changed', (e: any) => {
			const t = e.detail.resolvedTheme;
			if (t === 'option-b') globalTheme = 'option-b';
			else if (t === 'option-c') globalTheme = 'option-c';
			else if (t === 'option-d') globalTheme = 'option-d';
			else globalTheme = 'option-a';
		});
	});

	function toggleGlobalTheme(theme: 'option-a' | 'option-b' | 'option-c' | 'option-d') {
		globalTheme = theme;
		if ((window as any).setStereoitTheme) {
			(window as any).setStereoitTheme(theme);
		}
	}

	// Dynamic side-by-side matrix information for all 4 distinct design proposals
	const themesInfo = [
		{
			id: 'option-a',
			name: 'Option A: The Evening Architect (Dark)',
			badge: 'REFINED DARK BASELINE',
			bg: 'bg-[#121212] text-zinc-100 border border-zinc-800/80',
			labelColor: '#8F9E8B',
			textColor: 'text-zinc-400',
			accentDesc: 'Calming Sage Green on Warm Graphite base. Calm, sophisticated, and night-focused.',
			swatches: [
				{ name: 'primary', hex: '#8F9E8B', desc: 'Calming Sage', onHex: '#18181B' },
				{ name: 'primary-container', hex: '#2D352C', desc: 'Sage Panel Tint', onHex: '#DCE4DA' },
				{ name: 'secondary', hex: '#A1A1AA', desc: 'Titanium Grey', onHex: '#18181B' },
				{ name: 'secondary-container', hex: '#27272A', desc: 'Charcoal Card', onHex: '#E4E4E7' },
				{ name: 'tertiary', hex: '#D4AF37', desc: 'Sand Gold', onHex: '#1C1917' },
				{ name: 'background', hex: '#121212', desc: 'Graphite Canvas', onHex: '#FAFAFA' }
			]
		},
		{
			id: 'option-b',
			name: 'Option B: The Master Craftsman (Light)',
			badge: 'RAW CLAY & ALABASTER',
			bg: 'bg-[#FAF9F6] text-[#1C1917] border border-stone-200/80',
			labelColor: '#A76D53',
			textColor: 'text-stone-600',
			accentDesc: 'Raw Terracotta Clay on Alabaster. Tactile, premium, grounded, and human-centric.',
			swatches: [
				{ name: 'primary', hex: '#A76D53', desc: 'Raw Terracotta', onHex: '#FAF9F6' },
				{ name: 'primary-container', hex: '#F5EBE6', desc: 'Clay Panel Tint', onHex: '#6E3E2B' },
				{ name: 'secondary', hex: '#64748B', desc: 'Slate Blue', onHex: '#FAF9F6' },
				{ name: 'secondary-container', hex: '#F1F5F9', desc: 'Slate Card', onHex: '#1E293B' },
				{ name: 'tertiary', hex: '#7E8F7C', desc: 'Mineral Sage', onHex: '#FAF9F6' },
				{ name: 'background', hex: '#FAF9F6', desc: 'Gallery Alabaster', onHex: '#1C1917' }
			]
		},
		{
			id: 'option-c',
			name: 'Option C: The Prussian Blueprint (Light)',
			badge: 'BLUEPRINT BLUE & GOLD',
			bg: 'bg-[#FAF9F6] text-[#102A43] border border-blue-100/80',
			labelColor: '#1B2E4A',
			textColor: 'text-slate-600',
			accentDesc: 'Deep Indigo on Alabaster. Emphasizes intellectual authority, mathematical trust, and precision.',
			swatches: [
				{ name: 'primary', hex: '#1B2E4A', desc: 'Blueprint Indigo', onHex: '#FAF9F6' },
				{ name: 'primary-container', hex: '#ECEFF4', desc: 'Indigo Panel Tint', onHex: '#102A43' },
				{ name: 'secondary', hex: '#486581', desc: 'Steel Slate', onHex: '#FAF9F6' },
				{ name: 'secondary-container', hex: '#F0F4F8', desc: 'Steel Card', onHex: '#102A43' },
				{ name: 'tertiary', hex: '#B19253', desc: 'Brass/Gold Accent', onHex: '#1C1917' },
				{ name: 'background', hex: '#FAF9F6', desc: 'Gallery Alabaster', onHex: '#102A43' }
			]
		},
		{
			id: 'option-d',
			name: 'Option D: The Sustainable Haven (Light)',
			badge: 'FOREST SAGE & OCHRE',
			bg: 'bg-[#FAF9F6] text-[#1C1917] border border-stone-200/80',
			labelColor: '#4D5E52',
			textColor: 'text-[#4A4A4A]',
			accentDesc: 'Forest Sage on Alabaster. Represents rest, psychological safety, organic growth, and balance.',
			swatches: [
				{ name: 'primary', hex: '#4D5E52', desc: 'Forest Sage', onHex: '#FAF9F6' },
				{ name: 'primary-container', hex: '#F1F4F0', desc: 'Sage Panel Tint', onHex: '#213225' },
				{ name: 'secondary', hex: '#5C6B73', desc: 'Earthy Slate', onHex: '#FAF9F6' },
				{ name: 'secondary-container', hex: '#F4F1EA', desc: 'Warm Sand Card', onHex: '#2D3142' },
				{ name: 'tertiary', hex: '#D4A373', desc: 'Warm Ochre', onHex: '#1C1917' },
				{ name: 'background', hex: '#FAF9F6', desc: 'Gallery Alabaster', onHex: '#1C1917' }
			]
		}
	];
</script>

<div class="min-h-screen bg-bg-primary bg-grid-blueprint text-text-main p-6 md:p-12 transition-colors duration-400 font-sans" data-theme={globalTheme}>
	<!-- Atmospheric glow adjusted for structural clarity -->
	<div class="absolute top-[10%] left-[5%] w-[400px] h-[400px] rounded-full pointer-events-none z-0 bg-primary/2 blur-[100px] transition-all duration-400"></div>
	<div class="absolute bottom-[10%] right-[5%] w-[500px] h-[500px] rounded-full pointer-events-none z-0 bg-tertiary/2 blur-[120px] transition-all duration-400"></div>

	<!-- Storybook Header -->
	<header class="max-w-7xl mx-auto flex flex-col lg:flex-row lg:items-end justify-between border-b border-border-grid pb-8 mb-12 gap-6 relative z-10">
		<div class="text-left">
			<div class="flex items-center gap-3 font-mono text-[10px] text-primary tracking-widest uppercase mb-3">
				<span class="px-2 py-0.5 rounded border border-primary/20 bg-primary/5">STITCH_M3_SYSTEM</span>
				<span>[ ARCHITECTURAL COLOR PSYCHOLOGY LAB ]</span>
			</div>
			<h1 class="text-3xl sm:text-4xl font-bold tracking-tight text-text-main font-heading transition-colors duration-400">
				stereo<span class="text-primary">IT</span> Design Hub
			</h1>
			<p class="text-text-body text-sm font-light mt-2 max-w-2xl transition-colors duration-400 leading-relaxed">
				Explore the psychological representations of the stereoIT brand. Use the switcher below to change the global canvas state, or scroll down to audit all four design directions side-by-side.
			</p>
		</div>

		<!-- Segmented Control Widget with 4 distinct options -->
		<div class="flex flex-col items-start lg:items-end gap-2 shrink-0">
			<span class="text-[9px] font-mono text-text-body/60 uppercase tracking-widest">Active Canvas Direction</span>
			<div class="flex flex-wrap rounded border border-border-grid bg-bg-secondary p-0.5 transition-colors duration-300 shadow-sm gap-1">
				<button 
					onclick={() => toggleGlobalTheme('option-a')}
					class="px-3 py-2 rounded font-mono text-[9px] tracking-wider transition-all duration-300 flex items-center gap-2 {globalTheme === 'option-a' ? 'bg-primary text-on-primary font-bold shadow-md' : 'text-text-body hover:text-text-main'}"
				>
					<span class="w-2.5 h-2.5 rounded-full bg-[#8F9E8B] border border-black/10"></span>
					A [DARK SAGE]
				</button>
				<button 
					onclick={() => toggleGlobalTheme('option-b')}
					class="px-3 py-2 rounded font-mono text-[9px] tracking-wider transition-all duration-300 flex items-center gap-2 {globalTheme === 'option-b' ? 'bg-primary text-on-primary font-bold shadow-md' : 'text-text-body hover:text-text-main'}"
				>
					<span class="w-2.5 h-2.5 rounded-full bg-[#A76D53] border border-white/10"></span>
					B [TERRACOTTA]
				</button>
				<button 
					onclick={() => toggleGlobalTheme('option-c')}
					class="px-3 py-2 rounded font-mono text-[9px] tracking-wider transition-all duration-300 flex items-center gap-2 {globalTheme === 'option-c' ? 'bg-primary text-on-primary font-bold shadow-md' : 'text-text-body hover:text-text-main'}"
				>
					<span class="w-2.5 h-2.5 rounded-full bg-[#1B2E4A] border border-white/10"></span>
					C [INDIGO]
				</button>
				<button 
					onclick={() => toggleGlobalTheme('option-d')}
					class="px-3 py-2 rounded font-mono text-[9px] tracking-wider transition-all duration-300 flex items-center gap-2 {globalTheme === 'option-d' ? 'bg-primary text-on-primary font-bold shadow-md' : 'text-text-body hover:text-text-main'}"
				>
					<span class="w-2.5 h-2.5 rounded-full bg-[#4D5E52] border border-white/10"></span>
					D [FOREST SAGE]
				</button>
			</div>
		</div>
	</header>

	<main class="max-w-7xl mx-auto relative z-10">
		<!-- Tabs Navigation -->
		<div class="flex border-b border-border-grid mb-8 font-mono text-[11px] tracking-widest uppercase overflow-x-auto whitespace-nowrap">
			<button 
				onclick={() => activeTab = 'colors'} 
				class="py-3 px-6 border-b-2 font-medium transition-all duration-300 {activeTab === 'colors' ? 'border-primary text-text-main font-bold' : 'border-transparent text-text-body hover:text-text-main'}"
			>
				01 // COLOR PSYCHOLOGY ARCHETYPES
			</button>
			<button 
				onclick={() => activeTab = 'typography'} 
				class="py-3 px-6 border-b-2 font-medium transition-all duration-300 {activeTab === 'typography' ? 'border-primary text-text-main font-bold' : 'border-transparent text-text-body hover:text-text-main'}"
			>
				02 // TYPOGRAPHY COMPARISON
			</button>
			<button 
				onclick={() => activeTab = 'components'} 
				class="py-3 px-6 border-b-2 font-medium transition-all duration-300 {activeTab === 'components' ? 'border-primary text-text-main font-bold' : 'border-transparent text-text-body hover:text-text-main'}"
			>
				03 // ARCHITECTURAL COMPONENTS
			</button>
		</div>

		<!-- TAB 1: COLOR PSYCHOLOGY ARCHETYPES -->
		{#if activeTab === 'colors'}
			<div class="space-y-12">
				<div class="text-left max-w-3xl mb-8">
					<h2 class="text-xl font-bold font-heading text-text-main mb-1">Color Systems side-by-side</h2>
					<p class="text-text-body text-xs font-light leading-relaxed">
						We have mapped four archetypes matching distinct psychological paths for stereoIT. Hover and view the contrast details. Clicking "Apply Theme Context" on any panel will sync the storybook's components block.
					</p>
				</div>

				<!-- Side-by-Side 4 columns on large, stacked on mobile -->
				<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
					{#each themesInfo as theme}
						<div class="rounded-xl p-6 flex flex-col justify-between transition-all duration-400 {theme.bg} {globalTheme === theme.id ? 'ring-2 ring-primary ring-offset-2' : ''}">
							<!-- Panel Header -->
							<div class="text-left border-b pb-4 mb-5 border-current/10">
								<div class="flex items-center justify-between mb-1.5">
									<span class="text-[9px] font-mono uppercase tracking-widest py-0.5 px-2 bg-current/5 rounded" style="color: {theme.labelColor}">
										{theme.badge}
									</span>
									<span class="text-[9px] font-mono opacity-40">//{theme.id.toUpperCase()}</span>
								</div>
								<h3 class="text-base font-bold font-heading">{theme.name}</h3>
								<p class="text-[11px] font-light mt-2 leading-relaxed opacity-80">{theme.accentDesc}</p>
							</div>

							<!-- Color Chip Matrix -->
							<div class="space-y-2.5 mb-6 text-left">
								<span class="text-[9px] font-mono uppercase tracking-widest opacity-40 block mb-1">M3 Tokens Mapping</span>
								{#each theme.swatches as swatch}
									<div class="rounded p-2.5 flex items-center justify-between text-[11px] font-mono" style="background: {swatch.hex}; color: {swatch.onHex}">
										<span class="font-bold">{swatch.name}</span>
										<span class="opacity-70">{swatch.hex}</span>
									</div>
								{/each}
							</div>

							<!-- Activate Button -->
							<button 
								onclick={() => toggleGlobalTheme(theme.id as any)}
								class="w-full py-2.5 text-center font-mono text-[10px] tracking-wider rounded border border-current hover:bg-current hover:text-bg-primary transition-all duration-300"
							>
								{globalTheme === theme.id ? 'CURRENT_ACTIVE' : 'APPLY_THEME_CONTEXT'}
							</button>
						</div>
					{/each}
				</div>
			</div>
		{/if}

		<!-- TAB 2: TYPOGRAPHY COMPARISON -->
		{#if activeTab === 'typography'}
			<div class="space-y-12 text-left">
				<div class="max-w-3xl">
					<h2 class="text-xl font-bold font-heading text-text-main mb-1">Typography & Type-Scaling Archetypes</h2>
					<p class="text-text-body text-xs font-light leading-relaxed">
						To express deep craftsmanship and stability, we are auditing two visual directions: **The Editorial Serif** reflecting timeless high-end advisory services, and **The Swiss Architectural Sans** reflecting hyper-precision engineering.
					</p>
				</div>

				<!-- Visual Toggle -->
				<div class="flex items-center gap-3 bg-bg-secondary/40 border border-border-grid p-4 rounded-lg backdrop-blur-sm">
					<span class="text-[10px] font-mono text-text-body/60 uppercase">AUDIT_FONT_SET:</span>
					<div class="flex rounded border border-border-grid bg-bg-primary p-0.5">
						<button 
							onclick={() => fontChoice = 'serif'} 
							class="px-4 py-1.5 rounded font-mono text-[10px] tracking-wider transition-all duration-300 {fontChoice === 'serif' ? 'bg-primary text-on-primary font-bold' : 'text-text-body'}"
						>
							PLAYFAIR DISPLAY (SERIF)
						</button>
						<button 
							onclick={() => fontChoice = 'sans'} 
							class="px-4 py-1.5 rounded font-mono text-[10px] tracking-wider transition-all duration-300 {fontChoice === 'sans' ? 'bg-primary text-on-primary font-bold' : 'text-text-body'}"
						>
							GEIST SANS (SANS-SERIF)
						</button>
					</div>
				</div>

				<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
					<!-- Left: Large Render Scale Sandbox -->
					<div class="lg:col-span-8 border border-border-grid bg-bg-secondary/20 p-8 rounded-xl backdrop-blur-sm flex flex-col gap-8">
						<div>
							<span class="text-[10px] font-mono text-primary uppercase tracking-widest block mb-2">[ DISPLAY HEADER XL ]</span>
							<h3 class="text-4xl sm:text-6xl tracking-tight leading-[1.1] transition-all duration-300 {fontChoice === 'serif' ? 'font-serif font-light italic' : 'font-sans font-extralight tracking-wide'} text-text-main">
								Architects of Enduring Digital Infrastructure.
							</h3>
						</div>

						<div class="border-t border-border-grid pt-6">
							<span class="text-[10px] font-mono text-primary uppercase tracking-widest block mb-2">[ SECTION HEADER H2 ]</span>
							<h4 class="text-2xl font-bold font-heading text-text-main">
								We design, build, and scale complex systems that last.
							</h4>
						</div>

						<div class="border-t border-border-grid pt-6">
							<span class="text-[10px] font-mono text-primary uppercase tracking-widest block mb-2">[ READABLE BODY COPY ]</span>
							<p class="text-base text-text-body leading-relaxed font-light max-w-xl">
								A unified, highly experienced engineering team always delivers more than a disconnected collection of isolated individual contractors. We lead by serving your goals, establishing zero-error pipelines, and preparing architectures to stand the test of massive scale.
							</p>
						</div>

						<div class="border-t border-border-grid pt-6 flex flex-wrap gap-4 items-center">
							<div>
								<span class="text-[10px] font-mono text-primary uppercase tracking-widest block mb-2">[ TECHNICAL CODE / BLUEPRINT LABELS ]</span>
								<div class="flex items-center gap-3 font-mono text-[11px] text-text-body">
									<span class="px-2 py-0.5 border border-primary/25 text-primary bg-primary/5 rounded">DETAIL_A // COHESION</span>
									<span>[ SCALE 1:1 ]</span>
									<span>[ UPTIME: 99.999% ]</span>
								</div>
							</div>
						</div>
					</div>

					<!-- Right: Typography Specs Details Sheet -->
					<div class="lg:col-span-4 border border-border-grid bg-bg-secondary/40 p-6 rounded-xl flex flex-col gap-6">
						<div class="border-b border-border-grid pb-3">
							<h4 class="font-bold text-sm text-text-main">Typography Tokens Specs</h4>
						</div>

						<div class="space-y-4 text-xs font-mono">
							<div>
								<span class="text-text-body/60 block text-[10px]">DISPLAY-XL:</span>
								<span class="text-text-main block mt-1 font-bold">Playfair Display / Serif</span>
								<span class="text-text-body block">Size: 56px | Weight: Light | Height: 1.1</span>
							</div>
							<div class="border-t border-border-grid/50 pt-3">
								<span class="text-text-body/60 block text-[10px]">HEADLINE-LG:</span>
								<span class="text-text-main block mt-1 font-bold">Space Grotesk</span>
								<span class="text-text-body block">Size: 32px | Weight: Semi-Bold | Height: 1.2</span>
							</div>
							<div class="border-t border-border-grid/50 pt-3">
								<span class="text-text-body/60 block text-[10px]">BODY-MD:</span>
								<span class="text-text-main block mt-1 font-bold">Inter / Sans-Serif</span>
								<span class="text-text-body block">Size: 16px | Weight: Light (300) | Height: 1.7</span>
							</div>
							<div class="border-t border-border-grid/50 pt-3">
								<span class="text-text-body/60 block text-[10px]">MONO-LABEL:</span>
								<span class="text-text-main block mt-1 font-bold">JetBrains Mono</span>
								<span class="text-text-body block">Size: 11px | Track: 0.15em | Uppercase</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		{/if}

		<!-- TAB 3: ARCHITECTURAL COMPONENTS -->
		{#if activeTab === 'components'}
			<div class="space-y-12 text-left animate-fadeIn">
				<div class="max-w-3xl">
					<h2 class="text-xl font-bold font-heading text-text-main mb-1">Architectural UI Building Blocks</h2>
					<p class="text-text-body text-xs font-light leading-relaxed">
						These blocks dynamically inherit the active brand context (Option A, B, C, or D). Swap between the choices in the header to audit how typography, outlines, and buttons render.
					</p>
				</div>

				<div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
					
					<!-- 1. BUTTONS & CONTROLS BOX -->
					<div class="border border-border-grid bg-bg-secondary/20 p-8 rounded-xl flex flex-col gap-6">
						<div class="border-b border-border-grid pb-3 mb-2 flex items-center justify-between">
							<h3 class="text-lg font-bold font-heading text-text-main">01 / Button & Interactive Controls</h3>
							<span class="font-mono text-[9px] text-primary">COMP_01</span>
						</div>

						<p class="text-xs text-text-body font-light leading-relaxed mb-2">
							Buttons now emphasize solid material fills, thin border definitions, and tactile, calm interactions instead of intense neon bleeds.
						</p>

						<div class="flex flex-wrap gap-4 items-center">
							<!-- Primary CTA -->
							<button 
								onclick={() => sampleCounter++}
								class="px-6 py-3 bg-primary text-on-primary font-semibold text-sm tracking-wide rounded hover:bg-text-main hover:text-bg-primary transition-all duration-300"
							>
								Primary Action ({sampleCounter})
							</button>

							<!-- Secondary Ghost -->
							<button 
								class="px-6 py-3 border border-border-grid bg-transparent text-text-main font-medium text-sm tracking-wide rounded hover:bg-bg-secondary transition-all duration-300"
							>
								Secondary Action
							</button>

							<!-- Small Technical Tag -->
							<button 
								class="px-3 py-1 border border-primary/20 bg-primary/5 text-primary font-mono text-[10px] tracking-widest uppercase hover:bg-primary hover:text-on-primary transition-all duration-300"
							>
								[ SECURE_ACCESS ]
							</button>
						</div>

						<!-- Live Hover Simulator State controller -->
						<div class="border-t border-border-grid/60 pt-4 flex items-center justify-between">
							<label class="flex items-center gap-2 font-mono text-[11px] text-text-body select-none cursor-pointer">
								<input 
									type="checkbox" 
									bind:checked={isSimulatingHover}
									class="rounded bg-bg-primary border-border-grid text-primary focus:ring-0 cursor-pointer"
								/>
								Simulate Interactive State
							</label>

							{#if isSimulatingHover}
								<span class="text-[10px] font-mono text-tertiary animate-pulse font-bold">State: Tactile focus active</span>
							{/if}
						</div>
					</div>

					<!-- 2. STRUCTURAL ASYMMETRIC CARD -->
					<div class="border border-border-grid bg-bg-secondary/20 p-8 rounded-xl flex flex-col gap-6 justify-between">
						<div>
							<div class="border-b border-border-grid pb-3 mb-2 flex items-center justify-between">
								<h3 class="text-lg font-bold font-heading text-text-main">02 / Asymmetrical Structure Panel</h3>
								<span class="font-mono text-[9px] text-primary">COMP_02</span>
							</div>

							<p class="text-xs text-text-body font-light leading-relaxed mb-4">
								Emphasizing intentional negative space. This layout leaves the right-hand column open to draw focus to technical precision.
							</p>

							<div class="grid grid-cols-1 sm:grid-cols-12 gap-4">
								<div class="sm:col-span-8 p-5 bg-bg-secondary border border-border-grid rounded-lg flex flex-col gap-3">
									<div class="flex items-center gap-2 font-mono text-[10px] text-primary">
										<span>DETAIL // 01</span>
										<span>•</span>
										<span>SYNERGY</span>
									</div>
									<h4 class="text-base font-bold text-text-main">The Power of Cohesion</h4>
									<p class="text-xs text-text-body font-light leading-relaxed">
										A synchronized, battle-tested team always out-performs a collection of isolated specialists. We bring that collective force on day one.
									</p>
								</div>
								<div class="sm:col-span-4 border border-dashed border-border-grid rounded-lg flex items-center justify-center p-4">
									<span class="font-mono text-[9px] text-text-body/40 text-center uppercase tracking-widest">Asymmetric Space</span>
								</div>
							</div>
						</div>
					</div>

					<!-- 3. ARCHITECTURAL GRID AND DIVIDERS -->
					<div class="border border-border-grid bg-bg-secondary/20 p-8 rounded-xl flex flex-col gap-6">
						<div class="border-b border-border-grid pb-3 mb-2 flex items-center justify-between">
							<h3 class="text-lg font-bold font-heading text-text-main">03 / The Blueprint Grid System</h3>
							<span class="font-mono text-[9px] text-primary">COMP_03</span>
						</div>

						<p class="text-xs text-text-body font-light leading-relaxed mb-2">
							Instead of floating shadows, we use an integrated 60px drafting grid and thin outlines to bound content.
						</p>

						<!-- Grid Canvas Box -->
						<div class="h-44 w-full bg-bg-primary bg-grid-blueprint border border-border-grid rounded-lg relative overflow-hidden flex items-center justify-center">
							<div class="absolute inset-0 bg-gradient-to-br from-primary/5 to-transparent pointer-events-none"></div>
							
							<div class="border border-border-grid p-4 bg-bg-secondary/80 backdrop-blur-sm rounded max-w-xs text-center z-10 shadow-sm">
								<span class="font-mono text-[10px] text-primary block mb-1">[ COHESION_GRID ]</span>
								<p class="text-xs text-text-main font-semibold leading-tight">Structured Layout Base</p>
								<div class="mt-2 w-full h-1 bg-border-grid rounded-full overflow-hidden">
									<div class="w-2/3 h-full bg-primary animate-pulse"></div>
								</div>
							</div>
						</div>
					</div>

					<!-- 4. CLEAN SYSTEM BLUEPRINT ARCHITECTURE DIAGRAM -->
					<div class="border border-border-grid bg-bg-secondary/20 p-8 rounded-xl flex flex-col gap-6">
						<div class="border-b border-border-grid pb-3 mb-2 flex items-center justify-between">
							<h3 class="text-lg font-bold font-heading text-text-main">04 / Clean System Blueprint</h3>
							<span class="font-mono text-[9px] text-primary">COMP_04</span>
						</div>

						<p class="text-xs text-text-body font-light leading-relaxed mb-2">
							Communicating complex engineering platforms utilizing a structured visual blueprint flow with zero hacker terminals.
						</p>

						<!-- CSS Diagram -->
						<div class="bg-bg-secondary border border-border-grid rounded-lg p-6 flex flex-col gap-4 font-mono text-[10px] text-text-body relative overflow-hidden">
							<!-- API Gateway Layer -->
							<div class="border border-border-grid bg-bg-primary/50 py-3 rounded text-center relative z-10">
								<span class="text-primary font-bold">API GATEWAY LAYER [BFF]</span>
								<div class="text-[9px] text-text-body/50 mt-1 font-sans">Domain API Schema Decoupling (100% Type-Safe)</div>
							</div>

							<!-- Connection lines -->
							<div class="flex justify-around py-1 px-4 text-primary text-xs relative z-10">
								<span>│</span>
								<span>│</span>
							</div>

							<div class="grid grid-cols-2 gap-4 relative z-10">
								<!-- Left service -->
								<div class="border border-border-grid bg-bg-primary/50 p-3 rounded text-center">
									<span class="text-text-main font-bold">SERVICE_A</span>
									<div class="text-[8px] text-text-body/50 mt-1 font-sans">Domain Driven microservices</div>
								</div>

								<!-- Right service -->
								<div class="border border-border-grid bg-bg-primary/50 p-3 rounded text-center">
									<span class="text-text-main font-bold">INFRASTRUCTURE</span>
									<div class="text-[8px] text-text-body/50 mt-1 font-sans">Kubernetes Orch. (AWS/Azure)</div>
								</div>
							</div>

							<!-- Static metrics on the bottom -->
							<div class="border-t border-border-grid/50 pt-3 flex justify-between items-center text-[9px] text-text-body/60 relative z-10">
								<span>ENGINEERING EXPERIENCE: 20+ YEARS</span>
								<span>SYSTEM UPTIME: 99.999%</span>
							</div>
						</div>
					</div>

				</div>
			</div>
		{/if}
	</main>

	<!-- Footer -->
	<footer class="max-w-7xl mx-auto border-t border-border-grid py-8 mt-16 text-center text-xs font-mono text-text-body/40">
		<div>
			&copy; {new Date().getFullYear()} stereoIT s.r.o. Workshop Dashboard. All rights reserved.
		</div>
	</footer>
</div>
