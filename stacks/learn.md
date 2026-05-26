# Learn

**Inherits:** All tokens and global rules from [`DESIGN.md`](../DESIGN.md).

**URL:** [https://learn.wordpress.org/](https://learn.wordpress.org/)

**Theme:** `pub/wporg-learn-2024` + Sensei LMS

**Implementation:** FSE child theme of wporg-parent-2021.

---

## Learn typography (YAML + prose)

[learn.wordpress.org](https://learn.wordpress.org/) runs on **`pub/wporg-learn-2024`** (child of wporg-parent-2021) plus **Sensei LMS** for courses, lessons, and quizzes. Unlike marketing properties, Learn uses **Inter for almost all headings** — EB Garamond is reserved for promotional display headings only.

| Token | Font | Role |
|:------|:-----|:-----|
| `learn-hero-title` | Inter | Homepage H1 "Learn WordPress" — 50px white on `charcoal-2` |
| `learn-section-heading` | Inter 600 | Section H2s — "Get Started", "Featured Courses", "Featured Lessons" (32px) |
| `learn-display-heading` | EB Garamond | Promotional H2s — "Share your WordPress expertise" (70px heading-1 scale) |
| `learn-card-title` | Inter 600 | Course/lesson card titles in grids (26px h3 scale) |
| `learn-card-meta` | Inter | Duration, lesson count, level terms, course status chips (14px) |

Child `theme.json` sets h1 to EB Garamond 36px and h2–h6 to Inter 600. Taxonomy archives (`tax-learning-pathway`, `tax-level`, `tax-topic`) bump h1 to 50px. Sensei course player pages (`body.sensei`) use Inter throughout the lesson sidebar, quiz notices, and navigation.

## Learn layout (prose)

Homepage built from block patterns in `pub/wporg-learn-2024` with custom blocks under `wp-block-wporg-learn-*`:

| Section / class | Background | Layout |
|:----------------|:-----------|:-------|
| Hero | `charcoal-2` | H1 + tagline + search; sticky local nav with Learning Pathways submenu |
| `wp-block-wporg-learn-learning-pathway-cards` | pathway tint + SVG art | 3-column card grid; each card has illustrated header (`learning-pathway-{user,developer,designer}.svg`) |
| `wporg-learn-course-grid` | white | Responsive card grid (`is-style-cards-grid`); equal-height rows |
| `wporg-learn-lesson-grid` | white | Same grid pattern; lessons show duration + level term |
| `wp-block-wporg-learn-upcoming-online-workshops` | white | Workshop list (empty state when none scheduled) |
| Training CTA | `charcoal-2` | EB Garamond heading + primary/outline button pair |
| `wporg-learn-footer-signup` | `charcoal-1` | Jetpack subscribe form; left border divider from resources column |

Course cards use a **stacked-paper depth effect**: two pseudo-element layers (`::before`, `::after`) behind the card with 1px `light-grey-1` borders. Featured courses show a 16:9 thumbnail via Sensei's featured-label wrapper (text label hidden in grid). Custom blocks render duration (clock icon) and lesson count (lesson-plan icon) in `charcoal-4`.

Sensei LMS pages add a **course theme layout**: 60px header with progress bar (`learn-success-50` fill), ~280px collapsible sidebar with module/lesson tree, and main content column at 680px. Complete-lesson and quiz-submit buttons use `learn-success-50` / `learn-success-60` — not Blueberry.

## Components


### Component tokens


| Component | Role |
|:----------|:-----|
| `button-primary` | Training CTA |
| `card-course` | card course |
| `input-search` | Hero search |
| `learn-complete-button` | Sensei complete-lesson / quiz |
| `learn-course-card` | Featured course grid |
| `learn-course-status` | In-progress / completed chip |
| `learn-course-status-complete` | learn course status complete |
| `learn-footer-signup` | Jetpack subscribe column |
| `learn-hero` | Homepage title + search |
| `learn-lesson-card` | Featured lesson grid |
| `learn-pathway-card` | Learning pathway grid |
| `learn-training-cta` | "Get involved" band |
| `site-header / site-footer` | All sections |


### Component prose

**Learn page components (prose):**

- **`learn-hero`:** Charcoal-2 band with white Inter H1 (50px), tagline at line-height 2.3, and embedded search. Sticky local nav lists Learning Pathways, Courses, Lessons, Online Workshops, My courses.
- **`learn-pathway-card`:** Three-up grid from `wp-block-wporg-learn-learning-pathway-cards`. Each card links to a learning pathway (`/learning-pathway/user/`, `/developer/`, `/designer/`) with a full-bleed SVG illustration header and pathway-specific tint (`learn-pathway-user` `#F5FEF8`, `learn-pathway-developer` `#FFFFF4`, `learn-pathway-designer` `#FEF8F6`).
- **`learn-course-card`:** White card, 1px `light-grey-1` border, 2px radius, stacked-paper pseudo-layers. Shows 16:9 featured image, Inter title, duration + lesson-count rows with SVG icons, optional completed status chip.
- **`learn-lesson-card`:** Same grid shell as courses. Meta row: duration, bullet separator, level term (Beginner/Intermediate). Level taxonomy hidden on course cards.
- **`learn-course-status` / `learn-course-status-complete`:** Pill chips — grey for in-progress, `acid-green-3` background with `learn-success-70` text when completed.
- **`learn-training-cta`:** Charcoal-2 recruitment band with EB Garamond heading, body copy, primary "Get involved" + outline handbook link.
- **`learn-footer-signup`:** Charcoal-1 column with EB Garamond "Sign up for updates" and Jetpack compact subscription form.
- **`learn-complete-button`:** Sensei primary action — green `#008A20` for "Complete lesson" and quiz submit; Blueberry reserved for secondary/outline actions and nav CTAs.


## Do's and Don'ts


- On Learn, use `learn-success-50` for progress bars and completion actions — not Blueberry. Reserve EB Garamond for promotional display headings only; card titles are Inter 600.
