# Research: Frontend Design Skill — Isagawa Site Integration

## Status
Open

## Priority
Medium — directly applicable to isagawa-co.github.io; each new page currently starts from scratch without explicit aesthetic direction, leading to inconsistency at the margins

## Summary
Anthropics published a frontend-design skill (`github.com/anthropics/skills/tree/main/skills/frontend-design`) that forces aesthetic direction selection (Brutalism, Minimalism, Retro-futurism, etc.) before writing any CSS or HTML. The isagawa site has established visual patterns (pill-nav, flow cards, terminal demos) but no enforced aesthetic contract — new pages can drift. Research determines whether this skill adds value as a pre-pipeline check or as a standing convention in the site's CLAUDE.md.

## Requirements
- Read the frontend-design skill file — what does it actually instruct Claude to do before writing code?
- Assess fit: does the isagawa site have an implied aesthetic that should be codified? (dark backgrounds, monospace accents, card-based layouts, minimal color palette)
- Determine integration point: skill in `.claude/skills/` invoked per pipeline, named agent `@frontend`, or a standing directive added to the isagawa-co.github.io CLAUDE.md?
- Identify what the skill would catch that current page pipelines miss (e.g., `110-market-build-job-application-product-page.md` — did the job-application page drift from the established aesthetic?)
- Assess whether the skill is claude.ai-artifact-oriented or genuinely applicable to file-based HTML/CSS development

## References
- Frontend-design skill: `https://github.com/anthropics/skills/tree/main/skills/frontend-design`
- Isagawa site: `D:/my_ai_projects/isagawa-co.github.io`
- Existing pages: `qa-platforms.html`, `job-application.html`, `story.html`, `attestation.html`, `ssh-compliance.html`, `vibe-coder.html`
- Existing CSS: `styles.css`, `pill-nav.css`, `qa-platforms.css`, `job-application.css`

## Task Builder Input
- **Deliverable:** Research report — assessment of the skill, recommendation (adopt / adapt / skip), and (if recommended) a concrete integration plan specifying exactly where the skill lives and when it triggers
- **Location:** `subproject:frontend-design-skill-research`
- **Scope:** RESEARCH
- **Constraints:** The isagawa site already has established visual patterns — the skill should reinforce consistency, not override existing design. If adopted, must work with file-based HTML/CSS development, not just claude.ai artifacts.
