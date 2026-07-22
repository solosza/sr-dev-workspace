# Model Router Keyword Tuning — Build/Authoring Tasks Must Not Start on Haiku

## Status
Open

## Priority
Medium-High — cheap wins on output quality. 262 fixed *that* routing happens (task resolution) and the config bump set the tiers to opus-4-8/sonnet-5/haiku-4.5; this fixes *what tier* build/authoring tasks land on.

## Summary
With routing now functional (262) and tiers current, the keyword weighting still under-tiers real build/authoring work to Haiku — observed on 247/001 and 257/001, where tasks that write non-trivial code/specs were routed to the cheapest tier. Re-weight the router keywords so build/implement/author tasks start at Sonnet, reserving Haiku for genuinely mechanical work (copy, scaffold, rename, move), and prove the routing with tests.

## Requirements
- **Keyword re-weighting:** in `lib/model-routing-config.json`, adjust the tier keyword sets so task files whose action is build/implement/write/author/design route to the **sonnet** tier by default. Keep **haiku** for mechanical verbs only: copy, scaffold, rename, move, stub, register, index. Keep **opus** for the hardest tiers (multi-file architecture, gate/verify synthesis) per existing retry_upgrade_order.
- **Disambiguation rule:** when a task file matches both a mechanical and an authoring verb, the higher tier wins (a "copy then adapt" task is authoring). Document the precedence in the config or `model-router.sh`.
- **No silent default-to-cheapest:** if no keyword matches, default to **sonnet**, not haiku — an unclassified task is more likely real work than mechanical.
- **Routing tests:** a test harness that feeds representative task-file names/contents (including the 247/001 and 257/001 shapes) through `model-router.sh` and asserts the resolved tier: build→sonnet, copy/scaffold→haiku, architecture/gate→opus, unmatched→sonnet.

## References
- `lib/model-routing-config.json`, `lib/model-router.sh` (updated this session: default+opus→claude-opus-4-8, sonnet→claude-sonnet-5, haiku→claude-haiku-4-5)
- `docs/backlog/262-kernel-fix-runtask-hardening.md` (made routing actually fire — task resolution)
- Observed under-tiering: pipelines 247 task 001, 257 task 001
- `docs/backlog/268-kernel-research-chinese-models-cost.md` (downstream: an added cheap tier would slot into the same config)

## Task Builder Input
- **Deliverable:** Re-weighted `lib/model-routing-config.json` + any `model-router.sh` precedence logic so build/authoring routes to Sonnet and only mechanical work routes to Haiku, plus a routing-assertion test suite.
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Must not change the resolved model IDs (opus-4-8/sonnet-5/haiku-4.5) — only the keyword→tier mapping. `run-task.sh` sources the router, so STRICTLY SEQUENTIAL with 270/271 (lesson #28). Verify the two new model IDs still probe-resolve after edits.
