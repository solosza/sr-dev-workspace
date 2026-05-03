# Infrastructure Diff — sr_dev_workspace → isagawa-kernel

## Status
NEW

## Entirely Missing from Master

### lib/
| File | Purpose |
|------|---------|
| `lib/common.sh` | Shared shell helpers |
| `lib/attestation/__init__.py` | Package init |
| `lib/attestation/intent.py` | Intent chain recording |
| `lib/attestation/attest.py` | Attestation bundle creation |
| `lib/attestation/sign.py` | Sigstore signing |
| `lib/attestation/rekor.py` | Rekor transparency log |
| `lib/attestation/collect.py` | Evidence collection |
| `lib/attestation/schema.py` | Attestation schema |

### Shell Scripts
| File | Purpose |
|------|---------|
| `run-task.sh` | One-shot task execution with resume |
| `run-task-batch.sh` | Batch task execution |

### Lessons
| File | Purpose |
|------|---------|
| `.claude/lessons/lessons.md` | Actionable lessons index (RULE ZERO) |
| `.claude/lessons/*.md` (16 topic files) | Detailed lesson references |

Note: Master has a `lessons/` at root level with Python modules (tiered decay, recurrence). These are DIFFERENT from `.claude/lessons/` (markdown). Both coexist.

### CLAUDE.md
72 diff lines. Master version is outdated — missing task-builder, audit-workflow, execute-pipeline, prod-test, backlog command sections. Replace with sr_dev version.

### Settings
Master has `settings.local.json` with permissions + 2 hooks. Needs update to register all 6 hooks. See hooks-diff.md.

No `settings.json` exists in master — check sr_dev and copy if present.
