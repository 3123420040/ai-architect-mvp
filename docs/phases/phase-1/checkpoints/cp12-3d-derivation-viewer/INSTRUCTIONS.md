# CP12 — 3D Derivation + Viewer

**Muc tieu:** Them lop 3D ma khong pha canonical-first architecture
**Requires:** CP11 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp12-3d-derivation-viewer/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP12 — 3D Derivation + Viewer",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Backend/GPU derivation

Can cu:

- `implementation/06-api-contracts.md` muc `7b`
- `implementation/05-checkpoints.md` muc `CP5`
- `implementation/02-tech-stack-decisions.md` muc `2` va `4`

Implement:

- `POST /versions/{id}/derive-3d`
- `GET /versions/{id}/3d`
- Blender headless pipeline
- luu `model_url`, `render_urls`, `generation_metadata`

## Buoc 2 — Frontend viewer

Implement:

- `Viewer3D`
- viewer page
- feature flag `NEXT_PUBLIC_FF_VIEWER_3D`

```bash
cd ../ai-architect-api && pytest tests/integration/test_derive_3d_api.py -q
cd ../ai-architect-gpu && python -m pytest tests/test_blender_pipeline.py -q
cd ../ai-architect-web && NEXT_PUBLIC_FF_VIEWER_3D=true pnpm exec playwright test e2e/viewer-3d.spec.ts
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp12-3d-derivation-viewer/result.json`.

```json
{
  "cp": "cp12-3d-derivation-viewer",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "3D derivation API, Blender pipeline va viewer page da xong.",
  "artifacts": [
    {"file": "../ai-architect-api/app/api/v1/derivation.py", "action": "created"},
    {"file": "../ai-architect-gpu/pipelines/blender_3d_pipeline.py", "action": "created"},
    {"file": "../ai-architect-web/src/components/viewer/viewer-3d.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/app/projects/[id]/viewer/page.tsx", "action": "created"}
  ],
  "issues": [],
  "notes": "Neu Blender chua on dinh thi static renders van la P0, viewer la P1."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp12-3d-derivation-viewer \
  --role implementer \
  --status READY \
  --summary "3D derivation va viewer da xong." \
  --result-file docs/phases/phase-1/checkpoints/cp12-3d-derivation-viewer/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp12-3d-derivation-viewer/result.json
```
