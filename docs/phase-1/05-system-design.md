# Phase 1 – System Design: AI Architect as Agentic OS

*Ngày tạo: Apr 11, 2026*
*Input: 04-module-business-requirements.md + 03-agentic-os-architecture.md*

---

## 1. Module → Pipeline Mapping

9 business modules không map 1:1 vào 6 Agentic OS pipelines. Chúng **xuyên suốt** nhiều pipelines:

```
                         6 AGENTIC OS PIPELINES
         ┌──────┬──────┬──────┬──────┬──────┬──────┐
         │  P1  │  P2  │  P3  │  P4  │  P5  │  P6  │
         │Client│Query │ Tool │Multi │ Ctx  │Perm &│
         │  UI  │ Loop │Orch. │Agent │ Mgmt │ Sec  │
         ├──────┼──────┼──────┼──────┼──────┼──────┤
 M1 Exp  │██████│      │      │      │      │██████│  UI + Permission
 M2 Intk │██████│██████│██████│██████│      │      │  Full pipeline
 M3 Style│      │██████│██████│██████│██████│      │  Intelligence
 M4 Canon│      │      │██████│      │██████│██████│  State + Security
 M5 2DGen│      │██████│██████│██████│██████│      │  Core generation
 M6 Revw │██████│██████│██████│      │      │██████│  Review gate
 M7 3DDer│██████│██████│██████│██████│██████│      │  Derivation
 M8 Exprt│      │██████│██████│      │      │██████│  Export pipeline
 M9 Deliv│██████│      │      │      │      │██████│  Handoff
         └──────┴──────┴──────┴──────┴──────┴──────┘

 ██ = Module sử dụng pipeline đó
```

---

## 2. High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        EXPERIENCE LAYER (M1)                            │
│  ┌─────────────┐ ┌──────────────┐ ┌────────────┐ ┌────────────────┐   │
│  │ End-User    │ │ KTS Review   │ │ Admin      │ │ Delivery       │   │
│  │ Workspace   │ │ Workspace    │ │ Dashboard  │ │ Workspace      │   │
│  │             │ │              │ │            │ │ (Contractor)   │   │
│  │ • Gallery   │ │ • Annotate   │ │ • Team     │ │ • Bundles      │   │
│  │ • Chat      │ │ • Compare    │ │ • Style    │ │ • Download     │   │
│  │ • 3D Viewer │ │ • Approve    │ │ • Projects │ │ • Audit trail  │   │
│  └──────┬──────┘ └──────┬───────┘ └─────┬──────┘ └───────┬────────┘   │
│         │               │               │                │             │
│         └───────────────┴───────┬───────┴────────────────┘             │
│                                 │ WebSocket + REST API                  │
├─────────────────────────────────┼───────────────────────────────────────┤
│                                 │                                       │
│  ┌──────────────────────────────▼──────────────────────────────────┐   │
│  │                    AGENTIC ENGINE (Backend)                      │   │
│  │                                                                  │   │
│  │  ┌─── P2: QUERY LOOP ──────────────────────────────────────┐    │   │
│  │  │  while(true) {                                           │    │   │
│  │  │    Phase 1: Context Assembly                             │    │   │
│  │  │      ├── Design Brief (M2)                               │    │   │
│  │  │      ├── Style Profile (M3)                              │    │   │
│  │  │      ├── Canonical State (M4)                            │    │   │
│  │  │      └── Project Memory (P5)                             │    │   │
│  │  │                                                          │    │   │
│  │  │    Phase 2: LLM API Call (streaming)                     │    │   │
│  │  │      └── yield chunks → WebSocket → Frontend             │    │   │
│  │  │                                                          │    │   │
│  │  │    Phase 3: Tool Execution ─────────────────────┐        │    │   │
│  │  │      ├── M2 Tools: BriefParse, BriefUpdate      │        │    │   │
│  │  │      ├── M3 Tools: StyleResolve, StyleSearch     ├── P3  │    │   │
│  │  │      ├── M5 Tools: FloorPlanGenerate            │        │    │   │
│  │  │      ├── M7 Tools: Render3D, ModelDerive        │        │    │   │
│  │  │      └── M8 Tools: ExportPDF, ExportDXF         │        │    │   │
│  │  │                                          ───────┘        │    │   │
│  │  │    Phase 4: Stop or Continue                             │    │   │
│  │  │      └── needsFollowUp? → loop or exit                  │    │   │
│  │  │  }                                                       │    │   │
│  │  └──────────────────────────────────────────────────────────┘    │   │
│  │                                                                  │   │
│  │  ┌─── P4: MULTI-AGENT ─────────────────────────────────────┐    │   │
│  │  │  Coordinator (restricted: AssignTask, SendFeedback)      │    │   │
│  │  │    ├── Requirements Agent (M2)                           │    │   │
│  │  │    ├── Design Agent (M3+M5)                              │    │   │
│  │  │    ├── Review Agent (M6) [READ-ONLY]                     │    │   │
│  │  │    └── Revision Agent (M5+M6)                            │    │   │
│  │  └──────────────────────────────────────────────────────────┘    │   │
│  │                                                                  │   │
│  │  ┌─── P6: PERMISSION & REVIEW GATE ────────────────────────┐    │   │
│  │  │  KTS Approval State Machine (M4+M6)                      │    │   │
│  │  │  Role-based access (M1)                                   │    │   │
│  │  │  Generation budget (M5+M7)                                │    │   │
│  │  │  Audit trail (M9)                                         │    │   │
│  │  └──────────────────────────────────────────────────────────┘    │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                  DATA & STATE LAYER                               │   │
│  │  ┌──────────┐ ┌──────────────┐ ┌──────────┐ ┌────────────────┐  │   │
│  │  │PostgreSQL│ │  S3 / MinIO  │ │  Redis   │ │ Canonical      │  │   │
│  │  │          │ │              │ │          │ │ Design State   │  │   │
│  │  │ Projects │ │ Floor plans  │ │ Queue    │ │ (M4)           │  │   │
│  │  │ Users    │ │ 3D renders   │ │ Cache    │ │                │  │   │
│  │  │ Versions │ │ Exports      │ │ Sessions │ │ Brief+Geometry │  │   │
│  │  │ Reviews  │ │ Style assets │ │ PubSub   │ │ +Style+Review  │  │   │
│  │  │ Feedback │ │ Bundles      │ │          │ │ +Lineage       │  │   │
│  │  └──────────┘ └──────────────┘ └──────────┘ └────────────────┘  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │              GPU SERVICE (ai-architect-gpu)                       │   │
│  │  ComfyUI + Diffusers + ControlNet + Blender headless             │   │
│  │  [FloorPlan Pipeline] [Render Pipeline] [Model Pipeline]         │   │
│  └──────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Canonical Design State (M4) — Trung tâm sự thật

M4 là module quan trọng nhất về mặt kiến trúc. Mọi module khác tham chiếu đến nó.

```
                    CANONICAL DESIGN STATE (M4)
                    ═══════════════════════════
                    
┌─────────────────────────────────────────────────────────────┐
│                  Canonical Plan Version                       │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │ Design Brief │  │   Geometry   │  │  Style Profile   │  │
│  │ (M2 output)  │  │  (M5 output) │  │  (M3 resolved)   │  │
│  │              │  │              │  │                   │  │
│  │ • lot dims   │  │ • walls      │  │ • KTS profile ver │  │
│  │ • rooms      │  │ • rooms      │  │ • resolved params │  │
│  │ • style pref │  │ • dimensions │  │ • brief overrides │  │
│  │ • budget     │  │ • openings   │  │                   │  │
│  │ • lifestyle  │  │ • stairs     │  │                   │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │ Review State │  │   Lineage    │  │  Derived Assets  │  │
│  │ (M6 output)  │  │              │  │                   │  │
│  │              │  │ • parent_ver │  │ • floor_plan_urls │  │
│  │ • status     │  │ • change_log │  │ • render_urls     │  │
│  │ • reviewer   │  │ • feedback   │  │ • model_url       │  │
│  │ • annotations│  │ • created_at │  │ • export_urls     │  │
│  │ • approved_at│  │              │  │ • bundle_id       │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘

VERSION STATE MACHINE:
                                                                    
  [draft] ──gen──→ [generated] ──submit──→ [under_review]          
                        │                       │                   
                   ┌────┘                  ┌────┼────────┐          
                   │                       │             │          
              [superseded]           [approved]    [rejected]       
                                         │             │           
                                    [locked] ←──revise──┘          
                                         │                         
                                  [handoff_ready]                   
                                         │                         
                                   [delivered]                      
                                                                    
  RULES:                                                           
  • locked = immutable. Canonical truth.                           
  • 3D, export, bundle ONLY read from locked versions              
  • rejected → creates new draft (lineage preserved)               
  • superseded = old version replaced by new locked version        
  • handoff_ready requires: locked + KTS approved + exports done   
```

---

## 4. Sequence Diagrams — Use Cases Chi Tiết

### 4.1 UC-01: End-to-End — Từ Intake đến First 2D Options

```
 End User          Frontend(M1)       API Gateway       Query Loop(P2)     Req Agent(M2)     Design Agent(M5)     GPU Service
    │                   │                  │                  │                  │                  │                  │
    │  "Tôi muốn xây   │                  │                  │                  │                  │                  │
    │   nhà 5x20m"     │                  │                  │                  │                  │                  │
    ├──────────────────►│                  │                  │                  │                  │                  │
    │                   │ POST /projects   │                  │                  │                  │                  │
    │                   ├─────────────────►│                  │                  │                  │                  │
    │                   │                  │ create project   │                  │                  │                  │
    │                   │                  ├─────────────────►│                  │                  │                  │
    │                   │                  │                  │                  │                  │                  │
    │                   │◄─────── WS: "Xin chào! Cho tôi biết thêm..." ────────│                  │                  │
    │◄──────────────────│                  │                  │                  │                  │                  │
    │                   │                  │                  │                  │                  │                  │
    │  "4 tầng, 3PN,   │                  │                  │                  │                  │                  │
    │   modern, 2.5 tỷ" │                  │                  │                  │                  │                  │
    ├──────────────────►│                  │                  │                  │                  │                  │
    │                   │ WS: user message │                  │                  │                  │                  │
    │                   ├─────────────────►│                  │                  │                  │                  │
    │                   │                  │                  │ ── PHASE 2 ──►  │                  │                  │
    │                   │                  │                  │ LLM: "extract   │                  │                  │
    │                   │                  │                  │  requirements"  │                  │                  │
    │                   │                  │                  │                  │                  │                  │
    │                   │                  │                  │ ── PHASE 3 ──►  │                  │                  │
    │                   │                  │                  │ tool_use:        │                  │                  │
    │                   │                  │                  │ BriefParse()    │                  │                  │
    │                   │                  │                  ├─────────────────►│                  │                  │
    │                   │                  │                  │                  │ parse input      │                  │
    │                   │                  │                  │                  │ detect missing:  │                  │
    │                   │                  │                  │                  │ "hướng mặt tiền?"│                  │
    │                   │                  │                  │◄─────────────────┤                  │                  │
    │                   │                  │                  │                  │                  │                  │
    │                   │                  │                  │ ── PHASE 4 ──   │                  │                  │
    │                   │                  │                  │ needsFollowUp   │                  │                  │
    │                   │                  │                  │ = true (missing  │                  │                  │
    │                   │                  │                  │  info detected)  │                  │                  │
    │                   │                  │                  │                  │                  │                  │
    │                   │◄─── WS: "Hướng mặt tiền nhà bạn quay về đâu?" ───────│                  │                  │
    │◄──────────────────│                  │                  │                  │                  │                  │
    │                   │                  │                  │                  │                  │                  │
    │  "Hướng Nam"      │                  │                  │                  │                  │                  │
    ├──────────────────►│ ─────────────────────────────────► │                  │                  │                  │
    │                   │                  │                  │ ── PHASE 3 ──►  │                  │                  │
    │                   │                  │                  │ tool_use:        │                  │                  │
    │                   │                  │                  │ BriefUpdate()   │                  │                  │
    │                   │                  │                  ├─────────────────►│                  │                  │
    │                   │                  │                  │                  │ DesignBrief JSON │                  │
    │                   │                  │                  │                  │ complete!        │                  │
    │                   │                  │                  │◄─────────────────┤                  │                  │
    │                   │                  │                  │                  │                  │                  │
    │                   │◄─── WS: "Brief hoàn tất. Bạn xác nhận?" ─────────────│                  │                  │
    │◄──────────────────│                  │                  │                  │                  │                  │
    │                   │                  │                  │                  │                  │                  │
    │  "Xác nhận,       │                  │                  │                  │                  │                  │
    │   generate đi"    │                  │                  │                  │                  │                  │
    ├──────────────────►│ ─────────────────────────────────► │                  │                  │                  │
    │                   │                  │                  │ ── PHASE 2 ──►  │                  │                  │
    │                   │                  │                  │ LLM decides:     │                  │                  │
    │                   │                  │                  │ "generate 2D"    │                  │                  │
    │                   │                  │                  │                  │                  │                  │
    │                   │                  │                  │ ── PHASE 3 ──►  │                  │                  │
    │                   │                  │                  │ tool_use:        │                  │                  │
    │                   │                  │                  │ StyleResolve()  │  (CONCURRENT)    │                  │
    │                   │                  │                  │ BuildingCode()  │  ◄── batch 1     │                  │
    │                   │                  │                  │                  │                  │                  │
    │                   │                  │                  │ tool_use:        │                  │                  │
    │                   │                  │                  │ FloorPlanGen()  │  (EXCLUSIVE)     │                  │
    │                   │                  │                  │                  ├─────────────────►│                  │
    │                   │                  │                  │                  │                  ├─────────────────►│
    │                   │◄─── WS: progress "Đang tạo mặt bằng... 30%" ─────────│                  │     GPU work     │
    │◄──────────────────│                  │                  │                  │                  │                  │
    │                   │◄─── WS: progress "Đang tạo mặt bằng... 70%" ─────────│                  │                  │
    │                   │                  │                  │                  │                  │◄─────────────────┤
    │                   │                  │                  │                  │◄─────────────────┤  3 options done  │
    │                   │                  │                  │◄─── context_modifier: floor_plan_urls ──┤              │
    │                   │                  │                  │                  │                  │                  │
    │                   │                  │                  │ ── PHASE 4 ──   │                  │                  │
    │                   │                  │                  │ needsFollowUp   │                  │                  │
    │                   │                  │                  │ = false          │                  │                  │
    │                   │                  │                  │ → COMPLETED      │                  │                  │
    │                   │                  │                  │                  │                  │                  │
    │                   │◄─── WS: "3 phương án đã sẵn sàng!" ──────────────────│                  │                  │
    │◄──────────────────│                  │                  │                  │                  │                  │
    │                   │                  │                  │                  │                  │                  │
    │  Xem gallery      │                  │                  │                  │                  │                  │
    ├──────────────────►│ GET /designs     │                  │                  │                  │                  │
    │                   ├─────────────────►│                  │                  │                  │                  │
    │                   │◄─── 3 options ───┤                  │                  │                  │                  │
    │◄── Gallery view ──│                  │                  │                  │                  │                  │
    │                   │                  │                  │                  │                  │                  │
```

---

### 4.2 UC-02: KTS Review → Approve → Lock thành Canonical Version

```
     KTS              Frontend(M1)     API Gateway      Permission(P6)    Canonical(M4)     Style Intel(M3)
      │                   │                │                  │                │                │
      │ Mở Review Queue   │                │                  │                │                │
      ├──────────────────►│                │                  │                │                │
      │                   │ GET /reviews   │                  │                │                │
      │                   ├───────────────►│                  │                │                │
      │                   │                │ check role       │                │                │
      │                   │                ├─────────────────►│                │                │
      │                   │                │                  │ role=architect  │                │
      │                   │                │◄── ALLOW ────────┤                │                │
      │                   │◄── queue ──────┤                  │                │                │
      │◄── Review queue ──│                │                  │                │                │
      │                   │                │                  │                │                │
      │ Mở version V2     │                │                  │                │                │
      ├──────────────────►│                │                  │                │                │
      │                   │ GET /versions  │                  │                │                │
      │                   │ /{ver_id}      │                  │                │                │
      │                   ├───────────────►│                  │                │                │
      │                   │◄── version ────┤ (brief + floor   │                │                │
      │                   │                │  plan + renders)  │                │                │
      │◄── Review view ───│                │                  │                │                │
      │                   │                │                  │                │                │
      │ Annotate: "Cửa    │                │                  │                │                │
      │ sổ ở đây bị       │                │                  │                │                │
      │ hướng Tây"        │                │                  │                │                │
      ├──────────────────►│                │                  │                │                │
      │                   │ POST /annotate │                  │                │                │
      │                   ├───────────────►│                  │                │                │
      │                   │                │ save annotation  │                │                │
      │                   │                │ bound to version │                │                │
      │                   │◄── saved ──────┤                  │                │                │
      │◄── Annotation ────│                │                  │                │                │
      │    pinned on plan  │                │                  │                │                │
      │                   │                │                  │                │                │
      │ Click "Approve"   │                │                  │                │                │
      ├──────────────────►│                │                  │                │                │
      │                   │ POST /reviews  │                  │                │                │
      │                   │ /{ver}/approve │                  │                │                │
      │                   ├───────────────►│                  │                │                │
      │                   │                │ Permission check │                │                │
      │                   │                ├─────────────────►│                │                │
      │                   │                │                  │ classify:       │                │
      │                   │                │                  │ approve_design  │                │
      │                   │                │                  │ → ALLOW (KTS)   │                │
      │                   │                │◄── ALLOW ────────┤                │                │
      │                   │                │                  │                │                │
      │                   │                │ ═══ STATE TRANSITION ═══          │                │
      │                   │                │                  │                │                │
      │                   │                │ version.status   │                │                │
      │                   │                │ under_review     │                │                │
      │                   │                │ → approved       │                │                │
      │                   │                │                  │                │                │
      │                   │                │ ═══ LOCK AS CANONICAL ═══        │                │
      │                   │                │                  │                │                │
      │                   │                │ create Canonical │                │                │
      │                   │                │ Plan Version ────┼───────────────►│                │
      │                   │                │                  │                │ snapshot:       │
      │                   │                │                  │                │ • brief         │
      │                   │                │                  │                │ • geometry      │
      │                   │                │                  │                │ • review state  │
      │                   │                │                  │                │ • derived refs  │
      │                   │                │                  │                │                │
      │                   │                │ feed approval ───┼───────────────┼───────────────►│
      │                   │                │ signal to Style  │                │                │ record:
      │                   │                │ Intelligence     │                │                │ "KTS approved
      │                   │                │                  │                │                │  this pattern"
      │                   │                │                  │                │                │ → strengthen
      │                   │                │                  │                │                │   style weight
      │                   │                │                  │                │                │
      │                   │◄── approved ───┤                  │                │                │
      │◄── "V2 Approved   │                │                  │                │                │
      │     & Locked" ─────│                │                  │                │                │
      │                   │                │                  │                │                │
```

---

### 4.3 UC-03: 3D Derivation từ Canonical Version (M7)

```
     User/KTS          Frontend(M1)     Query Loop(P2)    Tool Orch(P3)    Canonical(M4)     GPU Service
      │                   │                │                  │                │                │
      │ "Tạo 3D cho V2"  │                │                  │                │                │
      ├──────────────────►│                │                  │                │                │
      │                   │ POST /3d       │                  │                │                │
      │                   │ /{ver_id}      │                  │                │                │
      │                   ├───────────────►│                  │                │                │
      │                   │                │                  │                │                │
      │                   │                │ === PHASE 1: Context Assembly === │                │
      │                   │                │                  │                │                │
      │                   │                │ Load canonical ──┼───────────────►│                │
      │                   │                │ version data     │                │ return:        │
      │                   │                │                  │                │ brief+geometry │
      │                   │                │◄─────────────────┼────────────────┤ +style+status  │
      │                   │                │                  │                │                │
      │                   │                │ VALIDATE: status │                │                │
      │                   │                │ must be "locked" │                │                │
      │                   │                │ ✓ OK             │                │                │
      │                   │                │                  │                │                │
      │                   │                │ === PHASE 2: LLM decides tools ══│                │
      │                   │                │                  │                │                │
      │                   │                │ LLM: "derive 3D  │                │                │
      │                   │                │ model + renders  │                │                │
      │                   │                │ from canonical"  │                │                │
      │                   │                │                  │                │                │
      │                   │                │ === PHASE 3: Tool Execution ═════│                │
      │                   │                │                  │                │                │
      │                   │                │ tool_use batch:  │                │                │
      │                   │                ├─────────────────►│                │                │
      │                   │                │                  │                │                │
      │                   │                │                  │ PARTITION:      │                │
      │                   │                │                  │ ┌──────────────┤                │
      │                   │                │                  │ │Batch 1 (EXCL)│                │
      │                   │                │                  │ │ModelDerive() │                │
      │                   │                │                  │ └──────┬───────┤                │
      │                   │                │                  │        │       │                │
      │                   │                │                  │        ├───────┼───────────────►│
      │                   │                │                  │        │       │  Blender:       │
      │                   │                │                  │        │       │  floor plan     │
      │◄─── WS: "Đang dựng mô hình 3D..." │                  │        │       │  → 3D model    │
      │                   │                │                  │        │       │  → GLTF export  │
      │                   │                │                  │        │       │◄────────────────┤
      │                   │                │                  │        │       │                │
      │                   │                │                  │ context_modifier:               │
      │                   │                │                  │ model_url = "s3://...gltf"      │
      │                   │                │                  │                │                │
      │                   │                │                  │ ┌──────────────┤                │
      │                   │                │                  │ │Batch 2 (EXCL)│                │
      │                   │                │                  │ │Render3D()    │ (uses model_url│
      │                   │                │                  │ │  exterior    │  from context)  │
      │                   │                │                  │ └──────┬───────┤                │
      │                   │                │                  │        ├───────┼───────────────►│
      │                   │                │                  │        │       │  ControlNet:   │
      │◄─── WS: "Đang render exterior..." ─┤                  │        │       │  depth map     │
      │                   │                │                  │        │       │  + style prompt │
      │                   │                │                  │        │       │  → render      │
      │                   │                │                  │        │       │◄────────────────┤
      │                   │                │                  │                │                │
      │                   │                │                  │ ┌──────────────┤                │
      │                   │                │                  │ │Batch 3 (EXCL)│                │
      │                   │                │                  │ │Render3D()    │                │
      │                   │                │                  │ │  interior×3  │                │
      │                   │                │                  │ └──────┬───────┤                │
      │                   │                │                  │        ├───────┼───────────────►│
      │◄─── WS: "Đang render nội thất..." ─┤                  │        │       │  3 rooms       │
      │                   │                │                  │        │       │◄────────────────┤
      │                   │                │                  │                │                │
      │                   │                │ === PHASE 4: COMPLETED ══════════│                │
      │                   │                │                  │                │                │
      │                   │                │ Save derived     │                │                │
      │                   │                │ assets → M4 ─────┼───────────────►│                │
      │                   │                │                  │                │ link:          │
      │                   │                │                  │                │ canonical_v2   │
      │                   │                │                  │                │ → model.gltf   │
      │                   │                │                  │                │ → exterior.png │
      │                   │                │                  │                │ → interior×3   │
      │                   │                │                  │                │                │
      │◄─── WS: "3D hoàn tất! Mở viewer?" │                  │                │                │
      │                   │                │                  │                │                │
      │ Mở 3D Viewer      │                │                  │                │                │
      ├──────────────────►│                │                  │                │                │
      │                   │ Load GLTF      │                  │                │                │
      │◄── Three.js       │ from S3 URL    │                  │                │                │
      │    3D model ───────│                │                  │                │                │
      │                   │                │                  │                │                │
```

---

### 4.4 UC-04: Client Feedback → Revision Loop (M5+M6)

```
   Client           Frontend(M1)     Query Loop(P2)    Revision Agent     Canonical(M4)     GPU Service
     │                  │                │                  │                │                │
     │ Mở share link    │                │                  │                │                │
     ├─────────────────►│                │                  │                │                │
     │                  │ GET /share     │                  │                │                │
     │                  │ /{token}       │                  │                │                │
     │                  ├───────────────►│                  │                │                │
     │                  │                │ Permission(P6):  │                │                │
     │                  │                │ role=client       │                │                │
     │                  │                │ → read_only       │                │                │
     │                  │◄── designs ────┤                  │                │                │
     │◄── Gallery +     │                │                  │                │                │
     │    3D renders ───│                │                  │                │                │
     │                  │                │                  │                │                │
     │ "Muốn phòng      │                │                  │                │                │
     │  khách rộng hơn,  │                │                  │                │                │
     │  bớt 1 PN tầng 2" │                │                  │                │                │
     ├─────────────────►│                │                  │                │                │
     │                  │ POST /feedback │                  │                │                │
     │                  ├───────────────►│                  │                │                │
     │                  │                │ Save feedback    │                │                │
     │                  │                │ bound to version │                │                │
     │                  │                │                  │                │                │
     │                  │◄── "Đã ghi ────┤                  │                │                │
     │◄── "Cảm ơn!      │  nhận"         │                  │                │                │
     │   KTS sẽ xem     │                │                  │                │                │
     │   feedback"  ─────│                │                  │                │                │
     │                  │                │                  │                │                │
     │                  │   ═══ NOTIFICATION TO KTS ═══     │                │                │
     │                  │                │                  │                │                │
     │                  │                │                  │                │                │
     │                  │                │                  │                │                │

   KTS              Frontend(M1)     Query Loop(P2)    Revision Agent     Canonical(M4)     GPU Service
     │                  │                │                  │                │                │
     │◄── Notification: │                │                  │                │                │
     │  "Client feedback │                │                  │                │                │
     │   on Project X"  │                │                  │                │                │
     │                  │                │                  │                │                │
     │ Click "AI Revise" │                │                  │                │                │
     ├─────────────────►│                │                  │                │                │
     │                  │ POST /revise   │                  │                │                │
     │                  │ /{ver_id}      │                  │                │                │
     │                  ├───────────────►│                  │                │                │
     │                  │                │                  │                │                │
     │                  │                │ === CONTEXT ASSEMBLY ═══════════ │                │
     │                  │                │                  │                │                │
     │                  │                │ Load:            │                │                │
     │                  │                │ • canonical V2 ──┼───────────────►│                │
     │                  │                │ • client feedback│                │◄───────────────┤
     │                  │                │ • style profile  │                │                │
     │                  │                │ • project memory │                │                │
     │                  │                │                  │                │                │
     │                  │                │ === LLM + REVISION AGENT ════════│                │
     │                  │                │                  │                │                │
     │                  │                │ Spawn Revision ──►                │                │
     │                  │                │ Agent (Pattern A) │                │                │
     │                  │                │                  │                │                │
     │                  │                │                  │ 1. Map feedback │                │
     │                  │                │                  │    to structured│                │
     │                  │                │                  │    changes:     │                │
     │                  │                │                  │    "living_room │                │
     │                  │                │                  │     +30%,       │                │
     │                  │                │                  │     bedrooms    │                │
     │                  │                │                  │     floor2: 3→2"│                │
     │                  │                │                  │                │                │
     │                  │                │                  │ 2. Update brief │                │
     │                  │                │                  │    (BR-M5.4:    │                │
     │                  │                │                  │    structured   │                │
     │                  │                │                  │    feedback)    │                │
     │                  │                │                  │                │                │
     │                  │                │                  │ 3. FloorPlan   │                │
     │                  │                │                  │    Generate() ──┼───────────────►│
     │◄── WS: "Đang tạo phương án mới dựa trên feedback..." │               │  GPU: generate │
     │                  │                │                  │                │◄────────────────┤
     │                  │                │                  │                │                │
     │                  │                │                  │ 4. Save as V3  │                │
     │                  │                │                  │    parent=V2 ──►│                │
     │                  │                │                  │    status=      │ V3 created     │
     │                  │                │                  │    generated    │ lineage: V2→V3 │
     │                  │                │                  │                │                │
     │                  │                │◄── result ────────┤                │                │
     │                  │                │                  │                │                │
     │◄── WS: "Phương án V3 đã sẵn sàng. So sánh V2 vs V3?" │              │                │
     │                  │                │                  │                │                │
     │ Click "Compare"  │                │                  │                │                │
     ├─────────────────►│                │                  │                │                │
     │                  │ GET /compare   │                  │                │                │
     │                  │ ?v1=V2&v2=V3   │                  │                │                │
     │                  ├───────────────►│                  │                │                │
     │                  │◄── diff data ──┤                  │                │                │
     │◄── Side-by-side  │                │                  │                │                │
     │    comparison ───│                │                  │                │                │
     │  "Living room:   │                │                  │                │                │
     │   12m² → 16m²    │                │                  │                │                │
     │   Bedrooms F2:   │                │                  │                │                │
     │   3 → 2"         │                │                  │                │                │
     │                  │                │                  │                │                │
```

---

### 4.5 UC-05: Style Intelligence — Import → Learn → Apply (M3)

```
  KTS/Admin         Frontend(M1)     API Gateway       Style Agent(M3)     Design Agent      GPU Service
     │                  │                │                  │                │                │
     │ Upload portfolio │                │                  │                │                │
     │ (20 past designs)│                │                  │                │                │
     ├─────────────────►│                │                  │                │                │
     │                  │ POST /styles   │                  │                │                │
     │                  │ /import        │                  │                │                │
     │                  │ [files×20]     │                  │                │                │
     │                  ├───────────────►│                  │                │                │
     │                  │                │                  │                │                │
     │                  │                │ ═══ BACKGROUND TASK: Style Ingestion ═══          │
     │                  │                │                  │                │                │
     │                  │                │ Create task ─────►│                │                │
     │                  │                │ (local_agent)     │                │                │
     │                  │                │                  │ For each file: │                │
     │                  │                │                  │ ├── classify   │                │
     │                  │                │                  │ │   (plan/      │                │
     │                  │                │                  │ │   render/     │                │
     │                  │                │                  │ │   photo)      │                │
     │                  │                │                  │ │              │                │
     │                  │                │                  │ ├── extract:   │                │
     │                  │                │                  │ │   façade      │                │
     │                  │                │                  │ │   language    │                │
     │                  │                │                  │ │   materials   │                │
     │                  │                │                  │ │   spatial     │                │
     │                  │                │                  │ │   adjacency   │                │
     │                  │                │                  │ │   proportions │                │
     │                  │                │                  │ │              │                │
     │                  │                │                  │ └── aggregate  │                │
     │                  │                │                  │     into Style │                │
     │                  │                │                  │     Profile    │                │
     │                  │                │                  │                │                │
     │◄── Notification: │                │                  │                │                │
     │  "Style profile  │                │                  │                │                │
     │   ready for      │                │                  │                │                │
     │   review"        │                │                  │                │                │
     │                  │                │                  │                │                │
     │ Review profile   │                │                  │                │                │
     ├─────────────────►│                │                  │                │                │
     │                  │ GET /styles    │                  │                │                │
     │                  │ /{profile_id}  │                  │                │                │
     │                  ├───────────────►│                  │                │                │
     │                  │◄── profile ────┤                  │                │                │
     │◄── Style profile │                │                  │                │                │
     │  "Bạn thường:    │                │                  │                │                │
     │   • Mặt tiền kính│                │                  │                │                │
     │   • Ban công lệch │                │                  │                │                │
     │   • Bê tông trần │                │                  │                │                │
     │   • Giếng trời   │                │                  │                │                │
     │     trung tâm"   │                │                  │                │                │
     │                  │                │                  │                │                │
     │ Correct: "Tôi    │                │                  │                │                │
     │ dùng gỗ nhiều    │                │                  │                │                │
     │ hơn bê tông"     │                │                  │                │                │
     ├─────────────────►│                │                  │                │                │
     │                  │ PATCH /styles  │                  │                │                │
     │                  ├───────────────►│                  │                │                │
     │                  │                │ Update profile ──►│                │                │
     │                  │                │                  │ Adjust weight: │                │
     │                  │                │                  │ wood ↑ concrete↓│                │
     │                  │                │                  │ Save profile V2│                │
     │                  │◄── updated ────┤                  │                │                │
     │◄── "Profile      │                │                  │                │                │
     │     updated" ─────│                │                  │                │                │
     │                  │                │                  │                │                │
     │                  │                │                  │                │                │
     │   ═══ LATER: Project Generation uses Style Profile ═══              │                │
     │                  │                │                  │                │                │
     │                  │                │ StyleResolve()   │                │                │
     │                  │                ├─────────────────►│                │                │
     │                  │                │                  │ Merge:         │                │
     │                  │                │                  │ brief (hard    │                │
     │                  │                │                  │  constraint)   │                │
     │                  │                │                  │ + style (soft  │                │
     │                  │                │                  │  constraint)   │                │
     │                  │                │                  │ = resolved     │                │
     │                  │                │                  │   params       │                │
     │                  │                │◄── resolved ──────┤                │                │
     │                  │                │                  │                │                │
     │                  │                │ FloorPlanGen     │                │                │
     │                  │                │ (with resolved ──┼───────────────►│                │
     │                  │                │  style params)   │                ├───────────────►│
     │                  │                │                  │                │   GPU: style-   │
     │                  │                │                  │                │   conditioned   │
     │                  │                │                  │                │   generation    │
     │                  │                │                  │                │                │
```

---

### 4.6 UC-06: Export & Delivery (M8+M9)

```
  KTS/PM            Frontend(M1)     Query Loop(P2)    Tool Orch(P3)     Canonical(M4)     Permission(P6)
     │                  │                │                  │                │                │
     │ Export PDF for V2 │                │                  │                │                │
     ├─────────────────►│                │                  │                │                │
     │                  │ POST /export   │                  │                │                │
     │                  │ /{ver}/pdf     │                  │                │                │
     │                  ├───────────────►│                  │                │                │
     │                  │                │                  │                │                │
     │                  │                │ Permission ──────┼───────────────┼───────────────►│
     │                  │                │ check            │                │                │ classify:
     │                  │                │                  │                │                │ export_pdf
     │                  │                │                  │                │                │ version.status
     │                  │                │                  │                │                │ == approved?
     │                  │                │                  │                │                │
     │                  │                │                  │                │                │ IF approved:
     │                  │                │◄── ALLOW ────────┼───────────────┼────────────────┤   ALLOW
     │                  │                │                  │                │                │ IF generated:
     │                  │                │                  │                │                │   ALLOW with
     │                  │                │                  │                │                │   watermark
     │                  │                │                  │                │                │   "CONCEPT"
     │                  │                │                  │                │                │
     │                  │                │ Load canonical ──┼───────────────►│                │
     │                  │                │ version          │                │ return:        │
     │                  │                │◄─────────────────┼────────────────┤ brief+plans    │
     │                  │                │                  │                │ +renders+meta  │
     │                  │                │                  │                │                │
     │                  │                │ ══ BACKGROUND TASK: Export ══     │                │
     │                  │                │                  │                │                │
     │                  │                │ tool: ExportPDF()│                │                │
     │                  │                ├─────────────────►│                │                │
     │                  │                │                  │ EXCLUSIVE      │                │
     │                  │                │                  │ Generate PDF:  │                │
     │                  │                │                  │ • Cover page   │                │
     │                  │                │                  │ • Brief summary│                │
     │                  │                │                  │ • Floor plans  │                │
     │                  │                │                  │ • 3D renders   │                │
     │                  │                │                  │ • Readiness:   │                │
     │                  │                │                  │   "APPROVED"   │                │
     │                  │                │                  │ • Watermark    │                │
     │                  │                │                  │   if concept   │                │
     │                  │                │                  │                │                │
     │                  │                │                  │ context_mod:   │                │
     │                  │                │                  │ pdf_url =      │                │
     │                  │                │                  │ "s3://...pdf"  │                │
     │                  │                │                  │                │                │
     │                  │                │                  │ Save to M4 ───►│                │
     │                  │                │                  │ (derived asset)│ link pdf to    │
     │                  │                │                  │                │ canonical ver  │
     │                  │                │                  │                │                │
     │                  │                │◄── completed ────┤                │                │
     │                  │◄── download ───┤                  │                │                │
     │◄── PDF file ─────│                │                  │                │                │
     │                  │                │                  │                │                │
     │                  │                │                  │                │                │
     │ Create handoff   │                │                  │                │                │
     │ bundle           │                │                  │                │                │
     ├─────────────────►│                │                  │                │                │
     │                  │ POST /handoff  │                  │                │                │
     │                  │ /{ver}         │                  │                │                │
     │                  ├───────────────►│                  │                │                │
     │                  │                │                  │                │                │
     │                  │                │ Permission: ─────┼───────────────┼───────────────►│
     │                  │                │ create_handoff   │                │                │ REQUIRE:
     │                  │                │                  │                │                │ • version locked
     │                  │                │                  │                │                │ • KTS approved
     │                  │                │                  │                │                │ • exports exist
     │                  │                │                  │                │                │ • role = KTS|PM
     │                  │                │◄── ALLOW ────────┼───────────────┼────────────────┤
     │                  │                │                  │                │                │
     │                  │                │ Bundle:          │                │                │
     │                  │                │ • PDF concept    │                │                │
     │                  │                │ • Floor plan PNGs│                │                │
     │                  │                │ • 3D renders     │                │                │
     │                  │                │ • Brief JSON     │                │                │
     │                  │                │ • Approval log   │                │                │
     │                  │                │ • Annotation hist│                │                │
     │                  │                │                  │                │                │
     │                  │                │ Mark as current ─┼───────────────►│                │
     │                  │                │ official handoff │                │ set bundle     │
     │                  │                │                  │                │ as official    │
     │                  │                │                  │                │ (old bundles   │
     │                  │                │                  │                │  → superseded) │
     │                  │                │                  │                │                │
     │                  │◄── bundle ─────┤                  │                │                │
     │◄── "Handoff      │  created       │                  │                │                │
     │     bundle V2    │                │                  │                │                │
     │     ready" ───────│                │                  │                │                │
     │                  │                │                  │                │                │
```

---

### 4.7 UC-07: Escalating Recovery khi Generation Fail

```
  Query Loop(P2)     Tool Orch(P3)      GPU Service       Recovery(P2)
     │                  │                  │                  │
     │ FloorPlanGen()   │                  │                  │
     ├─────────────────►│                  │                  │
     │                  ├─────────────────►│                  │
     │                  │                  │ ⚡ GPU TIMEOUT   │
     │                  │◄── ERROR ────────┤                  │
     │                  │                  │                  │
     │◄── error ────────┤                  │                  │
     │                  │                  │                  │
     │ ═══ LEVEL 1: Retry same config (×3) ═══               │
     │                  │                  │                  │
     │ retry_count = 1  │                  │                  │
     ├─────────────────►│                  │                  │
     │                  ├─────────────────►│                  │
     │                  │                  │ ⚡ TIMEOUT again │
     │                  │◄── ERROR ────────┤                  │
     │◄── error ────────┤                  │                  │
     │                  │                  │                  │
     │ retry_count = 2  │                  │                  │
     ├─────────────────►│─────────────────►│                  │
     │                  │                  │ ⚡ TIMEOUT again │
     │                  │◄── ERROR ────────┤                  │
     │◄── error ────────┤                  │                  │
     │                  │                  │                  │
     │ retry_count = 3 → MAX REACHED       │                  │
     │                  │                  │                  │
     │ ═══ LEVEL 2: Change params ═══      │                  │
     │                  │                  │                  │
     │ Reduce resolution│                  │                  │
     │ 2048→1024,       │                  │                  │
     │ remove ControlNet│                  │                  │
     ├─────────────────►│                  │                  │
     │                  ├─────────────────►│                  │
     │                  │                  │ ⚡ STILL FAIL    │
     │                  │◄── ERROR ────────┤                  │
     │◄── error ────────┤                  │                  │
     │                  │                  │                  │
     │ ═══ LEVEL 3: Switch model ═══       │                  │
     │                  │                  │                  │
     │ SDXL → SD 1.5    │                  │                  │
     │ (lighter model)  │                  │                  │
     ├─────────────────►│                  │                  │
     │                  ├─────────────────►│                  │
     │                  │                  │ ✓ SUCCESS!       │
     │                  │◄── result ───────┤                  │
     │◄── result ───────┤                  │                  │
     │                  │                  │                  │
     │ yield to UI:     │                  │                  │
     │ "Floor plan generated              │                  │
     │  (lower quality due to             │                  │
     │   fallback model)"                 │                  │
     │                  │                  │                  │
     │ IF LEVEL 3 ALSO FAILS:             │                  │
     │                  │                  │                  │
     │ ═══ LEVEL 4: Switch pipeline ═══   │                  │
     │ ComfyUI → Diffusers direct         │                  │
     │                  │                  │                  │
     │ ═══ LEVEL 5: Surface error ═══     │                  │
     │ yield to UI:                        │                  │
     │ "Generation thất bại sau           │                  │
     │  nhiều lần thử. Vui lòng:          │                  │
     │  1. Thử lại sau                     │                  │
     │  2. Đơn giản hóa yêu cầu           │                  │
     │  3. Liên hệ support"               │                  │
     │                  │                  │                  │
```

---

### 4.8 UC-08: Context Defense khi Design Session dài (P5)

```
  Query Loop(P2)     Context Mgmt(P5)   LLM API
     │                  │                  │
     │ Turn 1-10: Normal operation         │
     │ (intake + first generation)         │
     │ Token count: ~40K                   │
     ├──────────────────────────────────── │
     │                  │                  │
     │ Turn 11-25: Revisions + reviews     │
     │ Token count: ~90K                   │
     │                  │                  │
     │ ═══ Layer 1: TRUNCATION ═══         │
     │                  │                  │
     │ FloorPlanGen result (turn 5)        │
     │ output: 3000 chars                  │
     │ → persist to S3                     │
     │ → keep pointer only (50 chars)      │
     │ Saved: ~2950 chars per large result │
     │                  │                  │
     │ Turn 26-40: More revisions          │
     │ Token count: ~120K                  │
     │                  │                  │
     │ ═══ Layer 2: MICROCOMPACT ═══       │
     │                  │                  │
     │ Check: 120K > 60% of 200K? YES     │
     │                  │                  │
     │ Remove tool_results older than      │
     │ 5 turns:                            │
     │ • Turn 26 BriefGet → "[stale]"      │
     │ • Turn 27 StyleSearch → "[stale]"   │
     │ • Turn 28 FloorPlanGen → "[see S3]" │
     │                  │                  │
     │ Token count: ~95K (saved 25K)       │
     │                  │                  │
     │ Turn 41-60: Extended session        │
     │ Token count: ~170K                  │
     │                  │                  │
     │ ═══ Layer 3: AUTO-COMPACT ═══       │
     │                  │                  │
     │ Check: 170K > effective_window      │
     │ (200K - 20K reserved = 180K)? YES   │
     │                  │                  │
     │ Call LLM summarize ────────────────►│
     │                  │                  │ Summary:
     │                  │                  │ "Project: nhà phố
     │                  │                  │  5x20m, 4 tầng.
     │                  │                  │  V1 rejected:
     │                  │                  │  kitchen too small.
     │                  │                  │  V2 approved:
     │                  │                  │  open kitchen,
     │                  │                  │  3PN. V3 pending:
     │                  │                  │  client wants
     │                  │                  │  bigger living room.
     │                  │                  │  Style: modern
     │                  │                  │  minimalist, KTS
     │                  │                  │  Nguyen profile V2."
     │                  │◄─────────────────┤
     │                  │                  │
     │ Create compact boundary message     │
     │ All messages before boundary        │
     │ → REMOVED from API request          │
     │ Only summary + recent messages sent │
     │                  │                  │
     │ Token count: ~25K (compact done!)   │
     │                  │                  │
     │ ═══ ALSO: Memory Extraction ═══     │
     │                  │                  │
     │ Background: extract key decisions   │
     │ → Project memory:                   │
     │   "Client rejected V1 vì kitchen    │
     │    quá nhỏ. Open kitchen là must."  │
     │ → Client memory:                    │
     │   "Client Minh ưu tiên phòng khách  │
     │    và bếp rộng hơn phòng ngủ."     │
     │                  │                  │
     │ Turn 61: API returns 413 error      │
     │                  │                  │
     │ ═══ Layer 4: REACTIVE COMPACT ═══   │
     │                  │                  │
     │ Emergency: API rejected request     │
     │ → Immediate LLM summarize           │
     │ → Retry API call with compact       │
     │ → has_attempted_reactive = True     │
     │   (circuit breaker: no 2nd attempt) │
     │                  │                  │
```

---

## 5. Data Model — Entity Relationship

```
┌──────────────┐     ┌──────────────────┐     ┌──────────────────┐
│    User       │     │   Organization   │     │   StyleProfile   │
├──────────────┤     ├──────────────────┤     ├──────────────────┤
│ id            │     │ id               │     │ id               │
│ email         │◄────┤ name             │     │ kts_user_id      │
│ role          │     │ plan             │     │ org_id           │
│ org_id ───────┼────►│                  │     │ version          │
└──────────────┘     └──────────────────┘     │ patterns_json    │
                                               │ status           │
                                               │ approved_at      │
┌──────────────┐                               └────────┬─────────┘
│   Project     │                                        │
├──────────────┤     ┌──────────────────┐                │
│ id            │     │ DesignVersion    │                │
│ name          │     ├──────────────────┤                │
│ org_id        │     │ id               │                │
│ client_user_id│     │ project_id ──────┼───► Project    │
│ kts_user_id   │     │ parent_ver_id    │ (lineage)      │
│ status        │     │ version_number   │                │
│ style_profile ┼────►│ status ──────────┼───► state machine
│   _id         │     │                  │                │
└──────┬───────┘     │ ── Brief ──────  │                │
       │              │ brief_json       │                │
       │              │                  │                │
       │              │ ── Geometry ──── │                │
       │              │ geometry_json    │ ◄── M5 output  │
       │              │ floor_plan_urls  │                │
       │              │                  │                │
       │              │ ── Style ─────  │                │
       │              │ style_profile_id ┼────────────────┘
       │              │ resolved_params  │
       │              │                  │
       │              │ ── Review ────  │     ┌──────────────────┐
       │              │ reviewed_by      │     │   Annotation     │
       │              │ reviewed_at      │     ├──────────────────┤
       │              │ approval_status  │     │ id               │
       │              │                  │     │ version_id ──────┼──► DesignVersion
       │              │ ── Derived ──── │     │ user_id          │
       │              │ render_urls      │     │ x, y (coords)   │
       │              │ model_url        │     │ comment          │
       │              │ export_urls      │     │ created_at       │
       │              │ bundle_id        │     └──────────────────┘
       │              └──────────────────┘
       │
       │              ┌──────────────────┐     ┌──────────────────┐
       │              │ HandoffBundle    │     │   Feedback       │
       └─────────────►├──────────────────┤     ├──────────────────┤
                      │ id               │     │ id               │
                      │ project_id       │     │ version_id       │
                      │ version_id       │     │ user_id          │
                      │ is_current       │     │ type (text/annot)│
                      │ files_manifest   │     │ content          │
                      │ created_by       │     │ structured_json  │
                      │ created_at       │     │ created_at       │
                      │ readiness_label  │     └──────────────────┘
                      └──────────────────┘

                      ┌──────────────────┐
                      │  AuditLog        │
                      ├──────────────────┤
                      │ id               │
                      │ project_id       │
                      │ version_id       │
                      │ user_id          │
                      │ action           │
                      │ details_json     │
                      │ created_at       │
                      └──────────────────┘
```

---

## 6. Trả lời Open Questions

### Q1: Style Intelligence là core hay pilot?

**Quyết định: MVP+ (pilot cho 3-5 KTS đầu tiên)**

Lý do: M3 cần data (portfolio import) trước khi hoạt động. Phase 1 build infrastructure (import, extract, profile CRUD). Pilot với early adopters để validate giá trị trước khi scale. Generation vẫn hoạt động không có style profile (dùng brief + generic style prompt).

### Q2: Geometry JSON lưu đến mức nào?

**Quyết định: Dual-layer — preview image + structured geometry JSON**

```
Layer 1 (Phase 1): Preview image (PNG 2048×2048) + basic metadata JSON
  {
    "rooms": [{"name": "living", "area_m2": 24, "floor": 1}],
    "total_area_m2": 320,
    "floors": 4,
    "dimensions": {"width": 5, "depth": 20}
  }

Layer 2 (Phase 2): Full geometry JSON
  {
    "walls": [{"start": [0,0], "end": [5,0], "thickness": 0.2}],
    "rooms": [{"polygon": [[0,0],[5,0],[5,4.8],[0,4.8]], "type": "living"}],
    "openings": [{"type": "door", "wall_id": "w1", "position": 2.5}]
  }
```

Phase 1 đủ cho: canonical state, visual comparison, PDF export.
Phase 2 cần cho: DXF export, IFC export, accurate measurements.

### Q3: DXF bắt buộc Phase 1?

**Quyết định: SVG + PDF trước, DXF là P2 (nice to have)**

Phase 1: SVG (vector, scalable) + PDF (presentation). Đủ cho KTS review và client presentation.
Phase 2: DXF khi geometry JSON đủ chi tiết (Layer 2 ở Q2).

### Q4: 3D viewer P0 hay P1?

**Quyết định: Render images P0, Interactive viewer P1**

Phase 1 P0: Static 3D renders (exterior + 3 interior rooms) — đủ thuyết phục cho client.
Phase 1 P1: Three.js viewer với GLTF model — orbit, zoom, floor view.
Lý do: Render images production cost thấp hơn, client impression tốt. Viewer cần thêm effort nhưng KTS cần nó cho review.

### Q5: Tiêu chí handoff_ready?

**Quyết định: Checklist enforced bằng code**

```python
def can_create_handoff(version: DesignVersion) -> tuple[bool, list[str]]:
    errors = []
    if version.status != "locked":
        errors.append("Version chưa được lock")
    if version.approval_status != "approved":
        errors.append("Version chưa được KTS approve")
    if not version.export_urls.get("pdf"):
        errors.append("Chưa có PDF export")
    if not version.floor_plan_urls:
        errors.append("Chưa có floor plan")
    if not version.render_urls:
        errors.append("Chưa có 3D renders")
    return (len(errors) == 0, errors)
```

---

## 7. Implementation Priority Matrix

```
PHASE 1 MVP — Bắt buộc
═══════════════════════

Sprint 1-2: Foundation
├── M1 Experience Layer (basic: 3 workspaces)
├── M4 Canonical Design State (core state machine)
├── P6 Permission (roles + KTS gate)
└── P2 Query Loop (async generator engine)

Sprint 3-4: Intake + Generation
├── M2 Intake & Brief (chat + form → Design Brief JSON)
├── M5 2D Generation (brief → 2-3 floor plan options)
├── P3 Tool Orchestration (partitioning + 8 tools)
└── P5 Context Management (Layer 1-3)

Sprint 5-6: Review + Export
├── M6 Review & Annotation (annotate, approve/reject)
├── M8 Standards Export (PDF + SVG + render images)
├── P4 Multi-Agent (Coordinator + 4 workers)
└── P2 Recovery (escalating 5 levels)

PHASE 1 MVP+ — Rất nên có
═══════════════════════════

Sprint 7-8:
├── M3 Style Intelligence (import, extract, profile)
├── M7 3D Derivation (model + renders from canonical)
├── M1 3D Viewer (Three.js interactive)
└── P5 Context Management (Layer 4-5)

Sprint 9-10:
├── M9 Delivery & Handoff (bundles, contractor workspace)
├── M8 DXF Export (geometry Layer 2)
└── M3 Style feedback loop (learn from approvals/rejections)
```
