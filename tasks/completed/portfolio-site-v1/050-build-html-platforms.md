# Build HTML Platforms Section

## Context
Adds the QA platforms section to index.html showcasing the five AI-native test automation platforms.

## Type
BUILD

## Execution
inline

## Dependencies
- 049

## Requirements
- Add a `<section id="platforms">` to index.html after the catalog section
- Heading (h2): "AI-Native Test Automation"
- Subheading (p): "Five platforms. One architecture. Every testing layer covered."
- 5 platform cards, each with platform name, testing layer, and technology:
  1. **Selenium** | UI / Web | Python, Selenium WebDriver
  2. **Playwright** | Browser | TypeScript, Playwright
  3. **Docker** | Container Images | Python, Docker SDK
  4. **DeepEval** | LLM Evaluation | Python, DeepEval
  5. **SSH** | Infrastructure / Compliance | Python, Paramiko
- Each card should have consistent class for styling (e.g., `.platform-card`)

## Acceptance Criteria
- [ ] Section element exists with id="platforms"
- [ ] H2 heading matches: "AI-Native Test Automation"
- [ ] Subheading matches: "Five platforms. One architecture. Every testing layer covered."
- [ ] Five platform cards present with correct names, layers, and technologies
- [ ] Cards have consistent CSS class for styling

## Gates Satisfied
BUILD-11

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
