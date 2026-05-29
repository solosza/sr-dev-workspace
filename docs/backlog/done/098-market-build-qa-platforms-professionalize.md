# Professionalize All QA Platform Repos and Landing Page

## Status
Open

## Priority
High — CIQ evaluating SSH platform now; their engineers will click through to other repos. Every public repo must look professional and have correct licensing.

## Summary
Update all public isagawa-qa platform repos with professional READMEs (modeled on platform-ssh), proprietary evaluation licenses, and accurate claims. Update the qa-platforms.html landing page to add the API platform, correct the "works with" messaging to Claude Code only, and ensure all repo links and descriptions are accurate.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[098-market-build-qa-platforms-professionalize/platform-selenium]] | Selenium repo README, license, accuracy |
| [[098-market-build-qa-platforms-professionalize/platform-playwright]] | Playwright repo README, license, accuracy |
| [[098-market-build-qa-platforms-professionalize/platform-docker]] | Docker repo README, license, accuracy |
| [[098-market-build-qa-platforms-professionalize/platform-deepeval]] | DeepEval repo README, license, accuracy |
| [[098-market-build-qa-platforms-professionalize/landing-page-updates]] | qa-platforms.html updates (add API, accuracy pass, "works with" messaging) |
| [[098-market-build-qa-platforms-professionalize/design-decisions]] | Licensing choice, compatibility claims, what to say about other agents |

## Architecture

```
isagawa-qa org (public repos)
├── platform-selenium    ← README + license update
├── platform-playwright  ← README + license update
├── platform-docker      ← README + license update
├── platform-deepeval    ← README + license update (currently private — make public?)
└── platform-ssh         ← DONE (backlog 097)

isagawa-co.github.io
└── qa-platforms.html    ← Add API platform, accuracy pass, "Built for Claude Code"
```

## Requirements
- Each repo gets a professional README following the platform-ssh pattern (problem, solution, architecture, quick start, project structure)
- Each repo gets the Proprietary Evaluation license (same as platform-ssh)
- No em-dashes, no AI-style filler text
- "Built for Claude Code" as the compatibility claim (no false promises about other agents)
- qa-platforms.html adds API platform entry and updates all references to 5-layer
- All GitHub repo descriptions updated to match new READMEs

## References
- Completed model: `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh` (backlog 097)
- Landing page: `D:\my_ai_projects\isagawa-co.github.io\qa-platforms.html`
- Repos need cloning: platform-selenium, platform-playwright, platform-docker, platform-deepeval

## Task Builder Input
- **Deliverable:** Professional READMEs and licenses across 4 repos + updated landing page
- **Location:** workspace (orchestration) + multiple external repos
- **Scope:** BUILD
- **Constraints:** Must clone each repo first, read existing code to write accurate READMEs. platform-ssh is the template. platform-deepeval is currently private (may need to stay private or be made public). Do not make compatibility claims about agents other than Claude Code.
