# Launcher-Death Fix (280) — Task Index

Backlog: [[../../docs/backlog/280-kernel-fix-launcher-death-block-to-completion.md]]
Gate contract: [[gate-contract.md]]

| # | Task | Type |
|---|------|------|
| 001 | [[001-build-lesson-launcher-death.md]] | BUILD |
| 002 | [[002-build-skill-block-to-completion.md]] | BUILD |
| 003 | [[003-test-discipline-gate.md]] | TEST |

Fix: background pipelines launched INSIDE a sub-agent die when that sub-agent ends its turn.
Codify block-to-completion: the SPAWNED agent runs the pipeline FOREGROUND + blocks to completion (never detach-then-end).
Distinguish CALLER non-blocking (correct) from SPAWNED-agent blocking (the fix). Target: D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/skills/spawn-subagent/ + lessons.md.
