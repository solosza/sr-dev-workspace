# Refactor Isagawa.co Site Messaging: SDD Architecture

## Status
Open

## Priority
High — Current messaging contains overstated claims and "natural language" positioning that undermines credibility with technical buyers. Need precise "SDD architecture" terminology and removal of absolute language before local testing.

## Summary
The isagawa.co homepage is 70% correct but needs surgical refactoring: (1) Replace "spec-driven compilation" and "natural language" with "SDD architecture" terminology; (2) Remove overstated claims ("mechanically can't violate," "no human intervention") and replace with precise language; (3) Update hero copy and section subtitles to emphasize the kernel + domain specs + governance approach; (4) Clarify HITL capability (autonomous for deterministic, HITL for approvals/failures). All changes in feature branch, NO merge to main until local testing validates.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[142-market-refactor-isagawa-site-messaging/change-map]] | Exact page locations, current text, replacement text for all sections |
| [[142-market-refactor-isagawa-site-messaging/terminology-updates]] | Map of terms to replace (natural language → intent, compilation → SDD architecture, etc.) |
| [[142-market-refactor-isagawa-site-messaging/credibility-fixes]] | Overstated claims: locations, replacements, rationale |

## Requirements
- Remove all "natural language" claims from hero, growth, self-extension sections
- Replace "spec-driven compilation" with "SDD architecture"
- Update hero copy: new main heading + revised subtitle emphasizing architecture
- Tone down absolute language: "mechanically can't," "physically cannot," "no human intervention"
- Clarify HITL: "Autonomous for deterministic execution; HITL for approvals, failures, and judgment points"
- Update section subtitles to reflect SDD approach (not hype)
- All changes in `feature/spec-driven-framework-messaging` branch
- No merge to origin/main — local testing only

## References
- Feature branch: `feature/spec-driven-framework-messaging` (isagawa-co.github.io)
- Current site: `D:\my_ai_projects\isagawa-co.github.io\index.html`
- Kernel README (also needs tone alignment)

## Task Builder Input
- **Deliverable:** Refactored index.html + kernel.html with updated messaging
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** REFACTOR
- **Constraints:** Feature branch only, no merge to main, user will validate locally before merging
