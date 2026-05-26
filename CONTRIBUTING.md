# Contributing

This repo extends the [DESIGN.md format](https://github.com/google-labs-code/design.md) for WordPress.org. The **format spec** lives upstream — this guide covers **how we use it here**.

## Doc map

| File | Purpose |
|:-----|:--------|
| [`DESIGN.md`](DESIGN.md) | Canonical tokens (YAML) + global prose — **lint and export target** |
| [`stacks/{section}.md`](stacks/README.md) | Per-property typography, layout, components, Do's |
| [`AGENTS.md`](AGENTS.md) | Quick guide for coding agents |
| [`README.md`](README.md) | Research notes and project context |

**Rule:** tokens live in `DESIGN.md` only. Stack files reference tokens by name — never copy YAML into `stacks/`.

## Using DESIGN.md with agents

[DESIGN.md](https://github.com/google-labs-code/design.md) exists so coding agents can read exact token values **and** the rationale for applying them. This repo adds **section stacks** so agents don't load 1,700 lines of prose when they only need Showcase or Jobs.

See also [`AGENTS.md`](AGENTS.md) — the short operational guide agents should read first.

### In this repo (Cursor, Claude Code, etc.)

| Setup | What happens |
|:------|:-------------|
| **`AGENTS.md` at repo root** | Cursor and similar tools load it automatically as project context |
| **Manual `@` references** | `@DESIGN.md` + `@stacks/showcase.md` scopes context to one property |
| **Rules** | Optional `.cursor/rules` can point agents at `DESIGN.md` + one stack for theme work |

**Default load for agents in this repo:** `AGENTS.md` → `DESIGN.md` → one `stacks/{section}.md` if the task names a property.

### In another project (consumer repo)

When building a WordPress theme, plugin, or prototype **outside** this repo:

1. **Clone or submodule** this repo, or copy `DESIGN.md` + the relevant `stacks/*.md`.
2. **Add a pointer** in the consumer project's `AGENTS.md` (or README):

   ```markdown
   ## Design system
   Follow tokens in `path/to/orgdesignmd/DESIGN.md`.
   For Showcase work, also read `path/to/orgdesignmd/stacks/showcase.md`.
   Run `npm run design:lint` in orgdesignmd after token changes.
   ```

3. **`@`-mention** the files in each session, or add a Cursor rule with globs for your theme directory.
4. **Export tokens** into the consumer project when implementing CSS:

   ```bash
   cd orgdesignmd && npm run design:export:tailwind > ../my-theme/assets/theme.css
   ```

Agents should treat exported CSS as generated output — **edit `DESIGN.md`**, re-export, don't hand-edit `theme.css` as the source of truth.

### What to load (context budget)

| Task | Files | Avoid |
|:-----|:------|:------|
| Global button, color, spacing | `DESIGN.md` | All 19 stack files |
| One property UI | `DESIGN.md` + `stacks/{section}.md` | Unrelated stacks |
| Token edit / lint | `DESIGN.md` only | Stack files unless prose must change |
| Research / audit | `README.md` + stack + live theme link in stack header | Loading full DESIGN.md prose when YAML suffices |

**Section stack prose overrides** generic wporg patterns in `DESIGN.md` when they conflict. If an agent cites `charcoal-2` for a Showcase hero, it should re-read `stacks/showcase.md`.

### Inject the upstream spec

For agents unfamiliar with DESIGN.md format:

```bash
npx @google/design.md spec          # full format spec (markdown)
npx @google/design.md spec --rules  # spec + lint rules table
```

Paste into a prompt, or `@`-include in tools that support shell output. Use when the agent needs to **author or restructure** YAML, not for everyday UI work.

### Example prompts

**Scoped UI work:**

> Build a Showcase archive filter row. Use `DESIGN.md` tokens and follow `stacks/showcase.md` for layout, components, and Do's. Use `{colors.*}` values from YAML — don't invent hex codes.

**Token change:**

> Add a `showcase-archive-heading` typography token to `DESIGN.md`, reference it from the relevant component, update `stacks/showcase.md`, run `npm run design:lint`, fix any broken refs.

**Cross-repo consumption:**

> Implement this block theme pattern for the Plugins directory. Read `orgdesignmd/DESIGN.md` and `orgdesignmd/stacks/plugins.md`. Map components to `theme.json` and block markup; use exported `theme.css` for CSS variables where helpful.

### Agent verification loop

After any edit to `DESIGN.md` YAML:

```bash
npm run design:lint
```

Agents should run this before claiming tokens are valid. **0 errors** required; warnings (contrast, orphaned colors) should be reviewed but don't fail the linter.

Optional: `npx @google/design.md diff` before/after when refactoring tokens.

## Using DESIGN.md

### Read

| Scope | Load |
|:------|:-----|
| Full WordPress.org system | `DESIGN.md` |
| One property (e.g. Showcase) | `DESIGN.md` + `stacks/showcase.md` |

Section prose **overrides** generic wporg defaults when they conflict (hero band color, wide width, outlier stacks).

### Lint and export

```bash
npm install
npm run design:lint                 # required after token edits — must pass with 0 errors
npm run design:export:tailwind      # → theme.css (Tailwind v4 @theme)
npm run design:export:dtcg          # → tokens.json (W3C DTCG)
```

Upstream CLI reference: [`@google/design.md`](https://www.npmjs.com/package/@google/design.md). Inject spec context with `npx @google/design.md spec`.

Compare versions before/after a change:

```bash
npx @google/design.md diff DESIGN.md.bak DESIGN.md
```

### Token conventions (this repo)

- **Colors** — wporg palette (`charcoal-*`, `primary`, tints) plus section-scoped groups (`news-*`, `showcase-*`, `profiles-*`, `jobs-*`, …).
- **Typography** — shared wporg UI tokens (`body-md`, `headline-*`) plus section tokens (`showcase-hero-title`, `docs-hero-title`, …).
- **Components** — YAML in `DESIGN.md`; use `{colors.*}`, `{typography.*}`, `{rounded.*}`, `{spacing.*}` references. Variants are separate keys (`button-primary-hover`).
- **References** — must resolve; `broken-ref` lint errors block merge-quality changes.

Global prose sections in `DESIGN.md` follow the [canonical section order](https://github.com/google-labs-code/design.md): Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts.

## Editing workflow

### Change an existing token

1. Edit YAML in `DESIGN.md`.
2. Update related prose in `DESIGN.md` or the relevant `stacks/{section}.md` if behavior changed.
3. Run `npm run design:lint` — fix errors; review warnings (contrast, orphaned tokens).

### Add a component

1. Add the component block under `components:` in `DESIGN.md`.
2. Add a row to the **Component tokens** table in the matching `stacks/{section}.md`.
3. Add **Component prose** in that stack file if the component has non-obvious behavior.
4. Lint.

### Add or extend a section

1. Add section color/typography/component tokens to `DESIGN.md` YAML.
2. Create or update `stacks/{slug}.md` with header (URL, theme source), typography, layout, components, Do's.
3. Add the section to [`stacks/README.md`](stacks/README.md), [`DESIGN.md`](DESIGN.md) layout index, and [`README.md`](README.md) section table.
4. Lint.

### What not to do

- Don't put YAML tokens in stack files.
- Don't lint or export stack files.
- Don't duplicate the upstream DESIGN.md spec in this repo — link to it.
- Don't apply one section's patterns globally (e.g. Showcase frames on Plugins cards).

## Implementation stacks

Most properties are FSE children of [wporg-parent-2021](https://github.com/WordPress/wporg-parent-2021). Exceptions:

| Stack | Sections |
|:------|:---------|
| wporg-main-2022 patterns | Main, About, Blocks, Enterprise |
| BuddyPress | Profiles |
| Standalone `jobswp` | Jobs |

When auditing live UI, prefer open-source theme sources linked from each stack file header.

## License

Contributions are licensed under the same [GPLv2 or later](license.txt) license as WordPress.
