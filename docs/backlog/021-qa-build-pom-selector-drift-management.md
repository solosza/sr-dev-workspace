# POM/Selector Drift Management

## Status
Open

## Priority
Medium — Brian requested. Addresses a core pain point: page objects go stale when UI changes, breaking tests silently.

## Summary
Build a drift detection system into the QA framework (py-selenium-framework-mcp / platform-selenium). When a developer changes the UI, the framework detects which page objects and selectors are affected and guides the developer to update them. Reduces the "tests worked yesterday, broken today" problem.

## Requirements
- Detect stale selectors: framework scans page objects, attempts to resolve selectors against the live app, flags failures
- Map selectors to pages: know which page object owns which selector, so drift reports are actionable
- Guide updates: when drift detected, tell the dev exactly which file + line + selector needs updating
- Integration with test run: optionally run drift check as a pre-test step or separate command
- Support the 4-layer architecture: drift detection operates at the Page Object layer (Layer 4)

## References
- Brian's request (2026-03-23 text conversation)
- py-selenium-framework-mcp (local reference implementation)
- isagawa-qa/platform-selenium (GitHub)
- Page Object layer: `framework/pages/{workflow_name}/{page_name}.py`
- Selectors are class constants (UPPER_SNAKE_CASE) in page objects

## Task Builder Input
- **Deliverable:** Drift detection module that scans page objects, resolves selectors against live app, reports stale selectors with file/line/selector details
- **Scope:** BUILD
- **Constraints:** Must work within existing 4-layer architecture. Needs a running app to test against (or headless browser). Output should be a drift report (JSON + human-readable).
