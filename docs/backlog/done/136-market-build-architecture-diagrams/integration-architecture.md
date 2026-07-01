# Integration Architecture Diagram

## Status
NEW — needs design

## Location
docs/architecture-diagrams/integration-architecture.svg

## What it shows
How Isagawa Kernel connects to external systems:
```
User Code → Kernel CLI → Hook Enforcement →
Playwright Browser Control → Assertion Verification →
Result Reporting → Gate Enforcement → Next Action
```

## Key elements to visualize
1. CLI entry point (user invokes kernel command)
2. Domain spec loading
3. Hook injection points (pre-execution, post-execution, error handling)
4. Playwright integration (browser control, network monitoring, screenshots)
5. Testing loop (assert → verify → gate)
6. Feedback to user (pass/fail/remediate)

## Audiences
- Browser automation engineers (how Kernel controls Playwright)
- Testing platform builders (how to integrate Kernel governance)
- Infrastructure teams (deployment + hook management)

## Dependencies
Depends on: diagram-specifications.md
