# SSH Compliance Testing Showcase Page

## Status
NEW — strong enterprise niche, build second

## Location
`D:\my_ai_projects\isagawa-co.github.io\projects\ssh-compliance\index.html`

## What It Does
Showcases the automated SSH compliance validation framework — tests SSH server configurations against STIG, CIS, NIST 800-171, FIPS 140-3, PCI-DSS, HIPAA, SOC 2, and ISO 27001 standards. Real enterprise value — automated compliance auditing that typically requires expensive tools.

## Content Sections

1. **Hero** — "Automated compliance validation for 8 security standards" + badge grid
2. **Problem** — Manual SSH compliance auditing is slow, error-prone, and expensive; standards overlap but tools don't cross-reference
3. **Standards Grid** — Visual grid showing all 8 supported standards with check counts
4. **Architecture** — Diagram: host configs → validators → compliance auditor → reports
5. **How It Works** — Example: validate a Rocky Linux 9 server against STIG in one command
6. **Tech Stack** — Python, Paramiko, Docker, pytest, YAML fixtures
7. **Results** — N validators, N checks across 8 standards, Docker-based testing

## Dependencies
- SSH compliance framework at `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test`
- Domain spec factory output specs for SSH validators
- 8 compliance validators (STIG, CIS, NIST, FIPS, PCI, HIPAA, SOC2, ISO27001)
