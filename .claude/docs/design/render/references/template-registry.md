# Template Registry

Parent: [[../index.md]]. Templates are the extension surface — one template = one integration point.

## Anatomy

```
templates/[name]/
├── template.md      ← what it renders, artifact data source, ACTION MAP (action → kernel command, destructive flags)
└── generate.py      ← (artifact data) → self-contained page.html with annotation JS
```

`templates/INDEX.md` lists registered templates (name, purpose, consuming command). Step 1 resolves against it.

## Registration Rules

1. A template NEVER invents new transport — it emits the standard annotation schema; only the action map is its own.
2. Data sources reuse existing discovery (review-board uses review-queue's diff; chain-status will read the same state files the text report reads) — no parallel bookkeeping.
3. generate.py output must be self-contained HTML (no external hosts — works under any CSP, works offline) with the "Send to session" affordance and session-dir banner.
4. Adding a template = adding the folder + INDEX row. Core untouched.

## Planned Templates (post-v1, each its own backlog)

| Template | Renders | Consuming flow |
|----------|---------|----------------|
| review-board (v1) | Unreviewed done-backlog queue as actionable cards | /kernel/review-queue |
| chain-status | Verticals × gates dashboard, running pipelines, held items | execute-pipeline reporting |
| gate-report | Orchestrator validation checklists (collapsed-green, expanded-red) | per-merge gate passes |
| research-report | Report sections + actionable shortlist cards | RESEARCH pipeline outputs |
