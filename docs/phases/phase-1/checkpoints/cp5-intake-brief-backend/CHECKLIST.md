# CP5 Validation Checklist — Intake Query Loop + Brief Backend

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp5-intake-brief-backend/result.json`
**Muc tieu:** Xac nhan backend intake flow co the tao va cap nhat brief on dinh

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp5-intake-brief-backend/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP5 — Intake Query Loop + Brief Backend",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Unit tests cho query loop va brief validation pass

```bash
cd ../ai-architect-api && pytest tests/unit/test_query_loop.py tests/unit/test_brief_validation.py -q
```

**Expected:** Tat ca test pass
**Fail if:** Query loop khong dung orchestration rules

---

### CHECK-02: Integration tests cho `/projects/{id}/brief` va chat history pass

```bash
cd ../ai-architect-api && pytest tests/integration/test_brief_api.py tests/integration/test_chat_history.py -q
```

**Expected:** Tat ca test pass
**Fail if:** Brief CRUD hoac persisted chat history sai

---

### CHECK-03: Chat streaming smoke test qua WebSocket pass

```bash
cd ../ai-architect-api && pytest tests/integration/test_chat_stream.py -q
```

**Expected:** Co chunk events va event `chat:done`
**Fail if:** Khong stream duoc hoac metadata sai

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp5-intake-brief-backend \
  --role validator \
  --status PASS \
  --summary "Backend intake flow hop le, co the sang CP6." \
  --result-file docs/phases/phase-1/checkpoints/cp5-intake-brief-backend/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp5-intake-brief-backend/validation.json
```
