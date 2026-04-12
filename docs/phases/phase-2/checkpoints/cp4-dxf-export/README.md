# CP4 — DXF Export

**Code:** cp4-dxf-export  
**Order:** 4  
**Depends On:** cp3-schedules  
**Estimated Effort:** 4 days

## Mục tiêu

Generate a CAD-oriented DXF package from Layer 2 geometry with model space, paper space layouts, title blocks, dimensions, and schedule references.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/app/services/exporter.py` | updated | DXF exporter |
| `../ai-architect-api/requirements.txt` | updated | DXF dependencies |
| `../ai-architect-api/tests/*` | updated | DXF export assertions |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | DXF file generate duoc cho version locked | ✓ |
| CHECK-02 | Layer map co naming convention A-WALL / A-ANNO / A-ELEV / A-SECT | ✓ |
| CHECK-03 | Layout names bao gom cover, site, floor plans, elevations, sections, schedules | ✓ |

