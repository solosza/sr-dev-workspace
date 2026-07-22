# Task 005: L2 — Simulated Injection Behavior

**Type:** TEST (L2) | **Gates:** JIT-05

## Action

Run ONE script against a sandbox state dir (never live .claude/state):

1. Matching stdin (construct a call matching rule 1's tool+pattern) → stdout additionalContext contains rule 1's snippet; sandbox jit-injections.jsonl gains exactly 1 line
2. Non-matching stdin → no injection output, no counter line
3. Same matching call twice back-to-back → second suppressed (dedup)
4. Different matching rule between two rule-1 calls → rule 1 fires again (dedup is consecutive-same-rule only)
5. Malformed stdin AND missing map file → exit 0 both, silent

## Acceptance

5/5 PASS, exit 0, live state untouched (byte-identical before/after). Red → fix → /kernel/learn.
