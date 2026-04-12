# CP9 — Review + Annotation + Approval

**Muc tieu:** Chot workflow KTS review tren canonical version
**Requires:** CP8 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp9-review-annotation-approval/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP9 — Review + Annotation + Approval",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Backend review + annotations

Can cu:

- `implementation/06-api-contracts.md` muc `8`, `9`
- `implementation/07-database-schema.md` muc `2.5`
- `implementation/04-implementation-directives.md` muc `3.3`, `3.7`

Implement:

- `GET/POST /versions/{id}/annotations`
- `POST /reviews/{version_id}/approve`
- `POST /reviews/{version_id}/reject`
- audit log cho approve/reject/annotate

## Buoc 2 — Frontend review workspace

Implement:

- `FloorPlanViewer`
- `AnnotationLayer`
- `ReviewWorkspace`
- `ReviewActions`

```bash
cd ../ai-architect-api && pytest tests/integration/test_review_flow.py tests/integration/test_annotations_api.py -q
cd ../ai-architect-web && pnpm exec playwright test e2e/review-flow.spec.ts
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp9-review-annotation-approval/result.json`.

```json
{
  "cp": "cp9-review-annotation-approval",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Review workspace, annotation va lock flow da xong.",
  "artifacts": [
    {"file": "../ai-architect-api/app/api/v1/reviews.py", "action": "created"},
    {"file": "../ai-architect-api/app/api/v1/annotations.py", "action": "created"},
    {"file": "../ai-architect-web/src/components/review/review-workspace.tsx", "action": "created"},
    {"file": "../ai-architect-web/src/components/review/annotation-layer.tsx", "action": "created"}
  ],
  "issues": [],
  "notes": "Reject khong duoc mutate ve version cu; revision tao version moi."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp9-review-annotation-approval \
  --role implementer \
  --status READY \
  --summary "Review workspace va approval flow da xong." \
  --result-file docs/phases/phase-1/checkpoints/cp9-review-annotation-approval/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp9-review-annotation-approval/result.json
```
