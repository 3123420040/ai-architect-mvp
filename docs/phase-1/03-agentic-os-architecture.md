# Phase 1 – Agentic OS Architecture cho AI Architect

*Ngày tạo: Apr 11, 2026*
*Dựa trên: "Giải phẫu một Agentic Operating System" — 18 Architectural Patterns từ 513K LOC Claude Code*

---

## 1. Tại sao cần Agentic OS thay vì "wrapper app"

Bài học từ Chương 1 của sách: **wrapper app luôn thua model vendor ở generic capability. Chỉ domain-specific orchestration mới có defensible value.**

AI Architect KHÔNG phải wrapper gọi Stable Diffusion rồi hiển thị kết quả. Nó là **Agentic Operating System cho thiết kế kiến trúc nhà ở** — quản lý tài nguyên (GPU, context window, design versions), phân quyền (KTS review gate, client feedback), điều phối (multi-agent design pipeline), và recovery (khi generation fail, khi context đầy).

### Mức trưởng thành AI Maturity cho AI Architect

| Mức | Tên | Áp dụng cho AI Architect |
|-----|------|--------------------------|
| 1 | Manual | KTS vẽ bằng tay (status quo) |
| 2 | Tool | User gọi AI generate 1 lần, nhận kết quả |
| 3 | Assistant | AI nhớ context qua nhiều revision |
| 4 | **Copilot** | **AI đề xuất design, KTS approve/reject (Phase 1 target)** |
| 5 | Agent | AI tự lặp, tự check feasibility, tự revise đến khi đạt (Phase 2+) |

**Phase 1 target: Mức 4 (Copilot)** — AI đề xuất, human (KTS) approve. Human-in-the-loop bắt buộc. Phase 2+ tiến đến mức 5 cho một số task (auto-feasibility check).

---

## 2. 6 Pipeline lồng nhau — Kiến trúc tổng thể

Áp dụng trực tiếp mô hình 6 pipeline từ Chương 2:

```
┌─────────────────────────────────────────────────────────────────┐
│  1. CLIENT UI LAYER                                              │
│     Next.js + React + Three.js + ThatOpen BIM Components         │
│     [Chat] [Intake Form] [3D Viewer] [Review Dashboard]          │
│     [Design Gallery] [Version Timeline] [Notifications]          │
├─────────────────────────────────────────────────────────────────┤
│  2. QUERY LOOP (Trái tim — async generator)                      │
│     while(true) {                                                │
│       Phase 1: Context Assembly (design brief + history)         │
│       Phase 2: LLM API Call (streaming)                          │
│       Phase 3: Tool Execution (generate, render, export)         │
│       Phase 4: Stop or Continue (needsFollowUp)                  │
│     }                                                            │
├─────────────────────────────────────────────────────────────────┤
│  3. TOOL ORCHESTRATION                                           │
│     partitionToolCalls() → concurrent/serial batches             │
│     [FloorPlanGen] [3DRender] [ExportPDF] [DesignBriefParse]    │
│     [FeasibilityCheck] [DimensionCalc] [StyleTransfer]          │
├─────────────────────────────────────────────────────────────────┤
│  4. MULTI-AGENT COORDINATION                                     │
│     Pattern A: Subagent (Requirements → Design → Review)         │
│     Pattern B: Coordinator (KTS assigns, workers execute)        │
│     Pattern C: Fork (parallel design variations)                 │
├─────────────────────────────────────────────────────────────────┤
│  5. CONTEXT MANAGEMENT                                           │
│     5 layers: truncate → microcompact → auto-compact             │
│              → reactive compact → context collapse               │
│     + Design Memory (project decisions qua sessions)             │
├─────────────────────────────────────────────────────────────────┤
│  6. PERMISSION & SECURITY                                        │
│     Classify: read-only (view design) vs mutating (edit brief)   │
│     vs destructive (delete project) vs generation (GPU call)     │
│     KTS approval gate = human-in-the-loop enforcement            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Pattern Mapping: 18 Patterns → AI Architect

### Áp dụng trực tiếp (10 patterns)

| # | Pattern | Áp dụng trong AI Architect | Priority |
|---|---------|---------------------------|----------|
| **1** | **Async generator as control flow** | Query loop cho design pipeline: yield partial results (floor plan draft → 3D progress → final render) cho UI hiển thị real-time | P0 |
| **2** | **Stop-reason state machine** | `needsFollowUp` boolean: có tool_use block (cần generate tiếp) → continue. Không → done. Không trust API stop_reason | P0 |
| **3** | **Escalating recovery** | Generation fail → retry cùng prompt (×3) → đổi seed/params → switch model (SDXL→SD1.5) → notify user "Generation thất bại, hãy thử lại với yêu cầu khác" | P0 |
| **4** | **Concurrency-safe partitioning** | FloorPlanRead, DesignBriefGet, StyleSearch = SAFE (song song). FloorPlanGenerate, 3DRender, ExportPDF = EXCLUSIVE (tuần tự) | P0 |
| **7** | **Coordinator restriction** | **Design Coordinator** chỉ có: AssignTask, SendFeedback, ApproveDesign, RequestRevision. KHÔNG có GenerateFloorPlan, Render3D. Buộc phải delegate cho worker agents | P0 |
| **9** | **5-layer context defense** | Long design sessions (nhiều revision) cần context compaction. Layer 1: truncate large render outputs. Layer 2: microcompact old tool results. Layer 3: auto-compact design history | P0 |
| **10** | **Permission classification** | Classify actions: view (SAFE) → edit brief (ASK KTS) → generate (ALLOW) → delete project (ASK ADMIN) → export final (ASK KTS APPROVED) | P0 |
| **5** | **Streaming tool execution** | Bắt đầu render interior rooms ngay khi exterior render xong, không đợi tất cả renders hoàn thành | P1 |
| **6** | **Context modifier chain** | FloorPlanGenerate trả contextModifier thêm generated_floor_plan_url vào context. 3DRender tool tiếp theo nhận context đã có floor plan URL | P1 |
| **11** | **Conditional skill activation** | Skill "Vietnamese Building Code QCVN" auto-activate khi project location = Vietnam. Skill "Tropical Architecture" auto-activate khi style = tropical | P1 |

### Áp dụng gián tiếp / Phase 2+ (5 patterns)

| # | Pattern | Kế hoạch Phase 2+ |
|---|---------|-------------------|
| **8** | **Fork isolation** | Khi cần 3 design variations song song, mỗi variation chạy trên "design branch" riêng, merge khi user chọn |
| **12** | **Shell-in-prompt** | Inject dynamic context vào agent prompt: `!python get_lot_constraints.py ${lot_id}` → agent nhận constraints thật |
| **13** | **Dynamic skill discovery** | Walk project directory tìm `.architect/skills/` chứa domain-specific rules |
| **14** | **4-point plugin extension** | Plugin cho material databases, cost estimators, contractor directories |
| **15** | **Security sandbox** | Plugin third-party (material database) không được access project financial data |

### Không áp dụng (3 patterns — domain-specific cho terminal CLI)

| # | Pattern | Lý do không áp dụng |
|---|---------|---------------------|
| 16 | Reconciliation-based install | Web app, không cần marketplace reconciliation |
| 17 | Pure-TS native replacement | Web stack, không có native binary concern |
| 18 | Terminal-as-browser rendering | Web app dùng browser rendering trực tiếp |

---

## 4. Pipeline 2: Query Loop — Trái tim của AI Architect

### 4.1 Async Generator Design (Pattern #1)

```python
# ai-architect-api/app/agents/query_loop.py

async def design_query_loop(
    params: DesignQueryParams
) -> AsyncGenerator[DesignMessage | StreamEvent, DesignTerminal]:
    """
    Core agentic loop cho AI Architect.
    Yield messages cho frontend real-time.
    Pull-based: frontend controls pace.
    Cancel bằng generator.aclose().
    """
    state = build_initial_state(params)
    
    while True:
        # === PHASE 1: Context Assembly ===
        # Ghép: design brief + conversation history + project memories
        # Check auto-compact nếu context vượt ngưỡng
        messages = await assemble_context(state)
        
        # === PHASE 2: LLM API Call (streaming) ===
        needs_follow_up = False
        async for chunk in call_llm(messages, tools=DESIGN_TOOLS):
            if chunk.has_tool_use:
                needs_follow_up = True  # THE KEY LINE
                streaming_executor.add_tool(chunk.tool_use)
            yield chunk  # Push to frontend via WebSocket
        
        # === PHASE 3: Tool Execution ===
        async for result in streaming_executor.get_remaining():
            yield result
            tool_results.append(result)
            if result.context_modifier:
                state.context = result.context_modifier(state.context)
        
        # === PHASE 4: Stop or Continue ===
        if not needs_follow_up:
            # Recovery paths
            if state.withheld_error == "prompt_too_long":
                await reactive_compact(state)
                state.transition = "reactive_compact_retry"
                continue
            if state.withheld_error == "max_tokens":
                if state.recovery_count < 3:
                    state.recovery_count += 1
                    inject_recovery_message(state)
                    state.transition = "max_tokens_recovery"
                    continue
            
            # Run stop hooks (KTS review check, etc.)
            hook_result = await run_stop_hooks(state)
            if hook_result.blocked:
                inject_hook_error(state, hook_result)
                state.transition = "stop_hook_retry"
                continue
            
            return DesignTerminal(reason="completed")
        
        # Continue: build next state
        state = DesignState(
            messages=[*state.messages, *assistant_msgs, *tool_results],
            transition=Transition(reason="next_turn"),
            turn_count=state.turn_count + 1
        )
```

### 4.2 State Machine ẩn (Pattern #2)

```
                    ┌──────────────┐
                    │  next_turn   │ ←── Normal: tool results cần follow-up
                    └──────┬───────┘
                           │
              ┌────────────▼────────────┐
              │    QUERY LOOP ITERATION  │
              └────────────┬────────────┘
                           │
              needsFollowUp == false?
                    │              │
                   YES            NO → continue loop
                    │
         ┌──────────▼──────────┐
         │  Check error type   │
         └──────────┬──────────┘
                    │
    ┌───────────────┼───────────────┐
    │               │               │
  413 error    max_tokens      no error
    │               │               │
    ▼               ▼               ▼
reactive_      recovery ×3      run stop hooks
compact_retry  then escalate        │
                                    │
                              ┌─────┼─────┐
                              │           │
                          hook OK     hook blocked
                              │           │
                              ▼           ▼
                          COMPLETED   stop_hook_retry
```

### 4.3 Escalating Recovery (Pattern #3)

```
Cấp 1: Retry cùng config          → GPU timeout? Retry 3 lần (backoff)
Cấp 2: Thay đổi params            → Đổi seed, giảm resolution, bỏ ControlNet
Cấp 3: Switch model               → SDXL fail → SD 1.5 fallback  
Cấp 4: Switch pipeline            → ComfyUI fail → Diffusers pipeline fallback
Cấp 5: Surface error to user      → "Generation thất bại. Hãy thử lại."

Circuit breaker: has_attempted_reactive_compact = True → không retry lần 2
Death spiral prevention: Khi API error, KHÔNG chạy stop hooks (tránh inject thêm tokens)
```

---

## 5. Pipeline 3: Tool Orchestration — 12 Tools

### 5.1 Tool Inventory

```python
# Phân loại theo concurrency behavior

DESIGN_TOOLS = {
    # === READ-ONLY (concurrent-safe) ===
    "DesignBriefGet":       {"concurrent": True,  "desc": "Đọc design brief hiện tại"},
    "ProjectHistoryGet":    {"concurrent": True,  "desc": "Đọc version history"},
    "StyleSearch":          {"concurrent": True,  "desc": "Tìm kiếm style references"},
    "BuildingCodeLookup":   {"concurrent": True,  "desc": "Tra cứu quy chuẩn xây dựng"},
    "MaterialSearch":       {"concurrent": True,  "desc": "Tìm kiếm vật liệu"},
    
    # === CONDITIONAL (depends on input) ===
    "DimensionCalc":        {"concurrent": "depends", "desc": "Tính toán kích thước"},
    #   → DimensionCalc(read_only=True) → SAFE
    #   → DimensionCalc(update_brief=True) → EXCLUSIVE
    
    # === ALWAYS EXCLUSIVE ===
    "FloorPlanGenerate":    {"concurrent": False, "desc": "Generate 2D floor plan (GPU)"},
    "Render3D":             {"concurrent": False, "desc": "Generate 3D render (GPU)"},
    "DesignBriefUpdate":    {"concurrent": False, "desc": "Cập nhật design brief"},
    "ExportPDF":            {"concurrent": False, "desc": "Export PDF bản vẽ"},
    "ExportDXF":            {"concurrent": False, "desc": "Export DXF cho AutoCAD"},
    "FeasibilityCheck":     {"concurrent": False, "desc": "Kiểm tra khả thi kỹ thuật"},
}
```

### 5.2 Concurrency Partitioning (Pattern #4)

```python
def partition_tool_calls(tool_uses: list[ToolUse]) -> list[Batch]:
    """
    Giống hệt Claude Code: greedy batching.
    Safe-by-default: tool không khai báo → exclusive.
    Per-invocation: cùng tool, input khác → quyết định khác.
    """
    batches = []
    for tool_use in tool_uses:
        tool = find_tool(tool_use.name)
        is_safe = tool.is_concurrency_safe(tool_use.input)  # Per-invocation!
        
        if is_safe and batches and batches[-1].is_concurrent:
            batches[-1].blocks.append(tool_use)  # Gom vào batch trước
        else:
            batches.append(Batch(is_concurrent=is_safe, blocks=[tool_use]))
    
    return batches

# Ví dụ thực tế:
# LLM response chứa 5 tool calls:
# 1. DesignBriefGet()           → SAFE
# 2. StyleSearch("modern")      → SAFE  
# 3. BuildingCodeLookup("QCVN") → SAFE
# 4. FloorPlanGenerate(brief)   → EXCLUSIVE
# 5. Render3D(floor_plan)       → EXCLUSIVE
#
# Partition: [DesignBriefGet + StyleSearch + BuildingCodeLookup] → [FloorPlanGenerate] → [Render3D]
# 3 bước thay vì 5. Batch 1 chạy 3 reads song song.
```

### 5.3 Context Modifier Chain (Pattern #6)

```python
# Chỉ EXCLUSIVE tools mới được trả context_modifier

class FloorPlanGenerateTool:
    def execute(self, input, context):
        result = self.gpu_service.generate(input)
        return ToolResult(
            output=result.image_url,
            context_modifier=lambda ctx: ctx.update({
                "latest_floor_plan_url": result.image_url,
                "latest_floor_plan_metadata": result.metadata,
                "floor_plans_generated": ctx.get("floor_plans_generated", 0) + 1
            })
        )

class Render3DTool:
    def execute(self, input, context):
        # Tool tiếp theo nhận context đã có floor_plan_url!
        floor_plan = context["latest_floor_plan_url"]
        result = self.gpu_service.render_3d(floor_plan, input.style)
        return ToolResult(
            output=result.render_urls,
            context_modifier=lambda ctx: ctx.update({
                "latest_renders": result.render_urls
            })
        )
```

---

## 6. Pipeline 4: Multi-Agent — 3 Patterns

### 6.1 Agent Inventory

```
┌─────────────────────────────────────────────────────────┐
│                    AGENT HIERARCHY                        │
│                                                          │
│  ┌──────────────────────┐                                │
│  │  Design Coordinator  │ ← Pattern B: restricted tools  │
│  │  Tools: AssignTask,  │    KHÔNG có Generate, Render    │
│  │  SendFeedback,       │    BUỘC phải delegate           │
│  │  ApproveDesign       │                                │
│  └──────────┬───────────┘                                │
│             │                                            │
│    ┌────────┼────────┬──────────┐                        │
│    ▼        ▼        ▼          ▼                        │
│  ┌────┐  ┌────┐  ┌────┐  ┌──────────┐                   │
│  │Req │  │Des │  │Rev │  │Revision  │                    │
│  │Agt │  │Agt │  │Agt │  │Agent     │                    │
│  └────┘  └────┘  └────┘  └──────────┘                   │
│                                                          │
│  Pattern A: Subagents with specialized tool subsets      │
└─────────────────────────────────────────────────────────┘
```

### 6.2 4 Specialized Agents (Pattern A: Subagent)

| Agent | Tool Subset | Vai trò | Constraints |
|-------|-------------|---------|-------------|
| **Requirements Agent** | DesignBriefGet, DesignBriefUpdate, BuildingCodeLookup, StyleSearch | Thu thập & clarify yêu cầu từ user. Extract structured Design Brief | READ + WRITE brief only. Không generate |
| **Design Agent** | FloorPlanGenerate, Render3D, DimensionCalc, DesignBriefGet, StyleSearch | Generate floor plan + 3D renders từ Design Brief | Full generation access. Output = images |
| **Review Agent** | DesignBriefGet, FeasibilityCheck, BuildingCodeLookup, DimensionCalc | Kiểm tra feasibility, code compliance, spatial constraints | **READ-ONLY + check tools**. Không sửa. "Your job is to find issues, not fix them" |
| **Revision Agent** | FloorPlanGenerate, Render3D, DesignBriefGet, DesignBriefUpdate | Nhận feedback → regenerate. Combine old brief + feedback → new design | Full generation + brief update |

### 6.3 Design Coordinator (Pattern B: Coordinator Restriction — Pattern #7)

```python
# CRITICAL: Coordinator KHÔNG CÓ execution tools

COORDINATOR_TOOLS = {
    "AssignTask",       # Giao task cho agent
    "SendFeedback",     # Gửi feedback cho agent
    "ApproveDesign",    # Approve design cho client
    "RequestRevision",  # Yêu cầu revision
    "NotifyClient",     # Thông báo cho client
}

# Coordinator KHÔNG CÓ:
# - FloorPlanGenerate (phải giao cho Design Agent)
# - Render3D (phải giao cho Design Agent)
# - FeasibilityCheck (phải giao cho Review Agent)
# - DesignBriefUpdate (phải giao cho Requirements Agent)

# TẠI SAO: Nếu coordinator có thể generate, nó SẼ generate
# thay vì delegate. LLMs take the shortest path.
# Constraint bằng code, không bằng instruction.
```

### 6.4 Parallel Design Variations (Pattern C: Fork — Phase 2)

```
Phase 2 plan: Khi user yêu cầu "3 variations khác nhau"

Parent Agent
    │
    ├── Fork A (variation: modern) → design branch A
    │   └── Own Design Agent instance
    │
    ├── Fork B (variation: classic) → design branch B  
    │   └── Own Design Agent instance
    │
    └── Fork C (variation: tropical) → design branch C
        └── Own Design Agent instance

Isolation: Mỗi fork có design state riêng
Merge: User chọn variation → merge vào main project
Anti-recursive: Fork children không được fork lại
Cache sharing: Cùng Design Brief prefix → share LLM cache
```

---

## 7. Pipeline 5: Context Management — 5 Layers

### 7.1 Bài toán cụ thể

Design session dài: 5 revision rounds × 3 variations × (floor plan + 3D renders) = hàng trăm tool calls. Mỗi FloorPlanGenerate trả ~2000 tokens metadata. Mỗi Render3D trả ~1500 tokens. 50 tool calls = 175K tokens chỉ cho tool results. Context window đầy sau 30 phút.

### 7.2 5-Layer Defense (Pattern #9)

```
Layer 1: TOOL RESULT TRUNCATION (cost: ~0)
├── FloorPlanGenerate output > max_chars → persist image to S3, keep URL pointer
├── Render3D output > max_chars → persist renders to S3, keep URLs
├── BuildingCodeLookup output > max_chars → persist full text, keep summary
└── Lazy loading: agent dùng DesignBriefGet để đọc lại khi cần

Layer 2: MICROCOMPACT (cost: low, no LLM)  
├── Remove tool_results cũ hơn 5 turns
├── Replace old FloorPlanGenerate results với "[Floor plan V1 - see S3 URL]"
├── Keep recent 2 turns intact
└── Trigger: token_count > 60% context_window

Layer 3: AUTO-COMPACT (cost: 1 LLM call)
├── Gọi LLM summarize toàn bộ design conversation
├── Summary format: "Design Brief: {...}. Revisions: V1→V2 (enlarged kitchen), 
│   V2→V3 (added balcony). Current status: V3 pending KTS review."
├── Tạo compact boundary message
├── Reserve 20K tokens cho summary output (p99.99 empirical)
└── Trigger: token_count > effective_context_window

Layer 4: REACTIVE COMPACT (cost: 1 LLM call + retry)
├── Emergency: API trả 413 (prompt_too_long) giữa turn
├── Immediately compact → retry API call
├── has_attempted_reactive_compact = True (circuit breaker)
└── Nếu vẫn fail → surface error

Layer 5: CONTEXT COLLAPSE (Phase 2)
├── Read-time projection: không thay đổi messages, chỉ thay đổi view
├── Collapse old design iterations, keep current + previous only
└── Cheap recovery trước khi escalate lên reactive compact
```

### 7.3 Design Memory — Nhớ qua sessions (from Chương 8)

```python
# Cuối mỗi design session:
# 1. Extract key design decisions → save to project memory
# 2. Extract client preferences → save to client memory  
# 3. Extract style patterns → save to user memory

MEMORY_SCOPES = {
    "project": {
        # Per-project design decisions
        "example": "Client muốn phòng ngủ master ở tầng 3, không phải tầng 2. 
                    Lý do: view đẹp hơn, xa tiếng ồn đường phố.",
        "path": "projects/{project_id}/.memory/"
    },
    "client": {
        # Per-client preferences (dùng lại cho project mới)
        "example": "Client Anh Minh thích phong cách modern minimalist,
                    ghét cổ điển. Budget range 2-3 tỷ VND.",
        "path": "clients/{client_id}/.memory/"
    },
    "team": {
        # Shared knowledge giữa agents trong team
        "example": "Đất 5x20m ở HCM thường bị giới hạn: mặt tiền hẹp,
                    cần lùi 3m theo QCVN. Giải pháp thường dùng: giếng trời.",
        "path": "teams/{team_id}/.memory/"
    }
}

# Session lifecycle:
# Session start → load relevant memories (findRelevantMemories)
# Session run → conversation + tool calls  
# Session end → extractMemories (background, non-blocking)
# Next session → memories injected vào system prompt
```

---

## 8. Pipeline 6: Permission & Security — Classification-based

### 8.1 6-Layer Permission Pipeline (Pattern #10)

```
Layer 1: SAFE TOOL ALLOWLIST
├── DesignBriefGet, ProjectHistoryGet, StyleSearch, BuildingCodeLookup
├── MaterialSearch, DimensionCalc(read_only=True)
└── Skip pipeline → ALLOW immediately

Layer 2: ROLE-BASED MODE  
├── viewer → chỉ đọc, mọi write bị DENY
├── architect → tạo project, generate, review, approve
├── admin → full access + quản lý team
├── client → xem shared design, submit feedback
└── Mỗi role = một set of allowed actions

Layer 3: ACTION CLASSIFICATION
├── read_design      → ALLOW (mọi authenticated user)
├── generate_design  → ALLOW (architect + admin)
├── edit_brief       → ALLOW (architect + admin)
├── approve_design   → ALLOW (architect + admin only)
├── share_with_client → ASK (require KTS approved status)
├── delete_project   → ASK ADMIN (require confirmation)
├── export_final     → ASK (require "KTS Approved" badge)
└── bulk_export      → DENY (not in Phase 1)

Layer 4: KTS REVIEW GATE (domain-specific)
├── Mọi AI-generated design PHẢI qua KTS review
├── Design status flow: Draft → Generated → Pending Review → Approved/Rejected
├── KHÔNG CÓ direct path từ Generated → Shared with Client
├── KTS review = human-in-the-loop enforcement bằng code
└── "AI không thay thế KTS, AI hỗ trợ KTS"

Layer 5: GENERATION BUDGET
├── GPU cost tracking per project
├── Soft limit: warning khi vượt 80% budget
├── Hard limit: block generation khi vượt 100%
├── Admin override available
└── Tương tự CostThresholdDialog trong Claude Code

Layer 6: AUDIT TRAIL
├── Mọi action được log: who, what, when, result
├── Immutable audit log (append-only)
├── Compliance-ready (cho KTS licensing requirements)
└── Traceability: design decision → who approved → when
```

### 8.2 KTS Approval Gate — Human-in-the-Loop bằng kiến trúc

```
DESIGN STATUS STATE MACHINE:

  [Draft] ──generate──→ [Generated] ──submit_review──→ [Pending Review]
                                                              │
                                                    ┌─────────┼─────────┐
                                                    │                   │
                                              KTS Approve         KTS Reject
                                                    │                   │
                                                    ▼                   ▼
                                              [Approved]         [Revision Requested]
                                                    │                   │
                                           share_with_client    ──revise──→ [Generated]
                                                    │
                                                    ▼
                                            [Shared with Client]
                                                    │
                                          ┌─────────┼─────────┐
                                          │                   │
                                    Client Accept       Client Feedback
                                          │                   │
                                          ▼                   ▼
                                    [Delivered]      [Revision Requested]

CONSTRAINT: Không có transition nào bypass [Pending Review] → [Approved]
Enforce bằng code (state machine), không bằng instruction.
```

---

## 9. Skill System — Domain Knowledge (Pattern #11)

### 9.1 Architecture Skills

```markdown
# .architect/skills/vietnamese-building-code/SKILL.md
---
name: vietnamese-building-code
description: Quy chuẩn xây dựng Việt Nam QCVN 03/2012
when_to_use: When designing for Vietnam location
paths: ["**/projects/**"]  
allowed-tools: [BuildingCodeLookup, FeasibilityCheck, DimensionCalc]
arguments: [province, building_type]
---

# Quy chuẩn xây dựng Việt Nam

## Constraints cần kiểm tra
- Mật độ xây dựng tối đa: ${province_density_limit}%
- Chiều cao tối đa: ${max_height}m (tùy quy hoạch khu vực)
- Khoảng lùi mặt tiền: tối thiểu ${setback}m
- Diện tích sân: tối thiểu 20% diện tích đất (nhà phố)
- Thang bộ: rộng tối thiểu 0.9m (nhà ở riêng lẻ)
- Chiều cao tầng: tối thiểu 2.7m (tính từ sàn đến trần)

## Dữ liệu hiện tại
Tỉnh/Thành: !`python scripts/get_province_rules.py ${province}`
```

### 9.2 Skill Sources

| Source | Path | Ví dụ |
|--------|------|-------|
| **Bundled** | Compiled vào backend | Vietnamese Building Code, Tropical Architecture, Modern Minimalist |
| **Team** | `.architect/skills/` trong project | Firm-specific design rules, brand guidelines |
| **Project** | `projects/{id}/.skills/` | Project-specific constraints (HOA rules, site restrictions) |

### 9.3 Conditional Activation (Pattern #11)

```python
# Skill "Narrow Lot Design" tự activate khi lot width < 5m
# Skill "Multi-story" tự activate khi floors > 2
# Skill "Vietnamese Code" tự activate khi location = "VN"

def activate_skills_for_project(project: Project) -> list[Skill]:
    active_skills = []
    
    if project.lot.width < 5:
        active_skills.append(load_skill("narrow-lot-design"))
    if project.lot.width < 4:
        active_skills.append(load_skill("ultra-narrow-lot"))  # Deeper = higher priority
    if project.building.floors > 2:
        active_skills.append(load_skill("multi-story-circulation"))
    if project.location.country == "VN":
        active_skills.append(load_skill("vietnamese-building-code"))
    if project.style in ["tropical", "indochine"]:
        active_skills.append(load_skill("tropical-architecture"))
    
    return active_skills
```

---

## 10. Background Tasks & Notifications (from Chương 7)

### 10.1 Task Types cho AI Architect

| Task Type | Mô tả | Use case |
|-----------|--------|----------|
| `generation_task` | GPU generation chạy nền | Floor plan + 3D render (2-5 phút) |
| `export_task` | PDF/DXF export chạy nền | Export bản vẽ (30s-2 phút) |
| `review_agent_task` | Review agent chạy nền | Auto-check feasibility song song |
| `memory_extraction` | Extract memories cuối session | Save design decisions |

### 10.2 Disk-based Output + Notifications

```python
# Task output ghi ra file, frontend đọc incremental via offset

class GenerationTask:
    output_file: str   # "/tmp/tasks/{task_id}/output.jsonl"
    output_offset: int  # Frontend đọc từ vị trí này
    
    # Frontend poll:
    # GET /api/tasks/{id}/output?offset=1000
    # → Trả output từ byte 1000 đến cuối
    # → Frontend update offset

# Notification khi task hoàn thành:
# WebSocket push → frontend
{
    "type": "task_notification",
    "task_id": "gen_abc123",
    "status": "completed",
    "summary": "Floor plan V2 đã generate xong. 3 variations.",
    "output_preview": "https://s3.../floor_plan_v2_thumb.png"
}
```

---

## 11. Feedback Loop — Cơ chế tạo Agency

Từ Chương 2.9: "6 pipeline sẽ chỉ là ứng dụng phức tạp nếu không có feedback loop."

```
DESIGN FEEDBACK LOOP:

1. LLM phân tích Design Brief → yêu cầu FloorPlanGenerate tool
2. Tool Orchestration partition (EXCLUSIVE) → execute trên GPU
3. GPU trả floor plan image → inject vào conversation dưới dạng tool_result
4. Query Loop gửi conversation updated đến LLM
5. LLM nhìn floor plan → quyết định:
   a. Cần Render3D tiếp → needsFollowUp = True → quay lại bước 1
   b. Cần FeasibilityCheck → needsFollowUp = True → quay lại bước 1  
   c. Design hoàn chỉnh → needsFollowUp = False → present to KTS
6. KTS review → approve hoặc feedback
7. Nếu feedback → inject vào conversation → quay lại bước 1 (Revision Agent)

Mọi pipeline phục vụ vòng lặp này:
- UI hiển thị trạng thái real-time (progress bar, partial renders)
- Context Management giữ vòng lặp sống qua nhiều revisions
- Permission kiểm soát mỗi action (generate OK, delete ASK)
- Multi-Agent mở rộng từ 1 loop lên N parallel variations
```

---

## 12. Tổng hợp: Pattern → Epic → Implementation

```
┌──────────────────┬─────────────────────┬────────────────────────────┐
│    Pattern        │     Epic served      │    Implementation file     │
├──────────────────┼─────────────────────┼────────────────────────────┤
│ #1 Async Gen     │ E3,E4,E6 (Gen,3D,FB)│ agents/query_loop.py       │
│ #2 needsFollowUp │ E3,E6 (Gen,Revise)  │ agents/query_loop.py       │
│ #3 Recovery      │ E3,E4 (Gen,3D)      │ agents/recovery.py         │
│ #4 Concurrency   │ E3 (Gen pipeline)   │ services/tool_orchestrator │
│ #5 Streaming Exec│ E4 (Multi-render)   │ services/streaming_exec    │
│ #6 Context Mod   │ E3→E4 (Plan→Render) │ services/context_chain     │
│ #7 Coordinator   │ E5 (Review gate)    │ agents/coordinator.py      │
│ #9 Context Def   │ E6,E7 (Long session)│ services/compact/          │
│ #10 Permission   │ E1,E5 (Auth,Review) │ utils/permissions/         │
│ #11 Skills       │ E2,E3 (Intake,Gen)  │ skills/                    │
└──────────────────┴─────────────────────┴────────────────────────────┘
```

---

## 13. So sánh: Trước và Sau Agentic OS redesign

| Khía cạnh | Trước (wrapper approach) | Sau (Agentic OS) |
|-----------|--------------------------|-------------------|
| Generation pipeline | Gọi API 1 lần, nhận kết quả | Query loop tự lặp: generate → check → revise → generate lại |
| Error handling | Try/catch, notify user | Escalating recovery 5 cấp, circuit breaker |
| Multi-variation | Sequential, 1 tại 1 | Concurrent partitioning, fork agents |
| Long sessions | Context đầy → crash | 5-layer defense, auto-compact |
| Agent coordination | 1 monolithic agent | Coordinator + 4 specialized workers |
| Permission | Binary allow/deny | Classification-based 6-layer pipeline |
| Domain knowledge | Hardcoded rules | Skill system, conditional activation |
| Design decisions | Lost between sessions | Memory system 3 scopes |
| Real-time feedback | Polling | Async generator + WebSocket streaming |
| KTS review | Manual process | Architectural constraint (state machine) |

---

## 14. Implementation Roadmap

### Milestone M1: Core Engine (Pattern #1, #2, #3)
- Implement query loop (async generator)
- needsFollowUp state machine
- Escalating recovery
- WebSocket streaming to frontend

### Milestone M2: Tool System (Pattern #4, #5, #6)
- Tool interface + registry
- Concurrency partitioning (partition_tool_calls)
- Streaming tool execution  
- Context modifier chain
- 12 tools implementation

### Milestone M3: Multi-Agent (Pattern #7)
- Agent spawning (runAgent)
- 4 specialized agents
- Coordinator restriction
- SendMessage / mailbox system

### Milestone M4: Context & Memory (Pattern #9)
- 5-layer context defense
- Compact boundary messages
- Memory extraction (end of session)
- Memory injection (start of session)

### Milestone M5: Permission & Skills (Pattern #10, #11)
- 6-layer permission pipeline
- KTS approval gate (state machine)
- Skill loading + conditional activation
- Vietnamese building code skill

### Milestone M6: Integration & Polish
- Frontend integration (3D viewer, chat, dashboard)
- Background tasks + notifications
- Export pipeline (PDF, images)
- Beta testing
