# Create Pydantic Data Contracts

## Context
Pydantic models that define the data passed between pipeline modules. These are the testable interfaces between steps.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-project-structure

## Phase Gate
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/__init__.py` exists

## Requirements
- All models use Pydantic BaseModel
- Models:
  - `ExtractedIdentifier` — name, kind (table/column/schema/sp/temp/variable), positions (list of tuples), context (where found)
  - `ExtractionResult` — source_text, identifiers (list of ExtractedIdentifier), stats (dict)
  - `MappingEntry` — real_name, synthetic_name, kind, first_seen_file
  - `MappingStore` — entries (dict[str, MappingEntry]), metadata (dict), with load/save methods for JSON persistence
  - `ReplacementResult` — sanitized_text, replacements_made (int), mapping_snapshot (dict)
  - `LeakReport` — status (CLEAN/FLAGGED), flagged_tokens (list of dict with token/line/col/reason), scan_stats (dict)
  - `PipelineResult` — input_file, sanitized_text, leak_report (LeakReport), mapping_file (str)

## Acceptance Criteria
- [ ] `D:/my_ai_projects/sp-sanitizer/sp_sanitizer/contracts.py` exists
- [ ] All 7 models importable: `from sp_sanitizer.contracts import ExtractedIdentifier, ExtractionResult, MappingEntry, MappingStore, ReplacementResult, LeakReport, PipelineResult`
- [ ] Pydantic validation works (instantiation with valid data succeeds)

## Gates Satisfied
- BUILD-05, FUNC-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
