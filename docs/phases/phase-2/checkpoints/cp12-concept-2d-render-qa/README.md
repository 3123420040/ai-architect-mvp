# CP12 — Concept 2D Render QA

**Code:** cp12-concept-2d-render-qa
**Order:** 12
**Depends On:** cp11-layout-technical-defaults
**Estimated Effort:** 1-2 days

## Mục tiêu

Compile the concept model into a drawing package and render customer-readable PDF/DXF sheets with semantic and visual QA.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/app/services/design_intelligence/drawing_package_model.py` | created | Sheet/view/dimension/annotation model |
| `../ai-architect-api/app/services/professional_deliverables/concept_pdf_generator.py` | created/updated | Concept 2D PDF renderer |
| `../ai-architect-api/app/services/professional_deliverables/concept_dxf_exporter.py` | created/updated | Concept 2D DXF renderer |
| `../ai-architect-api/app/services/design_intelligence/concept_drawing_qa.py` | created | QA gates |
| `../ai-architect-api/tests/professional_deliverables/test_concept_2d_package.py` | created | End-to-end render QA tests |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | Package contains site, floor plans, elevation, section, schedules, assumptions | ✓ |
| CHECK-02 | Dimensions are derived from geometry and labels do not overlap title blocks | ✓ |
| CHECK-03 | PDF pages render nonblank and DXF opens with expected layers | ✓ |
