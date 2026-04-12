# CP6 Validation Checklist — Intake UI + Brief Editor

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp6-intake-ui-brief-editor/result.json`
**Muc tieu:** Xac nhan intake UX tren frontend hoat dong tron ven

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp6-intake-ui-brief-editor/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP6 — Intake UI + Brief Editor",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Component tests cho chat, form va brief editor pass

```bash
cd ../ai-architect-web && \
pnpm test src/components/chat/__tests__/chat-interface.test.tsx && \
pnpm test src/components/forms/__tests__/intake-form.test.tsx && \
pnpm test src/components/brief/__tests__/brief-editor.test.tsx
```

**Expected:** Tat ca test pass
**Fail if:** Interaction state/validation sai

---

### CHECK-02: Intake E2E flow pass

```bash
cd ../ai-architect-web && pnpm exec playwright test e2e/intake-flow.spec.ts
```

**Expected:** Tao duoc brief qua chat hoac form
**Fail if:** Flow bi block o bat ky buoc nao

---

### CHECK-03: Mode switcher `Chat/Form` va brief summary hoat dong dung

```bash
cd ../ai-architect-web && pnpm test src/components/intake/__tests__/mode-switcher.test.tsx
```

**Expected:** Toggle dung va summary render brief da confirm
**Fail if:** UI state sai hoac summary khong khop data

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp6-intake-ui-brief-editor \
  --role validator \
  --status PASS \
  --summary "Intake UX hop le, co the sang CP7." \
  --result-file docs/phases/phase-1/checkpoints/cp6-intake-ui-brief-editor/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp6-intake-ui-brief-editor/validation.json
```
