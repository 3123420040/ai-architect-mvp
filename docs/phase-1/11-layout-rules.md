# Phase 1 – Layout Rules

*Ngày tạo: Apr 11, 2026*
*Grid System: CSS Grid + Flexbox via Tailwind CSS*
*Reference: Vercel whitespace philosophy*

---

## 1. Layout Philosophy

### Vercel-inspired Principles Applied to AI Architect

1. **Gallery emptiness** — Floor plan và 3D render cần "thở". Whitespace lớn giữa các phần tử giúp user tập trung vào thiết kế, không bị overwhelm bởi UI chrome.

2. **Compressed text, expanded space** — Heading dùng negative tracking (chữ nén), nhưng padding xung quanh rộng rãi. Text nén + space rộng = tension tạo visual interest.

3. **Border-as-rhythm** — Section separation bằng shadow-border và spacing, KHÔNG bằng background color. Tránh striped section pattern (section trắng / section xám xen kẽ).

4. **Content density scales with role** — End-user workspace sparser, KTS review workspace denser. Admin dashboard densest.

---

## 2. Grid System

### 2.1 Page Grid

```
Max content width: 1200px
Centered with auto margins
Gutter (column gap): 24px
Padding (page edge): 24px (desktop), 16px (mobile)
```

### 2.2 Column Patterns

| Pattern | Columns | Dùng cho |
|---------|---------|----------|
| **Single** | 1 col, max-w 720px | Chat intake, focused content |
| **Two-equal** | 2 col, 1fr 1fr | Version compare side-by-side |
| **Two-asymmetric** | main (1fr) + panel (360px) | KTS review workspace |
| **Three-equal** | 3 col, 1fr 1fr 1fr | Option gallery (desktop) |
| **Dashboard grid** | auto-fill, minmax(300px, 1fr) | Project card grid |
| **Sidebar layout** | sidebar (240px) + main (1fr) | App shell with sidebar |

### 2.3 Responsive Column Collapse

```
Desktop (≥1024px):  3-column grid
Tablet  (768–1023): 2-column grid
Mobile  (<768px):   1-column stack

Option Gallery specific:
- ≥1024px: 3 cards per row
- 640–1023px: 2 cards per row, horizontal scroll option
- <640px: 1 card, horizontal swipe carousel
```

---

## 3. Spacing Rules

### 3.1 Section Spacing (Vertical rhythm)

| Context | Desktop | Mobile | Token |
|---------|---------|--------|-------|
| Between major page sections | 80px | 48px | `--space-20` / `--space-12` |
| Between sub-sections | 48px | 32px | `--space-12` / `--space-8` |
| Section heading → content | 32px | 24px | `--space-8` / `--space-6` |
| Between cards in grid | 24px | 16px | `--space-6` / `--space-4` |
| Between list items | 8px | 8px | `--space-2` |
| Between form fields | 16px | 16px | `--space-4` |
| Label → input | 6px | 6px | `--space-1.5` |

### 3.2 Component Internal Spacing

| Component | Padding | Internal Gap |
|-----------|---------|--------------|
| Card | 24px | 16px |
| Card compact | 16px | 12px |
| Button default | 8px 16px | 8px (icon ↔ text) |
| Button small | 6px 12px | 6px |
| Input | 8px 12px | — |
| Badge/Pill | 2px 10px | 4px (icon ↔ text) |
| Chat bubble | 12px 16px | — |
| Nav item | 8px 12px | 8px (icon ↔ text) |
| Modal | 24px | 16px |
| Table cell | 12px 16px | — |
| Toast | 12px 16px | 8px |
| Tooltip | 4px 8px | — |

### 3.3 Page Edge Padding

| Viewport | Edge Padding |
|----------|-------------|
| ≥1280px | 32px (content centered, max-w 1200px) |
| 1024–1279px | 24px |
| 768–1023px | 20px |
| 640–767px | 16px |
| <640px | 16px |

### 3.4 The 16→32 Jump Rule

Giống Vercel, spacing scale nhảy từ 16px → 32px (bỏ 20px, 24px cho gap). 24px chỉ dùng cho **padding bên trong** component, KHÔNG dùng cho gap giữa components. 

```
Đúng: gap-4 (16px) hoặc gap-8 (32px) giữa các card
Sai:  gap-5 (20px) hoặc gap-6 (24px) giữa các card

Đúng: p-6 (24px) bên trong card
```

---

## 4. Screen Layouts — Detailed Rules

### 4.1 Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│  TopNav (56px, fixed)                                        │
├────────────┬────────────────────────────────────────────────┤
│            │  ┌── Stats Bar (surface bg, 72px) ──────────┐ │
│            │  │  [12 Projects] [3 Pending] [5 Approved]   │ │
│  Sidebar   │  └──────────────────────────────────────────┘ │
│  (240px)   │                                                │
│            │  ┌── Filter Bar ────────────────────────────┐ │
│            │  │  [Search...] [Status ▾] [Grid|List] [+New]│ │
│            │  └──────────────────────────────────────────┘ │
│            │         gap: 24px                              │
│            │  ┌────────┐ ┌────────┐ ┌────────┐            │
│            │  │ Proj 1 │ │ Proj 2 │ │ Proj 3 │            │
│            │  │        │ │        │ │        │            │
│            │  └────────┘ └────────┘ └────────┘            │
│            │         gap: 24px                              │
│            │  ┌────────┐ ┌────────┐ ┌──────────────────┐  │
│            │  │ Proj 4 │ │ Proj 5 │ │  + Tạo dự án mới │  │
│            │  └────────┘ └────────┘ └──────────────────┘  │
└────────────┴────────────────────────────────────────────────┘
```

**Rules:**
- Stats bar: full content width, surface bg, shadow-border bottom
- Filter bar: flex, items center, gap 12px
- Project grid: CSS Grid, `auto-fill, minmax(300px, 1fr)`, gap 24px
- Content padding: 32px top (below stats), 24px horizontal
- "+ New" card: dashed border, centered content

### 4.2 Intake — Chat Mode

```
┌─────────────────────────────────────────────────────────────┐
│  TopNav                                                      │
├────────────┬────────────────────────────────────────────────┤
│            │                                                │
│  Sidebar   │  ┌──── Chat Area (max-w: 720px, centered) ──┐ │
│            │  │                                            │ │
│            │  │  ┌── AI message ──────────────────────┐   │ │
│            │  │  │ Xin chào! Cho tôi biết...         │   │ │
│            │  │  └────────────────────────────────────┘   │ │
│            │  │                                            │ │
│            │  │          ┌── User message ────────────┐   │ │
│            │  │          │ Đất 5x20m, 4 tầng         │   │ │
│            │  │          └────────────────────────────┘   │ │
│            │  │                                            │ │
│            │  │  ┌── AI message ──────────────────────┐   │ │
│            │  │  │ Tôi hiểu. Để xác nhận:            │   │ │
│            │  │  │ • Kích thước: 5m x 20m            │   │ │
│            │  │  │ • Số tầng: 4                       │   │ │
│            │  │  └────────────────────────────────────┘   │ │
│            │  │                                            │ │
│            │  │  ┌── Input Bar ───────────────────────┐   │ │
│            │  │  │ Nhập tin nhắn...           📎 ➤   │   │ │
│            │  │  └────────────────────────────────────┘   │ │
│            │  └────────────────────────────────────────────┘ │
└────────────┴────────────────────────────────────────────────┘
```

**Rules:**
- Chat container: max-w 720px, margin auto (centered)
- Messages: gap 16px between messages
- AI messages: align left, max-w 85% of chat width
- User messages: align right, max-w 75% of chat width
- Input bar: sticky bottom, within chat container
- Brief card: appears inline in chat when brief is complete, full chat width
- Scroll: auto-scroll to bottom on new message

### 4.3 Intake — Form Mode

```
┌─────────────────────────────────────────────────────────────┐
│  TopNav                                                      │
├────────────┬────────────────────────────────────────────────┤
│            │                                                │
│  Sidebar   │  ┌──── Form Area (max-w: 640px, centered) ──┐ │
│            │  │                                            │ │
│            │  │  ── Step Indicator ───────────────────     │ │
│            │  │  (1)──(2)──(3)──(4)──(5)                  │ │
│            │  │   ●    ○    ○    ○    ○                   │ │
│            │  │                                            │ │
│            │  │  ── Form Content ─────────────────────     │ │
│            │  │  Chiều rộng (m) *                          │ │
│            │  │  ┌──────────────────────────┐              │ │
│            │  │  │ 5                         │              │ │
│            │  │  └──────────────────────────┘              │ │
│            │  │                                gap: 16px   │ │
│            │  │  Chiều sâu (m) *                           │ │
│            │  │  ┌──────────────────────────┐              │ │
│            │  │  │ 20                        │              │ │
│            │  │  └──────────────────────────┘              │ │
│            │  │                                            │ │
│            │  │  ── Navigation ───────────────────────     │ │
│            │  │  [← Quay lại]              [Tiếp theo →]  │ │
│            │  └────────────────────────────────────────────┘ │
└────────────┴────────────────────────────────────────────────┘
```

**Rules:**
- Form container: max-w 640px, centered
- Step indicator: full form width, height 48px, margin-bottom 32px
- Form fields: full width, gap 16px
- Two-column fields (width + depth): side-by-side on desktop, stacked on mobile
- Navigation: flex, justify-between, sticky bottom or after form content
- Validation error: appears below field, red text, 6px margin-top

### 4.4 Option Gallery

```
┌─────────────────────────────────────────────────────────────┐
│  TopNav                                                      │
├────────────┬────────────────────────────────────────────────┤
│            │                                                │
│  Sidebar   │  ┌── Section Header ────────────────────────┐ │
│            │  │  "Phương án thiết kế"     [Regenerate ↻]  │ │
│            │  └──────────────────────────────────────────┘ │
│            │           gap: 32px                            │
│            │  ┌───────────┐ ┌───────────┐ ┌───────────┐   │
│            │  │           │ │           │ │           │   │
│            │  │  [Floor   │ │  [Floor   │ │  [Floor   │   │
│            │  │   Plan    │ │   Plan    │ │   Plan    │   │
│            │  │   Image]  │ │   Image]  │ │   Image]  │   │
│            │  │           │ │           │ │           │   │
│            │  │ Option A  │ │ Option B  │ │ Option C  │   │
│            │  │ Hiện đại  │ │ Classic   │ │ Tropical  │   │
│            │  │ [Chọn]    │ │ [Chọn]    │ │ [Chọn]    │   │
│            │  └───────────┘ └───────────┘ └───────────┘   │
│            │           gap: 24px                            │
│            │  ┌── Selected Action Bar ───────────────────┐ │
│            │  │  Option A đã chọn  [Xem chi tiết] [Next →]│ │
│            │  └──────────────────────────────────────────┘ │
└────────────┴────────────────────────────────────────────────┘
```

**Rules:**
- Section header: flex, justify-between, align-center
- Card grid: 3 columns (≥1024px), gap 24px
- Cards: equal height (CSS Grid auto-rows)
- Image ratio: 4:3
- Selected card: shadow-focus ring, check icon overlay
- Action bar: sticky bottom, surface bg, shadow-border top, padding 16px
- Mobile: horizontal swipe carousel with dots indicator

### 4.5 KTS Review Workspace

```
┌─────────────────────────────────────────────────────────────┐
│  TopNav                                                      │
├────────────┬──────────────────────────────┬─────────────────┤
│            │                              │                  │
│  Sidebar   │  Floor Plan Viewer           │  Review Panel    │
│            │  (flex-1, interactive)        │  (360px fixed)   │
│            │                              │                  │
│            │  ┌────────────────────────┐  │  Brief Summary   │
│            │  │                        │  │  ┌────────────┐  │
│            │  │    [Floor Plan with    │  │  │ 5x20m...   │  │
│            │  │     Annotation Pins]   │  │  └────────────┘  │
│            │  │                        │  │                  │
│            │  │    ① "Cửa sổ hướng    │  │  Annotations     │
│            │  │        Tây quá nóng"   │  │  ┌────────────┐  │
│            │  │                        │  │  │ ① Comment  │  │
│            │  │    ② "Phòng ngủ nhỏ"  │  │  │ ② Comment  │  │
│            │  │                        │  │  │ ③ Comment  │  │
│            │  └────────────────────────┘  │  └────────────┘  │
│            │                              │                  │
│            │  ┌── View Tabs ───────────┐  │  ┌────────────┐  │
│            │  │ [Tầng 1] [Tầng 2] ... │  │  │ [Approve]  │  │
│            │  └────────────────────────┘  │  │ [Revise]   │  │
│            │                              │  │ [Reject]   │  │
│            │                              │  └────────────┘  │
└────────────┴──────────────────────────────┴─────────────────┘
```

**Rules:**
- Split layout: flex, no gap (shared border via shadow)
- Floor plan area: flex-1, min-w 0 (prevent overflow)
- Review panel: fixed 360px width, border-left `--shadow-border`
- Panel sections: scrollable independently
- Floor tabs: line variant, below viewer
- Action buttons: sticky bottom of panel, bg white, shadow-border top
- Mobile: tab switch between viewer and panel (NOT side-by-side)
- Annotation pins: positioned absolutely on floor plan, z-index 40

### 4.6 Version Compare

```
┌─────────────────────────────────────────────────────────────┐
│  TopNav                                                      │
├────────────┬────────────────────────────────────────────────┤
│            │                                                │
│  Sidebar   │  ┌── Compare Header ────────────────────────┐ │
│            │  │  Version 2 vs Version 3    [Close ✕]      │ │
│            │  └──────────────────────────────────────────┘ │
│            │                                                │
│            │  ┌──────────────────┬──────────────────┐      │
│            │  │   Version 2      │   Version 3      │      │
│            │  │   Apr 10, 2026   │   Apr 11, 2026   │      │
│            │  │   [Rejected]     │   [Under Review]  │      │
│            │  │                  │                   │      │
│            │  │   [Floor Plan]   │   [Floor Plan]   │      │
│            │  │   (synced zoom)  │   (synced zoom)  │      │
│            │  │                  │                   │      │
│            │  └──────────────────┴──────────────────┘      │
│            │                                                │
│            │  ┌── Diff Summary ──────────────────────────┐ │
│            │  │  • Phòng ngủ 3: 12m² → 15m²              │ │
│            │  │  • Bếp di chuyển sang phía Đông           │ │
│            │  │  • Thêm ban công tầng 3                    │ │
│            │  └──────────────────────────────────────────┘ │
└────────────┴────────────────────────────────────────────────┘
```

**Rules:**
- Two-column equal split, gap 0 (border between)
- Both floor plans: same scale, same orientation
- Synced interaction: zoom/pan on one syncs to the other
- Header per column: version info + StatusBadge
- Diff summary: below compare area, full width, surface bg
- Mobile: vertical stack (version 2 top, version 3 bottom)

### 4.7 3D Viewer Full Screen

```
┌─────────────────────────────────────────────────────────────┐
│  TopNav (semi-transparent on dark viewer)                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│                    3D Model Viewer                            │
│                    (full viewport)                            │
│                                                              │
│   ┌── Controls ──┐                                          │
│   │ [Exterior]   │                                          │
│   │ [Floor Plan] │                                          │
│   │ [Section]    │                                          │
│   │ [+] [-]      │                                          │
│   │ [Reset]      │                                          │
│   └──────────────┘                                          │
│                                                              │
│                              ┌── Room Info ──────────────┐  │
│                              │ Phòng khách               │  │
│                              │ 24.5 m² │ 5.0m × 4.9m    │  │
│                              └──────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Rules:**
- Viewer: full viewport minus nav height
- Background: `--color-foreground` (dark) for immersive viewing
- Controls: absolute positioned, bottom-left, bg rgba(0,0,0,0.7), rounded
- Room info popup: absolute, near clicked room, white card, shadow-elevated
- Nav: semi-transparent when over viewer, full opacity on hover
- No sidebar in full-screen viewer mode
- ESC or close button to exit full-screen

### 4.8 Export / Delivery

```
┌─────────────────────────────────────────────────────────────┐
│  TopNav                                                      │
├────────────┬────────────────────────────────────────────────┤
│            │                                                │
│  Sidebar   │  ┌── Page Header ───────────────────────────┐ │
│            │  │  "Hồ sơ bàn giao"  [Tạo bundle mới]      │ │
│            │  └──────────────────────────────────────────┘ │
│            │                                                │
│            │  ┌── Current Bundle Card ───────────────────┐ │
│            │  │  ★ Official Handoff Bundle                │ │
│            │  │  Version 3 — Approved Apr 11              │ │
│            │  │                                            │ │
│            │  │  📄 concept-package.pdf     4.2 MB  [↓]  │ │
│            │  │  🖼️ renders.zip             28 MB   [↓]  │ │
│            │  │  📐 floor-plans-svg.zip     1.1 MB  [↓]  │ │
│            │  │                                            │ │
│            │  │  [Tải tất cả ↓]                           │ │
│            │  └──────────────────────────────────────────┘ │
│            │                                                │
│            │  ┌── Previous Bundles (collapsed) ──────────┐ │
│            │  │  ▸ Version 2 — Superseded Apr 10          │ │
│            │  │  ▸ Version 1 — Superseded Apr 9           │ │
│            │  └──────────────────────────────────────────┘ │
└────────────┴────────────────────────────────────────────────┘
```

**Rules:**
- Single column, max-w `--width-content-max`
- Current bundle: prominent card, shadow-elevated
- File list: table-like layout, icon + name + size + download button
- Previous bundles: collapsed accordion, muted style
- Readiness labels: badge next to each file

---

## 5. Navigation Rules

### 5.1 TopNav Behavior

| Viewport | Behavior |
|----------|----------|
| ≥768px | Full horizontal nav: logo + workspace tabs + actions |
| <768px | Logo + hamburger menu + notification icon |

- Always sticky (position: fixed, top: 0)
- Z-index: `--z-sticky` (10)
- Shadow-border bottom
- Height: 56px fixed

### 5.2 Sidebar Behavior

| Viewport | Behavior |
|----------|----------|
| ≥1024px | Persistent, open by default (240px) |
| 768–1023px | Collapsed (56px, icons only), expandable on hover |
| <768px | Hidden, accessible via hamburger menu (overlay) |

- Z-index: `--z-sidebar` (20)
- Transition: width change, `--duration-medium`
- Active item: surface bg + foreground text + left accent bar (2px)

### 5.3 Breadcrumb Rules

- Position: top of main content area, below nav
- Format: `Dashboard / Project Name / Version N / Current View`
- Separator: `/` character, `--color-subtle-foreground`
- Current page: `--color-foreground`, `--font-medium`
- Previous pages: `--color-link`, clickable
- Mobile: show only last 2 levels, "..." for truncated path

---

## 6. Image & Media Rules

### 6.1 Floor Plan Images

| Property | Value |
|----------|-------|
| Aspect ratio | 4:3 (card thumbnail) or natural (detail view) |
| Border | 1px solid `--color-divider` |
| Border radius | `--radius-xl` (12px) for cards, 0 for full-width viewer |
| Min resolution | 2048x2048px source, responsive display |
| Loading | Skeleton placeholder → fade in |
| Zoom | Click to lightbox (gallery), native pan/zoom (viewer) |

### 6.2 3D Renders

| Property | Value |
|----------|-------|
| Aspect ratio | 16:9 |
| Border | 1px solid `--color-divider` |
| Border radius | `--radius-xl` (12px) |
| Resolution | 1920x1080px minimum |
| Loading | Blur placeholder → sharp |
| Download | Click download icon → original resolution PNG |

### 6.3 Thumbnails

| Context | Size | Radius |
|---------|------|--------|
| Project card | 100% width, 16:9 | `--radius-xl` top corners |
| Version timeline | 48px square | `--radius-sm` |
| Chat reference image | 200px max-width | `--radius-lg` |
| Style library | 120px square | `--radius-md` |

---

## 7. Overflow & Scroll Rules

### 7.1 Scroll Behavior

| Area | Scroll |
|------|--------|
| Page body | Vertical, smooth scroll |
| Sidebar nav | Vertical, independent of main |
| Chat messages | Vertical, auto-scroll to bottom |
| Review panel | Vertical, independent |
| Floor plan viewer | Pannable (no page scroll) |
| 3D viewer | Orbit (no page scroll) |
| Option gallery (mobile) | Horizontal swipe |
| Table (wide) | Horizontal scroll |

### 7.2 Scroll Indicators

- Custom scrollbar: thin (6px), `--color-divider` track, `--color-subtle-foreground` thumb
- Horizontal scroll: fade gradient on edges (8px)
- Auto-scroll: smooth behavior, scroll-margin-top = nav height

### 7.3 Overflow Prevention

- Text: `text-overflow: ellipsis` with `line-clamp-2` for card descriptions
- Tables: horizontal scroll wrapper on mobile
- Images: `object-fit: cover` for thumbnails, `object-fit: contain` for floor plans

---

## 8. Responsive Breakpoint Rules — Summary

### Mobile (<640px)

```
- Single column everything
- Sidebar hidden → hamburger menu
- Option cards: horizontal carousel
- Review: tab switch (viewer | panel), NOT split
- 3D Viewer: full screen
- Nav: logo + hamburger + bell
- Section spacing: 48px
- Edge padding: 16px
- Typography: display 32px, h1 28px, h2 24px
```

### Tablet (640–1023px)

```
- 2-column card grids
- Sidebar: collapsed (icons only)
- Review: still tab switch on <768px, split on ≥768px
- Nav: full horizontal
- Section spacing: 48px–64px
- Edge padding: 20px
- Typography: display 40px, h1 32px, h2 28px
```

### Desktop (≥1024px)

```
- Full layout: sidebar + main + optional panel
- 3-column card grids
- Review: split panel
- Nav: full horizontal with workspace tabs
- Section spacing: 80px
- Edge padding: 24px–32px
- Typography: full scale (display 48px, h1 40px, h2 32px)
```

---

## 9. Do's and Don'ts — Layout

### Do

- Dùng gap-based spacing (CSS gap) thay margin trên children
- Dùng max-width constraint cho content → center với auto margin
- Dùng shadow-border cho separation, không dùng background color alternation
- Dùng CSS Grid cho 2D layouts (card grid, dashboard), Flexbox cho 1D layouts (nav, button group)
- Test layout ở 3 breakpoints: 375px (iPhone SE), 768px (iPad), 1280px (laptop)
- Giữ consistent padding bên trong cùng loại component
- Dùng aspect-ratio CSS property cho image containers

### Don't

- Không hardcode width/height bằng pixel cho responsive content
- Không dùng negative margin để fix spacing issues — fix source
- Không dùng `position: absolute` cho layout (chỉ cho overlay, annotation pin, popup)
- Không để content chạm edge màn hình — luôn có edge padding
- Không mix column patterns trong cùng 1 section (vd: 3-col rồi 2-col)
- Không dùng fixed height cho card — để content quyết định height (CSS Grid auto-rows giúp equal height)
- Không hardcode sidebar width bên trong component — dùng layout token
- Không bỏ qua mobile carousel cho option gallery — 3 card stack trên mobile quá dài

---

## 10. Performance Rules

| Rule | Threshold |
|------|-----------|
| Largest Contentful Paint (LCP) | < 2.5s |
| First Input Delay (FID) | < 100ms |
| Cumulative Layout Shift (CLS) | < 0.1 |
| 3D model initial load | < 5s cho model < 50MB |
| Image lazy loading | Tất cả images below fold |
| Skeleton loading | Hiện skeleton trong 200ms nếu content chưa ready |
| Font loading | `font-display: swap` cho Geist — FOUT OK, FOIT not OK |
| Floor plan images | Next.js Image component với srcset |
| 3D viewer | Lazy import Three.js bundle — chỉ load khi user mở tab |
