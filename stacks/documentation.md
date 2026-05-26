# Documentation

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/documentation/](https://wordpress.org/documentation/)

**Theme:** [wporg-documentation-2022](https://github.com/WordPress/wporg-documentation-2022)

**Implementation:** FSE child theme of wporg-parent-2021 (formerly HelpHub).

---

## Documentation typography (YAML + prose)

[wordpress.org/documentation](https://wordpress.org/documentation/) runs on [wporg-documentation-2022](https://github.com/WordPress/wporg-documentation-2022) (child of wporg-parent-2021; formerly HelpHub / wordpress.org/support). The child `theme.json` narrows the heading scale and switches **in-article headings to Inter 600** — EB Garamond is reserved for page titles, archive titles, and the front-page hero.

| Token | Font | Role |
|:------|:-----|:-----|
| `docs-hero-title` | EB Garamond | Front-page H1 "Documentation" — 50px white on `charcoal-2` |
| `docs-section-heading` | Inter 600 | Front-page section H2s — "WordPress overview", "Technical guides" (20px `heading-5`) |
| `docs-topic-card-title` | Inter 600 | Card titles inside `is-style-cards-grid` link wrappers (16px) |
| `docs-article-title` | EB Garamond | Single-article and query titles via `core/post-title` / `core/query-title` (36px) |
| `docs-body-heading` | Inter 600 | Article H2–H4 — 24px / 20px / 18px per child `theme.json` element overrides |

Child heading presets: `heading-1` 38px → `heading-6` 18px (smaller than parent marketing scale). Code blocks (`core/code`, `core/preformatted`) use `light-grey-2` background with 1px `light-grey-1` border at 2px radius — not the dark `code-block` component used elsewhere.

## Documentation layout (prose)

Templates and patterns in [wporg-documentation-2022](https://github.com/WordPress/wporg-documentation-2022):

| Template / class | Background | Layout |
|:-----------------|:-----------|:-------|
| `header-home` | `charcoal-2` hero + white search row | Sticky local nav (`menuSlug: documentation`); EB Garamond H1; `wporg/language-suggest` band |
| `front-page-content` pattern | white | Four `alignwide` sections; each: Inter H2 link + `charcoal-4` blurb + 3-up `is-style-cards-grid` (`minimumColumnWidth: 32.3%`) |
| `page-overview`, `page-technical-guides`, etc. | white | Breadcrumbs (`wporg/site-breadcrumbs`); H1 + term description; `wporg/article-list` grouped by subcategory |
| `single.html` | white | `.has-three-columns.has-no-left-sidebar`: 248px floating TOC (`wporg/sidebar-container` + `wporg/table-of-contents`) + 680px article; metadata row (first published / last updated) |
| `footer-content` pattern | `charcoal-2` | "Get more help" — 4×25% columns with `blueberry-2` link labels (forums, developer docs, issue tracker, Learn) |

Front-page section H2 links suppress underline by default (underline on hover only). Card grid cells: 1px `light-grey-1` border, 2px radius, 20px padding; hover shifts to `light-grey-2` background.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Header CTA |
| `docs-code-block` | Inline article code/pre |
| `docs-help-footer` | "Get more help" band |
| `docs-hero` | Front-page title band |
| `docs-toc-sidebar` | Article table of contents |
| `docs-topic-card` | Front-page topic cards |
| `input-search` | Docs hero + inner pages |
| `site-header / site-footer` | All sections |


### Component prose

**Documentation page components (prose):**

- **`docs-hero`:** Charcoal-2 band below sticky local nav. EB Garamond "Documentation" at 50px; white text. Followed by `wporg/language-suggest` (default `blueberry-4` wash) and a full-width search row (`is-style-default` on home, `is-style-secondary-search-control` on inner pages).
- **`docs-topic-card`:** Cells in parent-theme `is-style-cards-grid` — white background, 1px `light-grey-1` border, 2px radius, 20px padding. Wrapped in `wp-block-wporg-link-wrapper`; Inter 600 title + 14px description. Hover: `light-grey-2` fill, no underline on wrapper (title underline on hover only for section H2 links).
- **`docs-code-block`:** Article `core/code` and `core/preformatted` — `light-grey-2` background, `charcoal-1` text, IBM Plex Mono, 1px `light-grey-1` border. Not the dark marketing `code-block` component.
- **`docs-toc-sidebar`:** Floating 248px sidebar via `wporg/sidebar-container` + `wporg/table-of-contents`. Pins beside the 680px article column at ≥768px; stacks above content on mobile. Article pattern injects TOC before post content in `single.html`.
- **`docs-help-footer`:** Charcoal-2 "Get more help" band before global footer. Four equal columns; link labels in `blueberry-2`, body copy in white. Links to support forums, developer.wordpress.org, Documentation issue tracker, and Learn.


## Do's and Don'ts


- On Documentation, use Inter 600 for section and in-article headings — EB Garamond for page/article titles only. Use light `docs-code-block` styling in articles, not the dark marketing code block. Topic cards use 2px radius with `is-style-cards-grid`, not 8px directory cards.
