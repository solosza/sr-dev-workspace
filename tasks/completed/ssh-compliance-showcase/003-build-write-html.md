# 003 — Write SSH Compliance HTML

## Type
BUILD

## Description
Write `ssh-compliance.html` in `D:\my_ai_projects\isagawa-co.github.io`. Product showcase page for the SSH compliance testing platform.

### Content sections (from backlog 072):
1. **Loop badge** — "This platform was built by the same system described on the homepage." + link
2. **Hero** — "Automated SSH compliance against four federal frameworks." Subtitle about continuous compliance replacing manual audits.
3. **Problem** — SSH configs drift. Manual audits take days. You find out you are non-compliant when the auditor does. Continuous compliance should not require continuous human effort.
4. **Frameworks** — Four evidence cards: STIG (DoD hardening), CIS Benchmarks Level 1 (industry baselines), NIST 800-171 (CUI protection), FIPS 140-3 (crypto validation). Each with brief description.
5. **How it works** — Flow: host config (fixture) → validator selection → pytest execution → compliance report. Flow cards matching attestation page style.
6. **Architecture** — 5-layer diagram: Test → Role → Validator → Task → Interface. Fixture-driven. New host = new JSON. New framework = new validator.
7. **Tech stack** — badges: Python, pytest, Paramiko, STIG, CIS, NIST, FIPS
8. **Results** — stat cards: 4 frameworks, validators count, compliance checks count
9. **Who this is for** — DevSecOps, government contractors, security teams, MSPs
10. **CTA** — View on GitHub link to isagawa-qa/platform-ssh
11. **Footer** — matching site footer

### Writing rules:
- NO dashes in content copy (no em-dashes, no hyphens-as-dashes). Use periods, commas, or rewrite.
- Human-like writing. Natural flowing sentences.
- Product-first framing. The SSH compliance platform is its own product, not just a kernel demo.

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-co.github.io\ssh-compliance.html` exists
- [ ] Links to `ssh-compliance.css`
- [ ] Contains all 11 content sections
- [ ] No em-dashes or hyphens used as dashes in content
- [ ] Links to isagawa-qa/platform-ssh GitHub repo
