# Build Portfolio Site — "The Loop" Theme

## Status
Open

## Priority
High — the site is the proof that the harness works. Supersedes 041 (scratched). Consumes 044 (extraction).

## Summary
Build the Isagawa portfolio site from design tokens extracted by backlog 044. Theme: make the loop visible in 90 seconds. The site itself is the demonstration — built by the harness from conversational intent, with the loop narrative baked into every section. Four anchor moments (Seed → Growth → Self-Extension → This Page) tell the story. Dark/terminal aesthetic. Static HTML/CSS output. Provenance page with Sigstore attestation (backlog 046) proves it was all produced from natural language.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[047-market-build-portfolio-site-loop-theme/positioning]] | What Isagawa is — single framing, five views, hero copy |
| [[047-market-build-portfolio-site-loop-theme/theme-and-narrative]] | 90-second test, 4 anchor moments, content rules, provenance |
| [[047-market-build-portfolio-site-loop-theme/build-phases]] | 4-phase execution plan: token merge → CSS → HTML sections → polish |

## Architecture

```
044 extraction output          047 build
(data/portfolio-site/)         (tasks/portfolio-site/)

suero/*.json ──┐
               ├──→ Token Merge ──→ CSS Foundation ──→ HTML Sections ──→ Polish
shader/*.json ─┘         |              |                    |              |
                    unified         reset, vars,        4 anchor        responsive,
                    tokens          grid, type          moments         a11y, dark
                                                            |
                                                       Provenance
                                                       (046 output)
```

## Extraction Reality (from 044 results)
Suero extraction is thorough — 17-section structure, spacing, grid, nav, breakpoints all captured with precision. Shader extraction is thin — typography returned all 16px/400 defaults (canvas/SVG/hydration blind spot), colors have a #fff vs rgb(0,0,0) conflict, suero-components.json possibly missing. The portfolio will be **Suero-structural with a hand-crafted dark terminal aesthetic inspired by Shader**, not a mechanical merge of both token sets. Shader contributes: STIX Two Text font family, color palette (conflict to resolve), dark mode intent. Everything else is hand-built or Suero-derived.

## Requirements
- Consume design tokens from `data/portfolio-site/` (produced by backlog 044)
- Use Suero structure/spacing/grid as the layout foundation
- Hand-craft dark terminal aesthetic inspired by Shader (extraction too thin for mechanical merge)
- Resolve shader-colors.json conflict: `--background: #fff` vs computed `rgb(0,0,0)` — use the dark value
- Check if `suero-components.json` exists; if missing, extract manually or skip
- Build 4 scroll sections mapping to Seed / Growth / Self-Extension / This Page
- Hero communicates the loop immediately — "conversational agent factory"
- Punchline at bottom: visitor knows this page is the last link in the chain
- No jargon in first 90 seconds of scroll
- Dark mode / terminal aesthetic (hand-crafted, Shader-inspired — not Suero with dark tint)
- Static HTML/CSS output — no JavaScript framework
- Provenance section with dual attestation display (site's own + second bundle), intent-led layout, client-side Rekor verification badge, modular bundle swap

## Anti-Requirements
- Do NOT extract from reference sites — that's 044's job
- Do NOT use a JavaScript framework — static HTML/CSS only
- Do NOT over-section — 4 anchor moments + nav + footer, not 17 sections

## References
- Backlog 044: `docs/backlog/044-market-clone-portfolio-site-references.md` (extraction — input to this build)
- Backlog 046: `docs/backlog/046-kernel-build-sigstore-attestation-pipeline.md` (provenance section)
- Backlog 041: `docs/backlog/041-market-build-portfolio-site.md` (prior attempt, scratched — lessons in 044's extraction-lessons sub-doc)
- Website cloner skill: `.claude/skills/website-cloner/`
- Skill-as-app research: `projects/kernel-architecture/skill-as-app-research.md`

## Task Builder Input
- **Deliverable:** Complete static portfolio site (index.html + styles.css) with "the loop" theme, dark terminal aesthetic, 4 narrative sections, provenance page
- **Location:** workspace:tasks/portfolio-site/
- **Scope:** BUILD
- **Constraints:** Depends on 044 (extraction) completing first. Provenance section depends on 046 (attestation). Second attestation bundle uses #050 run-task.sh fix (or any other completed pipeline — bundles are modular, swap any bundle by changing one JSON blob). Content must pass the 90-second test. Static HTML/CSS only.
