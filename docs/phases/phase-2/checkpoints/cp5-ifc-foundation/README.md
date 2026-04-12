# CP5 — IFC Foundation

**Code:** cp5-ifc-foundation  
**Order:** 5  
**Depends On:** cp4-dxf-export  
**Estimated Effort:** 2 days

## Mục tiêu

Add a basic IFC handoff lane from the same canonical geometry so the package can cross into BIM-oriented review flows.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/app/services/exporter.py` | updated | IFC foundation export |
| `../ai-architect-api/tests/*` | updated | IFC export assertions |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | IFC file duoc export cung package | ✓ |
| CHECK-02 | IFC payload co project, site, building, storeys, walls, openings, spaces | ✓ |
| CHECK-03 | Handoff manifest include IFC reference | ✓ |

