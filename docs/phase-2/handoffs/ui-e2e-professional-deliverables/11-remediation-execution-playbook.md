---
title: UI E2E Professional Deliverables Remediation Execution Playbook
phase: 2
status: ready-for-execution-review
date: 2026-04-27
owner: Codex Coordinator
related_files:
  - 09-retro-action-plan.md
  - 10-remediation-implementation-contract.md
source_project_id: 3b00f863-3144-4223-b04d-dec825c894d8
---

# UI E2E Professional Deliverables Remediation Execution Playbook

Tài liệu này viết để một dev/agent bất kỳ có thể dựa vào đó sửa lại toàn bộ flow đã phát hiện lỗi, không cần phải đọc lại toàn bộ log điều tra ban đầu.

Mục tiêu của tài liệu này là biến phần phân tích ở `09-retro-action-plan.md` và contract ở `10-remediation-implementation-contract.md` thành kế hoạch sửa cụ thể theo thứ tự, có input, output, file cần đụng, kiểm chứng, và câu hỏi cần PM chốt.

## 1. Tóm Tắt Vấn Đề Cần Sửa

Flow Phase 2 hiện đã có một happy path từng được sign-off, nhưng khi kiểm tra project thật `3b00f863-3144-4223-b04d-dec825c894d8`, sản phẩm chưa đạt mức dùng được:

- Intake không thực sự là AI extraction; parser regex bỏ sót và parse sai tiếng Việt tự nhiên.
- Designs, Review, Delivery không load được hình vì asset MinIO bị private.
- Mỗi page tự chọn version khác nhau; Delivery có thể chọn nhầm version `superseded`.
- Professional deliverables job có tạo một số file thật, nhưng job failed và không register asset vào DB.
- Video pipeline cho phép MP4 invalid đi tiếp sang bước sau.
- Product path đang chạy cả Sprint 4, trái scope Option B first slice.
- Share link gọi sai API path.
- Viewer dùng pipeline Presentation3D legacy, không dùng GLB từ professional deliverables.
- UX của Designs, Review, Delivery, Viewer không thể hiện đúng lifecycle, state, lỗi và next action.
- Professional worker thiếu `usd-core==26.5`.

Kết luận: phải sửa theo nền tảng trước, UX sau. Nếu chỉ redesign UI mà không sửa asset/version/job state, sản phẩm vẫn nói sai.

## 2. Phạm Vi Được Sửa

### API repo

Root:

`/Users/nguyenquocthong/project/ai-architect/ai-architect-api`

Được sửa:

- `app/services/storage.py`
- `app/api/v1/projects.py`
- `app/api/v1/share.py`
- `app/api/v1/professional_deliverables.py`
- `app/services/professional_deliverables/orchestrator.py`
- `app/tasks/professional_deliverables.py`
- `app/services/professional_deliverables/video_renderer.py`
- `app/services/professional_deliverables/sprint3_demo.py`
- `app/services/professional_deliverables/camera_path.py`
- `app/services/professional_deliverables/geometry_adapter.py` nếu cần fix wall/room bounds.
- `app/models.py`
- `app/schemas.py`
- `app/services/briefing.py`
- `app/services/llm.py` chỉ khi quyết định bật structured LLM.
- `Dockerfile.professional-worker`
- `alembic/versions/` nếu đổi schema.
- `tests/`

Không được sửa theo hướng phá scope:

- Không bỏ golden fixture functions.
- Không đưa Blender/KTX/FFmpeg vào main API image.
- Không overload `Presentation3DBundle` cho professional deliverables.
- Không chạy render nặng trong FastAPI request.

### Web repo

Root:

`/Users/nguyenquocthong/project/ai-architect/ai-architect-web`

Được sửa:

- `src/lib/api.ts`
- `src/lib/professional-deliverables.ts`
- new `src/lib/version-selection.ts`
- new shared UI component nếu cần:
  - `src/components/asset-image.tsx`
  - `src/components/professional-deliverables-status.tsx`
  - `src/components/version-badge.tsx`
- `src/components/designs-client.tsx`
- `src/components/review-client.tsx`
- `src/components/delivery-client.tsx`
- `src/components/viewer-client.tsx`
- `src/components/share-client.tsx`

Không được làm:

- Không xóa legacy export/handoff/presentation 3D UI.
- Không thêm Sprint 4 UI artifact slots.
- Không che lỗi bằng cách ẩn mọi trạng thái failed.

### Docs/compose repo

Root:

`/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`

Được sửa:

- `docker-compose.local.yml` nếu cần cho worker/toolchain/MinIO bootstrap.
- Docs trong thư mục handoff này.

## 3. Quyết Định Kỹ Thuật Đề Xuất

Các quyết định dưới đây là mặc định khuyến nghị để dev không bị kẹt. Nếu PM không đồng ý, phải chốt lại trước khi code.

### D-01 - Asset access

Khuyến nghị: dùng API asset proxy hoặc presigned URL helper, không để browser đọc raw private MinIO URL.

Mặc định đề xuất:

- Persist canonical storage reference trong DB hoặc URL hiện có.
- Khi serialize API response, convert sang browser-readable URL.
- Với file local `/media/...`, tiếp tục dùng `/media/...`.
- Với object MinIO, trả presigned URL hoặc API proxy URL.

Lý do:

- Public bucket local-only dễ chạy nhưng không đúng production shape.
- Presigned/proxy giúp Web không cần biết object storage internals.

### D-02 - Current version

Khuyến nghị: latest approved/locked version là current.

Rule:

1. Latest `locked` version.
2. Latest `handoff_ready`.
3. Latest `delivered`.
4. Latest non-superseded generated/candidate version.
5. Superseded chỉ được chọn nếu không còn version nào khác.

Tất cả Designs, Review, Delivery, Viewer phải dùng cùng helper.

### D-03 - Partial artifact behavior

Khuyến nghị: cho phép hiển thị artifact đã tạo thành công ở trạng thái `partial`, có warning rõ.

Lý do:

- Nếu PDF/GLB/USDZ đã tạo xong nhưng video/camera gate fail, khách hàng/dev vẫn cần thấy evidence thật.
- Không được gọi chúng là final approved deliverables nếu validation fail.

### D-04 - Viewer source

Khuyến nghị: Viewer ưu tiên professional deliverables GLB, sau đó mới fallback Presentation3D legacy.

Priority:

1. Professional GLB asset của current version.
2. Legacy Presentation3D scene GLB nếu có.
3. Empty state hướng user về Review/Delivery để generate.

### D-05 - Intake intelligence

Khuyến nghị ngắn hạn: sửa deterministic parser và thêm tests. Không bật LLM thật nếu chưa có quyết định credentials/cost/reliability.

Nếu product vẫn gọi đây là "AI hỏi đáp", cần roadmap bật structured LLM extraction sau, nhưng P0/P1 không nên phụ thuộc vào nó.

## 4. Quyết Định PM Đã Chốt

PM đã chốt toàn bộ theo khuyến nghị. Người implement không cần hỏi lại các quyết định này.

1. Asset URL strategy: dùng API proxy hoặc presigned URL helper. Không dùng raw private MinIO URL. Không lấy public MinIO bucket làm product default.
2. Partial artifacts: được cho tải artifact đã tạo thành công khi bundle failed/partial, nhưng phải gắn nhãn rõ `Partial / not final`.
3. Viewer: được hiển thị GLB từ bundle failed/partial nếu GLB hợp lệ, nhưng phải có warning rằng bundle chưa final.
4. Current version: latest `locked` version là source of truth.
5. Intake: fix deterministic parser trước. Không yêu cầu structured LLM thật trong remediation này.

## 5. Trình Tự Thực Hiện

Không đảo thứ tự nếu không có lý do kỹ thuật rõ ràng.

### Batch 1 - Product foundations

Mục tiêu: các page nhìn thấy đúng dữ liệu và asset.

1. Fix asset access.
2. Fix share path.
3. Tạo shared current-version helper.
4. Áp helper vào Designs, Review, Delivery, Viewer.
5. Thêm fallback image component.

Exit criteria:

- Designs/Review/Delivery/Share load hình.
- Share token page không còn 404.
- Review/Delivery/Viewer chọn cùng current version.

### Batch 2 - Professional deliverables correctness

Mục tiêu: job không chạy sai scope và API nói thật.

1. Remove Sprint 4 from product path.
2. Fix stage/progress contract.
3. Register artifacts theo phase hoặc partial.
4. Preserve gate summaries on failure.
5. Fix retry semantics.

Exit criteria:

- New job không có `derive_reel`, `build_manifest`.
- Delivery thấy failed/partial/ready đúng.
- DB có asset rows cho file đã tạo thành công.

### Batch 3 - Media/render robustness

Mục tiêu: video và camera gate fail đúng chỗ, rõ lý do.

1. Validate MP4 immediately after render.
2. Stop on invalid MP4.
3. Add structured video error.
4. Reproduce V4 camera collision.
5. Fix camera path/fallback.

Exit criteria:

- Invalid MP4 không được expose.
- Camera path không collide với V4 fixture hoặc fail sớm trước render.

### Batch 4 - Worker toolchain

Mục tiêu: worker đúng requirement.

1. Install `usd-core==26.5`.
2. Verify `from pxr import Usd`.
3. Ensure main API image vẫn slim.

Exit criteria:

- Worker toolchain verification pass.

### Batch 5 - UX cleanup

Mục tiêu: người dùng hiểu trạng thái và next action.

1. Review state-driven layout.
2. Delivery artifact/status layout.
3. Viewer professional GLB integration.
4. Designs lifecycle grouping.

Exit criteria:

- Không có raw backend error làm primary message.
- Không có anchor rỗng.
- Không có Sprint 4 slots.
- Current/selected/historical versions rõ.

### Batch 6 - Intake parser

Mục tiêu: parse đúng các câu tiếng Việt thực tế đã fail.

1. Fix dimension separators.
2. Fix compound orientation order.
3. Fix Vietnamese negation splitting.
4. Add tests.

Exit criteria:

- Regression sentence parse đúng.
- Brief không ready nếu field critical ambiguous.

## 6. Implementation Cards

### Card A1 - Asset URL resolver

Problem:

- `storage.py` trả direct MinIO URL private.

Target:

- API response trả URL browser đọc được.

Implementation notes:

1. Mở `app/services/storage.py`.
2. Tìm function sinh URL hiện tại.
3. Thêm helper phân loại:
   - local media path
   - already public HTTP URL
   - MinIO/S3 object URL
   - storage key
4. Nếu chọn presigned:
   - helper lấy bucket/key.
   - gọi MinIO/S3 presign at response time.
5. Nếu chọn API proxy:
   - tạo route `/api/v1/assets/{...}` hoặc `/media/assets/{token}`.
   - route validate access hoặc dùng signed opaque token.
6. Áp resolver trong serializer project/version/share/professional bundle.

Files:

- `app/services/storage.py`
- `app/api/v1/projects.py`
- `app/api/v1/share.py`
- `app/services/professional_deliverables/orchestrator.py`

Tests:

- Unit test resolver với raw MinIO URL.
- API test project detail trả URL không gây 403.

Manual:

- Curl image URL.
- Browser `img.naturalWidth > 0`.

Do not:

- Không hardcode replace `localhost:19000` bằng web origin trong frontend.
- Không lưu presigned URL dài hạn vào DB.

### Card A2 - Shared image component

Problem:

- Broken images collapse or look empty.

Target:

- Every image box has stable ratio and visible fallback.

Implementation notes:

1. Tạo `src/components/asset-image.tsx`.
2. Props:
   - `src`
   - `alt`
   - `className`
   - `aspectRatio`
   - `fallbackLabel`
3. Track `onError`.
4. Render fallback block if missing/error.
5. Use `assetUrl()` only once inside component or before passing in, but be consistent.

Use in:

- `designs-client.tsx`
- `review-client.tsx`
- `delivery-client.tsx`
- `share-client.tsx`

Acceptance:

- Missing image never collapses.
- User sees `Không tải được hình` or equivalent.

### Card B1 - Version selection helper

Problem:

- Review, Delivery, Viewer select different versions.

Target:

- One helper determines current version.

Implementation notes:

Create `src/lib/version-selection.ts`:

```ts
export type VersionLike = {
  id: string;
  version_number?: number | null;
  status?: string | null;
  created_at?: string | null;
};

export function pickCurrentVersion<T extends VersionLike>(versions: T[]): T | null {
  // Sort newest first by version_number, then created_at.
  // Prefer statuses in order:
  // locked, handoff_ready, delivered, approved, generated/under_review/non-superseded, superseded last.
}
```

Also expose:

```ts
export function isHistoricalVersion(version: VersionLike, currentId?: string | null): boolean;
export function versionLifecycleLabel(version: VersionLike, currentId?: string | null): string;
```

Files to update:

- `src/components/designs-client.tsx`
- `src/components/review-client.tsx`
- `src/components/delivery-client.tsx`
- `src/components/viewer-client.tsx`

Acceptance:

- Same current version id on all pages.
- For regression project, V4 should be selected if it is the latest locked version.

### Card C1 - Share fetch path

Problem:

- `publicFetch()` calls API origin without `/api/v1`.

Target:

- Share page calls `http://localhost:18000/api/v1/share/{token}`.

Implementation notes:

In `src/lib/api.ts`:

- Keep `API_ORIGIN` for media URLs.
- Add `PUBLIC_API_BASE_URL` or make `publicFetch()` call `buildApiUrl(path)`.

Expected simple fix:

```ts
export async function publicFetch<T>(path: string): Promise<T> {
  const response = await fetch(buildApiUrl(path), { cache: "no-store" });
  ...
}
```

Then check `assetUrl()` still uses origin for `/media/...`.

Acceptance:

- Share page no longer renders raw `{"detail":"Not Found"}`.

### Card D1 - Remove Sprint 4 from product task

Problem:

- Product task calls `derive_sprint4_video_outputs`, `build_manifest`, `run_sprint4_gates`.

Target:

- Phase 2 product task only checks required Phase 2 artifacts.

Implementation notes:

In `app/tasks/professional_deliverables.py`:

1. Remove imports:
   - `build_manifest` if only used for Sprint 4 final manifest.
   - `run_sprint4_gates`.
   - `derive_sprint4_video_outputs`.
2. Change `REQUIRED_PRODUCT_ARTIFACTS` to:
   - `2d/bundle.pdf`
   - `3d/model.glb`
   - `3d/model.fbx`
   - `3d/model.usdz`
   - `video/master_4k.mp4`
   - `sprint3_gate_summary.json`
   - `sprint3_gate_summary.md`
   - plus at least one `2d/*.dxf`
   - DWG optional with explicit ODA skip.
3. Remove stage calls:
   - `derive_reel`
   - `build_manifest`
   - `archive_bundle`
4. Set `validate` to progress 95.
5. Keep golden Sprint 4 tests untouched if they exist as standalone, but do not run Sprint 4 from product job.

Acceptance:

- New product job output root has no Sprint 4 product outputs.
- Existing Sprint 1-3 commands still pass.

### Card E1 - Stage/progress contract

Problem:

- Existing stages do not match contract.

Target:

Allowed stages:

```text
queued 0
adapter 10
export_2d 25
export_3d 50
export_usdz 65
render_video 85
validate 95
ready 100
failed preserves last progress
```

Implementation notes:

In `orchestrator.py`:

- Replace `STAGE_PROGRESS`.
- Ensure `mark_job_failed()` does not reset progress except when no real progress happened.
- Add `updated_at` touch if needed.

In Web:

- Stage labels only for approved stages.
- Unknown stage should render as technical fallback, not crash.

Acceptance:

- Progress bar never shows removed stages in new jobs.

### Card E2 - Partial artifact registration

Problem:

- Asset rows only registered after all validation passes.

Target:

- Register artifacts once they exist and pass minimal file checks.

Implementation approach:

1. Add helper:

```py
def register_existing_artifacts(db, bundle, root, *, status="ready") -> list[ProfessionalDeliverableAsset]:
    ...
```

2. Call after each phase:
   - after 2D generation: PDF, DXF, DWG if exists, Sprint 1 gate summaries if desired.
   - after 3D generation: GLB, FBX.
   - after USDZ generation: USDZ.
   - after video generation and ffprobe validation: MP4.
   - after gate summary generation: JSON/MD.
3. Make registration idempotent:
   - unique by `bundle_id + asset_role + storage_key`, or manually check before insert.
4. Add `asset.status` if schema supports it; if not, add migration.

Recommended schema additions if not already present:

- `ProfessionalDeliverableAsset.status`: `ready | partial | failed | skipped`
- `ProfessionalDeliverableAsset.skip_reason`
- `ProfessionalDeliverableAsset.validation_error`
- `ProfessionalDeliverableBundle.failed_gates_json`
- `ProfessionalDeliverableBundle.warnings_json`
- `ProfessionalDeliverableBundle.missing_artifacts_json`
- `ProfessionalDeliverableBundle.user_message`
- `ProfessionalDeliverableBundle.technical_details_json`

If avoiding schema expansion:

- Use existing `degraded_reasons_json` plus job error fields.
- Still register artifact rows that exist.

Acceptance:

- Failed V4-style job can show PDF/GLB/FBX/USDZ/MP4 if they exist and pass file checks.
- Failed V2-style job must not show invalid MP4 as ready.

### Card F1 - MP4 validation boundary

Problem:

- Invalid `master_4k.mp4` continues to later stages.

Target:

- Validate master MP4 immediately.

Implementation notes:

In video renderer or task:

1. After `generate_project_ar_video_bundle`, locate `video/master_4k.mp4`.
2. Run ffprobe check using existing validator if available.
3. If invalid:
   - set job failed.
   - error_code: `VIDEO_MASTER_INVALID`
   - user message: `Video master render failed.`
   - technical details: ffprobe output.
   - do not register MP4 as ready.
   - do not proceed to any next generation.

If `sprint3_demo.py` currently records gate failure but returns result, task must inspect gate results before continuing.

Acceptance:

- 48-byte MP4 is not downloadable.
- Error stage is `render_video` or `validate`.

### Card G1 - Camera collision fixture

Problem:

- V4 fails camera collision after expensive render.

Target:

- Detect/fix camera collision for generated geometry.

Implementation notes:

1. Dump V4 `geometry_json` into a test fixture or build a compact equivalent fixture.
2. Reproduce camera path with `geometry_to_drawing_project`.
3. Run camera collision validator without full video render if possible.
4. Fix camera path:
   - keep minimum wall offset.
   - avoid paths through room bounding boxes that intersect walls.
   - add fallback: center orbit / doorway-safe path / static room viewpoint.
5. Add regression test.

Acceptance:

- V4 fixture no longer fails `Bep va an at 28.0s intersects wall-f1-07`.
- If no safe path exists, fail before render with `CAMERA_PATH_UNSAFE`.

### Card H1 - Worker usd-core

Problem:

- `usd-core==26.5` missing.

Target:

- Professional worker includes USD Python bindings.

Implementation notes:

In `Dockerfile.professional-worker`:

- Install `usd-core==26.5` in the Python 3.12 environment used by the worker.
- Verify with `from pxr import Usd`.
- Keep main API Dockerfile unchanged.

Acceptance:

```bash
docker exec kts-blackbirdzzzz-art-professional-worker python -m pip show usd-core
docker exec kts-blackbirdzzzz-art-professional-worker python -c "from pxr import Usd; print('ok')"
```

### Card I1 - Professional deliverables API response shape

Problem:

- Current response is too thin for honest UI.

Target:

Response should let UI render state without guessing.

Minimum response:

```json
{
  "bundle_id": "...",
  "version_id": "...",
  "status": "queued|running|failed|partial|ready",
  "quality_status": "pending|pass|partial|failed",
  "is_degraded": false,
  "degraded_reasons": [],
  "user_message": "Short customer-readable message",
  "technical_details": {},
  "failed_gates": [],
  "missing_artifacts": [],
  "assets": [
    {
      "url": "/media/...",
      "asset_type": "2d|3d|video|gate_summary",
      "asset_role": "pdf|dxf|dwg|glb|fbx|usdz|mp4|gate_summary_json|gate_summary_md",
      "status": "ready|partial|failed|skipped",
      "content_type": "...",
      "byte_size": 123,
      "skip_reason": null,
      "validation_error": null
    }
  ],
  "current_job": {
    "job_id": "...",
    "status": "queued|running|failed|succeeded",
    "stage": "render_video",
    "progress_percent": 85,
    "error_code": null,
    "error_message": null
  },
  "updated_at": "..."
}
```

If schema changes are too large, keep backward compatibility:

- Existing fields must remain.
- New fields optional.

Acceptance:

- Review/Delivery can render all states from API response alone.

### Card J1 - Review UI state machine

Target states:

```text
no_current_version
version_selected_not_locked
locked_no_bundle
bundle_queued
bundle_running
bundle_failed
bundle_partial
bundle_ready
```

Primary action by state:

- `no_current_version`: go to Designs.
- `version_selected_not_locked`: approve/lock version.
- `locked_no_bundle`: generate professional deliverables.
- `bundle_queued/running`: no destructive primary action; show progress.
- `bundle_failed`: retry job.
- `bundle_partial`: go to Delivery, retry optional.
- `bundle_ready`: go to Delivery.

Do:

- Show selected/current version clearly.
- Show progress card near primary action.
- Use short error copy.

Do not:

- Put approve/reject/export/share/generate all at same visual priority.
- Show raw ffprobe as primary text.

### Card K1 - Delivery UI state machine

Target:

- Delivery is artifact readiness/download page.

Sections:

1. Current version summary.
2. Professional deliverables status.
3. Artifact list.
4. Gate/warning summary.
5. Legacy export/handoff/presentation section, separate.

Artifact rows:

- PDF
- DXF
- DWG
- GLB
- FBX
- USDZ
- MP4
- Gate JSON
- Gate MD

Row states:

- `ready`: clickable.
- `partial`: clickable with warning.
- `skipped`: not clickable, show reason.
- `missing`: not clickable, show missing.
- `failed`: not clickable or diagnostic only.

Do not:

- Render `<a>` without `href`.
- Show Sprint 4 rows.
- Say `Chưa tạo` if a failed bundle exists.

### Card L1 - Viewer GLB integration

Implementation notes:

1. Fetch current version professional bundle.
2. Find asset role `glb`.
3. If exists, pass to existing 3D viewer scene.
4. If no professional GLB, fetch legacy Presentation3D as fallback.
5. Empty state should say:
   - `Chưa có mô hình 3D cho phiên bản hiện tại. Hãy tạo professional deliverables từ Review.`

Acceptance:

- Viewer opens GLB from professional deliverables for current version.
- Failed/partial bundle can still show GLB with warning if GLB asset is valid.

### Card M1 - Designs lifecycle grouping

Target grouping:

- Current approved version.
- Candidate versions.
- Historical versions.

Implementation notes:

- Use `pickCurrentVersion`.
- Sort newest first within groups.
- De-emphasize superseded.
- Generation action after lock should be secondary and framed as creating a revision, not the main next step.

Acceptance:

- User can immediately identify the approved design.

### Card N1 - Intake parser regression

Implementation notes:

In `briefing.py`:

- Dimension regex:

```py
r"(\d+(?:[.,]\d+)?)\s*(?:x|×|\*|by)\s*(\d+(?:[.,]\d+)?)"
```

- Orientation: ensure compound directions are evaluated before simple directions.
- Improve negation:
  - split `bat buoc A va tranh B` into must-have `A`, must-not-have `B`.
  - handle `khong muon`, `tranh`, `han che`.

Tests:

- Add to `tests/test_briefing.py`.

Regression sentence:

```text
Nha biet thu xay moi lo 7*25m huong Tay Nam, 3 tang, 4 phong ngu, 3 WC, gara 1 o to, phong tho, 6 nguoi o gom ong ba va 2 tre nho, phong cach hien dai am xanh gan gui tu nhien, ngan sach khoang 7 ty, muon hoan thanh trong 8 thang, bat buoc nhieu anh sang thong gio va tranh khong gian bi.
```

Expected:

- `lot.width_m = 7`
- `lot.depth_m = 25`
- `lot.orientation = southwest`
- `floors = 3`
- `rooms.bedrooms = 4`
- `rooms.bathrooms = 3`
- `special_requests` includes garage and prayer room.
- `occupant_count = 6`
- `budget_vnd = 7000000000`
- `timeline_months = 8`
- daylight/ventilation priorities captured.
- avoid cramped/dark spaces captured as negative constraint.

## 7. Testing Matrix

### Backend tests

Required:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/test_briefing.py
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py
make sprint3-ci-linux
```

Add focused tests:

- Asset resolver tests.
- Current-version selection API if implemented backend-side.
- Professional deliverables response includes partial assets.
- Product job excludes Sprint 4.
- Invalid MP4 does not register ready asset.
- Intake regression sentence.

### Web tests/checks

Required:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build
```

Add if test framework exists:

- `pickCurrentVersion` helper tests.
- `findProfessionalAsset` role matching tests.
- State mapping tests for professional bundle status.

### Docker/toolchain

Required:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
docker compose -f docker-compose.local.yml up --build
```

Worker checks:

```bash
docker exec kts-blackbirdzzzz-art-professional-worker blender --version
docker exec kts-blackbirdzzzz-art-professional-worker ktx --version
docker exec kts-blackbirdzzzz-art-professional-worker ffmpeg -version
docker exec kts-blackbirdzzzz-art-professional-worker ffprobe -version
docker exec kts-blackbirdzzzz-art-professional-worker node --version
docker exec kts-blackbirdzzzz-art-professional-worker python --version
docker exec kts-blackbirdzzzz-art-professional-worker python -m pip show usd-core
docker exec kts-blackbirdzzzz-art-professional-worker python -c "from pxr import Usd; print('ok')"
```

### Browser/manual checks

Use Playwright or manual browser:

1. Open `/projects/3b00f863-3144-4223-b04d-dec825c894d8/designs`.
2. Confirm all visible images have non-zero natural size.
3. Confirm current approved version is obvious.
4. Open `/review`.
5. Confirm same current version.
6. Confirm professional deliverables state is correct.
7. Retry/generate a job if needed.
8. Observe progress stages.
9. Open `/delivery`.
10. Confirm same current version.
11. Confirm artifact list is honest.
12. Open `/viewer`.
13. Confirm professional GLB renders or empty state gives next action.
14. Open `/share/k2GgHmvg6UG2SOEXdrP_C687`.
15. Confirm shared content loads.

## 8. Done Criteria By Severity

### P0 done

- Asset images load.
- Share link works.
- Current version consistent.
- No Sprint 4 in new product job path.
- Delivery no longer lies about failed/partial bundle state.

### P1 done

- Invalid MP4 stops correctly.
- Camera collision regression fixed or fails early.
- Partial artifacts registered.
- Worker has `usd-core==26.5`.

### P2 done

- Review usable as decision/progress page.
- Delivery usable as artifact page.
- Viewer loads professional GLB.
- Designs page lifecycle is understandable.

### P3 done

- Intake parser handles the regression Vietnamese sentence.
- Critical ambiguity is not silently accepted.

## 9. Common Failure Modes To Avoid

- Fixing images only in Web by changing URL strings, while API still returns private storage URLs.
- Making MinIO public globally without documenting that this is local-only.
- Selecting current version differently per page.
- Hiding failed jobs and showing `Chưa tạo`.
- Registering invalid MP4 as ready.
- Continuing pipeline after render failure.
- Adding Sprint 4 artifacts back into Delivery because files exist on disk.
- Breaking Sprint 1-3 golden commands while changing product path.
- Making Viewer depend only on Presentation3D.
- Showing raw ffmpeg logs to customer as the main message.
- Marking job `ready` when required Phase 2 artifacts are missing.

## 10. Suggested Agent Prompt For Implementation

Use this prompt for a coding agent after PM confirms or accepts the defaults:

```text
You are the implementation agent for AI Architect Phase 2 remediation.

Read:
- docs/phase-2/handoffs/ui-e2e-professional-deliverables/09-retro-action-plan.md
- docs/phase-2/handoffs/ui-e2e-professional-deliverables/10-remediation-implementation-contract.md
- docs/phase-2/handoffs/ui-e2e-professional-deliverables/11-remediation-execution-playbook.md

Implement the remediation in batches:
1. Asset access, share link, current-version helper, image fallback.
2. Professional deliverables scope/state fixes: remove Sprint 4 from product path, approved stages only, partial artifact registration.
3. Invalid MP4 handling, camera collision regression, worker usd-core.
4. Review/Delivery/Viewer/Designs UX cleanup.
5. Intake parser regression fixes.

Do not push remote. Do not open PR. Do not commit unless asked.
Do not relax PRD acceptance. Do not add Sprint 4 outputs to Phase 2 UI E2E.
Preserve Sprint 1-3 golden pipelines.
Keep heavy tools in professional-worker only.

Run required API, Web, Docker, and manual verification commands.
Report PASS/BLOCKED/NEEDS_REVIEW using the report format in 10-remediation-implementation-contract.md.
```

## 11. Final PM Decisions

These decisions are already approved:

1. Asset access uses API proxy or presigned URL helper.
2. Partial artifacts are downloadable when individually valid and clearly labeled.
3. Viewer may display valid GLB from failed/partial bundles with warning.
4. Latest `locked` version is the current approved version.
5. Intake remediation fixes deterministic parser first; real LLM extraction is deferred unless separately approved.

Implementation should proceed using these decisions without reopening scope.
