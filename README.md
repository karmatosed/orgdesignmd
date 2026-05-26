# orgdesignmd

A [DESIGN.md](https://github.com/google-labs-code/design.md) design system for [WordPress.org](https://wordpress.org/), derived from the live site and its open source themes.

## What this is

[DESIGN.md](DESIGN.md) is Google's format for giving coding agents a persistent, structured understanding of a visual identity. Each file has two layers:

1. **YAML front matter** — machine-readable design tokens (colors, typography, spacing, components)
2. **Markdown body** — human-readable rationale in a fixed section order

This repo captures WordPress.org's shared design language so agents can build UI that matches the real site without guessing from screenshots.

### How the docs are split

| File | Role | Spec-compliant? |
|:-----|:-----|:----------------|
| [`DESIGN.md`](DESIGN.md) | **Canonical** — all YAML tokens and global prose | Yes — lint/export target |
| [`stacks/`](stacks/README.md) | **Supplementary** — per-section typography, layout, components, Do's | No — plain markdown add-ons |

Load **`DESIGN.md` only** for the full system, or **`DESIGN.md` + one section file** (e.g. `stacks/showcase.md`) when working on a single property. Section files do not inherit tokens automatically — they reference `DESIGN.md` by convention.

**Agents:** operational guide in [`AGENTS.md`](AGENTS.md). **Contributors:** editing tokens and sections in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Demo

A visual sample lives in [`demo/demo.html`](demo/demo.html). Open that file in a browser to preview the design system palette and typography.

## What we did

### 1. Researched the live site across sections

WordPress.org is a **federated visual brand** — several implementation stacks, not one child-theme tree. Most properties use [wporg-parent-2021](https://github.com/WordPress/wporg-parent-2021); About/Blocks/Enterprise use [wporg-main-2022](https://github.com/WordPress/wporg-main-2022) patterns; Profiles (BuddyPress) and Jobs (`jobswp`) are outliers. We audited:

| Section | URL | Theme source |
|:--------|:----|:-------------|
| Main | [wordpress.org](https://wordpress.org/) | [wporg-main-2022](https://github.com/WordPress/wporg-main-2022) |
| News | [wordpress.org/news](https://wordpress.org/news/) | [wporg-news-2021](https://github.com/WordPress/wporg-news-2021) |
| Showcase | [wordpress.org/showcase](https://wordpress.org/showcase/) | [wporg-showcase-2022](https://github.com/WordPress/wporg-showcase-2022) |
| Plugins | [wordpress.org/plugins](https://wordpress.org/plugins/) | [pub/wporg-plugins-2024](https://github.com/WordPress/wordpress.org/tree/trunk/wordpress.org/public_html/wp-content/themes/pub/wporg-plugins-2024) + **plugin-directory** plugin |
| Themes | [wordpress.org/themes](https://wordpress.org/themes/) | [pub/wporg-themes-2024](https://github.com/WordPress/wordpress.org/tree/trunk/wordpress.org/public_html/wp-content/themes/pub/wporg-themes-2024) (sibling to Plugins) |
| About | [wordpress.org/about](https://wordpress.org/about/) | wporg-main-2022 |
| Enterprise | [wordpress.org/enterprise](https://wordpress.org/enterprise/) | [wporg-main-2022](https://github.com/WordPress/wporg-main-2022) (`enterprise.php` pattern) |
| Five for the Future | [wordpress.org/five-for-the-future](https://wordpress.org/five-for-the-future/) | [wporg-5ftf-2024](https://github.com/WordPress/five-for-the-future) + **wporg-5ftf** plugin |
| Events | [events.wordpress.org](https://events.wordpress.org/) | [wporg-events-2023](https://github.com/WordPress/wordcamp.org/tree/production/public_html/wp-content/themes/wporg-events-2023) in [WordCamp.org](https://github.com/WordPress/wordcamp.org) |
| Make | [make.wordpress.org](https://make.wordpress.org/) | [wporg-make-2024](https://github.com/WordPress/wporg-make) |
| Blocks | [wordpress.org/blocks](https://wordpress.org/blocks/) | [wporg-main-2022](https://github.com/WordPress/wporg-main-2022) (`blocks.php` pattern) |
| Patterns | [wordpress.org/patterns](https://wordpress.org/patterns/) | [wporg-pattern-directory-2024](https://github.com/WordPress/pattern-directory) |
| Photos | [wordpress.org/photos](https://wordpress.org/photos/) | [wporg-photos-2024](https://github.com/WordPress/wporg-photo-directory) |
| Learn | [learn.wordpress.org](https://learn.wordpress.org/) | `pub/wporg-learn-2024` + Sensei LMS |
| Documentation | [wordpress.org/documentation](https://wordpress.org/documentation/) | [wporg-documentation-2022](https://github.com/WordPress/wporg-documentation-2022) |
| Support Forums | [wordpress.org/support/forums](https://wordpress.org/support/forums/) | [pub/wporg-support-2024](https://github.com/WordPress/wordpress.org/tree/trunk/wordpress.org/public_html/wp-content/themes/pub/wporg-support-2024) + bbPress |
| Developer | [developer.wordpress.org](https://developer.wordpress.org/) | [wporg-developer-2023](https://github.com/WordPress/wporg-developer) |
| Profiles | [profiles.wordpress.org](https://profiles.wordpress.org/) | BuddyPress + legacy `profiles.wordpress.org` child theme (Template: `bp-default`) + shared global header |
| Jobs | [jobs.wordpress.net](https://jobs.wordpress.net/) | Standalone `jobswp` v2.0.0 classic theme + **jobswp** plugin ([WordPress/wordpress.org](https://github.com/WordPress/wordpress.org)) |

### 2. Extracted tokens from source

Primary source: [wporg-parent-2021/theme.json](https://github.com/WordPress/wporg-parent-2021/blob/trunk/source/wp-content/themes/wporg-parent-2021/theme.json) — the shared parent used across most properties. Values were verified against live CSS custom properties on wordpress.org.

Profiles is a **separate property** from the block-theme stack. It runs on **BuddyPress** with the legacy child theme at `wp-content/themes/profiles.wordpress.org/` (forked from `bp-default`, not wporg-parent-2021). The global header/footer comes from the same `pub-sync` mu-plugins as the main site, but profile content, activity streams, and badges are rendered by BuddyPress templates and theme CSS. We audited live profile pages for patterns that differ from the marketing site — hero layout, impact stats, team chips, sponsorship pills, contribution medals, and tabbed sections (Activity, Plugins, Photos, Courses) — not any single contributor's data.

Key findings:

- **Colors:** Charcoal neutrals + Blueberry (`#3858E9`) primary, with Pomegrade, Acid Green, Lemon, and Purple accent families for campaign blocks
- **Typography:** EB Garamond (headlines), Inter (body/UI), IBM Plex Mono (code)
- **Shapes:** 2px button radius — a distinctive WordPress.org brand marker
- **Layout:** 680px content / 1160px wide columns

About-specific findings (from [about.php](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/about.php) pattern + live CSS):

- **Surface:** Warm parchment `#F0EDE7` (`about-surface`) across every section — not white
- **Typography:** Inter for display headings (not EB Garamond); Courier Prime for all body copy, labels, and link columns
- **Voice:** Deliberately lowercase editorial — "democratize publishing" cover, GPL freedoms numbered 0–3
- **Layout:** 40/60 two-column grid (heading left, body right); three-column link footer (technology, details, people)
- **Decorative:** Hand-drawn SVG underlines on section headings (`charcoal-1` ink strokes via `:after` pseudo-elements)
- **Template:** `page-about.html` in wporg-main-2022; section classes prefixed `wporg-about-section-*`

Blocks-specific findings (from [blocks.php](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/blocks.php) pattern + live CSS):

- **Stack:** wporg-main-2022 block pattern in `page-blocks.html` — same parent as About, not a child theme
- **Surface:** Stacked dark bands (`charcoal-2` hero, `charcoal-1` prose sections); `light-grey-2` release promo; white footer link list
- **Typography:** Inter throughout — 70px hero H1 (not EB Garamond); `heading-3` (29px) for split-layout section titles
- **Block grid:** Unique 4×2 icon grid with dark divider lines (`blocks-grid-border-*`); 24px block icons + 12px labels
- **Editor mockup:** Stacked `charcoal-3` code block + `light-grey-2` preview pane (5px radius) in "Create your own"
- **CTAs:** `is-style-outline-on-dark` on dark bands; primary fill for Showcase and release buttons

Enterprise-specific findings (from [enterprise.php](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/enterprise.php) pattern + live CSS):

- **Stack:** wporg-main-2022 block pattern in `page-enterprise.html` — same parent as About and Blocks; global header/footer blocks
- **Surface:** Solid `primary` cover band; `charcoal-2` logo marquee; white use-case and feature sections; `light-grey-2` download CTA footer band
- **Typography:** EB Garamond 120px cover H1 (`heading-cta` preset); Inter 600 use-case H3s; EB Garamond `heading-4` feature H2s; Inter 300 98px "Get WordPress" linked display (`is-style-with-arrow`, 52px mobile)
- **Logo band:** 10 enterprise brand WebP logos in a centered flex row; mobile 2-column grid with 20px max logo height
- **Features:** 3-column band with 1px `light-grey-1` vertical dividers and PNG icons; stacks on mobile
- **Resources:** Two 3-column PDF/Vimeo link grids under the download CTA

Patterns-specific findings (from [wporg-pattern-directory-2024](https://github.com/WordPress/pattern-directory) `theme.json`, patterns, and live CSS):

- **Stack:** wporg-parent-2021 FSE child theme in the [pattern-directory](https://github.com/WordPress/pattern-directory) repo; custom blocks (`wporg/pattern-thumbnail`, `wporg/pattern-preview`, `wporg/query-filter`, `wporg/favorite-button`)
- **Surface:** White grid body; `charcoal-2` hero + sticky local nav; `charcoal-1` global footer
- **Typography:** EB Garamond 50px hero; Inter for grid titles (14px), single-pattern H1 (`heading-3`), and section headings
- **Grid:** 3-column thumbnail layout with category button-list, search, curation/sort filters, and centered pagination
- **Thumbnails:** 4:3 aspect ratio, `light-grey-2` fill, 4px radius, Blueberry linked titles, small favorite buttons
- **Single pattern:** iframe preview with responsive `light-grey-2` frame (4px–20px), copy button, author row, category tags, related 3-up grid

Photos-specific findings (from [wporg-photos-2024](https://github.com/WordPress/wporg-photo-directory) `theme.json`, patterns, and live CSS):

- **Stack:** wporg-parent-2021 FSE child theme in the [wporg-photo-directory](https://github.com/WordPress/wporg-photo-directory) repo; custom blocks (`wporg/meta-list`, `wporg/photo-attribution`, shared `wporg/query-filter`, `wporg/favorite-button`)
- **Surface:** White grid body; `charcoal-2` hero + sticky local nav; `charcoal-1` global footer
- **Typography:** EB Garamond 50px site-title hero + single-photo post titles; Inter 600 for detail section headings (`heading-6`); Inter for query total and author links
- **Grid:** 4-column bordered thumbnail layout (responsive 4→3→2) with search, four filter dropdowns (category, color, orientation, sort), and centered pagination — no titles under grid cells
- **Thumbnails:** 16:9 aspect ratio, 1px `black-opacity-15` border, 2px radius — image-only cells via `post-featured-image`
- **Single photo:** Author row + favorite + Blueberry download menu → featured image → alt text + Image info/EXIF meta → attribution tabs → CC0 license copy → "Discover more" CTA
- **Wide layout:** Child `theme.json` sets `wideSize` to **1760px** (wider than parent 1160px)

Showcase-specific findings (from [wporg-showcase-2022](https://github.com/WordPress/wporg-showcase-2022) `theme.json`, patterns, and live CSS):

- **Stack:** wporg-parent-2021 FSE child theme; custom blocks (`wporg/site-screenshot`, `wporg/site-meta-list`); shared `wporg/query-total`, `wporg/query-filter`, `wporg/local-navigation-bar`
- **Surface:** White grid body; **`charcoal-1`** global header, local nav, and homepage hero — not `charcoal-2` like Plugins/Patterns; `charcoal-1` two-column page footer; per-site **`has-feature-color-background`** brand color on single-site heroes
- **Typography:** EB Garamond `heading-2` hero + single-site titles; Inter `normal` for grid post titles; Inter 300 `heading-cta` (120px) "View all sites" link with arrow
- **Layout:** **1760px** wide (`showcase-wide-max`, same as Photos); 3-column featured grid (3→2 @≤1600px, 1 @≤800px); dot-pattern hero with rotating featured site meta table
- **Screenshots:** Custom frame block — 10px `rgba(30,30,30,0.1)` border, 20px radius, mshots via Interactivity API; desktop 535:300, mobile 375:600 aspect ratios
- **Filters:** Search + `wporg/query-total` count + category dropdown — not Plugins' business-model button-list
- **Depth:** Border frames only — no card box-shadow (documented in Elevation section)

News-specific findings (from [wporg-news-2021](https://github.com/WordPress/wporg-news-2021) `theme.json`, front-page template parts, and live CSS):

- **Surface:** Blue hero `#3E58E1` (`news-blue`) on front page — not the off-white body default; white latest-posts band; `#F8F3EC` people grid
- **Typography:** EB Garamond hero (80–160px "News" title) + section headings; Inter 200-weight release version numerals; Inter 14px meta
- **Layout:** Repeating sidebar + content split (390px meta column); three front-page query sections + 2×2 bottom banner
- **Components:** Custom `wporg/release-version` block; brush-stroke SVG accents on "See All" links; square people tiles with grayscale→blue hover
- **Editorial:** Pullquotes 50px serif; blockquotes 30px with 2px `deep-blueberry` left border; body line-height 1.9
- **Template:** `front-page.html` with `body.news-front-page`; section classes `front__latest-release`, `front__latest-posts`, `front__people-of-wordpress`

Learn-specific findings (from `pub/wporg-learn-2024` theme.json, live CSS, and Sensei LMS):

- **Stack:** wporg-parent-2021 child theme + Sensei LMS for courses/lessons/quizzes; custom blocks under `wp-block-wporg-learn-*`
- **Surface:** Charcoal-2 hero and training CTA; white card grids; pathway-specific pastel tints (`learn-pathway-user`, `-developer`, `-designer`)
- **Typography:** Inter-first — Inter 600 for section and card headings; EB Garamond only for promotional display headings ("Share your WordPress expertise")
- **Success green:** Dedicated `learn-success-50/60/70` (`#008A20` → `#005C12`) for progress bars, complete-lesson, and quiz submit — separate from campaign acid-green accents
- **Cards:** 2px-radius white cards with stacked-paper pseudo-layers; 16:9 course thumbnails; duration + lesson-count icon rows
- **Layout:** Homepage sections — hero → pathway cards → featured courses → featured lessons → workshops → training CTA → resources → footer signup; Sensei pages use sidebar + progress header

Documentation-specific findings (from [wporg-documentation-2022](https://github.com/WordPress/wporg-documentation-2022) `theme.json`, patterns, and live CSS):

- **Stack:** wporg-parent-2021 child theme (formerly HelpHub / wordpress.org/support); custom `wporg/article-list` block
- **Surface:** White body; `charcoal-2` hero band and "Get more help" footer; `blueberry-4` language-suggest bar — no campaign accents
- **Typography:** Inter 600 for section headings and in-article H2–H4; EB Garamond for page/article titles (36px) and front-page hero (50px); narrowed heading scale (38px → 18px)
- **Cards:** Parent-theme `is-style-cards-grid` — 3-up topic cards with 1px `light-grey-1` border, 2px radius, hover to `light-grey-2`
- **Articles:** `.has-three-columns` layout with 248px floating table-of-contents sidebar; light grey code blocks (not dark marketing style)
- **Layout:** Front page stacks four topic sections (overview, technical guides, support guides, customization); topic landing pages use `wporg/article-list` grouped by subcategory

Support Forums-specific findings (from `pub/wporg-support-2024` theme.json, bbPress templates, and live CSS):

- **Stack:** wporg-parent-2021 child theme + **bbPress** (classic PHP theme, not FSE); Blocks Everywhere for Gutenberg in replies
- **Surface:** White body; `charcoal-2` hero + "More resources" footer; lead topic wash `#FBFBFB` (`forums-light-grey-3`); sticky topics on `lemon-3`
- **Typography:** Inter 600 for section headings and bbPress table chrome; EB Garamond for hero (50px) and forum titles (36px)
- **Homepage:** Welcome cards → 10 forum cards in `is-style-cards-grid` → Themes & Plugins callout → topic view filters → charcoal footer
- **Topic lists:** bbPress table — Topic / Participants / Replies / Last Post; Blueberry pagination hover
- **Posts:** Circular avatars (80px lead, 50px reply); role badges (moderator, OP, plugin author); resolved indicator `#00D084`
- **Notices:** bbPress template notices use campaign tints — `blueberry-4`, `acid-green-3`, `pomegrade-3`, `lemon-3`

Developer-specific findings (from [wporg-developer-2023](https://github.com/WordPress/wporg-developer) `theme.json`, patterns, and live CSS):

- **Stack:** wporg-parent-2021 FSE child theme; custom blocks (`wporg/code-reference-title`, `wporg/latest-news`, `wporg/reference-new-updated`)
- **Surface:** White body; `charcoal-2` hero + footer; `lemon-3` API version notice (not Documentation's language-suggest); `dev-linen` handbook wash
- **Typography:** Inter 600 for section and in-article headings; EB Garamond for hero (50px) and Developer Blog card titles; IBM Plex Mono for code reference H1s (24px)
- **Syntax colors:** `dev-syntax-*` tokens for API type badges — functions green, hooks red, classes yellow, methods blue
- **Homepage:** Documentation 3-col cards → API Reference 2-col cards → Developer Blog `wporg/latest-news` → Get Involved 2-col → charcoal footer
- **Code reference:** Plex Mono titles, copy-toolbar code blocks, floating TOC sidebar (same pattern as Documentation)

Profiles-specific findings (unique to the BuddyPress legacy theme):

- **Stack:** BuddyPress activity/notifications + legacy theme CSS; not block patterns or `theme.json`
- **Typography:** Inter for profile headings (not EB Garamond); serif only on impact stat numbers (52px)
- **Components:** Team chips, sponsor pill, impact tiles (30/90/365 days), activity feed, per-team contribution medals
- **Shapes:** 8px cards and pill chips; global header buttons still 2px
- **Tokens:** Local `--c-*` aliases in `style.css` map to the shared Blueberry/Charcoal palette

Jobs-specific findings (from `jobswp` theme `style.css`, live site, and [2026 redesign PR #575](https://github.com/WordPress/wordpress.org/pull/575)):

- **Stack:** Standalone classic PHP theme (`jobswp` v2.0.0, Underscores-based) + **jobswp** plugin — not wporg-parent-2021, not shared global header/footer blocks
- **Surface:** White sticky header; `light-grey-2` hero + candidates band; white job grid; `charcoal-1` custom four-column footer
- **Typography:** EB Garamond 70px hero + card titles; Inter for nav, labels, meta, and forms; body line-height 1.875
- **Accent:** **Acid green** — `acid-green-1` active filter pills, `acid-green-2` hero keyword highlight, `acid-green-3` category/Open-to-Work badges
- **Grid:** 3-column job cards (→2 @900px, →1 @600px) with category filter pills; 2-column candidate cards linking to profiles.wordpress.org
- **Single job:** Breadcrumb + 2-column layout (prose + 340px sticky sidebar with Job Details)
- **Forms:** Post a Job, FAQ, Feedback, Remove a Job at 680px content width

Five for the Future-specific findings (from [wporg-5ftf-2024](https://github.com/WordPress/five-for-the-future) `theme.json`, patterns, and live CSS):

- **Stack:** wporg-parent-2021 FSE child theme in the [five-for-the-future](https://github.com/WordPress/five-for-the-future) repo + **wporg-5ftf** plugin for pledges CPT; refreshed September 2024
- **Surface:** `charcoal-1` global header and local nav (not `charcoal-2` like Patterns/Photos); WordCamp photo cover; `light-grey-2` benefit grid; `primary` CTA band; `charcoal-1` testimonials footer
- **Typography:** EB Garamond 50px site title in nav; Inter 600 benefit headings at `normal` size; EB Garamond `heading-2` on CTA band; narrowed heading scale in child `theme.json`
- **Layout:** Editor-managed block content on front page — TL;DR hero section, 2×2 benefit columns, WordCamp Asia image row, links-list CTAs, 3-up testimonial grid
- **Testimonials:** 100px rounded avatars with `wp-duotone-grayscale`; sponsor links to pledge pages; "See all testimonials" in `blueberry-2`
- **Pledges:** Custom post type `5ftf_pledge` archive at `/pledges/` with dedicated list styling in theme SCSS

Events-specific findings (from [wporg-events-2023](https://github.com/WordPress/wordcamp.org/tree/production/public_html/wp-content/themes/wporg-events-2023) patterns, `style.css`, and live CSS):

- **Stack:** wporg-parent-2021 FSE child theme in the [WordCamp.org](https://github.com/WordPress/wordcamp.org) repo; custom blocks (`wporg/google-map`, `wporg/event-list`, shared `wporg/query-filter`)
- **Surface:** White global header + white sticky local nav — not `charcoal-2` directory hero bands; `charcoal-0` hero text on white; `#AADAFF` map wash (`events-map-sky`)
- **Typography:** EB Garamond `heading-2` cover H1 with block-level italic emphasis; Inter 700 section headings; EB Garamond `heading-6` stat tiles
- **Layout:** 1600px wide (`events-wide-max`); 50/50 cover (33/67 at ≥1440px) with embedded Google Map; bordered 3-up stat row; filter row + event list + contributors gallery footer
- **Filters:** Search + four single-select dropdowns (Format, Type, Month, Country) — not Patterns' category button-list
- **List:** `wporg/event-list` rows reuse `.wporg-marker-list-item` bordered stack styling (title / location / date-time grid at desktop)

Make-specific findings (from [wporg-make-2024](https://github.com/WordPress/wporg-make) patterns, `theme.json`, and live CSS):

- **Stack:** wporg-parent-2021 FSE child theme in [wporg-make](https://github.com/WordPress/wporg-make); custom `wporg-make/meeting-time` block; wporg-glossary plugin for team blurb hovercards
- **Surface:** `charcoal-2` global header, local nav, and hero band; white team directory body; `primary` Five for the Future CTA footer
- **Typography:** EB Garamond 50px hero H1; Inter 600 for section headings and Blueberry team titles (`heading-6`); EB Garamond `heading-1` for wizard prompt and CTA
- **Layout:** 1160px content width; hero 50/50 intro + community photo; team list as 19% / flex / 36% three-column rows with bottom borders
- **Teams:** `make_site` custom post type queried on front page; each row links to team blog (e.g. `/core/`, `/design/`)
- **Meetings:** `wporg-make/meeting-time` shows next meeting, relative time, and Slack channel when scheduled
- **CTA:** Shared 5FTF pattern — `blueberry-1` band with `is-style-links-list` organization/individual links

Plugins-specific findings (from **`pub/wporg-plugins-2024`** patterns, `theme.json`, plugin-directory blocks, and live CSS):

- **Stack:** wporg-parent-2021 FSE child theme in [WordPress/wordpress.org](https://github.com/WordPress/wordpress.org) + **plugin-directory** plugin (`wporg/front-page`, `wporg/query-total`); custom theme `plugin-card` block; local dev via `npm run plugins:env start` in wordpress.org repo
- **Surface:** White body; `charcoal-2` hero + sticky local nav; `light-grey-2` (`#F6F6F6`) plugin cards; classic `#secondary` sidebar widgets — not block patterns
- **Typography:** EB Garamond 50px hero H1; Inter 600 for section headings and linked card titles; Inter `small` for author/installs/tested-with meta row
- **Layout:** 960px content / 1160px wide (child `theme.json`); filter row with search + business-model button-list (All / Community / Commercial); curated sections (Featured, Beta, Popular, Block-Enabled) with "See all" links
- **Cards:** `is-style-cards-grid` equal-height rows — icon thumbnail (128/256px from `ps.w.org`) + star rating + excerpt + footer meta with SVG icons
- **Ratings:** `wporg-ratings` Dashicons at `#FFB900` (`plugins-star-rating`) — WordPress admin star yellow
- **Locale:** `wporg/language-suggest` bar with `/plugins/v2/locale-banner` REST endpoint (same pattern as Documentation)
- **Sibling:** [Themes directory](https://wordpress.org/themes/) uses `pub/wporg-themes-2024` with the same hero and card patterns

### 3. Captured the full token set

The YAML block in `DESIGN.md` now includes:

- **wporg-parent-2021** — full Charcoal, Blueberry, and campaign accent palettes (85 colors total)
- **Profiles/BuddyPress** — `profiles-*` semantic tokens from `:root` in `profiles.wordpress.org/style.css`
- **Contribution badges** — all 31 unique `badge-*` colors mapped from `.badge-*` CSS classes (64 class variants including `-contributor`, `-reviewer`, `-team` aliases)
- **Typography** — wporg headline scale, About-specific tokens, Blocks tokens, Enterprise tokens, Five for the Future tokens, Events tokens, Make tokens, Plugins tokens (`plugins-hero-title`, `plugins-card-title`, etc.), Showcase tokens (`showcase-hero-title`, `showcase-card-title`, etc.), Patterns tokens, Photos tokens, Jobs tokens, News-specific tokens, Learn tokens, Documentation tokens, Support Forums tokens, Developer tokens, plus Profiles-specific tokens
- **Components** — shared wporg UI, About/Blocks/Enterprise/Five for the Future/Events/Make/Plugins/Showcase/Patterns/Photos/Jobs page patterns, News front-page patterns, Learn patterns, Documentation patterns, Support Forums patterns, Developer patterns, plus BuddyPress patterns

RGBA washes (`--c-blue-wash`, badge `--tint-color` overlays) remain documented in prose — the DESIGN.md linter accepts hex only.

### 4. Mapped sections to components

The Components prose includes a cross-section table showing which UI patterns apply where (e.g. `card-showcase` is Showcase-only; `impact-tile` is Profiles-only).

## Sections at a glance

What each WordPress.org property looks like in design terms:

| Section | Voice | Distinctive UI |
|:--------|:------|:---------------|
| **Main** | EB Garamond display, campaign accent blocks | Logo marquee, download counter, 120px hero |
| **News** | EB Garamond hero + Inter meta, editorial serif | Blue hero band, giant release numeral, sidebar+feed layout, people photo grid, brush-stroke links |
| **Showcase** | EB Garamond hero + single titles, Inter grid UI | Charcoal-1 hero/nav, 1760px wide, 20px screenshot borders, dot-pattern hero, brand-color singles |
| **Plugins** | EB Garamond hero, Inter card UI | Charcoal-2 hero, business-model filter tabs, icon + rating + meta plugin cards, classic sidebar widgets |
| **Themes** | Same as Plugins (sibling directory) | Shared card grid and filter patterns via `pub/wporg-themes-2024` |
| **About** | Inter display + Courier Prime body, lowercase editorial | Warm `#F0EDE7` surface, 40/60 column grid, GPL freedom rows, SVG heading underlines |
| **Enterprise** | EB Garamond 120px cover, Inter CTA display | Blueberry cover, charcoal logo marquee, 3-column feature dividers, PDF link footer |
| **Five for the Future** | EB Garamond nav title, Inter benefit headings | Charcoal-1 nav, WordCamp cover, light-grey benefit grid, links-list CTA, grayscale testimonial avatars |
| **Events** | EB Garamond hero + stat tiles, Inter filters/list | Light white header, sky-blue map, bordered event rows, contributor gallery |
| **Make** | EB Garamond 50px hero, Inter team titles | Charcoal-2 hero, three-column team directory, meeting times, 5FTF CTA band |
| **Blocks** | Inter display (70px hero), dark stacked sections | Charcoal hero, 4×2 block icon grid, editor mockup, outline-on-dark CTAs |
| **Patterns** | EB Garamond hero, Inter grid UI | 3-column thumbnail grid, iframe preview frame, category filters, favorites |
| **Photos** | EB Garamond hero + single titles, Inter grid UI | 4-column bordered 16:9 grid, four filter dropdowns, download menu, attribution tabs |
| **Learn** | Inter-first course UI, pathway tints | Pathway cards, stacked-paper course cards, Sensei progress green |
| **Documentation** | Inter utility headings, EB Garamond titles | Charcoal hero, 3-up topic card grid, floating TOC sidebar, light code blocks |
| **Support Forums** | Inter table UI, EB Garamond hero/titles | bbPress topic table, forum card grid, role badges, resolved indicator |
| **Developer** | Inter utility headings, Plex Mono API titles | Charcoal hero, `lemon-3` version notice, handbook card grids, syntax type colors, Developer Blog cards |
| **Profiles** | Inter UI, data-dense (BuddyPress legacy) | Hero grid, impact stats, team chips, contribution medals, activity feed |
| **Jobs** | EB Garamond hero + card titles, Inter UI | 3-column job grid, acid-green filter pills, Open to Work candidates, sticky job sidebar |

## DESIGN.md sections

The markdown body follows the [DESIGN.md spec section order](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md):

| # | Section | What's documented |
|:--|:--------|:-----------------|
| 1 | Overview | Editorial Open Source personality; federated stack architecture |
| 2 | Colors | Full YAML palette + BuddyPress badge class map + section application table |
| 3 | Typography | wporg + stack token group index (detail in `stacks/`) |
| 4 | Layout | 680/1160px grid + layout pattern index → stack guides |
| 5 | Elevation & Depth | Tonal layers, no card shadows, showcase border frames |
| 6 | Shapes | 2px button radius, 8px profile cards, pill chips |
| 7 | Components | Shared UI in YAML; per-section component tables in `stacks/` |
| 8 | Do's and Don'ts | Global guardrails; section-specific rules in `stacks/` |

## Section guides

| Section | File |
|:--------|:-----|
| Main | [stacks/main.md](stacks/main.md) |
| News | [stacks/news.md](stacks/news.md) |
| Showcase | [stacks/showcase.md](stacks/showcase.md) |
| Plugins | [stacks/plugins.md](stacks/plugins.md) |
| Themes | [stacks/themes.md](stacks/themes.md) |
| About | [stacks/about.md](stacks/about.md) |
| Blocks | [stacks/blocks.md](stacks/blocks.md) |
| Enterprise | [stacks/enterprise.md](stacks/enterprise.md) |
| Patterns | [stacks/patterns.md](stacks/patterns.md) |
| Photos | [stacks/photos.md](stacks/photos.md) |
| Learn | [stacks/learn.md](stacks/learn.md) |
| Documentation | [stacks/documentation.md](stacks/documentation.md) |
| Support Forums | [stacks/forums.md](stacks/forums.md) |
| Developer | [stacks/developer.md](stacks/developer.md) |
| Five for the Future | [stacks/five-for-the-future.md](stacks/five-for-the-future.md) |
| Events | [stacks/events.md](stacks/events.md) |
| Make | [stacks/make.md](stacks/make.md) |
| Profiles | [stacks/profiles.md](stacks/profiles.md) |
| Jobs | [stacks/jobs.md](stacks/jobs.md) |

See [stacks/README.md](stacks/README.md) for usage.

## Tooling

Uses [@google/design.md](https://www.npmjs.com/package/@google/design.md) to validate and export tokens.

```bash
npm install

# Validate DESIGN.md against the spec
npm run design:lint

# Export tokens for implementation
npm run design:export:tailwind   # → theme.css (Tailwind v4 @theme)
npm run design:export:dtcg       # → tokens.json (W3C format)
```

## Files

```
DESIGN.md              Canonical tokens + global prose (lint/export)
stacks/                Per-section supplementary guides (not DESIGN.md format)
  README.md            Section index and usage
  main.md, news.md, …  One file per WordPress.org property
package.json           Lint and export scripts
README.md              This file
AGENTS.md              Agent operational guide
CONTRIBUTING.md        How to edit DESIGN.md and stack files
license.txt            GPLv2 or later (same as WordPress)
demo/                  Visual sample (`demo.html`)
```

## License

This project is free software, released under the [GNU General Public License v2 (or later)](license.txt) — the same license as [WordPress](https://wordpress.org/about/license/).

## References

- [DESIGN.md format spec](https://github.com/google-labs-code/design.md)
- [wporg-parent-2021](https://github.com/WordPress/wporg-parent-2021) — shared parent theme
- [Advancing the WordPress Design System](https://make.wordpress.org/design/2024/09/05/advancing-the-wordpress-design-system/) — ongoing consolidation effort
