# Task 002: Codify Block-to-Completion in spawn-subagent Skill
**Type:** BUILD | **Gates:** LD-02
## Action
Update .claude/skills/spawn-subagent/SKILL.md and references/step-03-invoke-agent.md to mandate block-to-completion for long-running pipelines.
## Spec
READ SKILL.md + step-03 + step-04 first. Add an explicit rule: for LONG-RUNNING pipelines (run-task.sh, run-spec-factory.sh, prod-test), the SPAWNED background agent MUST run the pipeline in the FOREGROUND and BLOCK until it completes (or definitively fails) — it must NOT detach the run and end its turn (that kills the run: launcher-death). Preserve and clearly distinguish the existing correct behavior: the CALLER returns non-blocking to the USER (the user is not blocked). The change is about the spawned agent's own execution, not the caller's return. Add a short "Launcher-Death" note documenting the failure mode.
## Acceptance
SKILL.md + step-03 mandate spawned-agent block-to-completion for long pipelines; caller-non-blocking vs spawned-agent-blocking distinction is explicit; launcher-death documented.
