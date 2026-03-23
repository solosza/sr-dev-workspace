# Test QA Platform in Dev Workspace Without Kernel

## Status
Open

## Priority
Medium — validates the QA platform works standalone before testing kernel integration

## Summary
Pull the QA platform (isagawa-qa/platform-selenium) into a fresh dev workspace and run it without the Isagawa Kernel installed. Verify the platform functions on its own — tests run, framework generates eval suites, all features work without kernel enforcement.

## Why
Establishes the baseline. If the platform doesn't work standalone, kernel integration issues will be hard to isolate. Need to confirm the platform is self-sufficient before layering the kernel on top.

## Steps
- [ ] Use an existing dev workspace (e.g., sr-dev-workspace) — don't create a fresh repo. The test is: can a user drop the QA platform into their existing workspace and use it?
- [ ] Clone `isagawa-qa/platform-selenium` into the workspace
- [ ] Follow platform README setup instructions
- [ ] Run existing tests — confirm they pass
- [ ] Generate an eval suite from scratch — confirm workflow works
- [ ] Document any issues or missing dependencies

## Success Criteria
- Platform runs independently with no kernel files present
- All platform tests pass
- Eval suite generation works end-to-end

## Task Builder Input
- **Deliverable:** Test report documenting QA platform standalone functionality — test results, eval suite generation results, issues found
- **Scope:** TEST
- **Constraints:** Use existing dev workspace (e.g., sr-dev-workspace). No kernel files involved. Output to `docs/research/`
