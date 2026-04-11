# GitHub Research – AI Architect MVP

*Tổng hợp các repository hữu ích từ session research ngày Apr 11, 2026*

---

## 1. Floor Plan Generation & Processing

### ArchGPT / Floor Plan AI
- **Repo:** https://github.com/topics/floor-plan-generation
- **Relevance:** AI-based floor plan generation từ text/image prompts
- **Use case:** Core engine cho intake → floor plan step

### FloorplanToBlender3d
- **Repo:** https://github.com/grebtsew/FloorPlanToBlender3D
- **Stars:** ~1.5k
- **Description:** Convert 2D floor plan images → Blender 3D scene tự động
- **Relevance:** Pipeline 2D → 3D render
- **License:** MIT
- **Integration:** Nhận PNG/SVG floor plan → export .blend → render

### Roomformer
- **Paper:** CVPR 2023
- **Repo:** https://github.com/ywyue/RoomFormer
- **Description:** Transformer-based room layout estimation từ point cloud
- **Relevance:** Nếu có scan 3D của căn nhà hiện tại → extract layout

---

## 2. AI Agent Frameworks

### LangGraph
- **Repo:** https://github.com/langchain-ai/langgraph
- **Stars:** ~8k+
- **Description:** Graph-based state machine cho multi-agent orchestration
- **Relevance:** Agent orchestration layer (Requirements Agent → Design Agent → Review Agent)
- **Why choose:** Explicit state management, dễ debug, supports human-in-the-loop

### AutoGen (Microsoft)
- **Repo:** https://github.com/microsoft/autogen
- **Stars:** ~30k+
- **Description:** Multi-agent conversation framework
- **Relevance:** Alternative orchestration, tốt cho multi-agent debate/review

### CrewAI
- **Repo:** https://github.com/crewAIInc/crewAI
- **Stars:** ~20k+
- **Description:** Role-based multi-agent framework
- **Relevance:** Dễ define roles (KTS_agent, client_agent, reviewer_agent)

---

## 3. 3D Visualization

### Three.js
- **Repo:** https://github.com/mrdoob/three.js
- **Stars:** ~100k+
- **Description:** WebGL 3D library
- **Relevance:** Frontend 3D viewer cho client (web-based, không cần install)

### IFC.js (Web-IFC-Viewer)
- **Repo:** https://github.com/IFCjs/web-ifc-viewer
- **Stars:** ~2k+
- **Description:** BIM viewer trong browser
- **Relevance:** Nếu muốn đẩy output sang BIM format (IFC)

### IfcOpenShell
- **Repo:** https://github.com/IfcOpenShell/IfcOpenShell
- **Stars:** ~2.5k+
- **Description:** Python library để read/write/convert IFC files
- **Relevance:** Backend integration với BIM workflow

---

## 4. Stable Diffusion & ControlNet for Architecture

### ControlNet
- **Repo:** https://github.com/lllyasviel/ControlNet
- **Stars:** ~28k+
- **Description:** Conditioning SD với structural inputs (depth, edge, pose, segmentation)
- **Relevance:** Floor plan → exterior/interior render (conditioned generation)
- **Models:** `control_v11p_sd15_mlsd` (line detection) tốt cho kiến trúc

### Stable Diffusion WebUI (AUTOMATIC1111)
- **Repo:** https://github.com/AUTOMATIC1111/stable-diffusion-webui
- **Stars:** ~140k+
- **Relevance:** API endpoint để trigger generation từ backend

### ComfyUI
- **Repo:** https://github.com/comfyanonymous/ComfyUI
- **Stars:** ~60k+
- **Description:** Node-based SD workflow
- **Relevance:** Build reproducible pipeline: floor plan → ControlNet edge → render

---

## 5. Specialized Architecture AI Tools

### Maket.ai (Commercial, closed source)
- **URL:** https://www.maket.ai
- **Description:** AI floor plan generation SaaS
- **Stars:** N/A (commercial)
- **Relevance:** Direct competitor, study their UX/flow

### Finch3D
- **URL:** https://finch3d.com
- **Description:** Generative design for multi-unit residential
- **Relevance:** B2B angle, study their go-to-market

### ChatCAD / CAD-GPT
- **Search:** https://github.com/topics/cad-generation
- **Relevance:** Text to CAD generation research

---

## 6. BIM & Construction Management

### Speckle
- **Repo:** https://github.com/specklesystems/speckle-server
- **Stars:** ~1.5k+
- **Description:** Open-source data platform cho AEC (như Dropbox cho BIM data)
- **Relevance:** Collaboration layer giữa AI output và KTS teams

### OpenBIM Components
- **Repo:** https://github.com/ThatOpen/engine_components
- **Stars:** ~700+
- **Description:** Web-based BIM components
- **Relevance:** Lightweight BIM viewer cho MVP

---

## 7. Recommended Tech Stack cho MVP

```
Layer               | Technology
--------------------|------------------------------------------
AI Orchestration    | LangGraph (agent graph) + GPT-4o / Claude
Floor Plan Gen      | Custom model or Maket.ai API (if available)
2D → 3D             | FloorPlanToBlender3D + Blender headless
Render              | ComfyUI + ControlNet (SD-based)
Backend             | FastAPI (Python) + Celery (async tasks)
Frontend            | Next.js + Three.js (3D viewer)
Database            | PostgreSQL + S3 (file storage)
Infra               | Docker + GPU server (RunPod / vast.ai)
```

---

## 8. Action Items / Next Steps

- [ ] Clone & test FloorPlanToBlender3D locally
- [ ] Set up ComfyUI with ControlNet mlsd model
- [ ] Build basic LangGraph agent: intake form → floor plan prompt → SD generation
- [ ] Research Maket.ai API availability
- [ ] Check QCVN quy chuẩn xây dựng để train validation rules
- [ ] Design database schema: project, version, design_file, feedback
