# CP7 Validation Checklist — GPU Service + Workflow Base

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp7-gpu-service-workflow-base/result.json`
**Muc tieu:** Xac nhan GPU service boundary da dung va goi duoc

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7-gpu-service-workflow-base/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP7 — GPU Service + Workflow Base",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: GPU wrapper boot duoc va `/health` tra thong tin GPU/ComfyUI

```bash
curl -fsS http://localhost:8001/health
```

**Expected:** JSON co status/gpu_available
**Fail if:** Endpoint fail hoac khong co health payload

---

### CHECK-02: Workflow JSON validate duoc va generation API nhan request

```bash
cd ../ai-architect-gpu && python -m pytest tests/test_workflow_validation.py tests/test_generate_request.py -q
```

**Expected:** Tat ca test pass
**Fail if:** Workflow JSON sai hoac request schema sai

---

### CHECK-03: Progress callback va webhook skeleton hoat dong

```bash
cd ../ai-architect-gpu && python -m pytest tests/test_progress_callback.py -q
```

**Expected:** Co event progress hoac webhook callback mocked
**Fail if:** Khong phat signal duoc

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp7-gpu-service-workflow-base \
  --role validator \
  --status PASS \
  --summary "GPU workflow base hop le, co the sang CP8." \
  --result-file docs/phases/phase-1/checkpoints/cp7-gpu-service-workflow-base/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp7-gpu-service-workflow-base/validation.json
```
