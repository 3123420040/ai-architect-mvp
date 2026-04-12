# CP4 Validation Checklist — Project Workspace + API Contracts

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp4-project-workspace-contracts/result.json`
**Muc tieu:** Xac nhan vertical slice project dashboard da thong tu backend den frontend

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp4-project-workspace-contracts/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP4 — Project Workspace + API Contracts",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Integration tests cho `POST/GET /projects` pass

```bash
cd ../ai-architect-api && pytest tests/integration/test_projects.py -q
```

**Expected:** Tat ca test pass
**Fail if:** CRUD khong dung contract

---

### CHECK-02: Type generation tu OpenAPI chay duoc va frontend build pass

```bash
cd ../ai-architect-web && pnpm run generate:types && pnpm build
```

**Expected:** Types duoc generate va build thanh cong
**Fail if:** Contract mismatch hoac build fail

---

### CHECK-03: Dashboard/project workspace hien duoc project list va detail shell

```bash
cd ../ai-architect-web && pnpm exec playwright test e2e/project-dashboard.spec.ts
```

**Expected:** Dashboard va project workspace smoke pass
**Fail if:** Khong load duoc list/detail shell

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp4-project-workspace-contracts \
  --role validator \
  --status PASS \
  --summary "Project vertical slice hop le, co the sang CP5." \
  --result-file docs/phases/phase-1/checkpoints/cp4-project-workspace-contracts/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp4-project-workspace-contracts/validation.json
```
