# Frontend Design Skill — Summary

## What It Does

The Anthropic `frontend-design` skill guides Claude to create distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. It triggers when users ask to build web components, pages, artifacts, posters, or applications (websites, landing pages, dashboards, React components, HTML/CSS layouts).

## How It Works

### 1. Design Thinking Phase (Before Code)

The skill mandates understanding context and committing to a BOLD aesthetic direction before writing any code:

- **Purpose**: What problem does the interface solve? Who uses it?
- **Tone**: Pick an extreme aesthetic direction from options like: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian
- **Constraints**: Technical requirements (framework, performance, accessibility)
- **Differentiation**: What makes this UNFORGETTABLE?

Key principle: "Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work — the key is intentionality, not intensity."

### 2. Implementation Requirements

Code must be:
- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

### 3. Aesthetic Selection Mechanism

The skill does NOT present a menu of aesthetics for the user to choose from. Instead, it instructs Claude to:
1. Understand the context (purpose, audience, constraints)
2. Select an appropriate aesthetic direction itself
3. Commit fully to that direction
4. Vary between light/dark themes, different fonts, different aesthetics across generations

The enforcement is directive-based: Claude is told to NEVER converge on common choices and to NEVER use generic patterns.

## Aesthetic Guidelines

| Dimension | Instruction |
|-----------|-------------|
| Typography | Beautiful, unique, characterful fonts. NEVER use generic fonts (Arial, Inter, Roboto, system fonts). Pair distinctive display font with refined body font. |
| Color & Theme | Cohesive aesthetic via CSS variables. Dominant colors with sharp accents. NEVER use cliched schemes (purple gradients on white). |
| Motion | CSS-only animations for HTML. Motion library for React. Focus on high-impact page load with staggered reveals (animation-delay). Scroll-triggering and surprise hover states. |
| Spatial Composition | Unexpected layouts, asymmetry, overlap, diagonal flow, grid-breaking elements, generous negative space OR controlled density. |
| Backgrounds & Details | Atmosphere and depth — gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, grain overlays. |

## Anti-Patterns (Explicitly Banned)

- Overused font families: Inter, Roboto, Arial, system fonts
- Cliched color schemes: purple gradients on white backgrounds
- Predictable layouts and component patterns
- Cookie-cutter design lacking context-specific character
- Converging on common choices (e.g., Space Grotesk) across generations

## Artifact-Based vs File-Based Applicability

The skill is **framework-agnostic**. It mentions HTML/CSS/JS, React, and Vue as implementation options. It references "artifacts" in its description ("posters, artifacts") suggesting it was designed primarily for **claude.ai artifact-based development** (where Claude generates self-contained HTML/CSS/JS in an artifact window).

However, the principles are fully applicable to file-based development:
- Typography, color, and layout rules apply to any CSS file
- The "Design Thinking" phase works regardless of output format
- The anti-patterns are universal
- CSS variable usage and animation techniques are standard web practices

The skill does NOT assume a specific development environment — it's a set of design principles enforced via directive.

## File Structure

The skill consists of two files:
- `SKILL.md` — The full instruction set (single file, ~60 lines of directives)
- `LICENSE.txt` — License terms

No sub-references, no step files, no enforcement hooks. It's a flat directive — a standing instruction that shapes all frontend output.
