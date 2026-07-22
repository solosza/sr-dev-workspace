# Personal Skill Path — On-Prem LLM Skills for Job Hunting

## Context
Independent of the Isagawa pivot, the user wants these skills personally — for job hunting and career leverage. This complements the active AI-harness job search (pipeline 029). Produces `projects/on-prem-llm-pivot-research/04-personal-skill-path.md`.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] `projects/on-prem-llm-pivot-research/02-solution-landscape.md` exists

## Requirements
- Read 02 output first — skills map to the landscape tiers
- Skill inventory: GPU infrastructure basics, model serving (vLLM/Ollama/NIM), quantization (GGUF/AWQ), fine-tuning (LoRA), private RAG, security/compliance for AI deployments
- Job-market check (web research, sourced): which roles/titles demand these (ML infra engineer, LLMOps, AI platform engineer, solutions architect), sample postings, how they overlap with the user's agent-harness positioning from pipeline 029
- Portfolio projects that SIGNAL the skills cheaply — ideally reusing existing assets (e.g., run the Isagawa Kernel loop against a local model via Ollama on consumer hardware; publish the writeup)
- Produce a 30-60-90 day plan: what to learn/build/publish each phase, with concrete first steps and hardware assumptions (what's doable on the user's current machine vs needs cloud GPU rental)
- Write `projects/on-prem-llm-pivot-research/04-personal-skill-path.md`

## Acceptance Criteria
- [ ] `projects/on-prem-llm-pivot-research/04-personal-skill-path.md` exists
- [ ] Contains a 30-60-90 (time-phased) plan
- [ ] Names target job titles with sourced examples
- [ ] Includes ≥ 2 portfolio project suggestions reusing existing Isagawa assets

## Gates Satisfied
- RSCH-07, RSCH-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
