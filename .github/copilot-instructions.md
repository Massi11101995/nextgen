## Purpose
This repo is a minimal static single-page site. These instructions help an AI coding agent make safe, focused edits that match project structure and conventions.

## Big picture
- Single entry: `index.html` is the whole application (UI + small client JS).
- Assets live in the `images/` folder (e.g., `images/header2.jpg`).
- No backend: reservations are simulated client-side via `confirmReservation()` which generates a local code and a QR image using https://api.qrserver.com.

## What to edit and why
- UI and layout: update `index.html` (inline `<style>`). Keep CSS changes in the head or move to a new `styles.css` only if you update links accordingly.
- Client logic: modify the inline `<script>` near the bottom. Key functions: `openReservation()`, `closeReservation()`, `generateRandomCode()`, `confirmReservation()`.
- Static assets: add new images to `images/` and reference them with relative paths (case-sensitive on many hosts—avoid renaming case only on Windows).

## Developer workflows (quick commands)
- Preview locally: open `index.html` in a browser (no build step).
- Linting/tests: none present. If you add JS tooling, include `package.json` and document `npm run lint` or `npm test` in README.

## Patterns & conventions
- Keep markup and small JS in the single page unless adding multi-page navigation.
- When adding JavaScript files, place `<script src="..."></script>` before `</body>` to preserve current behavior.
- Image references use relative paths (e.g., `<img src="images/header2.jpg">`).
- Do not embed secrets or API keys—QR generation currently calls a public service from the client.

## Integration points
- External QR API: `https://api.qrserver.com/v1/create-qr-code/` (client-side).
- `tel:` link exists for a contact phone number—phone handling is client/browser responsibility.

## Safe edits checklist for PRs
- Preserve: do not remove the reservation modal markup or its IDs (`reservationModal`, `resultatReservation`, `basket`, `campus`).
- Verify: open the page and click "Réserver un panier" to exercise `confirmReservation()` and check console for errors.
- Assets: ensure any added images are placed in `images/` and referenced with correct relative paths.

## If you find or add infra
- If you introduce a build step or package manager, add clear commands to `README.md` and update this file with the new workflow.

---
If any part of the codebase is missing from this workspace or you want a stricter agent policy (tests, CI, build), tell me which areas to expand and I will update this file.
