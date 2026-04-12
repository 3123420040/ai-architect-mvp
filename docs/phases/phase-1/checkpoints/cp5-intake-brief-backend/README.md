# CP5 — Intake Query Loop + Brief Backend

**Code:** cp5-intake-brief-backend
**Order:** 5
**Depends On:** cp4-project-workspace-contracts
**Estimated Effort:** 1 ngay

## Muc tieu

Dung query loop cho intake, brief tools, chat history va brief CRUD de backend co the tao va cap nhat `Design Brief JSON` qua chat hoac form.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-api/app/engine/query_loop.py` | created | Async query loop + streaming hooks |
| `../ai-architect-api/app/agents/requirements_agent.py` | created | Requirement extraction agent |
| `../ai-architect-api/app/tools/design_brief_tools.py` | created | BriefParse + BriefUpdate |
| `../ai-architect-api/app/api/v1/brief.py` | created | Brief endpoints |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Unit tests cho query loop va brief validation pass | ✓ |
| CHECK-02 | Integration tests cho `/projects/{id}/brief` va chat history pass | ✓ |
| CHECK-03 | Chat streaming smoke test qua WebSocket pass | ✓ |
