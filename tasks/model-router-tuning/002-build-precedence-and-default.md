# Task 002: Precedence + No Silent Cheapest
**Type:** BUILD | **Gates:** MR-02
## Action
Edit lib/model-router.sh so multi-match resolves to the higher tier and unmatched tasks default to Sonnet.
## Spec
READ model-router.sh routing logic first. (1) PRECEDENCE: when a task file matches BOTH a mechanical (haiku) and an authoring (sonnet) verb — e.g. 'copy then adapt' — the HIGHER tier wins (sonnet over haiku, opus over sonnet). Document the precedence in the config or the router. (2) DEFAULT: if NO keyword matches, default to SONNET, not haiku (an unclassified task is more likely real work than mechanical). Keep the retry_upgrade_order intact. Model IDs unchanged.
## Acceptance
Higher-tier-wins precedence on multi-match; unmatched defaults to sonnet; retry order + model IDs intact.
