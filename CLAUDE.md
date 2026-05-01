# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repo overview

NeuroBite is a Jekyll static blog deployed to GitHub Pages. Content is Chinese-language rapid-review notes on neuroscience/AI papers (and occasionally interviews). Each paper note follows a structured 11-section analysis template (sections 0–10).

## Commands

```bash
# Dev server with live reload
bundle exec jekyll serve --livereload

# Build for production
bundle exec jekyll build
```

## Content authoring

### Paper reviews

Create a new `.md` file in `_posts/` named `YYYY-MM-DD-slug.md`. Use the prompt template in `_posts/_PROMPT.md` — paste the paper text and have Claude generate the structured Markdown output directly into the post file.

### Interviews

Same naming convention. Use `_posts/_INTERVIEW_PROMPT.md` as the prompt template. Interviews require `content_type: interview` in front matter.

### Front matter rules

All posts use `layout: post`. Required fields differ by type:

| Field | Paper | Interview |
|-------|-------|-----------|
| `layout` | `post` | `post` |
| `title` | Chinese title | Format: `受访者 × 议题` |
| `date` | `YYYY-MM-DD` | `YYYY-MM-DD` |
| `venue` | Single source name (journal/conference/arXiv) | Podcast/media name |
| `content_type` | — (omit) | `interview` |
| `description` | One-sentence takeaway ≤50 chars | Same |

**Never** add `parent`, `nav_order`, or `layout: default` to post front matter — they break rendering.

## Architecture

### Site pages

- **Home** (`index.md`): hero section + latest 9 paper cards (sorted by date descending via Liquid `{% assign papers = site.posts | sort: "date" | reverse %}`) + about section
- **All papers** (`论文速读.md`, permalink `/papers/`): full archive listing, same card format but unlimited
- **Individual posts**: rendered by `_layouts/post.html`, which wraps content in `.post-container` with share bar

### Templates

- `_layouts/default.html` — site chrome (sticky header with nav, footer with Bilibili link). All pages extend this.
- `_layouts/post.html` — post wrapper; reads `page.content_type` to conditionally show "Interview" badge vs. venue badge in the meta line.

### Styling

`assets/css/neurobite.css` — hand-written, no framework. Key design tokens:
- Primary: `--nature-red: #b31b1b`, `--bili: #FB7299`
- Serif body (`Noto Serif SC`), sans-serif labels (`Noto Sans SC`)
- Post content targets `.post-content` (h2/h3, tables, blockquotes, code all styled there)

### Config

`_config.yml` key settings:
- `permalink: /papers/:title` — individual post URLs live under `/papers/`
- `plugins: [jekyll-feed]` — auto-generates RSS feed at `/feed.xml` linked in site nav
- `future: true` — future-dated posts are published immediately (no scheduling)

### CI/CD

Pushing to `main` triggers `.github/workflows/jekyll-gh-pages.yml` → builds with `actions/jekyll-build-pages@v1` → deploys to GitHub Pages.
