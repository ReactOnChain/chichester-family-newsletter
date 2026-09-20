# Chichester Family Newsletter (hosted mockup)

Hosted web mockup of the Chichester Family Newsletter (open-with-photos edition). Static HTML for Vercel.

Live: https://chichester-family-newsletter.vercel.app/

## Saturday workflow note

**Always self-host event images on this site.** Do not hotlink organiser domains (e.g. Conservancy, Weald & Downland, CFT CDN, Cathedral, press sites) — many return a “Stop! This image was hotlinked” graphic when loaded from vercel.app.

1. Download images with a normal browser User-Agent (or reuse local copies).
2. Save under `images/YYYY-MM-DD/` with stable filenames.
3. Reference them with relative paths like `/images/2026-09-20/harbour-tots.jpg`.
4. Keep attribution via the organiser booking links in the HTML.

Fair use for a local newsletter mockup linking to the organiser.

## Self-hosted images

Event photos live as base64 text under `image-sources/YYYY-MM-DD/*.jpg.b64` (git-friendly).
`python3 scripts/decode-images.py` writes the real JPEGs to `images/YYYY-MM-DD/` (run automatically on Vercel build).
HTML must reference `/images/YYYY-MM-DD/name.jpg` only — never organiser domains.
