# Build A/B Testing Framework for DeepEval Eval Platform

## Status
Open

## Priority
High — validates whether the tiered index architecture (core kernel design pattern) actually improves agent output quality. Evidence-based design decisions.

## Summary
Build a generalized A/B testing component for the deepeval eval platform. Given any command or skill, the framework dynamically generates two variants — flat (monolithic) and tiered (indexed with checkpoints and contracts) — runs identical task prompts against both via `claude -p`, scores outputs with DeepEval GEval metrics, and compares paired results across N runs. Integrates into `/kernel/eval` as a new mode. First experiment: `check-data-engine` from hmsa-healthcare-qa.

## Architecture

```
/kernel/eval --ab <artifact> <source>
    │
    ▼
Step 0: Resolve source + detect artifact
    │
    ▼
Step 1: Variant Generator
    │  ├── Read tiered artifact (SKILL.md → steps/ → references/)
    │  ├── Flatten into single monolithic file (Variant A)
    │  └── Copy tiered structure as-is (Variant B)
    │
    ▼
Step 2: Task Prompt Builder
    │  ├── Analyze artifact to determine a realistic task
    │  ├── Generate golden expected output (or use provided one)
    │  └── Produce identical prompt for both variants
    │
    ▼
Step 3: Runner (N iterations)
    │  FOR i in 1..N:
    │  ├── Run prompt against Variant A (flat) via claude -p
    │  ├── Run prompt against Variant B (tiered) via claude -p
    │  └── Capture both outputs
    │
    ▼
Step 4: Scorer
    │  ├── Score each output with DeepEval GEval metrics
    │  ├── Metrics: compliance, adherence, completeness, drift
    │  └── Paired comparison per run
    │
    ▼
Step 5: Report
    ├── Per-metric score deltas (B - A)
    ├── Statistical summary (mean, std, effect size)
    ├── Verdict: tiered better / same / worse
    └── Raw data in score-history.json
```

## Design Documents

| Document | Purpose |
|----------|---------|
| [[171-kernel-build-eval-ab-testing-framework/variant-generator]] | Dynamic flattening algorithm — how to mechanically convert tiered → flat |
| [[171-kernel-build-eval-ab-testing-framework/runner-and-isolation]] | Execution isolation — claude -p sessions, env setup, output capture |
| [[171-kernel-build-eval-ab-testing-framework/scoring-and-metrics]] | DeepEval metric selection, paired comparison, statistical methods |
| [[171-kernel-build-eval-ab-testing-framework/eval-integration]] | How --ab mode integrates into existing /kernel/eval command + skill |

## Requirements
- Generalized — works with any command/skill from any repo, not hardcoded
- Dynamic variant generation — reads tiered structure, produces flat equivalent mechanically
- Identical prompts — same task, same context, only structure differs
- Multiple runs — N≥3 minimum for stochastic variance
- Paired scoring — same DeepEval metrics applied to both outputs per run
- Statistical comparison — not just "A scored higher" but effect size and confidence
- First experiment uses `check-data-engine` from hmsa-healthcare-qa

## References
- Tiered index architecture: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\docs\design\tiered-index-architecture\`
- First experiment artifact: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\skills\check-data-engine\`
- Existing eval skill: `.claude/skills/eval/`
- DeepEval platform: `D:\my_ai_projects\project_test_repos\platform-deepeval\`
- Backlog 144: kernel-build-deepeval-tiered-index-ab-experiment (prior related work)

## Task Builder Input
- **Deliverable:** A/B testing component integrated into eval platform + first experiment results
- **Location:** `workspace:.claude/skills/eval/` (eval mode extension) + `new-repo:D:\my_ai_projects\project_test_repos\platform-deepeval` (framework components)
- **Scope:** BUILD
- **Constraints:** Requires working `claude -p` for runner. DeepEval + OpenAI API key for scoring. hmsa-healthcare-qa repo must be accessible for first experiment.
