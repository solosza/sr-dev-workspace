# AI Harness Engineering Job Search

## Status
Open

## Priority
High — active job search targeting top AI companies

## Summary
Research and compile harness engineering / AI agent infrastructure roles at top AI companies that match my skillset. Use the AI agent architect resume and full innovation inventory as matching criteria. Save job URLs in a format consumable by the job application automation platform (backlog 005). This is NOT a QA job search — target agent platform, harness, infrastructure, evaluation, and developer tools roles.

## What I Built (Matching Profile)

**The Isagawa Kernel** — an AI management layer that sits on top of Claude Code and makes AI agents reliable over long tasks. Application-level infrastructure, built on Claude Code's hook system.

### Core system
- **Mechanical enforcement** — Hook pipeline that blocks agent tool calls until compliance conditions are met. Not advisory guidance — actual blocks. 5 hooks working together.
- **Work loop** — session-start → anchor (forced protocol re-read every N actions) → work → learn (after failures) → complete. Prevents the drift that degrades agent output over long sessions.
- **Self-building setup** — Agent scans any repo, discovers its patterns, and writes its own protocol + enforcement. No templates or configuration needed.

### What makes it useful
- **Spec-Driven Development (SDD)** — Domain expertise packaged as installable specs. Kernel = constant management. Spec = variable expertise. Drop a spec into any project, agent builds to that domain's standards. Strongest original contribution — Kiro/Spec Kit/BMAD are adjacent but none have the enforcement piece.
- **End-to-end delivery pipeline** — `/kernel/backlog` → `/kernel/task-builder` (atomic decomposition + gate contracts) → `run-task.sh` (headless batch execution with session resume) → `/kernel/complete`. One sentence to verified artifact.
- **Spec factory** — 12-step system with its own commands (`/spec-factory-score`, `/spec-factory-build`, `/spec-factory-run`). Audit → score (8-dimension model) → design → write from original research → validate → push. 14 specs manufactured through it.
- **Production test system** — Assembles master repo, copies to disposable test repo, runs inner agents under enforcement. Tests deliverables the way they'll actually be used.
- **Job application submission pipeline** — End-to-end workflow from positioning research (backlog 003) → resume AI pipeline (tailored resume per job) → job-application-spec (structured submission automation, backlog 005). Another full e2e system — research to application with no manual steps between stages.

### Portfolio evidence
Built and shipped solo. Not prototypes — working systems used to produce real output.

## Portfolio Evidence

- **37 published repos** across 2 GitHub orgs (isagawa-co, isagawa-qa)
- **24 domain specs** — QA, health insurance, DevOps, security/compliance, real estate
- **14 specs manufactured autonomously** via the spec factory
- **6 platforms shipped** — Selenium, Playwright, Docker, DeepEval, SSH, Zentyent
- **Other tools** — SP Sanitizer (7-module T-SQL pipeline), Resume AI Pipeline

## Requirements
- Master resume: `D:\my_python_projects\resume-ai-pipeline\resumes\ai-agent-architect-resume.md`
- Target companies: Anthropic, OpenAI, Google DeepMind, Meta AI, xAI, Cohere, Mistral, Databricks, Scale AI, Hugging Face, and others with agent infrastructure teams
- Target roles: AI agent platform engineer, harness/infrastructure engineer, evaluation infrastructure, developer tools/DX engineer, AI safety infrastructure — NOT QA
- Priority: fully remote positions
- Will consider relocation for top-tier companies (Anthropic, OpenAI, Google DeepMind)
- Save each job as structured data with URL, company, title, location, remote status, match score
- Output format must be compatible with job-application-spec pipeline (backlog 005)

## References
- Master resume: `D:\my_python_projects\resume-ai-pipeline\resumes\ai-agent-architect-resume.md`
- Resume pipeline repo: `D:\my_python_projects\resume-ai-pipeline\`
- Job application automation: `docs/backlog/005-domain-build-job-application-automation.md`
- Job application spec repo: `C:\Users\solos\my_ai_projects\job-application-spec`
- isagawa-co repos: https://github.com/orgs/isagawa-co/repositories
- isagawa-qa repos: https://github.com/orgs/isagawa-qa/repositories

## Task Builder Input
- **Deliverable:** Curated list of matching jobs with URLs, match scores, and structured data ready for job-application-spec pipeline
- **Scope:** RESEARCH
- **Constraints:** Needs web access for job board searches. Resume file must exist. Output format must align with backlog 005 job-application-spec. Human review required for final application decisions.
