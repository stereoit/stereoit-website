---
name: stereoIT Architectural Studio
colors:
  # Official Primary Theme — Option B: The Master Craftsman (Gallery Alabaster & Raw Terracotta)
  background: '#FAF9F6'
  on-background: '#1C1917'
  surface: '#F5F5F4'
  surface-dim: '#E7E5E4'
  surface-bright: '#FAFAFA'
  surface-container-lowest: '#FFFFFF'
  surface-container-low: '#F5F5F4'
  surface-container: '#FAF9F6'
  surface-container-high: '#E7E5E4'
  surface-container-highest: '#D6D3D1'
  on-surface: '#44403C'
  on-surface-variant: '#78716C'
  outline: 'rgba(226, 232, 240, 0.95)'
  outline-variant: 'rgba(212, 212, 216, 0.6)'
  primary: '#A76D53'
  on-primary: '#FAF9F6'
  primary-container: '#F5EBE6'
  on-primary-container: '#6E3E2B'
  secondary: '#64748B'
  on-secondary: '#FAF9F6'
  secondary-container: '#F1F5F9'
  on-secondary-container: '#1E293B'
  tertiary: '#7E8F7C'
  on-tertiary: '#FAF9F6'
  tertiary-container: '#EAECE9'
  on-tertiary-container: '#2C3C2A'
  error: '#BA1A1A'
  on-error: '#FFFFFF'
  error-container: '#FFDAD6'
  on-error-container: '#410002'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 56px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '300'
    lineHeight: '1.7'
    letterSpacing: 0.015em
  mono-label:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 24px
  grid-overlay-size: 60px
---

# stereoIT s.r.o. -- Design System and Visual Guidelines

This document outlines the transition of stereoIT's brand from high-tech cyberpunk terminal aesthetics to a calm, highly-structured "Architectural Studio" design language. 

The official, primary visual direction of stereoIT is established as Option B: The Master Craftsman.

---

## 1. Brand Essence, Atmosphere and Color Psychology
*   Official Visual Direction: Option B -- Spacious Light (The Master Craftsman).
*   Core Metaphor: The Master Craftsman. We reject cold corporate machinery and high-velocity start-up noise. Instead, we view software engineering as a physical, enduring craft. We build digital systems with the same care, planning, and rigor that master architects use to build physical monuments.
*   Atmosphere: Calming, sophisticated, spacious, and trust-inspiring.
*   Layout Philosophy: Asymmetric balance, extensive whitespace (letting the layout "breathe"), thin structural grid lines (2% to 5% opacity), and minimal elevation.
*   Color Psychology and Reasoning:
    *   Gallery Alabaster (#FAF9F6): Represents absolute clarity, spaciousness, and room to breathe. It evokes the feeling of entering a well-designed, pristine gallery space where every element is intentional.
    *   Raw Terracotta (#A76D53): Terracotta is the color of clay, raw bricks, and ancient foundations. It shifts the perception of software from "virtual code" to "solid, physical construction." Psychologically, its earthy warmth conveys approachable human connection, grounding, and organic endurance. This perfectly reinforces stereoIT's commitment to human cohesion, psychological safety, and servant leadership -- we are proud, supportive craftsmen.
    *   Slate and Concrete (#64748B / #F5F5F4): Serves as the structural slate that grounds the design, representing raw engineering precision and systematic order.

---

## 2. Design Language Level 1: Color Token Matrices
We have defined our primary color mappings matching the "Architectural Studio" aesthetic, conforming to the Google Stitch + Material Design 3 schema.

### Primary Theme: Spacious Light (Gallery Alabaster and Raw Clay)
A light-flooded, airy, museum-gallery layout reflecting absolute structural clarity and tactile craftsmanship.

| Token | CSS Custom Property | Value (HEX) | Role / Application |
| :--- | :--- | :--- | :--- |
| Primary | --token-color-primary | #A76D53 | Raw Clay / Terracotta: Brand accents and interactive highlights |
| On-Primary | --token-color-on-primary | #FAF9F6 | Off-white text on top of Terracotta |
| Primary Container | --token-color-primary-container | #F5EBE6 | Warm sand/terracotta tint for highlight panels |
| On-Primary Container | --token-color-on-primary-container | #6E3E2B | Dark terracotta-brown text on top of Primary Container |
| Secondary | --token-color-secondary | #64748B | Slate Blue / Grey: Structural labels and secondary copy |
| On-Secondary | --token-color-on-secondary | #FAF9F6 | Soft off-white text on top of Secondary surfaces |
| Secondary Container | --token-color-secondary-container | #F1F5F9 | Warm white-grey panel for secondary blocks |
| On-Secondary Container | --token-color-on-secondary-container | #1E293B | Deep slate-dark text on secondary containers |
| Tertiary | --token-color-tertiary | #7E8F7C | Mineral Sage: Secondary green accent for tags / stats |
| On-Tertiary | --token-color-on-tertiary | #FAF9F6 | Off-white text on top of Mineral Sage |
| Background | --token-color-bg-primary | #FAF9F6 | Gallery Alabaster: Main crisp off-white background |
| On-Background | --token-color-text-main | #1C1917 | Raw Graphite dark headings and title cards |
| Surface | --token-color-bg-secondary | #F5F5F4 | Light concrete/stone panel surfaces |
| On-Surface | --token-color-text-body | #44403C | Muted dark-stone color for standard paragraph copy |
| Border / Grid | --token-color-border-grid | rgba(226, 232, 240, 0.95) | Soft slate lines representing grid blueprint lines |

---

## 3. Typography Scale
To represent precise craftsmanship and intellectual consulting, the typography is highly structured and spaced.

*   Display Title (Hero Heading)
    *   Primary Archetype: Playfair Display (Light/Medium weight, tight line-height). Represents heritage, wisdom, craftsmanship, and prestige.
*   Section Headers (H2/H3)
    *   Space Grotesk or Geist Sans (Medium/Regular weight, tracked tight, clean geometric endings).
*   Body Copy (Readability)
    *   Inter (Light, line-height: 1.7, letter-spacing: 0.015em). Optimized for dense paragraphs and descriptions.
*   Technical / Blueprint Metadata Labels
    *   JetBrains Mono or Geist Mono (Small size: 10px-11px, text-transform: uppercase, letter-spacing: 0.15em). Used for numbering, scale markers, and small tech-badges (e.g., SCALE 1:1, DETAIL_A // COHESION).

---

## 4. Architectural Elements and UI Signatures
*   Drafting Grids: The background is covered in a delicate, infinite background grid (repeating 60px by 60px) utilizing var(--token-color-border-grid) lines.
*   The Blueprint Frame: Layout blocks are explicitly bounded by ultra-thin borders resembling structural blueprints. Instead of card blocks with thick drop-shadows, UI modules use clean framing lines.
*   Asymmetry and Blank Space: One-third of major rows is intentionally left as white/empty space to mimic the layout of modern architectural blueprint boards.
*   Atmospheric Illumination: Gentle soft-shading and light concrete/stone surface structures, mimicking natural side-lighting in a concrete craftsman studio.
