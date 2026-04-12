# CP4 — Project Workspace + API Contracts

**Code:** cp4-project-workspace-contracts
**Order:** 4
**Depends On:** cp3-frontend-shell-auth
**Estimated Effort:** 1 ngay

## Muc tieu

Noi `project CRUD` giua backend va frontend, dong bo typed contracts, project dashboard shell va workspace navigation de team co mot vertical slice dau tien.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-api/app/api/v1/projects.py` | created | Project CRUD endpoints |
| `../ai-architect-web/src/app/dashboard/page.tsx` | created | Dashboard shell |
| `../ai-architect-web/src/app/projects/[id]/layout.tsx` | created | Project workspace layout |
| `../ai-architect-web/src/types/api.ts` | created | Generated TS types tu OpenAPI |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Integration tests cho `POST/GET /projects` pass | ✓ |
| CHECK-02 | Type generation tu OpenAPI chay duoc va frontend build pass | ✓ |
| CHECK-03 | Dashboard/project workspace hien duoc project list va detail shell | ✓ |
