# stereoIT s.r.o. — Technology Stack Specifications

## 1. Frontend Framework
- **Framework**: **SvelteKit** (using Svelte 5 Runes)
  - *Reactivity Model*: Native Svelte 5 Runes (`$state`, `$derived`, `$effect`) for high performance and lightweight bundle size.
  - *Styling*: **Tailwind CSS** mapped directly to our graphic tokens.
  - *Animation*: **Svelte-Transitions** or **Motion One** for smooth animations.

## 2. Component System
- **UI Framework**: **shadcn-svelte**
  - Fully accessible, unstyled Radix Svelte primitives customized using our custom design tokens.

## 3. Rendering & Hosting Architecture
- **Rendering Strategy**: **SSG (Static Site Generation)** — Pre-rendering all pages at compile-time to guarantee static assets are served directly from edge locations.
- **CDN**: **Cloudflare Edge** — Global distribution with near-zero latency.
