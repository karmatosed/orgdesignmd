# Support Forums

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://wordpress.org/support/forums/](https://wordpress.org/support/forums/)

**Theme:** `pub/wporg-support-2024` + bbPress

**Implementation:** Classic PHP child theme of wporg-parent-2021 wrapping bbPress.

---

## Support Forums typography (YAML + prose)

[wordpress.org/support/forums](https://wordpress.org/support/forums/) runs on **`pub/wporg-support-2024`** ([wordpress.org repo](https://github.com/WordPress/wordpress.org/tree/trunk/wordpress.org/public_html/wp-content/themes/pub/wporg-support-2024)) — a classic PHP child theme of wporg-parent-2021 wrapping **bbPress**. Typography closely matches Documentation: Inter for UI and table chrome; EB Garamond for the hero and forum titles.

| Token | Font | Role |
|:------|:-----|:-----|
| `forums-hero-title` | EB Garamond | Archive H1 "Forums" — 50px white on `charcoal-2` (front `/support/` uses "Support") |
| `forums-section-heading` | Inter 600 | Section H2s — "Forums", "Topics", "More resources" (20px `heading-5`) |
| `forums-forum-card-title` | Inter 600 | Forum names in homepage `is-style-cards-grid` (16px) |
| `forums-forum-title` | EB Garamond | Single-forum H1 + topic lead title (36px `heading-1` in child `theme.json`) |
| `forums-topic-table-header` | Inter | bbPress table headers — Topic / Participants / Replies / Last Post (14px `small`) |

In-article headings inside topic/reply content inherit Inter 600 from child `theme.json` element overrides (same scale as Documentation). bbPress meta lines (started-by, freshness, @handles) render at 14px or 0.8rem in `charcoal-3`/`charcoal-4`.

## Support Forums layout (prose)

Templates and patterns in [pub/wporg-support-2024](https://github.com/WordPress/wordpress.org/tree/trunk/wordpress.org/public_html/wp-content/themes/pub/wporg-support-2024):

| Template / class | Background | Layout |
|:-----------------|:-----------|:-------|
| `header.php` hero | `charcoal-2` | Sticky local nav (`menuSlug: forums`); EB Garamond H1 + tagline; `wporg/language-suggest`; `search-field` pattern |
| `welcome-cards` pattern | white | 3-up grid — Welcome / Documentation / Get Involved intro cards |
| `loop-forums-homepage` | white | 10 core forums in `is-style-cards-grid` via `wp-block-wporg-link-wrapper`; full-width "Themes & Plugins" span row |
| `forums-views` pattern | white | 3-up topic filter cards — All topics, No replies, Unresolved |
| `forums-homepage-footer` | `charcoal-2` | "More resources" — 2×50% columns with `blueberry-2` link headings (Documentation, Learn, etc.) |
| Single forum (`bbp-topics`) | white | Bordered table: header row + paginated topic list; create-topic + search row above |
| Single topic | white | Lead topic (`forums-light-grey-3`) → reply list separated by 1px borders; admin links pinned bottom-right |

Topic table columns at ≥321px: 60% title, 12% participants, 8% replies, 20% last post (right-aligned freshness). Pagination uses bordered page-number chips; hover/active states use Blueberry. Plugin/theme review forums reuse the same shell with bbPress view templates.

Author role badges (`author-badge-*`) pin to the top-left of posts with 2px radius: moderator (`primary`), thread starter (`acid-green-2` + dark text), plugin author (`pomegrade-1`), theme author (`purple-2` / vivid-purple), reporter (`vivid-red` border on whole post). Resolved topics show a `forums-resolved` green pill with Dashicons checkmark.

bbPress template notices map to tint components: default/success → `acid-green-3`, info → `blueberry-4`, error → `pomegrade-3`, warning → `lemon-3`.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Create topic CTA |
| `forums-author-badge-moderator` | Moderator pill |
| `forums-author-badge-plugin` | Plugin author pill |
| `forums-author-badge-thread-starter` | OP pill |
| `forums-forum-card` | Homepage forum grid |
| `forums-hero` | Archive title band |
| `forums-more-resources` | Homepage footer band |
| `forums-notice-error` | bbPress error notice |
| `forums-notice-info` | bbPress info notice |
| `forums-notice-success` | bbPress success notice |
| `forums-notice-warning` | bbPress warning notice |
| `forums-reply-post` | Topic/reply content |
| `forums-resolved-indicator` | Resolved topic badge |
| `forums-topic-lead` | Lead post wash |
| `forums-topic-row` | bbPress topic table row |
| `input-search` | Forums hero search |
| `site-header / site-footer` | All sections |


### Component prose

**Support Forums components (prose):**

- **`forums-hero`:** Charcoal-2 band with EB Garamond H1 (50px) and white tagline. Matches Documentation hero structure; archive title reads "Forums", root `/support/` reads "Support". Followed by language-suggest + search field pattern.
- **`forums-forum-card`:** Homepage forum cells in `is-style-cards-grid` — same 1px border / 2px radius / hover treatment as Documentation topic cards. Wrapped in `wp-block-wporg-link-wrapper` with Inter 600 title + 14px description.
- **`forums-topic-row`:** Rows in `.bbp-topics` table — white background, 1px top border (`light-grey-1`). Sticky rows override to `lemon-3`. Title links suppress underline until hover.
- **`forums-topic-lead`:** Original post in a thread — `forums-light-grey-3` (`#FBFBFB`) wash, 80px circular avatar, optional author badge offset.
- **`forums-reply-post`:** Subsequent replies — white background, 50px avatar, 20px padding, code/pre blocks on `light-grey-2` with 1px border.
- **`forums-author-badge-*`:** Role pills from `theme.json` custom colors — moderator (`primary`), thread starter (`acid-green-2`), plugin author (`pomegrade-1`). Reporter uses a 2px red border on the whole post, not a fill badge.
- **`forums-notice-*`:** bbPress `div.bbp-template-notice` variants — map success/default to `acid-green-3`, info to `blueberry-4`, error to `pomegrade-3`, warning to `lemon-3`.
- **`forums-resolved-indicator`:** Green `#00D084` pill with white checkmark Dashicon on resolved plugin/theme topics.
- **`forums-more-resources`:** Charcoal-2 homepage footer — "More resources" with `blueberry-2` link headings linking to Documentation, Learn, and contributor handbook.


## Do's and Don'ts


- On Support Forums, use bbPress table layout for topic lists — not card grids. Role badges use theme.json semantic colors (`primary`, `acid-green-2`, `pomegrade-1`); lead posts sit on `forums-light-grey-3`. Map bbPress notices to tint components, not solid primary fills.
