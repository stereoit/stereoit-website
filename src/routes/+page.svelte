<script lang="ts">
	import { onMount } from 'svelte';

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

	// Svelte 5 state for Theme Override
	let activeTheme = $state('option-b');

	onMount(() => {
		// Default to Option B (Master Craftsman) as our official brand direction
		const saved = localStorage.getItem('stereoit-theme') || 'option-b';
		activeTheme = saved;

		if ((window as any).setStereoitTheme) {
			(window as any).setStereoitTheme(saved);
		}

		// Listen for layout theme state sync
		window.addEventListener('theme-changed', (e: any) => {
			activeTheme = e.detail.theme;
		});
	});

	function selectTheme(theme: string) {
		activeTheme = theme;
		if ((window as any).setStereoitTheme) {
			(window as any).setStereoitTheme(theme);
		}
	}

	// Contact Form state management (Svelte 5 runes)
	let formName = $state('');
	let formEmail = $state('');
	let formDesc = $state('');
	let formSubmitted = $state(false);

	function handleFormSubmit(e: Event) {
		e.preventDefault();
		if (formName && formEmail) {
			formSubmitted = true;
		}
	}
</script>

<div 
	onmousemove={handleMouseMove}
	onmouseleave={handleMouseLeave}
	role="none"
	style="--x: {x}px; --y: {y}px;"
	class="min-h-screen bg-bg-primary bg-grid-blueprint relative flex flex-col selection:bg-primary selection:text-on-primary transition-colors duration-400 font-sans"
>
	<!-- Subtle Atmospheric Glows -->
	{#if isMouseInWindow}
		<div class="fixed inset-0 pointer-events-none z-0 radial-glow-mint transition-opacity duration-300"></div>
		<div class="fixed inset-0 pointer-events-none z-0 radial-glow-cyan transition-opacity duration-300"></div>
	{:else}
		<!-- Default static ambient illumination -->
		<div class="absolute top-[20%] left-[10%] w-[500px] h-[500px] rounded-full pointer-events-none z-0 bg-primary/3 blur-[120px]"></div>
		<div class="absolute bottom-[20%] right-[10%] w-[600px] h-[600px] rounded-full pointer-events-none z-0 bg-tertiary/2 blur-[140px]"></div>
	{/if}

	<!-- Header / Navigation Bar -->
	<header class="sticky top-0 z-50 bg-bg-primary/80 backdrop-blur-md border-b border-border-grid px-6 py-5 transition-colors duration-400">
		<div class="max-w-7xl mx-auto flex items-center justify-between">
			<!-- Logo -->
			<a href="#home" class="flex items-center gap-2 group">
				<span class="font-heading text-2xl font-bold tracking-tight text-text-main transition-colors duration-300">
					stereo<span class="text-primary group-hover:text-tertiary transition-colors duration-300">IT</span>
				</span>
				<span class="w-1.5 h-1.5 bg-primary rounded-full animate-pulse shadow-[0_0_8px_rgba(167,109,83,0.8)]"></span>
			</a>

			<!-- Desktop Nav Links -->
			<nav class="hidden md:flex items-center gap-8 text-[11px] font-mono tracking-widest">
				<a 
					href="#philosophy" 
					class="text-text-body hover:text-text-main transition-colors duration-300 flex items-center gap-1.5"
				>
					<span class="text-primary text-[10px]">01//</span> PHILOSOPHY
				</a>
				<a 
					href="#capabilities" 
					class="text-text-body hover:text-text-main transition-colors duration-300 flex items-center gap-1.5"
				>
					<span class="text-primary text-[10px]">02//</span> CAPABILITIES
				</a>
				<a 
					href="#architecture" 
					class="text-text-body hover:text-text-main transition-colors duration-300 flex items-center gap-1.5"
				>
					<span class="text-primary text-[10px]">03//</span> TRUE ARCHITECTURE
				</a>
				<a 
					href="/storybook" 
					class="text-text-body hover:text-text-main transition-colors duration-300 flex items-center gap-1.5"
				>
					<span class="text-primary text-[10px]">04//</span> STORYBOOK
				</a>
			</nav>

			<!-- Contact Button -->
			<a 
				href="#contact" 
				class="px-5 py-2.5 rounded bg-primary text-on-primary text-xs font-mono tracking-widest uppercase hover:bg-text-main hover:text-bg-primary transition-all duration-300 shadow-sm"
			>
				Book a Session
			</a>
		</div>
	</header>

	<!-- Main Layout Container -->
	<main class="flex-grow z-10">
		<!-- HERO SECTION -->
		<section id="home" class="max-w-7xl mx-auto px-6 pt-20 pb-28 md:pt-32 md:pb-40 flex flex-col gap-12 border-b border-border-grid transition-colors duration-400">
			<!-- Monospace Section Indicator -->
			<div class="flex items-center gap-3 font-mono text-[10px] text-primary tracking-widest uppercase">
				<span class="px-2 py-0.5 rounded border border-primary/20 bg-primary/5">EST. 2024 // PRAGUE</span>
				<span>[ ARCHITECTURAL_INTEGRITY ]</span>
			</div>

			<!-- Main Heading Area -->
			<div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
				<div class="lg:col-span-8 flex flex-col gap-8 text-left">
					<h1 class="text-4xl sm:text-6xl lg:text-7xl font-light tracking-tight text-text-main leading-[1.08] font-serif transition-colors duration-400">
						Architects of <br class="hidden sm:inline" />
						<span class="text-primary italic font-medium">Enduring</span> Digital Infrastructure.
					</h1>
					<p class="text-lg text-text-body font-light max-w-2xl leading-relaxed transition-colors duration-400">
						We design, build, and consult on complex technical structures that stand the test of scale. Bringing rigorous engineering principles, human cohesion, and meticulous craftsmanship to high-stakes codebases.
					</p>
					
					<div class="flex flex-wrap gap-4 mt-4">
						<a 
							href="#contact" 
							class="px-8 py-4 bg-primary text-on-primary font-bold text-sm tracking-wide rounded hover:bg-text-main hover:text-bg-primary transition-all duration-300 text-center shadow-md"
						>
							Connect with Our Craftsmen
						</a>
						<a 
							href="#philosophy" 
							class="px-8 py-4 border border-border-grid bg-bg-secondary/40 text-text-main font-semibold text-sm tracking-wide rounded hover:bg-bg-secondary/80 transition-all duration-300 text-center"
						>
							Our Story
						</a>
					</div>
				</div>

				<!-- Asymmetric Blueprint Wireframe Graphics (Architectural Draft lines) -->
				<div class="lg:col-span-4 hidden lg:flex flex-col items-center justify-center h-80 relative border border-dashed border-border-grid rounded-xl bg-bg-secondary/10">
					<div class="absolute inset-0 bg-grid-blueprint opacity-60"></div>
					<div class="border border-border-grid p-6 bg-bg-secondary rounded-lg z-10 w-72 text-left shadow-sm">
						<span class="text-[9px] font-mono text-primary block mb-1">[ SYSTEM_MODEL_A ]</span>
						<p class="text-sm font-semibold text-text-main mb-3 font-heading">Structural Blueprint</p>
						<div class="space-y-2">
							<div class="h-1.5 w-full bg-border-grid rounded overflow-hidden">
								<div class="w-4/5 h-full bg-primary"></div>
							</div>
							<div class="h-1.5 w-full bg-border-grid rounded overflow-hidden">
								<div class="w-3/5 h-full bg-tertiary"></div>
							</div>
							<div class="h-1.5 w-full bg-border-grid rounded overflow-hidden">
								<div class="w-1/2 h-full bg-secondary"></div>
							</div>
						</div>
					</div>
					<span class="absolute bottom-4 right-4 font-mono text-[9px] text-text-body/30 tracking-widest">SCALE 1:1</span>
				</div>
			</div>
		</section>

		<!-- SECTION 01: THE TRUTH & THE HOOK (FAST, GOOD, CHEAP) -->
		<section id="philosophy" class="max-w-7xl mx-auto px-6 py-20 md:py-32 border-b border-border-grid transition-colors duration-400">
			<div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
				<!-- Text Description -->
				<div class="lg:col-span-7 flex flex-col gap-6 text-left">
					<div class="font-mono text-[10px] text-primary tracking-widest uppercase">
						[ 01 // THE TRUTH ]
					</div>
					<h2 class="text-3xl sm:text-5xl font-bold tracking-tight text-text-main transition-colors duration-300">
						Fast. Good. Cheap.<br />
						<span class="text-primary italic font-serif font-light">You can only choose two.</span>
					</h2>
					<div class="text-text-body text-base font-light space-y-4 leading-relaxed max-w-xl">
						<p>
							In modern software development, everyone promises all three. But as a leader, you already know the truth: rushing leads to fragile code, and cutting corners creates structural debt that you will pay for with compounding interest later.
						</p>
						<p>
							At <span class="text-text-main font-semibold">stereoIT</span>, we do not build fragile systems, and we do not rush foundations. We stand firmly for <span class="text-primary font-bold">Quality and Longevity</span>.
						</p>
						<p>
							Because enduring software is not an accident of speed—it is a result of deliberate, meticulous craftsmanship. We build digital systems with the same care, planning, and rigor that master architects use to build physical monuments.
						</p>
					</div>
				</div>

				<!-- INFOGRAPHIC 01: THE PROJECT TRIANGLE -->
				<div class="lg:col-span-5 flex justify-center">
					<div class="border border-border-grid bg-card-bg rounded-xl p-8 w-full max-w-md relative overflow-hidden backdrop-blur-sm shadow-sm text-center">
						<div class="font-mono text-[9px] text-text-body/40 absolute top-4 right-4 tracking-widest">INFOGRAPHIC_01</div>
						<h3 class="text-sm font-semibold text-text-main font-mono tracking-wider mb-8">[ THE_COMPROMISE_MATRIX ]</h3>
						
						<!-- CSS Triangle Container -->
						<div class="relative w-64 h-64 mx-auto flex items-center justify-center">
							<!-- Infinite Grid Lines background -->
							<div class="absolute inset-0 bg-grid-blueprint opacity-20"></div>

							<!-- SVG Triangle Path -->
							<svg class="absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 256 256">
								<polygon points="128,40 40,190 216,190" fill="none" stroke="currentColor" class="text-border-grid" stroke-width="2" />
								<!-- Overlap highlight -->
								<polygon points="128,40 128,115 216,190" fill="rgba(167, 109, 83, 0.1)" stroke="none" />
							</svg>

							<!-- Vertices Labels -->
							<div class="absolute top-2 left-1/2 -translate-x-1/2 font-mono text-[11px] text-text-main font-bold uppercase tracking-wider">
								FAST
							</div>
							<div class="absolute bottom-10 left-2 font-mono text-[11px] text-text-main font-bold uppercase tracking-wider">
								CHEAP
							</div>
							<div class="absolute bottom-10 right-2 font-mono text-[11px] text-text-main font-bold uppercase tracking-wider">
								GOOD
							</div>

							<!-- Intersection Highlights -->
							<!-- Fast & Cheap Overlap -->
							<div class="absolute top-36 left-12 w-20 text-center font-sans">
								<span class="text-[9px] font-mono text-text-body/60 uppercase block">FAST + CHEAP</span>
								<span class="text-[10px] text-zinc-500 font-semibold block leading-tight">Fragile Debt</span>
							</div>

							<!-- Good & Cheap Overlap -->
							<div class="absolute top-36 right-12 w-20 text-center font-sans">
								<span class="text-[9px] font-mono text-text-body/60 uppercase block">GOOD + CHEAP</span>
								<span class="text-[10px] text-zinc-400 font-bold block leading-tight">The Myth</span>
							</div>

							<!-- stereoIT Path Overlap -->
							<div class="absolute top-16 left-1/2 -translate-x-1/2 w-32 text-center p-2 rounded bg-primary/10 border border-primary/20 z-10">
								<span class="text-[9px] font-mono text-primary font-bold uppercase tracking-widest block">FAST + GOOD</span>
								<span class="text-xs text-primary font-bold block leading-none mt-1">stereoIT Quality</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>

		<!-- SECTION 02: THE CORE DUAL-MASTERY (WHAT WE DO) -->
		<section id="capabilities" class="max-w-7xl mx-auto px-6 py-20 md:py-32 border-b border-border-grid transition-colors duration-400">
			<!-- Section header -->
			<div class="flex flex-col gap-4 mb-16 text-left">
				<div class="font-mono text-[10px] text-primary tracking-widest uppercase">
					[ 02 // CAPABILITIES ]
				</div>
				<h2 class="text-3xl sm:text-5xl font-light tracking-tight text-text-main font-serif transition-colors duration-400">
					We Restore. We Create. <span class="text-primary italic font-medium">We Build to Last.</span>
				</h2>
				<p class="text-text-body max-w-2xl text-base font-light transition-colors duration-400 leading-relaxed">
					Whether you need to carefully restore a historic system or lay the first brick on pristine land, we bring the elite expertise required to build structures that endure.
				</p>
			</div>

			<!-- Grid layouts -->
			<div class="grid grid-cols-1 md:grid-cols-2 gap-10 text-left">
				
				<!-- Greenfield Architecture Panel -->
				<div class="group border border-border-grid bg-card-bg rounded-xl p-8 relative overflow-hidden backdrop-blur-sm hover:border-primary/40 hover:bg-bg-secondary/40 transition-all duration-300 flex flex-col justify-between min-h-[360px]">
					<div class="absolute inset-0 bg-gradient-to-tr from-primary/3 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
					
					<div>
						<div class="flex items-center justify-between mb-8">
							<span class="font-mono text-xs text-primary font-semibold tracking-widest">[ CORE_CREATE ]</span>
							<span class="font-mono text-xl font-bold text-text-body/20 group-hover:text-primary/30 transition-colors duration-300">//01</span>
						</div>
						<h3 class="text-2xl font-bold text-text-main mb-4 group-hover:text-primary transition-colors duration-300">
							Greenfield Architecture
						</h3>
						<p class="text-text-body leading-relaxed text-sm font-light transition-colors duration-400">
							Starting a new, high-stakes system is a rare opportunity to do it right. We design clean, modular, and pristine digital architectures. We plan for your 10-year growth on day one, ensuring your software is adaptable, secure, and ready to scale without structural cracking.
						</p>
					</div>

					<!-- Svelte Tags block -->
					<div class="mt-8 flex flex-wrap gap-2 text-[9px] font-mono text-text-body">
						<span class="px-2 py-0.5 border border-border-grid bg-bg-secondary/50 rounded">DOMAIN_DRIVEN_DDD</span>
						<span class="px-2 py-0.5 border border-border-grid bg-bg-secondary/50 rounded">MICROSERVICES</span>
						<span class="px-2 py-0.5 border border-border-grid bg-bg-secondary/50 rounded">HIGH_THROUGHPUT_APIS</span>
					</div>
				</div>

				<!-- Legacy Restoration Panel -->
				<div class="group border border-border-grid bg-card-bg rounded-xl p-8 relative overflow-hidden backdrop-blur-sm hover:border-primary/40 hover:bg-bg-secondary/40 transition-all duration-300 flex flex-col justify-between min-h-[360px]">
					<div class="absolute inset-0 bg-gradient-to-tr from-primary/3 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
					
					<div>
						<div class="flex items-center justify-between mb-8">
							<span class="font-mono text-xs text-primary font-semibold tracking-widest">[ CORE_RESTORE ]</span>
							<span class="font-mono text-xl font-bold text-text-body/20 group-hover:text-primary/30 transition-colors duration-300">//02</span>
						</div>
						<h3 class="text-2xl font-bold text-text-main mb-4 group-hover:text-primary transition-colors duration-300">
							Legacy Restoration
						</h3>
						<p class="text-text-body leading-relaxed text-sm font-light transition-colors duration-400">
							Some of the most valuable software systems are like historical castles—beautiful and critical to your business, but heavy and fragile to change. We carefully restore, refactor, and stabilize legacy systems without halting your active business operations, turning monoliths into modular assets.
						</p>
					</div>

					<!-- Svelte Tags block -->
					<div class="mt-8 flex flex-wrap gap-2 text-[9px] font-mono text-text-body">
						<span class="px-2 py-0.5 border border-border-grid bg-bg-secondary/50 rounded">STRANGLER_FIG</span>
						<span class="px-2 py-0.5 border border-border-grid bg-bg-secondary/50 rounded">TEST_INJECTION</span>
						<span class="px-2 py-0.5 border border-border-grid bg-bg-secondary/50 rounded">ZERO_DOWNTIME_EVOLUTION</span>
					</div>
				</div>

			</div>
		</section>

		<!-- SECTION 03: TRUE ARCHITECTURE (UNCLE BOB QUOTE & 4 PILLARS) -->
		<section id="architecture" class="max-w-7xl mx-auto px-6 py-20 md:py-32 border-b border-border-grid transition-colors duration-400">
			<div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">
				
				<!-- INFOGRAPHIC 02: 4 PILLARS FLOORPLAN -->
				<div class="lg:col-span-5 order-2 lg:order-1 flex justify-center">
					<div class="border border-border-grid bg-card-bg rounded-xl p-8 w-full max-w-md relative overflow-hidden backdrop-blur-sm shadow-sm text-left">
						<div class="font-mono text-[9px] text-text-body/40 absolute top-4 right-4 tracking-widest">INFOGRAPHIC_02</div>
						<h3 class="text-xs font-semibold text-text-main font-mono tracking-wider mb-8">[ THE_PILLARS_FLOORPLAN ]</h3>

						<!-- Asymmetrical 2x2 grid representing the floorplan rooms -->
						<div class="grid grid-cols-2 gap-4 relative">
							<!-- Room 1: Code -->
							<div class="border border-border-grid p-4 rounded bg-bg-primary/20 flex flex-col justify-between h-28 relative">
								<span class="font-mono text-[9px] text-primary">ROOM 01 //</span>
								<h4 class="text-xs font-bold text-text-main font-heading uppercase leading-tight">Code Quality</h4>
							</div>
							
							<!-- Room 2: People -->
							<div class="border border-border-grid p-4 rounded bg-bg-primary/20 flex flex-col justify-between h-28 relative">
								<span class="font-mono text-[9px] text-primary">ROOM 02 //</span>
								<h4 class="text-xs font-bold text-text-main font-heading uppercase leading-tight">People Dynamics</h4>
							</div>
							
							<!-- Room 3: Org -->
							<div class="border border-border-grid p-4 rounded bg-bg-primary/20 flex flex-col justify-between h-28 relative">
								<span class="font-mono text-[9px] text-primary">ROOM 03 //</span>
								<h4 class="text-xs font-bold text-text-main font-heading uppercase leading-tight">Organization</h4>
							</div>
							
							<!-- Room 4: Prioritization -->
							<div class="border border-border-grid p-4 rounded bg-bg-primary/20 flex flex-col justify-between h-28 relative">
								<span class="font-mono text-[9px] text-primary">ROOM 04 //</span>
								<h4 class="text-xs font-bold text-text-main font-heading uppercase leading-tight">Prioritization</h4>
							</div>

							<!-- Central intersection highlighted in Terracotta -->
							<div class="absolute inset-0 m-auto w-16 h-16 rounded-full bg-primary border-2 border-on-primary flex items-center justify-center shadow-lg text-center p-1 z-10 animate-pulse">
								<span class="font-mono text-[8px] font-bold text-on-primary uppercase leading-tight">DURABLE SYSTEM</span>
							</div>
						</div>
					</div>
				</div>

				<!-- Description Copy & Quote -->
				<div class="lg:col-span-7 order-1 lg:order-2 flex flex-col gap-8 text-left">
					<div class="font-mono text-[10px] text-primary tracking-widest uppercase">
						[ 03 // PHILOSOPHY ]
					</div>
					
					<!-- Quote callout -->
					<div class="border-l-4 border-primary pl-6 py-2">
						<blockquote class="text-xl sm:text-2xl italic font-serif text-text-main font-light leading-relaxed">
							"The goal of software architecture is to minimize the human effort required to build and maintain the required system."
						</blockquote>
						<cite class="text-xs font-mono text-primary tracking-widest uppercase block mt-3">— Robert C. Martin, Clean Architecture</cite>
					</div>

					<h3 class="text-2xl sm:text-3xl font-bold tracking-tight text-text-main font-heading mt-4 transition-colors">
						True Architecture is a Balance.
					</h3>

					<p class="text-text-body text-base font-light leading-relaxed max-w-xl">
						Many view software architecture purely as a technical blueprint of code and databases. We know it is much wider. True architecture is the active synchronization of four pillars: <span class="text-text-main font-semibold">Code, People, Organization, and Prioritization.</span>
					</p>
					<p class="text-text-body text-base font-light leading-relaxed max-w-xl">
						Our mission as craftsmen is to design structures that maintain a healthy balance. We help you maximize delivery today, while ensuring that debugging, spelunking, and technical debt never compound into an organizational tax that freezes your progress tomorrow. We do not just organize your files; we organize your capability to scale.
					</p>
				</div>

			</div>
		</section>

		<!-- SECTION 04: HUMAN CHEMISTRY (COHESIVE TEAMS & LIFECYCLE GRAPH) -->
		<section class="max-w-7xl mx-auto px-6 py-20 md:py-32 border-b border-border-grid transition-colors duration-400">
			<div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
				<!-- Text Description -->
				<div class="lg:col-span-7 flex flex-col gap-6 text-left">
					<div class="font-mono text-[10px] text-primary tracking-widest uppercase">
						[ 04 // TEAM CHEMISTRY ]
					</div>
					<h2 class="text-3xl sm:text-5xl font-bold tracking-tight text-text-main transition-colors duration-300 font-heading">
						Cohesive Teams > Solo Geniuses
					</h2>
					<div class="text-text-body text-base font-light space-y-4 leading-relaxed max-w-xl">
						<p>
							A house is not built by a collection of isolated specialists who do not talk to each other. It is built by a synchronized guild.
						</p>
						<p>
							We believe that a synchronized, battle-tested team will always outperform a disjointed group of solo engineers, no matter how skilled the individuals. Building high-performing chemistry takes years. We bring you that collective force and proven cooperation on day one.
						</p>
						<p class="font-semibold text-text-main mt-4">
							Our Human Principles:
						</p>
						<ul class="space-y-3 font-light text-sm pl-4 list-disc border-l-2 border-primary/30">
							<li><strong class="text-text-main">Servant Leadership:</strong> We do not just write blueprints and walk away. We serve your goals, work shoulder-to-shoulder with your organization, and mentor your internal talent so they can become highly autonomous.</li>
							<li><strong class="text-text-main">Psychological Safety:</strong> We create calm, orderly, and supportive environments. When engineers feel safe and supported, they produce their most rigorous, zero-error work.</li>
						</ul>
					</div>
				</div>

				<!-- INFOGRAPHIC 03: SOFTWARE LIFECYCLE COST GRAPH -->
				<div class="lg:col-span-5 flex justify-center">
					<div class="border border-border-grid bg-card-bg rounded-xl p-8 w-full max-w-md relative overflow-hidden backdrop-blur-sm shadow-sm text-center">
						<div class="font-mono text-[9px] text-text-body/40 absolute top-4 right-4 tracking-widest">INFOGRAPHIC_03</div>
						<h3 class="text-xs font-semibold text-text-main font-mono tracking-wider mb-8">[ SOFTWARE_LIFECYCLE_ROI ]</h3>

						<!-- Coordinate Line Graph in CSS -->
						<div class="relative w-full h-56 border-l border-b border-border-grid font-mono text-[9px] text-text-body/50">
							<!-- Graph background grid -->
							<div class="absolute inset-0 bg-grid-blueprint opacity-10"></div>

							<!-- Axis labels -->
							<span class="absolute bottom-2 right-2 uppercase tracking-widest font-bold">Time</span>
							<span class="absolute top-2 left-2 uppercase tracking-widest font-bold rotate-90 origin-left -translate-y-full ml-1">Cost</span>

							<!-- Graph curves -->
							<svg class="absolute inset-0 w-full h-full" viewBox="0 0 256 160">
								<!-- Hasty Path (Exponential Curve) -->
								<path d="M 0,140 Q 150,135 240,20" fill="none" stroke="#e11d48" stroke-width="2.5" stroke-dasharray="4 4" />
								
								<!-- stereoIT Path (Predictable Flat Line) -->
								<path d="M 0,110 L 256,105" fill="none" stroke="var(--token-color-primary)" stroke-width="3" />
							</svg>

							<!-- Legend / Overlay labels -->
							<div class="absolute top-6 right-2 text-right">
								<span class="text-[8px] font-bold text-red-500 uppercase tracking-wide block">Hasty Path (No Architecture)</span>
								<span class="text-[7px] text-text-body/55 block">Compounding tax freezes progress</span>
							</div>

							<div class="absolute bottom-16 right-2 text-right">
								<span class="text-[8px] font-bold text-primary uppercase tracking-widest block">stereoIT Crafted Path</span>
								<span class="text-[7px] text-text-body/55 block">Linear effort, predictable scale</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>

		<!-- SECTION 05: CONTACT & BLUEPRINTS FORM -->
		<section id="contact" class="max-w-7xl mx-auto px-6 py-20 md:py-32">
			<div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">
				
				<!-- Description details -->
				<div class="lg:col-span-7 flex flex-col gap-8 text-left">
					<div class="font-mono text-[10px] text-primary tracking-widest uppercase">
						[ 05 // CONTACT ]
					</div>
					<h2 class="text-4xl sm:text-6xl font-light tracking-tight text-text-main leading-none font-serif transition-colors duration-400">
						Let’s look at your <span class="text-primary italic font-medium">blueprints.</span>
					</h2>
					<p class="text-text-body text-base font-light max-w-xl leading-relaxed transition-colors duration-400">
						You do not need to commit to a massive, multi-year project today. Let us start with a simple, human conversation. Tell us about the system you want to build, or the one you need to restore. We will review your current structures and help you plan the next phase of your digital house.
					</p>

					<!-- Contact list details -->
					<div class="flex flex-col gap-4 font-mono text-xs tracking-widest uppercase">
						<a 
							href="mailto:info@stereoit.com" 
							class="flex items-center gap-3 text-text-body hover:text-primary transition-colors duration-300"
						>
							<span class="text-primary font-bold">EMAIL:</span> info@stereoit.com
						</a>
						<a 
							href="tel:+420776763478" 
							class="flex items-center gap-3 text-text-body hover:text-primary transition-colors duration-300"
						>
							<span class="text-primary font-bold">PHONE:</span> +420 776 763 478
						</a>
					</div>
				</div>

				<!-- Official intake form -->
				<div class="lg:col-span-5 border border-border-grid bg-card-bg rounded-xl p-8 text-left relative overflow-hidden backdrop-blur-sm shadow-sm transition-colors duration-400">
					<div class="absolute top-0 right-0 w-[120px] h-[120px] bg-primary/5 rounded-full blur-[30px] pointer-events-none"></div>

					{#if formSubmitted}
						<!-- Success feedback state -->
						<div class="py-12 text-center flex flex-col items-center gap-4 animate-fadeIn">
							<div class="w-12 h-12 rounded-full bg-primary/10 border border-primary/30 flex items-center justify-center font-mono text-xl text-primary font-bold">
								✓
							</div>
							<h3 class="text-xl font-bold font-heading text-text-main">Blueprint Received</h3>
							<p class="text-text-body text-xs font-light leading-relaxed max-w-xs mx-auto">
								Thank you. One of our master builders will review your description and get in touch with you shortly to schedule a conversation.
							</p>
							<button 
								onclick={() => formSubmitted = false}
								class="mt-4 font-mono text-[10px] text-primary uppercase border-b border-primary/20 pb-0.5 hover:text-text-main hover:border-text-main transition-all duration-300"
							>
								Submit Another Blueprint
							</button>
						</div>
					{:else}
						<form onsubmit={handleFormSubmit} class="space-y-6">
							<div class="border-b border-border-grid pb-4 mb-4">
								<span class="text-[9px] font-mono text-primary tracking-wider uppercase block mb-1">INTAKE_Blueprints</span>
								<h3 class="text-lg font-bold text-text-main font-heading leading-tight">Review Your Digital House</h3>
							</div>

							<!-- Inputs fields -->
							<div class="flex flex-col gap-4 text-xs font-mono">
								<div>
									<label for="name" class="block text-[9px] text-text-body/60 uppercase tracking-widest mb-1.5">Full Name</label>
									<input 
										type="text" 
										id="name"
										bind:value={formName}
										placeholder="e.g. Robert Smol" 
										required
										class="w-full bg-bg-primary/50 border border-border-grid rounded px-4 py-3 text-text-main placeholder-text-body/30 focus:border-primary focus:ring-0 transition-all duration-300"
									/>
								</div>

								<div>
									<label for="email" class="block text-[9px] text-text-body/60 uppercase tracking-widest mb-1.5">Email Address</label>
									<input 
										type="email" 
										id="email"
										bind:value={formEmail}
										placeholder="e.g. robert.smol@stereoit.com" 
										required
										class="w-full bg-bg-primary/50 border border-border-grid rounded px-4 py-3 text-text-main placeholder-text-body/30 focus:border-primary focus:ring-0 transition-all duration-300"
									/>
								</div>

								<div>
									<label for="desc" class="block text-[9px] text-text-body/60 uppercase tracking-widest mb-1.5">System Description</label>
									<textarea 
										id="desc"
										bind:value={formDesc}
										placeholder="Tell us about the digital system you want to build, or the legacy structures you need to restore..." 
										rows="4"
										class="w-full bg-bg-primary/50 border border-border-grid rounded px-4 py-3 text-text-main placeholder-text-body/30 focus:border-primary focus:ring-0 transition-all duration-300 resize-none font-sans"
									></textarea>
								</div>
							</div>

							<!-- Submit Trigger -->
							<button 
								type="submit"
								class="w-full py-3.5 rounded bg-primary text-on-primary font-mono text-xs font-bold tracking-widest uppercase hover:bg-text-main hover:text-bg-primary transition-all duration-300 shadow-sm"
							>
								Submit Blueprints
							</button>
						</form>
					{/if}
				</div>
			</div>
		</section>
	</main>

	<!-- Footer -->
	<footer class="border-t border-border-grid py-12 px-6 mt-auto transition-colors duration-400">
		<div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-8 text-xs font-mono text-text-body/60">
			<div class="flex flex-col gap-1 text-center md:text-left">
				<div>
					&copy; {new Date().getFullYear()} stereoIT s.r.o. All rights reserved.
				</div>
				<div class="text-[10px] text-text-body/40">
					Proud Software Craftsmen | Prague, Czech Republic
				</div>
			</div>

			<!-- Theme Segmented Toggle Widget (Dynamic context router) -->
			<div class="flex flex-col items-center gap-2">
				<span class="text-[9px] text-text-body/45 tracking-widest uppercase">ACTIVE_THEME</span>
				<div class="flex items-center rounded border border-border-grid bg-bg-secondary p-0.5 transition-colors duration-300">
					<button 
						onclick={() => selectTheme('system')}
						class="px-3 py-1.5 rounded text-[9px] tracking-wider transition-all duration-300 {activeTheme === 'system' ? 'bg-primary text-on-primary font-bold shadow-sm' : 'text-text-body hover:text-white'}"
					>
						AUTO
					</button>
					<button 
						onclick={() => selectTheme('option-a')}
						class="px-3 py-1.5 rounded text-[9px] tracking-wider transition-all duration-300 {activeTheme === 'option-a' ? 'bg-primary text-on-primary font-bold shadow-sm' : 'text-text-body hover:text-white'}"
					>
						DARK SAGE
					</button>
					<button 
						onclick={() => selectTheme('option-b')}
						class="px-3 py-1.5 rounded text-[9px] tracking-wider transition-all duration-300 {activeTheme === 'option-b' ? 'bg-primary text-on-primary font-bold shadow-md' : 'text-text-body hover:text-white'}"
					>
						TERRACOTTA
					</button>
				</div>
			</div>

			<div class="flex gap-6">
				<a href="#philosophy" class="hover:text-text-main transition-colors duration-300">PHILOSOPHY</a>
				<a href="#capabilities" class="hover:text-text-main transition-colors duration-300">CAPABILITIES</a>
				<a href="#contact" class="hover:text-text-main transition-colors duration-300">CONTACT</a>
			</div>
		</div>
	</footer>
</div>
