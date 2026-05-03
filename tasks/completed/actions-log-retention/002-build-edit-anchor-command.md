# 002 — Edit Anchor Command to Read from JSONL

## Type
BUILD

## Action
Edit `.claude/commands/kernel/anchor.md` Part B (step 6) and Part C (step 11) to read from `.claude/state/actions.jsonl` instead of the `actions_log` array in session_state.json.

## What to Do

1. **Part B, Step 6 — Read the actions log:**
   - Change from "Read `actions_log` array from `session_state.json`"
   - To: "Read `.claude/state/actions.jsonl` — each line is a JSON object with `timestamp`, `tool`, `entry` fields"
   - The agent reads the JSONL file, parses each line, and reviews as before

2. **Part C, Step 11 — Archive and reset actions log:**
   - Change the archive step to:
     - Read `.claude/state/actions.jsonl`
     - Archive contents to `.claude/state/anchor-logs/YYYY-MM-DD/HH-MM-SSZ.json` (same format as before)
     - Truncate `actions.jsonl` to empty (write empty string)
     - Clear `actions_log` array in session_state.json to `[]` (backward compat summary)
   - The authoritative log is now actions.jsonl, not the session_state array

3. **Add note** that `actions_log` in session_state.json is now a backward-compatible summary (last 10 entries) and the full log lives in actions.jsonl

## Target File
`.claude/commands/kernel/anchor.md`

## Acceptance
- [ ] Step 6 references actions.jsonl as the primary log source
- [ ] Step 11 archives from actions.jsonl
- [ ] Step 11 truncates actions.jsonl after archive
- [ ] Note about session_state.json backward compatibility added

## Dependencies
None
