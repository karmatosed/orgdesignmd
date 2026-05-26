# Agent guide — WordPress.org design system

This repo documents the **WordPress.org federated visual brand** in [DESIGN.md](DESIGN.md) format. Use it when building UI that should match a specific wordpress.org property.

## What to load

| Task | Read |
|:-----|:-----|
| Tokens, colors, spacing, lint/export | [`DESIGN.md`](DESIGN.md) only |
| Work on one property (Showcase, Forums, Jobs, …) | [`DESIGN.md`](DESIGN.md) + [`stacks/{section}.md`](stacks/README.md) |
| Pick the section file | [`stacks/README.md`](stacks/README.md) index |

**Always start with `DESIGN.md`.** Section files are supplementary prose — not DESIGN.md format, not lint targets, no YAML tokens.

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
npm run design:lint          # required after DESIGN.md token edits
npm run design:export:tailwind   # optional — Tailwind v4 @theme
npm run design:export:dtcg         # optional — W3C tokens.json
```

## Global guardrails (from DESIGN.md)

- Button radius **2px** everywhere (`rounded.sm`).
- Links: Blueberry, underlined by default, no underline on hover.
- Don't use Anton / `display-cta` outside Main homepage and Enterprise cover.
- Don't apply Showcase screenshot frames to directory UI.
- Profiles: use `profiles-*` tokens and `badge-*` for medals — not wporg `headline-*` / `charcoal-*` in body UI.

Full rationale and research: [`README.md`](README.md).
