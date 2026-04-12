# Phase 1 – Design Tokens

*Ngày tạo: Apr 11, 2026*
*Format: CSS Custom Properties → Tailwind config mapping*
*Reference: Vercel Geist Design System*

---

## 1. Cách sử dụng

Design token được định nghĩa dưới dạng CSS custom properties trong `:root` và map sang Tailwind config. Mọi component phải dùng token — KHÔNG hardcode hex value trực tiếp.

```css
/* globals.css */
:root {
  /* Colors */
  --color-foreground: #171717;
  --color-background: #ffffff;
  /* ... */
}
```

```ts
// tailwind.config.ts
export default {
  theme: {
    extend: {
      colors: {
        foreground: 'var(--color-foreground)',
        background: 'var(--color-background)',
        // ...
      }
    }
  }
}
```

---

## 2. Color Tokens

### 2.1 Core Palette

| Token | Value | Tailwind Class | Dùng cho |
|-------|-------|----------------|----------|
| `--color-foreground` | `#171717` | `text-foreground` | Text chính, heading, icon |
| `--color-background` | `#ffffff` | `bg-background` | Page background, card surface |
| `--color-muted-foreground` | `#4d4d4d` | `text-muted-foreground` | Text phụ, description |
| `--color-subtle-foreground` | `#666666` | `text-subtle-foreground` | Text bậc 3, placeholder |
| `--color-disabled-foreground` | `#808080` | `text-disabled-foreground` | Disabled state text |
| `--color-surface` | `#fafafa` | `bg-surface` | Subtle background tint, table stripe |
| `--color-divider` | `#ebebeb` | `border-divider` | Image border, explicit divider line |

### 2.2 Shadow-Border Tokens

| Token | Value | Dùng cho |
|-------|-------|----------|
| `--shadow-border` | `rgba(0, 0, 0, 0.08) 0px 0px 0px 1px` | Shadow-as-border standard |
| `--shadow-border-light` | `rgb(235, 235, 235) 0px 0px 0px 1px` | Lighter ring — tab, image |
| `--shadow-subtle` | `rgba(0, 0, 0, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 2px 2px` | Standard card |
| `--shadow-elevated` | `rgba(0,0,0,0.08) 0px 0px 0px 1px, rgba(0,0,0,0.04) 0px 2px 2px, rgba(0,0,0,0.04) 0px 8px 8px -8px, #fafafa 0px 0px 0px 1px` | Featured card, hover, selected |
| `--shadow-focus` | `0 0 0 2px hsla(212, 100%, 48%, 1)` | Focus ring |

### 2.3 Status Colors

| Token | Value | Tailwind Class | Trạng thái |
|-------|-------|----------------|------------|
| `--color-status-draft` | `#666666` | `text-status-draft` | Draft |
| `--color-status-draft-bg` | `#f3f4f6` | `bg-status-draft` | Draft badge bg |
| `--color-status-generating` | `#0a72ef` | `text-status-generating` | AI đang generate |
| `--color-status-generating-bg` | `#ebf5ff` | `bg-status-generating` | Generating badge bg |
| `--color-status-review` | `#d97706` | `text-status-review` | Under Review |
| `--color-status-review-bg` | `#fef3c7` | `bg-status-review` | Review badge bg |
| `--color-status-approved` | `#059669` | `text-status-approved` | Approved |
| `--color-status-approved-bg` | `#d1fae5` | `bg-status-approved` | Approved badge bg |
| `--color-status-rejected` | `#dc2626` | `text-status-rejected` | Rejected |
| `--color-status-rejected-bg` | `#fee2e2` | `bg-status-rejected` | Rejected badge bg |
| `--color-status-locked` | `#171717` | `text-status-locked` | Locked (canonical) |
| `--color-status-locked-bg` | `#e5e7eb` | `bg-status-locked` | Locked badge bg |
| `--color-status-handoff` | `#7c3aed` | `text-status-handoff` | Handoff Ready |
| `--color-status-handoff-bg` | `#ede9fe` | `bg-status-handoff` | Handoff badge bg |
| `--color-status-superseded` | `#9ca3af` | `text-status-superseded` | Superseded |
| `--color-status-superseded-bg` | `#f3f4f6` | `bg-status-superseded` | Superseded badge bg |

### 2.4 Interactive Colors

| Token | Value | Tailwind Class | Dùng cho |
|-------|-------|----------------|----------|
| `--color-link` | `#0072f5` | `text-link` | Link text |
| `--color-link-hover` | `#005bc4` | `hover:text-link-hover` | Link hover |
| `--color-focus` | `hsla(212, 100%, 48%, 1)` | — | Focus ring (dùng qua shadow) |
| `--color-primary` | `#171717` | `bg-primary` | Primary button bg |
| `--color-primary-foreground` | `#ffffff` | `text-primary-foreground` | Primary button text |
| `--color-destructive` | `#ef4444` | `bg-destructive` | Destructive button |
| `--color-destructive-foreground` | `#ffffff` | `text-destructive-foreground` | Destructive button text |

### 2.5 Workspace Accent Colors

| Token | Value | Workspace |
|-------|-------|-----------|
| `--color-accent-user` | `#0a72ef` | End-User workspace |
| `--color-accent-user-bg` | `#ebf5ff` | End-User accent background |
| `--color-accent-review` | `#f59e0b` | KTS Review workspace |
| `--color-accent-review-bg` | `#fef3c7` | Review accent background |
| `--color-accent-admin` | `#171717` | Admin workspace |
| `--color-accent-admin-bg` | `#f3f4f6` | Admin accent background |
| `--color-accent-delivery` | `#8b5cf6` | Delivery workspace |
| `--color-accent-delivery-bg` | `#ede9fe` | Delivery accent background |

### 2.6 Overlay & Backdrop

| Token | Value | Dùng cho |
|-------|-------|----------|
| `--color-overlay-backdrop` | `hsla(0, 0%, 0%, 0.5)` | Modal backdrop |
| `--color-overlay-surface` | `#ffffff` | Modal/dialog surface |

---

## 3. Typography Tokens

### 3.1 Font Family

| Token | Value |
|-------|-------|
| `--font-sans` | `'Geist', Arial, system-ui, sans-serif` |
| `--font-mono` | `'Geist Mono', ui-monospace, SFMono-Regular, 'Roboto Mono', Menlo, Monaco, monospace` |

### 3.2 Font Size Scale

| Token | Size | Rem | Line Height | Tracking | Dùng cho |
|-------|------|-----|-------------|----------|----------|
| `--text-display` | 48px | 3.00rem | 1.08 | -2.4px | Hero title |
| `--text-h1` | 40px | 2.50rem | 1.20 | -2.4px | Page heading |
| `--text-h2` | 32px | 2.00rem | 1.25 | -1.28px | Section heading |
| `--text-h3` | 24px | 1.50rem | 1.33 | -0.96px | Card title, sub-section |
| `--text-body-lg` | 20px | 1.25rem | 1.80 | normal | Intro paragraph |
| `--text-body` | 18px | 1.125rem | 1.56 | normal | Standard body |
| `--text-body-sm` | 16px | 1.00rem | 1.50 | normal | UI text |
| `--text-label` | 14px | 0.875rem | 1.43 | normal | Button, link, caption |
| `--text-caption` | 12px | 0.75rem | 1.33 | normal | Metadata, tag, timestamp |
| `--text-micro` | 7px | 0.4375rem | 1.00 | normal | Micro badge (uppercase) |

### 3.3 Font Weight

| Token | Value | Role |
|-------|-------|------|
| `--font-normal` | 400 | Body, reading |
| `--font-medium` | 500 | UI, interactive, nav |
| `--font-semibold` | 600 | Heading, emphasis |
| `--font-bold` | 700 | Micro badge only |

### 3.4 Monospace Typography

| Token | Size | Weight | Line Height | Dùng cho |
|-------|------|--------|-------------|----------|
| `--mono-body` | 16px | 400 | 1.50 | Code block, technical data |
| `--mono-caption` | 13px | 500 | 1.54 | Version ID, measurement label |
| `--mono-small` | 12px | 500 | 1.00 | Technical label (uppercase) |

---

## 4. Spacing Tokens

### 4.1 Base Unit

**Base: 8px** — Tất cả spacing là bội số hoặc ước số của 8.

### 4.2 Spacing Scale

| Token | Value | Dùng cho |
|-------|-------|----------|
| `--space-0` | 0px | Reset |
| `--space-px` | 1px | Hairline (shadow-border visual) |
| `--space-0.5` | 2px | Micro gap (icon-text inline) |
| `--space-1` | 4px | Tight gap (badge padding-y) |
| `--space-1.5` | 6px | Button padding compact |
| `--space-2` | 8px | Standard gap — base unit |
| `--space-2.5` | 10px | Pill padding-x |
| `--space-3` | 12px | Card inner padding compact |
| `--space-4` | 16px | Standard padding, input padding-x |
| `--space-5` | 20px | Section inner padding |
| `--space-6` | 24px | Card padding standard |
| `--space-8` | 32px | Section gap |
| `--space-10` | 40px | Large section gap |
| `--space-12` | 48px | Mobile section spacing |
| `--space-16` | 64px | Desktop section spacing |
| `--space-20` | 80px | Major section divider |
| `--space-24` | 96px | Hero top padding |
| `--space-32` | 128px | Hero section spacing |

**Lưu ý:** Scale nhảy từ 16px → 32px (bỏ 20px, 24px ở spacing) giống Vercel pattern. 24px dùng cho card padding nhưng KHÔNG phải gap giữa sections.

### 4.3 Component-specific Spacing

| Component | Padding | Gap |
|-----------|---------|-----|
| Button (primary) | 8px 16px | — |
| Button (small) | 6px 12px | — |
| Button (icon-only) | 8px | — |
| Card | 24px | 16px (internal) |
| Card compact | 16px | 12px (internal) |
| Input field | 8px 12px | — |
| Badge/Pill | 2px 10px | — |
| Nav item | 8px 12px | — |
| Sidebar item | 8px 12px | 4px between items |
| Chat message | 12px 16px | — |
| Modal | 24px | 16px (internal) |

---

## 5. Border Radius Tokens

| Token | Value | Dùng cho |
|-------|-------|----------|
| `--radius-xs` | 2px | Inline code, small span |
| `--radius-sm` | 4px | Small container, tooltip |
| `--radius-md` | 6px | Button, input, link |
| `--radius-lg` | 8px | Card, list item, dialog |
| `--radius-xl` | 12px | Featured card, image container |
| `--radius-2xl` | 16px | Modal, large panel |
| `--radius-pill-sm` | 64px | Tab navigation pill |
| `--radius-pill-lg` | 100px | Large nav link |
| `--radius-full` | 9999px | Badge, status pill, tag |
| `--radius-circle` | 50% | Avatar, icon button round |

---

## 6. Z-Index Scale

| Token | Value | Dùng cho |
|-------|-------|----------|
| `--z-base` | 0 | Default content |
| `--z-sticky` | 10 | Sticky header, floating toolbar |
| `--z-sidebar` | 20 | Project sidebar |
| `--z-dropdown` | 30 | Dropdown menu, popover |
| `--z-annotation` | 40 | Annotation pin trên floor plan |
| `--z-modal-backdrop` | 50 | Modal backdrop |
| `--z-modal` | 60 | Modal content |
| `--z-toast` | 70 | Toast notification |
| `--z-tooltip` | 80 | Tooltip |
| `--z-3d-controls` | 90 | 3D viewer controls overlay |

---

## 7. Animation Tokens

### 7.1 Duration

| Token | Value | Dùng cho |
|-------|-------|----------|
| `--duration-fast` | 100ms | Micro-interaction (opacity toggle) |
| `--duration-normal` | 150ms | Hover state, card elevation change |
| `--duration-medium` | 200ms | Tab switch, modal open, content fade |
| `--duration-slow` | 300ms | Toast slide, complex transition |

### 7.2 Easing

| Token | Value | Dùng cho |
|-------|-------|----------|
| `--ease-out` | `cubic-bezier(0, 0, 0.2, 1)` | Element appearing (modal open, toast in) |
| `--ease-in` | `cubic-bezier(0.4, 0, 1, 1)` | Element disappearing (modal close) |
| `--ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` | Content transition (tab switch, crossfade) |
| `--ease-linear` | `linear` | Progress bar, continuous animation |

---

## 8. Breakpoint Tokens

| Token | Value | Tailwind |
|-------|-------|----------|
| `--bp-sm` | 640px | `sm:` |
| `--bp-md` | 768px | `md:` |
| `--bp-lg` | 1024px | `lg:` |
| `--bp-xl` | 1280px | `xl:` |
| `--bp-2xl` | 1536px | `2xl:` |

---

## 9. Layout Tokens

| Token | Value | Dùng cho |
|-------|-------|----------|
| `--width-content-max` | 1200px | Max content width |
| `--width-chat-max` | 720px | Chat column max width |
| `--width-sidebar` | 240px | Project sidebar width |
| `--width-sidebar-collapsed` | 56px | Collapsed sidebar (icon only) |
| `--width-review-panel` | 360px | KTS review side panel |
| `--height-nav` | 56px | Top navigation height |
| `--height-input` | 40px | Standard input height |
| `--height-input-sm` | 32px | Small input height |
| `--height-button` | 40px | Standard button height |
| `--height-button-sm` | 32px | Small button height |

---

## 10. Tailwind Config Reference

```ts
// tailwind.config.ts — Mapping summary
export default {
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-sans)'],
        mono: ['var(--font-mono)'],
      },
      colors: {
        foreground: 'var(--color-foreground)',
        background: 'var(--color-background)',
        'muted-foreground': 'var(--color-muted-foreground)',
        'subtle-foreground': 'var(--color-subtle-foreground)',
        surface: 'var(--color-surface)',
        divider: 'var(--color-divider)',
        link: 'var(--color-link)',
        primary: {
          DEFAULT: 'var(--color-primary)',
          foreground: 'var(--color-primary-foreground)',
        },
        destructive: {
          DEFAULT: 'var(--color-destructive)',
          foreground: 'var(--color-destructive-foreground)',
        },
        status: {
          draft: 'var(--color-status-draft)',
          'draft-bg': 'var(--color-status-draft-bg)',
          generating: 'var(--color-status-generating)',
          'generating-bg': 'var(--color-status-generating-bg)',
          review: 'var(--color-status-review)',
          'review-bg': 'var(--color-status-review-bg)',
          approved: 'var(--color-status-approved)',
          'approved-bg': 'var(--color-status-approved-bg)',
          rejected: 'var(--color-status-rejected)',
          'rejected-bg': 'var(--color-status-rejected-bg)',
          locked: 'var(--color-status-locked)',
          'locked-bg': 'var(--color-status-locked-bg)',
          handoff: 'var(--color-status-handoff)',
          'handoff-bg': 'var(--color-status-handoff-bg)',
          superseded: 'var(--color-status-superseded)',
          'superseded-bg': 'var(--color-status-superseded-bg)',
        },
      },
      boxShadow: {
        border: 'var(--shadow-border)',
        'border-light': 'var(--shadow-border-light)',
        subtle: 'var(--shadow-subtle)',
        elevated: 'var(--shadow-elevated)',
        focus: 'var(--shadow-focus)',
      },
      borderRadius: {
        xs: 'var(--radius-xs)',
        sm: 'var(--radius-sm)',
        md: 'var(--radius-md)',
        lg: 'var(--radius-lg)',
        xl: 'var(--radius-xl)',
        '2xl': 'var(--radius-2xl)',
        'pill-sm': 'var(--radius-pill-sm)',
        'pill-lg': 'var(--radius-pill-lg)',
        full: 'var(--radius-full)',
      },
      spacing: {
        sidebar: 'var(--width-sidebar)',
        'sidebar-collapsed': 'var(--width-sidebar-collapsed)',
        'review-panel': 'var(--width-review-panel)',
        nav: 'var(--height-nav)',
      },
      maxWidth: {
        content: 'var(--width-content-max)',
        chat: 'var(--width-chat-max)',
      },
      transitionDuration: {
        fast: 'var(--duration-fast)',
        normal: 'var(--duration-normal)',
        medium: 'var(--duration-medium)',
        slow: 'var(--duration-slow)',
      },
      transitionTimingFunction: {
        'ease-out': 'var(--ease-out)',
        'ease-in': 'var(--ease-in)',
        'ease-in-out': 'var(--ease-in-out)',
      },
    },
  },
};
```

---

## 11. Token Usage Rules

### Do

- Luôn dùng token thay vì hardcode value: `text-foreground` thay vì `text-[#171717]`
- Dùng shadow token cho border: `shadow-border` thay vì `border border-gray-200`
- Dùng status token cho badge: `text-status-approved bg-status-approved-bg`
- Dùng spacing scale: `p-6` (24px), `gap-4` (16px), `gap-8` (32px)

### Don't

- Không hardcode hex color trong JSX: ~~`style={{ color: '#171717' }}`~~
- Không tạo token mới mà không thêm vào file này
- Không dùng spacing ngoài scale (vd: `p-[13px]`, `gap-[22px]`)
- Không dùng `border` CSS property cho card — luôn dùng `shadow-border`
- Không dùng weight 700 ngoại trừ `--text-micro` badge
