# CP3 Validation Checklist — Frontend Shell + Auth

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp3-frontend-shell-auth/result.json`
**Muc tieu:** Xac nhan FE shell build on dinh va auth flow chay duoc

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp3-frontend-shell-auth/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP3 — Frontend Shell + Auth",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Frontend `pnpm build` pass

```bash
cd ../ai-architect-web && pnpm build
```

**Expected:** Build thanh cong
**Fail if:** Build fail hoac type error

---

### CHECK-02: Component tests cho `StatusBadge` va auth pages pass

```bash
cd ../ai-architect-web && pnpm test src/components/common/__tests__/status-badge.test.tsx
```

**Expected:** Test pass
**Fail if:** Co test fail

---

### CHECK-03: Auth E2E flow `Register -> Login -> Dashboard` pass

```bash
cd ../ai-architect-web && pnpm exec playwright test e2e/auth-flow.spec.ts
```

**Expected:** Flow pass end-to-end
**Fail if:** Khong dang nhap duoc hoac khong vao dashboard

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp3-frontend-shell-auth \
  --role validator \
  --status PASS \
  --summary "Frontend shell va auth flow hop le, co the sang CP4." \
  --result-file docs/phases/phase-1/checkpoints/cp3-frontend-shell-auth/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp3-frontend-shell-auth/validation.json
```
