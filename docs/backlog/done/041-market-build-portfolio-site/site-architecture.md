# Site Architecture

## Status
NEW

## Page Layout

Single-page scroll with anchor navigation. Follows Suero's section-by-section B2B conversion flow.

## Navigation

```
[Isagawa logo]  Kernel  |  Factory  |  Catalog  |  Platforms  |  Contact
```

- Fixed/sticky header
- Links anchor-scroll to sections
- Mobile: hamburger or collapse menu

## Section Order (Conversion Flow)

| # | Section | Purpose | Conversion Role |
|---|---------|---------|-----------------|
| 1 | Hero | "The AI Management Layer" — what Isagawa is | Hook — stop scrolling |
| 2 | Architecture | Kernel → Factory → Agents diagram | Educate — show the system |
| 3 | Kernel | 4 mechanisms (anchor token, gates, learn loop, self-audit) | Differentiate — why this is hard to replicate |
| 4 | Spec Factory | Pipeline visual + 3 output types | Prove capability — compiler, not catalog |
| 5 | Catalog | 27+ specs by vertical with type badges | Prove breadth — any domain |
| 6 | QA Platforms | 5 platforms, shared 5-layer architecture | Prove depth — tangible products |
| 7 | Loop | Compounding flywheel visual | Prove durability — gets better over time |
| 8 | CTA | "What domain do you need managed?" + contact | Convert — start conversation |
| 9 | Footer | Links, copyright, social | Standard |

## Responsive Strategy

Three breakpoints:
- **Desktop:** ≥1024px — full layout, multi-column grids
- **Tablet:** 768px–1023px — reduced columns, smaller typography
- **Mobile:** <768px — single column, stacked cards, hamburger nav

## Output Structure

```
isagawa-portfolio-site/
  index.html          ← Single page, semantic HTML5
  styles.css          ← All styles, CSS variables, responsive
  assets/
    images/           ← Diagrams, icons, any visual assets
    fonts/            ← Local font files if needed
```

Self-contained — opens directly in a browser with no build step.

## Dependencies
- Design tokens must be finalized before section CSS (Phase 2 before Phase 3)
- Content spec drives HTML content (see [[041-market-build-portfolio-site/content-spec]])
- Catalog data drives section 5 cards (see [[041-market-build-portfolio-site/catalog-data]])
