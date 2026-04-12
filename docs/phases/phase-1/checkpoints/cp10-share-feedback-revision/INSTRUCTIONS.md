# CP10 — Share Link + Feedback + Revision

**Muc tieu:** Mo feedback loop ben ngoai ma van giu duoc lineage va canonical control
**Requires:** CP9 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp10-share-feedback-revision/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP10 — Share Link + Feedback + Revision",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Backend share/feedback/revision

Can cu:

- `implementation/06-api-contracts.md` muc `10`, `12`
- `implementation/07-database-schema.md` muc `2.6`, `2.8`
- `implementation/05-checkpoints.md` muc `CP4`

Implement:

- `POST /projects/{project_id}/share`
- `GET /share/{token}`
- `POST /versions/{version_id}/feedback`
- `POST /versions/{version_id}/revise`
- lineage tren `design_versions.parent_version_id`

## Buoc 2 — Frontend share page va revision trigger

Implement:

- public share page
- feedback form
- version timeline cap nhat version moi
- notification hook cho feedback/revision done

```bash
cd ../ai-architect-api && pytest tests/integration/test_share_api.py tests/integration/test_feedback_api.py tests/integration/test_revision_flow.py -q
cd ../ai-architect-web && pnpm exec playwright test e2e/share-feedback-revision.spec.ts
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp10-share-feedback-revision/result.json`.

```json
{
  "cp": "cp10-share-feedback-revision",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Share link, feedback, revision va version lineage da xong.",
  "artifacts": [
    {"file": "../ai-architect-api/app/api/v1/share.py", "action": "created"},
    {"file": "../ai-architect-api/app/api/v1/feedback.py", "action": "created"},
    {"file": "../ai-architect-api/app/agents/revision_agent.py", "action": "created"},
    {"file": "../ai-architect-web/src/app/share/[token]/page.tsx", "action": "created"}
  ],
  "issues": [],
  "notes": "Reject/revise phai tao version moi, khong mutate version da lock."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp10-share-feedback-revision \
  --role implementer \
  --status READY \
  --summary "Share, feedback va revision flow da xong." \
  --result-file docs/phases/phase-1/checkpoints/cp10-share-feedback-revision/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp10-share-feedback-revision/result.json
```
