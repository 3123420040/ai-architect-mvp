# CP4 — Project Workspace + API Contracts

**Muc tieu:** Co vertical slice dau tien tu DB -> API -> frontend dashboard
**Requires:** CP3 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp4-project-workspace-contracts/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP4 — Project Workspace + API Contracts",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Backend CRUD + contract

Can cu `implementation/06-api-contracts.md` muc `1`, `3` va `implementation/07-database-schema.md` muc `2.3`.

Implement:

- `GET /projects`
- `POST /projects`
- `GET /projects/{project_id}`
- Pagination, filtering, error format dung chuan

## Buoc 2 — Frontend dashboard + type generation

Implement:

- dashboard page
- project list shell
- workspace layout + sidebar nav
- typed API client tu OpenAPI

```bash
cd ../ai-architect-api && pytest tests/integration/test_projects.py -q
curl -fsS http://localhost:8000/api/v1/openapi.json > /tmp/ai-architect-openapi.json
cd ../ai-architect-web && pnpm run generate:types && pnpm build
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp4-project-workspace-contracts/result.json`.

```json
{
  "cp": "cp4-project-workspace-contracts",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Project CRUD, dashboard shell va generated TS contracts da xong.",
  "artifacts": [
    {"file": "../ai-architect-api/app/api/v1/projects.py", "action": "created"},
    {"file": "../ai-architect-web/src/app/dashboard/page.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/app/projects/[id]/layout.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/types/api.ts", "action": "created"}
  ],
  "issues": [],
  "notes": "Khong nhung project data vao Zustand; dung TanStack Query."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp4-project-workspace-contracts \
  --role implementer \
  --status READY \
  --summary "Project CRUD va dashboard shell da san sang." \
  --result-file docs/phases/phase-1/checkpoints/cp4-project-workspace-contracts/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp4-project-workspace-contracts/result.json
```
