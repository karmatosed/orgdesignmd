# Photos

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/photos/](https://wordpress.org/photos/)

**Theme:** [wporg-photos-2024](https://github.com/WordPress/wporg-photo-directory)

**Implementation:** FSE child theme of wporg-parent-2021.

---

## Photos typography (YAML + prose)

[wordpress.org/photos](https://wordpress.org/photos/) runs on [wporg-photos-2024](https://github.com/WordPress/wporg-photo-directory) (child of wporg-parent-2021). The directory shares Patterns' EB Garamond 50px hero treatment; grid cells show images only — no linked titles under thumbnails. Single-photo titles and post titles use EB Garamond via `core/post-title`; section labels stay Inter 600.

| Token | Font | Role |
|:------|:-----|:-----|
| `photos-hero-title` | EB Garamond | Front-page site title — 50px white on `charcoal-2`; dynamic tagline "Browse over X free photos" at line-height 2.3 |
| `photos-query-total` | Inter | Result count beside search — "38,069 photos" in `charcoal-4` (`small`) |
| `photos-single-title` | EB Garamond | Single-photo H1 via `core/post-title` (`heading-3`, 29px); screen-reader duplicate on detail pages |
| `photos-section-heading` | Inter 600 | Detail-page H2s — "Image info", "EXIF data", "Attribution", "License/usage" (`heading-6`, 18px) |
| `photos-discover-heading` | EB Garamond | Footer CTA — *Discover more content submitted by the WordPress community* (`heading-3`, line-height 1.28) |

Author name links in the single-photo header use Inter `small` in `charcoal-1`. Alt-text labels in post content use Inter 600 via `.wporg-alt-text-label`. EXIF meta list variant (`is-style-has-border`) adds bordered rows on the detail page.

## Photos layout (prose)

Templates and patterns in [wporg-photos-2024](https://github.com/WordPress/wporg-photo-directory):

| Template / pattern | Background | Layout |
|:-------------------|:-----------|:-------|
| `header-front-page` | `charcoal-2` | Sticky local nav + site-title H1 at 50px + dynamic "Browse over X free photos" tagline; scroll variant shows site title in nav bar |
| `grid.php` (`grid` pattern) | white | Search + `wporg/query-total` row → four `wporg/query-filter` dropdowns (category, color, orientation, sort) → 4-column `post-template` grid at 20px gap → centered pagination |
| Grid cell | white | `wporg/link-wrapper` `is-style-no-underline` → 1px `black-opacity-15` border, 2px radius → `post-featured-image` 16:9 — image only, no title row |
| `single.php` | white | Author row (40px avatar + linked name) + favorite + Blueberry download nav → 16:9 featured image (`contain`) → post content (alt text) → Image info / EXIF two-column meta → attribution tabs → license prose → "Discover more" EB Garamond CTA + primary/outline buttons |
| `page-filters.php` | white | H1 `heading-3` + three columns listing `photo_category`, `photo_color`, and `photo_orientation` taxonomies with post counts |
| Global footer | `charcoal-1` | Standard wporg global footer |

Grid responsive breakpoints in `_grid.scss`: 4 columns default → 3 columns at ≤1280px → 2 columns at ≤782px. Filter row scrolls horizontally at ≤889px. Single-photo featured image drops fixed 16:9 aspect ratio below 599px (max-height 700px). Child `theme.json` sets `wideSize` to **1760px** — wider than the parent 1160px default.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Header CTA |
| `input-search` | Photo search |
| `patterns-query-total-label` | Result count label |
| `photos-attribution` | RTF/HTML tab panel |
| `photos-download-menu` | Size dropdown nav |
| `photos-grid-cell` | Bordered 16:9 thumbnail |
| `photos-hero` | Title band + tagline |
| `photos-meta-list` | Image info + EXIF rows |
| `photos-query-total-label` | Result count label |
| `photos-single-header` | Author + favorite + download |
| `site-header / site-footer` | All sections |


### Component prose

**Photos page components (prose):**

- **`photos-hero`:** Charcoal-2 band below sticky local nav — site-title H1 at 50px (EB Garamond via theme) + dynamic tagline "Browse over X free photos" at line-height 2.3. Tagline count rounds down to nearest thousand above 1,000 published photos.
- **`photos-grid-cell`:** 4-column grid of image-only cells — `wporg/link-wrapper` `is-style-no-underline` wrapping a 1px `black-opacity-15` border group (2px radius) with 16:9 `post-featured-image`. No title or favorite row under thumbnails (unlike Patterns). Grid gap is 20px; columns drop to 3 at ≤1280px and 2 at ≤782px.
- **`photos-query-total-label`:** `wporg/query-total` beside `is-style-secondary-search-control` — result count in `charcoal-4` at 14px (e.g. "38,069 photos"). Paired with four `wporg/query-filter` dropdowns: category, color, orientation, sort. Filter row scrolls horizontally below 889px.
- **`photos-single-header`:** `is-entry-header` flex row — 40px circular avatar + linked author name left; `wporg/favorite-button` + download navigation right. Visible H1 is screen-reader-only; page title comes from post title styling elsewhere.
- **`photos-download-menu`:** `core/navigation` with `menuSlug: download`, class `is-download-menu` — Blueberry fill, 2px radius, small button sizing aligned with favorite button. Submenu lists file sizes with `charcoal-4` filesize labels; focus ring uses Blueberry outline + white inset shadow.
- **`photos-meta-list`:** Custom `wporg/meta-list` block — Image info column (date, dimensions, color/category/orientation/tag taxonomies); EXIF column uses `is-style-has-border` variant for aperture, focal length, ISO, shutter speed.
- **`photos-attribution`:** Custom `wporg/photo-attribution` block with Interactivity API tabs (RTF/HTML) — tab buttons on `light-grey-2` hover, selected tab on white with 1px `light-grey-1` border; HTML tab uses IBM Plex Mono; copy button below panel.


## Do's and Don'ts


- On Photos, use EB Garamond for the hero site title and single-photo post titles — grid cells are image-only with 16:9 aspect ratio and 1px `black-opacity-15` borders, not Patterns' 4:3 `light-grey-2` thumbnails. Use four filter dropdowns (category, color, orientation, sort), not Patterns' category button-list. Wide layout is 1760px, not 1160px. Download actions use a Blueberry navigation submenu, not inline links.
