---
Document: Third-Party GitHub Research Context
Status: Draft
Last updated: Apr 11, 2026
Owner:
---

# AI Architect – Context Chuẩn Cho Bên Thứ 3 Research GitHub Repos

## 1. Mục đích tài liệu

Tài liệu này dùng để handoff cho một bên thứ 3 chuyên đi research GitHub repositories có thể tận dụng cho AI Architect, với mục tiêu:

- giảm khối lượng phải tự build từ đầu
- tìm đúng repo có thể tái sử dụng cho từng phần của kiến trúc
- đánh giá repo nào nên `adopt`, repo nào nên `wrap`, repo nào chỉ nên `tham khảo`
- bám theo thiết kế hệ thống mới nhất, không research rời rạc theo cảm tính

Tài liệu này không yêu cầu bên research đề xuất kiến trúc mới từ đầu.  
Mục tiêu là research **để phục vụ kiến trúc đã chốt**.

---

## 2. Quyết định đã chốt

Đây là các nguyên tắc đã được quyết định. Bên research phải coi đây là ràng buộc đầu vào, không tranh luận lại từ đầu.

### 2.1 Về phạm vi implementation

- Chúng tôi muốn **implement toàn bộ hệ thống theo end-state một lần**, không chia theo phase rollout để thiết kế lại nhiều lần.
- Vẫn có thể có thứ tự build nội bộ, nhưng research phải nhìn theo **kiến trúc hoàn chỉnh**, không chỉ theo MVP rút gọn.

### 2.2 Về bản chất sản phẩm

AI Architect không phải một app gọi AI rồi hiện ảnh.  
Nó là một **Agentic OS cho workflow thiết kế nhà ở**, có:

- intake và brief chuẩn hóa
- generation 2D nhanh
- canonical design state
- review gate của KTS
- derivation 3D
- standards export
- delivery/handoff
- style intelligence cho từng KTS

### 2.3 Về nguyên tắc hệ thống

- End user phải thấy **demo 2D nhanh nhất**.
- KTS phải làm việc trên **file chuẩn / canonical state**, không làm việc trực tiếp trên ảnh đẹp.
- 3D là lớp **dẫn xuất từ bản 2D đã khóa**, không phải nguồn sự thật.
- Mục tiêu cuối là ra **bộ file chuẩn** để user, KTS và nhà thầu có thể chốt và triển khai.
- Hệ thống phải học được **phong cách riêng của từng KTS** từ thư viện thiết kế họ import trước đó.

### 2.4 Về canonical truth

Mọi module trong hệ thống phải quay về cùng một `Canonical Design State`.

Điều đó có nghĩa là:

- 2D option sau khi được chọn sẽ được khóa thành canonical version
- 3D, render, export, handoff đều phải tham chiếu tới canonical version đó
- hệ thống phải tránh việc cùng một yêu cầu mà mỗi lần generate lại trôi sang một hướng khác

---

## 3. Tài liệu nguồn cần đọc trước khi research

Bên research phải đọc ít nhất các file này trước khi bắt đầu:

- [README.md](/Users/nguyenquocthong/Documents/New%20project/ai-architect-mvp/README.md)
- [docs/phase-1/00-mvp-overview.md](/Users/nguyenquocthong/Documents/New%20project/ai-architect-mvp/docs/phase-1/00-mvp-overview.md)
- [docs/phase-1/02-tech-repos.md](/Users/nguyenquocthong/Documents/New%20project/ai-architect-mvp/docs/phase-1/02-tech-repos.md)
- [docs/phase-1/03-agentic-os-architecture.md](/Users/nguyenquocthong/Documents/New%20project/ai-architect-mvp/docs/phase-1/03-agentic-os-architecture.md)
- [docs/phase-1/04-module-business-requirements.md](/Users/nguyenquocthong/Documents/New%20project/ai-architect-mvp/docs/phase-1/04-module-business-requirements.md)
- [docs/phase-1/05-system-design.md](/Users/nguyenquocthong/Documents/New%20project/ai-architect-mvp/docs/phase-1/05-system-design.md)
- [deep-research-report (1).md](/Users/nguyenquocthong/Documents/New%20project/ai-architect-mvp/deep-research-report%20%281%29.md)
- [research-github-updated.md](/Users/nguyenquocthong/Documents/New%20project/ai-architect-mvp/research-github-updated.md)

---

## 4. Kiến trúc hệ thống – Bản tóm tắt để research

### 4.1 9 business modules

| ID | Module | Mục đích |
| --- | --- | --- |
| M1 | Experience Layer | Workspace cho end user, KTS, admin, contractor |
| M2 | Intake & Brief Module | Chuẩn hóa requirement thành brief có cấu trúc |
| M3 | Architect Style Intelligence | Học phong cách đặc trưng của từng KTS |
| M4 | Canonical Design State | Nguồn sự thật kỹ thuật cho từng version đã khóa |
| M5 | 2D Generation Engine | Tạo option 2D nhanh |
| M6 | Review & Annotation Module | Review, annotate, approve/reject |
| M7 | 3D Derivation & Visual Generation | Dẫn xuất 3D và render từ canonical 2D |
| M8 | Standards Export Module | SVG, DXF, PDF, về sau là IFC |
| M9 | Delivery & Handoff Module | Đóng gói bundle và bàn giao |

### 4.2 6 Agentic OS pipelines

| Pipeline | Vai trò |
| --- | --- |
| P1 | Client UI |
| P2 | Query Loop |
| P3 | Tool Orchestration |
| P4 | Multi-Agent Coordination |
| P5 | Context Management |
| P6 | Permission & Security |

### 4.3 Các use case hệ thống quan trọng

Bên research phải ưu tiên fit repo theo đúng các use case này:

1. Intake → first 2D options
2. KTS review → approve → lock thành canonical version
3. 3D derivation từ canonical version
4. Client feedback → revision loop
5. Style Intelligence: import → learn → apply
6. Export & delivery
7. Escalating recovery khi generation fail
8. Context defense khi design session dài

---

## 5. Nhiệm vụ research theo từng module

Mỗi module dưới đây cần được research theo hướng:

- có repo nào có thể dùng trực tiếp?
- có repo nào chỉ phù hợp để wrap như service?
- có repo nào chỉ nên dùng làm reference implementation?
- module nào buộc phải tự build phần lõi?

### M1. Experience Layer

**Cần research:**

- repo/workbench cho review workspace, annotation layer, asset gallery
- web viewer có measurement / floor-plan navigation / BIM-style navigation
- compare view / review dashboard patterns

**Câu hỏi cần trả lời:**

- Có repo nào giúp giảm công build review workspace và annotation không?
- Có repo nào phục vụ 3D viewer / floorplan view / measurement tốt cho AEC?
- Repo nào đủ tốt cho frontend production, repo nào chỉ là demo?

### M2. Intake & Brief Module

**Cần research:**

- conversational intake frameworks
- structured extraction / form-to-schema / JSON extraction
- multi-turn requirement clarification patterns

**Câu hỏi cần trả lời:**

- Repo nào phù hợp cho intake + clarification flow?
- Repo nào có stateful agent/workflow đủ tốt để điều phối hỏi-đáp cho brief?
- Có repo nào giúp parse requirement thành schema ổn định không?

### M3. Architect Style Intelligence

**Cần research:**

- repo cho document/image ingestion
- repo cho style embedding, retrieval, similarity, tagging
- repo cho pattern extraction từ image/render/bản vẽ
- repo cho portfolio indexing và retrieval

**Câu hỏi cần trả lời:**

- Có repo nào có thể giúp ingest portfolio của KTS không?
- Có repo nào học style từ ảnh/render/reference một cách thực dụng?
- Có repo nào đủ tốt cho retrieval + style conditioning thay vì fine-tune nặng?
- Module này nên build bao nhiêu phần lõi, tận dụng bao nhiêu phần từ OSS?

### M4. Canonical Design State

**Cần research:**

- repo / library cho geometry schema, CAD/BIM-ish intermediate representation
- repo giúp quản lý versioned design state
- repo cho compare/diff geometry hoặc design states

**Câu hỏi cần trả lời:**

- Có repo nào đáng dùng làm nền cho canonical geometry / room graph không?
- Có repo nào hỗ trợ design versioning / traceability tốt không?
- Phần lõi canonical state có bắt buộc phải tự build hoàn toàn không?

### M5. 2D Generation Engine

**Cần research:**

- floor plan generation
- text/sketch-conditioned generation
- image-to-structure / vectorization / floor plan parsing
- reproducible generation pipelines

**Câu hỏi cần trả lời:**

- Repo nào tạo 2D option nhanh nhất có thể dùng được?
- Repo nào tạo được output có cấu trúc hoặc có khả năng canonicalize tốt?
- Repo nào phù hợp để chạy như generation service production?

### M6. Review & Annotation Module

**Cần research:**

- annotation frameworks cho image / canvas / floor plan
- review workflows / approval state machine patterns
- collaborative comments / threaded review

**Câu hỏi cần trả lời:**

- Có repo nào đáng tận dụng cho annotation layer?
- Có repo nào đã có review queue / approval pattern tương tự?
- Phần nào nên tự build vì liên quan chặt đến canonical version?

### M7. 3D Derivation & Visual Generation

**Cần research:**

- 2D → 3D derivation
- floor plan to Blender / GLTF / scene graph
- 3D render pipelines conditioned by plan/geometry/style

**Câu hỏi cần trả lời:**

- Repo nào đáng dùng cho 2D → 3D?
- Repo nào chỉ dùng được cho demo, repo nào có thể đi xa hơn?
- Làm sao giữ consistency giữa canonical 2D và 3D output bằng OSS?

### M8. Standards Export Module

**Cần research:**

- SVG / DXF export
- IFC generation / read-write
- BIM conversion / geometry export

**Câu hỏi cần trả lời:**

- Repo nào đáng dùng cho DXF?
- Repo nào đáng dùng cho IFC/BIM?
- Khi nào nên export từ geometry JSON, khi nào nên export từ model?

### M9. Delivery & Handoff Module

**Cần research:**

- document bundling
- package manifests
- audit trail / delivery records
- artifact packaging

**Câu hỏi cần trả lời:**

- Có repo nào phục vụ delivery package / signed bundle / audit manifest không?
- Phần này nên tận dụng object storage + metadata tự build, hay có OSS đáng dùng?

---

## 6. Những phần ưu tiên research cao nhất

Nếu nguồn lực research có hạn, ưu tiên theo thứ tự này:

1. `M5` 2D Generation Engine
2. `M4` Canonical Design State
3. `M7` 3D Derivation & Visual Generation
4. `M8` Standards Export
5. `M3` Architect Style Intelligence
6. `M6` Review & Annotation
7. `M1` Experience Layer
8. `M2` Intake & Brief
9. `M9` Delivery & Handoff

Lý do:

- `M5 + M4 + M7 + M8` là lõi tạo giá trị và lõi rủi ro kỹ thuật
- `M3` là lợi thế cạnh tranh
- các module còn lại quan trọng nhưng dễ tự build hơn hoặc có nhiều pattern phổ biến hơn

---

## 7. Tiêu chí đánh giá mỗi GitHub repo

Bên research không chỉ liệt kê repo.  
Mỗi repo phải được đánh giá theo cùng một framework.

### 7.1 Thông tin bắt buộc cho mỗi repo

| Trường | Mô tả |
| --- | --- |
| Repo name | Tên repo |
| URL | Link GitHub |
| Module fit | Phục vụ module nào |
| Use case fit | Gắn với use case nào |
| Core capability | Năng lực chính |
| License | MIT / Apache / GPL / AGPL / MPL / khác |
| Maintenance signal | commit/release/activity gần đây |
| Stars / adoption | mức phổ biến |
| Production fit | demo / prototype / production candidate |
| Integration mode | adopt / wrap / reference / avoid |
| Key risks | license, quality, lock-in, missing feature |

### 7.2 Cách chấm mức độ fit

Mỗi repo nên được chấm theo 5 chiều, thang 1-5:

- `Functional fit`
- `Integration complexity`
- `Production readiness`
- `License safety`
- `Long-term maintainability`

Kèm kết luận:

- `Adopt now`
- `Pilot`
- `Use as reference only`
- `Do not use`

---

## 8. Câu hỏi research bắt buộc phải trả lời

Báo cáo của bên thứ 3 phải trả lời tối thiểu các câu hỏi sau:

1. Module nào có thể tận dụng OSS mạnh nhất?
2. Module nào bắt buộc phải tự build phần lõi?
3. Có repo nào đủ tốt để làm nền cho `Canonical Design State` không?
4. Có tổ hợp repo nào tạo được flow `2D fast -> canonicalize -> 3D derive -> export` không?
5. Có repo nào thực dụng cho `Architect Style Intelligence`, hay module này phải custom nhiều?
6. Có rủi ro license nào khiến một số repo không phù hợp với commercial product không?
7. Nếu phải chốt 1 stack OSS khả dụng nhất để giảm effort dev, stack đó là gì?

---

## 9. Kỳ vọng đầu ra từ bên research

Đầu ra mong muốn không phải một file note dài liệt kê lung tung.  
Đầu ra mong muốn là một tài liệu có cấu trúc như sau:

### Phần A – Executive Summary

- Top 10 repo đáng chú ý nhất
- 3 repo/stack nên adopt ngay
- 3 phần lõi vẫn phải tự build
- rủi ro lớn nhất

### Phần B – Module-by-module Recommendations

Với từng module `M1..M9`:

- shortlist repo
- repo đề xuất nhất
- vì sao fit
- vì sao chưa fit
- kết luận adopt / wrap / reference / avoid

### Phần C – Suggested OSS Stack

Một stack end-to-end khả thi nhất cho AI Architect dựa trên kiến trúc hiện tại.

Ví dụ kiểu:

- intake / orchestration
- 2D generation
- canonical state support
- style intelligence support
- 3D derivation
- export / BIM
- review / viewer

### Phần D – Gaps

Những phần không có repo OSS đủ tốt và nên tự build.

---

## 10. Điều không nên làm trong research

- Không chỉ liệt kê repo theo từ khóa.
- Không đề xuất repo chỉ vì nhiều stars nhưng không map được vào use case thực.
- Không bỏ qua license.
- Không đề xuất lại kiến trúc mới hoàn toàn nếu chưa chứng minh kiến trúc hiện tại không khả thi.
- Không chỉ nhìn từng repo riêng lẻ; phải nhìn khả năng ghép thành flow hệ thống.

---

## 11. One-line brief để gửi bên research

Nếu cần gửi rất ngắn gọn, dùng đoạn này:

> Chúng tôi đang thiết kế một hệ thống AI Architect theo mô hình Agentic OS, có 9 business modules và 6 pipelines kỹ thuật. Mục tiêu là tìm các GitHub repos có thể tận dụng cho từng phần của hệ thống, đặc biệt là 2D generation, canonical design state, architect style intelligence, 3D derivation và standards export, để giảm effort tự build toàn bộ mà vẫn bám đúng kiến trúc đã chốt.

---

## 12. Kết luận

Tài liệu này tồn tại để đảm bảo bên thứ 3 research đúng bài toán:

- research theo **kiến trúc đã chốt**
- research theo **module và use case**
- research để trả lời câu hỏi **cái gì tận dụng được, cái gì vẫn phải tự build**

Không phải để họ làm một vòng discovery mới từ đầu.
