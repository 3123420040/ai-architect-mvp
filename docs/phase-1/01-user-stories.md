# Phase 1 – User Stories Chi Tiết

*Ngày tạo: Apr 11, 2026*

---

## Quy ước

- **Priority:** P0 = Must have, P1 = Should have, P2 = Nice to have
- **Size:** S = 1-2 ngày, M = 3-5 ngày, L = 1-2 tuần
- **Format:** Given/When/Then cho Acceptance Criteria (AC)

---

## Epic 1: User Onboarding & Authentication

### US-1.1: Đăng ký tài khoản công ty thiết kế [P0, S]

**As a** quản lý công ty thiết kế,
**I want to** đăng ký tài khoản cho công ty trên platform,
**So that** team của tôi có thể sử dụng AI để tạo concept design.

**Acceptance Criteria:**
- [ ] **AC1:** Given user ở trang đăng ký, When nhập email công ty + password + tên công ty + số điện thoại, Then tài khoản được tạo và nhận email xác nhận.
- [ ] **AC2:** Given user đã đăng ký, When click link xác nhận email, Then tài khoản được activate.
- [ ] **AC3:** Given email đã tồn tại, When thử đăng ký lại, Then hiển thị lỗi "Email đã được sử dụng".

**Notes:** Phase 1 dùng email/password. OAuth (Google) ở Phase 2.

---

### US-1.2: Đăng nhập hệ thống [P0, S]

**As a** user đã có tài khoản,
**I want to** đăng nhập vào hệ thống,
**So that** tôi có thể truy cập các dự án thiết kế.

**Acceptance Criteria:**
- [ ] **AC1:** Given user ở trang login, When nhập đúng email/password, Then redirect vào dashboard.
- [ ] **AC2:** Given user nhập sai password 5 lần, When thử lần thứ 6, Then tài khoản bị lock 15 phút.
- [ ] **AC3:** Given user đã đăng nhập, When refresh trang, Then vẫn giữ session (JWT token).

---

### US-1.3: Quản lý thành viên team [P1, M]

**As a** quản lý công ty thiết kế,
**I want to** mời thành viên vào team và phân quyền,
**So that** KTS trong team có thể review và chỉnh sửa design.

**Acceptance Criteria:**
- [ ] **AC1:** Given user là admin, When nhập email thành viên mới + chọn role (admin/architect/viewer), Then gửi email mời.
- [ ] **AC2:** Given thành viên nhận email mời, When click link accept, Then được thêm vào team với role tương ứng.
- [ ] **AC3:** Given user là admin, When thay đổi role của thành viên, Then quyền truy cập được cập nhật ngay lập tức.

**Roles:**
- **Admin:** Full access + quản lý team
- **Architect:** Tạo project, review design, annotate, approve
- **Viewer:** Chỉ xem project, không chỉnh sửa

---

## Epic 2: Project & Intake (Thu thập yêu cầu)

### US-2.1: Tạo dự án mới [P0, S]

**As a** architect/admin,
**I want to** tạo một dự án thiết kế mới,
**So that** tôi bắt đầu quy trình thu thập yêu cầu và thiết kế.

**Acceptance Criteria:**
- [ ] **AC1:** Given user ở dashboard, When click "Tạo dự án mới" và nhập tên dự án, Then project được tạo với trạng thái "Draft" và redirect vào project workspace.
- [ ] **AC2:** Given project vừa được tạo, Then hiển thị prompt chọn phương thức intake: "Chat với AI" hoặc "Điền form".
- [ ] **AC3:** Given project đã tạo, Then project xuất hiện trong danh sách projects trên dashboard với thông tin: tên, ngày tạo, trạng thái, người tạo.

---

### US-2.2: Thu thập yêu cầu qua Chat AI (Intake Chatbot) [P0, L]

**As a** user (architect hoặc end-client khi được mời),
**I want to** chat với AI để mô tả yêu cầu thiết kế nhà,
**So that** AI hiểu rõ nhu cầu và tạo design brief có cấu trúc.

**Acceptance Criteria:**
- [ ] **AC1:** Given user chọn "Chat với AI", When bắt đầu conversation, Then AI chào hỏi và bắt đầu hỏi về: loại công trình (nhà phố, biệt thự, căn hộ), kích thước đất (dài x rộng x mặt tiền), số tầng mong muốn.
- [ ] **AC2:** Given AI đang hỏi, When user trả lời "đất 5x20m, muốn xây 4 tầng", Then AI extract được: width=5m, depth=20m, floors=4 và xác nhận lại với user.
- [ ] **AC3:** Given AI đã có kích thước đất, When tiếp tục conversation, Then AI hỏi tiếp về: số phòng ngủ, số WC, có cần garage không, phong cách (hiện đại/cổ điển/tối giản), budget range, lifestyle đặc biệt (WFH, người già, trẻ nhỏ, thú cưng).
- [ ] **AC4:** Given user upload hình ảnh tham khảo (reference images), Then AI nhận diện phong cách và xác nhận: "Tôi thấy bạn thích phong cách hiện đại tối giản với mặt tiền kính. Đúng không?"
- [ ] **AC5:** Given AI đã thu thập đủ thông tin, Then AI tạo **Design Brief** dạng structured JSON và hiển thị summary cho user confirm trước khi generate.
- [ ] **AC6:** Given user confirm design brief, Then trạng thái project chuyển từ "Draft" → "Brief Confirmed".

**Design Brief Output Format:**
```json
{
  "lot": { "width": 5, "depth": 20, "frontage": "south", "unit": "m" },
  "building": { "floors": 4, "type": "townhouse" },
  "rooms": [
    { "type": "bedroom", "count": 4, "notes": "1 master with ensuite" },
    { "type": "bathroom", "count": 3 },
    { "type": "living_room", "count": 1 },
    { "type": "kitchen", "count": 1, "notes": "open kitchen" },
    { "type": "garage", "count": 1, "notes": "1 car" }
  ],
  "style": "modern_minimalist",
  "budget_range": { "min": 2000000000, "max": 3000000000, "currency": "VND" },
  "lifestyle": ["work_from_home", "small_children"],
  "reference_images": ["url1", "url2"],
  "special_requests": "Muốn có ban công tầng 3 rộng, thoáng gió"
}
```

---

### US-2.3: Thu thập yêu cầu qua Structured Form [P0, M]

**As a** user,
**I want to** điền form có cấu trúc để nhập yêu cầu thiết kế,
**So that** tôi có thể nhanh chóng cung cấp thông tin mà không cần chat nhiều.

**Acceptance Criteria:**
- [ ] **AC1:** Given user chọn "Điền form", Then hiển thị multi-step form với các bước: (1) Thông tin lô đất, (2) Yêu cầu phòng, (3) Phong cách & Budget, (4) Yêu cầu đặc biệt, (5) Review & Confirm.
- [ ] **AC2:** Bước 1 – Thông tin lô đất: input fields cho chiều rộng, chiều sâu, hướng mặt tiền (dropdown N/S/E/W), số tầng, loại công trình. Các trường bắt buộc: chiều rộng, chiều sâu, số tầng.
- [ ] **AC3:** Bước 2 – Yêu cầu phòng: dynamic form cho phép thêm/xóa loại phòng (bedroom, bathroom, kitchen, living, garage, study, laundry...) với số lượng và ghi chú.
- [ ] **AC4:** Bước 3 – Phong cách: chọn từ gallery styles (modern, minimalist, classic, tropical, industrial) + upload reference images (max 5, max 10MB mỗi file) + nhập budget range (slider hoặc input).
- [ ] **AC5:** Bước 4 – Yêu cầu đặc biệt: textarea cho free-text, checkbox cho lifestyle options (WFH, elderly, kids, pets, home gym, rooftop garden).
- [ ] **AC6:** Bước 5 – Review: hiển thị tất cả thông tin đã nhập, cho phép quay lại sửa. Khi confirm, tạo Design Brief JSON giống output của chatbot.
- [ ] **AC7:** Given form đã được submit, Then data được validate (kích thước > 0, ít nhất 1 phòng) và project status chuyển thành "Brief Confirmed".

---

### US-2.4: Xem và chỉnh sửa Design Brief [P1, S]

**As a** architect,
**I want to** xem và chỉnh sửa Design Brief đã được tạo,
**So that** tôi có thể tinh chỉnh yêu cầu trước khi AI bắt đầu generate.

**Acceptance Criteria:**
- [ ] **AC1:** Given project ở trạng thái "Brief Confirmed", When architect mở project, Then hiển thị Design Brief dạng editable.
- [ ] **AC2:** Given architect thay đổi field bất kỳ (vd: thêm phòng, đổi style), When click "Save", Then brief được cập nhật và ghi log thay đổi.
- [ ] **AC3:** Given architect đã chỉnh sửa brief, When click "Generate Design", Then bắt đầu quy trình AI generation.

---

## Epic 3: AI Floor Plan Generation

### US-3.1: Generate 2D Floor Plan từ Design Brief [P0, L]

**As a** user,
**I want to** AI tạo bản vẽ 2D floor plan từ yêu cầu trong Design Brief,
**So that** tôi nhanh chóng có bản concept để review.

**Acceptance Criteria:**
- [ ] **AC1:** Given project ở trạng thái "Brief Confirmed", When user click "Generate Design", Then hệ thống gửi Design Brief đến AI generation pipeline.
- [ ] **AC2:** Given generation đang chạy, Then hiển thị progress indicator với estimated time (thường 2-5 phút).
- [ ] **AC3:** Given generation hoàn thành, Then hiển thị **2-3 floor plan variations** cho mỗi tầng, mỗi variation có layout khác nhau.
- [ ] **AC4:** Mỗi floor plan bao gồm: tường (wall lines), phân chia phòng, label tên phòng, kích thước cơ bản (chiều dài x chiều rộng mỗi phòng), cầu thang (nếu nhiều tầng), cửa ra vào và cửa sổ.
- [ ] **AC5:** Given floor plan được generate, Then hình ảnh có resolution tối thiểu 2048x2048px, format PNG.
- [ ] **AC6:** Given user nhấn vào một variation, Then hiển thị full-screen view với khả năng zoom in/out.
- [ ] **AC7:** Given generation thất bại (timeout, GPU error), Then hiển thị thông báo lỗi rõ ràng và nút "Retry".

**Technical Notes:**
- Pipeline: Design Brief JSON → prompt engineering → ControlNet conditioned generation → post-processing (label overlay)
- Mỗi tầng generate riêng, dùng floor plan tầng dưới làm constraint cho tầng trên (cầu thang, cột)

---

### US-3.2: Chọn floor plan variation ưa thích [P0, S]

**As a** user,
**I want to** chọn floor plan variation mà tôi thích nhất,
**So that** AI sử dụng layout đó làm base cho 3D visualization và các bước tiếp theo.

**Acceptance Criteria:**
- [ ] **AC1:** Given 2-3 variations đã được generate, Then hiển thị dạng card grid, mỗi card có thumbnail + tên (Option A, B, C).
- [ ] **AC2:** Given user click "Chọn" trên một variation, Then variation đó được mark là "Selected" và các variation khác chuyển thành "Alternative".
- [ ] **AC3:** Given user đã chọn variation, When click "Next: 3D Visualization", Then bắt đầu pipeline 3D render dựa trên selected floor plan.
- [ ] **AC4:** Given user muốn đổi ý, When click "Chọn" trên variation khác, Then selection được cập nhật (trước khi bấm Next).

---

### US-3.3: Regenerate floor plan với điều chỉnh [P0, M]

**As a** user,
**I want to** yêu cầu AI tạo lại floor plan với chỉnh sửa cụ thể,
**So that** tôi nhận được design gần với ý muốn hơn mà không cần bắt đầu lại từ đầu.

**Acceptance Criteria:**
- [ ] **AC1:** Given floor plans đã được generate, When user click "Yêu cầu chỉnh sửa", Then mở text input cho user nhập feedback (vd: "Phòng ngủ master quá nhỏ, muốn phòng khách ở vị trí khác").
- [ ] **AC2:** Given user nhập feedback và click "Regenerate", Then AI xử lý feedback, kết hợp với Design Brief gốc, và generate lại 2-3 variations mới.
- [ ] **AC3:** Given regeneration hoàn thành, Then hiển thị variations mới, đồng thời vẫn giữ variations cũ trong tab "Previous Versions".
- [ ] **AC4:** Given user đã regenerate 5 lần, Then hiển thị warning: "Bạn đã regenerate nhiều lần. Hãy thử chỉnh sửa Design Brief hoặc liên hệ KTS để hỗ trợ."

---

## Epic 4: 3D Visualization

### US-4.1: Generate 3D render từ floor plan [P0, L]

**As a** user,
**I want to** xem bản render 3D của căn nhà dựa trên floor plan đã chọn,
**So that** tôi hình dung rõ hơn thiết kế thực tế sẽ trông như thế nào.

**Acceptance Criteria:**
- [ ] **AC1:** Given user đã chọn floor plan variation, When click "Generate 3D", Then hệ thống bắt đầu pipeline: floor plan → 3D model → render.
- [ ] **AC2:** Given generation đang chạy, Then hiển thị progress bar với stages: "Đang tạo mô hình 3D..." → "Đang render exterior..." → "Đang render interior...".
- [ ] **AC3:** Given generation hoàn thành, Then hiển thị: (a) 1 exterior render (mặt tiền), (b) 2-3 interior renders (phòng khách, phòng ngủ master, bếp).
- [ ] **AC4:** Mỗi render có resolution tối thiểu 1920x1080px, style phù hợp với preference trong Design Brief (modern/classic/...).
- [ ] **AC5:** Given user click vào một render, Then hiển thị full-screen với zoom, download option.

**Technical Notes:**
- Exterior: ControlNet (depth/edge map từ floor plan) + style prompt → SD render
- Interior: Room layout → ControlNet conditioning → interior render per room
- Dùng ComfyUI workflow, chạy trên GPU server (RunPod)

---

### US-4.2: Interactive 3D Viewer trên browser [P0, L]

**As a** user,
**I want to** xem và tương tác với mô hình 3D của căn nhà trên browser,
**So that** tôi có thể khám phá thiết kế từ mọi góc nhìn.

**Acceptance Criteria:**
- [ ] **AC1:** Given 3D model đã được generate, When user mở tab "3D Viewer", Then hiển thị 3D model trong web viewer.
- [ ] **AC2:** Given viewer đang hiển thị, Then user có thể: orbit (xoay quanh), zoom in/out, pan (di chuyển).
- [ ] **AC3:** Given viewer đang hiển thị, When user click vào một phòng, Then hiển thị popup: tên phòng, kích thước (m²).
- [ ] **AC4:** Given viewer đang hiển thị, Then user có thể chuyển đổi giữa: "Exterior View" (nhìn từ ngoài), "Floor Plan View" (nhìn từ trên), "Cut Section View" (cắt tầng).
- [ ] **AC5:** Given viewer trên mobile browser, Then hỗ trợ touch gestures (pinch to zoom, swipe to rotate).
- [ ] **AC6:** Given 3D model loading, Then hiển thị skeleton/placeholder trong khi tải, tải xong hiển thị smooth (< 5s cho model < 50MB).

**Technical Notes:**
- Three.js cho rendering engine
- ThatOpen BIM Components cho measurement tools & floor plan navigation mode
- GLTF/GLB format cho 3D model (lightweight cho web)

---

### US-4.3: Đo kích thước trên 3D viewer [P1, M]

**As a** architect,
**I want to** đo kích thước các phần trong 3D model,
**So that** tôi kiểm tra xem layout có hợp lý và đúng tỷ lệ không.

**Acceptance Criteria:**
- [ ] **AC1:** Given user ở chế độ "Measurement", When click 2 điểm trên model, Then hiển thị khoảng cách giữa 2 điểm (đơn vị m/cm).
- [ ] **AC2:** Given measurement đã được tạo, Then measurement labels hiển thị persistent trên model cho đến khi user xóa.
- [ ] **AC3:** Given user click "Clear Measurements", Then xóa tất cả measurement labels.

---

## Epic 5: Expert Review Gate

### US-5.1: Queue review cho KTS [P0, M]

**As a** architect (KTS),
**I want to** xem danh sách các design đang chờ review,
**So that** tôi có thể review và approve trước khi trình cho khách hàng.

**Acceptance Criteria:**
- [ ] **AC1:** Given architect đăng nhập, When mở "Review Queue", Then hiển thị danh sách projects có design chờ review, sort theo ngày tạo mới nhất.
- [ ] **AC2:** Mỗi item trong queue hiển thị: tên project, tên client, ngày generate, thumbnail floor plan, trạng thái (Pending Review / Reviewed / Approved / Rejected).
- [ ] **AC3:** Given architect click vào một project, Then mở review workspace với: floor plan, 3D renders, Design Brief, và conversation history.

---

### US-5.2: Annotate và comment trên design [P0, M]

**As a** architect,
**I want to** đánh dấu và ghi chú trực tiếp lên floor plan/3D render,
**So that** feedback của tôi rõ ràng và cụ thể cho từng vị trí.

**Acceptance Criteria:**
- [ ] **AC1:** Given architect ở review workspace, When chọn tool "Annotate", Then có thể vẽ marker (pin) lên vị trí cụ thể trên floor plan.
- [ ] **AC2:** Given architect đặt marker, Then mở text input để nhập comment cho marker đó (vd: "Cửa sổ ở đây sẽ bị hướng Tây, quá nóng").
- [ ] **AC3:** Given annotations đã được thêm, Then tất cả annotations hiển thị dạng numbered list bên cạnh floor plan.
- [ ] **AC4:** Given architect click vào annotation trong list, Then floor plan tự động pan/zoom đến vị trí marker tương ứng.

---

### US-5.3: Approve hoặc Reject design [P0, S]

**As a** architect,
**I want to** approve hoặc reject một design,
**So that** chỉ design đạt chất lượng mới được trình cho khách hàng.

**Acceptance Criteria:**
- [ ] **AC1:** Given architect đã review xong, When click "Approve", Then project status chuyển thành "Approved" và sẵn sàng trình client.
- [ ] **AC2:** Given architect click "Request Revision", Then bắt buộc nhập lý do/feedback, và status chuyển thành "Revision Requested". AI sẽ dùng feedback này để regenerate.
- [ ] **AC3:** Given architect click "Reject", Then bắt buộc nhập lý do, status chuyển thành "Rejected", và team nhận notification.
- [ ] **AC4:** Given design đã approved, Then hiển thị badge "KTS Approved" trên design khi trình client.

---

## Epic 6: Client Feedback & Revision Loop

### US-6.1: Chia sẻ design cho client [P0, M]

**As a** architect,
**I want to** chia sẻ design đã approved cho client xem,
**So that** client có thể review và đưa feedback.

**Acceptance Criteria:**
- [ ] **AC1:** Given design đã approved, When architect click "Share with Client", Then generate một link chia sẻ (có thể set password, expiry date).
- [ ] **AC2:** Given client mở link, Then hiển thị presentation view: floor plans, 3D renders, 3D viewer (read-only), Design Brief summary. Không cần đăng nhập.
- [ ] **AC3:** Given client xem xong, Then có nút "Đồng ý thiết kế này" hoặc "Tôi muốn chỉnh sửa".

---

### US-6.2: Client feedback trên design [P0, M]

**As a** client (end-user),
**I want to** ghi feedback trực tiếp trên design,
**So that** architect/AI hiểu chính xác tôi muốn thay đổi gì.

**Acceptance Criteria:**
- [ ] **AC1:** Given client chọn "Tôi muốn chỉnh sửa", Then mở feedback interface với 2 options: (a) chat feedback, (b) annotate trên floor plan.
- [ ] **AC2:** Given client chọn chat feedback, When nhập "Muốn phòng khách rộng hơn, bớt 1 phòng ngủ tầng 2", Then feedback được lưu và gắn vào project.
- [ ] **AC3:** Given client chọn annotate, When vẽ marker lên floor plan + nhập comment, Then annotation được lưu kèm vị trí.
- [ ] **AC4:** Given client đã submit feedback, Then architect nhận notification và có thể xem tất cả feedback trong review workspace.

---

### US-6.3: AI regenerate dựa trên client feedback [P0, L]

**As a** architect,
**I want to** yêu cầu AI regenerate design dựa trên feedback của client,
**So that** vòng revision nhanh hơn mà không cần KTS thao tác thủ công.

**Acceptance Criteria:**
- [ ] **AC1:** Given client feedback đã được submit, When architect mở project, Then hiển thị tất cả feedback items (text + annotations) trong panel "Client Feedback".
- [ ] **AC2:** Given architect click "AI Revise", Then AI đọc feedback + Design Brief gốc + current design, và generate lại floor plan + 3D (2-3 variations mới).
- [ ] **AC3:** Given AI revision hoàn thành, Then hiển thị variations mới bên cạnh version cũ để so sánh.
- [ ] **AC4:** Given architect satisfied, When approve design mới, Then gửi lại cho client xem.
- [ ] **AC5:** Given project đã qua 3+ vòng revision, Then hệ thống suggest: "Hãy cân nhắc meeting trực tiếp với client để align yêu cầu".

---

## Epic 7: Version History & Comparison

### US-7.1: Xem lịch sử versions [P1, M]

**As a** architect/user,
**I want to** xem lịch sử tất cả các version design đã generate,
**So that** tôi có thể track sự thay đổi và quay lại version cũ nếu cần.

**Acceptance Criteria:**
- [ ] **AC1:** Given project có nhiều versions, When mở tab "Version History", Then hiển thị timeline với tất cả versions: V1, V2, V3... mỗi entry có thumbnail, ngày tạo, lý do (initial / client feedback / architect revision).
- [ ] **AC2:** Given user click vào một version, Then hiển thị full design của version đó (floor plans + renders).
- [ ] **AC3:** Given user muốn quay lại version cũ, When click "Use this version", Then tạo một version mới (clone) từ version cũ.

---

### US-7.2: So sánh 2 versions side-by-side [P1, M]

**As a** architect,
**I want to** so sánh 2 versions cạnh nhau,
**So that** tôi thấy rõ sự khác biệt giữa các lần revision.

**Acceptance Criteria:**
- [ ] **AC1:** Given user ở Version History, When chọn 2 versions và click "Compare", Then hiển thị side-by-side view.
- [ ] **AC2:** Given side-by-side view, Then floor plans hiển thị cùng tỷ lệ, cùng orientation, và có thể synchronized zoom/pan.
- [ ] **AC3:** Given side-by-side view, Then bên dưới hiển thị diff summary: "Phòng ngủ 3 thay đổi kích thước từ 12m² → 15m²".

---

## Epic 8: Export & Delivery

### US-8.1: Export PDF bản vẽ sơ bộ [P0, M]

**As a** architect/user,
**I want to** export bản vẽ concept dưới dạng PDF,
**So that** tôi có tài liệu để in, trình bày, và chia sẻ offline.

**Acceptance Criteria:**
- [ ] **AC1:** Given design đã được approved, When user click "Export PDF", Then hệ thống generate PDF.
- [ ] **AC2:** PDF bao gồm: (a) Trang bìa với tên project + client, (b) Design Brief summary, (c) Floor plan mỗi tầng (1 trang/tầng), (d) 3D renders (exterior + interior), (e) Thông tin kỹ thuật cơ bản (diện tích mỗi tầng, tổng diện tích sàn).
- [ ] **AC3:** Given PDF đã generate, Then tự động download file, đồng thời lưu trong project files.
- [ ] **AC4:** PDF có watermark "CONCEPT DESIGN – NOT FOR CONSTRUCTION" trên mỗi trang.

---

### US-8.2: Download hình ảnh 3D renders [P1, S]

**As a** user,
**I want to** download từng hình 3D render ở chất lượng cao,
**So that** tôi sử dụng để trình bày cho stakeholders.

**Acceptance Criteria:**
- [ ] **AC1:** Given user xem 3D render, When click icon "Download", Then download hình PNG ở resolution gốc (min 1920x1080).
- [ ] **AC2:** Given user muốn download tất cả, When click "Download All Renders", Then download ZIP chứa tất cả renders + floor plans.

---

### US-8.3: Export DXF cơ bản [P2, M]

**As a** architect,
**I want to** export floor plan dưới dạng DXF,
**So that** tôi có thể mở và chỉnh sửa tiếp trong AutoCAD/SketchUp.

**Acceptance Criteria:**
- [ ] **AC1:** Given design đã được approved, When click "Export DXF", Then hệ thống convert floor plan sang DXF format.
- [ ] **AC2:** DXF bao gồm: walls (polylines), room labels (text), basic dimensions.
- [ ] **AC3:** Given DXF đã export, Then file có thể mở thành công trong AutoCAD LT hoặc LibreCAD.

**Notes:** P2 vì phụ thuộc vào khả năng structured geometry của AI output. Nếu AI chỉ output image, cần thêm bước image → vector conversion.

---

## Epic 9: Dashboard & Project Management

### US-9.1: Dashboard tổng quan [P0, M]

**As a** architect/admin,
**I want to** thấy dashboard tổng quan tất cả projects,
**So that** tôi quản lý được workload và trạng thái từng project.

**Acceptance Criteria:**
- [ ] **AC1:** Given user đăng nhập, Then dashboard hiển thị: (a) Số project theo trạng thái (Draft, In Progress, Pending Review, Approved, Delivered), (b) List projects có thể filter/sort, (c) Quick actions (tạo mới, open recent).
- [ ] **AC2:** Given user click vào một project card, Then redirect vào project workspace.
- [ ] **AC3:** Given user search tên project hoặc client name, Then filter danh sách real-time.

---

### US-9.2: Notification system [P1, M]

**As a** team member,
**I want to** nhận thông báo khi có sự kiện quan trọng,
**So that** tôi không bỏ lỡ việc cần xử lý.

**Acceptance Criteria:**
- [ ] **AC1:** Given design mới cần review, Then architect nhận notification "Design mới cho Project X đang chờ review".
- [ ] **AC2:** Given client submit feedback, Then architect nhận notification "Client đã gửi feedback cho Project X".
- [ ] **AC3:** Given AI generation hoàn thành, Then user nhận notification "Design đã sẵn sàng cho Project X".
- [ ] **AC4:** Notifications hiển thị in-app (bell icon) + email (configurable).

---

## Summary: User Story Map

```
                        PHASE 1 USER STORY MAP
═══════════════════════════════════════════════════════════════

Epic 1: Auth          │ US-1.1 Đăng ký │ US-1.2 Login │ US-1.3 Team
──────────────────────┼────────────────────────────────────────────
Epic 2: Intake        │ US-2.1 Tạo project │ US-2.2 Chat │ US-2.3 Form │ US-2.4 Edit Brief
──────────────────────┼────────────────────────────────────────────
Epic 3: Generation    │ US-3.1 Floor Plan │ US-3.2 Chọn variation │ US-3.3 Regenerate
──────────────────────┼────────────────────────────────────────────
Epic 4: 3D            │ US-4.1 3D Render │ US-4.2 3D Viewer │ US-4.3 Measure
──────────────────────┼────────────────────────────────────────────
Epic 5: Review        │ US-5.1 Queue │ US-5.2 Annotate │ US-5.3 Approve/Reject
──────────────────────┼────────────────────────────────────────────
Epic 6: Feedback      │ US-6.1 Share │ US-6.2 Client FB │ US-6.3 AI Revise
──────────────────────┼────────────────────────────────────────────
Epic 7: Versioning    │ US-7.1 History │ US-7.2 Compare
──────────────────────┼────────────────────────────────────────────
Epic 8: Export        │ US-8.1 PDF │ US-8.2 Images │ US-8.3 DXF
──────────────────────┼────────────────────────────────────────────
Epic 9: Dashboard     │ US-9.1 Overview │ US-9.2 Notifications

═══════════════════════════════════════════════════════════════
P0 (Must have): 16 stories    P1 (Should have): 6 stories    P2 (Nice to have): 1 story
Total: 23 user stories
```
