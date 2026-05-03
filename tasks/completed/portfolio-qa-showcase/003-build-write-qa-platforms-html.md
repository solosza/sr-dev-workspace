# 003 — Write qa-platforms.html

**Type:** BUILD
**Depends on:** 002

## Goal
Write the full HTML page for the AI-native test automation showcase at `D:\my_ai_projects\isagawa-co.github.io\qa-platforms.html`.

## Requirements

Write a complete HTML page with these sections (match existing attestation.html and ssh-compliance.html patterns):

1. **Header nav** — ISAGAWA logo + links (Home, Feed, Attestation, SSH Compliance) + attested counter
2. **Loop badge** — "Every platform below was produced from a domain spec by the same system described on the homepage."
3. **Hero** — "Describe what to test. Get production-grade test code." with sub-copy explaining AI-native test automation across 5 platforms
4. **Problem section** — "UI tests are brittle. Every engineer writes them differently." — selector drift, inconsistency, unmaintainable AI-generated tests
5. **Architecture section** — 4-layer diagram (Page Object → Task → Role → Test) using flow-card pattern. Each layer: name, one-sentence responsibility, key rule
6. **How it works** — 4-step flow: "You describe → AI discovers → AI generates → You run" with explanation for each step
7. **Multi-platform grid** — 5 platform cards: Selenium (Python), Playwright (TypeScript), Docker (container testing), DeepEval (LLM eval), SSH (compliance). Each card: name, stack, what it tests, GitHub link
8. **Demo section** — Terminal animation showing test generation from plain English + pytest execution (content in JS file)
9. **Tech stack badges** — Python, TypeScript, Selenium, Playwright, pytest, Docker, MCP
10. **Results section** — stat cards: 5 platforms, 4-layer architecture, "Works with Claude Code, Cursor, Windsurf"
11. **Who this is for** — evidence cards for QA leads, engineering managers, teams adopting AI testing
12. **CTA** — link to isagawa-qa GitHub org
13. **Footer** — same pattern as attestation.html

Reference:
- Use attestation.html as the structural template (same class names, same section patterns)
- Content from `D:\my_ai_projects\py_sel_framework_mcp\ARCHITECTURE.md` for architecture section
- Platform info from backlog 073

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-co.github.io\qa-platforms.html` exists with all 13 sections
