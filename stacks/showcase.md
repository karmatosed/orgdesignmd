# Showcase

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/showcase/](https://wordpress.org/showcase/)

**Theme:** [wporg-showcase-2022](https://github.com/WordPress/wporg-showcase-2022)

**Implementation:** FSE child theme of wporg-parent-2021.

---

## Showcase typography (YAML + prose)

[wordpress.org/showcase](https://wordpress.org/showcase/) runs on [wporg-showcase-2022](https://github.com/WordPress/wporg-showcase-2022) (child of wporg-parent-2021). Unlike Plugins or Patterns directories, Showcase uses **`charcoal-1`** for the global header, sticky local nav, and homepage hero band — not `charcoal-2`. Child `theme.json` defines screenshot frame tokens (`10px` border, `20px` radius, `rgba(30, 30, 30, 0.1)` color). Homepage and archive grids use **1760px** wide layout (`spacing.showcase-wide-max`).

| Token | Font | Role |
|:------|:-----|:-----|
| `showcase-hero-title` | EB Garamond | Homepage hero H1 "Showcase" — `heading-2` (50px) white on `charcoal-1` |
| `showcase-hero-tagline` | Inter | Tagline — "The best websites, built with WordPress." below hero H1 |
| `showcase-card-title` | Inter | Linked grid post titles — `normal` (16px) with `has-inter-font-family` override |
| `showcase-site-title` | EB Garamond | Single-site post title — `heading-2` (50px) on `has-feature-color-background` hero |
| `showcase-section-heading` | Inter 300 | "View all sites" linked display — `heading-cta` (120px) with `is-style-with-arrow`, letter-spacing −2px |
| `showcase-query-total` | Inter | Result count beside search — "137 sites" in `charcoal-4` (`small`) |

Grid category terms (`core/post-terms`) use Inter `normal` (16px) with no underline until hover. Single-site meta tables use Inter `small` (14px) label/value rows via `wporg/site-meta-list`.

## Showcase layout (prose)

Templates and patterns in [wporg-showcase-2022](https://github.com/WordPress/wporg-showcase-2022):

| Template / pattern | Background | Layout |
|:-------------------|:-----------|:-------|
| `front-page.html` | `charcoal-1` header/footer | Global header + `nav-front` sticky local nav → `front-page` pattern → showcase footer pattern |
| `site-hero` (homepage) | `charcoal-1` | `.is-section-site-hero` query — 50/50 columns: left stack (EB Garamond H1 + tagline + `wporg/site-meta-list` `has-hidden-label` with `light-grey-2` text / `charcoal-3` border) + right `dots-hero.svg` cover with overlapping desktop (`is-size-desktop`, 535:300) and mobile (`is-size-mobile`, 375:600) `wporg/site-screenshot` blocks |
| `site-grid-featured` | white | Filter row → Inter H2 "Featured sites" → 3-column `post-template` grid at 1760px (`spacing-40` gap); responsive 3→2 at ≤1600px, 1 column at ≤800px |
| Grid cell | white | `wporg/site-screenshot` (`is-linked-image`) + Inter `normal` linked `post-title` + `post-terms` category (shows first one–two terms; truncates with ellipsis) |
| `View all sites` | white | Inter 300 `heading-cta` (120px) linked H2 with `is-style-with-arrow` → `/archives/` |
| `has-dots-background` spacer | white | 60px-tall repeating dot row (light-grey + Blueberry accent dots) above footer |
| Single site hero | per-site brand color | `has-feature-color-background` full-bleed band — custom `--wporg-site-screenshot--background-color` matches site brand (e.g. NASA `#1f4788`); desktop screenshot flex 4:1 over mobile; rounded top corners only |
| Single site body | white | EB Garamond `heading-2` post title + bordered `wporg/site-meta-list` (country, category, etc.) + prose content |
| Related sites | white | Inter `heading-5` "Related sites" + 3-up `wporg/site-screenshot` grid (`.wporg-related-posts`) |
| `footer` / `is-page-footer` | `charcoal-1` | Two equal columns — "Feeling inspired?" (Explore the Showcase) + "Want to be featured?" (Submit a site) with `is-style-outline-on-dark` buttons; stacks on mobile with 1px `white-opacity-15` divider |

Filter row scrolls horizontally below 889px. Search uses `is-style-secondary-search-control` with "Search sites…" placeholder. Category filter is a single `wporg/query-filter` dropdown (Business, Community, Creative, Publication, Store, etc.).

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Header CTA |
| `card-showcase` | Screenshot frames |
| `input-search` | Showcase filter |
| `showcase-featured-meta` | Rotating site meta |
| `showcase-filter-bar` | Search + count + filter |
| `showcase-hero-band` | Dot-pattern hero |
| `showcase-page-footer` | Inspired / featured CTAs |
| `showcase-site-card` | Grid cell |
| `showcase-site-header` | Charcoal-1 nav |
| `showcase-site-meta-list` | Site meta table |
| `showcase-site-screenshot` | Screenshot frame block |
| `showcase-view-all-cta` | View all sites link |
| `site-header / site-footer` | All sections |


### Component prose

**Showcase page components (prose):**

- **`showcase-site-header`:** Global header and sticky local nav both on **`charcoal-1`** — not `charcoal-2` like Plugins or Patterns. White text; site title ("Showcase") fades in on scroll via `wporg-local-navigation-bar__show-on-scroll`. Archive/search/single pages hide duplicate titles in the nav bar via theme CSS.
- **`showcase-hero-band`:** Full-bleed `charcoal-1` band containing the `.is-section-site-hero` query — EB Garamond `heading-2` "Showcase", Inter tagline, and a rotating featured site with desktop + mobile `wporg/site-screenshot` blocks overlaid on `dots-hero.svg`. Hero uses 1760px constrained width.
- **`showcase-featured-meta`:** `wporg/site-meta-list` with `has-hidden-label` on the homepage hero — table rows for site title, URL, and category in `light-grey-2` text with `charcoal-3` 1px border. Labels hidden; values link in `blueberry-2`.
- **`card-showcase` / `showcase-site-screenshot`:** YAML `card-showcase` captures the generic framed-thumbnail token (`rounded.showcase`, 10px padding). The live block is custom **`wporg/site-screenshot`** — **10px border** at `rgba(30, 30, 30, 0.1)`, **20px radius**, white/`light-grey-2` fill. Grid cards use default frame; hover darkens border to `rgba(30,30,30,0.25)`. Single-site hero uses responsive clamp borders (4px–20px) with rounded top corners only and `charcoal-3` border on `.is-section-site-hero`. Loads mshots via Interactivity API (`wporg/showcase/screenshot` store) with spinner loader. Desktop aspect ratio 535:300; mobile 375:600.
- **`showcase-filter-bar`:** Flex row — `is-style-secondary-search-control` ("Search sites…") + `wporg/query-total` count + category `wporg/query-filter` dropdown. Scrolls horizontally below 889px.
- **`showcase-site-card`:** Grid cell — linked `wporg/site-screenshot` + Inter `normal` linked `post-title` + truncated `post-terms` category link. 3-column grid at 1760px with `spacing-40` gap; drops to 2 columns at ≤1600px, 1 at ≤800px.
- **`showcase-view-all-cta`:** Inter 300 linked "View all sites" at `heading-cta` (120px) with `is-style-with-arrow` and −2px letter-spacing — links to `/archives/`.
- **`showcase-page-footer`:** `charcoal-1` two-column band (`is-page-footer`) — "Feeling inspired?" + Explore the Showcase outline button | "Want to be featured?" + Submit a site outline button. Uses `is-style-outline-on-dark`. Mobile stacks with top border divider.
- **`showcase-site-meta-list`:** Border table on single sites — rows for country, category, etc. with Inter `small` labels left-aligned and values right-aligned; 1px row dividers inherit border color. Standard variant uses `light-grey-1` border; hero variant uses hidden labels.

Depth on screenshots comes from the **border frame**, not box-shadow — unique to Showcase among wporg directories.


## Do's and Don'ts


- On Showcase, use **`charcoal-1`** for global header, local nav, and homepage hero — not `charcoal-2`. Grid post titles are **Inter `normal`**, not EB Garamond — reserve EB Garamond for hero H1 and single-site titles. Screenshot depth uses **10px border frames** at 20px radius (`rounded.showcase`), not card shadows or directory `is-style-cards-grid` patterns. Single-site heroes use per-post **`has-feature-color-background`** brand colors, not fixed wporg palette bands. Wide layout is **1760px**, not 1160px. Category filter is one **`wporg/query-filter`** dropdown, not Plugins' business-model button-list.
