# Developer

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://developer.wordpress.org/](https://developer.wordpress.org/)

**Theme:** [wporg-developer-2023](https://github.com/WordPress/wporg-developer)

**Implementation:** FSE child theme of wporg-parent-2021.

---

## Developer typography (YAML + prose)

[developer.wordpress.org](https://developer.wordpress.org/) runs on [wporg-developer-2023](https://github.com/WordPress/wporg-developer) (child of wporg-parent-2021). The homepage mirrors Documentation's card-grid layout, but handbooks and the code reference add **IBM Plex Mono titles** and syntax-highlighted API type colors.

| Token | Font | Role |
|:------|:-----|:-----|
| `dev-hero-title` | EB Garamond | Front-page H1 "Developer Resources" — 50px white on `charcoal-2`; tagline "/The freedom to build" |
| `dev-section-heading` | Inter 600 | Section H2s — "Documentation", "API Reference", "Developer Blog", "Get Involved" (20px) |
| `dev-handbook-card-title` | Inter 600 | Handbook/API cards in `is-style-cards-grid` (16px) |
| `dev-code-reference-title` | IBM Plex Mono | Function/class/hook page H1 via `wporg/code-reference-title` (24px `extra-large`) |
| `dev-latest-news-title` | EB Garamond | Post titles in `wporg/latest-news` `is-style-cards` block (16px normal) |

Handbook prose uses Inter 600 for H2–H4 (same narrowed scale as Documentation). Inline code uses `light-grey-2` background at 2px radius; fenced blocks use the `wporg-developer-code-block` toolbar pattern (grey header bar + white pre body).

Code reference list items color-code API types via `dev-syntax-*` tokens: functions (`dev-syntax-green`), hooks (`dev-syntax-red`), classes (`dev-syntax-class`), methods (`dev-syntax-blue`).

## Developer layout (prose)

Templates and patterns in [wporg-developer-2023](https://github.com/WordPress/wporg-developer):

| Template / class | Background | Layout |
|:-----------------|:-----------|:-------|
| `front-page-header` pattern | `charcoal-2` hero + `lemon-3` notice | Sticky local nav (`menuSlug: developer`); EB Garamond H1 + tagline; centered version API link |
| `front-page-content` pattern | white | Documentation 3-col `is-style-cards-grid`; API Reference 2-col grid (`minimumColumnWidth: 49%`); Developer Blog white band with `wporg/latest-news` `is-style-cards`; Get Involved 2-col grid |
| `wporg-front-page-footer` | `charcoal-2` | "More resources" + "Related" — 2×50% columns with `blueberry-2` handbook links |
| Handbook (`single-handbook.html`) | white / `dev-linen` | `.has-three-columns` + floating TOC; Inter body headings |
| Code reference (`single.html`) | white | Plex Mono H1 (`wporg/code-reference-title`); TOC sidebar; source/changelog/related blocks below content |
| Reference index (`page-reference.html`) | white | Two-column: new/updated list + bordered API nav box (`wporg-reference-list`) |

Handbook landing pages (Block Editor, Themes, Plugins, etc.) often use `dev-linen` (`#FBFAF7`) as a warm content wash — distinct from Documentation's white default. Callout boxes (`.callout`, `.callout-info`, `.callout-alert`, `.callout-warning`) reuse Documentation-style tint mapping: `acid-green-3`, `blueberry-4`, `lemon-3`, `pomegrade-3`.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Header CTA |
| `dev-callout` | Handbook callout box |
| `dev-code-block` | Copy-toolbar code block |
| `dev-code-reference-title` | Plex Mono API H1 |
| `dev-handbook-card` | Handbook/API cards |
| `dev-hero` | Front-page title band |
| `dev-latest-news-card` | Developer Blog cards |
| `dev-more-resources` | Homepage footer band |
| `dev-syntax-badge-class` | Class type pill |
| `dev-syntax-badge-function` | Function type pill |
| `dev-syntax-badge-hook` | Hook type pill |
| `dev-version-notice` | API version banner |
| `input-search` | Global header |
| `site-header / site-footer` | All sections |


### Component prose

**Developer page components (prose):**

- **`dev-hero`:** Charcoal-2 band with sticky local nav (`menuSlug: developer`). EB Garamond "Developer Resources" at 50px; tagline "/The freedom to build" in white. No language-suggest bar — version notice follows instead.
- **`dev-version-notice`:** Full-width `lemon-3` banner below hero — "See what has changed in the WordPress X.X API" with Blueberry link. Distinct from Documentation's `blueberry-4` language-suggest.
- **`dev-handbook-card`:** Cells in `is-style-cards-grid` — same 1px border / 2px radius / hover as Documentation topic cards. Documentation section uses 3-up grid; API Reference uses 2-up (`minimumColumnWidth: 49%`).
- **`dev-latest-news-card`:** `wporg/latest-news` block with `is-style-cards` — EB Garamond post titles, category + date meta in `charcoal-4` at 14px.
- **`dev-code-reference-title`:** `wporg/code-reference-title` block — IBM Plex Mono 24px H1 with semantic type color (function/hook/class/method). Type label uses alpha-washed background from `dev-syntax-*` tokens.
- **`dev-code-block`:** `.wporg-developer-code-block` — grey toolbar header on `light-grey-2` with copy button; white pre body below. Inline `code` uses `light-grey-2` fill at 2px radius.
- **`dev-callout`:** Handbook callout boxes (`.callout`, `.callout-info`, `.callout-alert`, `.callout-warning`) — default `acid-green-3`, info `blueberry-4`, alert `lemon-3`, warning `pomegrade-3`.
- **`dev-syntax-badge-*`:** API type pills in reference lists — function (`dev-syntax-green`), hook (`dev-syntax-red`), class (`dev-syntax-class`). Method type uses `dev-syntax-blue`.
- **`dev-more-resources`:** Charcoal-2 homepage footer — "More resources" + "Related" columns with `blueberry-2` handbook links (Documentation Contributor Handbook, Core Contributor Handbook, Learn WordPress).


## Do's and Don'ts


- On Developer, use `lemon-3` for the API version notice — not Documentation's `blueberry-4` language-suggest. Code reference titles are IBM Plex Mono with `dev-syntax-*` type colors; handbook prose headings stay Inter 600. Reuse Documentation's card grid and TOC sidebar patterns; handbook pages may use `dev-linen` wash.
