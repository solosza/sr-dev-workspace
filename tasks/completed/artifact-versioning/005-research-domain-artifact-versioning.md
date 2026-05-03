# Task 005: Research — Domain vs Kernel Artifact Versioning Strategy

## Objective
Design how domain-specific artifacts (commands, skills, protocols) version independently from kernel artifacts.

## Instructions

1. Read the existing report sections from tasks 001-004
2. Analyze the two artifact categories:
   - **Kernel artifacts** — shared across all repos (commands, hooks, skills, CLAUDE.md template)
   - **Domain artifacts** — repo-specific (domain protocol, domain commands, domain skills, domain specs)
3. Design a dual-versioning strategy:
   - How to distinguish "kernel v2.1 + domain-healthcare v1.3"
   - Whether domain artifacts get their own manifest section
   - How domain-setup stamps the domain version
   - Whether domain specs (from spec-factory) carry their own version
4. Address edge cases:
   - A domain skill that wraps a kernel command — whose version is it?
   - A protocol that references both kernel and domain patterns — which version matters?
   - Repos that have kernel but no domain (vanilla kernel) — version string format
5. Write findings as `## 5. Domain-Specific Artifact Versioning` in the report

## Acceptance Criteria
- Kernel vs domain distinction clearly defined
- Dual-version notation proposed (e.g., `kernel@2.1 + domain@1.3`)
- Edge cases addressed

## Gate
RESEARCH-05
