# Hash Collection — Post-Pipeline Step

## Status
NEW

## Location
`workspace:.claude/skills/execute-pipeline/` (extension to step 5)

## What It Does
After execute-pipeline completes, computes SHA-256 of all inputs and outputs to populate the attestation bundle.

## Inputs to Hash

| Input | Source | What It Proves |
|-------|--------|---------------|
| Output files | `git diff` or task output manifest | What was produced |
| Backlog document | `pipeline_state.backlog_path` from session state | What the intent was |
| Session transcript / prompt | Current conversation or backlog creation prompt | That natural language drove it (hash only) |

## Collection Method
- Use `python hashlib.sha256()` to compute all hashes
- Walk output directory or use git diff to identify all created/modified files
- Read backlog document path from `session_state.json → pipeline_state.backlog_path`
- For session transcript: hash the backlog's raw content as the minimum viable input proof
- Record timestamp bracket from `pipeline_state` (start) and completion time (end)

## Output
- JSON attestation bundle written to `.claude/state/attestations/<backlog-number>-<timestamp>.json`
- Bundle follows the `natural-language-session/v1` format

## Dependencies
- Pipeline must be complete (all tasks done or skipped)
- Attestation format must be defined
