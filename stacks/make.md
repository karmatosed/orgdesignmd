# Make

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://make.wordpress.org/](https://make.wordpress.org/)

**Theme:** [wporg-make-2024](https://github.com/WordPress/wporg-make)

**Implementation:** FSE child theme of wporg-parent-2021.

---

## Make typography (YAML + prose)

[make.wordpress.org](https://make.wordpress.org/) runs on [wporg-make-2024](https://github.com/WordPress/wporg-make) (child of wporg-parent-2021). The hub theme (September 2024) lists contributor teams from the custom post type `make_site` and surfaces upcoming meetings via the `wporg-make/meeting-time` block. Child `theme.json` **narrows the heading scale** and sets **Inter 600 for h2–h6** — only page/post titles and promotional display headings use EB Garamond.

| Token | Font | Role |
|:------|:-----|:-----|
| `make-hero-title` | EB Garamond | Cover H1 "Make WordPress" — 50px white on `charcoal-2` (pattern inline override) |
| `make-section-heading` | Inter 600 | "Teams" section H2 — `heading-4` (24px) per theme.json element override |
| `make-team-title` | Inter 600 | Linked team names in the directory — `heading-6` (18px) in `blueberry-1` |
| `make-team-body` | Inter | Team blurbs in the middle column — `small` (14px); glossary terms via wporg-glossary plugin |
| `make-meeting-meta` | Inter | Next-meeting lines — `extra-small` (12px) from `wporg-make/meeting-time` |
| `make-wizard-heading` | EB Garamond | "Not sure which team to contribute to?" — `heading-1` (38px) |
| `make-cta-heading` | EB Garamond | "Shape the future of WordPress" on `primary` band — `heading-1` (38px) |

Hero intro copy uses `large` (20px) at line-height 1.7 for the lead paragraph; secondary paragraph uses default body size. Individual team blogs (e.g. `/core/`, `/design/`) use legacy P2/bbPress themes — document the **hub** only.

## Make layout (prose)

Templates and patterns in [wporg-make-2024](https://github.com/WordPress/wporg-make):

| Template / pattern | Background | Layout |
|:-------------------|:-----------|:-------|
| `front-page-header.php` | `charcoal-2` | Standard `wporg/global-header` (white-opacity-15 bottom border) → white-text sticky local nav with site title on scroll → hero band with 50px H1 + `.wporg-make-front-page-intro` 50/50 flex (large tagline + body copy \| `community.webp`) |
| `front-page-content.php` | white | Inter 600 "Teams" H2 → `wporg-make-team-list` query (`make_site` CPT, 100 per page) using `card-team` template part → EB Garamond wizard H2 + contributor wizard link → full-bleed `blueberry-1` 5FTF CTA (55% heading + 45% `is-style-links-list`) |
| `card-team.html` | white | 3-column row — 19% Blueberry linked Inter `heading-6` title \| flex post content at `small` \| 36% `wporg-make/meeting-time` at `extra-small`; 1px `light-grey-1` bottom border, 30px vertical padding |
| `wporg-make/meeting-time` | white | Renders next meeting title, relative time, Slack channel link; empty when no upcoming meeting |
| Global footer | `charcoal-1` | Standard wporg global footer |

Content width is 1160px (`contentSize` in child `theme.json`). Glossary hovercards (wporg-glossary plugin) annotate terms like Core, Plugin, Slack in team blurbs. The 5FTF CTA band mirrors the Five for the Future subsite pattern — EB Garamond `heading-1` + large links list on `primary`.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Header CTA |
| `input-search` | Global header |
| `make-cta-band` | make cta band |
| `make-hero-band` | make hero band |
| `make-meeting-time` | make meeting time |
| `make-site-header` | make site header |
| `make-team-row` | make team row |
| `make-wizard-prompt` | make wizard prompt |
| `site-header / site-footer` | All sections |


### Component prose

**Make page components (prose):**

- **`make-site-header`:** Standard wporg `charcoal-2` global header with 1px `white-opacity-15` bottom border, plus sticky `charcoal-2` local nav with white text. Site title ("Make WordPress") fades in on scroll via `wporg-local-navigation-bar__show-on-scroll`. Section menu: Meetings, Team Updates, Project Updates, Five for the Future, Contributor Handbook, Communicate, Log in.
- **`make-hero-band`:** Full-bleed `charcoal-2` band — EB Garamond "Make WordPress" at 50px; `.wporg-make-front-page-intro` splits 50/50 with `large` lead paragraph (line-height 1.7) + body copy left and bottom-aligned `community.webp` photo right.
- **`make-team-row`:** Rows in `.wporg-make-team-list` query — `card-team` template renders three columns at 19% / flex / 36% with 40px gap. Team title links in **`blueberry-1`** Inter 600 `heading-6`; blurb column at `small` with glossary hovercards; meeting column optional.
- **`make-meeting-time`:** Custom `wporg-make/meeting-time` block — "Next meeting:" + bold meeting title + optional "(+N more)" link to `/meetings/#team`, `<time>` element with relative countdown, Slack channel link. Renders at `extra-small`; empty div when no meeting scheduled.
- **`make-wizard-prompt`:** White section below team list — EB Garamond `heading-1` "Not sure which team to contribute to?" + body paragraph linking to [make.wordpress.org/contribute/](https://make.wordpress.org/contribute/) contributor wizard.
- **`make-cta-band`:** Full-bleed **`primary`** band — same pattern as Five for the Future subsite: 55/45 columns with EB Garamond `heading-1` "Shape the future of WordPress", `is-style-short-text` tagline, and `is-style-links-list` with `large` organization/individual links to wordpress.org/five-for-the-future.


## Do's and Don'ts


- On Make, use **`charcoal-2`** for global header, local nav, and hero — same dark band treatment as Documentation/Patterns, not Events' light header. Hero H1 is **50px EB Garamond on `charcoal-2`**, not 50px in a separate nav-only band. Team directory uses **three-column table rows** with Blueberry Inter `heading-6` titles — not `is-style-cards-grid`. Section headings ("Teams") are **Inter 600**, not EB Garamond. Team blurbs use **glossary hovercards** (wporg-glossary). 5FTF footer CTA reuses **`is-style-links-list`** on `primary`, matching the Five for the Future subsite.
