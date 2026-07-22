# References — /summarize

## Design Doc

→ `.claude/docs/design/summarize/index.md`

## Design Payloads

| Reference | Purpose |
|-----------|---------|
| → `.claude/docs/design/summarize/references/workflow.md` | Step details and phase flow |
| → `.claude/docs/design/summarize/references/source-resolution.md` | How to find input files for a target |
| → `.claude/docs/design/summarize/references/summary-format.md` | Output template and dynamic sizing rules |

## Integration Points

| Integration | File |
|------------|------|
| `/kernel/complete` | `.claude/commands/kernel/complete.md` |
| `/kernel/review-queue` | `.claude/skills/review-queue/SKILL.md` |
| Review state | `.claude/state/review-status.json` |
