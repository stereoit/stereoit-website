# stereoIT s.r.o. — Design System & Visual Guidelines

Inspired by the clean, immersive, and high-tech experience of Google Antigravity.

## 1. Brand Essence
- **Core Theme**: Cyber-Minimalism, Deep Architectural Precision, and Absolute Engineering Competency.
- **Atmosphere**: Deep, focused, immersive, and trust-inspiring.

## 2. Color Palette (Obsidian & Cyber-Emerald)
- **Primary Background**: `#080809` (Obsidian Black) — Pitch black base.
- **Secondary Background**: `#121214` (Deep Charcoal) — Panel/Card surfaces.
- **Primary Accent**: `#00F5A0` (Cyber Mint / Electric Emerald) — Primary glow, CTA hovers, active elements.
- **Secondary Accent**: `#00E5FF` (Laser Cyan) — Support accent for gradients and status lights.
- **Text & Borders**:
  - Main Text: `#FFFFFF` (Pure White) — Crisp headings.
  - Body Text: `#94A3B8` (Muted Slate) — Ultra-readable copy.
  - Accent/Label Text: `#00F5A0` (Cyber Mint) — Small tech labels.
  - Borders/Grids: `#1E293B` (Dark Slate, 40-60% opacity) — Layout structures.

## 3. Typography
- **Headings (Display/H1/H2)**: `Space Grotesk` or `Geist Sans`
  - *Details*: Tight tracking, bold, ultra-clean geometric sans-serif.
- **Technical/Mono**: `Geist Mono` or `JetBrains Mono`
  - *Details*: Small uppercase tags, indexes, metrics, code decorators (e.g., `[01 // COHESION]`).
- **Body Text**: `Inter` or `Geist Sans` (Light/Regular weights)
  - *Details*: Excellent legibility at all resolutions.

## 4. Design & Graphical Tokens
Our design tokens act as the single source of truth for the styling layer, declared via CSS Custom Properties:

```css
:root {
  --token-color-bg-primary: #080809;
  --token-color-bg-secondary: #121214;
  --token-color-accent-primary: #00F5A0;
  --token-color-accent-secondary: #00E5FF;
  --token-font-heading: 'Space Grotesk', sans-serif;
  --token-font-body: 'Inter', sans-serif;
  --token-grid-thickness: 1px;
  --token-grid-color: rgba(30, 41, 59, 0.4);
}
```

## 5. Layout & Interaction Signature
- **Architectural Grid Layout**: Subtle, semi-transparent background lines resembling a blueprint.
- **Illumination & Depth**: Soft radial gradient background glows (`#00F5A0` and `#00E5FF` at `5% - 10%` opacity).
- **Micro-interactions & Physics**: Magnetic buttons, viewport-reveal animations, and interactive cursor-magnetic elements.
