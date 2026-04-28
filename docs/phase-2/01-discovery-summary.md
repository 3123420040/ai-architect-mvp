---
title: Discovery Summary — Professional Deliverables (2D / 3D / Video)
phase: 2
status: draft
date: 2026-04-26
facilitator: PM/Architect Agent (Claude)
stakeholder: Product Owner (evo-pm-vn@trustingsocial.com)
---

# Discovery Summary — Professional Deliverables Track

## 1. Context

Phase 1 MVP đã có nền: chatbot intake → AI generate floor plan PNG → 3D viewer GLTF → PDF concept package. Tuy nhiên Phase 1 chỉ ở mức **concept-stage visual** — không đạt chuẩn ngành về drafting (line weight, title block, layer organization), không có editable handoff format (DWG/IFC/FBX), và **chưa có video deliverable nào**.

Phase 2 track này nâng deliverables lên **chuẩn thị trường (professional grade)** cho cả 3 trục: 2D, 3D, Video — kèm research + docs market standards đính kèm để dev/test agent có cơ sở thực thi.

## 2. Problem Landscape

| Mục | Hiện tại (Phase 1) | Mong muốn (Phase 2) |
|---|---|---|
| **2D output** | PNG floor plan, không layer/line weight chuẩn | Editable DWG/DXF + PDF presentation, theo NCS hoặc ISO 13567 |
| **3D output** | GLB cho web viewer, không LOD rõ ràng | Multi-format: GLB/USDZ (web/AR) + IFC/FBX/SKP (engineer handoff), LOD 200 |
| **Video output** | Không có | Cinematic flythrough kiểu Twinmotion (4K) + reel social (9:16) |
| **Standards binding** | Tham khảo, chưa bind | Bind chính thức qua ADR, có spec gốc đính kèm |

## 3. Target Users của Output

Sản phẩm phục vụ 3 use case (theo thứ tự ưu tiên):

1. **Sales — Trình khách hàng chốt concept** *(ưu tiên #1)*
   - Khách: chủ nhà tự xây / khách thuê developer
   - Cần: hình ảnh đẹp, dễ hiểu, "wow factor" để chốt deal
   - Không cần: kích thước kỹ thuật chi tiết

2. **Marketing — Bán hàng cho developer BĐS** *(ưu tiên #2)*
   - Khách: developer dự án nhà phố / biệt thự / townhouse
   - Cần: cinematic video reel cho social, hình render độ phân giải cao cho brochure
   - Format: vertical 9:16 (TikTok/Reels) + horizontal 16:9 + still 4K

3. **Engineering Handoff — Kỹ sư thiết kế refine thành sản phẩm cuối** *(ưu tiên #3)*
   - Khách: KTS / kỹ sư thiết kế nội bộ hoặc đối tác
   - Cần: file editable mở được trong tool của họ, đủ structure để pickup không phải rebuild
   - Tools đầu cuối: **SketchUp + V-Ray/Enscape** hoặc **3ds Max + Twinmotion/Lumion**

> ⚠️ **OUT OF SCOPE (xác nhận với PO):** Không cần shop drawing thi công, không cần xin giấy phép xây dựng, không cần TCVN/QCVN compliance trong phase này.

## 4. Scope nội dung output

| Trục | Trong scope | Ngoài scope |
|---|---|---|
| **Phong cách** | Modern minimalist, Tropical (nhiệt đới VN) | Classical, Indochine, Neoclassical (Phase 3+) |
| **Quy mô nhà** | Đa dạng: nhà phố, biệt thự, townhouse, mini hotel | Cao tầng (high-rise apartment, commercial tower) |
| **Stage thiết kế** | Concept Design + Schematic Design (RIBA Stage 2-3) | Detailed Design, Construction Documentation (Stage 4-5) |

## 5. Constraints

- **Budget:** TBD — sẽ ước lượng sau khi có market research
- **Timeline:** TBD — phụ thuộc Phase 1 đang trong M1-M6
- **Technical:**
  - GPU service đã có (`ai-architect-gpu`) — Diffusers/ControlNet/ComfyUI/Blender headless
  - Web viewer Three.js + ThatOpen Components đã có
  - Backend FastAPI orchestration đã có
- **Compliance:** Không bind chuẩn VN trong phase này
- **Open source preference:** Có cân nhắc tool open source (vd. pascalorg/editor) — đang được evaluate

## 6. Key Quotes (verbatim từ stakeholder)

- *"đầu ra của dự án này phải có các sản phẩm file chuyên nghiệp của 2d và 3d và video của sản phẩm, tất cả những đầu ra này phải trên chuẩn của thị trường hiện tại"*
- *"các chuẩn của thị trường hiện tại cũng có research và đầy đủ docs đính kèm"*
- *"Trình khách hàng để chốt concept & Marketing/bán hàng (developer BĐS) → ưu tiên 3D + video render đẹp & đủ cơ sở file kỹ thuật để kỹ sư thiết kế thực hiện công việc tinh chỉnh thành sản phẩm cuối"*
- *"đa dạng quy mô; phong cách chủ yếu hướng đến Modern minimalist, Tropical (nhiệt đới VN)"*

**Reference video sample do PO cung cấp:** YouTube short (https://www.youtube.com/shorts/aVXNUi_UMQQ) + keyword *"Twinmotion design house"* — cinematic real-time architectural visualization, lighting đẹp, vegetation thực, camera mượt.

## 7. Working Model (3 bên)

```
┌─ PM/Architect agent ─┐                    ┌─ Dev/Test agent ─┐
│  • Elicit & clarify   │                    │  • Implement      │
│  • Research standards │ ── via PO/User ──▶ │  • Test           │
│  • Viết PRD/Spec/ADR  │ ◀── (cầu nối) ──── │  • Report back    │
└───────────────────────┘                    └───────────────────┘
```

**Artifacts handoff format:**
1. PRD per deliverable
2. Acceptance Criteria (Given/When/Then, có ví dụ pass/fail)
3. Market Standards Reference Pack (PDF/MD specs gốc)
4. ADR — quyết định chính thức chuẩn nào theo
5. Test Spec cho dev/test agent verify

## 8. Open Questions — RESOLVED (B3 Clarification, 2026-04-26)

| # | Question | Decision |
|---|---|---|
| OQ1 | GPU/render time cap? | **Async-first.** User submit → notification 15-60 phút khi bundle ready. RunPod cloud GPU. |
| OQ2 | Pricing model: flat vs tier? | **Tier — keep simple.** Defer detailed tier design; document placeholder Free/Pro split later. |
| OQ3 | Video độ dài + số cut? | **2 cuts từ 1 master render.** Master walkthrough 60s 4K 16:9 + Marketing reel 20-30s 1080×1920 9:16. Reel auto-derived (no extra GPU). |
| OQ4 | Material library strategy? | **Plan A → Plan C.** MVP: curate CC0 (Quixel/Polyhaven) + ~50 starter Modern Minimalist + Tropical VN. Phase post-MVP: AI procedural via ROOM project — see `agentic-room/docs/external-use-cases/ai-architect-procedural-materials.md` and DEF-006. |
| OQ5 | Multi-language drawing labels? | **VN-only default.** EN translation pass deferred (post-MVP). |

## 9. Next Steps

- [x] **B1 — Discovery** (this doc)
- [x] **B2 — Market Research** → [02-market-standards-research.md](02-market-standards-research.md)
- [x] **B3 — Clarification** OQ1-OQ5 resolved above
- [x] **B4 — ADR-001** ratified → [03-adr-001-standards-combo.md](03-adr-001-standards-combo.md)
- [x] **B4b — Deferred Roadmap** logged → [04-deferred-roadmap.md](04-deferred-roadmap.md)
- [ ] **B5 — PRD + Acceptance Criteria** per deliverable → `05-prd-deliverables.md`
- [ ] **B6 — Sprint Brief handoff** cho dev/test agent → `06-sprint-brief-handoff.md`

---

*Discovery phase COMPLETE 2026-04-26. Moving to PRD + Sprint Brief.*
