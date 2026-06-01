# Write job-application.js

## Context
The JavaScript for job-application.html. Must include the same scroll reveal + hero entrance logic from vibe-coder.js. The terminal animation section is replaced with a job-application-specific demo animation. The agent MUST read vibe-coder.js in full before writing.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-market-build-feature-branch

## Phase Gate
- [ ] Branch `feature/job-application-page` is checked out

## Requirements

**CRITICAL — READ FIRST:** Read `D:/my_ai_projects/isagawa-co.github.io/vibe-coder.js` in full before writing.

**File:** `D:/my_ai_projects/isagawa-co.github.io/job-application.js`

**Copy these sections verbatim from vibe-coder.js:**
1. Scroll Reveal block — `IntersectionObserver` watching `.reveal` elements
2. Hero Entrance block — `document.querySelector('.hero').classList.add('entered')`

**Replace the terminal animation section with a job-application demo animation:**
- Use the same IIFE pattern, same `terminalBody` / `terminalLines` structure as vibe-coder.js
- Terminal ID: `demoTerminal` (same element ID, so HTML can reuse the same demo-terminal section)
- Lines should show the AI discovering and filling a job application form:
  ```
  { type: 'command', text: '$ /apply --url "https://jobs.example.com/apply/12345"' },
  { type: 'prompt', text: '> Scanning form fields...' },
  { type: 'text', text: '  Found 14 fields: name, email, phone, address,' },
  { type: 'text', text: '  linkedin, github, resume, cover_letter, work_auth...' },
  { type: 'blank', text: '' },
  { type: 'prompt', text: '> Matching profile...' },
  { type: 'success', text: '✓ 14/14 fields matched from profile' },
  { type: 'blank', text: '' },
  { type: 'prompt', text: '> Preview ready. Review before submitting.' },
  { type: 'text', text: '  name: Alex Johnson' },
  { type: 'text', text: '  email: alex@example.com' },
  { type: 'text', text: '  linkedin: linkedin.com/in/alexjohnson' },
  { type: 'blank', text: '' },
  { type: 'recommendation', text: '  [REVIEW] All fields look correct.' },
  { type: 'blank', text: '' },
  { type: 'prompt', text: '> Submit? (Y/n): Y' },
  { type: 'success', text: '✓ Application submitted. Confirmation: #JA-48291' }
  ```
- Same typewriter effect, same LOOP_DELAY, CHAR_DELAY, LINE_DELAY constants
- Same `animateTerminal()` loop structure

## Acceptance Criteria
- [ ] `D:/my_ai_projects/isagawa-co.github.io/job-application.js` exists
- [ ] File contains `IntersectionObserver`
- [ ] File contains `entered` (hero entrance)
- [ ] File is at least 40 lines

## Gates Satisfied
- BUILD-04, FUNC-11, FUNC-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
