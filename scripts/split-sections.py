#!/usr/bin/env python3
"""Split bundled stack files into per-section guides with component tables."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STACKS = ROOT / "stacks"
DESIGN = ROOT / "DESIGN.md"

SECTION_META = {
    "main": {
        "title": "Main",
        "url": "https://wordpress.org/",
        "theme": "[wporg-main-2022](https://github.com/WordPress/wporg-main-2022)",
        "impl": "Homepage block patterns in wporg-main-2022 — shared global header/footer via mu-plugins.",
        "column": "Main",
        "prefixes": [],
    },
    "news": {
        "title": "News",
        "url": "https://wordpress.org/news/",
        "theme": "[wporg-news-2021](https://github.com/WordPress/wporg-news-2021)",
        "impl": "FSE child theme of wporg-parent-2021.",
        "column": "News",
        "prefixes": ["news-", "card-news"],
    },
    "showcase": {
        "title": "Showcase",
        "url": "https://wordpress.org/showcase/",
        "theme": "[wporg-showcase-2022](https://github.com/WordPress/wporg-showcase-2022)",
        "impl": "FSE child theme of wporg-parent-2021.",
        "column": "Showcase",
        "prefixes": ["showcase-", "card-showcase"],
    },
    "plugins": {
        "title": "Plugins",
        "url": "https://wordpress.org/plugins/",
        "theme": "`pub/wporg-plugins-2024` + **plugin-directory** plugin",
        "impl": "FSE child theme in WordPress/wordpress.org repo.",
        "column": "Plugins/Themes",
        "prefixes": ["plugins-"],
    },
    "themes": {
        "title": "Themes",
        "url": "https://wordpress.org/themes/",
        "theme": "`pub/wporg-themes-2024` (sibling to Plugins)",
        "impl": "Same directory patterns as Plugins — see [plugins.md](plugins.md).",
        "column": None,
        "prefixes": [],
        "alias_of": "plugins",
    },
    "about": {
        "title": "About",
        "url": "https://wordpress.org/about/",
        "theme": "wporg-main-2022 [`about.php` pattern](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/about.php)",
        "impl": "Block pattern in wporg-main-2022 — not a separate child theme.",
        "column": "About",
        "prefixes": ["about-"],
    },
    "blocks": {
        "title": "Blocks",
        "url": "https://wordpress.org/blocks/",
        "theme": "wporg-main-2022 [`blocks.php` pattern](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/blocks.php)",
        "impl": "Block pattern in wporg-main-2022.",
        "column": "Blocks",
        "prefixes": ["blocks-"],
    },
    "enterprise": {
        "title": "Enterprise",
        "url": "https://wordpress.org/enterprise/",
        "theme": "wporg-main-2022 [`enterprise.php` pattern](https://github.com/WordPress/wporg-main-2022/blob/trunk/source/wp-content/themes/wporg-main-2022/patterns/enterprise.php)",
        "impl": "Block pattern in wporg-main-2022.",
        "column": None,
        "prefixes": ["enterprise-"],
    },
    "patterns": {
        "title": "Patterns",
        "url": "https://wordpress.org/patterns/",
        "theme": "[wporg-pattern-directory-2024](https://github.com/WordPress/pattern-directory)",
        "impl": "FSE child theme of wporg-parent-2021.",
        "column": "Patterns",
        "prefixes": ["patterns-"],
    },
    "photos": {
        "title": "Photos",
        "url": "https://wordpress.org/photos/",
        "theme": "[wporg-photos-2024](https://github.com/WordPress/wporg-photo-directory)",
        "impl": "FSE child theme of wporg-parent-2021.",
        "column": "Photos",
        "prefixes": ["photos-"],
    },
    "learn": {
        "title": "Learn",
        "url": "https://learn.wordpress.org/",
        "theme": "`pub/wporg-learn-2024` + Sensei LMS",
        "impl": "FSE child theme of wporg-parent-2021.",
        "column": "Learn",
        "prefixes": ["learn-", "card-course"],
    },
    "documentation": {
        "title": "Documentation",
        "url": "https://wordpress.org/documentation/",
        "theme": "[wporg-documentation-2022](https://github.com/WordPress/wporg-documentation-2022)",
        "impl": "FSE child theme of wporg-parent-2021 (formerly HelpHub).",
        "column": "Docs",
        "prefixes": ["docs-"],
    },
    "forums": {
        "title": "Support Forums",
        "url": "https://wordpress.org/support/forums/",
        "theme": "`pub/wporg-support-2024` + bbPress",
        "impl": "Classic PHP child theme of wporg-parent-2021 wrapping bbPress.",
        "column": "Forums",
        "prefixes": ["forums-"],
    },
    "developer": {
        "title": "Developer",
        "url": "https://developer.wordpress.org/",
        "theme": "[wporg-developer-2023](https://github.com/WordPress/wporg-developer)",
        "impl": "FSE child theme of wporg-parent-2021.",
        "column": "Dev",
        "prefixes": ["dev-"],
    },
    "five-for-the-future": {
        "title": "Five for the Future",
        "url": "https://wordpress.org/five-for-the-future/",
        "theme": "[wporg-5ftf-2024](https://github.com/WordPress/five-for-the-future) + **wporg-5ftf** plugin",
        "impl": "FSE child theme of wporg-parent-2021.",
        "column": None,
        "prefixes": ["5ftf-"],
    },
    "events": {
        "title": "Events",
        "url": "https://events.wordpress.org/",
        "theme": "[wporg-events-2023](https://github.com/WordPress/wordcamp.org) in WordCamp.org repo",
        "impl": "FSE child theme of wporg-parent-2021.",
        "column": None,
        "prefixes": ["events-"],
    },
    "make": {
        "title": "Make",
        "url": "https://make.wordpress.org/",
        "theme": "[wporg-make-2024](https://github.com/WordPress/wporg-make)",
        "impl": "FSE child theme of wporg-parent-2021.",
        "column": None,
        "prefixes": ["make-"],
    },
    "profiles": {
        "title": "Profiles",
        "url": "https://profiles.wordpress.org/",
        "theme": "BuddyPress + legacy `profiles.wordpress.org` theme",
        "impl": "Hybrid — global header/footer via pub-sync mu-plugins; BuddyPress body UI.",
        "column": "Profiles",
        "prefixes": [
            "chip-team",
            "impact-tile",
            "activity-badge",
            "sponsor-pill",
            "timeline-",
            "medal-",
            "profiles-",
        ],
        "extra_sections": ["Colors"],
    },
    "jobs": {
        "title": "Jobs",
        "url": "https://jobs.wordpress.net/",
        "theme": "Standalone `jobswp` v2.0.0 + **jobswp** plugin",
        "impl": "Not wporg-parent-2021 — own header/footer.",
        "column": None,
        "prefixes": ["jobs-"],
    },
}


def read(path: Path) -> str:
    return path.read_text() if path.exists() else ""


def normalize_section_name(header: str) -> str:
    h = header.strip()
    for suffix in (
        " typography (YAML + prose)",
        " typography",
        " layout (prose)",
        " layout",
    ):
        if h.endswith(suffix):
            h = h[: -len(suffix)]
    return h.strip()


def extract_h3_blocks(text: str, must_contain: str) -> dict[str, str]:
    """Extract ### blocks whose header contains must_contain (e.g. 'typography')."""
    pattern = rf"^### (.+{must_contain}.+)$"
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    out: dict[str, str] = {}
    for i, m in enumerate(matches):
        name = normalize_section_name(m.group(1))
        start = m.start()
        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            rest = text[m.end() :]
            nxt = re.search(r"^## ", rest, re.MULTILINE)
            end = m.end() + nxt.start() if nxt else len(text)
        out[name] = text[start:end].strip() + "\n"
    return out


def extract_component_blocks(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    pattern = r"\*\*(.+?) (?:page )?components \(prose\):\*\*"
    matches = list(re.finditer(pattern, text))
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        start = m.start()
        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            rest = text[m.end() :]
            nxt = re.search(r"^## ", rest, re.MULTILINE)
            end = m.end() + nxt.start() if nxt else len(text)
        out[name] = text[start:end].strip() + "\n"
    return out


def extract_layout_one_liners(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for m in re.finditer(r"^\d+\. \*\*(.+?)\*\* — (.+)$", text, re.MULTILINE):
        out[m.group(1).strip()] = m.group(2).strip()
    return out


def parse_components_table(path: Path) -> dict[str, dict[str, str]]:
    lines = path.read_text().strip().splitlines()
    header = [h.strip() for h in lines[0].strip("|").split("|")]
    cols = header[1:]
    by_section: dict[str, dict[str, str]] = {c: {} for c in cols}
    for line in lines[2:]:
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        comp = cells[0]
        for col, val in zip(cols, cells[1:]):
            if val and val != "—":
                by_section[col][comp] = val
    return by_section


def parse_design_components() -> dict[str, str]:
    """Component keys from DESIGN.md YAML — role is the key itself."""
    text = DESIGN.read_text()
    m = re.search(r"^components:\n", text, re.MULTILINE)
    if not m:
        return {}
    chunk = text[m.end() :]
    end = re.search(r"^[a-z]+:", chunk, re.MULTILINE)
    chunk = chunk[: end.start()] if end else chunk
    return {line.split(":")[0].strip(): line.split(":")[0].strip() for line in chunk.splitlines() if re.match(r"^  [a-z0-9]", line)}


def components_table_for_section(rows: dict[str, str], shared: dict[str, str]) -> str:
    merged: dict[str, str] = {}
    for comp, role in {**shared, **rows}.items():
        merged[comp] = role
    if not merged:
        return "_No section-specific YAML components documented yet._\n"
    lines = ["| Component | Role |", "|:----------|:-----|"]
    for comp in sorted(merged.keys()):
        lines.append(f"| `{comp}` | {merged[comp]} |")
    return "\n".join(lines) + "\n"


def shared_components(by_col: dict[str, dict[str, str]]) -> dict[str, str]:
    shared: dict[str, str] = {}
    for comp, val in by_col.get("Main", {}).items():
        if comp in ("button-primary", "input-search", "site-header / site-footer"):
            shared[comp] = val
    return shared


def extract_dos(text: str) -> dict[str, list[str]]:
    dos: dict[str, list[str]] = {slug: [] for slug in SECTION_META}
    dos["_global"] = []
    seen: set[str] = set()
    for line in text.splitlines():
        if not line.startswith("- "):
            continue
        if line in seen:
            continue
        matched = False
        for meta in SECTION_META.values():
            title = meta["title"]
            if line.startswith(f"- On {title},") or line.startswith(f"- On {title} "):
                slug = next(k for k, v in SECTION_META.items() if v["title"] == title)
                dos[slug].append(line)
                seen.add(line)
                matched = True
                break
        if not matched:
            if "Profiles" in line or "profiles-" in line or "contribution medals" in line:
                dos["profiles"].append(line)
                seen.add(line)
            elif (
                "Don't apply showcase" in line
                or "Don't use Anton" in line
            ):
                dos["_global"].append(line)
                seen.add(line)
    return dos


def section_header(slug: str) -> str:
    meta = SECTION_META[slug]
    inherit_note = (
        "wporg palette and global header/footer chrome from [`DESIGN.md`](../DESIGN.md). "
        "Use `profiles-*` tokens for profile body UI — not `charcoal-*`."
        if slug == "profiles"
        else "Color values mirror wporg palette in CSS custom properties — see [`DESIGN.md`](../DESIGN.md). "
        "Global wporg header/footer **do not apply**."
        if slug == "jobs"
        else "All tokens and global rules from [`DESIGN.md`](../DESIGN.md)."
    )
    return f"""# {meta['title']}

**Inherits:** {inherit_note}

**URL:** [{meta['url']}]({meta['url']})

**Theme:** {meta['theme']}

**Implementation:** {meta['impl']}

---
"""


def build_main_typography() -> str:
    return """## Typography

Main homepage uses wporg display tokens from [`DESIGN.md`](../DESIGN.md):

| Token | Role |
|:------|:-----|
| `display-cta` | 120px EB Garamond hero headline |
| `headline-1`–`headline-6` | Campaign section headings |
| `code-display` | Download counter (Plex Mono, clamp scale) |
| `accent-display` | Anton marketing patterns only |

Body and UI use Inter at `body-md` (16px, line-height 1.875). Buttons use Inter 600 at `rounded.sm` (2px).
"""


def comp_rows_for_section(
    slug: str,
    meta: dict,
    by_col: dict[str, dict[str, str]],
    yaml_components: dict[str, str],
) -> dict[str, str]:
    rows: dict[str, str] = {}
    col = meta.get("column")
    if col and col in by_col:
        rows.update(by_col[col])
    for comp in yaml_components:
        for p in meta.get("prefixes", []):
            if comp.startswith(p) or comp == p:
                rows[comp] = by_col.get(col or "", {}).get(comp) or comp.replace("-", " ")
    return rows


def write_section_file(
    slug: str,
    *,
    typography: str = "",
    layout: str = "",
    components_prose: str = "",
    comp_rows: dict[str, str],
    shared: dict[str, str],
    dos: list[str],
    extra: str = "",
) -> None:
    meta = SECTION_META[slug]
    if meta.get("alias_of"):
        target = meta["alias_of"]
        content = f"""# {meta['title']}

**Inherits:** [`DESIGN.md`](../DESIGN.md) and [{target}.md]({target}.md).

**URL:** [{meta['url']}]({meta['url']})

**Theme:** {meta['theme']}

{meta['impl']}

The Themes directory shares the Plugins directory card grid, filter bar, and hero patterns documented in [plugins.md](plugins.md).
"""
        (STACKS / f"{slug}.md").write_text(content)
        return

    parts = [section_header(slug)]
    if extra:
        parts.append(extra.rstrip() + "\n")

    if typography:
        block = typography.strip()
        if not block.startswith("##"):
            block = "## Typography\n\n" + block
        parts.append(block.replace("### ", "## ", 1) if block.startswith("###") else block)
        parts.append("")
    elif slug == "main":
        parts.append(build_main_typography())
        parts.append("")

    if layout:
        block = layout.strip()
        if not block.startswith("##"):
            block = f"## Layout\n\n{block}"
        parts.append(block.replace("### ", "## ", 1) if block.startswith("###") else block)
        parts.append("")

    parts.append("## Components\n")
    parts.append("\n### Component tokens\n\n")
    parts.append(components_table_for_section(comp_rows, shared if slug != "jobs" else {}))
    if components_prose:
        prose = components_prose.strip()
        if prose.startswith("**"):
            parts.append("\n### Component prose\n\n" + prose + "\n")
        else:
            parts.append("\n### Component prose\n\n" + prose + "\n")

    parts.append("\n## Do's and Don'ts\n\n")
    if dos:
        parts.extend(d + "\n" for d in dos)
    else:
        parts.append("_See [`DESIGN.md`](../DESIGN.md) global Do's and Don'ts._\n")

    (STACKS / f"{slug}.md").write_text("\n".join(parts))


def extract_h2_section(text: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\n"
    m = re.search(pattern, text, re.MULTILINE)
    if not m:
        return ""
    rest = text[m.end() :]
    nxt = re.search(r"^## ", rest, re.MULTILINE)
    chunk = rest[: nxt.start()] if nxt else rest
    return chunk.strip() + "\n"


def main() -> None:
    fse = read(STACKS / "wporg-fse.md")
    main_stack = read(STACKS / "wporg-main.md")
    profiles_src = read(STACKS / "profiles.md")
    jobs_src = read(STACKS / "jobs.md")

    typo_main = extract_h3_blocks(main_stack, "typography")
    typo_fse = extract_h3_blocks(fse, "typography")
    typo_main.pop("Showcase", None)
    typography = {**typo_main, **typo_fse}

    layout_detail = {**extract_h3_blocks(main_stack, "layout"), **extract_h3_blocks(fse, "layout")}
    layout_lines = {**extract_layout_one_liners(main_stack), **extract_layout_one_liners(fse)}
    comp_prose = {**extract_component_blocks(main_stack), **extract_component_blocks(fse)}
    dos_map = extract_dos(main_stack + "\n" + fse + "\n" + profiles_src + "\n" + jobs_src)

    by_col = parse_components_table(STACKS / "components-table.md")
    shared = shared_components(by_col)
    yaml_components = parse_design_components()

    for slug, meta in SECTION_META.items():
        if slug == "themes":
            write_section_file(slug, comp_rows={}, shared={}, dos=[])
            continue

        title = meta["title"]

        if slug in ("profiles", "jobs"):
            src = profiles_src if slug == "profiles" else jobs_src
            t = extract_h2_section(src, "Typography") or typography.get(title, "")
            ld = extract_h2_section(src, "Layout")
            cp = extract_h2_section(src, "Components")
            # strip duplicate headings from components chunk
            cp = re.sub(r"^### Component tokens\n\n[\s\S]*?\n\n", "", cp)
            cp = re.sub(r"^### Component prose\n\n", "", cp)
            extra = extract_h2_section(src, "Colors") if slug == "profiles" else ""
            if extra:
                extra = "## Colors\n\n" + extra.replace("## Colors\n\n", "", 1)
            section_dos = [ln for ln in src.splitlines() if ln.startswith("- ") and "## Do's" in src.split(ln)[0][-200:]]
            section_dos = []
            in_dos = False
            for ln in src.splitlines():
                if ln.startswith("## Do's"):
                    in_dos = True
                    continue
                if in_dos and ln.startswith("## "):
                    break
                if in_dos and ln.startswith("- "):
                    section_dos.append(ln)
            rows = comp_rows_for_section(slug, meta, by_col, yaml_components)
            write_section_file(
                slug,
                typography=t,
                layout=ld,
                components_prose=cp,
                comp_rows=rows,
                shared=shared if slug != "jobs" else {},
                dos=section_dos or dos_map.get(slug, []),
                extra=extra,
            )
            continue

        t = typography.get(title, "")
        ld = layout_detail.get(title, "")
        ol = layout_lines.get(title, "")
        if ld:
            layout = ld
        elif ol:
            layout = ol + "\n"
        else:
            layout = ""

        cp = comp_prose.get(title, "")
        rows = comp_rows_for_section(slug, meta, by_col, yaml_components)
        section_dos = dos_map.get(slug, [])
        if slug == "main":
            section_dos = dos_map.get("_global", [])

        write_section_file(
            slug,
            typography=t,
            layout=layout,
            components_prose=cp,
            comp_rows=rows,
            shared=shared,
            dos=section_dos,
        )

    index_rows = [f"| {m['title']} | [`{s}.md`]({s}.md) |" for s, m in SECTION_META.items()]
    readme = f"""# Section guides

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
{chr(10).join(index_rows)}

## Inheritance

Each section file **references** [`DESIGN.md`](../DESIGN.md) for shared tokens and global rules. Component tables list only tokens relevant to that section, plus shared chrome (`button-primary`, `site-header`, etc.) where applicable.

Implementation note: most sections use wporg-parent-2021 FSE child themes; About/Blocks/Enterprise/Main use wporg-main-2022 patterns; Profiles uses BuddyPress; Jobs uses standalone `jobswp`.
"""
    (STACKS / "README.md").write_text(readme)

    for old in ("wporg-main.md", "wporg-fse.md", "components-table.md"):
        p = STACKS / old
        if p.exists():
            p.unlink()

    print("Section files:", sorted(p.name for p in STACKS.glob("*.md")))


if __name__ == "__main__":
    main()
