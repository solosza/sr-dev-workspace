# 161 Verdict: Research Unified File Linking Convention for Tiered Index Architecture

**Parent:** docs/backlog/done/161-kernel-research-linking-convention.md
**Reviewer note (verbatim):** "check if this is still necessary"
**Date:** 2026-07-22

---

## Verdict: DONE-CONFIRMED

The research deliverable is complete. All five requirements from the backlog are satisfied by the shipped artifacts.

---

## Evidence

### Deliverables (all at `.claude/docs/design/tiered-index-architecture/`)

| File | Satisfies Requirement |
|------|----------------------|
| `linking-convention.md` | Design decision document — layered convention with 3 rules (Status: Accepted, 2026-07-06) |
| `linking-migration-checklist.md` | Migration path for existing files — 4-priority incremental plan |
| `index.md` | Tiered index architecture design doc updated (linking convention integrated as a sub-document) |

### Requirement Coverage

1. **"Evaluate which format gives the strongest read signal"** — Done. Task 002 findings in linking-convention.md: neither wikilinks nor code spans trigger auto-reading; the `→` arrow prefix is the key signal. Both formats work equally with the arrow.
2. **"Test whether @path works in skill files"** — Done. Task 001 confirmed `@path` is CLAUDE.md-specific (client-parsed at startup only); inert plain text in skill files, protocols, and design docs.
3. **"Propose single or layered convention with clear rules"** — Done. Layered convention: `→ [[path]]` for directives, `` `path` `` for informational. Three rules, teachable in one reading.
4. **"Update tiered index architecture design doc"** — Done. `linking-convention.md` added to the architecture folder alongside the three layer documents.
5. **"Provide migration path"** — Done. `linking-migration-checklist.md` with before/after examples, verification commands, 4-priority plan, and explicit "what NOT to migrate" section.

### Current Adoption State

Migration is intentionally incremental ("fix on touch" — per the checklist's own Migration Strategy section):
- SKILL.md step tables: 46 code-span references across 6 files; 1 file (render/SKILL.md) uses `→ [[]]` convention (created post-convention)
- Lessons index: topic table still uses code spans (not yet touched since convention shipped)
- Protocol/CLAUDE.md tables: correctly remain code spans per Rule 2 (anchor ceremony provides the directive)

Incomplete migration is the designed behavior, not a gap — the checklist explicitly says "fix on touch + prioritized batch" and "incremental Priority 3-4."

### Superseding Work Check

No later backlog references or modifies the linking convention. Grepped `docs/backlog/done/` for "linking convention" and "161" — only 161 itself matched. The convention remains the current accepted standard.

---

## Recommendation

**Accept parent backlog 161.** The research is complete, the design decision is accepted and documented, and the migration path is defined. No build follow-up needed — the incremental migration strategy is working as designed (new files adopt the convention; existing files migrate when touched).
