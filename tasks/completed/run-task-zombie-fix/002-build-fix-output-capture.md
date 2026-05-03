# 002 — Fix Output Capture Reliability on Windows

## Type
BUILD

## Description
Ensure `run_claude()` in `run-task.sh` reliably captures `claude -p --output-format json` output on Windows Git Bash.

## Requirements
- Verify file-based output capture is used (not `$()` command substitution)
- Add a post-run validation: if logfile exists but contains non-JSON (e.g., error messages mixed in), extract the last valid JSON object
- Add fallback: if `claude -p` writes to stderr instead of stdout, capture both (`2>&1` is already there, verify it works)
- Ensure `extract_session_id` and `extract_result` in `common.sh` handle malformed JSON gracefully (don't crash on parse errors)
- If output capture is already working correctly, verify and mark as no-op

## Acceptance Criteria
- [ ] `run_claude()` uses file-based output (not `$()`)
- [ ] JSON extraction handles malformed input gracefully

## Gates
BUILD-01
