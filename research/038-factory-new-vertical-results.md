# Task 038 — Spec Factory: Health Insurance Testing

**Date:** 2026-03-10
**Industry:** Health Insurance (modeled after HMSA)
**Sub-domains built:** 4 of 12 identified (top scorers)

---

## Sub-Domain Scores (from research)

| Domain | Regulatory | Repetitive | Doc Avail | Automation | Pain | Total |
|--------|-----------|------------|-----------|------------|------|-------|
| EDI Testing | 5 | 5 | 5 | 5 | 5 | 25/25 |
| Claims Testing | 5 | 5 | 5 | 4 | 5 | 24/25 |
| Benefits/Plan Config | 4 | 5 | 4 | 4 | 5 | 22/25 |
| Auth/UM | 5 | 4 | 4 | 4 | 5 | 22/25 |
| Provider Management | 4 | 4 | 4 | 4 | 4 | 20/25 |
| Compliance/Regulatory | 5 | 3 | 4 | 3 | 4 | 19/25 |
| Billing/Premium | 4 | 4 | 3 | 4 | 4 | 19/25 |
| Integration/API | 3 | 4 | 4 | 4 | 4 | 19/25 |
| Portal/Digital | 3 | 4 | 4 | 4 | 3 | 18/25 |
| Membership/Enrollment | 4 | 4 | 3 | 3 | 4 | 18/25 |
| Data/Analytics | 4 | 3 | 3 | 3 | 3 | 16/25 |
| Correspondence | 3 | 4 | 3 | 3 | 3 | 16/25 |

## Specs Built

| Spec | Location | Files | Lines | Commit |
|------|----------|-------|-------|--------|
| EDI Testing | `specs/edi-testing-spec` | 16 | 3,507 | `f673c10` |
| Claims Testing | `specs/claims-testing-spec` | 18 | 3,978 | `5d26e5c` |
| Benefits Config | `specs/benefits-config-spec` | 25 | 4,555 | `dae9d6f` |
| Auth/UM | `specs/auth-um-spec` | 21 | 4,849 | `117723b` |
| **Total** | — | **80** | **16,889** | — |

## Quality Assessment vs Hand-Built Specs

| Dimension | Selenium (hand-built) | Factory skeleton (037) | Health insurance specs (038) |
|-----------|----------------------|----------------------|----------------------------|
| File structure | 19 files | 18 files (79%) | 16-25 files (100%+) |
| Content depth | ~2,800 lines | ~1,100 lines (39%) | 3,507-4,849 lines (125-173%) |
| Domain accuracy | Hand-crafted | Generic | Deep, standards-referenced |
| Seeded lessons | Battle-hardened | 1 topic | 13-29 lessons per spec |
| Usability | Production-ready | Needs work | Production-ready |

## Key Improvements Over Factory Skeleton (037)

1. **Content depth:** 3-4x deeper than 037's skeleton output
2. **Real standards:** X12 segments, CARC/RARC codes, FHIR resources, CMS rules
3. **Worked examples:** Payment calculations, accumulator sequences, COB scenarios
4. **Platform references:** Facets, QNXT, HealthEdge, Jiva, GuidingCare
5. **Regulatory currency:** CMS-0057-F deadlines, No Surprises Act, ACA/MHPAEA

## Next Steps

- Remaining 8 domains (Provider, Compliance, Billing, Integration, Portal, Membership, Data, Correspondence) can be built on demand
- Push specs to GitHub as `isagawa-co/[domain]-spec` repos
- Test each spec via kernel bootstrap (like task 034)
