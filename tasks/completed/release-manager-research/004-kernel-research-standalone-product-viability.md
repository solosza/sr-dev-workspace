# Research: Standalone Product Viability

## Context
Assess whether "release manager for GitHub Pages sites" is a standalone product worth building — separate from the kernel integration track.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002-kernel-research-assess-release-gap.md

## Phase Gate
- [ ] `projects/release-manager-research/release-gap-assessment.md` exists

## Requirements
- Identify the target audience: GitHub Pages users, small agencies, solo developers with static sites
- Assess competitive landscape: Netlify/Vercel handle this for their platforms — what's the gap for raw GitHub Pages users?
- Research existing tools: any GitHub Actions for release management of static sites?
- Assess distribution options: CLI tool, GitHub Action, VS Code extension — which is most viable?
- Assess monetization: open source + paid tier? One-time purchase? Is there a viable path?
- Honest size-of-market estimate: how many people have this problem AND would pay?
- Write to `projects/release-manager-research/standalone-product-assessment.md`

## Acceptance Criteria
- [ ] `projects/release-manager-research/standalone-product-assessment.md` exists
- [ ] File covers competitive landscape (Netlify, Vercel, GitHub Actions)
- [ ] File assesses distribution options
- [ ] File has honest go/no-go on standalone product

## Gates Satisfied
- DOC-06, DOC-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
