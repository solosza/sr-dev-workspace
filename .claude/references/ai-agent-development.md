# AI Agent Development

## State Management
- Explicit state over hidden state
- State files must be JSON (parseable, serializable)
- Commands update state, hooks verify state
- State is proof of work - can't fake it

## Tool/Command Design
- Single responsibility per tool/command
- Clear input/output contracts
- Exit codes: 0=pass, non-zero=fail, 2=block
- Smart blocks tell agent HOW to fix

## Prompt Engineering
- Instructions before data
- Structured format (headers, sections)
- No hardcoded prompts in code - use template files
- Token-aware chunking for long content

## Learning Loop
- Failure → Diagnose → Fix → Learn
- Soft enforcement: add to protocol (knowledge)
- Hard enforcement: add to hooks (prevention)
- Every lesson makes the kernel smarter

## Observability
- Audit trail for AI decisions
- State files track all workflow progress
- Hooks log blocks with fix instructions
