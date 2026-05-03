# Gate Contract — AI Clone Product Opportunity

## Level 1: Structural Gates
- [ ] `test -d projects/ai-clone-opportunity`
- [ ] `test -f projects/ai-clone-opportunity/candidate-matrix.md`
- [ ] `test -f projects/ai-clone-opportunity/top-3-deep-dives.md`
- [ ] `test -f projects/ai-clone-opportunity/mvp-plan.md`
- [ ] `test -f projects/ai-clone-opportunity/final-report.md`

## Level 2: Content Gates
- [ ] `grep -c "^|" projects/ai-clone-opportunity/candidate-matrix.md` >= 12 (header + 10-15 candidates)
- [ ] `grep -q "Score" projects/ai-clone-opportunity/candidate-matrix.md`
- [ ] `grep -q "MVP" projects/ai-clone-opportunity/mvp-plan.md`
- [ ] `grep -q "Go-to-Market" projects/ai-clone-opportunity/mvp-plan.md`

## Level 3: Quality Gates
- [ ] Final report references all scored candidates
- [ ] #1 pick has tech stack, timeline, and revenue path
- [ ] Top 3 each have AI-native differentiation clearly stated
