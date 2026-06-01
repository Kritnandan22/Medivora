# CLAUDE.md — Rx Automata

This file is the single source of context for every Claude Code session in this
repository. Read it before making changes.

## What this is

**Rx Automata** is a public, vendor-neutral, educational website that explains
how workflow automation and agentic (AI agent) automation are reshaping
pharmaceuticals and medicine management. The build is governed by
[`docs/SPEC.md`](docs/SPEC.md) — when this file and the spec disagree, the
spec wins. Update both if you change the plan.

## Tech stack

- **Framework**: Astro 5 (static site generator, content collections, "islands"
  for interactive parts).
- **Styling**: Tailwind CSS v4 via `@tailwindcss/vite`, with brand design
  tokens declared in `src/styles/global.css` under `@theme`.
- **Content**: Markdown / MDX content collections under `src/content/`
  (added in Phase 2).
- **Hosting**: Render Static Site (free tier, global CDN, automatic TLS),
  defined in `render.yaml`.
- **Type system**: TypeScript strict (`astro/tsconfigs/strict`).
- **Tooling**: Prettier with `prettier-plugin-astro` +
  `prettier-plugin-tailwindcss`, ESLint with `eslint-plugin-astro`.

## File structure

```
/
├── CLAUDE.md                     ← this file
├── docs/
│   ├── SPEC.md                   ← the build specification (source of truth)
│   └── reference/                ← original handoff materials (HTML prototype, docx)
├── render.yaml                   ← Render Blueprint
├── astro.config.mjs              ← Astro + Tailwind + Sitemap config
├── tsconfig.json
├── package.json
├── eslint.config.js
├── .prettierrc.json
├── public/                       ← static assets (favicon, robots.txt, OG images)
└── src/
    ├── pages/                    ← route pages (.astro / .md)
    ├── layouts/                  ← page shells (BaseLayout.astro etc.)
    ├── components/               ← reusable UI (added in Phase 1)
    ├── content/                  ← markdown content collections (added in Phase 2)
    └── styles/
        └── global.css            ← Tailwind import + @theme tokens + base layer
```

## Design tokens (brand)

Declared in `src/styles/global.css`. Use the CSS variable form
(`var(--color-green)`) when applying in arbitrary Tailwind values
(`bg-[color:var(--color-green)]`). The palette:

| Token | Hex | Role |
| --- | --- | --- |
| `--color-paper` | `#F1ECE0` | Page background — warm paper |
| `--color-paper-2` | `#E8E1D1` | Card / panel surfaces |
| `--color-paper-3` | `#DED5C2` | Recessed surfaces |
| `--color-ink` | `#13201B` | Primary text / dark surfaces |
| `--color-ink-2` | `#2C3A34` | Body text |
| `--color-ink-soft` | `#54625B` | Secondary text |
| `--color-green` | `#0E6B54` | Apothecary green — primary accent |
| `--color-green-bright` | `#16A684` | Active / interactive green |
| `--color-green-deep` | `#0A4F3F` | Hover / depth |
| `--color-amber` | `#C06A24` | Signal amber — secondary accent |
| `--color-amber-bright` | `#E08A2B` | Highlights, indicators |

Typography:

- Headings: `Fraunces` (editorial serif), `font-weight: 600`, tight tracking.
- Body: `Hanken Grotesk` (clean sans).
- Mono / eyebrow labels: `JetBrains Mono`, uppercase, wide letter-spacing — use
  the `.mono` utility from `global.css`.

## Conventions

### Do

- Ship **as little JavaScript as possible**. Static-by-default; reach for
  Astro "islands" (`client:visible`, `client:idle`) only when interactivity
  truly needs them.
- Author content as **Markdown content collections** wherever possible, not
  hard-coded JSX/HTML. The seven value-chain stages, case studies, and blog
  posts are all collections (Phase 2).
- Use **semantic HTML landmarks** (`<header>`, `<nav>`, `<main>`, `<footer>`,
  `<article>`) and a logical heading order. Always include a
  "Skip to content" link in the layout.
- Keep colour contrast **≥ 4.5:1** for body text; never rely on colour alone.
- Respect `prefers-reduced-motion` — already wired in `global.css` base layer.
- Set explicit dimensions on images / embeds to prevent layout shift.
- Use the `~/` import alias (`~/components/Foo.astro`) — configured in
  `tsconfig.json`.

### Don't

- Don't add a runtime backend until Phase 4 actually requires one. The spec
  starts on Render Static Site (Option A); Option B (Web Service + Postgres)
  is only for stored data.
- Don't pull in heavy client-side frameworks for things Astro can do at build
  time.
- Don't bake content into `.astro` files when it belongs in a content
  collection — it makes it hard to edit and to query across pages.
- Don't commit secrets. Use environment variables in Render's dashboard.
- Don't claim a feature is "done" without verifying it builds (`npm run build`)
  and looks right in `npm run dev`.

## Build phases (see SPEC §11)

| Phase | Focus | Status |
| --- | --- | --- |
| 0 | Setup & deployable skeleton | ✅ scaffold complete |
| 1 | Design system & layout shell | next |
| 2 | Core content pages (Markdown collections) | |
| 3 | Interactive features (value-chain explorer, agent diagram, decision tool) | |
| 4 | Engagement & data (optional backend) | |
| 5 | SEO, accessibility, performance | |
| 6 | Analytics, security headers, monitoring | |
| 7 | Launch & iterate | |

Work one phase at a time. Deploy to Render at the end of each phase to surface
issues early.

## Common commands

```bash
npm run dev          # local dev server at http://localhost:4321
npm run build        # production build → dist/
npm run preview      # preview the production build
npm run format       # prettier --write everything
npm run lint         # eslint
```

## Reference materials

- `docs/SPEC.md` — full build specification.
- `docs/reference/pharma-automation-field-guide.html` — the original
  single-page HTML prototype. **The visual language is canonical**; future
  Phase 1 / Phase 2 work should port it into the Astro component model
  rather than rewriting the design from scratch.
- `docs/reference/Rx-Automata-Website-Build-Spec.docx` — original handoff doc
  (`SPEC.md` is the working copy).
