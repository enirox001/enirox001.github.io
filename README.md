# enirox’s personal website

A small, static GitHub Pages site. Live at https://enirox001.github.io/.

## Editing

The source for page content and the shared layout is `scripts/build.py`. The
bookshelf is maintained in `content/books.json`. Styling and theme behaviour
live in `assets/`. No packages, framework, or Jekyll installation are required.

After editing, use Python 3.12 or newer:

```sh
python3 scripts/build.py
```

Commit the changed sources **and generated HTML**. GitHub Pages serves the root
of `main`; the existing `.nojekyll` file keeps this a plain static site.
The build script never deletes files or writes under `coverage/`.

To preview locally:

```sh
python3 -m http.server 8000
```

Visit http://localhost:8000/. Content and navigation work without JavaScript;
JavaScript only controls the saved colour theme. Fonts are local system fonts.

## Bookshelf

Each book has a unique URL-safe `slug`, a title, authors, a reading status,
category, optional personal note, and book URL. Add actual reading entries to
`content/books.json`, then run the build. Book artwork is an original typographic
representation, not a reproduction of the publisher’s cover.

## Design references

- https://ludwigabap.com/ — Gruvbox palette, restrained typography and text-first layout.
- https://ismaelsadeeq.github.io/ — personal introduction and a bookshelf with reading status.
- https://achow101.com/ — articles, contact, and current/previous project sections.

Implementation is original. The site does not copy another person’s biography,
book reviews, reading history, or proprietary fonts. Articles are authored here; review notebooks are not imported.

## Publishing your own articles

Add an entry to `content/articles.json` with `slug`, `title`, `date`
(`YYYY-MM-DD`), and `description`. Put the article body in
`content/articles/<slug>.html`, using ordinary HTML paragraphs and headings.
Run `python3 scripts/build.py` and commit the source and generated pages.
Keep the list in newest-first order. The homepage shows its first three entries.
The list starts empty until you publish your own writing.
