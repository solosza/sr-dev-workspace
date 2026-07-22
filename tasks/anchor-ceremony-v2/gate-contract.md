# Gate Contract — 245 Anchor Ceremony v2

Deliverable: PreCompact re-anchor hook + registration, actions_limit 50 (hybrid policy), anchor Step 10 rolling ledger + Step 5 read-back. Compaction forces a full anchor via existing Gate 3; failed-attempt history survives compaction.

| Gate | Check | Method | Task | Pass Criteria |
|------|-------|--------|------|---------------|
| AC-01 | `.claude/hooks/precompact-reanchor.py` exists, imports `state_io` (atomic write + utf-8-sig read), resolves agent routing from KERNEL_AGENT_ID/agent_id | file_exists + grep | 001 | file present; `from state_io import` or `import state_io`; `KERNEL_AGENT_ID` referenced; `anchored` set False; exits 0 on all paths |
| AC-02 | PreCompact registered in `settings.local.json` with matcher `auto|manual` → `python .claude/hooks/precompact-reanchor.py` | grep + run_code (json parse) | 002 | hooks.PreCompact[0].matcher == "auto\|manual"; command references precompact-reanchor.py |
| AC-03 | Live `sr_dev_workflow.json` has `actions_limit: 50` | run_code | 003 | json load → actions_limit == 50 |
| AC-04 | Domain-setup seed template seeds `actions_limit: 50` | grep | 004 | `.claude/skills/kernel-domain-setup/references/step-10-state.md` contains `"actions_limit": 50` |
| AC-05 | anchor.md Step 10 has ledger schema `{ts, kind: decision|failure|constraint, summary, refs}` + rolling window cap (5) + Step 14 clears `compaction_anchor_reason` | grep | 005 | all three greps hit in anchor.md |
| AC-06 | anchor.md Step 5 reads ledger back on context restore | grep | 006 | Step 5 section mentions ledger read-back |
| AC-07 | L2: hook invoked with simulated PreCompact stdin (auto AND manual) sets `anchored: false` in ROUTED workflow file, writes `compaction_anchor_reason` + `compaction_timestamp` to routed session state, BOM-free; no-op (exit 0, no crash) on missing state; with KERNEL_AGENT_ID set, parent files byte-identical | run_test | 008 | all sub-checks pass in sandbox |
| AC-08 | L3: real compaction (spawned fresh `claude -p` with manual `/compact`) fires the hook → workflow `anchored` flips false → next write hook-blocks into anchor; ledger array in context survives | run_test | 009 | hook fired (state flipped by hook process, not test); Gate 3 block observed; ledger intact post-compaction |
| AC-09 | Gate 3 in `universal-gate-enforcer.py` unmodified; no Candidate B artifacts (no rolling-summary.jsonl hook, no periodic summarizer) | run_code (git diff) + grep | 007 | `git diff HEAD -- .claude/hooks/universal-gate-enforcer.py` empty; no summarizer hook file |

## Rules

- READ each file fully before editing (RULE ZERO) — especially anchor.md structure and settings.local.json existing hook arrays (merge, never clobber existing PreToolUse/PostToolUse entries)
- State writes via `state_io.atomic_write_json` / Python json.dump UTF-8 no BOM — never PowerShell (lesson #49)
- Hook must exit 0 even on error paths — a crashing PreCompact hook must never block compaction
- Test scripts: AST/JSON-parse based checks where semantics matter; no naive string greps on Python docstrings (lesson #39)
- Any red → fix → /kernel/learn
