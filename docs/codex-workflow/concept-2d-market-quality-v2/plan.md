# Concept 2D Market Quality V2 Plan

Status: ready for bootstrap

## Decision

Technical live integration is accepted, but market-quality risk remains. The generated files are now valid enough to inspect; the next problem is whether the 2D package is persuasive, readable, and useful for homeowner review before a human architect or downstream production phase continues.

This phase must not chase construction documentation. It must improve concept-package quality only.

## Goal

```text
At the end of this phase, AI Architect should generate a live Concept 2D package that a homeowner can review without technical handholding and that an architect would consider a credible first-pass concept design package, while preserving concept-only scope and selected-version geometry.
```

## Market Acceptance Dimensions

- Client readability: the package explains the concept, room program, tradeoffs, assumptions, and next review questions in homeowner language.
- Spatial plausibility: rooms, stairs, wet cores, openings, furniture, circulation, storage, and vertical stacking feel believable.
- Drawing craft: plans/elevations/sections/schedules have usable scale, hierarchy, dimensions, labels, legends, title blocks, and no collisions.
- Style expression: selected style affects facade rhythm, openings, shading, notes, material palette, and presentation tone.
- Revision usefulness: natural-language and reference-image-descriptor feedback changes the right model fields and regenerates traceable sheets.
- Safety: no construction/permit/structural/MEP/legal-ready claims.

## 20-Case Matrix

C2DQ1 may refine these, but closeout must cover at least the same breadth:

1. 5x20 townhouse, minimal warm, 3 floors, 3 bedrooms.
2. 5x20 townhouse, modern tropical, 4 floors, elder bedroom on ground floor.
3. 7x25 townhouse, modern tropical, garage and garden priority.
4. 4x18 narrow townhouse, minimal warm, compact stair/wet core.
5. 6x22 townhouse, Indochine, family with two children.
6. 8x20 villa-like house, modern tropical, courtyard/lightwell.
7. 10x20 corner lot, modern minimalist, two street fronts.
8. Apartment 70m2, Indochine, 2 bedrooms, reference-image descriptors.
9. Apartment 95m2, minimal warm, work-from-home and storage priority.
10. Small studio apartment, minimal warm, flexible furniture.
11. Townhouse with explicit dislike: less glass, warmer facade.
12. Townhouse with explicit dislike: avoid dark/closed interior.
13. Townhouse with low-communication brief: AI must infer and ask only essential confirmation.
14. Multi-generation family: elder bedroom/wet core access.
15. Young couple: open kitchen/social living priority.
16. Home business/shophouse: front service zone and privacy split.
17. Budget-constrained concept: keep forms simple and assumptions clear.
18. Reference descriptors: arches/wood/rattan/neutral palette.
19. Revision case: enlarge kitchen, reduce bedroom, add storage.
20. Revision case: change style from modern tropical to minimal warm without losing geometry.

## Workstreams

- C2DQ0 Bootstrap/Worktrees: create clean worktrees from pushed `main`.
- C2DQ1 Acceptance Rubric And Case Matrix: define pass/fail criteria and fixtures before implementation.
- C2DQ2 Spatial Planning Quality: improve concept model/layout generation.
- C2DQ3 Drawing Craft And Readability: improve PDF/DXF render quality and gates.
- C2DQ4 Style And Facade Expression: improve style-specific output and notes.
- C2DQ5 Client Revision Truth Loop: validate review/regeneration behavior.
- C2DQ6 Integrated Closeout Acceptance: rerun from integrated `main` with browser and artifact evidence.

## Exit Gate

PASS only if:

- all accepted slices are merged into local and remote `main`;
- no repo has uncommitted product changes;
- integrated tests pass;
- fresh browser full-flow acceptance passes;
- the case matrix produces artifact evidence for at least 20 cases;
- at least 5 generated PDFs are manually/visually inspected as architect/customer;
- PDF/DXF keep selected-version geometry and concept-only warnings;
- market-quality rubric is explicit in JSON/MD evidence;
- known residual gaps are written as product decisions, not hidden under passing gates.

NEEDS_REVIEW if:

- the package is review-useful but one non-critical visual polish issue remains.

BLOCKED if:

- live generation cannot complete;
- layout/model data is insufficient without an architecture decision;
- fixes require construction/permit/MEP/legal scope.
