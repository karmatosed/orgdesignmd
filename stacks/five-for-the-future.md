# Five for the Future

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/five-for-the-future/](https://wordpress.org/five-for-the-future/)

**Theme:** [wporg-5ftf-2024](https://github.com/WordPress/five-for-the-future) + **wporg-5ftf** plugin

**Implementation:** FSE child theme of wporg-parent-2021.

---

## Five for the Future typography (YAML + prose)

[wordpress.org/five-for-the-future](https://wordpress.org/five-for-the-future/) runs on [wporg-5ftf-2024](https://github.com/WordPress/five-for-the-future/tree/production/themes/wporg-5ftf-2024) (child of wporg-parent-2021) with the **wporg-5ftf** plugin for pledges. Refreshed September 2024 ([Meta announcement](https://make.wordpress.org/meta/2024/09/12/the-five-for-the-future-site-gets-a-refresh/)). Unlike Patterns/Photos directories, the local nav band uses **`charcoal-1`**, not `charcoal-2`. Child `theme.json` narrows the heading scale: h1 maps to `heading-2` (50px), h2 to `heading-3` (36px), h3 to `heading-4` (30px).

| Token | Font | Role |
|:------|:-----|:-----|
| `5ftf-hero-title` | EB Garamond | Site title "Five for the Future" in sticky local nav — 50px white on `charcoal-1` |
| `5ftf-hero-tagline` | Inter | Tagline "Commit to the future of WordPress and the open web." — line-height 2.3 |
| `5ftf-tldr` | Inter | Intro paragraph in hero section — `extra-large` (24px) with `is-style-wporg-tldr` |
| `5ftf-section-heading` | EB Garamond | Content H2s — "Take your seat at the table", "Extend your expertise…" (`heading-3`, 36px) |
| `5ftf-benefit-heading` | Inter 600 | Benefit column titles — Strategic advantage, Recruit talent, etc. (`normal`, 16px) |
| `5ftf-cta-heading` | EB Garamond | "Shape the future of WordPress" on `primary` band — `heading-2` (50px) |
| `5ftf-feature-heading` | Inter 600 | Case study H3 — "Salesforce empowers WordPress" (`extra-large`, 24px) |
| `5ftf-testimonial-name` | Inter 600 | Contributor name on dark band — `large` (20px); sponsor line at `small` |

Benefit body copy uses default Inter prose. Testimonial quotes use `is-style-short-text` in `light-grey-1`. CTA band links use `is-style-links-list` at `large` size — not button components.

## Five for the Future layout (prose)

Templates and patterns in [wporg-5ftf-2024](https://github.com/WordPress/five-for-the-future) + block editor page content on the front page:

| Template / pattern | Background | Layout |
|:-------------------|:-----------|:-------|
| `header-front-page.php` | `charcoal-1` | Sticky local nav — site-title H1 at 50px + white tagline; global header also on `charcoal-1` (not `charcoal-2`) |
| WordCamp cover block | photo + overlay | Full-bleed `core/cover` with `5ftf-wordcamp.jpg`, min-height 260px, light overlay |
| `.is-hero-section` | `charcoal-1` | Two columns — `is-style-wporg-tldr` + `is-style-short-text` intro (`extra-large`) left; header graphic PNG bottom-aligned right; stacks on mobile via theme SCSS |
| "Take your seat at the table" | white | `alignwide` EB Garamond H2 + prose with handbook / pledges / sponsorships links |
| Benefits grid | `light-grey-2` | 2×2 columns — 42–56px PNG icon + Inter 600 H2 (`normal`) + body paragraph each |
| Expertise section | white | WordCamp Asia cover image beside H2 + bullet list of contribution areas + Make/WordPress link |
| CTA band | `primary` | White text — `heading-2` H2 + `is-style-links-list` with `large` organization / individual links |
| "Driving WordPress Forward" | `charcoal-1` | Case study row (Inter 600 H3 + Salesforce copy + logo) → testimonial header row (H3 + `blueberry-2` "See all testimonials") → 3-column testimonial cards with 100px rounded duotone-grayscale avatars |
| Pledges archive | white | Custom post type `5ftf_pledge` list — `.wp-block-post:where(li.type-5ftf_pledge)` styling in `style.scss` |
| Global footer | `charcoal-1` | Standard wporg global footer |

Handbook, for-organizations, for-individuals, testimonials, and sponsorships pages reuse the same `header-front-page` pattern with standard FSE templates. Homepage content is editor-managed blocks, not a single monolithic pattern like Enterprise.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `5ftf-benefit-column` | 5ftf benefit column |
| `5ftf-case-study-row` | 5ftf case study row |
| `5ftf-cta-band` | 5ftf cta band |
| `5ftf-hero-section` | 5ftf hero section |
| `5ftf-photo-cover` | 5ftf photo cover |
| `5ftf-site-header` | 5ftf site header |
| `5ftf-testimonial-card` | 5ftf testimonial card |
| `button-primary` | Header CTA |
| `input-search` | Global header |
| `site-header / site-footer` | All sections |


### Component prose

**Five for the Future page components (prose):**

- **`5ftf-site-header`:** Global header and sticky local nav both on **`charcoal-1`** — darker than Patterns/Photos (`charcoal-2`). Site title renders as H1 at 50px EB Garamond; tagline "Commit to the future of WordPress and the open web." at line-height 2.3 in white Inter.
- **`5ftf-photo-cover`:** Full-bleed WordCamp crowd photo (`5ftf-wordcamp.jpg`) via `core/cover` — min-height 260px, light overlay, no text overlay.
- **`5ftf-hero-section`:** Charcoal-1 band with `.is-hero-section` class — two columns pairing `is-style-wporg-tldr` intro (`extra-large`) with the 5FTF header graphic PNG. Theme SCSS stacks columns on narrow viewports.
- **`5ftf-benefit-column`:** Cells in a `light-grey-2` 2×2 grid — centered PNG icon (42–56px), Inter 600 benefit title at `normal` size, body paragraph. Distinct from Enterprise's vertical-divider feature band.
- **`5ftf-cta-band`:** Full-bleed **`primary`** band with white text — EB Garamond `heading-2` "Shape the future of WordPress" plus `is-style-links-list` with `large` links to for-organizations and for-individuals. Uses link list, not button components.
- **`5ftf-case-study-row`:** Charcoal-1 row — Inter 600 `extra-large` H3, Salesforce sponsorship copy, and dark-background logo PNG. Opens the "Driving WordPress Forward" section.
- **`5ftf-testimonial-card`:** Three-up grid on charcoal-1 — 100px circular avatar with `is-style-wporg-hero is-style-rounded wp-duotone-grayscale`; Inter 600 name at `large`; sponsor attribution at `small` linking to pledge pages; quote in `is-style-short-text` at `light-grey-1`. "See all testimonials" link uses `blueberry-2`.


## Do's and Don'ts


- On Five for the Future, use **`charcoal-1`** for the local nav and hero bands — not `charcoal-2` like Patterns/Photos. Site title is 50px EB Garamond in the nav pattern, not a separate cover H1. CTA band uses **`is-style-links-list`** at `large` size on `primary`, not button components. Testimonial avatars use **`wp-duotone-grayscale`** with rounded hero style at 100px. Benefit titles are Inter 600 at `normal` size, not EB Garamond.
