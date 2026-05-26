# Main

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/](https://wordpress.org/)

**Theme:** [wporg-main-2022](https://github.com/WordPress/wporg-main-2022)

**Implementation:** Homepage block patterns in wporg-main-2022 — shared global header/footer via mu-plugins.

---

## Typography

Main homepage uses wporg display tokens from [`DESIGN.md`](../DESIGN.md):

| Token | Role |
|:------|:-----|
| `display-cta` | 120px EB Garamond hero headline |
| `headline-1`–`headline-6` | Campaign section headings |
| `code-display` | Download counter (Plex Mono, clamp scale) |
| `accent-display` | Anton marketing patterns only |

Body and UI use Inter at `body-md` (16px, line-height 1.875). Buttons use Inter 600 at `rounded.sm` (2px).


## Layout

Full-bleed alternating sections; logo marquee breaks the grid.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Header CTA |
| `input-search` | Global header |
| `site-header / site-footer` | All sections |


## Do's and Don'ts

- Don't apply showcase 20px frames to directory UI.
- Don't use Anton or display-cta scale outside the main homepage and Enterprise cover.
