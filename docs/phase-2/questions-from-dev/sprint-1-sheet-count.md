---
title: Sprint 1 Question — Golden Fixture Sheet Count
phase: 2
status: ANSWERED
date: 2026-04-26
answered: 2026-04-26
from: Dev/Test Agent
to: PM/Architect Agent via PO
---

# Context

The Sprint 1 handoff and Definition of Done say the DWG exporter should produce four sheets for the golden fixture: `A-100`, `A-101`, `A-201`, `A-301`.

The same sprint scope and PRD also say multi-storey buildings should produce one `A-101` floor plan sheet per floor. The golden fixture is a 2-storey townhouse, so strict per-floor output would produce at least five 2D drawing files/pages: `A-100`, `A-101-F1`, `A-101-F2`, `A-201`, `A-301`.

# Precise Question

For Sprint 1 acceptance on the golden fixture, should the implementation produce exactly four drawing sheets, or split `A-101` into one sheet per floor?

# Answer Format Needed

Please answer with one of:

1. `Four sheets`: keep `A-101-floorplan` as one sheet containing both floors for the golden fixture.
2. `Per-floor sheets`: produce `A-101-F1` and `A-101-F2`, and update Sprint 1 expected sheet count to five.

# Fallback If Not Answered Within 24 Hours

I will follow the explicit Sprint 1 Definition of Done and produce four sheets, with `A-101-floorplan` containing both floors in separate labeled viewports.

---

# Answer (PM/Architect Agent — 2026-04-26)

**Decision: Option 2 — Per-floor sheets.**

For the golden 2-storey townhouse fixture, produce **5 sheets**:

| Sheet | Filename | Content |
|---|---|---|
| 1 | `A-100-site.dwg` | Site, footprint, setbacks, north arrow |
| 2 | `A-101-F1-floorplan.dwg` | Ground floor plan |
| 3 | `A-101-F2-floorplan.dwg` | Upper floor plan |
| 4 | `A-201-elevations.dwg` | North + South + East + West elevations on one sheet |
| 5 | `A-301-sections.dwg` | One transverse + one longitudinal section on one sheet |

## Rationale
- PRD-05 F-2D-07 ("multi-storey buildings → one A-101-FN.dwg per floor") reflects real architectural practice; engineer downstream expects per-floor sheets.
- The "4 sheets" wording in the DoD was minimum-case (single-storey). Multi-storey fixture is the realistic shape we want to validate end-to-end before GA.
- Validates the per-floor branch of the pipeline early — Sprint 2/3 don't have to retrofit it.

## Naming convention
`A-101-F<N>-floorplan.dwg` where `<N>` = floor number, starting at 1 for ground floor. (We don't use European convention "F0 = ground" — VN convention is F1 = ground floor.)

## Action
PRD-05 has been updated to clarify:
- Definition of Done now reads "**all required DWG sheets** per the sheet strategy" instead of "all 4 DWG sheets".
- F-2D-07 priority is upgraded from `Should` → `Must` for multi-storey fixtures.
- Sheet table in the PRD output structure section now shows the per-floor pattern explicitly.

**This unblocks the sheet count gate. Proceed with implementation.**

