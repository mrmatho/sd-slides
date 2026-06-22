# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm run dev      # Start dev server at http://localhost:3030 (opens browser)
npm run build    # Build static site to dist/
npm run export   # Export slides as PDF
```

Note: The project uses pnpm conventions (`.npmrc` has pnpm settings), but npm scripts work fine. Use whichever is available.

## Architecture

This is a [Slidev](https://sli.dev/) presentation for a VCE Software Development (Units 3 & 4) course.

**Entry point:** `slides.md` — the root file that imports all page files in order via `src:` frontmatter directives. Each page file is a standalone Markdown file in `pages/`.

**Page files:** `pages/NN_topic_name.md` — numbered sequentially, each containing one or more slides separated by `---`. Slides use the [Neversink theme](https://gureckis.github.io/slidev-theme-neversink/getting-started.html) layouts and components.

**Theme:** `slidev-theme-neversink` — provides layouts like `top-title`, `top-title-two-cols`, and Vue components like `<SpeechBubble>`, `<Admonition>`, `<Toc>`. Colors are passed as `color:` frontmatter (e.g. `sky`, `blue-light`, `navy`).

**Custom components:** `components/Counter.vue` — auto-imported by Slidev, available in any slide as `<Counter />`.

**Snippets:** `components/snippets/external.ts` — code snippets importable into slides using Slidev's `<<< @/snippets/...` syntax with region markers (`#region snippet` / `#endregion snippet`).

**Deployment:** Netlify, publishing the `dist/` folder via `npm run build`.

## Slide authoring conventions

- Global defaults (`transition: fade`, `hideInToc: true`, `selectable: true`) are set in `slides.md` frontmatter and apply to all slides unless overridden per-slide.
- `hideInToc: false` on a slide makes it appear in the `<Toc>` table of contents on the title slide.
- `zoom:` frontmatter scales slide content — useful when a slide has a lot of content.
- `::title::`, `::left::`, `::right::`, `::content::` are slot markers used by Neversink layouts.
- MDC syntax is enabled (`mdc: true`) — allows inline directives like `==highlighted text==`.
- To add a new topic, create `pages/NN_topic.md` and add a corresponding `src:` entry in `slides.md`.

## Dependency notes

**`@slidev/cli` is pinned to `52.14.2`** — do not upgrade without testing. Version history:
- `52.14.2` — current working version. Fixes a bug where the "goto" dialog (press `g`) leaked a list of all slides onto the right side of every slide when the presentation had many pages ([#2520](https://github.com/slidevjs/slidev/pull/2520)).
- `52.14.1` — had the GotoDialog overflow bug above.
- `52.15.x` / `52.16.x` — introduced a separate breaking issue (reason unknown; GitHub issues confirmed it). Avoid until re-tested.

**Slidev UI tip:** If a dropdown list of slides appears on the right side of the screen, it is the "goto" dialog leaking through. Press `g` to toggle it, or check the `@slidev/cli` version.
