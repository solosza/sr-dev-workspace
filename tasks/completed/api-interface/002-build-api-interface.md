# Build api_interface.py — L1 REST Interface

## Context
Backlog 210. READ FIRST (RULE ZERO): (1) `projects/hmsa-qa-platform/01-interface-design/api-interface.md` in the workspace — the governing design; (2) `framework/interfaces/browser_interface.py` on the branch — match its constructor (driver/session, config dict, logger), logging style, and catch-log-RERAISE idiom exactly; (3) pattern source `D:/my_ai_projects/project_test_repos/platform-playwright/framework/interfaces/api-client.ts` — translate the SHAPE (verb methods, response object, timing), not the TypeScript.

## Type
BUILD
## Execution
inline
## Dependencies
- 001

## Requirements
- File: `framework/interfaces/api_interface.py`
- `ApiResponse` dataclass: `status: int`, `body` (parsed JSON when applicable, else text), `response_time: float` (seconds), plus whatever the design doc adds — design doc wins
- `ApiInterface.__init__(self, session: requests.Session, config: dict, logger)` (mirror browser_interface's DI: SDK object + config + logger; verify the exact param names the design doc specifies)
- Methods: `get/post/put/patch/delete(self, url, **kwargs) -> ApiResponse` — synchronous; each logs the call, times it, catches exceptions to LOG then RERAISE (contract error rule 1); no retries (retry.py is the sanctioned utility, wired at higher layers)
- L1 purity: NO domain vocabulary (no order/customer); no base-URL hardcoding (config may carry base_url per the design doc — read it); no try/except that swallows
- Imports: stdlib + requests only

## Acceptance Criteria
- [ ] Imports clean; all five verbs; ApiResponse correct; catch-log-reraise everywhere

## Gates Satisfied
- AIF-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
