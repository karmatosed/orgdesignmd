# Agent guide — WordPress.org design system

This repo documents the **WordPress.org federated visual brand** in [DESIGN.md](DESIGN.md) format. Use it when building UI that should match a specific wordpress.org property.

Human setup and consumer-repo patterns: [`CONTRIBUTING.md`](CONTRIBUTING.md#using-designmd-with-agents).

## What to load

| Task | Read |
|:-----|:-----|
| Tokens, colors, spacing, lint/export | [`DESIGN.md`](DESIGN.md) only |
| Work on one property (Showcase, Forums, Jobs, …) | [`DESIGN.md`](DESIGN.md) + [`stacks/{section}.md`](stacks/README.md) |
| Pick the section file | [`stacks/README.md`](stacks/README.md) index |
| Unfamiliar with DESIGN.md YAML format | `npx @google/design.md spec` ([upstream spec](https://github.com/google-labs-code/design.md)) |

**Always start with `DESIGN.md`.** Section files are supplementary prose — not DESIGN.md format, not lint targets, no YAML tokens.

**Do not** load every file in `stacks/` unless the task spans multiple properties. One section file per task keeps context accurate.

## How to apply DESIGN.md

1. **Read YAML first** — use `{colors.primary}`, `{typography.body-md}`, `{rounded.sm}` etc. from the front matter; don't guess hex or font sizes.
2. **Read section stack second** — heroes, grid width, component behavior, and Do's for that property live in `stacks/{section}.md` and **override** generic wporg prose when they conflict.
3. **Use component tokens** — prefer named components (`showcase-site-screenshot`, `plugins-job-card`) over re-inventing styles from raw colors.
4. **Respect Do's** — global rules in `DESIGN.md`; section rules in the stack file. Both apply; section wins on conflicts.

### Section → file

| Property | Stack file |
|:---------|:-----------|
| Main | [`stacks/main.md`](stacks/main.md) |
| News | [`stacks/news.md`](stacks/news.md) |
| Showcase | [`stacks/showcase.md`](stacks/showcase.md) |
| Plugins | [`stacks/plugins.md`](stacks/plugins.md) |
| Themes | [`stacks/themes.md`](stacks/themes.md) → also [`plugins.md`](stacks/plugins.md) |
| About / Blocks / Enterprise | [`about.md`](stacks/about.md) / [`blocks.md`](stacks/blocks.md) / [`enterprise.md`](stacks/enterprise.md) |
| Patterns / Photos / Learn | [`patterns.md`](stacks/patterns.md) / [`photos.md`](stacks/photos.md) / [`learn.md`](stacks/learn.md) |
| Documentation / Forums / Developer | [`documentation.md`](stacks/documentation.md) / [`forums.md`](stacks/forums.md) / [`developer.md`](stacks/developer.md) |
| Five for the Future / Events / Make | [`five-for-the-future.md`](stacks/five-for-the-future.md) / [`events.md`](stacks/events.md) / [`make.md`](stacks/make.md) |
| Profiles / Jobs | [`profiles.md`](stacks/profiles.md) / [`jobs.md`](stacks/jobs.md) |

Full index: [`stacks/README.md`](stacks/README.md).

## Architecture (important)

WordPress.org is **not one theme**. Properties share palette and global header/footer patterns but differ in heroes, layout width, typography, and components.

| Kind | Examples | Notes |
|:-----|:---------|:------|
| FSE child themes | News, Showcase, Plugins, Learn, Developer | Mostly `wporg-parent-2021` children |
| Main patterns | Main, About, Blocks, Enterprise | `wporg-main-2022` block patterns |
| Outliers | Profiles (BuddyPress), Jobs (`jobswp`) | Own body chrome; Jobs has no wporg global header |

Section-specific rules in `stacks/*.md` **override** generic wporg defaults. Examples: Showcase uses `charcoal-1` and 1760px wide; Plugins uses `charcoal-2`; Events uses a light header; Jobs uses acid green accents.

## Editing rules

1. **Token changes** — edit YAML in `DESIGN.md` only. Run `npm run design:lint` before finishing.
2. **Section prose** — typography, layout, component tables, Do's → edit the matching `stacks/{section}.md`.
3. **New components** — add YAML component + any section prose/table in the relevant stack file.
4. **Do not** duplicate tokens into stack files. Do not lint or export stack files.

## Verification

```bash
npm install
npm run design:lint          # required after DESIGN.md token edits — 0 errors
npm run design:export:tailwind   # optional — Tailwind v4 @theme
npm run design:export:dtcg         # optional — W3C tokens.json
```

Run `npm run design:lint` after token edits. Do not claim tokens are valid without linter output showing 0 errors.

## Global guardrails (from DESIGN.md)

- Button radius **2px** everywhere (`rounded.sm`).
- Links: Blueberry, underlined by default, no underline on hover.
- Don't use Anton / `display-cta` outside Main homepage and Enterprise cover.
- Don't apply Showcase screenshot frames to directory UI.
- Profiles: use `profiles-*` tokens and `badge-*` for medals — not wporg `headline-*` / `charcoal-*` in body UI.

Full rationale and research: [`README.md`](README.md). Contributor workflow: [`CONTRIBUTING.md`](CONTRIBUTING.md).
