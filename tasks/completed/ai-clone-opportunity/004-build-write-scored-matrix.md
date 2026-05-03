# Write Scored Candidate Matrix

## Type
BUILD

## Description
Write the scored candidate matrix as a structured markdown file.

## Requirements
1. Create `projects/ai-clone-opportunity/candidate-matrix.md`
2. Include markdown table with columns:
   - Product | Category | Revenue | Users | Build (1-10) | Market (1-10) | Vulnerability (1-10) | Defensibility (1-10) | Time-to-Revenue (1-10) | Total Score | Rank
3. Sort by total score descending
4. Include brief notes column or section with key rationale per candidate
5. Highlight top 3 with clear visual separation

## Acceptance Criteria
- [ ] `test -f projects/ai-clone-opportunity/candidate-matrix.md`
- [ ] `grep -c "^|" projects/ai-clone-opportunity/candidate-matrix.md` >= 12
- [ ] `grep -q "Score" projects/ai-clone-opportunity/candidate-matrix.md`
