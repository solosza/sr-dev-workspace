# Stat Number Consistency

## Status
EXISTS (needs enhancement)

## Location
`D:\my_ai_projects\isagawa-portfolio-site\index.html`

## Problem
Three evidence cards are missing stat numbers, creating visual asymmetry within their rows.

## Fixes

### Growth section: Workspaces card
- Currently: no stat
- Fix: add `<span class="evidence-stat">GOVERNED</span>` (verb phrase in --font-mono, --accent, same display size as numbers)

### Self-Extension section: Website Cloner card
- Currently: no stat
- Fix: add `<span class="evidence-stat">122</span>` (token categories extracted from 2 reference sites across 13 extraction files)

### Self-Extension section: Attestation Pipeline card
- Currently: no stat
- Fix: add `<span class="evidence-stat">5</span>` (signed pipelines to date: #046, #047, #050, #051, #052)

## Evidence
- 122 token categories: counted from `D:\my_ai_projects\isagawa-portfolio-site\extraction\` (13 JSON files, excluding `source` and `extracted` metadata keys)
- 5 signed pipelines: counted from `.claude/state/attestations/` (unique pipeline numbers)
