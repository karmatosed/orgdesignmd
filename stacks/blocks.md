# Blocks

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/blocks/](https://wordpress.org/blocks/)

**Theme:** wporg-main-2022 [`blocks.php` pattern](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/blocks.php)

**Implementation:** Block pattern in wporg-main-2022.

---

## Blocks typography (YAML + prose)

[wordpress.org/blocks](https://wordpress.org/blocks/) uses the [`blocks.php`](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/blocks.php) pattern in wporg-main-2022 (`page-blocks.html`). Unlike Documentation or Developer heroes, Blocks uses **Inter for the page title** — not EB Garamond.

| Token | Font | Role |
|:------|:-----|:-----|
| `blocks-hero-title` | Inter | H1 "Blocks" — 70px white on `charcoal-2`; tagline uses `is-style-short-text` |
| `blocks-section-heading` | Inter | Split-layout H2s — "Complete creative control", "Create your own", "See what's new", "Only the beginning" (`heading-3`, 29px) |
| `blocks-grid-label` | Inter | Block type names in the 4×2 icon grid — Paragraph, Heading, Media, etc. (`extra-small`, 12px, `light-grey-1`) |

Prose H2s in dark bands ("Build without limits", "WordPress's secret power") inherit default Inter h2 scale without the `heading-3` preset. Editor mockup preview text uses Blueberry at `extra-large` (24px).

## Blocks layout (prose)

Pattern [`wporg-main-2022/blocks`](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/blocks.php) in template `page-blocks.html`:

| Section metadata name | Background | Layout |
|:----------------------|:-----------|:-------|
| Hero | `charcoal-2` | 40/60 columns — Inter 70px H1 + `is-style-short-text` tagline left; `blocks-feature-1.png` right |
| Without limits | `charcoal-1` | `alignwide` prose + paired `is-style-outline-on-dark` buttons |
| Block grid | `charcoal-1` | Flex-wrap 4×2 grid — 25% cells with `blocks-grid-border-*` dividers; 24×24px block icons + `extra-small` labels |
| Secret power | `charcoal-1` | Prose + single `is-style-fill` primary button to Showcase |
| (collage) | — | Full-bleed `patterns-collage.jpg` between dark bands |
| Creative control | `charcoal-2` | 50/50 columns — `heading-3` H2 + outline CTA to `/gutenberg` |
| Create your own | `charcoal-2` | 50/50 — stacked editor mockup (code + preview) left; H2 + outline CTA right |
| Core & Features | `light-grey-2` | 50/50 — release copy + primary button left; bordered screenshot (4px radius, 1px `light-grey-1`) right |
| Only The Beginning | white | Dot separator (`is-style-dots-background`) + 66% column H2 + Blueberry link list |

Dark sections use white link color via block `elements.link` overrides. The block icon grid is unique to this page — not the parent `is-style-cards-grid` pattern used on Documentation or Developer.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `blocks-editor-mockup` | Code + preview stack |
| `blocks-grid-cell` | Block type icon grid |
| `blocks-hero` | Title band + feature image |
| `blocks-release-promo` | Release screenshot band |
| `blocks-section-dark` | Dark prose bands |
| `button-primary` | Outline-on-dark CTAs |
| `input-search` | Global header |
| `site-header / site-footer` | All sections |


### Component prose

**Blocks page components (prose):**

- **`blocks-hero`:** Charcoal-2 band with 40/60 columns — Inter 70px H1 "Blocks", `is-style-short-text` tagline, and `blocks-feature-1.png` hero illustration on the right.
- **`blocks-section-dark`:** Charcoal-1 prose bands with white text and white link overrides — "Build without limits", "WordPress's secret power". CTAs use `is-style-outline-on-dark` (outline white) or `is-style-fill` (Blueberry fill for primary actions like "Explore the Showcase").
- **`blocks-grid-cell`:** 4×2 flex grid on `charcoal-1` — 25% cells separated by `blocks-grid-border-top` / `-bottom` / `-right` lines; centered 24px block icon + `extra-small` label in `light-grey-1`.
- **`blocks-editor-mockup`:** Stacked editor preview — `charcoal-3` code block (5px top radius, IBM Plex Mono small) over `light-grey-2` preview pane (5px bottom radius) showing Blueberry `extra-large` sample output.
- **`blocks-release-promo`:** `light-grey-2` band with 50/50 columns — `heading-3` copy + primary button left; release screenshot with 1px `light-grey-1` border and 4px radius right.


## Do's and Don'ts


- On Blocks, use Inter for the hero title (70px) — not EB Garamond. Dark sections stack `charcoal-2` and `charcoal-1`; use `is-style-outline-on-dark` for secondary CTAs on dark backgrounds. The block type grid uses custom dark border tokens, not card-grid patterns.
