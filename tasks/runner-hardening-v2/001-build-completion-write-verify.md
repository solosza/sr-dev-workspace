# Task 001: Completion Write-Verify in run-task.sh
**Type:** BUILD | **Gates:** RH-01
## Action
Edit run-task.sh so the per-task completion path, after appending the finished task to `completed_tasks` in the routed `{agent-}workflow.json`, RE-READS the file and confirms the append landed; on mismatch, retries the state write (bounded retries) before advancing to the next task.
## Spec
READ the current complete/persist block in run-task.sh first. Use the existing state-write mechanism (Python json.dump / the 244 helper if present) — no PowerShell. Read path must accept utf-8-sig defensively. Route to `agent-{KERNEL_AGENT_ID}-workflow.json` when set, else `{domain}_workflow.json`. Log a clear line on retry. Do NOT change unrelated logic.
## Acceptance
Completion append is followed by a read-back confirmation + bounded retry-on-failure. Non-routed path unchanged.
