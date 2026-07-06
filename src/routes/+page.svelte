<script lang="ts">
	// Svelte 5 state for interactive custom mouse glow
	let x = $state(0);
	let y = $state(0);
	let isMouseInWindow = $state(false);

	function handleMouseMove(e: MouseEvent) {
		x = e.clientX;
		y = e.clientY;
		isMouseInWindow = true;
	}

	function handleMouseLeave() {
		isMouseInWindow = false;
	}

	// Philosophy highlights
	const philosophyItems = [
		{
			index: '01',
			title: 'Cohesive Team > Solo Genius',
			tagline: 'SYNERGY BY DESIGN',
			description: 'A synchronized, battle-tested team always out-performs a collection of isolated specialists. Building elite engineering chemistry takes years. We bring you that collective force and proven cooperation on day one.'
		},
		{
			index: '02',
			title: 'Servant Leadership & Safe Spaces',
			tagline: 'PSYCHOLOGICAL SAFETY',
			description: 'We lead by serving. We cultivate secure, transparent environments where engineering talent is mentored to express its full potential, guiding your internal squads to complete engineering autonomy.'
		},
		{
			index: '03',
			title: '20+ Years of Blueprints',
			tagline: 'STABLE SYSTEMS',
			description: 'For over two decades, we have designed and optimized architecture blueprints spanning software design, leadership structures, and secure cloud operations across startup and enterprise ecosystems alike.'
		}
	];

	// Capabilities grid
	const capabilityItems = [
		{
			title: 'Domain-Driven APIs',
			code: 'API_GATEWAY_DDD',
			description: 'Elegantly designed, highly optimized APIs aligned perfectly with your core business domain. We decouple client layers to guarantee flawless scalability and long-term evolutionary freedom.'
		},
		{
			title: 'Modern Microservices & BFF',
			code: 'MICROSERVICES_BFF',
			description: 'Resilient microservice architectures leveraging Backend-for-Frontend (BFF) patterns to orchestrate light, fast, and extremely responsive customer experiences across mobile and web.'
		},
		{
			title: 'Zero-Error DevOps & K8s',
			code: 'CD_PIPELINE_ORCH',
			description: 'Automated CI/CD release architectures covering development, test, and production. Built on Kubernetes, Azure, AWS, or multi-cloud environments for robust, fault-tolerant execution.'
		},
		{
			title: 'Legacy Modernization',
			code: 'REFACTOR_EVOLUTION',
			description: 'Surgical refactoring and incremental migration of highly complex legacy platforms. We improve observability, safety, and speed without interrupting active business operations.'
		}
	];

	// Terminal simulator data
	const terminalLogs = [
		{ time: '12:04:19', type: 'SYS', msg: 'stereoIT core architecture bootstrap initialized.' },
		{ time: '12:04:20', type: 'NET', msg: 'Cloudflare Edge CDN integration - STATUS: OK' },
		{ time: '12:04:20', type: 'K8S', msg: 'Kubernetes nodes active (3 replicas) - STATUS: HEALTHY' },
		{ time: '12:04:21', type: 'DDD', msg: 'Domain API schemas loaded (100% test coverage) - STATUS: ACTIVE' },
		{ time: '12:04:22', type: 'SEC', msg: 'Zero-trust network handshake verified.' }
	];
</script>

<div 
	onmousemove={handleMouseMove}
	onmouseleave={handleMouseLeave}
	role="none"
	style="--x: {x}px; --y: {y}px;"
	class="min-h-screen bg-obsidian bg-grid-blueprint relative flex flex-col selection:bg-cyber-mint selection:text-obsidian"
>
	<!-- Neon Glow Background Elements -->
	{#if isMouseInWindow}
		<div class="fixed inset-0 pointer-events-none z-0 radial-glow-mint transition-opacity duration-300"></div>
		<div class="fixed inset-0 pointer-events-none z-0 radial-glow-cyan transition-opacity duration-300"></div>
	{:else}
		<!-- Default static glows for non-mouse devices / landing -->
		<div class="absolute top-[20%] left-[20%] w-[500px] h-[500px] rounded-full pointer-events-none z-0 bg-cyber-mint/5 blur-[120px]"></div>
		<div class="absolute bottom-[20%] right-[20%] w-[600px] h-[600px] rounded-full pointer-events-none z-0 bg-laser-cyan/4 blur-[140px]"></div>
	{/if}

	<!-- Header / Navigation Bar -->
	<header class="sticky top-0 z-50 bg-obsidian/85 backdrop-blur-md border-b border-slate-dark/40 px-6 py-4">
		<div class="max-w-7xl mx-auto flex items-center justify-between">
			<!-- Logo -->
			<a href="#home" class="flex items-center gap-2 group">
				<span class="font-heading text-2xl font-bold tracking-tight text-white">
					stereo<span class="text-cyber-mint group-hover:text-laser-cyan transition-colors duration-300">IT</span>
				</span>
				<span class="w-1.5 h-1.5 bg-cyber-mint rounded-full animate-pulse shadow-[0_0_8px_rgba(0,245,160,0.8)]"></span>
			</a>

			<!-- Desktop Nav Links -->
			<nav class="hidden md:flex items-center gap-8 text-sm font-mono tracking-wider">
				<a 
					href="#philosophy" 
					class="text-slate-light hover:text-white transition-colors duration-300 flex items-center gap-1.5"
				>
					<span class="text-cyber-mint text-xs">01//</span> PHILOSOPHY
				</a>
				<a 
					href="#capabilities" 
					class="text-slate-light hover:text-white transition-colors duration-300 flex items-center gap-1.5"
				>
					<span class="text-cyber-mint text-xs">02//</span> CAPABILITIES
				</a>
				<a 
					href="#contact" 
					class="text-slate-light hover:text-white transition-colors duration-300 flex items-center gap-1.5"
				>
					<span class="text-cyber-mint text-xs">03//</span> CONTACT
				</a>
			</nav>

			<!-- Contact Button -->
			<a 
				href="#contact" 
				class="px-5 py-2 rounded border border-cyber-mint/30 bg-cyber-mint/5 text-cyber-mint text-sm font-mono tracking-wider hover:bg-cyber-mint hover:text-obsidian hover:border-cyber-mint hover:shadow-[0_0_15px_rgba(0,245,160,0.4)] transition-all duration-300"
			>
				BUILD WITH US
			</a>
		</div>
	</header>

	<!-- Main Layout Container -->
	<main class="flex-grow z-10">
		<!-- HERO SECTION -->
		<section id="home" class="max-w-7xl mx-auto px-6 pt-16 pb-24 md:pt-28 md:pb-36 flex flex-col gap-12 border-b border-slate-dark/30">
			<!-- Monospace Section Indicator -->
			<div class="flex items-center gap-3 font-mono text-xs text-cyber-mint tracking-widest uppercase">
				<span class="px-2 py-0.5 rounded border border-cyber-mint/20 bg-cyber-mint/10">SYSTEM_STABLE</span>
				<span>[ 00 // INCEPTION ]</span>
			</div>

			<!-- Main Heading Area -->
			<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
				<div class="lg:col-span-8 flex flex-col gap-6">
					<h1 class="text-4xl sm:text-6xl lg:text-7xl font-bold tracking-tight text-white leading-[1.05]">
						High-Performance Systems.<br />
						<span class="text-transparent bg-clip-text bg-gradient-to-r from-cyber-mint via-laser-cyan to-white">
							Cohesive Engineering Teams.
						</span>
					</h1>
					<p class="text-lg sm:text-xl text-slate-light font-light max-w-2xl leading-relaxed">
						We design, build, and scale resilient architectures—spanning software, people, and infrastructure. From greenfield startups to complex enterprise refactoring, we deliver bulletproof systems that operate without error.
					</p>
					
					<div class="flex flex-wrap gap-4 mt-4">
						<a 
							href="#contact" 
							class="px-8 py-4 bg-cyber-mint text-obsidian font-bold tracking-wide rounded hover:bg-white hover:text-obsidian hover:shadow-[0_0_25px_rgba(0,245,160,0.5)] transition-all duration-300"
						>
							Connect with Our Team
						</a>
						<a 
							href="#philosophy" 
							class="px-8 py-4 border border-slate-light/20 bg-charcoal/40 text-white font-semibold tracking-wide rounded hover:border-white hover:bg-charcoal/80 transition-all duration-300"
						>
							Our Story
						</a>
					</div>
				</div>

				<!-- Structural Technical Terminal Dashboard -->
				<div class="lg:col-span-4 border border-slate-dark/50 bg-charcoal/60 rounded-lg p-5 font-mono text-xs shadow-2xl relative overflow-hidden backdrop-blur-sm">
					<!-- Terminal header -->
					<div class="flex items-center justify-between border-b border-slate-dark/40 pb-3 mb-3">
						<div class="flex items-center gap-2">
							<span class="w-3 h-3 rounded-full bg-red-500/80"></span>
							<span class="w-3 h-3 rounded-full bg-yellow-500/80"></span>
							<span class="w-3 h-3 rounded-full bg-green-500/80"></span>
						</div>
						<div class="text-[10px] text-slate-light tracking-widest">CONSOLE // stereoIT.core</div>
					</div>

					<!-- Active monitor statistics -->
					<div class="grid grid-cols-2 gap-4 border-b border-slate-dark/40 pb-4 mb-4 text-left">
						<div>
							<div class="text-[10px] text-slate-light">ENGINEERING EXP</div>
							<div class="text-lg font-bold text-cyber-mint">20+ YEARS</div>
						</div>
						<div>
							<div class="text-[10px] text-slate-light">SYSTEM UPTIME</div>
							<div class="text-lg font-bold text-laser-cyan">99.999%</div>
						</div>
					</div>

					<!-- Log logs -->
					<div class="flex flex-col gap-2 text-left">
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
			</div>
		</section>

		<!-- PHILOSOPHY SECTION -->
		<section id="philosophy" class="max-w-7xl mx-auto px-6 py-20 md:py-28 border-b border-slate-dark/30">
			<!-- Section header -->
			<div class="flex flex-col gap-4 mb-16 text-left">
				<div class="font-mono text-xs text-cyber-mint tracking-widest uppercase">
					[ 01 // COHESION ]
				</div>
				<h2 class="text-3xl sm:text-5xl font-bold tracking-tight text-white">
					The Power of a Unified Team.
				</h2>
				<p class="text-slate-light max-w-2xl text-lg font-light">
					We believe that team can always do more than a single person, no matter the individual's skill. We foster cooperative strength and lead with a servant approach.
				</p>
			</div>

			<!-- Grid cards -->
			<div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-left">
				{#each philosophyItems as item}
					<div class="group border border-slate-dark/40 bg-charcoal/30 rounded-lg p-8 relative overflow-hidden backdrop-blur-sm hover:border-cyber-mint/30 hover:bg-charcoal/50 transition-all duration-300">
						<!-- Glow background hover -->
						<div class="absolute inset-0 bg-gradient-to-tr from-cyber-mint/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>

						<div class="flex items-center justify-between mb-8">
							<span class="font-mono text-sm text-cyber-mint border-b border-cyber-mint/20 pb-1 tracking-wider">
								{item.tagline}
							</span>
							<span class="font-mono text-2xl font-bold text-slate-dark/80 group-hover:text-cyber-mint/30 transition-colors duration-300">
								//{item.index}
							</span>
						</div>

						<h3 class="text-2xl font-bold text-white mb-4 group-hover:text-cyber-mint transition-colors duration-300">
							{item.title}
						</h3>
						<p class="text-slate-light leading-relaxed text-sm font-light">
							{item.description}
						</p>
					</div>
				{/each}
			</div>
		</section>

		<!-- CAPABILITIES SECTION -->
		<section id="capabilities" class="max-w-7xl mx-auto px-6 py-20 md:py-28 border-b border-slate-dark/30">
			<!-- Section header -->
			<div class="flex flex-col gap-4 mb-16 text-left">
				<div class="font-mono text-xs text-cyber-mint tracking-widest uppercase">
					[ 02 // CAPABILITIES ]
				</div>
				<h2 class="text-3xl sm:text-5xl font-bold tracking-tight text-white">
					Engineered for Scalability and Speed.
				</h2>
				<p class="text-slate-light max-w-2xl text-lg font-light">
					Our technical expertise spans modern design patterns and deep infrastructure engineering. We assemble absolute reliability from lines of code to containerized orchestration.
				</p>
			</div>

			<!-- Grid layout of capabilities -->
			<div class="grid grid-cols-1 md:grid-cols-2 gap-8 text-left">
				{#each capabilityItems as cap}
					<div class="group border border-slate-dark/40 bg-charcoal/20 hover:bg-charcoal/40 hover:border-laser-cyan/30 rounded-lg p-8 flex flex-col md:flex-row gap-6 items-start transition-all duration-300 relative">
						<!-- Code marker inside card -->
						<div class="font-mono text-[10px] text-slate-light/40 absolute top-4 right-4 tracking-widest uppercase">
							{cap.code}
						</div>

						<!-- Left Icon/Decorator block -->
						<div class="w-12 h-12 shrink-0 rounded border border-slate-dark/80 flex items-center justify-center font-mono text-lg text-cyber-mint bg-obsidian group-hover:border-laser-cyan group-hover:shadow-[0_0_10px_rgba(0,229,255,0.2)] transition-all duration-300">
							&lt;/&gt;
						</div>

						<!-- Body -->
						<div class="flex flex-col gap-2">
							<h3 class="text-xl font-bold text-white group-hover:text-laser-cyan transition-colors duration-300">
								{cap.title}
							</h3>
							<p class="text-slate-light text-sm leading-relaxed font-light">
								{cap.description}
							</p>
						</div>
					</div>
				{/each}
			</div>
		</section>

		<!-- CONTACT & RECOGNITION SECTION -->
		<section id="contact" class="max-w-7xl mx-auto px-6 py-20 md:py-32">
			<div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">
				<!-- Content Details -->
				<div class="lg:col-span-7 flex flex-col gap-8 text-left">
					<div class="font-mono text-xs text-cyber-mint tracking-widest uppercase">
						[ 03 // CONTACT ]
					</div>
					<h2 class="text-4xl sm:text-6xl font-bold tracking-tight text-white leading-none">
						Let’s build something built to last.
					</h2>
					<p class="text-slate-light text-lg font-light max-w-xl leading-relaxed">
						Whether you need to architect a new high-throughput platform or modernise a codebase, we provide the elite engineering team required to succeed.
					</p>

					<!-- Contacts lists -->
					<div class="flex flex-col gap-4 font-mono text-sm tracking-wider">
						<a 
							href="mailto:info@stereoit.com" 
							class="flex items-center gap-3 text-slate-light hover:text-cyber-mint transition-colors duration-300"
						>
							<span class="text-cyber-mint">EMAIL:</span> info@stereoit.com
						</a>
						<a 
							href="tel:+420776763478" 
							class="flex items-center gap-3 text-slate-light hover:text-cyber-mint transition-colors duration-300"
						>
							<span class="text-cyber-mint">PHONE:</span> +420 776 763 478
						</a>
					</div>
				</div>

				<!-- Official corporate details card -->
				<div class="lg:col-span-5 border border-slate-dark/50 bg-charcoal/30 rounded-lg p-8 text-left relative overflow-hidden backdrop-blur-sm">
					<div class="absolute top-0 right-0 w-[120px] h-[120px] bg-laser-cyan/5 rounded-full blur-[30px] pointer-events-none"></div>
					
					<div class="border-b border-slate-dark/40 pb-4 mb-6">
						<div class="text-xs font-mono text-cyber-mint tracking-wider uppercase mb-1">Corporate Registries</div>
						<h3 class="text-xl font-bold text-white font-heading">stereoIT s.r.o.</h3>
					</div>

					<div class="flex flex-col gap-5 text-sm font-light">
						<div>
							<div class="text-[10px] font-mono text-slate-light tracking-wider uppercase mb-1">Registered Address</div>
							<p class="text-slate-light leading-relaxed font-sans">
								Heřmanova 718/23<br />
								Praha 7 - Holešovice<br />
								170 00 Praha 7, Czech Republic
							</p>
						</div>

						<div class="grid grid-cols-2 gap-4 border-t border-slate-dark/30 pt-4">
							<div>
								<div class="text-[10px] font-mono text-slate-light tracking-wider uppercase mb-1">IČO</div>
								<div class="font-mono text-white text-sm">29030897</div>
							</div>
							<div>
								<div class="text-[10px] font-mono text-slate-light tracking-wider uppercase mb-1">DIČ (VAT ID)</div>
								<div class="font-mono text-white text-sm">CZ29030897</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
	</main>

	<!-- Footer -->
	<footer class="border-t border-slate-dark/30 py-8 px-6 mt-auto">
		<div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-mono text-slate-light/60">
			<div>
				&copy; {new Date().getFullYear()} stereoIT s.r.o. All rights reserved.
			</div>
			<div class="flex gap-6">
				<a href="#philosophy" class="hover:text-white transition-colors duration-300">PHILOSOPHY</a>
				<a href="#capabilities" class="hover:text-white transition-colors duration-300">CAPABILITIES</a>
				<a href="#contact" class="hover:text-white transition-colors duration-300">CONTACT</a>
			</div>
		</div>
	</footer>
</div>
