# Build: Targeted Resume Pair (AI Agent + AI QA)

## Status
Open

## Priority
High — active job search, resumes need to reflect current skillset and market positioning

## Summary
Research the current AI agent and AI QA job markets, analyze the user's skillset against market demand, determine the best positions to target, then produce two tailored resumes: one optimized for AI agent engineering roles and one for AI QA engineering roles. This replaces the existing single-purpose resume with a targeted pair that maximizes interview conversion for each track.

## Requirements

### Part 1: Research
- Analyze current AI agent job market (what companies want, hot skills, role titles)
- Analyze current AI QA job market (what companies want, automation frameworks, role titles)
- Review user's skillset from existing resume and kernel/portfolio work
- Determine best position titles and target companies for each track
- Identify gaps between current positioning and market demand
- Produce a positioning strategy: what to emphasize for each resume variant

### Part 2: Resume Review
- Read existing resumes at `D:\my_ai_projects\project_test_repos\job-application-spec\resumes\`:
  - `alain-ignacio-ai-agent-architect.md` (current AI agent resume)
  - `alain-ignacio-ai-agent-architect.pdf` (PDF version)
  - `alain-ignacio-qa-architect.md` (current QA resume)
- Identify what's working, what's missing, what needs repositioning
- Cross-reference against Part 1 research findings

### Part 3: Build Two Resumes
- **AI Agent Resume:** Optimized for AI agent engineering, infrastructure, and agentic systems roles
- **AI QA Resume:** Optimized for AI-powered QA, test automation, and quality engineering roles
- Both in markdown format (PDF generation handled separately)
- Both must reflect the user's actual work (isagawa-kernel, QA platforms, agent orchestration)
- Prose-only format (no bullet points) — matches existing resume style

## References
- Existing resumes: `D:\my_ai_projects\project_test_repos\job-application-spec\resumes\`
- Prior job search: pipeline 029, projects/ai-harness-job-search/
- Profile: `D:\my_ai_projects\project_test_repos\job-application-spec\profile.json`
- Kernel portfolio: isagawa-co org (kernel, observatory) + isagawa-qa org (QA platforms)

## Task Builder Input
- **Deliverable:** 2 updated resume markdown files + positioning research report
- **Location:** workspace:D:\my_ai_projects\project_test_repos\job-application-spec\resumes
- **Scope:** BUILD
- **Constraints:** Must read existing resumes before modifying. Prose-only format (no bullets). Research informs resume content — sequential dependency. PDF generation is out of scope (separate step).
