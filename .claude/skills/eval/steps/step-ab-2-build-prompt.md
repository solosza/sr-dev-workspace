# Step AB-2: Build Prompt

Build the task prompt that will be executed against both variants (flat and tiered) during the A/B experiment.

## Input

| Field | Source | Example |
|-------|--------|---------|
| `artifact_content` | Output of Step AB-1 | Flattened/tiered skill content |
| `config` | Experiment config | `{ "task_prompt": "...", "auto_generate": true }` |
| `target` | Output of Step 0 | `domain-setup` |

## Procedure

1. **Check for provided prompt:**
   ```
   if config.task_prompt is not None and config.task_prompt != "":
       prompt = config.task_prompt
       mode = "provided"
   else:
       mode = "auto-generated"
   ```

2. **Auto-generate prompt (if no provided prompt):**

   Read the artifact content and produce a realistic task that exercises 3+ distinct steps of the artifact's workflow.

   Template for LLM auto-generation:
   ```
   You are analyzing a skill/command artifact for "{target}".

   Artifact content:
   {artifact_content}

   Generate a realistic user task that:
   - Exercises at least 3 steps of this artifact's workflow
   - Is specific enough to produce verifiable output
   - Represents a real-world use case, not a toy example

   Output format:
   TASK: <the task prompt>
   EXPECTED: <brief description of what correct output looks like>
   ```

3. **Parse auto-generation output:**
   ```
   task_prompt = extract_task_line(llm_response)
   expected_output = extract_expected_line(llm_response)  # optional
   ```

4. **Validate prompt:**
   - `task_prompt` is non-empty (len > 10 characters)
   - Prompt references concepts present in the artifact (keyword overlap check)
   - Prompt implies multi-step execution (not a single yes/no question)

## Verification

| ID | Check | Method | Pass |
|----|-------|--------|------|
| GAB2.1 | Prompt non-empty | `len(task_prompt) > 10` | True |
| GAB2.2 | Exercises workflow | Keyword overlap with artifact > 2 terms | True |
| GAB2.3 | Multi-step task | Prompt implies 3+ actions | True |
| GAB2.4 | Mode recorded | `mode` is "provided" or "auto-generated" | True |

All checks must pass before transitioning to Step AB-3.

## Error Handling

| Failure | Action |
|---------|--------|
| LLM generation fails | Retry once. If second failure, abort with error. |
| Generated prompt too short | Re-prompt with explicit length constraint (min 50 chars). |
| No keyword overlap | Re-prompt asking LLM to reference specific artifact sections. |
| Provided prompt empty string | Treat as auto-generate mode. |

## Output

- `task_prompt`: the prompt string to run against both variants
- `expected_output`: optional description of correct output (null if not generated)
- `prompt_mode`: "provided" or "auto-generated"
- State transition: `variants_generated` -> `prompt_built` -> ready for Step AB-3
