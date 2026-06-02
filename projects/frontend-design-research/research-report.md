# Frontend Design Skill — Research Report

## 1. Skill Summary

The Anthropic `frontend-design` skill is a single-file directive (`SKILL.md`) that instructs Claude to create distinctive, production-grade frontend interfaces. It triggers on any request to build web components, pages, dashboards, or applications.

**Core mechanism:**
1. **Design Thinking phase** — Before writing code, Claude must understand purpose, choose a bold aesthetic direction (from options like brutalist, minimalist, maximalist, retro-futuristic, etc.), identify constraints, and define a differentiator.
2. **Implementation requirements** — Code must be production-grade, visually striking, cohesive, and meticulously refined.
3. **Anti-pattern enforcement** — Explicit bans on generic fonts (Inter, Roboto, Arial), cliched color schemes (purple gradients on white), predictable layouts, and convergence on common choices across generations.

The skill is framework-agnostic (HTML/CSS/JS, React, Vue) and was designed primarily for claude.ai artifact-based development, though its principles apply to file-based projects.

**Key insight:** The skill has no memory of prior aesthetic decisions. Each invocation starts fresh with "choose a bold direction." This is by design for artifact generation (each artifact is standalone) but problematic for multi-page sites with established brand identity.

## 2. Isagawa Aesthetic — Brief Style Guide

| Token | Value | Role |
|-------|-------|------|
| Background | `rgb(0,0,0)` + radial gradient to `rgb(10,10,14)` | Pure black foundation |
| Surface | `rgb(12,12,12)` | Card backgrounds |
| Text primary | `rgb(252,249,243)` / `#fcf9f3` | Warm off-white |
| Text secondary | Same at 60% opacity | Muted hierarchy |
| Accent | `#fcf9f3` (the text color IS the accent) | Monochromatic design |
| Semantic colors | Blue (BUILD), Green (WORKSPACE), Amber (OPERATE) | Badge variants only |
| Heading font | STIX Two Text (serif) | Academic gravitas |
| Mono font | SF Mono / Fira Code | Nav links, labels, meta |
| Grain | SVG noise at 2.5% opacity, fixed | Texture layer |
| Card hover | translateY(-2px) + border glow | Subtle depth |
| Section padding | clamp(8rem, 18vh, 18rem) | Generous breathing room |
| Scroll reveal | 30px translateY, 700ms ease-out, 120ms stagger | Entrance animation |

**Design philosophy:** Dark-only, monochromatic, serif headings + mono details, generous space, subtle depth through grain/glow/parallax. No bright colors, no light themes, no playful elements.

## 3. Fit Assessment

### Does the skill apply to file-based HTML/CSS?

**Yes, partially.** The typography, color, motion, and anti-pattern rules are universal. The "Design Thinking" phase works regardless of output format. However, the skill assumes standalone generation (each invocation picks a fresh direction), while file-based projects need consistency across pages.

### Does it reinforce or disrupt?

**Both.**

**Reinforces:**
- Anti-generic mandate aligns perfectly (isagawa already uses distinctive fonts, dark theme, grain texture)
- Typography emphasis protects against serif→sans-serif regression
- CSS variable recommendation matches existing token system
- Motion philosophy ("one orchestrated page load > scattered micro-interactions") matches scroll-reveal pattern

**Disrupts:**
- "Choose a BOLD aesthetic direction" assumes fresh start — could override established identity
- "NEVER converge on common choices across generations" conflicts with brand consistency (STIX Two Text should be used on every page)
- "Vary between light and dark themes" contradicts dark-only design decision
- "Asymmetry, overlap, diagonal flow" could break the structured, generous-padding layout language

## 4. Drift Analysis

**job-application.html** (produced by pipeline 110) was compared against the main site:

| Aspect | Status |
|--------|--------|
| Color variables | Consistent (same values) |
| Font stack | Consistent (STIX Two Text + mono) |
| Grain overlay | Present |
| Card patterns | Matching (evidence-card, flow-card) |
| Pill nav | Included |
| Factory origin | Present |

**Minor issues found:**
- CSS variables duplicated in `job-application.css` instead of importing shared `styles.css` (architecture issue, not aesthetic)
- Terminal green color uses `rgb(34, 197, 94)` instead of the design token `rgb(134, 239, 172)` (minor variant)

**Would the skill have caught this?** No. The skill addresses aesthetic direction, not CSS architecture or token consistency. The terminal color drift is the kind of thing a site-specific directive would catch ("always use `--badge-workspace-text` for success green").

## 5. Recommendation: ADAPT

**Do not adopt the skill as-is.** The re-selection risk outweighs the benefits for a site with an established identity.

**Do adapt** the useful parts into a site-specific frontend directive.

### What to extract from the skill:
1. Anti-pattern list (banned fonts, banned color schemes, banned generic patterns)
2. Quality bar (production-grade, meticulously refined)
3. Motion philosophy (orchestrated page load > scattered micro-interactions)
4. Texture encouragement (grain, gradients, depth)

### What to replace:
1. "Choose a bold direction" → "Continue the isagawa aesthetic" (codified style guide)
2. "Vary fonts/themes across generations" → "Use STIX Two Text for headings/body, mono stack for technical elements, dark theme always"
3. "Asymmetry, overlap" → "Structured layouts with generous padding, card-based content organization"

## 6. Integration Plan

**Target:** `D:/my_ai_projects/isagawa-co.github.io/CLAUDE.md`

**Action:** Add a `## Frontend Aesthetic` section that:

1. Codifies the design tokens (the style guide from section 2 above)
2. Lists anti-patterns from the Anthropic skill (no Inter, no purple gradients, no generic layouts)
3. Adds isagawa-specific anti-patterns (no light themes, no sans-serif headings, no bright accent colors)
4. References `styles.css` as the token source of truth
5. States: "New pages MUST import `styles.css` — do not duplicate CSS variables"
6. States: "Terminal/code elements use `--badge-workspace-text` for success green, not arbitrary green values"

**Not needed:**
- No `.claude/skills/` entry (too broad, applies only to the site repo)
- No `@frontend` named agent (overkill for a directive)
- No changes to the kernel (this is repo-level, not workspace-level)

**Estimated effort:** One task — add the section to CLAUDE.md. The style guide content is already written in this report.
