# Phase 1 – Đánh Giá Proposal OSS Cho AI Architect

*Ngày đánh giá: Apr 11, 2026*  
*Đầu vào: `05-system-design.md`, `AI_Architect_OSS_Research_Report.docx`, GitHub/official docs checked on Apr 11, 2026*

---

## 1. Kết luận ngắn

Proposal trong `AI_Architect_OSS_Research_Report.docx` là **đúng hướng về end-state architecture**, nhưng **chưa fit hoàn toàn với Phase 1 MVP** theo chính `05-system-design.md`.

Tôi chốt ở mức:

**Accept with recalibration**

Nghĩa là:

- giữ nguyên thesis lớn: **borrow mạnh ở orchestration, generation backend, viewer primitives, export IO**
- giữ nguyên quyết định: **canonical state, approval/review gate, lineage, readiness rules phải tự build**
- nhưng phải **hạ scope của một số repo khỏi critical path của Phase 1**

Điểm tôi đồng ý mạnh:

- Không có repo nào cover trọn `AI Architect Agentic OS`.
- `Canonical Design State` không nên bị outsourced cho repo bên ngoài.
- Dùng `ComfyUI`/GPU service qua service boundary là hợp lý.
- Không nên tự viết viewer, annotation, IFC IO từ số 0.

Điểm tôi không đồng ý nếu đem vào implementation backlog ngay:

- Report đang kéo vài thành phần của `MVP+` và `Phase 2` vào nhóm gần như `adopt now`.
- `LangGraph` nên là **agent runtime**, không phải nơi giữ business truth.
- `ControlNet` nên được xem là **capability/model family**, không nên coi repo gốc là runtime dependency trung tâm.
- `IFC`, `Speckle`, `That Open`, `Qdrant`, `FiftyOne`, `FreeCAD`, `DXF` không nên nằm trên critical path của vòng `intake -> first 2D options -> review -> PDF/SVG`.

---

## 2. Đối chiếu với `05-system-design.md`

### 2.1 Những điểm report đang khớp

- `M4 Canonical Design State` là lõi kiến trúc và phải tự build.
- `M6 Review/Approval` gắn chặt với business logic và không có OSS nào thay thế trọn.
- `M5 2D Generation` nên borrow backend generation thay vì tự build toàn bộ pipeline diffusion.
- `M1` nên borrow viewer/annotation primitives.

### 2.2 Những điểm report đang lệch phase

- `Q1` trong system design chốt `M3 Style Intelligence` là `MVP+`.
  - Vì vậy `Qdrant`, `FiftyOne`, phần lớn stack style-learning không phải core của Phase 1 MVP.
- `Q2` chốt Phase 1 chỉ cần `preview image + basic metadata JSON`.
  - Vì vậy `IfcOpenShell`, `engine_web-ifc`, `Speckle` không nên dẫn dắt canonical model sớm.
- `Q3` chốt `DXF` là `Phase 2`.
  - Vì vậy `ezdxf` chưa phải dependency bắt buộc của Phase 1.
- `Q4` chốt `3D viewer` là `P1`, còn `static renders` mới là `P0`.
  - Vì vậy `three.js` và `That Open` là hướng đúng, nhưng không nên block vòng MVP đầu tiên.
- `Q5` chốt `handoff_ready` là checklist code custom.
  - Điều này càng củng cố rằng workflow core và release gate phải nằm trong codebase riêng.

Kết luận phần này:

**Report phù hợp với end-state system design hơn là với implementation priority matrix của Phase 1.**

---

## 3. Điều chỉnh classification so với report

Những thay đổi tôi đề xuất:

- `LangGraph`: giữ `adopt`, nhưng chỉ cho orchestration. State chuẩn phải ở `PostgreSQL`.
- `ComfyUI`: giữ `adopt now`, nhưng bắt buộc chạy sau service boundary vì license/ops.
- `ControlNet`: giữ `adopt` ở mức capability, không ghim repo gốc làm runtime chính.
- `IfcOpenShell`: đổi từ `adopt now` sang `prepare adapter now, integrate when IFC/export thật sự cần`.
- `That Open engine_web-ifc` và `engine_components`: đổi từ gần-core sang `MVP+/P1`.
- `three.js`: giữ `adopt`, nhưng viewer interactive không phải blocker của P0.
- `Blender`: nên coi là `MVP+ core`, không phải blocker cho first 2D loop.
- `Qdrant`: đổi từ `adopt now` sang `MVP+`.
- `ezdxf`: đổi từ `adopt now` sang `Phase 2`.
- `Unstructured`: chỉ nên vào core path nếu thật sự hỗ trợ attachment/portfolio import ngay từ đầu.
- `PydanticAI` + `Guardrails`: giữ `pilot`, không nên dùng đồng thời quá sớm nếu chưa chứng minh failure mode.
- `Speckle`: giữ `pilot`, tuyệt đối không để định nghĩa canonical truth.

---

## 4. Review từng repo

### 4.1 Nên dùng cho Phase 1 core

| Repo | Ưu điểm chính | Nhược điểm / rủi ro | Đánh giá của tôi |
|---|---|---|---|
| `langchain-ai/langgraph` | Stateful graph orchestration, streaming, HITL, resume tốt cho intake/revision loop | Dễ bị lạm dụng thành nơi giữ business state; graph logic có thể phình nhanh và khó test nếu nhét quá nhiều domain rule | **Nên dùng** cho query loop và agent orchestration, nhưng `project/version/approval state` phải nằm ở DB riêng |
| `Comfy-Org/ComfyUI` | Mạnh nhất hiện tại cho workflow diffusion dạng graph, ecosystem node lớn, hợp GPU service | GPL-3.0, ops nặng, reproducibility giữa workflow/model version phải quản lý rất chặt | **Nên dùng** qua GPU service tách biệt; không embed vào core API |
| `lllyasviel/ControlNet` | Conditioning tốt cho sketch/edge/depth, giúp output bám intent hơn text-only diffusion | Repo gốc không còn là runtime production tốt nhất; maintenance signal của repo gốc không còn mạnh như narrative trong report | **Nên dùng capability**, nhưng nên tiêu thụ qua `ComfyUI` hoặc `diffusers`, không nên phụ thuộc trực tiếp repo gốc |
| `fabricjs/fabric.js` | Thực dụng cho canvas annotation, overlay, selection, pin/comment trên floor plan/render | Quản lý state canvas riêng; có thể vướng performance nếu canvas và object count lớn | **Nên dùng** cho lớp annotate/review 2D ở Phase 1 |

### 4.2 Đúng hướng nhưng không nên là blocker của Phase 1 MVP

| Repo | Ưu điểm chính | Nhược điểm / rủi ro | Đánh giá của tôi |
|---|---|---|---|
| `mrdoob/three.js` | Nền 3D web mature, linh hoạt, không khóa vào BIM stack cụ thể | Nếu kéo viewer interactive vào quá sớm sẽ làm nở scope frontend | **Nên chuẩn bị sẵn**, nhưng viewer interactive chỉ cần từ `P1/MVP+` |
| `Unstructured-IO/unstructured` | Giảm effort parse PDF/DOC/attachment, hữu ích cho intake files và portfolio docs | Thêm pipeline ETL sớm có thể làm lệch trọng tâm nếu MVP đầu chỉ nhập text/form | **Nên dùng có chọn lọc**; core nếu attachment là use case thật, còn không thì để sau |
| `IfcOpenShell/IfcOpenShell` | Strong nhất về IFC parse/convert/openBIM IO, rất có giá trị cho export/interoperability | IFC quá nặng nếu canonical Phase 1 mới chỉ là `image + metadata JSON`; không thay được internal truth | **Nên chuẩn bị adapter**, nhưng không nên ép canonical state Phase 1 đi theo IFC |
| `ThatOpen/engine_web-ifc` | Đọc/ghi IFC trong browser/Node rất nhanh, hợp web BIM tooling | Giá trị lớn nhất khi đã có IFC-driven workflow; Phase 1 chưa cần khóa chặt vào IFC | **Nên để P1/MVP+**, không phải core blocker |
| `ThatOpen/engine_components` | Có sẵn navigation, measurement, floor plan tooling, tiết kiệm công viewer AEC | Frontend sẽ mang hơi hướng BIM sớm hơn nhu cầu MVP; giá trị thấp nếu chưa có IFC/viewer rõ ràng | **Hợp cho viewer giai đoạn sau**, chưa cần trên critical path |
| `blender/blender` | Mạnh cho scene assembly, render, GLTF/export, automation headless | GPL, script automation có thể giòn, GPU/render ops phức tạp | **Rất hữu ích cho M7**, nhưng nên coi là `MVP+ core`, không block vòng 2D đầu tiên |
| `mozman/ezdxf` | Thực dụng cho DXF programmatic export | `DXF` đã được system design đẩy sang `Phase 2`; đưa vào sớm sẽ kéo geometry model lên quá nhanh | **Để Phase 2** |

### 4.3 Nên pilot, không nên commit sớm vào xương sống hệ thống

| Repo | Ưu điểm chính | Nhược điểm / rủi ro | Đánh giá của tôi |
|---|---|---|---|
| `specklesystems/speckle-server` | AEC data hub, versioned sharing, viewer, webhook, connectors | License mixed; có module enterprise riêng; dễ kéo sản phẩm đi theo data-hub model thay vì canonical state riêng | **Pilot only**; không nên là canonical backbone |
| `pydantic/pydantic-ai` | Schema-first agent pattern tốt, typed outputs rõ hơn | Chồng thêm một agent abstraction lên trên `LangGraph` có thể làm stack khó hiểu | **Pilot**; chỉ dùng nếu team thật sự cần typed agent nodes hơn mức Pydantic validation thuần |
| `guardrails-ai/guardrails` | Có value ở validation/re-ask/constraint enforcement | Dễ tăng complexity prompt/validator; overlap với retry + schema validation custom | **Pilot**; không nên bật full stack guardrails quá sớm |
| `voxel51/fiftyone` | Tốt cho internal dataset QA, inspect embedding/image clusters | Không phải end-user product capability; thêm infra/ops | **Pilot internal ops**, không phải production core |
| `FreeCAD/FreeCAD` | Có ích nếu cần kỹ thuật hóa geometry/CAD open-source sâu hơn | Automation friction cao, desktop-heavy, không hợp làm core service sớm | **Pilot** khi thật sự cần CAD bridge |
| `cvat-ai/cvat` | Rất mạnh cho annotation ops nội bộ | Không phù hợp làm customer-facing review UX | **Internal ops only** |
| `HumanSignal/label-studio` | Tốt cho labeling/QA nội bộ đa loại dữ liệu | Cũng không phải UX review cuối cho KTS/client | **Internal ops only** |

### 4.4 Chỉ nên tham khảo hoặc tránh làm roadmap anchor

| Repo | Ưu điểm chính | Nhược điểm / rủi ro | Đánh giá của tôi |
|---|---|---|---|
| `ennauata/houseganpp` | Có giá trị như research seed cho layout generation | License có ghi rõ chỉ dùng cho research; không phù hợp làm production dependency | **Reference only**, không nên đưa vào product plan thương mại |
| `ywyue/RoomFormer` | Hữu ích cho floorplan reconstruction/structured polygon understanding | Không giải trực tiếp bài toán end-to-end generation cho sản phẩm | **Reference only** |
| `ChatHouseDiffusion/chathousediffusion` | Ý tưởng text-to-floor-plan thú vị | Repo nhỏ, tín hiệu maturity còn sớm | **Reference only** |
| `opensourceBIM/BIMserver` | Có ý tưởng tốt về IFC database/versioning | AGPL-3.0, Java stack cũ hơn, friction sản phẩm cao | **Không nên làm backbone**; chỉ nghiên cứu ý tưởng |
| `LibreCAD/LibreCAD` | Có thể làm desktop validator/fallback converter | GPLv2, desktop-centric, không giải core workflow | **Fallback/reference only** |

### 4.5 MCP / external bridge được nêu trong report

| Tool / repo | Ưu điểm chính | Nhược điểm / rủi ro | Đánh giá của tôi |
|---|---|---|---|
| `Figma Dev Mode MCP` | Hữu ích cho workflow UI/dev handoff | Không giúp giải canonical geometry/BIM/CAD | **Đúng nhưng ngoài core bài toán** |
| `Autodesk MCP Servers` | Official signal rất mạnh từ Autodesk; đáng theo dõi cho Revit/model data/help | Tài liệu chính thức vẫn nhấn mạnh trạng thái `coming soon`/beta ở nhiều server | **Track closely**, chưa nên neo roadmap MVP vào đây |
| `Gorav22/Blender-mcp` | Chứng minh bridge Blender qua MCP là khả thi | Repo rất sớm, quy mô nhỏ, rủi ro bảo mật/ops nếu mở rộng | **Sandbox only** |
| `mcp-servers-for-revit/revit-mcp` | Cho thấy hướng Revit automation qua MCP | Repo đã archived; ecosystem còn phân mảnh | **Không nên phụ thuộc** |
| `gNucleus/text-to-cad-mcp` | Mẫu tham khảo hay cho third-party CAD bridge | Scope nghiêng về CAD hơn là workflow thiết kế nhà ở có review/canonical/handoff | **Reference only** |

---

## 5. Stack tôi khuyến nghị theo phase

### 5.1 Phase 1 MVP thật sự nên khóa ở đây

- `FastAPI + PostgreSQL + object storage + Redis/queue`
- `LangGraph` cho orchestration của intake/query loop
- `ComfyUI` GPU service + `ControlNet` capability qua workflow
- `Fabric.js` cho annotation/review 2D
- `PDF + SVG export` custom
- `Canonical state` custom với `preview image + basic metadata JSON`

Lưu ý:

- Nếu chưa có use case attachment nặng, có thể **chưa cần kéo `Unstructured` vào Sprint 1-2**.
- `three.js` có thể chuẩn bị interface từ sớm nhưng không nên block release đầu.

### 5.2 MVP+ / giai đoạn ngay sau khi core loop chạy ổn

- `three.js`
- `Blender headless`
- `IfcOpenShell`
- `That Open engine_web-ifc`
- `That Open engine_components`
- `Qdrant`

### 5.3 Chỉ pilot khi đã có tín hiệu nhu cầu rõ

- `Speckle Server`
- `PydanticAI`
- `Guardrails`
- `FiftyOne`
- `FreeCAD`
- `CVAT`
- `Label Studio`

### 5.4 Chỉ giữ làm research/reference

- `House-GAN++`
- `RoomFormer`
- `ChatHouseDiffusion`
- `BIMserver`
- `LibreCAD`
- community MCP repos cho Blender/Revit/CAD

---

## 6. Các nhận xét quan trọng nhất

1. Thesis của report là đúng: **moat của sản phẩm nằm ở state logic và workflow logic, không nằm ở repo OSS riêng lẻ.**
2. Sai lệch lớn nhất của report không phải ở việc chọn sai repo, mà ở việc **xếp sai thời điểm dùng repo**.
3. `LangGraph` + `ComfyUI` là hai lựa chọn hợp lý nhất để tiết kiệm effort ngay, nhưng cả hai đều phải bị đặt sau boundary rõ ràng:
   - `LangGraph` không được giữ truth
   - `ComfyUI` không được lẫn vào core API service
4. `IfcOpenShell`, `That Open`, `Blender`, `Qdrant` đều có giá trị thật, nhưng là giá trị **sau khi core loop intake -> 2D -> review -> PDF/SVG đã chạy ổn**.
5. `Speckle` đáng pilot, nhưng chỉ khi có nhu cầu collaboration/data exchange thật sự. Nếu không, nó sẽ thêm complexity sớm.

---

## 7. Verdict cuối cùng

Nếu mục tiêu là ra quyết định build thực dụng ngay bây giờ, tôi chốt như sau:

- **Chấp nhận research report làm tài liệu tham chiếu chiến lược**
- **Không dùng nguyên classification của report để làm backlog implementation**
- **Re-baseline Phase 1** quanh một core stack nhỏ hơn:
  - `LangGraph`
  - `ComfyUI`
  - `ControlNet` qua workflow
  - `Fabric.js`
  - `FastAPI + PostgreSQL + object storage`
  - custom `Canonical Design State`

Mọi thứ còn lại nên được gắn nhãn rõ là:

- `defer to MVP+`
- `pilot only`
- hoặc `reference only`

Đó là cách giữ đúng kiến trúc đã chốt mà vẫn tránh over-engineering trong Phase 1.
