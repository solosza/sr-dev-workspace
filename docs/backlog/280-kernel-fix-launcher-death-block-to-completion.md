# Launcher-Death Fix — Block-to-Completion Launch Discipline for Background Pipelines

## Status
Open

## Priority
High — this silently killed a live build (the platform-hybrid factory run) mid-flight and is a general orchestration hazard for every backgrounded pipeline. It must be codified so it can't recur by accident.

## Summary
A background pipeline launched *inside a sub-agent's session* dies when that sub-agent ends its turn. This session's platform-hybrid factory build detached its `run-spec-factory.sh` run and the launcher agent ended → the run died at step 6 with no error surfaced. (The 270 runner survived only because it happened to finish before its launcher ended — luck, not design.) A second attempt as a persistent main-session background bash avoided the death but hit the empty-output nested-`claude` failure (see 281) — so the *reliable* pattern is a sub-agent that runs the pipeline in the **foreground and blocks to completion** (the sub-agent context is what makes nested `claude -p` work; blocking is what keeps it alive). Codify this as the mandatory launch discipline.

## Evidence (this session)
- Factory build (`aaf1e150...`): sub-agent verified step 6, then **detached the remaining run and ended its turn** → detached `bp2ykibmq` died; steps 7–12 never ran. No failure was surfaced — the orchestrator only found it by checking process liveness + state mtime.
- The successful pipelines this session (223/269/261) all worked because their sub-agents ran `run-task.sh` in the **foreground and blocked** until it finished, *then* reported.
- Ledger entry 2026-07-23T00:05 records the failure.

## Requirements
- **Codify the rule in the spawn-subagent skill:** long-running pipelines (`run-task.sh`, `run-spec-factory.sh`, prod-test) MUST be launched by a sub-agent that runs them in the **foreground and blocks to completion** — the sub-agent does not detach the run and does not end its turn until the run finishes (or definitively fails). NEVER "launch-and-detach-then-end."
- **Document the failure mode explicitly** (launcher-death) so future orchestration reads it: a detached child of a sub-agent dies when the sub-agent's turn ends; only the sub-agent's own foreground/blocking execution (or a process owned by the persistent main session) survives.
- **Note the interaction with 281:** the "persistent main-session background bash" alternative avoids launcher-death but is subject to the nested-`claude` empty-output fragility — so the blocking-sub-agent is the recommended default until 281 lands.
- **Guard/verification:** a test or gate that checks the spawn-subagent skill mandates block-to-completion and contains no "detach then end" guidance; ideally a lint on orchestration prompts.
- **Lesson:** add a lessons.md entry for launcher-death with the block-to-completion fix.

## References
- `.claude/skills/spawn-subagent/` (SKILL.md, references/step-03-invoke-agent.md, step-04-return-task-id.md — currently emphasizes non-blocking return; that is correct for the *caller* but the SPAWNED agent must block on the pipeline)
- `docs/backlog/281-kernel-fix-factory-runner-empty-output-hardening.md` (the empty-output fragility that makes the main-session-bash alternative unreliable)
- This session's ledger (launcher-death failure entry); 223/269/261 (working blocking pattern) vs the factory build (failed detach pattern)

## Task Builder Input
- **Deliverable:** Updated spawn-subagent skill codifying block-to-completion as the mandatory pattern for long-running pipelines (with the launcher-death failure mode documented), a lessons.md entry, and a guard/test verifying the rule is present.
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Distinguish the CALLER's non-blocking return (correct — the user isn't blocked) from the SPAWNED agent's requirement to block on the pipeline (the fix). Runs via `run-task.sh` (now 270-hardened) launched block-to-completion. Independent of the factory repo — safe to run in parallel with the platform-hybrid build.
