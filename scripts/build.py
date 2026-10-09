#!/usr/bin/env python3
"""Build the personal pages using Python's standard library; leave coverage untouched."""
from pathlib import Path
from html import escape as e
import json

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://enirox001.github.io'
GITHUB = 'https://github.com/enirox001'
BOOKS = json.loads((ROOT / 'content/books.json').read_text())
NAV = [('Home', '/'), ('Articles', '/articles/'), ('Projects', '/projects/'), ('Bookshelf', '/books/'), ('Contact', '/contact/')]

def page(path, title, description, body, active='/'):
    nav = ''.join(f'<a href="{url}"' + (' aria-current="page"' if active == url else '') + f'>{name}</a>' for name, url in NAV)
    html = f'''<!doctype html>
<html lang="en" data-theme="gruvbox">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)} · enirox</title>
  <meta name="description" content="{e(description, quote=True)}">
  <meta name="author" content="Enoch Azariah">
  <meta name="color-scheme" content="dark light">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(title, quote=True)} · enirox">
  <meta property="og:description" content="{e(description, quote=True)}">
  <meta property="og:url" content="{SITE}{path}">
  <link rel="canonical" href="{SITE}{path}">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/assets/style.css">
  <script src="/assets/theme.js"></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="shell">
    <header class="site-header"><a class="wordmark" href="/" aria-label="enirox home">enirox<span>.</span></a><nav aria-label="Main navigation">{nav}</nav></header>
    <main id="main">{body}</main>
    <footer class="site-footer">
      <span>© 2026 Enoch Azariah</span>
      <div class="footer-links"><a href="{GITHUB}">GitHub</a><a href="mailto:enochazariah@proton.me">Email</a><a href="{GITHUB}/enirox001.github.io">Source</a></div>
      <div class="theme-control"><label for="theme">Colour theme</label><select id="theme"><option value="gruvbox">Gruvbox</option><option value="light">Light</option><option value="dark">Dark</option></select></div>
    </footer>
  </div>
</body>
</html>
'''
    dest = ROOT / (path.strip('/') + '/index.html' if path.endswith('/') and path != '/' else 'index.html' if path == '/' else path.lstrip('/'))
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html)

def heading(number, title):
    return f'<div class="section-heading"><span class="section-index">{number}</span><h2>{title}</h2></div>'

def row(title, url, description, meta=''):
    return f'<li>{f"<span class=\"meta\">{e(meta)}</span>" if meta else ""}<a class="row-title" href="{e(url, quote=True)}">{e(title)} <span aria-hidden="true">↗</span></a><p class="row-desc">{e(description)}</p></li>'

def cover(book):
    return f'<div class="book-cover" aria-hidden="true"><small>Programming<br>C++</small><div><strong>{e(book["title"])}</strong><span class="cover-rule"></span></div><small>Lippman · Lajoie · Moo</small></div>'

def book_card(book):
    return f'<article class="book"><a class="book-link" href="/books/{e(book["slug"])}/">{cover(book)}<span class="book-name">{e(book["title"])}</span></a><p class="book-author">{e(book["authors"])}</p><span class="status">{e(book["status"])}</span></article>'

notes = [
    ('Following an IPC memory leak', 'bitcoin_ipc_memleak.md', 'Notes tracing the investigation into memory growth, block-template lifetimes, and IPC.', 'Investigation · Bitcoin Core'),
    ('Bitcoin Core PR #36132', 'bitcoin_pr_review_36132.md', 'Working notes from a Bitcoin Core pull request review.', 'Code review · Bitcoin Core'),
    ('libmultiprocess PR #361', 'libmultiprocess_pr_review_361.md', 'Working notes from reviewing libmultiprocess.', 'Code review · libmultiprocess'),
    ('libmultiprocess PR #342', 'libmultiprocess_pr_review_342.md', 'Working notes from reviewing libmultiprocess.', 'Code review · libmultiprocess'),
    ('libmultiprocess PR #335', 'libmutiprocess_pr_review_335.md', 'Working notes from reviewing libmultiprocess.', 'Code review · libmultiprocess'),
]
def note_rows(items):
    return '<ul class="rows">' + ''.join(row(title, f'{GITHUB}/bitcoin-notes/blob/main/{file}', desc, meta) for title, file, desc, meta in items) + '</ul>'

page('/', 'Enoch Azariah', 'Software engineer and Bitcoin Core contributor. Projects, review notes, and a small bookshelf.', f'''
<section class="intro">
  <p class="eyebrow">Software engineer · Bitcoin open source</p>
  <img class="portrait" src="https://avatars.githubusercontent.com/u/66912335?v=4&amp;s=216" alt="Enoch Azariah’s GitHub profile picture" width="108" height="108">
  <h1>Enoch Azariah</h1>
  <p class="subtitle">I also go by <a href="{GITHUB}">enirox</a>.</p>
  <p>I’m a software engineer based in Nigeria, contributing to <a href="https://github.com/bitcoin/bitcoin">Bitcoin Core</a>. My interests are in wallets, the mempool, fuzzing, and multiprocess communication.</p>
  <p>I spend a lot of my time reading code, reviewing changes, and trying to understand why things work the way they do. Lately, that has meant digging into IPC and libmultiprocess, improving fuzz coverage, and experimenting with a Python client for Bitcoin Core.</p>
  <p>My background is in web and mobile development, particularly Flutter, TypeScript, and Python. I also worked on the Esplora GUI during my 2023 internship at <a href="https://www.blockchaincommons.com/">Blockchain Commons</a>. These days, I’m deepening my C++ through Bitcoin open-source work.</p>
  <div class="intro-links"><a href="{GITHUB}">GitHub ↗</a><a href="mailto:enochazariah@proton.me">Get in touch ↗</a></div>
</section>
<section>{heading('01', 'Current work')}
<ul class="rows">
{row('Bitcoin Core & libmultiprocess', 'https://github.com/bitcoin/bitcoin/pulls?q=is%3Apr+author%3Aenirox001', 'Contributions, code review, testing, and fuzzing, with a particular interest in IPC.', 'C++ · Python')}
{row('btc-ipc', f'{GITHUB}/btc-ipc', 'An experimental Python IPC client and reference indexer for exploring Bitcoin Core’s external interfaces.', 'Python · Cap’n Proto · SQLite')}
</ul><a class="more" href="/projects/">Projects & notable work →</a>
</section>
<section>{heading('02', 'Notes & reviews')}{note_rows(notes[:2])}<a class="more" href="/articles/">All articles & notes →</a></section>
<section>{heading('03', 'On my bookshelf')}<p>Currently working through C++ fundamentals.</p><div class="book-grid">{''.join(book_card(b) for b in BOOKS)}</div><a class="more" href="/books/">Visit the bookshelf →</a></section>
''')

page('/projects/', 'Projects', 'Current projects, notable Bitcoin Core work, and earlier projects by Enoch Azariah.', f'''
<p class="eyebrow">Code, experiments & contributions</p><h1>Projects</h1>
<p class="subtitle page-intro">Most of my open-source work is on <a href="{GITHUB}">GitHub</a>. Here are a few things I’ve been working on.</p>
<section>{heading('01', 'Notable work')}<ul class="rows">
{row('IPC round-trip fuzz target', 'https://github.com/bitcoin/bitcoin/pull/35118', 'A fuzz target exercising the Cap’n Proto / libmultiprocess serialization bridge and client–server interaction.', 'Bitcoin Core · #35118')}
{row('Expanding IPC fuzz coverage', 'https://github.com/bitcoin/bitcoin/pull/35916', 'Work on argument checks, callbacks, and raw request and response payloads.', 'Bitcoin Core · #35916')}
{row('IPC fuzz coverage report', '/coverage/ipc/', 'The generated coverage report accompanying my IPC fuzzing work.', 'Testing · Coverage')}
</ul></section>
<section>{heading('02', 'Current')}
<article class="project"><h3><a href="https://github.com/bitcoin/bitcoin">Bitcoin Core ↗</a></h3><p>Contributing code, reviewing pull requests, and testing changes. My interests include wallet and mempool behaviour, fuzzing, and multiprocess / IPC.</p><a class="more" href="https://github.com/bitcoin/bitcoin/pulls?q=is%3Apr+author%3Aenirox001">My pull requests →</a></article>
<article class="project"><h3><a href="{GITHUB}/btc-ipc">btc-ipc ↗</a></h3><p>A reusable Python IPC client with a reference indexer, benchmarks, and tests. The indexer tracks block metadata, ordered transaction IDs, and active-chain membership, including reorg reconciliation. It is an experiment for evaluating capabilities and their semantics; using a method successfully does not establish a stable API.</p><div class="tags"><span class="tag">Python</span><span class="tag">Cap’n Proto</span><span class="tag">SQLite</span></div></article>
<article class="project"><h3><a href="https://github.com/bitcoin-core/libmultiprocess">libmultiprocess ↗</a></h3><p>Review and testing around the library behind Bitcoin Core’s multiprocess communication.</p><a class="more" href="{GITHUB}/bitcoin-notes">Review notebook →</a></article>
</section>
<section>{heading('03', 'Previous')}<ul class="rows">{row('Esplora GUI', f'{GITHUB}/esplora', 'Earlier work on the Bitcoin block explorer interface, including my Blockchain Commons internship.', 'Web · Bitcoin')}{row('Web & mobile projects', f'{GITHUB}?tab=repositories', 'Earlier projects and experiments with Flutter, TypeScript, and Python.', 'Flutter · TypeScript · Python')}</ul></section>
''', '/projects/')

page('/articles/', 'Articles & notes', 'Code-review notes and investigations by Enoch Azariah, covering Bitcoin Core and libmultiprocess.', f'''
<p class="eyebrow">Learning in public</p><h1>Articles & notes</h1>
<p class="subtitle page-intro">Things I’m working through in Bitcoin Core and the software around it.</p>
<p class="note">These are working notes from my public notebook: questions, investigations, and code reviews. They open on GitHub.</p>
<section>{heading('01', 'From the notebook')}{note_rows(notes)}<a class="more" href="{GITHUB}/bitcoin-notes">Browse the complete notebook ↗</a></section>
''', '/articles/')

page('/books/', 'Bookshelf', 'Books Enoch Azariah is reading, with reading status and personal notes.', f'''
<p class="eyebrow">Away from the code editor</p><h1>Bookshelf</h1>
<p class="subtitle page-intro">A small record of what I’m reading, with notes along the way.</p>
<section>{heading('01', 'Currently reading')}<div class="book-grid">{''.join(book_card(b) for b in BOOKS)}</div></section>
''', '/books/')
for book in BOOKS:
    page(f'/books/{book["slug"]}/', book['title'], book['note'], f'''
<a class="back" href="/books/">← Back to the bookshelf</a>
<h1>{e(book['title'])}</h1><p class="subtitle">{e(book['authors'])}</p>
<div class="book-detail">{cover(book)}<div><span class="status">{e(book['status'])}</span><h2 style="margin-top:24px">Why I’m reading it</h2><p>{e(book['note'])}</p><p class="small">{e(book['category'])}</p><a class="more" href="{e(book['url'], quote=True)}">Book details at the publisher ↗</a></div></div>
''', '/books/')

page('/contact/', 'Contact', 'Contact Enoch Azariah about software engineering and Bitcoin open-source work.', f'''
<p class="eyebrow">Say hello</p><h1>Contact</h1>
<p class="subtitle page-intro">You can reach me by email or find my work on GitHub.</p>
<dl class="contact-list"><div><dt>Email</dt><dd><a href="mailto:enochazariah@proton.me">enochazariah@proton.me</a></dd></div><div><dt>GitHub</dt><dd><a href="{GITHUB}">@enirox001 ↗</a></dd></div></dl>
''', '/contact/')
page('/404.html', 'Page not found', 'This page could not be found.', '<p class="eyebrow">404</p><h1>This page wandered off.</h1><p>The link may be out of date. You can head back to the homepage or browse the notebook.</p><div class="intro-links"><a href="/">← Home</a><a href="/articles/">Articles & notes →</a></div>', '')
print('Built 7 pages. Existing coverage files were not modified.')
