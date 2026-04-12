# CP2 — 4 Elevations + Enhanced Dimensions

**Code:** cp2-elevations-dimensions  
**Order:** 2  
**Depends On:** cp1-geometry-layer2  
**Estimated Effort:** 4 days

## Mục tiêu

Render duoc 4 mat dung, 2 sections, va enhanced dimension chains tu cung mot canonical geometry Layer 2.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/app/services/exporter.py` | updated | Plan/elevation/section renderer + dimension engine |
| `../ai-architect-api/tests/*` | updated | Export verification cho elevations, sections, dimensions |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | PDF/SVG package co 4 elevations va 2 sections | ✓ |
| CHECK-02 | Plan sheets co dimension chains overall + grid + wall + opening | ✓ |
| CHECK-03 | Schedule marks D/W xuat hien tren plan va elevation | ✓ |

