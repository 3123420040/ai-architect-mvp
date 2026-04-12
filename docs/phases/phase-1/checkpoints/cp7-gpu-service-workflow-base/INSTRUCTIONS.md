# CP7 — GPU Service + Workflow Base

**Muc tieu:** Chot GPU service boundary ro rang truoc khi noi voi backend generation
**Requires:** CP6 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7-gpu-service-workflow-base/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP7 — GPU Service + Workflow Base",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Dung GPU wrapper va workflow

Can cu:

- `implementation/02-tech-stack-decisions.md` muc `4`
- `implementation/04-implementation-directives.md` muc `4.1`, `4.2`, `4.3`
- `implementation/08-deployment-guide.md` muc `2.4`

Bat buoc co:

- `POST /generate/floor-plan`
- progress callback/webhook
- workflow versioning
- fallback pipeline skeleton

## Buoc 2 — Smoke test local

```bash
cd ../ai-architect-gpu
python -m uvicorn api.server:app --port 8001
curl -fsS http://localhost:8001/health
python -m pytest tests/test_api_health.py tests/test_workflow_validation.py -q
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp7-gpu-service-workflow-base/result.json`.

```json
{
  "cp": "cp7-gpu-service-workflow-base",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "GPU wrapper, workflow base va fallback skeleton da san sang.",
  "artifacts": [
    {"file": "../ai-architect-gpu/api/server.py", "action": "created"},
    {"file": "../ai-architect-gpu/comfyui/workflows/floor_plan_gen.json", "action": "created"},
    {"file": "../ai-architect-gpu/pipelines/floor_plan_pipeline.py", "action": "created"},
    {"file": "../ai-architect-gpu/Dockerfile.gpu", "action": "created"}
  ],
  "issues": [],
  "notes": "ComfyUI phai chay isolated qua service boundary."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp7-gpu-service-workflow-base \
  --role implementer \
  --status READY \
  --summary "GPU service boundary va workflow base da xong." \
  --result-file docs/phases/phase-1/checkpoints/cp7-gpu-service-workflow-base/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp7-gpu-service-workflow-base/result.json
```
