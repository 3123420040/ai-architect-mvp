# Phân Tích Đầy Đủ – AI Architect MVP

*Tổng hợp từ session nghiên cứu & phân biện ngày Apr 11, 2026*

---

## 1. Ý Tưởng Cốt Lõi

Xây dựng nền tảng AI-native phục vụ thiết kế nhà cửa. AI Agent đóng vai trò kiến trúc sư ảo, hỗ trợ end-user từ bước đầu lên ý tưởng đến khi bàn giao công trình.

---

## 2. Phân Tích SWOT

### Strengths
- **Rào cản chi phí thấp hơn:** Khách hàng không cần thuê kiến trúc sư đắt tiền cho giai đoạn concept
- **Tốc độ:** AI tạo draft nhanh, giảm thời gian revision từ nhiều ngày xuống còn giờ/phút
- **24/7 availability:** Không bị hạn chế giờ làm việc
- **Consistent quality:** Output có thể standardize và reproduce
- **Data flywheel:** Mỗi project là training data cho model tiếp theo

### Weaknesses
- **Hallucination trong thiết kế kỹ thuật:** AI có thể tạo design đẹp nhưng không khả thi về mặt kỹ thuật (kết cấu, điện, nước)
- **Local context hạn chế:** AI chưa hiểu rõ quy chuẩn xây dựng địa phương (Việt Nam, từng tỉnh thành)
- **Trust gap:** Khách hàng Việt Nam quen tin tưởng kiến trúc sư con người
- **3D generation chất lượng:** Hiện tại SOTA vẫn cần human touch-up cho output professional

### Opportunities
- **Thị trường VN growing:** Đô thị hóa mạnh, nhu cầu nhà ở tăng, tầng lớp trung lưu mở rộng
- **Thiếu kiến trúc sư qualified:** Số lượng KTS giỏi có hạn, demand vượt supply
- **AI tooling mature nhanh:** ControlNet, ArchGPT, các model 3D đang tiến bộ nhanh
- **B2B angle:** Bán tool cho công ty thiết kế để tăng throughput

### Threats
- **Competition từ global tools:** Autodesk AI, Midjourney, Dall-E cho interior design
- **Regulatory risk:** Quy chuẩn pháp lý về AI trong xây dựng chưa rõ
- **Liability:** Ai chịu trách nhiệm khi AI design dẫn đến lỗi kết cấu?

---

## 3. User Personas

### Persona 1: Chủ nhà tự xây (Anh Minh, 38 tuổi, HCM)
- Có lô đất 80m², muốn xây nhà phố 5 tầng
- Budget: 2-3 tỷ VND
- Pain: Không biết tìm KTS ở đâu, sợ bị "hét giá", muốn thấy hình ảnh trước khi quyết định
- Expectation: Chat với AI, đưa yêu cầu, nhận 3D render trong vài phút

### Persona 2: Công ty thiết kế nhỏ (5-10 nhân sự)
- Muốn tăng capacity mà không thuê thêm người
- Dùng AI để tạo draft nhanh, KTS review và finalize
- ROI: Giảm 60-70% thời gian làm bản vẽ concept

### Persona 3: Developer bất động sản
- Cần thiết kế nhiều căn hộ/unit với biến thể khác nhau
- Muốn customize nhanh theo từng lô đất

---

## 4. MVP Scope

### In Scope (Phase 1)
- [ ] **Intake form:** Thu thập thông tin lô đất, budget, style preference, số phòng, lifestyle
- [ ] **AI floor plan generation:** Từ text + kích thước đất → 2D floor plan
- [ ] **3D visualization:** Floor plan → 3D render (exterior + interior key rooms)
- [ ] **Revision loop:** User feedback → AI adjusts design
- [ ] **Export:** PDF bản vẽ sơ bộ, hình ảnh 3D

### Out of Scope (Phase 1)
- Bản vẽ thi công (cần KTS licensed)
- Tính toán kết cấu, MEP (điện, nước, HVAC)
- Quản lý thi công
- Tích hợp nhà thầu/vật liệu

---

## 5. Architecture Overview

```
User Input Layer
  └── Chat interface (text + image upload)
  └── Structured form (lot dimensions, preferences)

AI Processing Layer
  └── Agent Orchestrator (LangGraph / AutoGen)
      ├── Requirements Agent: Extract & clarify requirements
      ├── Design Agent: Generate floor plan + 3D
      ├── Review Agent: Check feasibility, highlight issues
      └── Revision Agent: Apply user feedback to design

Output Layer
  └── 2D Floor Plan (vector/raster)
  └── 3D Render (exterior, interior)
  └── Summary report (PDF)

Human Review Gate
  └── KTS review queue
  └── Approval before delivery to client
```

---

## 6. Phản Biện & Rủi Ro

### "AI không thể thay KTS"
**Counter:** MVP không nhằm thay KTS hoàn toàn. Mục tiêu là automate 70-80% công việc lặp lại (drafting, revision, visualization), để KTS focus vào judgment calls và client relationship.

### "Chất lượng output AI chưa đủ professional"
**Counter:** Đúng cho bản vẽ thi công. Nhưng cho giai đoạn concept/visualization là đủ, và đây là pain point lớn nhất (client cần thấy hình ảnh nhanh để quyết định).

### "Ai sẽ chịu trách nhiệm pháp lý?"
**Counter:** Output của AI là "concept design" – không phải "bản vẽ thi công" (cần KTS licensed ký). Model rõ ràng từ đầu.

### "Market education khó"
**Counter:** Bắt đầu B2B (sell to design firms) thay vì B2C. Thay đổi behavior của công ty dễ hơn end-user.

---

## 7. Go-to-Market

1. **Phase 1 (0-6 tháng):** Closed beta với 5-10 công ty thiết kế ở HCM/HN
2. **Phase 2 (6-12 tháng):** B2B SaaS, pricing per project hoặc subscription
3. **Phase 3 (12-24 tháng):** Mở B2C với freemium model
4. **Phase 4:** Marketplace (kết nối với KTS, nhà thầu, vật liệu)

---

## 8. Metrics MVP

- Time-to-first-concept: < 10 phút từ khi user nhập yêu cầu
- Revision cycles: < 3 vòng để đạt client approval
- NPS từ beta users: > 40
- % design được KTS approve mà không cần major rework: > 60%
