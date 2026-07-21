# 📱 JobHub → Google Play — Launch Track

**Strategy:** PWA-first → TWA (Trusted Web Activity) → Play Store.
Zero-budget, no native rewrite, one codebase. The React PWA in `/frontend` IS the app.

---

## Phase A — PWA Readiness (before anything else)
- [ ] `manifest.json` complete: name, short_name, icons 192/512 (maskable), theme_color, display: standalone
- [ ] Service worker via Workbox: offline shell + cached job lists (2G doctrine)
- [ ] Lighthouse PWA audit: installable, offline-capable, fast on Moto G-class device
- [ ] HTTPS everywhere (Vercel/host provides)

## Phase B — TWA Packaging (Bubblewrap)
```bash
npm install -g @bubblewrap/cli
bubblewrap init --manifest https://<jobhub-domain>/manifest.json
bubblewrap build
```
- Package name: `za.co.jobhub.app` (reserve via the domain you control — a jobhub domain)
- Signing key: generate ONCE, back up offline (losing it = losing the app listing forever)
- `assetlinks.json` hosted at `https://<jobhub-domain>/.well-known/assetlinks.json`
  (proves app↔domain link; without it the TWA shows a URL bar)

## Phase C — Play Console ($25 one-time fee — the ONLY cost)
- [ ] Google Play Developer account (pay once, lifetime)
- [ ] Store listing: title **JobHub — SA's Employment Platform**, short desc, full desc (constitution tone),
  screenshots (phone + 7" tablet), feature graphic 1024×500, app icon 512×512
- [ ] Content rating questionnaire (IARC)
- [ ] Data safety form: declare PII collection per POPIA (matches CONSTITUTION.md — keep answers honest)
- [ ] Target audience: 18+ (employment platform)
- [ ] Privacy policy URL (host a `/privacy` page — POPIA-compliant)

## Phase D — Release
1. Internal testing track (you + Neo + 10 testers)
2. Closed beta (Johannesburg CBD + Soweto cohort per Phase 0)
3. Production rollout: 10% → 50% → 100% staged

## Notes
- Android 16 focus is fine — but set `minSdk` to Android 8 (R1,500-phone doctrine from the constitution)
- Keep app size < 15MB download — 2G users abandon heavy apps
- Every Play update = just redeploy the PWA (TWA serves live content); only rebuild the APK for manifest changes

---
*The PWA is the app. The Play Store is just the doorway.* 🚪🐘
