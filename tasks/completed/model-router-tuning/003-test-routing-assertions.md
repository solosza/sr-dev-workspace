# Task 003: Routing-Assertion Test
**Type:** TEST | **Gates:** MR-03
## Action
Write + RUN a live test that feeds representative task shapes through model-router.sh and asserts the resolved tier.
## Spec
Create tests/test_model_router_tiers.sh (or .py). For each representative shape, invoke the real router resolution and assert the tier: (a) a BUILD/authoring task (mirror 247/001 + 257/001 filenames/content) -> sonnet; (b) a copy/scaffold task -> haiku; (c) an architecture/gate/verify task -> opus; (d) an unmatched/ambiguous task -> sonnet; (e) a 'copy then adapt' multi-match -> sonnet (higher wins). Use the actual router function, not a re-implementation. Portable (absolute paths, explicit PYTHONPATH if python). Assert model IDs still resolve (opus-4-8/sonnet-5/haiku-4.5).
## Acceptance
All routing assertions pass live against the real router; model IDs verified unchanged.
