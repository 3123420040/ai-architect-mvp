# CP6 — Integration + QA

**Code:** cp6-integration-qa  
**Order:** 6  
**Depends On:** cp5-ifc-foundation  
**Estimated Effort:** 3 days

## Mục tiêu

Chot full Phase 2 package: generation -> review -> export -> handoff -> production deploy -> loop verification.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/tests/*` | updated | End-to-end flow tests phu hop Phase 2 exports |
| `scripts/production_check_loops.py` | updated if needed | Production loop phu hop export package moi |
| `artifacts/production-checks/*` | created/updated | Ket qua re-validation sau deploy |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | Full flow tests pass tren codebase moi | ✓ |
| CHECK-02 | Production deploy thanh cong | ✓ |
| CHECK-03 | 2 production loops pass end-to-end | ✓ |

