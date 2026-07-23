# Gate Contract — 272 Model Router Keyword Tuning

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| MR-01 | model-routing-config.json keyword sets re-weighted: build/implement/write/author/design verbs route to the SONNET tier by default; HAIKU keyword set is mechanical-only (copy, scaffold, rename, move, stub, register, index); OPUS keeps the hardest tiers (multi-file architecture, gate/verify synthesis) | grep + read | 001 | build->sonnet, haiku mechanical-only |
| MR-02 | Disambiguation + no-silent-cheapest in model-router.sh: when a task matches BOTH a mechanical and an authoring verb, the HIGHER tier wins (documented); an UNMATCHED task defaults to SONNET (not haiku). Model IDs unchanged (opus-4-8/sonnet-5/haiku-4.5) | grep + read | 002 | precedence + sonnet-default present |
| MR-03 | Routing-assertion test: feed representative task shapes through model-router.sh and assert the resolved tier — build/write -> sonnet (incl. 247/001 + 257/001 shapes), copy/scaffold -> haiku, architecture/gate -> opus, unmatched -> sonnet. Runs live | live bash | 003 | all routing assertions pass live |

## Rules
- READ lib/model-routing-config.json + lib/model-router.sh FIRST (RULE ZERO) — understand the current keyword->tier structure before editing
- Change ONLY the keyword->tier mapping + precedence/default — NOT the resolved model IDs (opus-4-8/sonnet-5/haiku-4.5, set this session)
- Verify the model IDs still probe-resolve after edits (no accidental ID change)
- One action per task. Any RED -> fix -> /kernel/learn.
