# CP11 — Export + Bundle + Readiness

**Muc tieu:** Chot lop export/delivery core truoc khi them 3D interactive
**Requires:** CP10 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp11-export-bundle-readiness/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP11 — Export + Bundle + Readiness",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Implement export va readiness

Can cu:

- `implementation/06-api-contracts.md` muc `11`, `14`
- `implementation/05-checkpoints.md` muc `CP5`
- `implementation/03-architecture-blueprint.md` phan canonical/handoff rules

Implement:

- `POST /exports/{version_id}`
- `GET /exports/{version_id}`
- `POST /handoff/{version_id}`
- watermark logic
- `can_create_handoff(...)`

## Buoc 2 — Test exports va handoff

```bash
cd ../ai-architect-api
pytest tests/unit/test_handoff_readiness.py tests/integration/test_exports_api.py tests/integration/test_handoff_api.py -q
pytest tests/integration/test_export_files_manifest.py -q
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp11-export-bundle-readiness/result.json`.

```json
{
  "cp": "cp11-export-bundle-readiness",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "PDF/SVG export, readiness checks va handoff bundle da xong.",
  "artifacts": [
    {"file": "../ai-architect-api/app/services/pdf_export.py", "action": "created"},
    {"file": "../ai-architect-api/app/tools/export_tools.py", "action": "created"},
    {"file": "../ai-architect-api/app/api/v1/exports.py", "action": "created"},
    {"file": "../ai-architect-api/app/api/v1/handoff.py", "action": "created"}
  ],
  "issues": [],
  "notes": "DXF de phase sau; CP11 chi chot PDF/SVG/images/bundle."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp11-export-bundle-readiness \
  --role implementer \
  --status READY \
  --summary "Export va handoff readiness da xong." \
  --result-file docs/phases/phase-1/checkpoints/cp11-export-bundle-readiness/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp11-export-bundle-readiness/result.json
```
