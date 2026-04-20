# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal resume and portfolio website for Noah Stephenson — Systems Engineering Cadet at West Point (USMA). Built as a Pelican static site, deployed on Render via GitHub.

**Audience**: Army leadership, defense tech recruiters, MBA programs, consulting firms.
**Aesthetic goal**: Professional engineering/consulting — signal clarity, discipline, and technical competence.

This site is the front door to a broader ecosystem that will eventually include Django web apps showcasing engineering and full-stack projects.

## Tech Stack

- **Pelican** — Python static site generator
- **Custom HTML/CSS theme** — built from scratch (no Bootstrap or frameworks)
- **Vanilla JavaScript** — dark mode toggle only
- **Deployment** — Render (build command: `pelican content`, publish directory: `output`)
- **Version control** — GitHub

## Commands

```bash
# Install dependencies
pip install pelican markdown

# Run local dev server (auto-rebuilds on change)
pelican --autoreload --listen

# Build for production
pelican content

# Build with explicit settings file
pelican content -s publishconf.py
```

## Architecture

Standard Pelican layout:

- `content/` — Markdown source files (pages and articles)
- `themes/` — Custom theme directory (templates + static assets)
  - `themes/<theme-name>/templates/` — Jinja2 HTML templates
  - `themes/<theme-name>/static/` — CSS, JS, images
- `output/` — Generated site (not committed to git; this is the publish directory on Render)
- `pelicanconf.py` — Main Pelican configuration
- `publishconf.py` — Production overrides (absolute URLs, etc.)

## Key Conventions

- All styling is custom CSS — no utility frameworks. Keep it clean and purposeful.
- JavaScript is intentionally minimal (dark mode toggle only). Do not add JS complexity.
- Content is authored in Markdown inside `content/`. Pages (resume, about, projects) use `content/pages/`.
- The theme is the main creative asset — treat it with care.
- `output/` is gitignored; Render builds it from source on deploy.
