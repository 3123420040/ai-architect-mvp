# CP5 — Delivery Workspace and Status

**Objective:** Turn Program B into visible product value in the delivery workspace.
**Requires:** CP4 PASS.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp5-program-b-delivery-workspace-and-status/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP5 — Program B delivery workspace and status",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Add Program B frontend fetch and view components

Create:

- `../ai-architect-web/src/lib/coordination.ts`
- `../ai-architect-web/src/components/coordination-handoff.tsx`

Update:

- `../ai-architect-web/src/components/delivery-client.tsx`

## Step 2 — Implement required UI slices

Required UI:

- readiness summary panel
- schedule preview tab
- issue summary panel
- release status chip
- authorized release action

Copy must avoid implying:

- native BIM authoring
- construction certainty

## Step 3 — Validate frontend build

```bash
cd ../ai-architect-web && pnpm build
```

## Step 4 — Record completion artifacts

Create:

- `artifacts/program-b/cp5-program-b-delivery-workspace-and-status/result.json`
- `artifacts/program-b/cp5-program-b-delivery-workspace-and-status/notes.md`
- `artifacts/program-b/cp5-program-b-delivery-workspace-and-status/ui-notes.md`

## Step 5 — Notify and post status

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp5-program-b-delivery-workspace-and-status \
  --role implementer \
  --status READY \
  --summary "CP5 complete. Program B delivery workspace and status UX are implemented." \
  --result-file artifacts/program-b/cp5-program-b-delivery-workspace-and-status/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/program-b/cp5-program-b-delivery-workspace-and-status/result.json
```
