# Gate Contract — 280 Launcher-Death Fix

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| LD-01 | lessons.md has a launcher-death entry: background pipeline launched inside a sub-agent dies when the sub-agent ends its turn; fix = spawned agent runs FOREGROUND + blocks to completion (never detach-then-end). Cites this session's factory-build death at step 6 | grep + read | 001 | lesson present w/ fix |
| LD-02 | spawn-subagent skill (SKILL.md + references/step-03-invoke-agent.md) mandates that for LONG-RUNNING pipelines (run-task.sh / run-spec-factory.sh / prod-test) the SPAWNED agent runs the pipeline in the FOREGROUND and BLOCKS to completion — does not detach the run and does not end its turn until it finishes/definitively fails. Distinguishes caller-non-blocking (kept) from spawned-agent-blocking (added) | grep + read | 002 | rule present, distinction clear |
| LD-03 | Discipline gate: grep the spawn-subagent skill — the block-to-completion rule is present AND there is no guidance telling the SPAWNED agent to detach-then-return/end for long pipelines. Lesson present. Evidence captured | grep | 003 | zero detach-then-end for spawned pipelines |

## Rules
- READ the spawn-subagent skill (SKILL.md, step-03, step-04) + lessons.md FIRST (RULE ZERO)
- The CALLER returning non-blocking to the USER is CORRECT and stays — the fix is that the SPAWNED background agent must block on the pipeline it runs. Do not conflate the two.
- One action per task. Any RED -> fix -> /kernel/learn.
