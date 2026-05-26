# About

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/about/](https://wordpress.org/about/)

**Theme:** wporg-main-2022 [`about.php` pattern](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/about.php)

**Implementation:** Block pattern in wporg-main-2022 — not a separate child theme.

---

## About typography (YAML + prose)

[wordpress.org/about](https://wordpress.org/about/) is a deliberate departure from the EB Garamond marketing voice. It uses the `page-about` template and the [`about.php`](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/about.php) block pattern in wporg-main-2022.

| Token | Font | Role |
|:------|:-----|:-----|
| `about-cover-title` | Inter | Cover H1 — lowercase mission phrase split across two `<span>` rows ("democratize" / "publishing") |
| `about-section-heading` | Inter | Section H2s — "our story", "our mission", "the four freedoms" |
| `about-cover-pretext` | Courier Prime 700 | Cover label — "our mission:" |
| `about-body` | Courier Prime | Story copy, mission pillars, freedom descriptions, link-column intros |
| `about-freedom-number` | Inter 200 | GPL freedom index (0–3) at 160px desktop / 120px tablet |

Responsive scaling uses CSS `clamp()` in the theme (cover title 52px→96px; section headings 52px→90px) — fixed token sizes above are the pattern defaults. Section headings include hand-drawn SVG underlines (`:after` pseudo-elements in `charcoal-1` `#202020`) that differ per section (`wporg-about-section-mission` vs `wporg-about-section-freedoms`). Cover pretext and title also carry decorative SVG flourishes. All copy is lowercase by design.

## Layout

Full-bleed editorial scroll on `#F0EDE7`; shared 40/60 two-column grid (heading left, Courier Prime body right). Sections: cover → story → mission pillars → four freedoms (numbered 0–3) → three link columns (technology, details, people). Template: `page-about.html`; pattern classes: `wporg-about-section-cover`, `-story`, `-mission`, `-freedoms`, `-freedom-1`…`-freedom-4`, `-software`. Subpages reuse `_nav-about-subpage.php` with the same surface and typography.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `about-cover` | Mission cover block |
| `about-freedom-row` | GPL freedoms 0–3 |
| `about-link-column` | Technology / details / people nav |
| `about-section-row` | Story / mission 40/60 rows |
| `button-primary` | Header CTA |
| `input-search` | Global header |
| `site-header / site-footer` | All sections |


### Component prose

**About page components (prose):**

- **`about-cover`:** Warm `#F0EDE7` full-bleed band with 1px `charcoal-1` bottom border. Pretext label + two-line Inter title on a CSS grid; intro tagline in Courier Prime right-aligned in a 60% column.
- **`about-section-row`:** Repeating 40/60 column split — Inter section heading (with SVG underline) in the narrow column, Courier Prime body in the wide column. Used for story and mission pillars (`h3` + paragraph pairs at line-height 1.9).
- **`about-freedom-row`:** Four stacked rows (`wporg-about-section-freedom-1`…`-4` map to GPL indices 0–3). 40% column holds an ultra-light Inter numeral; 60% column holds the freedom description. Rows 2–4 separated by 1px `charcoal-1` top borders.
- **`about-link-column`:** Three equal columns at the footer — lowercase Courier Prime heading, intro paragraph, vertical navigation block. Technology column links use Blueberry.


## Do's and Don'ts


- On About, use Inter for display headings and Courier Prime for body — not EB Garamond. Keep all copy lowercase.
