# Section guides

Supplementary prose for WordPress.org properties. **Not [DESIGN.md](https://github.com/google-labs-code/design.md) files** — no YAML tokens, no lint target.

## Usage

| Mode | Load |
|:-----|:-----|
| Full system | [`DESIGN.md`](../DESIGN.md) only |
| Scoped work | `DESIGN.md` + **one section file** below |

Tokens, lint, and export always use **`DESIGN.md` only**. Section files add typography, layout, component tables, prose, and Do's for that property.

## Section index

| Section | File |
|:--------|:-----|
| Main | [`main.md`](main.md) |
| News | [`news.md`](news.md) |
| Showcase | [`showcase.md`](showcase.md) |
| Plugins | [`plugins.md`](plugins.md) |
| Themes | [`themes.md`](themes.md) |
| About | [`about.md`](about.md) |
| Blocks | [`blocks.md`](blocks.md) |
| Enterprise | [`enterprise.md`](enterprise.md) |
| Patterns | [`patterns.md`](patterns.md) |
| Photos | [`photos.md`](photos.md) |
| Learn | [`learn.md`](learn.md) |
| Documentation | [`documentation.md`](documentation.md) |
| Support Forums | [`forums.md`](forums.md) |
| Developer | [`developer.md`](developer.md) |
| Five for the Future | [`five-for-the-future.md`](five-for-the-future.md) |
| Events | [`events.md`](events.md) |
| Make | [`make.md`](make.md) |
| Profiles | [`profiles.md`](profiles.md) |
| Jobs | [`jobs.md`](jobs.md) |

## Inheritance

Each section file **references** [`DESIGN.md`](../DESIGN.md) for shared tokens and global rules. Component tables list only tokens relevant to that section, plus shared chrome (`button-primary`, `site-header`, etc.) where applicable.

Implementation note: most sections use wporg-parent-2021 FSE child themes; About/Blocks/Enterprise/Main use wporg-main-2022 patterns; Profiles uses BuddyPress; Jobs uses standalone `jobswp`.
