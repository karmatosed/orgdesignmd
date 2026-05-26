# News

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/news/](https://wordpress.org/news/)

**Theme:** [wporg-news-2021](https://github.com/WordPress/wporg-news-2021)

**Implementation:** FSE child theme of wporg-parent-2021.

---

## News typography (YAML + prose)

[wordpress.org/news](https://wordpress.org/news/) runs on [wporg-news-2021](https://github.com/WordPress/wporg-news-2021) with its own `theme.json`. Headlines are EB Garamond; UI/meta is Inter at 14px (`small`). Body line height is **1.9** on articles (slightly looser than the 1.875 wporg default).

| Token | Font | Role |
|:------|:-----|:-----|
| `news-hero-title` | EB Garamond | Front-page H1 "News" — white on blue, scales 80px→160px |
| `news-section-heading` | EB Garamond | Section H2s — "Latest Release", "Latest Posts", "People of WordPress" (38px→50px) |
| `news-release-version` | Inter 200 | `wporg/release-version` block — giant version numeral (e.g. "7.0") |
| `news-post-title` | EB Garamond | Post titles in lists (26px h2 scale) and article headers |
| `news-meta` | Inter | Category terms, dates, author bylines (`entry-meta`) |

Article blocks add editorial scales not in YAML: pullquotes at 50px EB Garamond; blockquotes at 30px with a 2px `deep-blueberry` left border; drop caps at 110px. Single posts use EB Garamond H1 at 38px desktop / 70px mobile per `theme.json` custom heading breakpoints.

## News layout (prose)

Front page template parts in [wporg-news-2021/block-template-parts/front-page/](https://github.com/WordPress/wporg-news-2021/tree/trunk/source/wp-content/themes/wporg-news-2021/block-template-parts/front-page):

| Section class | Background | Layout |
|:--------------|:-----------|:-------|
| `front__site-title` | `news-blue` | Full-bleed H1 with `brush-stroke-big.svg` mask overlay in `deep-blueberry` |
| `front__latest-release` | `news-blue` | Flex row: sidebar heading + release version link; 1px `deep-blueberry` divider |
| `front__latest-posts` | white | Flex row: sidebar heading + 5-post list; 1px `light-grey-1` divider |
| `front__people-of-wordpress` | `news-surface` | 5-up square tile grid; title overlays on hover |
| `bottom-banner-items` | white | 2×2 grid of CTA columns (Follow The Code, Find An Event, Subscribe, Contribute) |

"See All" links (`front__next-page`) use hand-drawn brush-stroke SVG backgrounds unique to each section. Single posts: meta line → EB Garamond title → full-width separator → content → Jetpack share icons in `news-blue`.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Header CTA |
| `card-news` | People/archive cards |
| `input-search` | Global header |
| `news-bottom-banner` | 4-column CTA footer |
| `news-hero` | Front-page title band |
| `news-latest-posts` | Post list section |
| `news-latest-release` | Release version row |
| `news-people-tile` | People grid tiles |
| `news-release-version` | Version numeral block |
| `site-header / site-footer` | All sections |


### Component prose

**News page components (prose):**

- **`news-hero`:** Full-bleed blue band blending global header into content. EB Garamond "News" at up to 160px; decorative brush stroke via CSS `mask-image` on `::after`.
- **`news-latest-release`:** Queries latest post in `releases` category. Sidebar "Latest Release" heading; linked `news-release-version` numeral (Inter 200); date and "See All Releases" pinned to bottom-left on desktop. Hover darkens release link area and animates a right-arrow SVG (≥1500px).
- **`news-latest-posts`:** Five most recent posts. Inter 600 is *not* used — titles inherit EB Garamond h2 scale. Category terms + date in `news-meta` row.
- **`news-people-tile`:** Square aspect-ratio cards tagged `people-of-wordpress`. Grayscale photos with blue multiply overlay on hover; white title fades in. Fallback tiles are solid `news-blue`.
- **`news-bottom-banner`:** Four equal CTA panels with 1px `light-grey-1` grid dividers; Jetpack subscription form in the subscribe column.
- **`news-release-version`:** Custom block (`wporg/release-version`) parsing version numbers from release post titles; renders major version only when `showMajorVersion` is set.


## Do's and Don'ts


- On News front page, white links on blue sections invert the default link color; do not apply `primary` link styling inside `news-latest-release`.
