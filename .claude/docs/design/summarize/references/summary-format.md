# Summary Format — /summarize

## Output Template

```
SUMMARY: [backlog title or project name]
Backlog: [NNN] | Scope: [BUILD/RESEARCH/REFACTOR]
Status: [complete/partial/failed]

## Requirement Diff

| # | Requirement | Status | Evidence |
|---|------------|--------|----------|
| 1 | [requirement text] | Met | [file path or description] |
| 2 | [requirement text] | Partial | [what's missing] |
| 3 | [requirement text] | Not addressed | — |

Requirements: N/M met, K partial, J not addressed

## Decisions Needed

[Only present if there are decisions. Each item is a recommendation requiring human choice.]

- **[Decision title]** — [description of options/trade-off]. Options: [A] / [B].

## Deliverable Inventory

| File | Type | Description |
|------|------|-------------|
| [path] | [created/modified] | [brief description] |

Files: N created, M modified

## Problems

[Only present if there are problems.]

- **[Problem]** — [description, impact, suggested fix]

## Informational

[Completions, findings, facts that don't require action.]

- [item]
```

## Dynamic Sizing Rules

1. **No line limits.** If the agent produced 20 files, list all 20.
2. **No section suppression.** If a section has items, show it. If empty, omit the section entirely.
3. **Requirement diff always present** for backlog-based summaries. Omit for path-only summaries.
4. **Decisions section appears first after requirement diff** — these need human attention.
5. **Problems section appears before informational** — problems need awareness even if not actionable.

## Section Presence Rules

| Section | When Present |
|---------|-------------|
| Requirement Diff | Always (backlog mode) / Never (path-only mode) |
| Decisions Needed | Only if decisions exist |
| Deliverable Inventory | Always |
| Problems | Only if problems exist |
| Informational | Only if informational items exist |

## Integrated Mode Storage

When writing to review-status.json, store the full summary text under a `summary` key:

```json
{
  "188": {
    "status": "accepted",
    "action": "accept",
    "timestamp": "...",
    "notes": "...",
    "summary": "SUMMARY: ...\n\n## Requirement Diff\n..."
  }
}
```
