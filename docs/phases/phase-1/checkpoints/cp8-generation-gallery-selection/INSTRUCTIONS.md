# CP8 — Generation Orchestration + Gallery Selection

**Muc tieu:** Tao duoc full loop generation dau tien sau khi brief da confirm
**Requires:** CP7 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp8-generation-gallery-selection/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP8 — Generation Orchestration + Gallery Selection",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Backend generation orchestration

Can cu:

- `implementation/06-api-contracts.md` muc `6`, `7`
- `implementation/05-checkpoints.md` muc `CP3`
- `implementation/09-testing-strategy.md` muc generation flow

Implement:

- `POST /projects/{id}/generate`
- `GET /projects/{id}/generation/{job_id}`
- `FloorPlanGenerate`
- Celery orchestration + metadata logging
- `POST /versions/{id}/select`

## Buoc 2 — Frontend gallery va progress

Implement:

- `GenerationProgress`
- `OptionGallery`
- `OptionCard`
- generation error/recovery state

```bash
cd ../ai-architect-api && pytest tests/integration/test_generation_api.py tests/integration/test_version_select.py -q
cd ../ai-architect-web && pnpm exec playwright test e2e/generation-flow.spec.ts
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp8-generation-gallery-selection/result.json`.

```json
{
  "cp": "cp8-generation-gallery-selection",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Flow generation 3 options, gallery va option selection da xong.",
  "artifacts": [
    {"file": "../ai-architect-api/app/tools/generation_tools.py", "action": "created"},
    {"file": "../ai-architect-api/app/tasks/generation_task.py", "action": "created"},
    {"file": "../ai-architect-web/src/components/generation/option-gallery.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/app/projects/[id]/designs/page.tsx", "action": "created"}
  ],
  "issues": [],
  "notes": "Log seed/model/workflow_version de dam bao reproducibility."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp8-generation-gallery-selection \
  --role implementer \
  --status READY \
  --summary "Generation orchestration va gallery selection da xong." \
  --result-file docs/phases/phase-1/checkpoints/cp8-generation-gallery-selection/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp8-generation-gallery-selection/result.json
```
