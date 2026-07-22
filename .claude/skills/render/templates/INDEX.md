# Template Registry

One template = one integration point. Anatomy: `[name]/template.md` (data source + action map) + `[name]/generate.py` (data → self-contained page.html). Registration = folder + row here. See design payload template-registry.md for rules.

| Template | Renders | Consuming flow | Status |
|----------|---------|----------------|--------|
| review-board | Unreviewed done-backlog queue as actionable cards | /kernel/review-queue | PENDING BUILD (backlog 232 pipeline) |
| chain-status | Verticals × gates dashboard | execute-pipeline reporting | planned |
| gate-report | Orchestrator validation checklists | per-merge gate passes | planned |
| research-report | Report sections + shortlist cards | RESEARCH pipeline outputs | planned |
