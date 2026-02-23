# Step 6: Build Generation Pipeline

## Goal

Implement LLM-based answer generation using retrieved context and prompt templates.

## Spec Reference

→ `_reference/generation-spec.md`

## Actions

1. **Read the generation spec** — interface contract, prompt templates, citation format
2. **Implement `GenerationInterface`** — concrete class following the spec
3. **Context injection** — format retrieved chunks into prompt context window
4. **Prompt templates** — externalized templates (not hardcoded), configurable per use case
5. **Citation references** — response includes references to source chunks used
6. **Provider-agnostic LLM interface** — swap models without changing generation logic
7. **Write integration tests** — mock LLM, verify prompt construction, citation extraction

## Key Decisions (Agent Makes During Build)

- LLM provider: OpenAI, Anthropic, local model
- Context window strategy: stuff all chunks vs map-reduce vs refine
- Citation format: inline references, footnotes, source list
- Prompt engineering: system prompt, few-shot examples, chain-of-thought

## Gate

→ See `gate-contract.md` Step 6 criteria
