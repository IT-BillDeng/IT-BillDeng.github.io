# Bill Deng — Personal Site

This repository hosts my academic/personal website (Jekyll + Minimal Mistakes/Academic Pages) with my CV, publications, projects, and contact info.

## What's inside
- Home, CV, publications, projects, talks/teaching pages.
- PDF CVs in `files/`.
- Data for nav and site settings in `_config.yml` and `_data/`.
- Publication entries in `_publications/` (Markdown + front matter).

## Local preview
1. Install Ruby and Bundler (Linux/macOS):
   ```bash
   bundle config set --local path 'vendor/bundle'
   bundle install
   ```
2. Serve locally:
   ```bash
   bundle exec jekyll serve -l -H localhost
   ```
   Site appears at `http://localhost:4000`, hot-reloads on change.

## Docker
1. Build and run with the provided compose file:
   ```bash
   docker compose up --build
   ```
   Then open `http://localhost:4000`.
2. Stop and clean up:
   ```bash
   docker compose down
   ```

## Deploy
Open a pull request into `master`; GitHub Actions builds the Jekyll site for review. After the pull request is merged, GitHub Actions deploys the site to `https://<username>.github.io`.

## Repo layout
- `_pages/` — Home, CV, and custom pages.
- `_publications/` — Publication entries.
- `_data/navigation.yml` — Menu links.
- `files/` — PDFs (CV, papers, slides).
- `assets/` — Images and static assets.

## Contact
- Email: it.billdeng@gmail.com
- ORCID: 0009-0001-0270-3266

## License
Content © Bill Deng. Theme code is MIT licensed (see `LICENSE`).

## Acknowledgement
Built on the Academic Pages template (Minimal Mistakes), originally by Stuart Geiger and maintained by the community. Thank you to the maintainers and contributors.
