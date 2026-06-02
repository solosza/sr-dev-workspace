# Isagawa Fit Assessment — Frontend Design Skill

## The Isagawa Aesthetic (Codified)

The isagawa site has a strong, consistent visual identity derived from a shader-based design system:

### Color Palette
- **Background**: Pure black (`rgb(0,0,0)`) with subtle radial gradient (`rgb(10,10,14)` at center)
- **Surface**: Near-black (`rgb(12,12,12)`) for cards
- **Elevated**: Dark gray (`rgb(24,24,24)`) for nested elements
- **Primary text**: Warm off-white (`rgb(252,249,243)` / `#fcf9f3`)
- **Secondary text**: Same warm white at 60% opacity
- **Accent**: The warm off-white IS the accent — monochromatic, not a separate hue
- **Only color exceptions**: Badge variants (blue for BUILD, green for WORKSPACE, amber for OPERATE) and the green attested counter

### Typography
- **Heading + Body**: STIX Two Text (serif) — a distinctive, academic-feeling choice
- **Mono**: SF Mono / Fira Code stack — used for nav links, labels, meta text, terminal elements
- **Scale**: 1.25 ratio from 16px base, hero at 3rem, section titles at clamp(2.75rem, 5.5vw, 5rem)

### Layout Patterns
- **pill-nav**: Floating centered nav with blur backdrop, 100px border-radius, dropdown menu
- **evidence-card**: Dark surface cards with subtle border, hover lift (translateY(-2px)), glow shadow
- **flow-card**: Horizontal layout with large faded step numbers + content
- **anchor-section**: Full-width sections with oversized faded section numbers (parallax), generous vertical padding (clamp(8rem, 18vh, 18rem))
- **terminal**: Floating 3D-perspective terminal with dot header, typing animation

### Texture & Effects
- **Grain overlay**: SVG noise texture at 2.5% opacity, fixed position, covers entire viewport
- **Scroll reveals**: Elements fade in from 30px below with 700ms ease-out
- **Stagger animations**: Children reveal sequentially with 120ms delay multiplier
- **Parallax**: Section numbers move independently on scroll
- **Terminal float**: Gentle 5s float animation on perspective-transformed terminal

### Design Philosophy
- **Dark-only** — no light theme, no toggle
- **Monochromatic** — warm off-white on black, color used sparingly for semantic meaning
- **Serif headings + mono details** — academic gravitas meets technical precision
- **Generous space** — sections breathe with 8-18rem vertical padding
- **Subtle depth** — grain, card lift, glow shadows, not dramatic 3D or gradients

## Skill Compatibility Analysis

### Where the Skill REINFORCES the Isagawa Aesthetic

1. **Anti-generic mandate**: The skill explicitly bans Inter, Roboto, Arial, system fonts, and purple-gradient-on-white. Isagawa already uses STIX Two Text (serif) and a monochromatic dark palette — the skill would catch any regression toward generic choices.

2. **Typography emphasis**: The skill demands "characterful, unexpected font choices." STIX Two Text qualifies. The skill would prevent future pages from defaulting to a safe sans-serif.

3. **Texture and atmosphere**: The skill encourages "gradient meshes, noise textures, geometric patterns, grain overlays." Isagawa already uses grain overlay and radial gradients — perfect alignment.

4. **CSS variables**: The skill recommends CSS variables for consistency. Isagawa already has a comprehensive token system (`--bg-primary`, `--text-primary`, `--accent`, `--space-*`, `--card-*`).

5. **Motion with restraint**: The skill says "one well-orchestrated page load with staggered reveals creates more delight than scattered micro-interactions." Isagawa's scroll-reveal with stagger delays matches this exactly.

### Where the Skill Could CONFLICT or Cause Drift

1. **Aesthetic re-selection risk**: The skill instructs Claude to "commit to a BOLD aesthetic direction" each time, choosing from options like "brutally minimal, maximalist chaos, retro-futuristic." On a new page, Claude might pick a different extreme than the established monochromatic-dark-serif identity. The skill has NO mechanism for "continue the existing aesthetic" — it assumes each project is fresh.

2. **Font variety pressure**: The skill says "NEVER converge on common choices across generations" and "vary between different fonts." For isagawa, STIX Two Text IS the font — it should NOT vary page to page. The skill's anti-convergence directive directly conflicts with brand consistency.

3. **Light/dark variation**: The skill says "vary between light and dark themes." Isagawa is dark-only by design. The skill could push a new page toward a light theme.

4. **Layout experimentation**: The skill encourages "asymmetry, overlap, diagonal flow, grid-breaking elements." Isagawa uses structured, predictable layouts (centered content, grid cards, generous padding). The skill might push toward layouts that break the visual language.

## Drift Analysis — job-application.html

The job-application page (from pipeline 110) was checked against the main site:

**Consistent elements:**
- Same CSS variable system (colors, fonts, spacing)
- Same grain overlay
- Same card patterns (evidence-card, flow-card)
- Same hero gradient text treatment
- Pill nav included
- Factory origin strip + loop badge

**Minor drift:**
- Uses its own `job-application.css` instead of importing from `styles.css` — variables are duplicated inline rather than shared
- Terminal color variants slightly different (`rgb(34, 197, 94)` vs `var(--badge-workspace-text)` which is `rgb(134, 239, 172)`)

**Verdict:** Minimal drift. The page was produced by the factory loop and maintained aesthetic consistency. The frontend-design skill would NOT have caught the CSS duplication (that's an architecture issue, not an aesthetic one). The terminal color variance is minor.

## Integration Point Recommendation

**Option A: Skill in `.claude/skills/`** — Available to all repos. Too broad — most isagawa work doesn't need generic "pick an aesthetic" instructions.

**Option B: Named agent `@frontend`** — Overkill for a directive. Named agents are for complex multi-step workflows.

**Option C: Standing directive in isagawa-co.github.io CLAUDE.md** — Best fit. The directive lives where the code lives, applies only to the site repo, and can encode the SPECIFIC aesthetic (not the generic menu).

**Recommended: Option C (ADAPT)** — Don't use the skill as-is. Extract the useful anti-patterns and quality checks, combine with the codified isagawa aesthetic above, and write a site-specific frontend directive in the isagawa repo's CLAUDE.md.
