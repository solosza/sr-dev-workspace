# Task 001: Record Launcher-Death Lesson
**Type:** BUILD | **Gates:** LD-01
## Action
Append a launcher-death lesson to .claude/lessons/lessons.md.
## Spec
Record: a background pipeline launched INSIDE a sub-agent's session dies when that sub-agent ends its turn (a detached child does not outlive its sub-agent). This session's platform-hybrid factory build detached run-spec-factory.sh and its launcher agent ended -> the run died silently at step 6; no error surfaced. The 270 runner survived only because it finished before its launcher ended (luck). Fix: the SPAWNED agent must run the pipeline in the FOREGROUND and BLOCK to completion (do not detach, do not end the turn until it finishes/definitively fails) — the pattern 223/269/261 used successfully. A persistent MAIN-session process also survives but is subject to the nested-claude empty-output fragility (backlog 281), so the blocking sub-agent is the default.
## Acceptance
lessons.md has the launcher-death entry with the block-to-completion fix, citing the factory step-6 death.
