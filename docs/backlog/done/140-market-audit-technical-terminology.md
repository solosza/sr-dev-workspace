# Audit & Update Technical Terminology

## Status
Open

## Priority
Medium — Terminology is precise internally but creates accessibility barriers for newcomers; needs consistent definitions and alternatives

## Summary
The Isagawa framework uses precise technical terms ("domain spec," "harness," "enforcement loop," "gate contract") that are correct but often confusing to audiences unfamiliar with the pattern. This backlog covers auditing terminology usage across documentation and marketing materials, defining each term clearly, and identifying where simpler language or analogies would improve accessibility without losing precision.

## Requirements
- Audit terminology usage across isagawa.co, Kernel README, and core documentation
- Create terminology glossary with definitions + accessibility-first language alternatives:
  - "domain spec" → sometimes "behavioral spec" or "spec" depending on context
  - "harness" → "test framework" or "testing infrastructure" (context-dependent)
  - "enforcement loop" → "verification + enforcement cycle" (more descriptive)
  - "gate contract" → "validation gate" or "assert-then-gate pattern"
  - "domain setup" → "infrastructure initialization"
- Identify where terminology is essential (technical docs) vs. where alternatives improve accessibility (marketing, homepage)
- Create content strategy: which terms stay precise, which get simplified, where to add explanatory callouts
- Coordinate with backlog 137 (README tone) for documentation consistency
- Coordinate with backlog 135 (homepage messaging) for marketing consistency

## References
- Backlog 135: Homepage messaging update
- Backlog 137: Kernel README refactor
- Backlog 138: Audience-specific messaging
- Current Kernel documentation and isagawa.co copy

## Task Builder Input
- **Deliverable:** Terminology glossary + content guidance (which terms to use in which contexts)
- **Location:** `subproject:isagawa-terminology-guide`
- **Scope:** RESEARCH + BUILD
- **Constraints:** Must coordinate with backlogs 135, 137, 138 for consistency; no merge to main until testing complete per user constraint
