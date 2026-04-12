# Production Loop Audit - 2026-04-12

## Scope

- Run repeated end-to-end production loops on `kts.blackbirdzzzz.art`
- Validate UI/UX around `generate -> select -> review -> approve -> lock -> export -> derive-3d -> handoff`
- Check lock-state behavior for generated revisions and delivery-ready versions

## Fixes Shipped

### 1. Dashboard current status no longer points to `superseded`

- Backend now picks the latest non-`superseded` version as the current version summary.
- This fixes cases where a project already `under_review` or `handoff_ready` was shown as `superseded` on the dashboard.

Files:

- `../ai-architect-api/app/api/v1/projects.py`
- `../ai-architect-api/tests/test_flows.py`

### 2. Review actions now respect state machine

- `generated` versions now show `Dua vao review` as the next action.
- `Approve + Lock`, `Reject`, `Export Assets`, `Create Handoff`, `Derive 3D` are disabled unless the current version is in a valid backend state.
- Inline next-step guidance is shown based on the current version status.
- Success and error messages are now shown inside the workspace instead of failing silently in console.

Files:

- `../ai-architect-web/src/components/review-client.tsx`
- `../ai-architect-web/src/lib/api.ts`

### 3. Revision workflow is clearer

- After creating a revision, the review workspace now moves focus to the new revision instead of keeping the old version selected.
- Revision lineage now shows parent version numbers instead of raw UUIDs.

Files:

- `../ai-architect-web/src/components/review-client.tsx`

### 4. Designs gallery now avoids invalid selection actions

- Only `generated` options can be sent into review.
- Other statuses now show disabled labels like `Dang review`, `Da khoa`, `Da reject`, `Da bo qua`.

Files:

- `../ai-architect-web/src/components/designs-client.tsx`

### 5. Auth UX polish

- Added browser autocomplete hints for auth inputs.

Files:

- `../ai-architect-web/src/components/auth-form.tsx`

## Browser Validation

Test account used:

- `ui-audit-e172b167@kts.blackbirdzzzz.art`

Scenario projects:

- `generated`: `6b652026-d104-4e29-8a6c-ebba12279cfd`
- `under_review`: `64f80f64-1770-4415-9e98-0fff8bd28ce5`
- `handoff_ready`: `7e54e528-6a24-4ec0-9143-18756700505d`
- `revision_generated`: `974edff4-7cc1-418a-b8c7-6ca21cd04f40`

Verified after deploy:

- Dashboard shows `handoff ready` correctly for `UI Audit Delivery`
- Dashboard shows `under review` correctly for `UI Audit Under Review`
- Review page for generated revision shows:
  - `Dua vao review` enabled
  - `Approve + Lock` disabled
  - `Export Assets` disabled
  - `Create Handoff` disabled
  - `Derive 3D` disabled
- After clicking `Dua vao review`, the same version changes to `under review` and enables `Approve + Lock`
- After clicking `Approve + Lock`, the version changes to `locked` and enables `Export Assets` and `Derive 3D`

## Loop Results

### Public edge

Report:

- `artifacts/production-checks/public-ten-loops-after-fix-20260412.json`

Result:

- Passed loops: `4`
- Failed loop: `5`
- Failure:
  - `POST /api/v1/auth/refresh failed: curl: (35) Recv failure: Connection reset by peer`

Observation:

- Before fix, public loop also failed once at `handoff` with the same `connection reset by peer` pattern.
- After fix, the failure moved to `auth/refresh`, which indicates the remaining flake is not tied to one business endpoint.

### Internal origin via Caddy

Report:

- `artifacts/production-checks/internal-ten-loops-after-fix-20260412.json`

Result:

- Passed loops: `10/10`

Interpretation:

- App core and origin path are stable after the UI/API fixes.
- Remaining instability appears on the public edge path, likely `Cloudflare Tunnel` and/or edge abuse protection under rapid synthetic traffic.

## Verdict

- `Contained fix`: completed for dashboard state summary and review/design UX guardrails.
- `App core`: verified healthy.
- `Residual risk`: public edge resets under aggressive repeated automation still need a separate hardening pass.

## Next Actions

1. Add edge-focused monitoring around `cloudflared` disconnects and upstream resets.
2. Decide whether synthetic production loops should run against public edge or internal origin.
3. If public edge loops are required at high rate, add Cloudflare-side allowances or a lower-frequency monitor profile.
