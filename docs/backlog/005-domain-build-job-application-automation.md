# Backlog 005: Job Application Form Automation

## Status
Open

## Priority
Medium — useful when applying at volume (Phase 2/3 of resume-ai-pipeline)

## Summary
Use the Isagawa QA automation platform (Selenium or Playwright) to automate job application form submissions. The resume-ai-pipeline already generates tailored resumes and cover letters per job. This closes the loop by automating the actual submission. Same problem the platform already solves: navigate to URL, locate fields, fill data from structured source, submit, verify confirmation.

## Why This Fits
Job application forms (Greenhouse, Lever, Workday, etc.) are standard HTML forms with predictable field patterns. The QA platform already handles form interaction, file uploads, dropdown selection, and submission verification. This is a natural extension, not a new capability.

## Target Platforms
| ATS | Used By | Form Pattern |
|-----|---------|-------------|
| Greenhouse | Anthropic, many startups | Standard HTML form, file upload for resume |
| Lever | Mid-size tech companies | Similar pattern |
| Workday | Enterprise (Fortune 500) | More complex, multi-page |
| Custom | Varies | Case-by-case |

## Data Flow
```
resume-ai-pipeline (generates content)
    ↓
application-data.json (structured answers per job)
    ↓
QA platform (fills form, uploads resume, submits)
    ↓
confirmation screenshot / verification
```

## Field Categories (Greenhouse Example)
| Category | Fields | Source |
|----------|--------|--------|
| Personal info | Name, email, phone, LinkedIn | Static config (reusable) |
| Yes/No questions | Visa, relocation, in-office, prior interview | Static config |
| Essays | "Why [company]?", cover letter | Generated per job by resume-ai-pipeline |
| Resume upload | PDF file | Generated per job by resume-ai-pipeline |
| EEOC | Gender, race, veteran, disability | Static config (optional) |

## Implementation Approach
- Page Object per ATS platform (Greenhouse first)
- Config-driven: personal info in shared config, per-job answers in job-specific JSON
- Resume-ai-pipeline outputs job-specific JSON alongside HTML resume
- File upload handling for resume PDF
- Confirmation page verification (screenshot + assertion)
- Dry-run mode: fill all fields but don't submit (for review)

## When to Build
- **Not now:** 3 manual applications don't justify the setup cost
- **Phase 2:** When resume-ai-pipeline scrapes job listings and generates resumes in batch
- **Phase 3:** Full end-to-end: scrape jobs, generate resume, fill application, submit, track status

## Dependencies
- resume-ai-pipeline Phase 2 (job scraping + batch generation)
- Structured output format from resume-ai-pipeline (JSON with form answers)
- Platform page objects for target ATS systems

## References
- resume-ai-pipeline: github.com/solosza/resume-ai-pipeline
- Greenhouse form field analysis: FDE role (4985877008) fully mapped
- QA platforms: isagawa-qa/platform-selenium, isagawa-qa/platform-playwright

## Task Builder Input
- **Deliverable:** Page objects for Greenhouse/Lever ATS forms, config-driven form filler, dry-run mode, integration with resume-ai-pipeline output
- **Scope:** BUILD
- **Constraints:** Depends on resume-ai-pipeline Phase 2 (batch generation). Uses QA platform (Selenium or Playwright). Phase 2/3 work — not immediate.
