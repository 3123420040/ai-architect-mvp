---
Feature: AI Architect Module Business Requirements
Author:
Status: Draft
Last updated: Apr 11, 2026
---

# Phase 1 – Business Requirements Và User Stories Theo Từng Module

## 1. Mục tiêu tài liệu

Tài liệu này chuyển kiến trúc module của AI Architect thành ngôn ngữ product/business để team có thể:

- chốt vai trò của từng module trong hệ thống
- hiểu rõ module đó giải quyết vấn đề gì cho business và cho user
- có user stories đủ cụ thể để breakdown sang backlog implementation

Tài liệu này bám theo định hướng đã chốt:

- end user phải thấy demo 2D nhanh nhất
- phương án 2D phải được khóa thành file chuẩn để KTS tiếp tục làm việc
- 3D là lớp dẫn xuất từ phương án đã khóa, không phải nguồn sự thật
- mục tiêu cuối là đi tới bộ file chuẩn để client, KTS và nhà thầu có thể chốt và triển khai
- hệ thống phải học được phong cách riêng của từng KTS từ thư viện thiết kế đã import trước đó

## 2. Các actor chính

| Actor | Vai trò |
| --- | --- |
| End user | Người có nhu cầu thiết kế nhà, góp ý và chốt hướng phương án |
| Architect / KTS | Người review, khóa hướng, chỉnh sửa chuyên môn và duyệt hồ sơ |
| Design firm admin | Quản trị team, thư viện phong cách, phân quyền và dự án |
| Reviewer / kỹ sư | Người review tính khả thi hoặc chất lượng ở các phase sâu hơn |
| Contractor / nhà thầu | Bên nhận hồ sơ để bóc tách và triển khai thi công |

## 3. Danh sách module

| ID | Module | Vai trò chính |
| --- | --- | --- |
| M1 | Experience Layer | Giao diện làm việc cho end user, KTS, reviewer và contractor |
| M2 | Intake & Brief Module | Thu thập và chuẩn hóa yêu cầu thành brief có cấu trúc |
| M3 | Architect Style Intelligence | Học phong cách đặc trưng của từng KTS từ dữ liệu đã import |
| M4 | Canonical Design State | Lưu nguồn sự thật kỹ thuật cho từng phương án đã khóa |
| M5 | 2D Generation Engine | Tạo phương án 2D nhanh cho phase explore |
| M6 | Review & Annotation Module | Cho KTS review, annotate, approve hoặc reject |
| M7 | 3D Derivation & Visual Generation | Dẫn xuất 3D và render từ phương án 2D đã khóa |
| M8 | Standards Export Module | Xuất file chuẩn như SVG, DXF, PDF, về sau là IFC |
| M9 | Delivery & Handoff Module | Đóng gói và bàn giao hồ sơ theo version approved |

---

## M1. Experience Layer

### Business purpose

Module này đảm bảo mỗi nhóm người dùng nhìn thấy đúng thứ họ cần, vào đúng thời điểm, với đúng mức quyền hạn. Nó là lớp trải nghiệm giúp biến một hệ thống AI phức tạp thành workflow dễ dùng và dễ tin.

### Business requirements

- `BR-M1.1` Hệ thống phải cung cấp workspace tách biệt cho end user, KTS, admin và bên nhận bàn giao.
- `BR-M1.2` End user phải có thể xem option 2D nhanh, dễ so sánh, và góp ý mà không cần hiểu cấu trúc kỹ thuật sâu.
- `BR-M1.3` KTS phải có workspace riêng để review, annotate, khóa hướng và theo dõi version.
- `BR-M1.4` Mọi màn hình hiển thị phải bám vào version được duyệt từ `Canonical Design State`, không tự suy diễn “bản hiện tại”.
- `BR-M1.5` Hệ thống phải cho phép trình bày rõ trạng thái của mỗi version: draft, under review, approved, superseded, handoff-ready.

### User stories

### M1-US-01: End user xem gallery phương án

**As a** end user  
**I want** xem các phương án 2D ở dạng gallery dễ hiểu  
**So that** tôi có thể chọn nhanh một hướng phù hợp mà không bị choáng bởi chi tiết kỹ thuật.

**Acceptance Criteria:**
- Given dự án đã generate xong option 2D, When user mở màn hình designs, Then hiển thị các phương án dưới dạng card có thumbnail, tên phương án và mô tả ngắn.
- Given user chọn một card, When mở chi tiết, Then hiển thị preview lớn, ghi chú công năng chính và trạng thái review của KTS nếu có.
- Given phương án chưa được KTS approved, When user xem, Then hiển thị rõ đây là bản concept chưa phải hồ sơ triển khai.

### M1-US-02: KTS có workspace review chuyên biệt

**As a** KTS  
**I want** có workspace riêng cho review và annotate  
**So that** tôi có thể duyệt, chỉnh hướng và phê duyệt phương án mà không lẫn với trải nghiệm của end user.

**Acceptance Criteria:**
- Given KTS đăng nhập, When mở một project, Then có tab review workspace riêng.
- Given project có version chờ review, When KTS mở workspace, Then hiển thị floor plan, render, brief và lịch sử feedback liên quan tới đúng version đó.
- Given KTS annotate hoặc approve, When thao tác thành công, Then hệ thống ghi log gắn đúng vào version đang review.

### M1-US-03: Delivery workspace cho bàn giao

**As a** contractor hoặc PM  
**I want** truy cập một workspace bàn giao chỉ chứa bản approved  
**So that** tôi chỉ làm việc trên đúng bộ hồ sơ chính thức.

**Acceptance Criteria:**
- Given project có handoff package, When người dùng có quyền mở delivery workspace, Then chỉ hiển thị bundle đã approved.
- Given có nhiều version lịch sử, When xem delivery workspace, Then chỉ một version được đánh dấu là current handoff package.
- Given bundle mới được phê duyệt, When mở lại workspace, Then bundle mới thay thế bundle cũ làm bản mặc định.

---

## M2. Intake & Brief Module

### Business purpose

Module này giải quyết bài toán lớn nhất ở đầu quy trình: biến nhu cầu mơ hồ thành brief đủ rõ để AI và KTS cùng làm việc trên cùng một cách hiểu.

### Business requirements

- `BR-M2.1` Hệ thống phải hỗ trợ intake qua cả chat và form có cấu trúc.
- `BR-M2.2` Hệ thống phải phát hiện các thông tin còn thiếu hoặc mâu thuẫn trước khi bắt đầu generate.
- `BR-M2.3` Kết quả của intake phải được chuẩn hóa thành `Design Brief JSON`.
- `BR-M2.4` Brief phải có thể chỉnh sửa, version hóa và audit được.
- `BR-M2.5` Brief phải chứa đủ các trường nền cho generation, review và export về sau.

### User stories

### M2-US-01: Tạo brief qua chat

**As a** end user hoặc KTS  
**I want** mô tả nhu cầu qua chat tự nhiên  
**So that** hệ thống có thể nhanh chóng hiểu và chuẩn hóa yêu cầu thiết kế của tôi.

**Acceptance Criteria:**
- Given user chọn intake bằng chat, When conversation bắt đầu, Then AI hỏi tuần tự các thông tin nền như kích thước đất, số tầng, số phòng, phong cách, budget và yêu cầu đặc biệt.
- Given user trả lời tự nhiên, When AI parse dữ liệu, Then hệ thống extract thành các field cấu trúc và xác nhận lại với user.
- Given đã đủ thông tin, When user xác nhận, Then tạo `Design Brief JSON`.

### M2-US-02: Chỉnh sửa brief trước khi generate

**As a** KTS  
**I want** chỉnh sửa brief trước khi bắt đầu generate  
**So that** tôi có thể đảm bảo đầu vào phản ánh đúng yêu cầu và định hướng chuyên môn.

**Acceptance Criteria:**
- Given project đang ở trạng thái brief confirmed, When KTS mở brief editor, Then các trường chính có thể chỉnh sửa được.
- Given KTS thay đổi thông tin, When lưu lại, Then hệ thống tạo log thay đổi.
- Given brief đã sửa, When bắt đầu generate, Then generation phải dùng brief mới nhất.

### M2-US-03: Phát hiện mâu thuẫn trong intake

**As a** system  
**I want** phát hiện yêu cầu mâu thuẫn hoặc còn thiếu  
**So that** team không generate trên một brief sai ngay từ đầu.

**Acceptance Criteria:**
- Given brief thiếu thông tin cốt lõi, When user cố generate, Then hệ thống chặn và hiển thị các trường cần bổ sung.
- Given brief có mâu thuẫn logic, When validate, Then hiển thị cảnh báo cụ thể để user hoặc KTS sửa.
- Given mâu thuẫn đã được xử lý, When validate lại, Then project đủ điều kiện chuyển sang generation.

---

## M3. Architect Style Intelligence

### Business purpose

Module này giúp hệ thống không tạo ra output generic. Nó cho phép AI bám đúng “chữ ký thiết kế” của từng KTS hoặc từng công ty thiết kế, từ đó tăng trust và giảm tỷ lệ KTS phải sửa lại hoàn toàn.

### Business requirements

- `BR-M3.1` Hệ thống phải cho phép import thư viện thiết kế cũ của từng KTS hoặc design firm.
- `BR-M3.2` Hệ thống phải trích xuất được pattern phong cách từ bản vẽ, render, metadata và feedback lịch sử.
- `BR-M3.3` Hệ thống phải xây dựng `Architect Style Profile` versioned cho từng KTS.
- `BR-M3.4` Style profile phải được KTS review và chỉnh lại nếu hệ thống hiểu sai.
- `BR-M3.5` 2D generation và 3D visual generation phải có khả năng dùng style profile như constraint.

### User stories

### M3-US-01: Import thư viện thiết kế của KTS

**As a** KTS hoặc admin  
**I want** upload các bản thiết kế cũ của mình vào hệ thống  
**So that** AI có thể học được phong cách và ngôn ngữ thiết kế đặc trưng của tôi.

**Acceptance Criteria:**
- Given user ở style library workspace, When upload bộ file bản vẽ, render và metadata, Then hệ thống tạo style ingestion job.
- Given file được ingest thành công, When xử lý xong, Then assets được nhóm theo KTS và project nguồn.
- Given file lỗi định dạng, When import, Then hệ thống báo lỗi rõ file nào không đọc được.

### M3-US-02: KTS review style profile

**As a** KTS  
**I want** xem và chỉnh profile phong cách hệ thống học ra  
**So that** AI không hiểu sai DNA thiết kế của tôi.

**Acceptance Criteria:**
- Given style ingestion hoàn tất, When KTS mở style profile, Then hiển thị các pattern hệ thống nhận ra như façade language, vật liệu, bố cục không gian và adjacency phổ biến.
- Given có pattern sai, When KTS sửa hoặc tắt pattern đó, Then profile được cập nhật.
- Given profile đã approved, When generation chạy cho project mới, Then hệ thống dùng đúng profile này làm constraint.

### M3-US-03: Resolve style profile cho từng project

**As a** system  
**I want** kết hợp style profile của KTS với brief cụ thể của khách hàng  
**So that** output vừa đúng giọng KTS vừa đáp ứng yêu cầu riêng của từng dự án.

**Acceptance Criteria:**
- Given project được gán cho một KTS cụ thể, When bắt đầu generation, Then hệ thống resolve `Architect Style Profile` tương ứng.
- Given brief của khách mâu thuẫn với một số pattern của style profile, When resolve style, Then hệ thống giữ brief làm constraint cứng và style làm constraint mềm.
- Given style profile thay đổi theo version mới, When project generate ở thời điểm sau, Then system lưu rõ profile version nào đã được dùng.

---

## M4. Canonical Design State

### Business purpose

Đây là trung tâm sự thật của toàn hệ thống. Mục tiêu là để mọi module phía sau cùng làm việc trên một phiên bản thiết kế đã khóa, tránh drift giữa ảnh, render, viewer và file export.

### Business requirements

- `BR-M4.1` Hệ thống phải lưu được `Canonical Plan Version` cho mỗi phương án đã khóa.
- `BR-M4.2` Canonical state phải chứa brief, geometry, style profile, review state và liên kết đến các file dẫn xuất.
- `BR-M4.3` Mọi sequence sau khi chốt hướng phải làm việc trên canonical version, không làm việc lại trên prompt thô.
- `BR-M4.4` Hệ thống phải hỗ trợ lineage giữa các version.
- `BR-M4.5` Hệ thống phải cho phép compare và trace mọi thay đổi giữa các version.

### User stories

### M4-US-01: Khóa một phương án thành canonical version

**As a** KTS  
**I want** khóa một option 2D thành canonical version  
**So that** toàn bộ các bước tiếp theo dùng cùng một nguồn sự thật kỹ thuật.

**Acceptance Criteria:**
- Given project có nhiều option, When KTS chọn một option để lock, Then hệ thống tạo `Canonical Plan Version`.
- Given version đã được lock, When các module sau như export hoặc 3D chạy, Then phải tham chiếu tới canonical version đó.
- Given KTS lock một option khác sau này, When tạo canonical version mới, Then version cũ vẫn được giữ trong lineage.

### M4-US-02: So sánh hai version

**As a** KTS hoặc PM  
**I want** so sánh hai canonical version  
**So that** tôi hiểu được điều gì đã thay đổi trước khi chốt hướng tiếp theo.

**Acceptance Criteria:**
- Given project có từ hai version trở lên, When user chọn compare, Then hiển thị side-by-side các thay đổi chính.
- Given có khác biệt về geometry hoặc brief, When compare, Then hiển thị rõ thay đổi nằm ở đâu.
- Given cần quay lại version cũ, When clone from old version, Then tạo một canonical version mới dựa trên version đó.

### M4-US-03: Trace file dẫn xuất theo version

**As a** system  
**I want** gắn mọi render, export và bundle vào đúng canonical version  
**So that** không có chuyện dùng nhầm file từ version khác.

**Acceptance Criteria:**
- Given hệ thống sinh render hoặc export, When lưu file, Then file phải chứa reference đến canonical version nguồn.
- Given user mở delivery package, When xem metadata, Then biết bundle này xuất từ version nào.
- Given version bị superseded, When xem file cũ, Then hiển thị rõ file đó không còn là bản active.

---

## M5. 2D Generation Engine

### Business purpose

Module này tối ưu cho tốc độ ra phương án 2D đầu tiên, nhưng vẫn phải tạo ra output đủ chuẩn để canonical hóa, review và export tiếp.

### Business requirements

- `BR-M5.1` Hệ thống phải tạo được 2-3 phương án mặt bằng nhanh từ brief đã chuẩn hóa.
- `BR-M5.2` Mỗi option 2D phải có lớp preview để xem nhanh và lớp dữ liệu đủ để canonical hóa hoặc vector hóa.
- `BR-M5.3` Engine phải nhận style constraints từ `Architect Style Intelligence`.
- `BR-M5.4` Regeneration phải dựa trên feedback có cấu trúc, không chỉ là prompt lại tự do.
- `BR-M5.5` Engine phải đủ reproducible để team hiểu vì sao version mới khác version cũ.

### User stories

### M5-US-01: Generate option 2D đầu tiên

**As a** end user  
**I want** nhận 2-3 phương án 2D nhanh sau khi chốt brief  
**So that** tôi có thể sớm chọn hướng mình thích.

**Acceptance Criteria:**
- Given brief đã validated, When user bấm generate, Then hệ thống tạo 2-3 option 2D.
- Given generation hoàn tất, When hiển thị kết quả, Then mỗi option có preview rõ ràng, tên option và mô tả ngắn.
- Given generation lỗi, When job fail, Then hiển thị retry path rõ ràng.

### M5-US-02: Generate có bám style của KTS

**As a** KTS  
**I want** option 2D sinh ra có bám vào phong cách của tôi  
**So that** tôi không phải sửa lại toàn bộ ngôn ngữ thiết kế ở các vòng đầu.

**Acceptance Criteria:**
- Given project được gán style profile, When generate 2D, Then engine dùng style constraints tương ứng.
- Given user brief yêu cầu khác một phần so với style, When generate, Then hệ thống ưu tiên brief cứng và style mềm.
- Given KTS review output, When thấy output lệch style quá mức, Then có thể flag làm dữ liệu cải thiện profile.

### M5-US-03: Regenerate từ feedback có cấu trúc

**As a** end user hoặc KTS  
**I want** regenerate 2D theo feedback cụ thể  
**So that** phương án mới gần đúng ý hơn nhưng vẫn giữ được hướng đã chọn.

**Acceptance Criteria:**
- Given version hiện tại có feedback mới, When user/KTS gửi revise request, Then system map feedback vào thay đổi có cấu trúc.
- Given feedback chỉ chỉnh cục bộ, When regenerate, Then output mới giữ được phần lớn logic của version trước.
- Given regenerate hoàn tất, When lưu version mới, Then hiển thị rõ đây là version tiếp theo của version nào.

---

## M6. Review & Annotation Module

### Business purpose

Module này là cổng kiểm soát chất lượng bắt buộc để AI output trở thành thứ KTS có thể tin và chịu trách nhiệm review.

### Business requirements

- `BR-M6.1` Hệ thống phải có review queue cho các version chờ KTS duyệt.
- `BR-M6.2` KTS phải có thể annotate lên floor plan, render và về sau là model.
- `BR-M6.3` Mọi annotate và quyết định review phải gắn vào đúng version.
- `BR-M6.4` Hệ thống phải hỗ trợ approve, reject, request revise và log lý do tương ứng.
- `BR-M6.5` Feedback review phải quay ngược được về generation và style intelligence.

### User stories

### M6-US-01: KTS annotate trên floor plan

**As a** KTS  
**I want** đánh dấu và ghi chú trực tiếp lên floor plan  
**So that** team và AI biết chính xác khu vực nào cần chỉnh.

**Acceptance Criteria:**
- Given KTS mở review workspace, When chọn annotate tool, Then có thể đặt pin hoặc marker lên vị trí cụ thể.
- Given annotation được tạo, When lưu lại, Then note gắn với đúng version và đúng tọa độ/ngữ cảnh.
- Given người khác mở cùng version, When xem lại, Then thấy annotate đó trong review history.

### M6-US-02: Approve hoặc reject version

**As a** KTS  
**I want** approve hoặc reject một version  
**So that** hệ thống biết bản nào được đi tiếp và bản nào cần chỉnh lại.

**Acceptance Criteria:**
- Given version đang under review, When KTS click approve, Then version chuyển sang approved.
- Given KTS click reject, When xác nhận lý do, Then version chuyển sang rejected và lưu reject reason.
- Given version được approve, When user hoặc PM xem, Then hiển thị badge approved rõ ràng.

### M6-US-03: Review signal quay ngược về system

**As a** system  
**I want** dùng dữ liệu review làm tín hiệu cải thiện generation và style profile  
**So that** output sau này phù hợp hơn với KTS và ít bị reject hơn.

**Acceptance Criteria:**
- Given review bị reject, When lưu review result, Then reject reason được cấu trúc hóa để downstream modules dùng được.
- Given có pattern reject lặp lại nhiều lần, When analytics chạy, Then flag vấn đề cho generation hoặc style profile.
- Given KTS approve nhiều version cùng kiểu, When học pattern, Then system có thể tăng trọng số cho pattern đó về sau.

---

## M7. 3D Derivation & Visual Generation

### Business purpose

Module này biến phương án 2D đã chốt thành lớp 3D và visual đủ thuyết phục để user hình dung, nhưng vẫn giữ đúng hướng đã khóa.

### Business requirements

- `BR-M7.1` 3D phải được dẫn xuất từ canonical version, không sinh tự do từ brief gốc.
- `BR-M7.2` Render exterior và interior phải bám đồng thời vào geometry và style profile.
- `BR-M7.3` Viewer model và render image phải trace được về canonical version nguồn.
- `BR-M7.4` Nếu 3D và canonical 2D mâu thuẫn, canonical 2D là nguồn thắng.
- `BR-M7.5` Module phải phục vụ cả mục tiêu trình bày cho user và review cho KTS.

### User stories

### M7-US-01: Dẫn xuất 3D từ canonical 2D

**As a** system  
**I want** dựng 3D từ canonical plan version  
**So that** 3D luôn là diễn giải của đúng phương án đã được khóa.

**Acceptance Criteria:**
- Given project có canonical version approved cho phase 3D, When run 3D derivation, Then lấy dữ liệu từ canonical version đó.
- Given 3D model được sinh, When lưu lại, Then gắn reference tới canonical version nguồn.
- Given version nguồn thay đổi, When xem 3D cũ, Then hiển thị rõ đó là 3D của version cũ.

### M7-US-02: Render 3D theo style profile

**As a** end user  
**I want** xem render 3D đúng phong cách đã chốt  
**So that** tôi hiểu không gian thực tế sẽ trông như thế nào.

**Acceptance Criteria:**
- Given canonical version và style profile đã có, When generate render, Then exterior và interior dùng cùng style language.
- Given user mở render set, When xem gallery, Then thấy ít nhất exterior và các key rooms.
- Given KTS thấy render lệch so với 2D hoặc style, When review, Then có thể request refine mà không đổi canonical source.

### M7-US-03: Viewer đọc model dẫn xuất

**As a** end user hoặc KTS  
**I want** xem model 3D nhẹ trên web  
**So that** tôi có thể quan sát phương án từ nhiều góc nhìn.

**Acceptance Criteria:**
- Given model derivation thành công, When user mở viewer, Then hiển thị model GLB/GLTF tương ứng.
- Given user thao tác orbit, zoom và floor view, When tương tác, Then viewer phản hồi mượt với model ở kích thước chấp nhận được.
- Given model và floor plan có chênh lệch, When issue được phát hiện, Then canonical 2D được xem là nguồn tham chiếu đúng.

---

## M8. Standards Export Module

### Business purpose

Module này là cầu nối từ AI output sang workflow công cụ tiêu chuẩn mà KTS và các bên triển khai thực sự dùng.

### Business requirements

- `BR-M8.1` Hệ thống phải xuất được preview package cho trình bày nhanh.
- `BR-M8.2` Hệ thống phải xuất được file 2D làm việc như SVG, DXF và PDF từ cùng một canonical version.
- `BR-M8.3` Về sau module phải mở rộng sang IFC hoặc các format BIM khác.
- `BR-M8.4` Export phải giữ traceability về source version.
- `BR-M8.5` Mọi file export phải có readiness label rõ ràng: concept, review, approved, handoff.

### User stories

### M8-US-01: Export PDF concept package

**As a** KTS hoặc PM  
**I want** export PDF concept package  
**So that** tôi có tài liệu rõ ràng để trình khách hàng hoặc chia sẻ nội bộ.

**Acceptance Criteria:**
- Given version đã approved cho trình bày, When export PDF, Then hệ thống tạo PDF package.
- Given PDF được tạo, When mở file, Then có brief summary, floor plans, render và trạng thái readiness.
- Given PDF là bản concept, When xem mỗi trang, Then có watermark phù hợp.

### M8-US-02: Export DXF cho KTS

**As a** KTS  
**I want** export DXF từ canonical version  
**So that** tôi có thể mở tiếp bằng workflow CAD quen thuộc.

**Acceptance Criteria:**
- Given canonical version đủ dữ liệu geometry, When export DXF, Then file mở được trong AutoCAD LT hoặc LibreCAD.
- Given file đã export, When xem metadata, Then biết file được sinh từ canonical version nào.
- Given geometry chưa đủ để export đúng, When export, Then hệ thống báo rõ thiếu dữ liệu gì.

### M8-US-03: Quản lý readiness label của file export

**As a** PM hoặc contractor  
**I want** biết file nào chỉ để review và file nào đủ để đi tiếp  
**So that** tôi không dùng nhầm hồ sơ chưa sẵn sàng.

**Acceptance Criteria:**
- Given bundle được export, When xem file list, Then mỗi file có readiness label.
- Given file chỉ ở mức concept, When người dùng xem, Then hiển thị rõ không dùng cho thi công.
- Given bundle đã qua review sâu hơn, When cập nhật status, Then file readiness đổi theo approval state mới.

---

## M9. Delivery & Handoff Module

### Business purpose

Module này đảm bảo hệ thống không dừng ở việc generate và review, mà thực sự kết thúc bằng một gói hồ sơ có thể bàn giao và dùng tiếp trong quy trình triển khai.

### Business requirements

- `BR-M9.1` Hệ thống phải đóng gói được bundle hồ sơ theo từng version approved.
- `BR-M9.2` Bundle phải chứa đúng tập file theo readiness level của phase đó.
- `BR-M9.3` Handoff phải có log phê duyệt, lịch sử annotate và nguồn version rõ ràng.
- `BR-M9.4` Hệ thống phải hỗ trợ bàn giao cho các nhóm khác nhau như client, KTS nội bộ, contractor.
- `BR-M9.5` Chỉ một bundle được đánh dấu là current official handoff tại một thời điểm.

### User stories

### M9-US-01: Tạo official handoff bundle

**As a** PM hoặc KTS lead  
**I want** đóng gói official handoff bundle từ một version approved  
**So that** team có đúng một bộ hồ sơ chuẩn để gửi đi.

**Acceptance Criteria:**
- Given version đã đạt điều kiện handoff, When user tạo bundle, Then hệ thống đóng gói toàn bộ file liên quan theo version đó.
- Given bundle được tạo, When mở metadata, Then biết rõ version nguồn, ngày tạo và người phê duyệt.
- Given đã có bundle cũ, When bundle mới được officialize, Then bundle mới trở thành current handoff bundle.

### M9-US-02: Bàn giao cho contractor

**As a** contractor  
**I want** nhận đúng bộ hồ sơ approved có thể dùng tiếp  
**So that** tôi có cơ sở để bóc tách và chuẩn bị triển khai.

**Acceptance Criteria:**
- Given contractor được cấp quyền xem handoff, When mở delivery workspace, Then chỉ thấy bundle approved dành cho họ.
- Given bundle có nhiều file, When tải về, Then các file được nhóm rõ theo loại.
- Given file nào còn là concept only, When contractor mở bundle, Then file đó được đánh dấu rõ.

### M9-US-03: Audit trail của việc bàn giao

**As a** PM hoặc admin  
**I want** xem lịch sử bàn giao và phê duyệt của từng bundle  
**So that** tôi có thể audit quá trình chốt hồ sơ khi cần.

**Acceptance Criteria:**
- Given nhiều lần export và handoff, When xem lịch sử bundle, Then hiển thị timeline rõ ràng.
- Given bundle bị thay thế, When xem bundle cũ, Then biết vì sao nó bị superseded.
- Given cần truy ngược, When mở bundle bất kỳ, Then xem được approval record và annotations liên quan.

---

## 4. Story Map Gợi ý

| Giai đoạn | Modules chính |
| --- | --- |
| Intake và chuẩn hóa yêu cầu | M1, M2 |
| Học phong cách KTS | M1, M3 |
| Explore phương án 2D | M3, M5 |
| Review và khóa hướng | M4, M6 |
| Dẫn xuất 3D | M4, M7 |
| Export file chuẩn | M4, M8 |
| Delivery và handoff | M8, M9 |

## 5. Gợi ý ưu tiên triển khai

### MVP bắt buộc

- M1 Experience Layer
- M2 Intake & Brief
- M4 Canonical Design State
- M5 2D Generation Engine
- M6 Review & Annotation
- M8 Standards Export ở mức PDF + SVG

### MVP+ rất nên có

- M3 Architect Style Intelligence
- M7 3D Derivation & Visual Generation
- M9 Delivery & Handoff

### Phase sau

- M8 mở rộng sang DXF mạnh hơn và IFC
- M7 nâng chất lượng model 3D và trace sâu hơn
- M3 học từ feedback lịch sử và reject pattern tốt hơn

## 6. Open Questions

1. Phase 1 có muốn coi `Architect Style Intelligence` là core requirement hay chỉ pilot cho một số KTS đầu tiên?
2. Canonical design state ở Phase 1 nên lưu geometry JSON nội bộ đến mức nào trước khi export DXF?
3. DXF có phải bắt buộc ngay ở Phase 1 hay có thể đi theo lộ trình `SVG/PDF trước, DXF sau`?
4. 3D viewer có cần là P0, hay chỉ cần render set + lightweight model ở P1?
5. Tiêu chí nào đủ để chuyển một version từ `concept approved` sang `handoff ready`?
