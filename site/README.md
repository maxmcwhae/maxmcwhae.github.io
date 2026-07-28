# maxmcwhae.com

Personal academic homepage. Astro, static, zero client-side JavaScript,
deployed to GitHub Pages with a custom domain.

## Local development

```bash
npm install
npm run dev        # http://localhost:4321
npm run build      # outputs to dist/
```

## Writing a post

Add a markdown file to `src/content/writing/`:

```markdown
---
title: "Post title"
date: 2026-08-15
description: "One-line summary (used in RSS and meta tags)."
---

Body in markdown.
```

The home page, `/writing/`, and the RSS feed pick it up automatically at
`/writing/<filename-without-extension>/`.

## Deploying (one-time setup)

1. **Create the GitHub repo.** Any name works (e.g. `maxmcwhae.com`). Note
   which account you use — the DNS step needs it. (Your existing account is
   `mcawezome`; if you're creating a fresh `maxmcwhae` account instead,
   substitute accordingly below.)
2. **Push this project** to the repo's `main` branch.
3. **Enable Pages:** repo → Settings → Pages → Source: **GitHub Actions**.
   The included workflow (`.github/workflows/deploy.yml`) builds and deploys
   on every push to `main`.
4. **Porkbun DNS** (maxmcwhae.com → DNS records):

   | Type  | Host | Answer                  |
   |-------|------|-------------------------|
   | A     | (blank / apex) | 185.199.108.153 |
   | A     | (blank / apex) | 185.199.109.153 |
   | A     | (blank / apex) | 185.199.110.153 |
   | A     | (blank / apex) | 185.199.111.153 |
   | CNAME | www  | `<ACCOUNT>.github.io`   |

   Delete any parked-domain records Porkbun added by default.
5. **Custom domain:** repo → Settings → Pages → Custom domain →
   `maxmcwhae.com` → Save. Wait for the DNS check, then tick
   **Enforce HTTPS**. (The `public/CNAME` file keeps this setting across
   deploys.)

DNS can take up to an hour to propagate; the certificate usually follows
within another hour.

## Remaining TODOs

- [ ] **Headshot** — add your photo as `public/headshot.jpg`, then uncomment
      the `<img>` block at the top of `src/pages/index.astro`.
- [ ] **Meetup link** — replace the "Group page link coming soon" line in
      `src/pages/index.astro` with a link to the Meetup **group** page (not
      your member profile — that URL hits a login wall for visitors).
- [ ] **SANDGLASS repo** — once `github.com/mcawezome/sandglass` (or
      similar) exists, point the Code link in `src/pages/research.astro` at
      it directly.
- [ ] **Proposal PDF** — export the final grant application to PDF, save it
      as `public/sandglass-proposal.pdf`, and uncomment the link in
      `src/pages/research.astro`.
- [ ] **Email** — currently the site shows no email address. Add it to the
      Elsewhere section of `src/pages/index.astro` (plain text or
      `mailto:`) when you've decided which address to publish.
- [ ] **CV** — `public/cv.pdf` was generated from `scripts/generate_cv.py`
      (requires `pip install reportlab`). It has no email on it either;
      edit the script and re-run to regenerate, then copy the output over
      `public/cv.pdf`.

## Structure

```
public/            static files served as-is (CNAME, cv.pdf, favicon, robots)
src/content/       markdown content (writing/)
src/layouts/       Base.astro — head, header, footer
src/pages/         index, research, writing/, now, 404, rss.xml
src/styles/        global.css — the entire design
scripts/           generate_cv.py — regenerates public/cv.pdf
```
