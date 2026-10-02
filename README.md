# Adam Imdieke's website

Source for [adamimd.github.io](https://adamimd.github.io/), a public academic portfolio built with the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme.

## Content map

- `_pages/about.md` is the home page, with three featured research projects and four recent public updates. `_pages/projects.md` is the Projects hub at `/projects/`; it renders searchable cards from `_projects/`. Shared project navigation is `_includes/project-nav.liquid`; `assets/js/project-filter.js` filters titles, descriptions, and stage labels.
- `_pages/videos.md` is the video showcase at `/projects/videos/`. Add recordings to `_data/video_showcase.yml` with a project link, poster, and evidence caption; `_includes/showcase-video.liquid` renders each player. Native videos load on demand. Set `portrait: true` on a section and its videos for recordings that pair physical footage with sensor visualizations vertically; shared styling lives in `_sass/_video-showcase.scss`. Keep external media on its original project host and local recordings in `assets/video/projects/`.
- `_pages/gifs.md` is the GIF showcase at `/projects/gifs/`. It reuses the video descriptions and groups, with derived-image metadata in `_data/gif_showcase.json`. `_scripts/build_gif_showcase.py` and its source recipe create short GIFs, smaller animated WebP alternatives, and still previews. No video/iframe is embedded on this page. `assets/js/gif-showcase.js` loads animations in view, restores stills when paused/offscreen, and respects reduced motion. GIF downloads remain available without JavaScript. See `assets/img/gifs/README.md` for derivation settings and the rebuild command.
- `_projects/` contains the project summaries and evidence boundaries. `importance` sets order within each category.
- `_news/` contains dated home-page updates.
- `_bibliography/papers.bib` drives the publications page.
- `_data/cv.yml` drives the web CV, which takes precedence over any JSON resume data; `_pages/teaching.md` and `_data/public_code.yml` contain other public information. `_pages/repositories.md` renders the Code view at `/projects/code/` with direct public repository links.
- `assets/img/projects/` and `assets/video/projects/` hold sourced project media; see the media README and each page caption for evidence limits.
- `assets/` contains local images and documents. The old November 2025 CV PDF was removed because it omitted 2026 work; add a newly reviewed PDF before restoring a download link.

This is a public repository. Only add information and media approved for public release. Describe simulation, analytic results, hardware tests, and future plans distinctly; do not imply physical validation from a rendering or software pilot. When adding a paper, verify its title, authors, venue, status, and public link.

## Navigation and presentation

The main menu is About, Publications, Projects, CV, and Teaching. Videos, GIFs, and Code are views within Projects. The old `/videos/`, `/gifs/`, and `/repositories/` paths redirect to their new locations, preserving fragments and query strings when JavaScript is enabled; each redirect also provides a direct link and a refresh fallback. Use Jekyll `{% link %}` references for internal media links so route changes stay synchronized.

`_sass/_portfolio.scss` defines the shared colors, typography, cards, focus states, and responsive layout. The footer flows after content. Project cards use still thumbnails to keep animation in the media views. `_scripts/build_portfolio_thumbnails.py` (Python/Pillow) extracts those frames from existing animated WebPs; `assets/img/projects/thumbnails/provenance.json` records source/output hashes and settings. Project cards use `stage` metadata for publication venues or prototype/simulation context; update those labels only from evidence. The home news limit is applied after excluding milestones marked `show_on_about: false`, and `/news/` retains the complete archive.

Content was reviewed on October 2, 2026; see `docs/portfolio-content-review-2026-10-02.md` for sources and the scope of that review.

## Build and deployment

The deployment workflow is `.github/workflows/deploy.yml`. It builds on pushes to `main` and on pull requests targeting `main`; a push to `main` publishes the site. The workflow pins Ruby 3.3.5, installs ImageMagick, then runs `bundle exec jekyll build` with `JEKYLL_ENV=production`. `.github/workflows/broken-links-site.yml` checks generated local links on pull requests and after deployment.

The build pins Ubuntu 24.04. Both workflows set Git's temporary initial branch to `main` before checkout. Sass warnings for the bundled theme's legacy imports and global functions are explicitly silenced in `_config.yml`; migrate those styles together before Dart Sass 3. ActiveSupport uses the upcoming timezone behavior through `_plugins/00-active-support-timezone.rb`.

The main stylesheet URL includes the build timestamp so new shared styles reach returning visitors even when the Sass cache filter emits an unchanged digest.

ImageMagick generates responsive WebP files from still images. Animated GIFs remain in their original format; include them with `avoid_scaling=true` so the page does not refer to generated WebP files.

For a local build with those prerequisites:

```bash
bundle install
JEKYLL_ENV=production bundle exec jekyll build
```

Review the generated `_site/` before publishing. The existing `INSTALL.md`, `CUSTOMIZE.md`, and `FAQ.md` are upstream al-folio reference documentation, not site-specific content.
