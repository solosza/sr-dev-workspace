# Task 006: L3 — Live Injection in Real Session (GATE)

**Type:** TEST (L3) — GATE TASK: skip never waives (lesson #39); orchestrator validates regardless.
**Gates:** JIT-06

## Action

Scratch repo containing ONLY: the injector hook, the rule map, a settings.local.json registering just the injector, and an empty state dir. Run a fresh `env -u CLAUDECODE claude -p` with `--output-format json` and a prompt that performs ONE tool call matching rule 1's pattern, then ONE non-matching call.

Assert from the transcript/output:
(a) the injected system-reminder (rule 1 snippet text) appears after the matching call
(b) it does NOT appear for the non-matching call
(c) both commands actually EXECUTED — nothing was blocked
(d) scratch `.claude/state/jit-injections.jsonl` contains exactly the matching event

If additionalContext does not surface in `-p` transcripts on the installed Claude Code version, capture the raw hook stdout via a wrapper and document the exact limitation with the version string — degrade honestly, never fake the gate.

## Acceptance

Live evidence or documented residue with version proof. Red → fix → /kernel/learn.
