# Research Notes – AI Architect MVP

*Tổng hợp research ngày Apr 11, 2026*

---

## 1. Bối Cảnh Thị Trường

### Thị trường Việt Nam
- Đô thị hóa tăng nhanh (~40% năm 2023, dự kiến 50%+ năm 2030)
- Nhu cầu nhà ở phân khúc trung và cao cấp tăng
- Thiếu hụt kiến trúc sư có kinh nghiệm tại các tỉnh nhỏ
- Chi phí thiết kế kiến trúc: 2-8% tổng giá trị công trình (thường 50-300 triệu VND cho nhà phố)
- Thời gian thiết kế truyền thống: 2-6 tháng cho đến khi hoàn thiện bản vẽ thi công

### Xu hướng toàn cầu
- Generative AI trong AEC (Architecture, Engineering, Construction) đang nổi lên mạnh 2023-2025
- Autodesk đầu tư mạnh vào AI features (Autodesk AI, Forma)
- Các startup như Maket.ai, Finch3D, ARchilogic đã raise vốn đáng kể
- Thị trường AEC software toàn cầu: $10.8B (2023), dự kiến $17B+ (2028)

---

## 2. Competitive Landscape

| Tool | Focus | Strengths | Weaknesses |
|------|-------|-----------|------------|
| Midjourney/Dall-E | Image gen | Beautiful renders | Không scale, không floor plan |
| Maket.ai | Floor plan gen | AI-native, VC-backed | Chưa có tại VN, English only |
| ARchilogic | 3D floor plan | Good UX | Không có AI gen |
| Autodesk Forma | BIM + AI | Enterprise-grade | Quá phức tạp, đắt |
| Planner 5D | DIY design | Easy UX, affordable | Limited AI, B2C only |
| SketchUp + AI plugins | 3D modeling | Familiar to pros | Steep learning curve |

**Opportunity gap:** Không có tool nào phục vụ đúng segment **SME design firm tại SEA** với **AI-native workflow + local context**.

---

## 3. Workflow hiện tại của KTS

```
Client Brief → Site Survey → Concept Sketches → Schematic Design 
→ Design Development → Construction Documents → Bidding → Construction Admin
```

**AI có thể automate mạnh nhất:** Concept Sketches → Schematic Design → early Design Development

---

## 4. Key Challenges kỹ thuật

- **Floor plan generation:** Cần hiểu spatial constraints (load-bearing walls, circulation, natural light)
- **Code compliance:** Quy chuẩn QCVN 03/2012, TCXD 323:2004 (Việt Nam) – AI cần được trained
- **3D from 2D:** ControlNet + depth-to-3D pipeline còn nhiều artifact
- **User intent extraction:** "Tôi muốn nhà thoáng, hiện đại, có vườn" → precise design parameters
