# CP11 — Layout Technical Defaults

**Code:** cp11-layout-technical-defaults
**Order:** 11
**Depends On:** cp10-concept-model-contract
**Estimated Effort:** 1-2 days

## Mục tiêu

Generate a coherent first-pass concept layout and technical defaults from customer understanding, style profiles, and pattern memory.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/app/services/design_intelligence/program_planner.py` | created | Room program builder |
| `../ai-architect-api/app/services/design_intelligence/layout_generator.py` | created | First-pass room/wall/opening/stair layout |
| `../ai-architect-api/app/services/design_intelligence/technical_defaults.py` | created | Style-aware defaults for walls, openings, stairs, fixtures |
| `../ai-architect-api/tests/test_concept_layout_generator.py` | created | Layout validity tests |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | 7x25, 3-floor, 4-bedroom modern tropical brief creates coherent room program | ✓ |
| CHECK-02 | Generated rooms do not overlap and every room has access | ✓ |
| CHECK-03 | Walls, doors, windows, stairs, fixtures, and dimensions are generated from rules/patterns, not hardcoded stale golden data | ✓ |
