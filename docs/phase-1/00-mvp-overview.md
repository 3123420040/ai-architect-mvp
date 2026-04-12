# Phase 1 – MVP Overview: AI Architect

*Ngày chốt: Apr 11, 2026*

---

## 1. Product Vision

**AI Architect** là nền tảng AI-native giúp khách hàng thiết kế nhà ở từ giai đoạn ý tưởng đến bản vẽ concept, thay thế phần lớn công việc lặp lại của kiến trúc sư (drafting, revision, visualization) trong giai đoạn concept design.

---

## 2. Target Users (Phase 1)

| Persona | Mô tả | Giá trị nhận được |
|---------|--------|-------------------|
| **Chủ nhà tự xây** | Cá nhân có lô đất, muốn xây/cải tạo nhà | Xem được concept 3D trong vài phút, không cần thuê KTS cho giai đoạn ý tưởng |
| **Công ty thiết kế nhỏ (5-10 người)** | Cần tăng throughput mà không tuyển thêm | AI tạo draft nhanh, KTS chỉ review & finalize → giảm 60-70% thời gian concept |

> **Phase 1 focus: B2B** – bán tool cho công ty thiết kế (dễ onboard hơn, feedback loop nhanh hơn). B2C mở ở Phase 3.

---

## 3. Core Loop (MVP)

```
[1] User Input        →  Nhập thông tin lô đất, yêu cầu, style preference
        ↓
[2] AI Generate       →  AI tạo 2D floor plan + 3D visualization draft
        ↓
[3] Expert Review     →  KTS nội bộ review, annotate, approve/reject
        ↓
[4] Present to Client →  Trình bản concept cho khách hàng
        ↓
[5] Client Feedback   →  Khách hàng góp ý chỉnh sửa
        ↓
[6] AI Revise         →  AI update thiết kế → quay lại bước [3]
```

**Mục tiêu:** Giảm số vòng revision từ 8-10 xuống < 3, tăng chất lượng output mỗi lần trình bày.

---

## 4. Phase 1 Scope

### IN SCOPE

| Feature | Mô tả |
|---------|--------|
| **Intake Chatbot** | Chat AI thu thập thông tin: kích thước đất, budget, style, số phòng, lifestyle |
| **Structured Form** | Form bổ sung cho intake có cấu trúc (backup cho chat) |
| **AI Floor Plan Generation** | Text + kích thước đất → 2D floor plan (2-3 variations) |
| **3D Visualization** | Floor plan → 3D render exterior + interior key rooms |
| **3D Viewer (Web)** | Xem, xoay, zoom 3D model trên browser |
| **Revision Loop** | User feedback bằng text → AI regenerate design |
| **Version History** | Lưu lại các version design, so sánh side-by-side |
| **Expert Review Gate** | Queue cho KTS review, annotate, approve/reject |
| **Export** | PDF bản vẽ sơ bộ + hình ảnh 3D high-res |

### OUT OF SCOPE (Phase 1)

- Bản vẽ thi công (construction documents) – cần KTS licensed
- Tính toán kết cấu, MEP (điện, nước, HVAC)
- Quản lý thi công & tiến độ
- Marketplace kết nối nhà thầu/vật liệu
- IFC/BIM export đầy đủ (chỉ hỗ trợ basic DXF nếu kịp)
- Mobile app (web responsive first)
- Tự động kiểm tra quy chuẩn xây dựng QCVN

---

## 5. Success Metrics

| Metric | Target |
|--------|--------|
| Time-to-first-concept | < 10 phút từ khi user hoàn tất intake |
| Revision cycles | < 3 vòng để đạt client approval |
| KTS approval rate | > 60% design không cần major rework |
| NPS (beta users) | > 40 |
| Throughput improvement | 3x so với workflow truyền thống |

---

## 6. Key Decisions

1. **Visual plausibility first, engineering fidelity later** – MVP ưu tiên tạo concept đẹp, nhanh. Cấu trúc kỹ thuật (IFC, BIM) sẽ nâng cấp dần ở Phase 2+.
2. **Image-first generation** – Dùng Diffusion model (ControlNet + Stable Diffusion) để generate floor plan dạng image, không dùng parametric model (quá phức tạp cho MVP).
3. **Human-in-the-loop bắt buộc** – Mọi output AI đều phải qua KTS review trước khi trình khách hàng. AI không thay thế hoàn toàn KTS.
4. **Web-first** – Toàn bộ trải nghiệm trên browser, không yêu cầu cài đặt phần mềm.
5. **B2B trước B2C** – Phase 1 target design firms, Phase 3 mới mở cho end-user.

---

## 7. Architecture Strategy

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENT (Browser)                      │
│  Next.js + React + Three.js + ThatOpen BIM Components   │
│  [Chat UI] [Intake Form] [3D Viewer] [Review Dashboard] │
└──────────────────────┬──────────────────────────────────┘
                       │ REST/WebSocket
┌──────────────────────▼──────────────────────────────────┐
│                  BACKEND (FastAPI)                        │
│  [Auth] [Project API] [Version API] [Export API]         │
│  [Agent Orchestrator - LangGraph]                        │
│    ├── Requirements Agent                                │
│    ├── Design Agent                                      │
│    ├── Review Agent                                      │
│    └── Revision Agent                                    │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│              GENERATION SERVICE (GPU)                     │
│  ComfyUI / Diffusers + ControlNet                        │
│  [Floor Plan Gen] [3D Render Gen] [Revision Gen]         │
└─────────────────────────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                   DATA LAYER                              │
│  PostgreSQL (projects, users, versions, feedback)         │
│  S3/MinIO (images, 3D files, PDFs)                       │
│  Redis (queue, cache, realtime)                           │
└─────────────────────────────────────────────────────────┘
```

---

## 8. Timeline Estimate

| Milestone | Nội dung |
|-----------|----------|
| **M1: Foundation** | Project setup, DB schema, auth, basic UI shell |
| **M2: Intake + Agent** | Chat intake, structured form, LangGraph agent pipeline |
| **M3: Generation** | ComfyUI/Diffusers pipeline, floor plan gen, 3D render |
| **M4: Viewer + Review** | 3D viewer, version history, KTS review dashboard |
| **M5: Revision Loop** | Feedback → regeneration pipeline, side-by-side compare |
| **M6: Export + Polish** | PDF export, UX polish, beta testing |

---

## 9. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| AI output chưa đủ professional | Mất trust từ beta users | Human review gate bắt buộc, kỳ vọng rõ ràng "concept design only" |
| GPU cost cao | Burn rate vượt budget | ComfyUI optimize workflow, batch processing, RunPod spot instances |
| Licensing conflict (GPL repos) | Không thể commercialize | Audit license trước khi integrate; dùng MIT-licensed alternatives khi có thể |
| Floor plan không feasible | KTS reject rate cao | Thêm basic constraint rules, collect rejection data để improve model |
| B2B adoption chậm | Không đủ beta users | Bắt đầu với 3-5 firm quen biết, offer free trial |
