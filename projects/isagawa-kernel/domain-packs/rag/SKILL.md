# RAG Domain Pack

Build a Retrieval-Augmented Generation system from specification.

## Overview

This pack teaches an AI agent to build a complete RAG pipeline — from raw documents to generated answers — using markdown specifications instead of reference code. The agent builds from spec, guided by interface contracts and quality gates.

## Workflow

| Step | Action | Reference |
|------|--------|-----------|
| 1 | Project setup | → `steps/step-01-setup.md` |
| 2 | Build chunking pipeline | → `steps/step-02-chunking.md` |
| 3 | Build embedding pipeline | → `steps/step-03-embedding.md` |
| 4 | Set up vector store | → `steps/step-04-vector-store.md` |
| 5 | Build retrieval pipeline | → `steps/step-05-retrieval.md` |
| 6 | Build generation pipeline | → `steps/step-06-generation.md` |
| 7 | Build evaluation harness | → `steps/step-07-evaluation.md` |

→ Full data flow: [`workflow.md`](workflow.md)
→ Validation rules: [`gate-contract.md`](gate-contract.md)

## Reference Specs

| Spec | Purpose | Reference |
|------|---------|-----------|
| Architecture | System overview + anti-patterns | → `_reference/README.md` |
| Chunking | Document splitting strategies | → `_reference/chunking-spec.md` |
| Embedding | Vector encoding interface | → `_reference/embedding-spec.md` |
| Vector Store | Storage + indexing interface | → `_reference/vector-store-spec.md` |
| Retrieval | Query + similarity search | → `_reference/retrieval-spec.md` |
| Generation | LLM integration + prompts | → `_reference/generation-spec.md` |
| Evaluation | Quality metrics + test harness | → `_reference/evaluation-spec.md` |
| Config | Environment + tuning parameters | → `_reference/config-spec.md` |

## Key Principles

- **Spec-driven** — Build from markdown specifications, not reference code
- **Interface-first** — Define contracts before implementations
- **Tiered Index Architecture** — Every file is index or payload, never both
- **Gate-enforced** — Each step has pass/fail criteria checked before proceeding
