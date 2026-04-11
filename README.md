# AI Architect MVP

> AI-native platform phục vụ design nhà cửa – thay thế và hỗ trợ kiến trúc sư trong toàn bộ vòng đời dự án xây dựng.

## Vấn đề

Khách hàng có căn nhà / lô đất và muốn design lại hoàn toàn. Quy trình truyền thống:

1. Có ý tưởng cơ bản về căn nhà
2. Sắp xếp tài chính
3. Tìm kiếm kiến trúc sư phù hợp (giá, chất lượng, uy tín, phong cách, quen biết…)
4. Chốt kiến trúc sư
5. Cung cấp thông tin & nhu cầu cho kiến trúc sư (tương tác liên tục)
6. Kiến trúc sư vẽ nhiều iteration ra Version 1
7. End-user review V1, góp ý chỉnh sửa
8. Kiến trúc sư làm xuyên đêm để chỉnh theo yêu cầu
9. Loop bước 7–8 rất nhiều lần
10. Chốt bản vẽ → triển khai cho đội thi công
11. Quản lý chất lượng thi công, tiến độ, nhà thầu

**Pain points chính:**
- Chi phí kiến trúc sư cao, thời gian lâu
- Communication gap: khách hàng khó diễn đạt đúng ý, kiến trúc sư tốn nhiều vòng revision
- Thiếu visibility cho khách hàng trong quá trình thiết kế
- Quản lý thi công thủ công, dễ trễ tiến độ

## Giải pháp

Dùng **AI Agent** để thực hiện công việc của kiến trúc sư và hỗ trợ end-user từ đầu đến cuối, giúp quá trình xây dựng nhẹ nhàng hơn.

## MVP Focus

**Core loop:** Thu thập thông tin đầu vào → AI tạo bản vẽ/thiết kế draft → Kỹ sư/kiến trúc sư review & chỉnh sửa nội bộ → Trình khách hàng → Khách hàng feedback → AI update thiết kế.

→ Giảm số vòng revision với khách hàng, tăng chất lượng output mỗi lần trình bày.

## Tech Stack (Dự kiến)

- **AI Generation:** Stable Diffusion, ControlNet (floor plan → 3D render)
- **Agent Framework:** AutoGen / CrewAI / LangGraph
- **Floor Plan Processing:** ArchGPT, FloorplanToBlender3d
- **BIM Integration:** IfcOpenShell, IFC.js
- **Frontend:** Next.js + Three.js (3D viewer)
- **Backend:** FastAPI / NestJS

## Repo Structure

```
ai-architect-mvp/
├── README.md                   # Overview (file này)
├── analysis-full.md            # Phân tích product đầy đủ
├── research.md                 # Research notes chung
└── research-github-updated.md  # GitHub repos tổng hợp
```

## Status

- [x] Ý tưởng + product analysis (Apr 11, 2026)
- [x] GitHub research (Apr 11, 2026)
- [ ] PoC: AI floor plan generation pipeline
- [ ] PoC: Agent conversation flow với end-user
- [ ] Integration với BIM tools
