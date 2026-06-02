# Research: Release Manager — Release Discipline for isagawa-co.github.io

## Status
Open

## Priority
Medium — the isagawa site currently ships via ad-hoc git push from pipelines. No changelog, no version tags, no staged preview, no rollback procedure. As the site grows (10+ pages, QA platforms, job application product), release discipline matters. Research evaluates this as both a kernel integration and a standalone product opportunity.

## Summary
A release manager enforces a structured release cycle: changelog generation from commits, semantic versioning or date-based tags, staged preview (GitHub Pages preview branch or local), smoke tests before merge to main, and a rollback procedure. For isagawa-co.github.io this would prevent broken deployments and create an audit trail of what shipped when. The research also evaluates whether "release manager for GitHub Pages sites" is a standalone product worth building and selling.

## Requirements

### Kernel Integration Track
- Assess the current release gap: how do pipelines currently push to isagawa-co.github.io? What can break?
- Define a release workflow: feature branch → preview → smoke test → merge to main → tag
- Determine integration point: new kernel command `/kernel/release`, pre-push hook, or step appended to execute-pipeline for site pipelines?
- Evaluate changelog generation: auto-generate from commit messages (conventional commits), or require manual release notes?
- Define rollback procedure: git revert, branch restore, or GitHub Pages-specific mechanism?

### Standalone Product Track
- Who else has this problem? GitHub Pages users, small agencies, solo developers shipping static sites
- What does the competitive landscape look like? (Netlify, Vercel handle this for their platforms — what about raw GitHub Pages?)
- What would a standalone release-manager tool look like? CLI? GitHub Action? VS Code extension?
- Is there a viable distribution/monetization path, or is this kernel-only value?

## References
- Isagawa site: `D:/my_ai_projects/isagawa-co.github.io`
- Current pipeline that pushes site: various market-build-* backlogs in done/
- Backlog 117: frontend-design skill (aesthetic consistency — pairs with release consistency)
- GitHub Pages docs: deployment from main branch or gh-pages branch

## Task Builder Input
- **Deliverable:** Research report — gap assessment for current isagawa release process, recommended kernel integration design, and standalone product viability assessment (go / no-go with reasoning)
- **Location:** `subproject:release-manager-research`
- **Scope:** RESEARCH
- **Constraints:** Kernel integration must not add friction to existing execute-pipeline flow — release step should be optional/additive. Standalone product assessment should be honest about market size vs. build effort.
