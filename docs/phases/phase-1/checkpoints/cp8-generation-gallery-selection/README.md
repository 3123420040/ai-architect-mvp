# CP8 — Generation Orchestration + Gallery Selection

**Code:** cp8-generation-gallery-selection
**Order:** 8
**Depends On:** cp7-gpu-service-workflow-base
**Estimated Effort:** 1 ngay

## Muc tieu

Noi backend, frontend va GPU service thanh flow generation dau tien: confirm brief -> queue generation -> tao 3 versions -> gallery -> user select option.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-api/app/tools/generation_tools.py` | created | FloorPlanGenerate tool |
| `../ai-architect-api/app/tasks/generation_task.py` | created | Celery generation job |
| `../ai-architect-web/src/components/generation/option-gallery.tsx` | created | Gallery UI |
| `../ai-architect-web/src/app/projects/[id]/designs/page.tsx` | created | Designs page |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Integration tests cho `POST /generate` va job tracking pass | ✓ |
| CHECK-02 | Full generation E2E `brief -> 3 options -> select` pass | ✓ |
| CHECK-03 | Generation progress va recovery UI hien dung state | ✓ |
