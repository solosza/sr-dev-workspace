# Task 003: Discipline Gate
**Type:** TEST | **Gates:** LD-03
## Action
Verify the block-to-completion rule is present and no conflicting detach-then-end guidance remains; write evidence.
## Spec
Grep .claude/skills/spawn-subagent/ for the block-to-completion mandate (spawned agent runs foreground + blocks to completion for long pipelines). Confirm lessons.md has the launcher-death entry. Confirm there is NO guidance instructing the SPAWNED agent to detach-then-return/end for a long-running pipeline (the caller's non-blocking return to the user is fine and expected — do not flag that). Capture the matching lines as evidence + zero conflicting-guidance hits.
## Acceptance
Block-to-completion rule present, lesson present, zero spawned-agent-detach-then-end guidance for long pipelines. Evidence recorded.
