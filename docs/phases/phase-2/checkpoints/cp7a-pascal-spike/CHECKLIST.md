# CP7.A — Validation Checklist

## CHECK-01: Build PASS

```bash
cd ../ai-architect-web
pnpm install
pnpm build
```

**Expected:** Build success, 0 type error.
**Fail if:** Type/module resolution error tu Pascal package.

## CHECK-02: Lab route mount

```bash
cd ../ai-architect-web
pnpm dev &
# Mo http://localhost:3000/lab/pascal tren Chrome stable
# Xac nhan canvas xuat hien, khong crash console
```

**Expected:** Pascal editor scene render, khong runtime error.
**Fail if:** Page trang, console co fatal error.

## CHECK-03: Browser matrix

Kiem spike report co bang matrix 4 browser voi ket luan rõ Chrome/Edge PASS, Safari/Firefox ket qua cu the.
**Expected:** Bang day du + recommendation fallback.
**Fail if:** Thieu browser hoac khong co recommendation.

## CHECK-04 (warning): Bundle size

Spike report co con so cu the bundle size route `/lab/pascal`.
**Expected:** Documented, du co vuot dieu kien so bo.
**Warning if:** Thieu (khong block, nhung CP7.C phai set budget).

## CHECK-05 (warning): License compliance

```bash
test -f ../ai-architect-web/packages/pascal-editor/LICENSE && echo OK
grep -qi pascal ../ai-architect-web/NOTICE && echo OK
```

**Expected:** LICENSE ton tai, NOTICE chua ten.
**Warning if:** Thieu.

## Blocker checks

CHECK-01, CHECK-02, CHECK-03 → all PASS moi duoc trigger CP7.B.

## Notify

```bash
uv run python docs/phases/phase-2/checkpoints/notify.py \
  --cp cp7a-pascal-spike --role validator --status PASS \
  --summary "Spike PASS, san sang CP7.B" \
  --result-file docs/phases/phase-2/checkpoints/cp7a-pascal-spike/validation.json
```
