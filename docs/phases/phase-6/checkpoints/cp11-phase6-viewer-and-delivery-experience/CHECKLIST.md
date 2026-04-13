# CP11 Validation Checklist — Viewer and Delivery Experience

**For:** Validator  
**Read first:** `artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/result.json`  
**Goal:** Confirm the frontend now behaves like a presentation workspace rather than a debug page.

---

## Step 0 — Start Validation

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp11-phase6-viewer-and-delivery-experience/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Starting validation for CP11 — Viewer and Delivery Experience",
    "readyForNextTrigger": false
  }' || true
```

## Validation Checks

### CHECK-01: Viewer and delivery components reference bundle-first concepts and Vietnamese status copy

```bash
rg -n "Bản xem trước|Cần KTS duyệt|Đã duyệt|Bị chặn phát hành|walkthrough|manifest|gallery|DEGRADED" \
  ../ai-architect-web/src/components/viewer-client.tsx \
  ../ai-architect-web/src/components/delivery-client.tsx \
  ../ai-architect-web/src/components/status-badge.tsx
```

**Expected:** Frontend reflects presentation-grade states and Vietnamese copy.  
**Fail if:** UI still exposes technical/debug wording as the dominant experience.

### CHECK-02: Frontend build passes

```bash
cd ../ai-architect-web && pnpm build
```

**Expected:** Web build is green after viewer and delivery changes.  
**Fail if:** The build fails.

### CHECK-03: Acceptance screenshots are present

```bash
test -d artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/screenshots && \
find artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/screenshots -type f | grep -q .
```

**Expected:** Desktop and mobile screenshots were captured for review.  
**Fail if:** No screenshot artifacts were recorded.

## Record Validation

```bash
python3 docs/phases/phase-6/checkpoints/notify.py \
  --cp cp11-phase6-viewer-and-delivery-experience \
  --role validator \
  --status PASS \
  --summary "CP11 passed. Viewer and delivery UX now present a professional Phase 6 workflow." \
  --result-file artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/validation.json

python3 docs/phases/phase-6/checkpoints/post-status.py \
  --result-file artifacts/phase6/cp11-phase6-viewer-and-delivery-experience/validation.json
```
