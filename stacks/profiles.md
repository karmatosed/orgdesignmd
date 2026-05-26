# Profiles

**Inherits:** wporg palette and global header/footer chrome from [`DESIGN.md`](../DESIGN.md). Use `profiles-*` tokens for profile body UI — not `charcoal-*`.

**URL:** [https://profiles.wordpress.org/](https://profiles.wordpress.org/)

**Theme:** BuddyPress + legacy `profiles.wordpress.org` theme

**Implementation:** Hybrid — global header/footer via pub-sync mu-plugins; BuddyPress body UI.

---

## Colors

### Profiles CSS variable map

BuddyPress theme aliases in `style.css` map to YAML tokens:

| CSS var | YAML token |
|:--------|:-----------|
| `--c-blue` | `primary` |
| `--c-ink-1` … `--c-ink-4` | `profiles-ink-1` … `profiles-ink-4` |
| `--c-line-1`, `--c-line-2` | `profiles-line-1`, `profiles-line-2` |
| `--c-surface-1`, `--c-surface-2` | `profiles-surface-1`, `profiles-surface-2` |
| `--c-success`, `--c-success-wash` | `profiles-success`, `profiles-success-wash` |
| `--c-warn`, `--c-warn-wash` | `profiles-warn`, `profiles-warn-wash` |
| `--c-accent`, `--c-accent-wash` | `profiles-accent`, `profiles-accent-wash` |
| `--f-sans`, `--f-serif`, `--f-mono` | Inter, EB Garamond, IBM Plex Mono |

## Profiles typography (YAML + prose)

BuddyPress profile pages use **`profiles-heading`** (Inter) for `h1`–`h6` in the profile body — not wporg `headline-*` tokens. Serif appears via:

- **`profiles-impact-stat`** — 52px EB Garamond in `.impact-tile .n`
- **`profiles-section-title`** — 32px EB Garamond for timeline/specs section headers
- **`profiles-label-chip`** — 10px mono uppercase for chip labels, time windows, sponsor tags
- **`profiles-mono-sm`** — 11px mono for timestamps, pagination, joined date

## Profiles layout (prose)

Profile pages on [profiles.wordpress.org](https://profiles.wordpress.org/) use a **hybrid stack**: shared wporg global header/footer (block mu-plugins) plus BuddyPress-driven content in the legacy `profiles.wordpress.org` theme. Layout and components vary by what a contributor has enabled (teams, sponsorship, badges, tabs) — document the **patterns**, not individual profile content.

- **Hero (`wp-p2-hero`):** CSS grid — avatar | identity (name, @handle, location, team chips, optional sponsor pill) | social/meta links.
- **Impact row (`wp-p2-impact`):** Three equal tiles (30 / 90 / 365 days) when activity stats exist; large serif count, mono window label, high/med/impact breakdown.
- **Activity feed:** Chronological BuddyPress activity list with Dashicons per contribution type (Core, Meta, Plugins, GitHub, WordCamp, etc.).
- **Tabs:** Plugins, Photos, Courses, Favorites — rendered when applicable; 8px radius cards with `#E6E7E9` borders.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `activity-badge-high` | activity badge high |
| `activity-badge-high/med` | `.wbadge.high` / `.wbadge.med` |
| `activity-badge-med` | activity badge med |
| `button-primary` | Header CTA (shared) |
| `card-course` | Completed courses tab |
| `card-directory` | Plugin favorites tab |
| `chip-team` | Team pills (`wp-p2-chip`) |
| `impact-tile` | 30/90/365-day stats |
| `input-search` | Global header |
| `medal-*` | Contribution badges (see badge table) |
| `medal-buddypress` | medal buddypress |
| `medal-core-ai` | medal core ai |
| `medal-design` | medal design |
| `medal-plugins` | medal plugins |
| `medal-themes` | medal themes |
| `site-header / site-footer` | All sections |
| `sponsor-pill` | Five for the Future sponsorship |
| `timeline-filter-chip` | Activity type filters |
| `timeline-filter-chip-active` | timeline filter chip active |
| `timeline-row` | Activity list items |


### Component prose

### Profiles/BuddyPress components (prose)

YAML includes representative `medal-*` components wired to `badge-*` colors. When rendering any contribution badge, look up the CSS class in the badge table above and use the matching `colors.badge-*` token for the 4px ring and icon tint.

**Sponsor pill (`wp-p2-sponsor-pill`):** `sponsor-pill` component — mono `profiles-label-chip` "SPONSORED" tag on `profiles-ink-1`, verified checkmark in `profiles-success`.

**Activity timeline (`wp-p2-tlrow`):** bordered rows using `profiles-line-1`; filter chips toggle between `timeline-filter-chip` and `timeline-filter-chip-active`.


## Do's and Don'ts


- Do use YAML `badge-*` tokens for contribution medals — see badge table in [`DESIGN.md`](../DESIGN.md).

- Do use `profiles-*` tokens (not wporg `charcoal-*`) when building BuddyPress profile UI.

- Don't use wporg `headline-*` tokens on Profiles body headings — use `profiles-heading`.

- On Profiles, use Inter for headings — reserve EB Garamond for impact stat numbers only.

- Don't simplify contribution medals to one color; each WordPress team has a distinct badge color.
