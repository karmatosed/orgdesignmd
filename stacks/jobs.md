# Jobs

**Inherits:** Color values mirror wporg palette in CSS custom properties — see [`DESIGN.md`](../DESIGN.md). Global wporg header/footer **do not apply**.

**URL:** [https://jobs.wordpress.net/](https://jobs.wordpress.net/)

**Theme:** Standalone `jobswp` v2.0.0 + **jobswp** plugin

**Implementation:** Not wporg-parent-2021 — own header/footer.

---

## Jobs typography (YAML + prose)

[jobs.wordpress.net](https://jobs.wordpress.net/) runs on the standalone classic theme **`jobswp`** v2.0.0 ([WordPress/wordpress.org](https://github.com/WordPress/wordpress.org), redesigned 2026) with the **jobswp** plugin — not wporg-parent-2021 or the shared global header block. CSS custom properties in `style.css` mirror the wporg palette; **acid green** is the Jobs accent (filter pills, category badges), not Blueberry.

| Token | Font | Role |
|:------|:-----|:-----|
| `jobs-hero-title` | EB Garamond | Homepage H1 — 70px on `light-grey-2`; keyword span uses `acid-green-2` gradient highlight |
| `jobs-hero-tagline` | Inter | Hero subcopy — 24px in `charcoal-4`, max-width 600px centered |
| `jobs-stat-number` | EB Garamond | Dynamic hero stats — Open Positions / Categories / Remote Friendly (`heading-3`, 36px) |
| `jobs-stat-label` | Inter | Stat captions — 14px in `charcoal-4` |
| `jobs-card-title` | EB Garamond | Job listing H2 — 22px (`heading-6`) inside `.job-card` |
| `jobs-section-heading` | EB Garamond | "People Open to Work" H2 — 36px (`heading-3`) |
| `jobs-detail-title` | EB Garamond | Single-job H1 — 50px (`heading-2`) |
| `jobs-filter-label` | Inter 600 | "Filter by category" label — 14px in `charcoal-4` |

All default `h1`–`h6` use EB Garamond via `--font-heading`. Sidebar labels, nav links, form labels, and footer column headings use Inter. Body copy is Inter 16px at line-height 1.875.

## Jobs layout (prose)

Templates and styles in the **`jobswp`** theme ([jobs.wordpress.net](https://jobs.wordpress.net/)) — classic PHP/Underscores, not FSE. Does **not** use wporg global header/footer mu-plugins; ships its own sticky header and dark footer.

| Template / class | Background | Layout |
|:-----------------|:-----------|:-------|
| `.site-header` | white | Sticky top bar — WP.org logo SVG + "WordPress Jobs" wordmark; nav links (Jobs, Candidates, FAQ, Feedback) + primary "Post a Job" CTA; hamburger below 600px |
| `.hero` | `light-grey-2` | Centered EB Garamond H1 (70px) + tagline + Browse Jobs / Post a Job buttons + three stat tiles |
| `.filters` | white | "Filter by category" label + horizontal pill buttons (`filter-pill`); client-side category filter via `main.js` |
| `.jobs-grid` | white | 3-column linked job cards (→2 @900px, →1 @600px); empty state spans full grid width |
| `.candidates-section` | `light-grey-2` | Header row (H2 + count pill) + 2-column candidate cards (→1 @900px) + pagination + profile CTA |
| `.job-detail` | white | Breadcrumb → 2-column grid: prose body + 340px sticky `.job-sidebar__card` (→ stacked @900px) |
| `.job-detail-candidates` | `light-grey-2` wash | Compact 2-up candidate cards below single job |
| `.form-page` / `.post-job` | white | Post-a-job form at 680px content width; two-column contact/company fields |
| `.site-footer` | `charcoal-1` | 4-column link grid (About, Learn, Community, WordPress Jobs) + social row + EB Garamond italic "Code is Poetry." tagline |

Job cards hover to Blueberry border + subtle shadow (`rgba(56, 88, 233, 0.08)`). Active filter pills use solid `acid-green-1` fill. Category badges reuse `acid-green-3` pill treatment on both grid and detail views. Candidate cards link out to [profiles.wordpress.org](https://profiles.wordpress.org/) with 56px circular avatars (80px in homepage grid markup, 44px compact variant on job detail).

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `jobs-candidate-card` | jobs candidate card |
| `jobs-category-badge` | jobs category badge |
| `jobs-filter-pill` | jobs filter pill |
| `jobs-filter-pill-active` | jobs filter pill active |
| `jobs-hero` | jobs hero |
| `jobs-job-card` | jobs job card |
| `jobs-notice-success` | jobs notice success |
| `jobs-sidebar-card` | jobs sidebar card |
| `jobs-site-footer` | jobs site footer |
| `jobs-site-header` | jobs site header |


### Component prose

**Jobs page components (prose):**

- **`jobs-site-header`:** White sticky bar with 1px `light-grey-1` bottom border — WordPress.org logo SVG + "WordPress Jobs" wordmark; Inter 500 nav links; primary "Post a Job" button in header. Mobile hamburger toggles stacked nav below 600px. Accounts for wp-admin bar height via `top: var(--wp-admin--admin-bar--height)`.
- **`jobs-hero`:** Full-width `light-grey-2` band — EB Garamond 70px H1 with `.hero__highlight` keyword span (`acid-green-2` gradient underline at 40% height); 24px tagline in `charcoal-4`; centered Browse Jobs (primary) + Post a Job (outline) buttons; three dynamic stat tiles (Open Positions, Categories, Remote Friendly %).
- **`jobs-filter-pill` / `jobs-filter-pill-active`:** Pill buttons in a wrapping row — default white with 1px `light-grey-1` border; hover darkens border to `charcoal-5`; active state fills `acid-green-1` with `charcoal-1` text at weight 600. Client-side filter toggles `.job-card` visibility by `data-category` via `main.js`; empty state shows `.jobs-empty` message.
- **`jobs-job-card`:** Linked white card — 1px `light-grey-1` border, 2px radius, 30px padding. Contains `jobs-category-badge` pill, EB Garamond title (22px), Inter 600 company name, location/type meta row (emoji prefixes), and posted date separated by 1px `light-grey-2` top rule. Hover: Blueberry border + light shadow.
- **`jobs-candidate-card`:** Horizontal row on white — 56px circular avatar, "Open to Work" badge (`acid-green-3`), EB Garamond name (20px), role + optional company (`charcoal-3` / `charcoal-5`), right-arrow affordance. Links to profiles.wordpress.org. Compact variant on single-job pages uses 44px avatars.
- **`jobs-sidebar-card`:** Sticky 340px aside on single jobs — "Job Details" Inter 700 heading; label/value rows separated by 1px `light-grey-2` borders (Company, Job Type, Location, Budget, How to Apply with linked apply method).
- **`jobs-site-footer`:** `charcoal-1` four-column link grid (About, Learn, Community, WordPress Jobs) — Inter 700 uppercase column headings in `charcoal-5`; links in `light-grey-1`. Bottom row: social links + EB Garamond italic "Code is Poetry." tagline.
- **`jobs-notice-success`:** Post-a-job confirmation — `acid-green-3` background with dark green text; displays job management token.


## Do's and Don'ts


- On Jobs, use the standalone `jobswp` header/footer — not wporg global header blocks. Hero sits on `light-grey-2`, not `charcoal-2`. Use **acid green** (`acid-green-1` pills, `acid-green-3` badges) for Jobs accents — not Blueberry fills except links, buttons, and card hover borders. Job grid is 3 columns with EB Garamond card titles, not directory `is-style-cards-grid`. Candidate cards link to profiles.wordpress.org.
