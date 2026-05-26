# Enterprise

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/enterprise/](https://wordpress.org/enterprise/)

**Theme:** wporg-main-2022 [`enterprise.php` pattern](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/enterprise.php)

**Implementation:** Block pattern in wporg-main-2022.

---

## Enterprise typography (YAML + prose)

[wordpress.org/enterprise](https://wordpress.org/enterprise/) uses the [`enterprise.php`](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/enterprise.php) pattern in wporg-main-2022 (`page-enterprise.html`). The cover H1 uses the parent **`heading-cta`** preset (120px EB Garamond) on a solid **`primary`** band — the same display scale as the main homepage hero.

| Token | Font | Role |
|:------|:-----|:-----|
| `enterprise-cover-title` | EB Garamond | Cover H1 "Enterprise" — 120px white on `primary` (`heading-cta` preset) |
| `enterprise-section-heading` | EB Garamond | "Enterprise use cases" H2 — 36px (`heading-3`) |
| `enterprise-feature-heading` | EB Garamond | Feature column H2s — "Extensibility", "Security", "Open source" (`heading-4`, 30px) |
| `enterprise-use-case-heading` | Inter 600 | Use-case H3s — Media, E-commerce, Content marketing, Higher education (`large`, 20px) |
| `enterprise-cta-heading` | Inter 300 | "Get WordPress" linked H2 — 98px with `is-style-with-arrow`; scales to 52px on mobile |
| `enterprise-resource-heading` | EB Garamond | Link-column H3s — Case studies, White papers, Tutorials (`heading-5`, 26px) |

Use-case body copy uses `is-style-short-text`. Resource lists use Inter `small` (14px) with Blueberry links. External tutorial links carry the `external-link` list-item class.

## Enterprise layout (prose)

Pattern [`wporg-main-2022/enterprise`](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/enterprise.php) in template `page-enterprise.html`:

| Section class | Background | Layout |
|:--------------|:-----------|:-------|
| `wporg-enterprise-cover` | `primary` | Full-bleed EB Garamond H1 (`heading-cta`, 120px) + 55/45 columns — intro paragraph left, empty right column for balance |
| `wporg-enterprise-header` / `wporg-enterprise-logos` | `charcoal-2` | Centered flex-wrap logo row at 1020px — 10 brand WebP logos with fixed flex-basis widths; mobile: 2-column grid, logos capped at 20px height |
| `wporg-enterprise-use-cases` | white | `heading-3` H2 + intro paragraph + two stacked 2-column rows (Inter 600 H3 + `is-style-short-text` blurb each) |
| `wporg-enterprise-features` | white | 3 equal columns separated by 1px `light-grey-1` vertical borders — 48–56px PNG icon + `heading-4` H2 + prose; mobile stacks with top borders |
| `wporg-enterprise-get-wordpress` | `light-grey-2` | 1px `light-grey-1` top border; 5rem vertical padding; Inter 300 linked "Get WordPress" H2 with arrow (`is-style-with-arrow`, 98px→52px); 3-column PDF/Vimeo link lists + second 3-column "Additional case studies" grid |

Uses standard wporg global header/footer blocks. Section vertical padding overrides `--spacing-60` to `clamp(40px, 5.556vw, 80px)` on features and use-cases bands.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Header CTA |
| `enterprise-cover` | enterprise cover |
| `enterprise-download-cta` | enterprise download cta |
| `enterprise-feature-column` | enterprise feature column |
| `enterprise-logo-band` | enterprise logo band |
| `enterprise-resource-links` | enterprise resource links |
| `enterprise-use-cases` | enterprise use cases |
| `input-search` | Global header |
| `site-header / site-footer` | All sections |


### Component prose

**Enterprise page components (prose):**

- **`enterprise-cover`:** Full-bleed `primary` band — EB Garamond "Enterprise" at 120px (`heading-cta`); white text and links. 55% column holds the platform intro paragraph; 45% column intentionally empty for asymmetric layout.
- **`enterprise-logo-band`:** `charcoal-2` band wrapping `.wporg-enterprise-logos` — flex-wrap centered row of 10 enterprise brand logos (Sun, People, Reader's Digest, WWD, Variety, Time, TED, Facebook, Microsoft, CNN) as WebP images with per-logo fixed flex sizes. Mobile CSS switches to 2-column grid with 20px max logo height.
- **`enterprise-use-cases`:** White section — `heading-3` "Enterprise use cases" H2, intro copy, then 2×2 column grid of Inter 600 H3 titles with `is-style-short-text` descriptions (Media and publishing, E-commerce, Content marketing, Higher education).
- **`enterprise-feature-column`:** Three-column band with 1px `light-grey-1` right borders on the first two columns — PNG icon (48–63px) + EB Garamond `heading-4` H2 + body paragraph. Below 782px, columns stack with 1px top borders instead of vertical dividers.
- **`enterprise-download-cta`:** `light-grey-2` footer band — linked Inter 300 "Get WordPress" display heading at 98px with `is-style-with-arrow` (52px on mobile), Blueberry link color. Sits above the resource link grids.
- **`enterprise-resource-links`:** Three-column link lists inside the download band — Case studies, White paper references, and Tutorials (Vimeo external links with `external-link` class), plus a second 3-column row of additional PDF case studies. H3s use `heading-5`; list items at `small` size.


## Do's and Don'ts


- On Enterprise, use **`primary`** for the cover band and **`charcoal-2`** for the logo marquee — not the dark stacked bands from Blocks. Cover H1 uses **`heading-cta`** (120px EB Garamond), shared with the main homepage display scale. Feature columns use vertical `light-grey-1` dividers, not card borders. "Get WordPress" CTA is Inter 300 with `is-style-with-arrow`, not a button component.
