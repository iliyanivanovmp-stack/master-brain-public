# AI Essentials — Brand Style Reference

> Drop this file into any agent context to design on-brand. Do not deviate from these values without explicit instruction.

---

## Colors

### Named Brand Palette (Tailwind tokens)

| Token | Hex | Use |
|---|---|---|
| `ink` | `#0E0E0D` | Primary text, dark backgrounds, CTA buttons |
| `snow` | `#F8F8F7` | Light background tint, hover fills on nav |
| `brand-border` | `#E6E4E1` | All borders on light surfaces, card dividers |
| `mute` | `#929090` | Secondary / label text, captions |
| `purple` | `#6D0ABD` | Primary brand accent — hero italic, links, blockquote accents |
| `blue` | `#1F8CD7` | Secondary accent — section labels, stats, highlights |
| `orange` | `#F97316` | Tertiary accent — emphasis words, gradient ends |

### Surface Colors

| Surface | Value |
|---|---|
| Page background | `#ffffff` |
| Dark footer / reverse sections | `#0E0E0D` (ink) |
| Glassmorphic nav (idle) | `rgba(255,255,255,0.70)` + `backdrop-blur-xl` |
| Glassmorphic nav (scrolled) | `rgba(255,255,255,0.90)` + `backdrop-blur-2xl` |
| Card / panel | `#ffffff` with `border: 1px solid #E6E4E1` |
| Modal overlay | `rgba(0,0,0,0.60)` + `backdrop-blur-sm` |

### Body Text Colors

| Role | Value |
|---|---|
| Primary body copy | `#5E5C5A` |
| Secondary / lighter body | `#707070` |
| Muted / captions | `#929090` |
| On-dark text | `rgba(255,255,255,0.60)` for nav links; `rgba(255,255,255,0.25)` for copyright |

### Accent Gradients

```css
/* Blue-to-orange gradient bar — decorative accent line */
background: linear-gradient(to bottom, #1F8CD7, #F97316);

/* Blue-tinted panel background */
background: linear-gradient(to bottom, rgba(31,140,215,0.04), rgba(249,115,22,0.04));

/* Hero blob 1 (purple, top-right) */
background: radial-gradient(circle, rgba(109,10,189,0.07) 0%, transparent 70%);
filter: blur(90px);

/* Hero blob 2 (blue, bottom-left) */
background: radial-gradient(circle, rgba(31,140,215,0.065) 0%, transparent 70%);
filter: blur(90px);

/* Blog blockquote accent */
background: linear-gradient(to right, rgba(109,10,189,0.08), transparent);
border-left: 4px solid #6D0ABD;
```

---

## Typography

### Typeface

**Outfit** — the sole typeface for all text (headlines, body, UI labels).

```css
font-family: 'Outfit', system-ui, sans-serif;
```

- Tailwind tokens: `font-sans`, `font-headline` — both map to Outfit.
- Load via Google Fonts: `Outfit` weights 400, 600, 700, 800, 900.
- Font smoothing: `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;`

### Type Scale

| Element | Size | Weight | Tracking | Line-height | Color |
|---|---|---|---|---|---|
| H1 hero | `clamp(2.52rem, 4.41vw, 3.5rem)` | `font-black` (900) | `-0.03em` | `1.07` | `ink` |
| H2 section | `clamp(2rem, 3.5vw, 3.25rem)` | `font-black` (900) | `-0.035em` | `1.1` | `ink` |
| H3 card title | `1.15rem` | `font-bold` (700) | `-0.03em` | `1.3` | `ink` |
| Body large | `1.1rem` | `400` | — | `1.68` | `#5E5C5A` |
| Body default | `0.875rem` | `400` | — | `1.65` | `#707070` |
| Section label / eyebrow | `0.68–0.7rem` | `font-bold` (700) | `0.1–0.13em` | — | `mute` |
| Nav link | `0.78rem` | `font-semibold` (600) | `0.04em` | — | `ink` (hover: `purple`) |
| CTA button (large) | `1rem` | `font-bold` (700) | `tight` | — | `white` on `ink` |
| CTA button (small) | `0.78rem` | `font-bold` (700) | `tight` | — | `white` on `ink` |
| Stat large | `1.75rem` | `font-black` (900) | `-0.04em` | `1` | `ink` or `blue` |
| Footer nav | `0.65rem` | `font-bold` (700) | `0.12em` | — | `white/60` |
| Caption / reassurance | `0.78rem` | `400` | — | — | `mute` |

### Text Treatment Rules

- Section eyebrows are always **ALL CAPS**, ultra-small, tracked wide, in `mute`.
- Eyebrows are paired with a visual accent: either a `22px × 1.5px` horizontal line in `blue`, or a `7px` breathing dot in `blue`.
- H1/H2 headline italic emphasis uses `<em class="not-italic">` with `text-purple`.
- Blue inline highlight uses inline `style={{ color: '#1F8CD7' }}`.
- Orange inline emphasis uses `style={{ color: 'rgba(249,115,22,0.8)' }}` (slightly softened).

---

## Spacing & Layout

| Token | Value |
|---|---|
| Page max-width | `1400px` (`max-w-[1400px]`) |
| Content max-width (prose/hero) | `672px` (`max-w-[672px]`) |
| Nav max-width | `1080px` |
| Section vertical padding | `py-24` (6rem top/bottom) |
| Section horizontal padding | `px-6 md:px-10` |
| Card internal padding | `p-8` |
| Modal internal padding | `px-6 py-6` |

---

## Border Radius

| Context | Value |
|---|---|
| Base token (`--radius`) | `0.5rem` |
| Cards, modals, nav | `rounded-2xl` (1rem) |
| Buttons (CTA) | `rounded-lg` (0.5rem) |
| Stat chips | `rounded-xl` (0.75rem) |
| Blog blockquote | `0 0.5rem 0.5rem 0` |
| Reassurance bar | `rounded-sm` |

---

## Shadows

| Context | Value |
|---|---|
| Glassmorphic nav (idle) | `0 4px 20px rgba(0,0,0,0.04)` |
| Glassmorphic nav (scrolled) | `0 6px 32px rgba(0,0,0,0.07)` |
| Stat chip / float card | `0 6px 28px rgba(0,0,0,0.055)` |
| Primary CTA button (large) | `0 4px 20px rgba(14,14,13,0.20)` |
| Primary CTA button (small) | `0 2px 12px rgba(14,14,13,0.18)` |
| Mobile dropdown / modal | `0 8px 32px rgba(0,0,0,0.08)` |
| Modal dialog | `shadow-xl` |

---

## Components

### Primary CTA Button

```tsx
// Large (hero)
<a className="inline-flex items-center gap-2.5 bg-ink text-white text-[1rem] font-bold tracking-tight px-9 py-4 rounded-lg shadow-[0_4px_20px_rgba(14,14,13,0.2)]">
  Label <ArrowRight size={16} />
</a>

// Small (header)
<a className="inline-flex items-center gap-1.5 bg-ink text-white text-[0.78rem] font-bold tracking-tight px-4 py-2 rounded-lg shadow-[0_2px_12px_rgba(14,14,13,0.18)]">
  Label
</a>
```

- All external CTAs use `MagneticButton` (physics spring hover: stiffness 180, damping 18, offset factor 0.38).
- External links always get `target="_blank" rel="noopener noreferrer"`.

### Glassmorphic Navigation

```tsx
// Nav bar
className="fixed top-4 ... rounded-2xl border transition-all duration-500"
// Idle:    bg-white/70 backdrop-blur-xl  border-white/80
// Scrolled: bg-white/90 backdrop-blur-2xl border-[#E6E4E1]
```

### Section Eyebrow Pattern

```tsx
// With line
<div className="flex items-center gap-3 mb-7">
  <span className="w-[22px] h-[1.5px] rounded bg-blue" />
  <span className="text-[0.68rem] font-bold tracking-[0.13em] uppercase text-mute">Label</span>
</div>

// With breathing dot
<div className="flex items-center gap-2 mb-9">
  <span className="w-[7px] h-[7px] rounded-full bg-blue animate-breathe" />
  <span className="text-[0.7rem] font-bold tracking-[0.1em] uppercase text-mute">Label</span>
</div>
```

### Card Grid

```tsx
// 3-col grid with hairline dividers (no gap — dividers rendered as bg color)
<div className="grid grid-cols-1 md:grid-cols-3 bg-brand-border rounded-2xl overflow-hidden"
     style={{ gap: '1.5px', border: '1.5px solid #E6E4E1' }}>
  <div className="bg-white p-8">...</div>
</div>
```

### Floating Stat Chip

```tsx
<div className="bg-white border border-brand-border rounded-xl p-5 shadow-[0_6px_28px_rgba(0,0,0,0.055)] animate-float-a hidden xl:block">
  <p className="text-[0.63rem] font-bold tracking-[0.07em] uppercase text-mute mb-1">Label</p>
  <p className="text-[1.75rem] font-black tracking-[-0.04em] leading-none text-ink">Value</p>
  <p className="text-[0.7rem] text-mute mt-1">Subtext</p>
</div>
```

### Accent Divider Bar (blue → orange)

```tsx
<div className="flex items-stretch rounded-sm overflow-hidden"
     style={{ border: '1px solid rgba(31,140,215,0.12)', background: 'linear-gradient(to bottom, rgba(31,140,215,0.04), rgba(249,115,22,0.04))' }}>
  <div className="w-[3px] flex-shrink-0" style={{ background: 'linear-gradient(to bottom, #1F8CD7, #F97316)' }} />
  <p className="text-[0.7rem] font-semibold tracking-[0.1em] uppercase text-mute opacity-70 px-5 py-4">Text</p>
</div>
```

### Footer (dark reverse)

```
bg-ink  |  border-t border-white/[0.07]
Nav links: text-[0.65rem] font-bold tracking-[0.12em] uppercase text-white/60 hover:text-white
Format:  [ Label ]
Copyright: text-[0.72rem] font-bold tracking-[0.08em] uppercase text-white/25
```

### Modal

```tsx
// Overlay
<div className="fixed inset-0 z-[500] flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
// Panel
<div className="bg-white border border-brand-border rounded-2xl max-w-md w-full shadow-xl">
  // Header
  <div className="flex justify-between items-center px-6 py-5 border-b border-brand-border">
    <h2 className="text-xl font-bold text-ink">Title</h2>
    <button className="text-mute hover:text-ink"><X className="w-5 h-5" /></button>
  </div>
  // Body
  <div className="px-6 py-6">...</div>
</div>
```

---

## Animation

### Framer Motion Easing

All motion uses the custom ease `[0.16, 1, 0.3, 1]` — a fast-out, overshoot feel.

```ts
transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
```

### Entry Animations

```ts
// Standard fade-up (section reveals)
initial={{ opacity: 0, y: 22 }}
whileInView={{ opacity: 1, y: 0 }}
viewport={{ once: true, margin: '-60px' }}
transition={{ duration: 0.75, ease: [0.16, 1, 0.3, 1] }}

// Staggered children (hero)
container: { transition: { staggerChildren: 0.12, delayChildren: 0.15 } }
item: { hidden: { opacity: 0, y: 28 }, show: { opacity: 1, y: 0, transition: { duration: 0.8, ease: [0.16, 1, 0.3, 1] } } }
```

### CSS Keyframe Animations (Tailwind tokens)

| Token | Keyframe | Timing |
|---|---|---|
| `animate-breathe` | opacity 1→0.4, scale 1→0.78 | `2.4s ease-in-out infinite` |
| `animate-float-a` | translateY 0→-9px | `3.8s ease-in-out infinite` |
| `animate-float-b` | translateY 0→-9px | `3.8s ease-in-out 1.9s infinite` (offset phase) |
| `animate-spotlight` | opacity 0→1, translate+scale | `2s ease 0.75s 1 forwards` |
| `blobDrift1` | translate + scale drift | `16s ease-in-out infinite` |
| `blobDrift2` | translate + scale drift | `20s ease-in-out infinite` |

### MagneticButton Physics

```ts
// Spring config
useSpring(value, { stiffness: 180, damping: 18 })
// Offset factor: 0.38 of cursor-to-center distance
// On mouse leave: snaps back to 0
// On tap: whileTap={{ scale: 0.975 }}
```

---

## Voice & Messaging Conventions

- Brand name: **AI Essentials** (or **Aiessentials** in legal copy)
- Primary offer label: **Revenue Leak Report** (not "Profit Leak")
- CTA copy pattern: direct, benefit-first — "Get My Free Revenue Leak Report", "Book Free Call"
- Reassurance copy: "Free. 30 minutes. No pitch, no contracts."
- Tone: direct, honest, no hype — "If AI won't help, we will tell you."
- Purple emphasis used for the hook/payoff in headlines (italic `<em>` treatment).

---

## Do's and Don'ts

**Do:**
- Use `ink` for all primary buttons and dark surfaces (never plain black `#000`).
- Use `brand-border` (`#E6E4E1`) for all borders on white backgrounds.
- Pair eyebrows with a `blue` line or dot accent, never standalone.
- Apply the custom ease `[0.16, 1, 0.3, 1]` to all motion.
- Use `rounded-2xl` for cards and panels; `rounded-lg` for buttons only.
- Keep body text at `#5E5C5A` or `#707070` — never pure black on white.

**Don't:**
- Use any font other than Outfit.
- Add colors outside the palette without explicit approval.
- Use box shadows heavier than `0_8px_32px_rgba(0,0,0,0.08)`.
- Use green, red, or yellow as accent colors (reserved for system states only).
- Apply `bg-ink` to anything other than footer, CTA buttons, and the mobile menu button.
