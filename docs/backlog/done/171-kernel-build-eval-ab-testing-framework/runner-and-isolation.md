# Runner and Isolation

## Status
NEW

## Location
`platform-deepeval/framework/ab_testing/runner.py`

## What It Does

Executes identical task prompts against both variants in isolated `claude -p` sessions. Captures outputs for scoring.

## Execution Model

```
FOR run_id in 1..N:
    │
    ├── Setup Variant A workspace (flat)
    │   ├── Create temp dir with flat artifact + minimal harness
    │   ├── Run: env -u CLAUDECODE claude -p "<task_prompt>" --cwd <temp_dir_a>
    │   └── Capture stdout → results/run-{run_id}/variant-a-output.md
    │
    ├── Setup Variant B workspace (tiered)
    │   ├── Create temp dir with tiered artifact + minimal harness
    │   ├── Run: env -u CLAUDECODE claude -p "<task_prompt>" --cwd <temp_dir_b>
    │   └── Capture stdout → results/run-{run_id}/variant-b-output.md
    │
    └── Cleanup temp dirs (optional — configurable)
```

## Isolation Requirements

- **Separate workspaces** — each variant gets its own temp directory. No shared state.
- **No kernel governance** — the test harness should NOT have hooks/enforcement active. We're testing the artifact's instructional quality, not the kernel loop.
- **Identical prompt** — exact same task text, no variant-specific hints.
- **Identical model** — same Claude model for both (controlled via `claude -p` flags).
- **Sequential or parallel** — configurable. Sequential is simpler; parallel saves time but needs care with API rate limits.

## Task Prompt Generation

The runner needs a task prompt. Two modes:

| Mode | Source | When |
|------|--------|------|
| **Provided** | User supplies `task-prompt.md` | When testing a specific scenario |
| **Auto-generated** | LLM reads the artifact and generates a realistic task | Default — ensures the task exercises the artifact's instructions |

Auto-generation prompt template:
```
You are reading a command/skill specification. Generate a realistic task
that would require following these instructions. The task should:
1. Exercise at least 3 steps of the workflow
2. Require reading reference files to produce correct output
3. Have a verifiable correct answer
Output: the task prompt (what a user would type) + the expected output description.
```

## Output Schema

```
results/
├── run-1/
│   ├── variant-a-output.md
│   ├── variant-b-output.md
│   └── metadata.json          ← timestamps, model, token counts
├── run-2/
│   └── ...
└── run-N/
    └── ...
```

## Dependencies
- `claude` CLI available on PATH
- `env -u CLAUDECODE` pattern for subprocess isolation
