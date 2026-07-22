# Test Wikilinks vs Code Spans as Read Signals

## Context
Compare whether `→ [[path]]` (wikilinks) or `` `path` `` (code spans) gives Claude a stronger signal to read the referenced file. The convention that most reliably triggers file reads should win.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Review Claude Code's tool use behavior: what text patterns trigger the Read tool?
- Check existing kernel behavior: when the agent encounters `→ [[references/step-01.md]]` vs `` `references/step-01.md` ``, does it read the file?
- Search Claude Code docs for any documented file reference patterns
- Analyze: does the arrow prefix `→` add signal beyond bare wikilinks?
- Document findings with concrete examples
- Write results to `tasks/linking-convention-research/wikilink-vs-codespan-results.md`

## Acceptance Criteria
- [ ] Results document exists at `tasks/linking-convention-research/wikilink-vs-codespan-results.md`
- [ ] Contains comparison of read-trigger strength for each format
- [ ] Includes recommendation based on observed behavior

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
