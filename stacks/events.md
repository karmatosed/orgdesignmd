# Events

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://events.wordpress.org/](https://events.wordpress.org/)

**Theme:** [wporg-events-2023](https://github.com/WordPress/wordcamp.org) in WordCamp.org repo

**Implementation:** FSE child theme of wporg-parent-2021.

---

## Events typography (YAML + prose)

[events.wordpress.org](https://events.wordpress.org/) runs on [wporg-events-2023](https://github.com/WordPress/wordcamp.org/tree/production/public_html/wp-content/themes/wporg-events-2023) (child of wporg-parent-2021) in the [WordCamp.org](https://github.com/WordPress/wordcamp.org) repo. Launched 2023 as the NextGen events hub ([issue #1007](https://github.com/WordPress/wordcamp.org/issues/1007)). Unlike Patterns, Photos, or Documentation, Events uses a **light header stack** — white global header and white sticky local nav with **`charcoal-0`/`charcoal-1` text**, not a `charcoal-2` hero band. Child `theme.json` sets h1 to `clamp(30px, 4vw, 50px)` and widens the layout to **1600px** via `--wp--custom--layout--wide-size` in `style.css`.

| Token | Font | Role |
|:------|:-----|:-----|
| `events-hero-title` | EB Garamond | Cover H1 — *Meet the community* (italic, block display) + "behind WordPress" (`heading-2`, 50px) in `charcoal-0` on white |
| `events-stat-label` | EB Garamond | Stat tile copy — "4,099 events this year", etc. (`heading-6`, 22px) |
| `events-section-heading` | Inter 700 | Section H2 — "Upcoming events" (`medium`, 20px) |
| `events-contributors-heading` | EB Garamond | Footer H2 — "Where WordPress contributors meet" (default EB Garamond scale) |
| `events-list-title` | Inter | Event list row title links — `small` on mobile, `normal` from 1080px |

Map marker titles use Inter 600 at `normal` size (theme CSS). Local nav site title and section links render at `small` (14px). Hero tagline is default Inter body in `charcoal-0`.

## Events layout (prose)

Templates and patterns in [wporg-events-2023](https://github.com/WordPress/wordcamp.org):

| Template / pattern | Background | Layout |
|:-------------------|:-----------|:-------|
| `parts/header.html` | white | `wporg/global-header` with `charcoal-0` text + 1px `light-grey-1` bottom border → white `wporg/local-navigation-bar` with site title + `local-navigation` menu |
| `front-cover.php` | white | 50/50 columns (33/67 at ≥1440px) — EB Garamond H1 in `charcoal-0` + tagline left; `wporg/google-map` (`all-upcoming-map`, no list/search) right at 430px height (246px mobile) |
| Stats (`.wporg-events__stats`) | white | 3 equal columns — EB Garamond `heading-6` stat copy in 1px `light-grey-1` bordered boxes (2px radius) |
| `front-events.php` | white | Inter 700 "Upcoming events" H2 → filter row (search + Format / Type / Month / Country `wporg/query-filter` dropdowns) → `wporg/event-list` (limit 10 on home) → outline "Browse events" button |
| `front-contributors.php` | white | 50/50 — EB Garamond H2 + external `is-style-links-list` left; Jetpack `tiled-gallery` contributor photos right (min-width 565px at ≥1170px) |
| Event list rows (`.wporg-marker-list-item`) | white | Stacked bordered rows — 1px `light-grey-1` borders, 2px radius on first/last; 3-column grid at ≥960px (title / location / date-time) |
| `page-upcoming-events` | white | Full filter row + unbounded event list; loading placeholder at 90vh to reduce layout shift |
| Global footer | `charcoal-1` | Standard wporg global footer |

Filter row scrolls horizontally below 889px. Search uses `is-style-secondary-search-control` with "Search events…" placeholder. Map container uses `#AADAFF` (`events-map-sky`) fill at `clamp(200px, 50vh, 90vh)`.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Header CTA |
| `events-contributors-band` | events contributors band |
| `events-filters` | events filters |
| `events-google-map` | events google map |
| `events-hero-cover` | events hero cover |
| `events-list-row` | events list row |
| `events-site-header` | events site header |
| `events-stat-tile` | events stat tile |
| `input-search` | Global header |
| `site-header / site-footer` | All sections |


### Component prose

**Events page components (prose):**

- **`events-site-header`:** White global header with **`charcoal-0`** link text and 1px `light-grey-1` bottom border — not the default `charcoal-2` dark header. Sticky white local nav below with WP.org logo mark, "WordPress Events" site title at `small`, and section links (Upcoming events, Organize an event, Sponsor Events) in `charcoal-1`.
- **`events-hero-cover`:** White `.wporg-events__cover` band — 50/50 columns pairing EB Garamond `heading-2` H1 (*Meet the community* renders as block-level italic via CSS) + tagline with a full-height `wporg/google-map` block. Cover gains edge padding at ≥960px; column ratio shifts to 33/67 at ≥1440px.
- **`events-stat-tile`:** Three-up stat row — EB Garamond `heading-6` labels inside 1px `light-grey-1` bordered groups with 2px radius and asymmetric left padding (`spacing-30`). Dynamic counts on the live site (events this year, countries, participants).
- **`events-google-map`:** Custom `wporg/google-map` block — `#AADAFF` (`events-map-sky`) map container; Inter 600 marker titles; location/date-time meta with charcoal-5 dot separators. Homepage map hides list and search (`showList: false`, `showSearch: false`).
- **`events-filters`:** Flex row — `is-style-secondary-search-control` search (max 240px at ≥663px) + four `wporg/query-filter` single-select dropdowns (Format: Online/In Person; Type: Meetup/WordCamp/Other; Month; Country). Filter pills show applied state via toggle label count CSS.
- **`events-list-row`:** Rows rendered by `wporg/event-list` using `.wporg-marker-list-item` styling — 1px `light-grey-1` stacked borders, 20px padding, Inter linked title + location + date/time. Desktop grid columns widen from 45%/1fr/2fr to 60%/1fr/1fr at ≥1280px.
- **`events-contributors-band`:** White footer section — EB Garamond "Where WordPress contributors meet" H2 + `is-style-links-list` with external links (WordCamp Central, Campus Connect, Meetup.com, Do_Action, NextGen handbook) and ↗ affordance; Jetpack rectangular tiled gallery of contributor photos in the right column.


## Do's and Don'ts


- On Events, use the **light header stack** — white global header with `charcoal-0` text and white local nav, not `charcoal-2` hero bands. Hero H1 is **`charcoal-0` EB Garamond on white**, with italic *Meet the community* as a block line. Map wash is **`events-map-sky`** (`#AADAFF`), not `light-grey-2`. Event list rows use **stacked 1px borders**, not card grids. Wide layout is **1600px**, not 1160px. Filters use four **`wporg/query-filter`** dropdowns (Format, Type, Month, Country), not Patterns' category button-list.
