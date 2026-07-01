# Research Legal and IP

## Context
Users submit artifacts that may contain proprietary logic. The agent builds components from _reference/ patterns. Clean IP boundaries between user submissions, platform-generated components, and the open source framework are essential.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001

## Requirements
- Research component ownership:
  - Components built by the agent using _reference/ patterns — are they platform-generated or derived from user submissions?
  - Precedent from similar platforms (GitHub Copilot IP debate, Hugging Face model uploads)
  - Recommended ownership model: platform owns generated components, user retains submission IP
- Research user submission boundaries:
  - Submitted artifacts processed but not retained vs retained for platform improvement
  - Opt-in contribution model (user consents to component extraction)
  - Clear data flow: what enters the container, what leaves, what gets merged
- Research Terms of Service implications:
  - User grants limited license for processing
  - Platform disclaims liability for eval results
  - Indemnification for API key usage
  - DMCA / takedown process for component disputes
- Research open source licensing:
  - Framework OSS (MIT/Apache 2.0) + hosted platform commercial (dual licensing)
  - Component library licensing: platform-generated = platform license, contributed = CLA
  - Precedent: MongoDB SSPL, Elastic license, HashiCorp BSL
  - Risk: OSS fork competes with hosted platform
- Use WebSearch for ToS examples from comparable platforms and recent IP rulings on AI-generated code

## Acceptance Criteria
- [ ] File `projects/eval-web-app-research/08-legal-ip.md` exists
- [ ] Contains component ownership analysis with recommendation
- [ ] Contains user submission boundary definition
- [ ] Contains Terms of Service framework
- [ ] Contains open source licensing analysis with recommendation
- [ ] Minimum 400 words

## Gates Satisfied
DOC-22, DOC-23, DOC-24

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
