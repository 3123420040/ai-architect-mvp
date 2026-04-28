# CP13 — Client Review Revision Loop

**Code:** cp13-client-review-revision-loop
**Order:** 13
**Depends On:** cp12-concept-2d-render-qa
**Estimated Effort:** 1-2 days

## Mục tiêu

Turn homeowner feedback, chat, and annotations into structured revision operations that update the concept model and regenerate a new drawing version.

## Artifacts dự kiến

| File/Path | Action | Mô tả |
|-----------|--------|-------|
| `../ai-architect-api/app/services/design_intelligence/revision_interpreter.py` | created | Feedback-to-operation parser |
| `../ai-architect-api/app/services/design_intelligence/concept_revision.py` | created | Apply operations and version changelog |
| `../ai-architect-web/src/components/...` | updated | Minimal review UI only if needed |
| `../ai-architect-api/tests/test_concept_revision_loop.py` | created | Revision operation tests |

## Checklist Validator

| ID | Mô tả | Blocker |
|----|-------|---------|
| CHECK-01 | Feedback such as "phong khach rong hon" maps to structured operations | ✓ |
| CHECK-02 | Applying operations creates a child concept version and changelog | ✓ |
| CHECK-03 | Regenerated package preserves site truth and updates affected dimensions | ✓ |
