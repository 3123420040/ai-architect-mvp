# Phase 1 – Component List

*Ngày tạo: Apr 11, 2026*
*UI Library: shadcn/ui + custom components*
*Styling: Tailwind CSS + Vercel design tokens*

---

## 1. Component Architecture

```
components/
├── ui/                    ← shadcn/ui primitives (customized)
│   ├── button.tsx
│   ├── input.tsx
│   ├── dialog.tsx
│   └── ...
├── layout/                ← Layout shells
│   ├── app-shell.tsx
│   ├── top-nav.tsx
│   ├── sidebar.tsx
│   └── workspace-layout.tsx
├── common/                ← Shared business components
│   ├── status-badge.tsx
│   ├── version-timeline.tsx
│   ├── project-card.tsx
│   └── ...
├── intake/                ← Module M2
│   ├── chat-interface.tsx
│   ├── intake-form.tsx
│   └── brief-editor.tsx
├── generation/            ← Module M5
│   ├── option-gallery.tsx
│   ├── option-card.tsx
│   └── generation-progress.tsx
├── viewer/                ← Module M7
│   ├── viewer-3d.tsx
│   ├── floor-plan-viewer.tsx
│   └── measurement-tool.tsx
├── review/                ← Module M6
│   ├── review-workspace.tsx
│   ├── annotation-layer.tsx
│   └── review-actions.tsx
├── export/                ← Module M8
│   ├── export-dialog.tsx
│   └── pdf-preview.tsx
└── dashboard/             ← Module M1+M9
    ├── project-list.tsx
    ├── stats-bar.tsx
    └── notification-panel.tsx
```

---

## 2. Foundation Components (shadcn/ui Customized)

Các component cơ bản dựa trên shadcn/ui, customize theo Vercel design tokens.

### 2.1 Button

| Variant | Appearance | Token usage |
|---------|------------|-------------|
| `default` (primary) | Dark bg, white text | `bg-primary text-primary-foreground rounded-md shadow-border` |
| `secondary` | White bg, shadow-border | `bg-background text-foreground rounded-md shadow-border` |
| `ghost` | Transparent, no border | `bg-transparent text-foreground hover:bg-surface` |
| `destructive` | Red bg, white text | `bg-destructive text-destructive-foreground rounded-md` |
| `link` | Text-only, underline | `text-link underline-offset-4 hover:text-link-hover` |
| `outline` | White bg, light ring | `bg-background shadow-border-light rounded-md` |

| Size | Padding | Font | Height |
|------|---------|------|--------|
| `sm` | 6px 12px | 14px/500 | 32px |
| `default` | 8px 16px | 14px/500 | 40px |
| `lg` | 10px 24px | 16px/500 | 48px |
| `icon` | 8px | — | 40px (square) |

**Specs:**
- Border radius: `--radius-md` (6px)
- Focus ring: `--shadow-focus`
- Transition: `--duration-normal` `--ease-out`
- Hover (primary): opacity 0.9
- Hover (secondary): shadow-border opacity 0.08 → 0.12

### 2.2 Input

| Variant | Dùng cho |
|---------|----------|
| `default` | Text input — lot dimensions, project name |
| `textarea` | Free-text — feedback, special requests |
| `search` | Dashboard search — with search icon left |
| `number` | Numeric — dimensions (m), budget (VND) |

**Specs:**
- Height: `--height-input` (40px)
- Padding: 8px 12px
- Border: `--shadow-border` (shadow-as-border)
- Focus: `--shadow-focus` (2px blue ring)
- Font: `--text-body-sm` (16px/400)
- Placeholder: `--color-subtle-foreground`
- Radius: `--radius-md` (6px)

### 2.3 Dialog / Modal

**Specs:**
- Backdrop: `--color-overlay-backdrop`
- Surface: `--color-overlay-surface`, `--radius-2xl` (16px)
- Shadow: `--shadow-elevated`
- Padding: 24px
- Title: `--text-h3` (24px/600/-0.96px)
- Description: `--text-body-sm` (16px/400), `--color-muted-foreground`
- Animation: fade + scale 0.95→1, `--duration-medium`
- Close button: top-right, ghost button with X icon
- Z-index: `--z-modal`

### 2.4 Dropdown / Popover

**Specs:**
- Surface: white, `--shadow-elevated`
- Radius: `--radius-lg` (8px)
- Item padding: 8px 12px
- Item hover: `--color-surface`
- Separator: 1px `--color-divider`
- Z-index: `--z-dropdown`
- Animation: fade + slide 4px down, `--duration-normal`

### 2.5 Tabs

| Variant | Dùng cho |
|---------|----------|
| `line` | Content tabs — version details, floor plans per floor |
| `pill` | Workspace switcher — End-User / KTS Review / Admin |

**Line tabs specs:**
- Font: `--text-label` (14px/500)
- Active: `--color-foreground`, underline 2px
- Inactive: `--color-subtle-foreground`
- Border bottom: `--shadow-border-light`

**Pill tabs specs:**
- Font: `--text-label` (14px/500)
- Active: `--color-primary` bg, `--color-primary-foreground` text
- Inactive: transparent bg, `--color-muted-foreground` text
- Radius: `--radius-pill-sm` (64px)
- Padding: 6px 16px

### 2.6 Toast / Notification

| Variant | Icon | Color |
|---------|------|-------|
| `default` | Info circle | `--color-foreground` |
| `success` | Check circle | `--color-status-approved` |
| `error` | Alert triangle | `--color-status-rejected` |
| `warning` | Alert circle | `--color-status-review` |

**Specs:**
- Position: top-right, stacked
- Surface: white, `--shadow-elevated`
- Radius: `--radius-lg` (8px)
- Padding: 12px 16px
- Z-index: `--z-toast`
- Animation: slide in from right, `--duration-slow`
- Auto-dismiss: 5s (configurable)
- Title: `--text-label` (14px/500)
- Description: `--text-caption` (12px/400), `--color-muted-foreground`

### 2.7 Tooltip

**Specs:**
- Surface: `--color-foreground` (dark tooltip)
- Text: `--color-background` (white), `--text-caption` (12px/400)
- Radius: `--radius-sm` (4px)
- Padding: 4px 8px
- Z-index: `--z-tooltip`
- Delay: 500ms before show
- Arrow: 4px

### 2.8 Avatar

| Size | Dimension | Font |
|------|-----------|------|
| `sm` | 24px | 10px |
| `default` | 32px | 12px |
| `lg` | 40px | 14px |

**Specs:**
- Radius: `--radius-circle` (50%)
- Fallback: initials on `--color-surface` bg
- Border: `--shadow-border-light`

### 2.9 Skeleton / Loading

**Specs:**
- Background: `--color-surface` → `--color-divider` shimmer
- Radius: match component being loaded
- Animation: pulse, 1.5s infinite

---

## 3. Layout Components

### 3.1 AppShell

Container chính cho toàn bộ app. Quản lý top nav + sidebar + main content area.

```
Props:
- workspace: 'user' | 'review' | 'admin' | 'delivery'
- sidebarOpen: boolean
- children: ReactNode
```

**Layout:**
- Top nav: fixed, full-width, height `--height-nav` (56px)
- Sidebar: fixed left, width `--width-sidebar` (240px), below nav
- Main: margin-left = sidebar width, padding-top = nav height
- Mobile: sidebar hidden, main full-width

### 3.2 TopNav

Sticky horizontal navigation.

```
Sections:
- Left: Logo (AI Architect wordmark)
- Center: Workspace tabs (pill variant)
- Right: Notification bell + User avatar + dropdown
```

**Specs:**
- Height: 56px
- Background: `--color-background`
- Border bottom: `--shadow-border`
- Logo: Geist 16px/600, `--color-foreground`
- Z-index: `--z-sticky`

### 3.3 Sidebar

Project navigation sidebar.

```
Sections:
- Project selector (dropdown)
- Navigation items:
  - Overview
  - Design Brief
  - Floor Plans (with version sub-items)
  - 3D Renders
  - 3D Viewer
  - Version History
  - Export
- Team members (avatar stack)
```

**Specs:**
- Width: 240px (expanded), 56px (collapsed, icon only)
- Background: `--color-background`
- Border right: `--shadow-border`
- Nav item: 8px 12px padding, `--text-body-sm` (16px/400)
- Active item: `--color-surface` bg, `--color-foreground` text, `--font-medium`
- Hover: `--color-surface` bg
- Section label: `--text-caption` (12px/500) uppercase, `--color-subtle-foreground`

### 3.4 WorkspaceLayout

Defines the main content area structure per workspace type.

| Workspace | Layout |
|-----------|--------|
| End-User | Single column, centered, max-w `--width-content-max` |
| KTS Review | Split panel — floor plan left + review panel right |
| Admin | Grid dashboard, full-width stats bar |
| Delivery | Single column, bundle list |

---

## 4. Business Components — Common

### 4.1 StatusBadge

Pill badge cho version/project status.

```
Props:
- status: 'draft' | 'generating' | 'review' | 'approved' | 'rejected' | 'locked' | 'handoff' | 'superseded'
- size: 'sm' | 'default'
```

**Specs:**
- Radius: `--radius-full` (9999px)
- Padding: 2px 10px (default), 1px 8px (sm)
- Font: `--text-caption` (12px/500)
- Color: `--color-status-{status}` text + `--color-status-{status}-bg` background
- Icon: optional dot/icon left (8px)

### 4.2 ProjectCard

Card hiển thị project trên dashboard.

```
Props:
- project: { name, client, status, thumbnail, updatedAt, assignee }
- onClick: () => void
```

**Specs:**
- Shadow: `--shadow-subtle` (resting), `--shadow-elevated` (hover)
- Radius: `--radius-lg` (8px)
- Padding: 0 (image top) + 16px (content)
- Thumbnail: aspect-ratio 16/9, `--radius-xl` top corners, object-cover
- Title: `--text-body-sm` (16px/600/-0.32px)
- Client: `--text-caption` (12px/400), `--color-muted-foreground`
- Footer: StatusBadge + date + assignee avatar
- Transition: shadow `--duration-normal`

### 4.3 VersionTimeline

Timeline hiển thị version history.

```
Props:
- versions: Array<{ id, number, status, date, reason, thumbnail }>
- currentVersionId: string
- onSelect: (id) => void
```

**Specs:**
- Orientation: vertical
- Node: 12px circle, colored by status
- Line: 1px `--color-divider`, connecting nodes
- Entry: thumbnail (48px), version label (Geist Mono 13px/500), date, StatusBadge
- Current: ring highlight `--shadow-focus`
- Hover: `--color-surface` bg

### 4.4 MetricCard

Card hiển thị số liệu trên dashboard.

```
Props:
- value: string (e.g., "12", "< 3")
- label: string (e.g., "Active Projects", "Avg Revision Cycles")
- trend?: 'up' | 'down' | 'neutral'
```

**Specs:**
- Shadow: `--shadow-subtle`
- Radius: `--radius-lg`
- Padding: 24px
- Value: `--text-display` (48px/600/-2.4px)
- Label: `--text-body-sm` (16px/400), `--color-muted-foreground`

### 4.5 EmptyState

Placeholder khi không có data.

```
Props:
- icon: ReactNode
- title: string
- description: string
- action?: { label: string, onClick: () => void }
```

**Specs:**
- Centered trong container
- Icon: 48px, `--color-subtle-foreground`
- Title: `--text-h3` (24px/600)
- Description: `--text-body-sm` (16px/400), `--color-muted-foreground`
- Action: Primary button

### 4.6 FileUpload

Upload zone cho reference images, style library.

```
Props:
- accept: string[] (e.g., ['image/png', 'image/jpeg'])
- maxSize: number (bytes)
- maxFiles: number
- onUpload: (files) => void
```

**Specs:**
- Border: 2px dashed `--color-divider`, `--radius-lg`
- Hover/dragover: border `--color-link`, bg `--color-surface`
- Icon: upload icon, 32px, `--color-subtle-foreground`
- Text: `--text-body-sm`, `--color-muted-foreground`
- Preview: thumbnail grid, 64px each, with remove button

---

## 5. Business Components — Intake (M2)

### 5.1 ChatInterface

Chat UI cho intake chatbot.

```
Props:
- messages: Array<{ role: 'user' | 'ai', content, timestamp }>
- onSend: (message) => void
- isTyping: boolean
- designBrief?: DesignBrief
```

**Sections:**
- Message list (scrollable, max-w `--width-chat-max`)
- Input bar (fixed bottom within container)
- Brief summary card (when brief is complete)

**Message bubble specs:**
- AI message: left-aligned, `--color-surface` bg, `--radius-lg`
- User message: right-aligned, `--color-primary` bg, white text, `--radius-lg`
- Padding: 12px 16px
- Font: `--text-body-sm` (16px/400)
- Timestamp: `--text-caption` (12px/400), `--color-subtle-foreground`
- Typing indicator: 3 bouncing dots, `--color-muted-foreground`

**Input bar specs:**
- Container: `--shadow-border`, `--radius-lg`, white bg
- Input: auto-expanding textarea
- Send button: primary icon button, right side
- Attach button: ghost icon button (reference images)

### 5.2 IntakeForm

Multi-step structured form.

```
Steps:
1. Thông tin lô đất (lot info)
2. Yêu cầu phòng (room requirements)
3. Phong cách & Budget (style & budget)
4. Yêu cầu đặc biệt (special requests)
5. Review & Confirm
```

**Step indicator specs:**
- Horizontal stepper, numbered circles connected by lines
- Active step: `--color-primary` circle, `--font-semibold`
- Completed step: `--color-status-approved` circle with check icon
- Future step: `--color-divider` circle, `--color-subtle-foreground` text
- Font: `--text-caption` (12px/500)

**Form field specs:**
- Label: `--text-label` (14px/500), margin-bottom 6px
- Input: standard Input component
- Error: `--text-caption` (12px/400), `--color-status-rejected`
- Help text: `--text-caption` (12px/400), `--color-subtle-foreground`

### 5.3 BriefEditor

Editable Design Brief display.

```
Props:
- brief: DesignBrief
- editable: boolean
- onChange: (field, value) => void
- onSave: () => void
```

**Specs:**
- Section-based layout (Lot, Rooms, Style, Budget, Lifestyle)
- Each section: collapsible, with edit icon
- Field display: label (mono caption) + value (body)
- Edit mode: inline input fields
- JSON preview: collapsible code block, Geist Mono
- Save action: Primary button, bottom

### 5.4 BriefSummaryCard

Compact brief summary shown after intake confirmation.

**Specs:**
- Shadow: `--shadow-subtle`
- Radius: `--radius-lg`
- Grid: 2-column key-value pairs
- Key: `--text-caption` (12px/500) uppercase, Geist Mono, `--color-subtle-foreground`
- Value: `--text-body-sm` (16px/400)
- Header: "Design Brief" + StatusBadge (Confirmed)

---

## 6. Business Components — Generation (M5)

### 6.1 OptionGallery

Grid hiển thị 2-3 floor plan options.

```
Props:
- options: Array<{ id, name, description, thumbnail, status }>
- selectedId?: string
- onSelect: (id) => void
- onRegenerate: () => void
```

**Specs:**
- Grid: responsive — 1 col (mobile), 2 col (md), 3 col (lg)
- Gap: `--space-6` (24px)
- Header: `--text-h2` (32px/600/-1.28px) + regenerate button
- Empty: EmptyState component

### 6.2 OptionCard

Individual floor plan option card.

```
Props:
- option: { name, description, thumbnail, floors: FloorPlan[] }
- selected: boolean
- onSelect: () => void
- onViewDetail: () => void
```

**Specs:**
- Shadow: `--shadow-subtle` (default), `--shadow-elevated` (hover/selected)
- Selected state: `--shadow-focus` ring
- Radius: `--radius-lg`
- Image: aspect-ratio 4/3, `--radius-xl` top corners
- Content padding: 16px
- Title: `--text-h3` (24px/600/-0.96px) — "Option A"
- Description: `--text-body-sm` (16px/400), `--color-muted-foreground`, max 2 lines
- Footer: "Chọn" button (primary when not selected, secondary when selected)

### 6.3 GenerationProgress

AI generation progress indicator.

```
Props:
- status: 'queued' | 'generating' | 'post-processing' | 'complete' | 'failed'
- progress: number (0-100)
- stage: string (e.g., "Đang tạo mặt bằng tầng 1...")
- estimatedTime?: string
```

**Specs:**
- Container: centered, max-w 480px
- Icon: animated spinner (generating) or check (complete) or alert (failed)
- Stage text: `--text-body` (18px/400), `--color-foreground`
- Progress bar: height 4px, `--radius-full`, bg `--color-divider`, fill `--color-status-generating`
- Estimated time: `--text-caption` (12px/400), `--color-subtle-foreground`
- Fail state: error message + "Retry" button

### 6.4 FloorPlanImage

Full-width floor plan image with zoom.

```
Props:
- src: string
- alt: string
- floorLabel: string (e.g., "Tầng 1")
- dimensions?: { width: number, height: number }
- zoomable: boolean
```

**Specs:**
- Border: 1px solid `--color-divider`
- Radius: `--radius-xl` (12px)
- Label overlay: bottom-left, `--text-mono-caption` (13px/500), bg semi-transparent
- Zoom: click to open lightbox, pinch-to-zoom on mobile
- Loading: Skeleton placeholder

---

## 7. Business Components — Viewer (M7)

### 7.1 Viewer3D

Interactive Three.js 3D viewer.

```
Props:
- modelUrl: string (GLB/GLTF)
- viewMode: 'exterior' | 'floor-plan' | 'section'
- annotations?: Annotation[]
- onRoomClick?: (roomId) => void
```

**Specs:**
- Container: full available width/height, bg `--color-foreground` (dark viewer)
- Controls overlay: bottom-left, transparent dark bg, `--z-3d-controls`
  - View mode toggles: icon buttons (exterior/floor/section)
  - Zoom controls: +/- buttons
  - Reset view button
- Room popup: card overlay on room click, white, `--shadow-elevated`
  - Room name, area (m²), dimensions
- Loading: centered spinner + "Đang tải mô hình 3D..."
- Touch: pinch-to-zoom, swipe-to-rotate, two-finger-pan

### 7.2 FloorPlanViewer

2D floor plan viewer with pan/zoom.

```
Props:
- imageUrl: string
- annotations?: Annotation[]
- annotationMode: boolean
- onAddAnnotation?: (position, comment) => void
```

**Specs:**
- Container: full available width/height, bg white
- Pan: click-drag
- Zoom: scroll wheel, pinch-to-zoom, +/- controls
- Min zoom: fit-to-container
- Max zoom: 5x
- Annotation pins: overlaid at correct coordinates, `--z-annotation`

### 7.3 MeasurementTool

Đo kích thước trên 3D model.

```
Props:
- active: boolean
- measurements: Array<{ pointA, pointB, distance }>
- onMeasure: (pointA, pointB) => void
- onClear: () => void
```

**Specs:**
- Cursor: crosshair when active
- Point marker: 6px circle, `--color-link`
- Line: dashed, 1px, `--color-link`
- Label: `--text-mono-caption` (13px/500), bg white, `--shadow-border`, `--radius-sm`
- Clear button: ghost, "Xóa đo" text

---

## 8. Business Components — Review (M6)

### 8.1 ReviewWorkspace

Main review layout for KTS.

```
Props:
- version: CanonicalVersion
- annotations: Annotation[]
- brief: DesignBrief
- feedbackHistory: Feedback[]
```

**Layout:**
- Left (flex-1): FloorPlanViewer (interactive, with annotation layer)
- Right (`--width-review-panel`, 360px): Review panel
  - Brief summary (collapsible)
  - Annotation list (scrollable)
  - Action buttons (Approve / Request Revision / Reject)

### 8.2 AnnotationLayer

Pin annotations overlaid on floor plan.

```
Props:
- annotations: Array<{ id, position, comment, author, timestamp }>
- editable: boolean
- onAdd: (position) => void
- onSelect: (id) => void
- selectedId?: string
```

**Pin specs:**
- Size: 28px circle
- Background: `--color-status-review` (amber)
- Number: white, `--text-caption` (12px/600)
- Shadow: `--shadow-elevated`
- Selected: scale 1.2 + `--shadow-focus`
- New pin: pulsing animation

**Comment popover:**
- Appears on pin click
- Author avatar + name + timestamp
- Comment text: `--text-body-sm`
- Edit/delete actions (if own annotation)

### 8.3 AnnotationList

Scrollable list of annotations in review panel.

**Item specs:**
- Number badge: 24px circle, amber, white text
- Comment: `--text-body-sm`, truncated 2 lines
- Author: `--text-caption`, `--color-subtle-foreground`
- Click: scroll floor plan to annotation position
- Hover: highlight pin on floor plan

### 8.4 ReviewActions

Approve / Reject / Request Revision buttons.

```
Props:
- onApprove: () => void
- onReject: (reason: string) => void
- onRequestRevision: (feedback: string) => void
- disabled: boolean
```

**Specs:**
- Container: sticky bottom of review panel
- Background: white, `--shadow-border` top
- Padding: 16px
- Buttons: full-width, stacked
  - "Approve" — Primary (dark) + check icon
  - "Yêu cầu chỉnh sửa" — Secondary + edit icon
  - "Reject" — Destructive (ghost variant) + X icon
- Reject/Revision: opens inline textarea for reason (required)

---

## 9. Business Components — Export (M8)

### 9.1 ExportDialog

Modal cho export options.

```
Props:
- version: CanonicalVersion
- availableFormats: ('pdf' | 'svg' | 'dxf' | 'images')[]
- onExport: (format, options) => void
```

**Specs:**
- Dialog component
- Format selection: radio cards with icon + description
- Options per format:
  - PDF: include brief (checkbox), quality (standard/high)
  - Images: resolution select, format (PNG/JPEG)
  - DXF: layers selection
- Export button: Primary, "Xuất [format]"
- Progress: inline progress bar during generation

### 9.2 PdfPreview

Preview PDF before download.

**Specs:**
- Embedded PDF viewer or page-by-page image preview
- Page navigation: prev/next + page number
- Zoom controls
- Download button: Primary
- Watermark visible: "CONCEPT DESIGN – NOT FOR CONSTRUCTION"

---

## 10. Business Components — Dashboard (M1 + M9)

### 10.1 ProjectList

Grid/list of projects on dashboard.

```
Props:
- projects: Project[]
- view: 'grid' | 'list'
- filter: StatusFilter
- search: string
- onCreateNew: () => void
```

**Grid view:** ProjectCard components, responsive grid
**List view:** Table rows with columns: name, client, status, assignee, date, actions

### 10.2 StatsBar

Summary statistics bar at top of dashboard.

```
Props:
- stats: Array<{ label, value, icon }>
```

**Specs:**
- Horizontal row, evenly spaced
- Each stat: MetricCard compact (value 24px/600, label 12px/400)
- Background: `--color-surface`
- Padding: 16px 24px
- Radius: `--radius-lg`
- Shadow: `--shadow-border`

### 10.3 NotificationPanel

Notification dropdown/panel.

```
Props:
- notifications: Array<{ id, type, message, project, timestamp, read }>
- onMarkRead: (id) => void
- onMarkAllRead: () => void
```

**Specs:**
- Trigger: Bell icon in TopNav, with unread count badge (red dot)
- Panel: dropdown, max-h 400px, scrollable
- Item: padding 12px 16px, border-bottom `--color-divider`
- Unread: `--color-surface` background, dot indicator
- Read: white background
- Type icon: varies by notification type
- Message: `--text-body-sm`, `--color-foreground`
- Timestamp: `--text-caption`, `--color-subtle-foreground`
- "Đánh dấu tất cả đã đọc": ghost link, top-right

### 10.4 DeliveryBundleCard

Card for handoff bundle in delivery workspace.

```
Props:
- bundle: { id, version, files, createdAt, approver, status }
- onDownload: () => void
- onView: () => void
```

**Specs:**
- Shadow: `--shadow-subtle`
- Radius: `--radius-lg`
- Header: version name + StatusBadge (handoff_ready / delivered)
- File list: icon + filename + size + readiness label
- Footer: "Tải về" primary button + "Xem chi tiết" secondary
- Approver: avatar + name + date

---

## 11. Component Naming Conventions

| Rule | Ví dụ |
|------|-------|
| PascalCase cho component | `StatusBadge`, `OptionCard` |
| kebab-case cho file | `status-badge.tsx`, `option-card.tsx` |
| Props interface = ComponentName + Props | `StatusBadgeProps`, `OptionCardProps` |
| Variant dùng prop, không tạo component riêng | `<Button variant="destructive">` |
| Compound component cho complex | `<ReviewWorkspace.Panel>`, `<ReviewWorkspace.Actions>` |
| "use" prefix cho hooks | `useAnnotations()`, `useGenerationStatus()` |

---

## 12. Component Priority (Implementation Order)

### P0 — Must Have (MVP launch)

| # | Component | Module | Lý do |
|---|-----------|--------|-------|
| 1 | AppShell, TopNav, Sidebar | M1 | Shell cho toàn bộ app |
| 2 | Button, Input, Dialog (shadcn) | — | Foundation cho mọi thứ |
| 3 | StatusBadge | — | Dùng ở khắp nơi |
| 4 | ChatInterface | M2 | Core intake flow |
| 5 | IntakeForm | M2 | Backup intake |
| 6 | BriefEditor | M2 | KTS edit brief |
| 7 | OptionGallery + OptionCard | M5 | Hiển thị floor plan options |
| 8 | GenerationProgress | M5 | UX khi AI generate |
| 9 | FloorPlanViewer | M7 | Xem floor plan chi tiết |
| 10 | ReviewWorkspace + AnnotationLayer | M6 | KTS review gate |
| 11 | ReviewActions | M6 | Approve/reject |
| 12 | ProjectList + ProjectCard | M1 | Dashboard |
| 13 | ExportDialog | M8 | PDF export |
| 14 | VersionTimeline | M4 | Version tracking |

### P1 — Should Have

| # | Component | Module |
|---|-----------|--------|
| 15 | Viewer3D | M7 |
| 16 | MeasurementTool | M7 |
| 17 | NotificationPanel | M1 |
| 18 | StatsBar + MetricCard | M1 |
| 19 | BriefSummaryCard | M2 |
| 20 | AnnotationList | M6 |

### P2 — Nice to Have

| # | Component | Module |
|---|-----------|--------|
| 21 | DeliveryBundleCard | M9 |
| 22 | PdfPreview | M8 |
| 23 | FileUpload (style library) | M3 |
