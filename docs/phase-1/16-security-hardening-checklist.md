# Security Hardening Checklist

*Date: Apr 12, 2026*
*Target: `kts.blackbirdzzzz.art`*

## Runtime

- [x] Public exposure di qua Cloudflare Tunnel thay vi mo port API truc tiep
- [x] Public app route dung `Caddy -> web/api` sau edge
- [x] JWT secret da dua ra runtime file ngoai repo
- [x] LLM key da dua ra runtime file ngoai repo
- [x] Tunnel token da dua ra runtime file ngoai repo
- [x] CORS gioi han theo `https://kts.blackbirdzzzz.art,http://localhost`

## Application Controls

- [x] Auth register/login/refresh hoat dong voi access token + refresh token
- [x] RBAC gate cho route write va admin route co test
- [x] Public share lane dung token ngau nhien thay vi expose project public toan cuc
- [x] Review/export/handoff flow yeu cau role `architect|admin`
- [x] Media assets duoc phuc vu qua app gateway thay vi folder host mo truc tiep

## Operational Baseline

- [x] Backup baseline da chay va tao artifact local
- [x] Public load baseline da co artifact
- [x] Public loop verification da co artifact 5/5 pass
- [ ] Sentry event delivery confirmation
- [ ] Off-host backup destination
- [ ] Secret rotation cadence doc

## Open Actions

1. Bo sung `SENTRY_DSN` that va verify event den dashboard.
2. Chot dich backup off-host nhu `R2` hoac `S3-compatible bucket`.
3. Neu can muc production cao hon nua, them WAF rules / rate limiting cho auth va share endpoints.
