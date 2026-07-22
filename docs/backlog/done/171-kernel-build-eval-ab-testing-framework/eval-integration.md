# Eval Integration

## Status
NEW

## Location
- `workspace:.claude/skills/eval/` (new mode in existing skill)
- `workspace:.claude/commands/kernel/eval.md` (usage docs)

## What It Does

Adds `--ab` mode to `/kernel/eval` so A/B experiments run through the same command interface as artifact and harness evals.

## New Mode

```
/kernel/eval --ab <artifact> <source>
/kernel/eval --ab check-data-engine D:\...\hmsa-healthcare-qa
/kernel/eval --ab anchor D:\...\isagawa-kernel
```

## Mode Detection Update

Current (step-00):
| Args | Mode |
|------|------|
| 1 arg | Harness |
| 2 args | Artifact |

With A/B:
| Args | Mode |
|------|------|
| 1 arg | Harness |
| 2 args | Artifact |
| `--ab` + 2 args | A/B experiment |

## New Steps (A/B mode only)

The A/B mode reuses Step 0 (resolve source) but replaces Steps 1-6 with:

| Step | Action |
|------|--------|
| 0 | Resolve source + detect artifact (reused) |
| AB-1 | Generate variants (flat + tiered) |
| AB-2 | Build task prompt (auto or provided) |
| AB-3 | Run N iterations (claude -p both variants) |
| AB-4 | Score outputs (DeepEval GEval per metric) |
| AB-5 | Compare + report (deltas, stats, verdict) |

## Experiment Config

```json
{
  "mode": "ab",
  "artifact": "check-data-engine",
  "source": "D:\\...\\hmsa-healthcare-qa",
  "runs": 5,
  "model": "claude-sonnet-4-6",
  "judge_model": "gpt-4o-mini",
  "metrics": ["compliance", "adherence", "completeness", "following", "drift"],
  "thresholds": {
    "significant_delta": 0.05,
    "win_rate_threshold": 0.67
  },
  "task_prompt": null
}
```

When `task_prompt` is null, auto-generates from artifact analysis.

## Output Location

```
evals/eval-ab-<artifact>/
├── variants/
│   ├── flat/
│   └── tiered/
├── results/
│   ├── run-1/ ... run-N/
│   ├── scores.json
│   └── ab-report.md
└── experiment-config.json
```

Score history appended to source repo at `eval/results/ab-score-history.json`.

## Skill File Changes

| File | Change |
|------|--------|
| `steps/step-00-resolve-source.md` | Add `--ab` flag detection in Phase 1 |
| `workflow.md` | Add AB state machine branch |
| `SKILL.md` | Add A/B mode to vocabulary and workflow summary |
| New: `steps/step-ab-*.md` | One step file per AB step |
| `gate-contract.md` | Add AB-mode gates |

## Dependencies
- Variant generator, runner, scorer from platform-deepeval
- Working `claude -p` CLI
- Existing eval skill infrastructure
