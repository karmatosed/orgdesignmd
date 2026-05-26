# Plugins

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/plugins/](https://wordpress.org/plugins/)

**Theme:** `pub/wporg-plugins-2024` + **plugin-directory** plugin

**Implementation:** FSE child theme in WordPress/wordpress.org repo.

---

## Plugins typography (YAML + prose)

[wordpress.org/plugins](https://wordpress.org/plugins/) runs on **`pub/wporg-plugins-2024`** (child of wporg-parent-2021) in the [WordPress/wordpress.org](https://github.com/WordPress/wordpress.org) repo, with homepage sections rendered by the **plugin-directory** plugin's `wporg/front-page` block. Refreshed 2024 alongside Patterns and Photos directories. Child `theme.json` narrows the heading scale (Inter 600 for h2–h6) and sets **960px content / 1160px wide** layout. The sibling [Themes directory](https://wordpress.org/themes/) uses `pub/wporg-themes-2024` with the same hero and card patterns — document Plugins here; Themes shares tokens.

| Token | Font | Role |
|:------|:-----|:-----|
| `plugins-hero-title` | EB Garamond | Front-page H1 "Plugins" — 50px white on `charcoal-2` (pattern inline override) |
| `plugins-hero-tagline` | Inter | Dynamic tagline — "Browse over X free plugins" at line-height 2.3; count rounded down to nearest thousand |
| `plugins-section-heading` | Inter 600 | Curated section H2s — "Featured plugins", "Beta plugins", etc. (`heading-5`, 20px) |
| `plugins-card-title` | Inter 600 | Linked H3 inside `.plugin-card` — plugin name in card grid |
| `plugins-card-meta` | Inter | Footer meta row — author name, active installs, tested-with version (`small`, 14px) with inline SVG icons |
| `plugins-sidebar-heading` | Inter 600 | Classic widget H2 titles — "Add your plugin", "Create a plugin", "Stay up-to-date" |

Star ratings use Dashicons via `wporg-ratings` at **`plugins-star-rating`** (`#FFB900`) — WordPress admin star yellow, not campaign `lemon-*` tints. Excerpt copy uses default Inter body at 16px. "See all" section links use Inter at default size with Blueberry hover underline.

## Plugins layout (prose)

Templates and patterns in **`pub/wporg-plugins-2024`** + **plugin-directory** plugin blocks:

| Template / pattern | Background | Layout |
|:-------------------|:-----------|:-------|
| `front-page-nav.php` | `charcoal-2` | Sticky `wporg/local-navigation-bar` — site title shows on scroll (`wporg-local-navigation-bar__show-on-scroll`); `menuSlug: plugins` horizontal nav at `small` size |
| `front-page-header.php` | `charcoal-2` | EB Garamond 50px H1 + white tagline at line-height 2.3; plugin count floored to nearest thousand; followed by `wporg/language-suggest` with `/plugins/v2/locale-banner` endpoint |
| `wporg-plugins__filters` | white | Flex filter bar — `is-style-secondary-search-control` search ("Search plugins") + optional `wporg/query-total` + **`is-style-button-list`** nav (All / Community / Commercial via `plugin_business_model` query arg) |
| Curated sections (`.plugin-section`) | white | Inter 600 `heading-5` H2 + Blueberry "See all" link → `wp-block-query.plugin-cards` with `is-style-cards-grid` post template |
| Plugin card (`.plugin-card`) | `light-grey-2` | Custom theme block — icon thumbnail (128/256px from `ps.w.org`) + linked Inter H3 + `wporg-ratings` stars + excerpt + footer meta (author, active installs, tested-with SVG icons) |
| `#secondary` sidebar | white | Classic widget area — three text widgets with Inter widget titles; not block patterns |
| Global footer | `charcoal-1` | Standard wporg global footer |

Homepage sections are driven by the `wporg/front-page` block in the plugin-directory plugin — Featured, Beta, Popular, and Block-Enabled each query plugins by `plugin_section` taxonomy. Search and browse archive pages reuse the filter bar and card grid without curated section headings. Card cells use parent-theme **`is-style-cards-grid`** equal-height rows on **`surface-dim`** (`#F6F6F6`) — not Documentation's bordered white cards.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Header CTA |
| `card-directory` | Plugin/theme listings |
| `input-search` | Directory search |
| `plugins-filter-bar` | plugins filter bar |
| `plugins-hero-band` | plugins hero band |
| `plugins-language-suggest` | plugins language suggest |
| `plugins-plugin-card` | plugins plugin card |
| `plugins-sidebar-widget` | plugins sidebar widget |
| `plugins-site-header` | plugins site header |
| `site-header / site-footer` | All sections |


### Component prose

**Plugins page components (prose):**

- **`plugins-site-header`:** Standard wporg `charcoal-2` global header plus sticky `charcoal-2` local nav with white text. Site title ("Plugin Directory") fades in on scroll via `wporg-local-navigation-bar__show-on-scroll`. Horizontal `menuSlug: plugins` navigation at `small` size with 24px link gap.
- **`plugins-hero-band`:** Full-bleed `charcoal-2` band — EB Garamond "Plugins" at 50px; dynamic tagline "Browse over X free plugins" at line-height 2.3 (count rounded to nearest thousand via PHP in `front-page-header.php`).
- **`plugins-language-suggest`:** Full-width `wporg/language-suggest` bar below hero — `blueberry-4` wash matching Documentation; REST endpoint `/plugins/v2/locale-banner` for locale-specific banner copy.
- **`plugins-filter-bar`:** `.wporg-filter-bar.wporg-plugins__filters` flex row — `is-style-secondary-search-control` search with "Search plugins" placeholder; optional `wporg/query-total` count; **`is-style-button-list`** navigation for All / Community / Commercial (`plugin_business_model` query parameter). Homepage may hide count via `wporg-plugins__filters__no-count`.
- **`plugins-plugin-card`:** Custom theme `plugin-card` block inside `is-style-cards-grid` — `light-grey-2` (`surface-dim`) fill, 8px radius, equal-height rows. Structure: `.entry-thumbnail` with `plugin-icon` from `ps.w.org` (128px with 256px `srcset`) → linked Inter H3 `.entry-title` → `wporg-ratings` stars at **`plugins-star-rating`** (`#FFB900`) + rating count → excerpt paragraph → footer row with inline SVG icons for author, active installs, and tested-with version.
- **`plugins-sidebar-widget`:** Classic `#secondary.widget-area` on homepage — three text widgets ("Add your plugin", "Create a plugin", "Stay up-to-date") with Inter widget titles and Blueberry handbook links. Not FSE block patterns; rendered via registered sidebar.

Curated homepage sections (Featured, Beta, Popular, Block-Enabled) each pair an Inter 600 section H2 with a "See all" link to browse URLs. The `wporg/front-page` block in the plugin-directory plugin renders these query sections.


## Do's and Don'ts


- On Plugins, use **`charcoal-2`** for local nav and hero — same directory treatment as Patterns/Photos/Documentation, not Events' light header. Hero H1 is **50px EB Garamond** with dynamic plugin-count tagline at line-height 2.3. Filter tabs use **`is-style-button-list`** for business model (All / Community / Commercial), not Photos' four filter dropdowns. Plugin cards use **`is-style-cards-grid`** on **`surface-dim`** with icon + rating + excerpt + meta footer — not Documentation's bordered white topic cards. Star ratings use **`plugins-star-rating`** (`#FFB900`), not Blueberry or campaign lemon tints. Homepage sidebar uses **classic widgets** in `#secondary`, not block patterns.
