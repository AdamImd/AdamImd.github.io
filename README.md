# Adam Imdieke's website

Source for [adamimd.github.io](https://adamimd.github.io/), a public academic portfolio built with the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme.

## Content map

- `_pages/about.md` is the home page; `_pages/projects.md` renders cards from `_projects/`.
- `_projects/` contains the project summaries and evidence boundaries. `importance` sets order within each category.
- `_news/` contains dated home-page updates.
- `_bibliography/papers.bib` drives the publications page.
- `_data/cv.yml` drives the web CV, which takes precedence over any JSON resume data; `_pages/teaching.md` and `_data/repositories.yml` contain other public information.
- `assets/img/projects/` and `assets/video/projects/` hold sourced project media; see the media README and each page caption for evidence limits.
- `assets/` contains local images and documents. The old November 2025 CV PDF was removed because it omitted 2026 work; add a newly reviewed PDF before restoring a download link.

This is a public repository. Only add information and media approved for public release. Describe simulation, analytic results, hardware tests, and future plans distinctly; do not imply physical validation from a rendering or software pilot. When adding a paper, verify its title, authors, venue, status, and public link.

## Build and deployment

The deployment workflow is `.github/workflows/deploy.yml`. It builds on pushes to `main` and on pull requests targeting `main`; a push to `main` publishes the site. The workflow pins Ruby 3.3.5, installs ImageMagick, then runs `bundle exec jekyll build` with `JEKYLL_ENV=production`. `.github/workflows/broken-links-site.yml` checks generated local links on pull requests and after deployment.

The build pins Ubuntu 24.04. Sass warnings for the bundled theme's legacy imports and global functions are explicitly silenced in `_config.yml`; migrate those styles together before Dart Sass 3. ActiveSupport uses the upcoming timezone behavior through `_plugins/00-active-support-timezone.rb`.

ImageMagick generates responsive WebP files from still images. Animated GIFs remain in their original format; include them with `avoid_scaling=true` so the page does not refer to generated WebP files.

For a local build with those prerequisites:

```bash
bundle install
JEKYLL_ENV=production bundle exec jekyll build
```

Review the generated `_site/` before publishing. The existing `INSTALL.md`, `CUSTOMIZE.md`, and `FAQ.md` are upstream al-folio reference documentation, not site-specific content.
