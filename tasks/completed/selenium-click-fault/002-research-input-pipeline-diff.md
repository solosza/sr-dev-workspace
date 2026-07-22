# Research: Input-Pipeline Diff (chromedriver vs Playwright)

## Context
Backlog 235. Both stacks send CDP Input.dispatchMouseEvent; one drops ~15/16, the other never. Find the concrete difference.

## Type
RESEARCH
## Execution
inline
## Dependencies
- None

## Requirements
- Capture a FAILING click with chromedriver verbose logging: selenium `Service(log_output=..., service_args=["--verbose"])`; use the known repro (Orderly login → /orders → click delete). PORT ISOLATION: boot Orderly on PORT 8019 (`--port 8019`, DATABASE_URL env pointing at a COPY of the db in scratchpad) — pipeline 209 runs concurrently and owns 8017. Extract the Input.dispatchMouseEvent commands + target/session ids around the click
- Capture the equivalent Playwright click's protocol traffic: `PWDEBUG`/`DEBUG=pw:protocol` env (pip install playwright + chromium in scratchpad if needed — sanctioned diagnostic tooling)
- Diff: coordinates space, frame/target attachment, event sequence (mouseMoved before press?), flags. State the difference or explicitly conclude "identical at CDP — fault below protocol"
- Secondary probe if CDP looks identical: does adding an explicit Input.dispatchMouseEvent 'mouseMoved' before press change delivery rate? (10-trial mini-matrix)
- Write to `projects/selenium-click-fault/notes-pipeline-diff.md` with log excerpts

## Acceptance Criteria
- [ ] notes-pipeline-diff.md with captured logs + concrete diff or explicit null result

## Gates Satisfied
- SCF-02, SCF-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
