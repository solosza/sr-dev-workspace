# Catalog Data

## Status
NEW

## Overview
Full spec catalog for the Catalog section. Organized by vertical. Each entry includes spec name, type, and one-line description.

## IT & Security (9 specs)

| Spec | Type | Description |
|------|------|-------------|
| hipaa-audit-spec | OPERATE | HIPAA compliance audit lifecycle for healthcare organizations |
| pci-dss-spec | OPERATE | PCI DSS v4.0 compliance assessment for payment processors |
| sox-audit-spec | OPERATE | SOX/COSO/PCAOB internal control audit cycle |
| aml-kyc-spec | OPERATE | BSA program lifecycle — AML/KYC compliance agent |
| incident-response-spec | OPERATE | PICERL incident response lifecycle |
| soc-automation-spec | OPERATE | SOC automation — alert triage to remediation |
| iac-security-spec | BUILD | Infrastructure-as-code security scanning and remediation |
| auth-um-spec | BUILD | Authentication and user management testing |
| network-automation-spec | BUILD | Network configuration automation and validation |

## Healthcare Operations (4 specs)

| Spec | Type | Description |
|------|------|-------------|
| healthcare-qa-spec | WORKSPACE | Healthcare insurance QA automation — 18-step claims testing |
| claims-testing-spec | BUILD | Claims processing test automation |
| benefits-config-spec | BUILD | Benefits configuration validation |
| edi-testing-spec | BUILD | EDI transaction testing (837/835/270/271) |

## QA & Test Automation (5 platforms)

| Spec | Type | Description |
|------|------|-------------|
| platform-selenium | BUILD | UI/web test automation — Python/Selenium, 5-layer architecture |
| platform-playwright | BUILD | Browser test automation — TypeScript/Playwright |
| platform-docker | BUILD | Container image testing — Python/Docker SDK |
| platform-deepeval | BUILD | LLM evaluation platform — DeepEval framework |
| platform-ssh | BUILD | SSH infrastructure/compliance testing |

## DevOps & CI/CD (6 specs)

| Spec | Type | Description |
|------|------|-------------|
| azure-devops-spec | WORKSPACE | Azure DevOps pipeline operations |
| azure-devops-generator-spec | BUILD | Azure DevOps pipeline YAML generation |
| gitlab-ci-spec | WORKSPACE | GitLab CI pipeline operations |
| gitlab-ci-generator-spec | BUILD | GitLab CI pipeline YAML generation |
| github-actions-spec | WORKSPACE | GitHub Actions workflow operations |
| github-actions-generator-spec | BUILD | GitHub Actions workflow YAML generation |

## Real Estate & Finance (1 spec)

| Spec | Type | Description |
|------|------|-------------|
| lease-option-spec | OPERATE | Lease option wholesaling pipeline — 37 validated gates |

## Creative & Product (4 specs)

| Spec | Type | Description |
|------|------|-------------|
| content-production-spec | BUILD | Multi-platform social media content from single topic input |
| game-engine | BUILD | AI-powered game development — guided GDD creation + autonomous build |
| terminal-game-builder-spec | BUILD | ASCII terminal game builder (roguelike, sports, 4X, puzzle) |
| vibe-coder-spec | WORKSPACE | AI development partner for non-technical founders — 5-phase workflow |

## AI & Agent Operations (3 specs)

| Spec | Type | Description |
|------|------|-------------|
| ai-system-tuning-spec | OPERATE | AI system performance tuning and optimization |
| job-application-spec | BUILD | Autonomous job application form discovery and filling |
| platform-deepeval-spec | BUILD | DeepEval LLM evaluation domain spec |

## Summary Counts

| Vertical | Count | BUILD | WORKSPACE | OPERATE |
|----------|-------|-------|-----------|---------|
| IT & Security | 9 | 3 | 0 | 6 |
| Healthcare | 4 | 3 | 1 | 0 |
| QA & Testing | 5 | 5 | 0 | 0 |
| DevOps | 6 | 3 | 3 | 0 |
| Real Estate | 1 | 0 | 0 | 1 |
| Creative | 4 | 3 | 1 | 0 |
| AI/Agent Ops | 3 | 2 | 0 | 1 |
| **Total** | **32** | **19** | **5** | **8** |

## Notes
- Some specs appear in both isagawa-co (spec) and isagawa-qa (platform) orgs
- DevOps specs come in base+generator pairs (same vertical, different output)
- QA platforms are the most tangible — they produce running test automation
