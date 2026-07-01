# /kernel/human-check

Scan text for AI tells and enforce human-quality writing.

## Usage

```
/kernel/human-check [file-path]
/kernel/human-check [inline text]
```

## Input Modes

- **File path**: Pass a file path to scan its contents. Example: `/kernel/human-check docs/README.md`
- **Inline text**: Pass text directly to scan it. Example: `/kernel/human-check "This innovative solution leverages cutting-edge AI"`

## Examples

```
/kernel/human-check projects/resume-loops-agent-systems/report.md
```

```
/kernel/human-check "In today's rapidly evolving landscape, it's arguably the most essential framework"
```

## Instructions

Read and follow `.claude/skills/human-check/SKILL.md`

Pass the user's argument (file path or inline text) as input to step 1.
