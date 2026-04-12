# CP9 — Review + Annotation + Approval

**Code:** cp9-review-annotation-approval
**Order:** 9
**Depends On:** cp8-generation-gallery-selection
**Estimated Effort:** 1 ngay

## Muc tieu

Hoan tat review workspace cho KTS: annotate floor plan, approve/reject, lock version va ghi audit log day du.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-api/app/api/v1/reviews.py` | created | Approve/reject endpoints |
| `../ai-architect-api/app/api/v1/annotations.py` | created | Annotation CRUD |
| `../ai-architect-web/src/components/review/review-workspace.tsx` | created | Review layout |
| `../ai-architect-web/src/components/review/annotation-layer.tsx` | created | Fabric.js overlay |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Integration tests cho annotation CRUD va review endpoints pass | ✓ |
| CHECK-02 | Review E2E `annotate -> approve -> locked` pass | ✓ |
| CHECK-03 | Audit log duoc tao cho moi action review quan trong | ✓ |
