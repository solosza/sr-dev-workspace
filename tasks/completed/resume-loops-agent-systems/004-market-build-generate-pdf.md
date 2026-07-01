# Generate Resume PDF from Updated Markdown

## Context
Convert the rewritten markdown resume to PDF using fpdf2 and DejaVu fonts. Same generation approach as previous version.

## Type
BUILD

## Execution
inline

## Dependencies
- 003-market-build-rewrite-resume-md

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-architect.md` has been updated with loops/agent systems framing

## Requirements
- Use fpdf2 library for PDF generation
- Use DejaVu fonts from `C:/Windows/Fonts/DejaVuSans*.ttf`
- Generate PDF at `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-architect.pdf`
- Keep PDF under 60KB, max 4 pages
- Preserve prose formatting (no bullets rendering as bullets)

## Acceptance Criteria
- [ ] File exists: `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-architect.pdf`
- [ ] PDF is under 60KB
- [ ] PDF is 4 pages or fewer

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
