# Tổng hợp phản biện và quyết định chốt cho review OSS – AI Architect

*Nguồn đối chiếu chính: `05-system-design.md`, `AI_Architect_OSS_Research_Report.docx`, `07-oss-proposal-review.md`*  
*Ngày tổng hợp: 2026-04-11*

---

## 1) Kết luận ngắn

Tôi **đồng ý phần lớn** với review trong `07-oss-proposal-review.md` và chốt ở mức:

**Accept with recalibration**

Ý nghĩa:
- Đồng ý hướng lớn: **borrow mạnh ở orchestration, generation backend, viewer/export primitives**
- Đồng ý phần lõi phải tự build: **Canonical Design State, approval/review gate, lineage, readiness rules**
- Nhưng cần bổ sung vài điểm chưa được nhấn mạnh đủ:
  - rủi ro lớn nhất là **canonicalization gap** giữa generation output và technical truth
  - cần cắm sẵn **data hooks cho Style Intelligence**
  - cần thiết kế sớm **geometry schema** và **derived asset contract**
  - phải coi **reproducibility / audit / testability** là yêu cầu hạng A

---

## 2) Bảng tổng hợp phản biện và ý kiến của tôi

| Nhóm vấn đề | Điểm review | Ý kiến của tôi | Mức đồng ý | Ghi chú chốt |
|---|---|---|---|---|
| Thesis tổng thể | Không có repo nào cover trọn AI Architect end-to-end | Đồng ý mạnh | Rất cao | Dự án này phải là hệ thống ghép nhiều lớp OSS + custom workflow core |
| Product moat | Moat nằm ở workflow/state logic, không nằm ở repo OSS riêng lẻ | Đồng ý mạnh | Rất cao | Đây là luận điểm đúng nhất để định hướng build |
| Canonical Design State | M4 phải tự build, không outsource cho OSS | Đồng ý mạnh | Rất cao | M4 phải giữ version, lineage, approval, derived asset refs, readiness |
| LangGraph | Chỉ nên là orchestration/runtime, không giữ business truth | Đồng ý mạnh | Rất cao | State chuẩn phải nằm ở PostgreSQL/domain layer |
| ComfyUI | Nên dùng qua service boundary, không trộn vào core API | Đồng ý mạnh | Rất cao | Tách GPU service để kiểm soát ops, license, retry, reproducibility |
| ControlNet | Nên coi là capability/model family, không coi repo gốc là runtime trung tâm | Đồng ý mạnh | Rất cao | Tiêu thụ qua ComfyUI workflow hoặc Diffusers abstraction |
| Phase alignment | Research report đúng về end-state nhưng chưa đúng phase build | Đồng ý mạnh | Rất cao | Không bê nguyên report thành implementation backlog |
| IFC / Speckle / That Open / Qdrant | Không nên nằm trên critical path của vòng MVP đầu tiên | Đồng ý phần lớn | Cao | Đúng về phase, nhưng vẫn cần chuẩn bị adapter/schema từ sớm |
| Three.js viewer | Viewer interactive không nên block P0 | Đồng ý phần lớn | Cao | Nhưng phải define contract cho derived assets từ đầu |
| Blender | Hữu ích cho M7 nhưng không nên block first 2D loop | Đồng ý phần lớn | Cao | Xếp vào MVP+ core hợp lý |
| Style Intelligence | M3 là MVP+, chưa cần full stack style-learning ở Phase 1 | Đồng ý phần lớn | Cao | Nhưng phải cắm data hooks từ ngày đầu để không mất dữ liệu học |
| Unstructured | Chỉ nên vào core path nếu attachment thực sự là use case ngay từ đầu | Đồng ý một phần | Trung bình | Nếu brief/portfolio/reference file xuất hiện sớm thì nên đưa vào utility layer sớm |
| Speckle | Chỉ nên pilot, không làm canonical backbone | Đồng ý phần lớn | Cao | Tôi vẫn đánh giá Speckle đáng giá như exchange/collab layer về sau |
| IfcOpenShell | Chưa nên ép canonical state Phase 1 đi theo IFC | Đồng ý phần lớn | Cao | Không cần full IFC sớm, nhưng schema nội bộ phải map được IFC sau này |
| Testing strategy | Review chưa nói đủ về testability của domain logic | Không đồng ý hoàn toàn với mức nhấn mạnh hiện tại | Trung bình | Approval rules, lineage, readiness, permission, fallback phải có test từ đầu |
| Reproducibility / observability | Review có nhắc nhưng chưa nâng lên thành yêu cầu kiến trúc cấp cao | Không đồng ý hoàn toàn với mức nhấn mạnh hiện tại | Trung bình | Cần log model/workflow/prompt/seed/version để giải thích V2 vs V3 |
| Canonicalization gap | Review chưa nhấn mạnh đủ đây là rủi ro kỹ thuật lớn nhất | Không đồng ý với mức nhấn mạnh hiện tại | Cao | Đây là khoảng trống giữa M5 generation và M4 technical truth; nếu không giải quyết được thì sản phẩm sẽ chỉ là AI concept tool |

---

## 3) Bảng rất thực dụng để chốt backlog

| Điểm review | Tôi đồng ý mức nào | Ảnh hưởng tới backlog | Quyết định chốt |
|---|---|---|---|
| Không có repo nào cover trọn AI Architect end-to-end | 95% | Tránh tìm “silver bullet repo”, backlog phải chia theo capability layer | Chốt: kiến trúc ghép nhiều OSS + custom core |
| Canonical Design State phải tự build | 100% | Ưu tiên rất cao cho domain model, versioning, lineage, approval state | Chốt: M4 là custom core, không outsource |
| LangGraph chỉ dùng cho orchestration | 95% | Không nhét project/version/approval truth vào graph runtime | Chốt: dùng LangGraph cho P2/P4, truth nằm ở DB/domain service |
| ComfyUI qua service boundary | 95% | Tách GPU service, tách deploy/ops/retry/versioning khỏi core API | Chốt: `ai-architect-gpu` là service riêng |
| ControlNet chỉ là capability, không phải core runtime repo | 95% | Thiết kế abstraction cho conditioning, tránh lock vào repo gốc | Chốt: dùng qua ComfyUI/Diffusers workflow |
| IFC / That Open / Speckle / Qdrant không vào critical path P0 | 85% | Giảm scope Sprint 1–6, tập trung vào loop intake → 2D → review → PDF/SVG | Chốt: defer khỏi critical path, chỉ chuẩn bị interface/adapters |
| Three.js interactive viewer chưa phải blocker P0 | 85% | Không để frontend 3D làm chậm release đầu | Chốt: P0 dùng static renders; chuẩn bị asset contract để P1 thêm viewer |
| Blender không block vòng 2D đầu tiên | 85% | M7 không được làm chậm M5+M6 | Chốt: Blender vào MVP+ core |
| M3 Style Intelligence là MVP+ | 85% | Chưa cần Qdrant/FiftyOne full stack ngay | Chốt: defer full M3, nhưng log dữ liệu approve/reject/reference từ ngày đầu |
| Unstructured chỉ đưa vào khi attachment là use case thật | 70% | Tránh ETL phình sớm, nhưng vẫn nên để ngỏ utility layer | Chốt: optional early utility; chỉ kéo vào Sprint đầu nếu intake có PDF/DOC/portfolio |
| Speckle chỉ pilot, không làm canonical backbone | 85% | Không phụ thuộc data-hub ngoài cho truth nội bộ | Chốt: pilot later cho exchange/collab, không làm backbone |
| IfcOpenShell chưa nên dẫn dắt canonical model Phase 1 | 80% | Không ép Phase 1 đi theo IFC semantics đầy đủ | Chốt: chưa integrate full, nhưng canonical geometry schema phải map được DXF/IFC sau này |
| Review này chủ yếu đúng về scope control | 90% | Nên dùng review này để re-baseline implementation backlog | Chốt: dùng làm tài liệu điều chỉnh phase/build order |
| Review chưa nhấn mạnh đủ canonicalization gap | 90% | Backlog phải có riêng workstream “image/output -> structured state” | Chốt: thêm epic cho canonicalization pipeline ngay từ Phase 1 |
| Review chưa nhấn mạnh đủ testability | 90% | Phải có test plan cho state machine, readiness, permission, lineage, fallback | Chốt: thêm test harness/domain tests vào foundation phase |
| Review chưa nhấn mạnh đủ reproducibility / audit | 90% | Cần log workflow/model/prompt/seed/version ngay từ đầu | Chốt: thêm audit + run metadata vào mọi generation/export/revision job |

---

## 4) Các quyết định chốt tôi đề xuất đưa thẳng vào roadmap

### 4.1 Chốt cho Phase 1 core
- `FastAPI + PostgreSQL + Object Storage + Redis/Queue`
- `LangGraph` cho orchestration
- `ComfyUI` GPU service
- `ControlNet` qua workflow abstraction
- `Fabric.js` cho annotate/review 2D
- `Canonical Design State` custom
- `PDF + SVG export` custom

### 4.2 Chốt các thứ phải “defer nhưng chuẩn bị interface”
- `IfcOpenShell`
- `That Open`
- `three.js interactive viewer`
- `Blender headless`
- `Qdrant`
- `Speckle`

### 4.3 Chốt các việc nền phải làm ngay dù feature chưa mở
- Thiết kế **geometry schema** đủ mở để map DXF/IFC sau này
- Thiết kế **derived asset contract** cho render / model / viewer
- Log **approve/reject/reference/annotation** để nuôi M3 sau này
- Gắn **reproducibility metadata** cho mọi generation job
- Viết **domain tests** cho state machine, permission, readiness, lineage

---

## 5) Một câu chốt cuối

Review này **đúng hướng hơn research report nếu mục tiêu là ra backlog build thực dụng cho Phase 1**.  
Nhưng để dự án không bị hụt chân về sau, cần bổ sung mạnh 4 thứ vào quyết định chốt:

1. **Canonicalization pipeline**
2. **Geometry schema forward-compatible**
3. **Data hooks cho Style Intelligence**
4. **Reproducibility / audit / testability**
