# CP11 — Viewer and Delivery Experience

**Objective:** Turn the 3D page into a presentation workspace and integrate 3D status into delivery.  
**Requires:** `cp10-phase6-approval-gate-and-manifest` validator pass.

---

## Step 0 — Start Status

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp11-phase6-viewer-and-delivery-experience/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Starting CP11 — Viewer and Delivery Experience",
    "readyForNextTrigger": false
  }' || true
```

## Step 1 — Update the viewer experience

Update:

- `../ai-architect-web/src/components/viewer-client.tsx`

The page must include:

- title and source version reference
- bundle status chip
- hero still
- still gallery
- video player
- open/download model action
- approval panel
- QA/degraded status

Remove debug-first elements such as raw glTF text or payload inspection as primary content.

## Step 2 — Integrate delivery workspace behavior

Update:

- `../ai-architect-web/src/components/delivery-client.tsx`

The delivery workspace must show:

- latest 3D bundle status
- preview vs released state
- gated view/download actions

## Step 3 — Lock Vietnamese status copy

Use these labels or tighter equivalents with the same meaning:

- `Chưa tạo`
- `Đang xử lý`
- `Bản xem trước`
- `Cần KTS duyệt`
- `Đã duyệt`
- `Bị chặn phát hành`
- `Xem trước nội bộ`
- `Đã sẵn sàng phát hành`
- `Đã phát hành`
- `Phát hành bị chặn`

## Step 4 — Run required commands

```bash
cd ../ai-architect-web && pnpm build | tee ../ai-architect-mvp/artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/web-build.log
```

Capture desktop and mobile screenshots into:

- `artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/screenshots/`

## Step 5 — Record completion and notify

Create:

- `artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/result.json`
- `artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/notes.md`

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp11-phase6-viewer-and-delivery-experience \
  --role implementer \
  --status READY \
  --summary "CP11 complete. Viewer and delivery UX now reflect the Phase 6 presentation contract." \
  --result-file artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/result.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/result.json
```
