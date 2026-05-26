# Patterns

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/patterns/](https://wordpress.org/patterns/)

**Theme:** [wporg-pattern-directory-2024](https://github.com/WordPress/pattern-directory)

**Implementation:** FSE child theme of wporg-parent-2021.

---

## Patterns typography (YAML + prose)

[wordpress.org/patterns](https://wordpress.org/patterns/) runs on [wporg-pattern-directory-2024](https://github.com/WordPress/pattern-directory) (child of wporg-parent-2021). The directory hero matches Documentation's EB Garamond 50px treatment; grid and single-pattern UI stay Inter-first.

| Token | Font | Role |
|:------|:-----|:-----|
| `patterns-hero-title` | EB Garamond | Front-page H1 "Patterns" — 50px white on `charcoal-2`; tagline at line-height 2.3 |
| `patterns-card-title` | Inter | Linked post titles under thumbnails in the 3-column grid (`small`, 14px) |
| `patterns-single-title` | Inter | Single-pattern H1 via `core/post-title` (`heading-3`, 29px) |
| `patterns-section-heading` | Inter 600 | Related grid H2 — "More from this designer" (`large`, 20px) |
| `patterns-query-total` | Inter | Result count beside search — "2,252 patterns" in `charcoal-4` (`small`) |

Category navigation uses `is-style-button-list` at `small` size. Sticky local nav shows site title on the homepage and fades in filter/post titles on archive and single views (`wporg-local-navigation-bar__fade-in-scroll`).

## Patterns layout (prose)

Templates and patterns in [wporg-pattern-directory-2024](https://github.com/WordPress/pattern-directory):

| Template / pattern | Background | Layout |
|:-------------------|:-----------|:-------|
| `front-page-header` | `charcoal-2` | Sticky local nav + EB Garamond H1 "Patterns" + tagline; site title shows on scroll |
| `_grid.php` (`grid` pattern) | white | Category `is-style-button-list` nav → search + `wporg/query-total` + `wporg/query-filter` (curation, sort) → 3-column `post-template` grid → centered pagination |
| Grid cell | white | `wporg/pattern-thumbnail` (4:3, `light-grey-2` fill, 4px radius) + linked Inter title + `wporg/favorite-button` small variant |
| `single-pattern.php` | white | H1 + copy/favorite/author row → `wporg/pattern-view-control` iframe preview → category tags + report → related 3-up grid |
| `header.html` (inner pages) | `charcoal-2` | Local nav fades in archive H1 or single post title on scroll |
| Global footer | `charcoal-1` | Standard wporg global footer on pattern directory pages |

Archive, search, and index templates reuse the same `grid` pattern with inherited queries. Category taxonomy pages filter via the horizontal category menu (All, Featured, Posts, Text, Gallery, Call to Action, Banners, Headers, Footers, Wireframe). Pattern preview iframe uses a responsive `light-grey-2` outline frame (`patterns-preview-border`, clamp 4px–20px) with desktop/mobile viewport toggle and drag-to-resize handles.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Header CTA |
| `input-search` | Pattern search |
| `patterns-hero` | Title band + tagline |
| `patterns-pattern-preview` | Single-pattern iframe frame |
| `patterns-query-total-label` | Result count label |
| `patterns-thumbnail-card` | Grid + related pattern cells |
| `site-header / site-footer` | All sections |


### Component prose

**Patterns page components (prose):**

- **`patterns-hero`:** Charcoal-2 band below sticky local nav — EB Garamond "Patterns" at 50px; tagline "Add a beautiful, ready-to-go layout…" at line-height 2.3. Homepage hides the grid's screen-reader H1 to avoid duplicate headings.
- **`patterns-thumbnail-card`:** `wporg/pattern-thumbnail` in a 3-column grid — `light-grey-2` background, 4px radius, 4:3 aspect ratio, 40px inner padding on linked cells. Hover darkens wash to `rgba(0,0,0,0.1)`; focus uses Blueberry outline.
- **`patterns-pattern-preview`:** Single-pattern iframe inside `wporg/pattern-view-control` — responsive `patterns-preview-border` outline (clamp 4px–20px), desktop/mobile viewport toggle, drag handles on desktop. Copy button and favorite button sit above the preview frame.
- **`patterns-query-total-label`:** `wporg/query-total` beside `is-style-secondary-search-control` — result count in `charcoal-4` at 14px (e.g. "2,252 patterns"). Paired with `wporg/query-filter` dropdowns for curation and sort.

Category navigation is a horizontal `is-style-button-list` menu (All, Featured, Posts, Text, Gallery, etc.). Grid post titles link in Blueberry; favorite buttons use the small variant with optional count.


## Do's and Don'ts


- On Patterns, use EB Garamond for the directory hero only — grid titles and single-pattern H1 are Inter. Thumbnails use 4:3 aspect ratio on `light-grey-2`, not directory card borders. Pattern preview frames use `patterns-preview-border`, not the dark marketing code block.
