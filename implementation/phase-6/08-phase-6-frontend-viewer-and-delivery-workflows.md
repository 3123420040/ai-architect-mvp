# Phase 6 Frontend Viewer and Delivery Workflows

## 1. Purpose

This document freezes the frontend behavior for the Phase 6 presentation-grade 3D workflow.

It exists so web and product teams can implement the new viewer and delivery UX without drifting back into a debug-oriented page.

## 2. Primary Screens in Scope

Phase 6 frontend scope covers:

- 3D generation trigger entry point
- in-progress bundle state
- presentation viewer page
- architect approval surface
- delivery workspace integration

## 3. 3D Generation Entry Contract

### 3.1 Where the action starts

The user should only be able to start Phase 6 generation from a source version that is eligible for presentation derivation.

The UI must show:

- whether the version is eligible
- what outputs will be generated
- what state the current 3D bundle is in

### 3.2 Trigger copy

Suggested Vietnamese-first action language:

- `Tạo gói 3D trình bày`
- `Tạo lại gói 3D`
- `Xem bản xem trước 3D`

Avoid technical copy such as:

- `derive 3D`
- `download model payload`
- `inspect GLTF`

## 4. In-Progress Experience

### 4.1 Progress model

The UI must show a multi-stage progress experience, not just a spinner.

Minimum visible stages:

- `Chuẩn bị dữ liệu 3D`
- `Dựng cảnh`
- `Xuất mô hình 3D`
- `Render hình phối cảnh`
- `Tạo video walkthrough`
- `Kiểm tra chất lượng`

### 4.2 Failure handling

If the job fails:

- show the failure state clearly
- show whether retry is available
- keep prior approved bundle visible if one exists

## 5. Presentation Viewer Contract

### 5.1 Page role

The viewer page must behave like a professional presentation workspace.

It must not show:

- raw JSON payloads
- truncated glTF text
- debug-only internal identifiers as primary content

### 5.2 Required content blocks

The page must include:

- page title and source version reference
- 3D bundle status chip
- hero still preview
- still gallery
- walkthrough video player
- open/download 3D model action
- manifest/download actions where allowed
- approval and degraded status

### 5.3 Status presentation

Required status chips:

- `Chưa tạo`
- `Đang xử lý`
- `Bản xem trước`
- `Cần KTS duyệt`
- `Đã duyệt`
- `Bị chặn phát hành`

If degraded:

- show a compact but obvious `DEGRADED` badge
- show the top blocking reason

## 6. Architect Approval Surface

### 6.1 Required actions

Architect-facing UI must support:

- `Duyệt gói 3D`
- `Từ chối và ghi chú`
- `Xem báo cáo chất lượng`

### 6.2 Guardrails

The UI must block approval CTA when:

- QA status is `fail`
- a required asset is missing
- the bundle is still running

## 7. Delivery Workspace Integration

### 7.1 Relationship to existing delivery workspace

The delivery workspace must treat the Phase 6 3D bundle as one more controlled deliverable family, not as an unrelated viewer shortcut.

Required delivery presentation:

- show latest 3D bundle status beside other delivery outputs
- show whether the bundle is released or preview only
- expose download/view actions only when contract allows

### 7.2 Release labels

Required release labels:

- `Xem trước nội bộ`
- `Đã sẵn sàng phát hành`
- `Đã phát hành`
- `Phát hành bị chặn`

## 8. UX Rules

### 8.1 Content priority

Primary content order:

1. hero visual
2. delivery state
3. gallery and video
4. actions
5. technical metadata

### 8.2 Language quality

All user-facing strings in this phase must be:

- Vietnamese with diacritics
- concise
- non-technical where possible
- consistent across viewer and delivery workspace

### 8.3 Mobile and desktop

The viewer must still be functional on smaller screens, but desktop remains the primary target for the full gallery and approval experience.

## 9. Frontend Acceptance Criteria

Phase 6 frontend is acceptable only if:

- the page no longer looks like a debug viewer,
- users can understand whether a bundle is preview, approved, or blocked,
- approval actions are explicit,
- video and stills are part of the main experience,
- and the viewer reflects the bundle-based backend contract rather than legacy `model_url`-only behavior.
