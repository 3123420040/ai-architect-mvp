# Phase 1 – UI Design Decisions

*Ngày tạo: Apr 11, 2026*
*Design System: Vercel-inspired (Geist + Monochrome + Shadow-as-border)*
*Tech Stack: Next.js 14 + Tailwind CSS + shadcn/ui*

---

## 1. Design Philosophy

### Tại sao chọn Vercel-style?

AI Architect là nền tảng chuyên nghiệp dành cho công ty thiết kế kiến trúc. Giao diện cần:

| Yêu cầu | Vercel-style giải quyết thế nào |
|----------|--------------------------------|
| Chuyên nghiệp, không rối mắt | Monochrome palette — content nổi bật, chrome biến mất |
| Tập trung vào visual (floor plan, 3D render) | Gallery emptiness — whitespace lớn để hình ảnh thiết kế chiếm sân khấu |
| Phân biệt rõ trạng thái (draft/approved/rejected) | Workflow accent colors — mỗi trạng thái có màu riêng, gắn vào ngữ cảnh |
| Dùng được cho cả KTS lẫn end-user không chuyên | Minimal chrome + clear hierarchy — ai cũng đọc được |
| Developer-grade precision cho annotation/measurement | Geist Mono + technical label system — chính xác như IDE |

### Nguyên tắc cốt lõi

1. **Content-first, chrome-last** — Giao diện là khung trưng bày cho floor plan và 3D render, không phải là thứ cạnh tranh sự chú ý.
2. **Shadow-as-border** — Dùng `box-shadow: 0px 0px 0px 1px` thay CSS border truyền thống. Nhẹ hơn, tinh tế hơn, transition mượt hơn.
3. **Monochrome + Semantic color** — Palette chính là grayscale (`#171717` → `#ffffff`). Màu chỉ xuất hiện khi mang ý nghĩa: trạng thái version, workflow step, alert.
4. **Compressed text, expanded space** — Heading dùng negative letter-spacing tạo cảm giác "minified". Whitespace xung quanh rộng rãi để cân bằng.
5. **Three weights, strict roles** — 400 (đọc), 500 (tương tác), 600 (nhấn mạnh). Không dùng 700 bold trên body text.

---

## 2. Color System Decisions

### Primary Palette (Achromatic)

| Token | Hex | Vai trò |
|-------|-----|---------|
| `--color-foreground` | `#171717` | Text chính, heading, icon. Không dùng pure black — micro-warmth giảm harsh. |
| `--color-background` | `#ffffff` | Nền trang, card surface, button text trên dark |
| `--color-muted` | `#4d4d4d` | Text phụ, description, subtitle |
| `--color-subtle` | `#666666` | Text bậc 3, muted link, placeholder |
| `--color-border` | `rgba(0,0,0,0.08)` | Shadow-border thay CSS border |
| `--color-surface` | `#fafafa` | Surface nhẹ, inner glow của card, stripe row |
| `--color-divider` | `#ebebeb` | Divider, card outline, image border |

### Workflow Status Colors (Semantic)

Hệ thống AI Architect có version state machine phức tạp. Mỗi trạng thái cần màu riêng để KTS và end-user nhận diện ngay:

| Token | Hex | Trạng thái | Khi nào dùng |
|-------|-----|------------|--------------|
| `--color-status-draft` | `#666666` | Draft | Version vừa tạo, chưa generate |
| `--color-status-generating` | `#0a72ef` | Generating | AI đang generate floor plan / 3D |
| `--color-status-review` | `#f59e0b` | Under Review | Chờ KTS duyệt |
| `--color-status-approved` | `#10b981` | Approved | KTS đã approve |
| `--color-status-rejected` | `#ef4444` | Rejected | KTS reject, cần revision |
| `--color-status-locked` | `#171717` | Locked | Canonical truth — immutable |
| `--color-status-handoff` | `#8b5cf6` | Handoff Ready | Sẵn sàng bàn giao |
| `--color-status-superseded` | `#9ca3af` | Superseded | Version cũ bị thay thế |

**Quyết định:** Status colors chỉ xuất hiện ở badge, dot indicator, và status bar — KHÔNG dùng làm background trang hay tô màu card.

### Interactive Colors

| Token | Hex | Vai trò |
|-------|-----|---------|
| `--color-link` | `#0072f5` | Link text |
| `--color-focus` | `hsla(212, 100%, 48%, 1)` | Focus ring — accessibility |
| `--color-primary-cta` | `#171717` | Button CTA chính (dark) |
| `--color-primary-cta-text` | `#ffffff` | Text trên button CTA |

### Workspace Accent Colors

Mỗi workspace có accent color riêng để user nhận biết mình đang ở đâu:

| Workspace | Accent | Hex | Lý do |
|-----------|--------|-----|-------|
| End-User (Gallery, Chat) | Blue | `#0a72ef` | Thân thiện, tin cậy — giống "Develop" của Vercel |
| KTS Review | Amber | `#f59e0b` | Cẩn trọng, review — signaling "cần attention" |
| Admin Dashboard | Neutral | `#171717` | Authority, quản trị — monochrome thuần |
| Delivery/Contractor | Purple | `#8b5cf6` | Formal, bàn giao — phân biệt rõ với flow chính |

---

## 3. Typography Decisions

### Font Selection

| Loại | Font | Lý do |
|------|------|-------|
| **Primary** | `Geist Sans` | Font chính của Vercel ecosystem. Geometric, negative tracking ở display size. Đi kèm Next.js ecosystem. |
| **Monospace** | `Geist Mono` | Dùng cho technical label (kích thước phòng, diện tích, version ID), code block, measurement. |
| **Fallback** | `Arial, system-ui, sans-serif` | Đảm bảo render đúng khi font chưa load |

### Quyết định tracking (letter-spacing)

Letter-spacing giảm dần theo font size — đặc trưng nhận dạng của Vercel style:

| Size | Tracking | Ví dụ trong AI Architect |
|------|----------|--------------------------|
| 48px | -2.4px | Hero dashboard: "AI Architect" |
| 40px | -2.4px | Section heading: "Phương án thiết kế" |
| 32px | -1.28px | Card heading: "Option A — Hiện đại tối giản" |
| 24px | -0.96px | Sub-heading: "Mặt bằng tầng 1" |
| 16px | -0.32px | Strong label, active nav |
| 14px | normal | Button, link, caption |
| 12px | normal | Meta, tag, timestamp |

### Weight System

| Weight | Role | Ví dụ |
|--------|------|-------|
| 400 | Reading — body text, description | Mô tả brief, annotation comment |
| 500 | Interactive — UI element, nav link | Button label, tab title, nav item |
| 600 | Emphasis — heading, strong label | Page title, card heading, metric number |

**Quyết định:** KHÔNG dùng weight 700 (bold) ở bất kỳ đâu ngoại trừ micro-badge (7px). Hierarchy tạo bằng size + tracking, không bằng weight.

### OpenType Features

- `font-feature-settings: "liga"` bật trên toàn bộ Geist text — ligatures là structural, không decorative
- `font-feature-settings: "tnum"` bật trên số liệu (diện tích, kích thước, metric) — tabular numbers giúp align cột

---

## 4. Shadow & Depth Decisions

### Shadow-as-border: Kỹ thuật nền tảng

```css
/* KHÔNG dùng */
border: 1px solid #ebebeb;

/* DÙNG thay thế */
box-shadow: 0px 0px 0px 1px rgba(0, 0, 0, 0.08);
```

**Lý do:**
- Shadow nằm ở layer riêng → không ảnh hưởng box model
- Border-radius smooth hơn, không bị clipping
- Transition mượt khi hover (shadow opacity 0.08 → 0.12)
- Cho phép stack nhiều layer shadow trong 1 property

### Elevation Scale

| Level | Shadow | Dùng cho |
|-------|--------|----------|
| **L0 — Flat** | none | Background, text block, inline |
| **L1 — Ring** | `rgba(0,0,0,0.08) 0px 0px 0px 1px` | Card resting state, input field, divider line |
| **L1b — Light Ring** | `rgb(235,235,235) 0px 0px 0px 1px` | Tab, image container, lighter elements |
| **L2 — Subtle** | L1 + `rgba(0,0,0,0.04) 0px 2px 2px` | Standard card, list item |
| **L3 — Elevated** | L1 + L2 + `rgba(0,0,0,0.04) 0px 8px 8px -8px` + `#fafafa 0px 0px 0px 1px` | Featured card, selected option, hover state |
| **L4 — Focus** | `2px solid hsla(212, 100%, 48%, 1)` | Keyboard focus ring — accessibility |

**Quyết định quan trọng:** Inner `#fafafa` ring ở L3 tạo "glow from within" — đây là chi tiết nhỏ nhưng tạo nên cảm giác "built, not floating" của card. Không bỏ qua.

### Áp dụng vào AI Architect

| Component | Level | Lý do |
|-----------|-------|-------|
| Floor plan card (resting) | L2 | Standard card, nhiều card grid cùng lúc |
| Floor plan card (selected/hover) | L3 | Nổi bật option đang chọn |
| 3D Render preview | L1b | Image container, nhẹ nhàng |
| Chat message bubble | L1 | Minimal, không cạnh tranh nội dung |
| Review annotation pin | L3 | Cần nổi bật trên floor plan |
| Navigation bar | L1 (bottom border) | Sticky header, subtle separation |
| Modal / Dialog | L3 + backdrop overlay | Elevated above content |
| Status badge | L0 | Badge nổi bằng color, không cần shadow |

---

## 5. Component Pattern Decisions

### Button Hierarchy

| Variant | Style | Dùng khi |
|---------|-------|----------|
| **Primary** | Dark bg (`#171717`), white text, 6px radius | CTA chính: "Generate Design", "Approve", "Export PDF" |
| **Secondary** | White bg, shadow-border, dark text, 6px radius | Action phụ: "Compare", "View History", "Save Draft" |
| **Ghost** | Transparent bg, dark text, no border | Action nhẹ: "Cancel", "Skip", link-like button |
| **Destructive** | Red bg (`#ef4444`), white text | "Reject Design", "Delete Project" |
| **Pill Badge** | Tinted bg + dark text, 9999px radius | Status: "Approved", "Draft", "Under Review" |

**Quyết định:** Pill radius (9999px) CHỈ dùng cho badge/tag/status — KHÔNG dùng cho primary button.

### Card Patterns

| Pattern | Dùng cho | Đặc điểm |
|---------|----------|-----------|
| **Option Card** | Floor plan variation (Option A, B, C) | Thumbnail lớn, title, description ngắn, Select action |
| **Render Card** | 3D render gallery | Image full-width, caption, download icon |
| **Project Card** | Dashboard project list | Status badge, client name, date, thumbnail nhỏ |
| **Review Card** | KTS review queue item | Floor plan thumb, project info, status, reviewer assignment |
| **Metric Card** | Dashboard stats | Large number (Geist 48px/600), label below |
| **Version Card** | Version history timeline | Thumbnail, version number, date, status, change reason |

### Form Patterns

| Pattern | Dùng cho |
|---------|----------|
| **Chat Input** | Intake chatbot — full-width, auto-expand, send button |
| **Multi-step Form** | Structured intake — step indicator, prev/next, validation |
| **Annotation Input** | Pin marker + text input — appears on click position |
| **Feedback Textarea** | Client/KTS feedback — character count, submit |
| **Brief Editor** | Editable design brief — section-based, inline edit |

### Navigation Pattern

| Component | Mô tả |
|-----------|--------|
| **Top Nav** | Sticky white header. Logo left, workspace tabs center, user/notifications right. Shadow-border bottom. |
| **Workspace Switcher** | Tab pills cho End-User / KTS Review / Admin / Delivery. Active tab = dark bg. |
| **Project Sidebar** | Left sidebar trong workspace. Project tree, version list, quick actions. Collapsible trên mobile. |
| **Breadcrumb** | Dashboard > Project Name > Version N > Floor Plan. Geist 14px/500. |

---

## 6. Layout Architecture Decisions

### Workspace Layouts

```
┌──────────────────────────────────────────────────────────────┐
│  [Logo]    [End-User] [KTS Review] [Admin]    [🔔] [Avatar] │  ← Top Nav (sticky, 56px)
├──────────────────────────────────────────────────────────────┤
│         │                                                     │
│ Project │              Main Content                           │
│ Sidebar │                                                     │
│  240px  │          (max-width: 1200px, centered)              │
│         │                                                     │
│ • Proj  │                                                     │
│ • Vers  │                                                     │
│ • Files │                                                     │
│         │                                                     │
└─────────┴─────────────────────────────────────────────────────┘
```

### Key Screen Layouts

**Dashboard** — Grid layout
```
┌─────────────────────────────────────────────────┐
│  Stats Bar: [N Projects] [N Pending] [N Approved]│
├─────────────────────────────────────────────────┤
│  [Project Card] [Project Card] [Project Card]   │
│  [Project Card] [Project Card] [+ New Project]  │
└─────────────────────────────────────────────────┘
```

**Intake Chat** — Centered single-column
```
┌─────────────────────────────────────────────────┐
│           Chat Messages (max-w: 720px)           │
│  ┌─────────────────────────────────────────┐    │
│  │ AI: Xin chào! Cho tôi biết kích thước...│    │
│  └─────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────┐    │
│  │ User: Đất 5x20m, muốn xây 4 tầng       │    │
│  └─────────────────────────────────────────┘    │
│  ┌──────────────────────────────────┐  [Send]   │
│  │ Nhập tin nhắn...                 │           │
│  └──────────────────────────────────┘           │
└─────────────────────────────────────────────────┘
```

**Option Gallery** — Card grid
```
┌─────────────────────────────────────────────────┐
│  "Phương án thiết kế" (h2, 32px/600/-1.28px)    │
│                                                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │  Option A │  │  Option B │  │  Option C │      │
│  │  [thumb]  │  │  [thumb]  │  │  [thumb]  │      │
│  │  Modern   │  │  Classic  │  │  Tropical │      │
│  │  [Select] │  │  [Select] │  │  [Select] │      │
│  └──────────┘  └──────────┘  └──────────┘      │
└─────────────────────────────────────────────────┘
```

**KTS Review Workspace** — Split panel
```
┌───────────────────────────────┬──────────────────┐
│                               │  Review Panel     │
│     Floor Plan / 3D Viewer    │                   │
│     (interactive, zoomable)   │  Brief Summary    │
│                               │  Annotations List │
│                               │  [Approve]        │
│                               │  [Request Revise] │
│                               │  [Reject]         │
└───────────────────────────────┴──────────────────┘
```

**Version Compare** — Side-by-side
```
┌──────────────────────┬──────────────────────┐
│  Version 2           │  Version 3           │
│  [Floor Plan]        │  [Floor Plan]        │
│  Status: Rejected    │  Status: Under Review│
│  Date: Apr 10        │  Date: Apr 11        │
├──────────────────────┴──────────────────────┤
│  Diff Summary: "Phòng ngủ 3: 12m² → 15m²"  │
└─────────────────────────────────────────────┘
```

---

## 7. Responsive Strategy

### Breakpoints

| Name | Width | Layout Changes |
|------|-------|----------------|
| `sm` | < 640px | Single column, sidebar collapse, bottom nav |
| `md` | 640–768px | 2-column card grid, sidebar overlay |
| `lg` | 768–1024px | Full card grid, sidebar visible |
| `xl` | 1024–1280px | Standard desktop layout |
| `2xl` | > 1280px | Max-width centered, generous margins |

### Mobile-specific Decisions

- **Sidebar** → Bottom sheet hoặc hamburger menu
- **Option cards** → Horizontal scroll (swipeable) thay vì grid
- **Review workspace** → Tab switch giữa floor plan và review panel (không split)
- **3D Viewer** → Full screen mode, pinch-to-zoom, swipe-to-rotate
- **Chat** → Full height, input fixed bottom

### Touch Targets

- Minimum 44x44px cho tất cả interactive elements
- Button padding tối thiểu 8px vertical, 16px horizontal
- Annotation pin kích thước 32x32px, tap area 48x48px

---

## 8. Accessibility Decisions

| Concern | Decision |
|---------|----------|
| Color contrast | `#171717` trên `#ffffff` = ratio 15.4:1 (vượt WCAG AAA). `#4d4d4d` trên `#ffffff` = 7.7:1 (pass AAA). |
| Focus ring | `2px solid hsla(212, 100%, 48%, 1)` — visible, saturated blue. Không ẩn focus ring. |
| Status indicators | Status badge dùng cả color + text label + icon. Không chỉ dùng color alone. |
| Screen reader | Tất cả image (floor plan, render) phải có alt text mô tả. 3D viewer có text fallback. |
| Keyboard nav | Tab order logic: nav → sidebar → main content. Focus trap trong modal/dialog. |
| Motion | `prefers-reduced-motion` → disable animation, crossfade thay slide. |

---

## 9. Dark Mode Decision

**Phase 1: KHÔNG triển khai dark mode.**

Lý do:
- Floor plan và 3D render cần hiển thị trên nền trắng để chính xác màu sắc
- KTS annotation tools cần contrast rõ ràng trên light background
- PDF export (CONCEPT DESIGN watermark) render trên nền trắng
- Dark mode tăng gấp đôi design token set → complexity không cần thiết ở MVP

**Phase 2+:** Cân nhắc dark mode cho 3D Viewer standalone (immersive viewing) và Admin dashboard.

---

## 10. Animation & Motion Decisions

| Interaction | Animation | Duration | Easing |
|------------|-----------|----------|--------|
| Card hover | Shadow L2 → L3 | 150ms | ease-out |
| Tab switch | Content crossfade | 200ms | ease-in-out |
| Modal open | Fade in + scale 0.95→1 | 200ms | ease-out |
| Modal close | Fade out + scale 1→0.95 | 150ms | ease-in |
| Toast/Notification | Slide in from top-right | 300ms | ease-out |
| Progress bar | Width animation | 16ms (each frame) | linear |
| 3D Viewer orbit | Physics-based | — | momentum decay |
| Chat message appear | Fade + slide up 8px | 200ms | ease-out |

**Quyết định:** Tất cả transition dưới 300ms. Không dùng bounce, spring, hay animation phức tạp. UI nhanh, gọn, professional — giống Vercel.

---

## 11. Key Design Decisions Log

| # | Quyết định | Lý do | Alternative đã xét |
|---|-----------|-------|---------------------|
| D-01 | Vercel-style monochrome | Professional, content-first, phù hợp B2B architecture tool | Material Design (quá generic), Linear-style (quá dark cho floor plan) |
| D-02 | Shadow-as-border toàn hệ thống | Consistent, smooth, layerable | CSS border (box model issues, transition jerky) |
| D-03 | Geist font family | Đi kèm Next.js, aggressive tracking = identity | Inter (phổ thông quá), SF Pro (chỉ Apple) |
| D-04 | Status badge bằng pill (9999px) + tinted bg | Nhận diện nhanh, không chiếm diện tích | Sidebar color strip (chiếm space), icon-only (không rõ) |
| D-05 | Chat-first intake | Tự nhiên, giảm cognitive load cho end-user | Form-first (rigid), wizard (quá nhiều bước) |
| D-06 | Split panel cho KTS review | Floor plan + context cùng lúc, giảm switching | Full-screen + sidebar drawer (mất context khi mở drawer) |
| D-07 | Gallery whitespace > compact grid | Floor plan cần space để "thở", giống gallery triển lãm | Dense grid (rối, khó so sánh) |
| D-08 | No dark mode Phase 1 | Accuracy cho visual content, giảm complexity | Full dark mode (double token set, floor plan contrast issues) |
| D-09 | Workspace accent colors | KTS biết ngay mình ở workspace nào | Uniform color (confusing khi switch) |
| D-10 | Inner fafafa ring trên card | Subtle glow tạo depth, Vercel signature | Flat card (mất sophistication) |
