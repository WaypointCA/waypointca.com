#!/usr/bin/env python3
"""
AI Security Curriculum page generator
Waypoint Compliance Advisory - waypointca.com

Renders the pillar page and seven core pages into ../ai-security/curriculum/.

The shared shell (design tokens, nav, footer) is extracted from index.html at
build time rather than copied, so the curriculum cannot drift from the rest of
the site when index.html changes.

Usage:
    python3 curriculum/build.py            # from repo root
    python3 build.py                       # from curriculum/
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content import (  # noqa: E402
    AUTHOR, BASE, CORES, CREDITS, CREDIT_TOTAL, PILLAR, PRAXIS,
    REFERENCES, REFERENCES_NOTE, SITE, SYLLABUS,
)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "ai-security" / "curriculum"
INDEX = ROOT / "index.html"

GA = """    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-YKWY9GBXCT"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-YKWY9GBXCT');
    </script>"""

EXTRA_CSS = """
        /* ── Curriculum ───────────────────────────────── */
        .crumbs { background: var(--off-white); border-bottom: 1px solid var(--border);
                  padding: 0.7rem 2rem; font-size: 0.82rem; }
        .crumbs-inner { max-width: 1200px; margin: 0 auto; color: var(--text-muted); }
        .crumbs a { color: var(--text-muted); text-decoration: none; }
        .crumbs a:hover { color: var(--accent); text-decoration: underline; }
        .crumbs .sep { margin: 0 0.45rem; opacity: 0.5; }
        .crumbs [aria-current] { color: var(--navy); font-weight: 600; }

        .doc { max-width: 820px; margin: 0 auto; padding: 3rem 2rem 1rem; }
        .doc h2 { font-size: 1.55rem; font-weight: 800; color: var(--navy);
                  letter-spacing: -0.4px; margin: 2.75rem 0 1rem; }
        .doc h2:first-child { margin-top: 0; }
        .doc h3 { font-size: 1.12rem; font-weight: 700; color: var(--navy); margin: 1.9rem 0 0.6rem; }
        .doc p { margin-bottom: 1.15rem; line-height: 1.75; }
        .doc ul, .doc ol { margin: 0 0 1.35rem 1.35rem; }
        .doc li { margin-bottom: 0.55rem; line-height: 1.7; }
        .doc a { color: var(--accent); text-decoration: underline; text-underline-offset: 2px; }
        .doc a:hover { color: var(--accent-hover); }
        .doc code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.88em;
                    background: var(--light-bg); padding: 0.12rem 0.35rem; border-radius: 4px;
                    color: var(--navy); }
        .doc pre { background: var(--navy); color: #e6edf3; padding: 1.1rem 1.3rem;
                   border-radius: 8px; overflow-x: auto; margin: 0 0 1.5rem; font-size: 0.84rem;
                   line-height: 1.6; }
        .doc pre code { background: none; padding: 0; color: inherit; }

        .kicker { display: inline-block; font-size: 0.72rem; font-weight: 700;
                  text-transform: uppercase; letter-spacing: 1.4px; color: var(--accent);
                  margin-bottom: 0.6rem; }
        .lede { font-size: 1.12rem; color: var(--text-body); line-height: 1.7;
                border-left: 3px solid var(--accent); padding-left: 1.1rem; margin-bottom: 2rem; }
        .note { background: var(--off-white); border-left: 3px solid var(--gold);
                border-radius: 0 8px 8px 0; padding: 1rem 1.25rem; margin-bottom: 2rem;
                font-size: 0.9rem; line-height: 1.65; }

        .tbl { width: 100%; border-collapse: collapse; margin: 0 0 1.75rem; font-size: 0.9rem;
               display: block; overflow-x: auto; }
        .tbl th, .tbl td { border: 1px solid var(--border); padding: 0.6rem 0.8rem; text-align: left; }
        .tbl th { background: var(--light-bg); color: var(--navy); font-weight: 700; }
        .tbl td:first-child, .tbl th:first-child { white-space: nowrap; }
        .tbl tr.total td { font-weight: 700; color: var(--navy); background: var(--off-white); }

        .core-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.1rem;
                     margin: 0 0 1.5rem; }
        .core-card { display: block; background: var(--white); border: 1px solid var(--border);
                     border-radius: 10px; padding: 1.15rem 1.3rem; text-decoration: none;
                     color: inherit; transition: all 0.2s; }
        .core-card:hover { border-color: var(--accent); box-shadow: 0 3px 14px rgba(0,0,0,0.05);
                           transform: translateY(-2px); }
        .core-card .c-code { font-size: 0.7rem; font-weight: 700; letter-spacing: 1px;
                             text-transform: uppercase; color: var(--accent); }
        .core-card .c-title { font-size: 1rem; font-weight: 700; color: var(--navy);
                              margin: 0.3rem 0 0.35rem; line-height: 1.35; }
        .core-card .c-desc { font-size: 0.85rem; color: var(--text-muted); line-height: 1.55; }
        .core-card .c-flag { display: inline-block; font-size: 0.63rem; font-weight: 700;
                             text-transform: uppercase; letter-spacing: 0.6px; padding: 0.12rem 0.45rem;
                             border-radius: 3px; background: var(--accent-light); color: var(--accent);
                             margin-left: 0.4rem; vertical-align: middle; }

        .weekrow { border-left: 2px solid var(--border); padding-left: 1.1rem; margin-bottom: 1.2rem; }
        .weekrow .wk { font-weight: 700; color: var(--navy); font-size: 0.95rem; }
        .weekrow .wt { font-weight: 600; color: var(--text-dark); }
        .weekrow .lab { display: block; margin-top: 0.3rem; font-size: 0.85rem;
                        color: var(--accent); font-weight: 600; }

        .refs { font-size: 0.86rem; }
        .refs li { margin-bottom: 0.75rem; word-break: break-word; }

        .pager { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 3rem 0 0;
                 padding-top: 1.75rem; border-top: 1px solid var(--border); }
        .pager a { display: block; text-decoration: none; color: inherit; background: var(--white);
                   border: 1px solid var(--border); border-radius: 10px; padding: 0.95rem 1.15rem;
                   transition: all 0.2s; }
        .pager a:hover { border-color: var(--accent); }
        .pager .dir { display: block; font-size: 0.68rem; font-weight: 700; text-transform: uppercase;
                      letter-spacing: 1px; color: var(--text-muted); margin-bottom: 0.3rem; }
        .pager .t { font-size: 0.9rem; font-weight: 600; color: var(--navy); line-height: 1.35; }
        .pager .next { text-align: right; }

        @media (max-width: 768px) {
            .doc { padding: 2rem 1.25rem 1rem; }
            .doc h2 { font-size: 1.3rem; }
            .core-grid { grid-template-columns: 1fr; }
            .pager { grid-template-columns: 1fr; }
            .pager .next { text-align: left; }
            .crumbs { padding: 0.7rem 1.25rem; font-size: 0.76rem; }
        }
"""


def shell():
    """Pull design tokens, nav, and footer out of index.html so they never drift."""
    h = INDEX.read_text()
    style = h[h.index("<style>"):h.index("</style>")]
    nav = h[h.index("<!-- NAV -->"):h.index("<!-- HERO -->")]
    foot = h[h.index("<!-- FOOTER -->"):h.index("</footer>") + len("</footer>")]

    # Root-relative from a nested directory, and no same-page fragments.
    for frag in ("#markets", "#services", "#about", "#credentials", "#contact", "#insights"):
        nav = nav.replace(f'href="{frag}"', f'href="/{frag}"')
        foot = foot.replace(f'href="{frag}"', f'href="/{frag}"')
    nav = nav.replace('<a href="#" class="logo">', '<a href="/" class="logo">')
    foot = foot.replace('<a href="#" class="logo">', '<a href="/" class="logo">')
    foot = foot.replace('href="assets/', 'href="/assets/')
    return style + EXTRA_CSS + "</style>", nav, foot


def e(s: str) -> str:
    return html.escape(s, quote=False)


def crumbs(core=None) -> str:
    items = ['<a href="/ai-security/">AI Security</a>']
    if core:
        items.append(f'<a href="{BASE}/">Curriculum</a>')
        items.append(f'<span aria-current="page">{e(core["title"])}</span>')
    else:
        items.append('<span aria-current="page">Curriculum</span>')
    inner = '<span class="sep">/</span>'.join(items)
    return (f'<nav class="crumbs" aria-label="Breadcrumb"><div class="crumbs-inner">'
            f'<a href="/">Home</a><span class="sep">/</span>{inner}</div></nav>')


def breadcrumb_ld(core=None) -> str:
    items = [("Home", f"{SITE}/"), ("AI Security", f"{SITE}/ai-security/")]
    if core:
        items.append(("Curriculum", f"{SITE}{BASE}/"))
        items.append((core["title"], f"{SITE}{BASE}/{core['slug']}/"))
    else:
        items.append(("Curriculum", f"{SITE}{BASE}/"))
    els = ",".join(
        '{"@type":"ListItem","position":%d,"name":"%s","item":"%s"}'
        % (i + 1, html.escape(n, quote=True), u) for i, (n, u) in enumerate(items))
    return '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[%s]}' % els


def page(*, url, title, meta, body, ld_blocks) -> str:
    style, nav, foot = shell()
    lds = "\n".join(
        f'    <script type="application/ld+json">\n    {b}\n    </script>' for b in ld_blocks)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{e(title)}</title>
    <meta name="description" content="{html.escape(meta, quote=True)}">
    <link rel="canonical" href="{url}">
    <meta name="author" content="{AUTHOR['name']}">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{html.escape(title, quote=True)}">
    <meta property="og:description" content="{html.escape(meta, quote=True)}">
    <meta property="og:url" content="{url}">
    <meta property="og:site_name" content="Waypoint Compliance Advisory">
    <meta property="og:image" content="{SITE}/assets/waypoint-og.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html.escape(title, quote=True)}">
    <meta name="twitter:description" content="{html.escape(meta, quote=True)}">
    <meta name="twitter:image" content="{SITE}/assets/waypoint-og.png">
    <link rel="icon" href="/assets/favicon.ico" sizes="any">
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16x16.png">
    <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{style}
{lds}
{GA}
</head>
<body>

<a href="#main-content" class="skip-link">Skip to main content</a>

<div class="top-bar">
    SBA Certified SDVOSB <span>|</span> FL Certified Business Enterprise <span>|</span> SAM.gov Registered <span>|</span> MFMP Vendor
</div>

{nav}
{body}

{foot}

<script>function switchMarket(m) {{ window.location.href = '/#markets'; }}</script>

</body>
</html>
"""


def ul(items) -> str:
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(items) -> str:
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


# ── Pillar ──────────────────────────────────────────────────────────────────

def build_pillar() -> str:
    url = f"{SITE}{BASE}/"
    cards = ""
    for c in CORES:
        flag = '<span class="c-flag">Flagship</span>' if c.get("flagship") else (
            '<span class="c-flag">Security spine</span>' if c["spine"] else "")
        cards += (f'<a href="{BASE}/{c["slug"]}/" class="core-card">'
                  f'<span class="c-code">{e(c["code"])}</span>{flag}'
                  f'<div class="c-title">{e(c["title"])}</div>'
                  f'<div class="c-desc">{re.sub(r"<[^>]+>", "", c["description"])[:150].rsplit(" ", 1)[0]}.</div></a>')

    rows = ""
    for code, name, cr, slug in CREDITS:
        label = f'<a href="{BASE}/{slug}/">{e(name)}</a>' if slug else e(name)
        rows += f"<tr><td>{e(code)}</td><td>{label}</td><td>{cr}</td></tr>"
    rows += f'<tr class="total"><td colspan="2">Total</td><td>{CREDIT_TOTAL.split()[0]}</td></tr>'

    refs = ""
    for i, (text, href) in enumerate(REFERENCES, 1):
        refs += (f'<li id="ref-{i}">[{i}] {e(text)}<br>'
                 f'<a href="{href}" rel="noopener">{href}</a></li>')

    praxis = "".join(f"<h3>{e(t)}</h3><p>{e(d)}</p>" for t, d in PRAXIS)

    sections = ""
    for heading, blocks in PILLAR["sections"]:
        sections += f"<h2>{e(heading)}</h2>" + "".join(blocks)

    body = f"""<main id="main-content">
<section class="hero">
    <div class="hero-content" style="grid-template-columns:1fr;">
        <div class="hero-text" style="max-width:860px;">
            <div class="hero-eyebrow"><span class="dot" aria-hidden="true"></span>Authored Curriculum</div>
            <h1>Applied AI Security<br><span class="highlight">and Assurance</span></h1>
            <p class="subtitle">{e(PILLAR['lede'])}</p>
        </div>
    </div>
</section>

{crumbs()}

<div class="doc">
    <div class="note">
        <strong>What this is and is not.</strong> This curriculum was authored by
        {e(AUTHOR['name'])}, {e(AUTHOR['creds'])}, and is published as a body of knowledge and a
        professional reference. It is not an accredited program, and Waypoint Compliance Advisory
        does not offer admission, enrollment, or a degree. "Doctoral-level" describes the rigor of
        the material, not a credential available here.
    </div>

    {sections}

    <h2>The verified gap this addresses</h2>
    {''.join(PILLAR['gap'])}

    <h2>The security spine</h2>
    {''.join(PILLAR['spine'])}

    <h2>The seven cores</h2>
    <div class="core-grid">{cards}</div>

    <h2>The hands-on companion</h2>
    <p>Before the curriculum there is a free, self-directed lab. The
    <a href="https://github.com/WaypointCA/ai-security-lab" rel="noopener">AI Security Lab</a> is a 36-week
    open-source path covering foundations, offensive LLM work, classical adversarial machine
    learning, and building out a home lab. It is MIT licensed and takes pull requests.</p>
    <p>The lab is where you get reps. This curriculum is the same subject matter at research
    level, where the deliverable stops being a completed exercise and becomes a threat model
    that survives review, an evaluation methodology others can adopt, and an assurance case you
    can defend.</p>

    <h2>Scope and structure</h2>
    <p>The credit scope is included because it shows what a serious treatment of this field
    requires. Cores 4 through 7 are the security spine.</p>
    <table class="tbl">
        <thead><tr><th>Code</th><th>Course</th><th>Credits</th></tr></thead>
        <tbody>{rows}</tbody>
    </table>
    <p><strong>Sequencing.</strong> {''.join(PILLAR['sequencing']).replace('<p>', '').replace('</p>', '')}</p>

    <h2>Praxis sequence</h2>
    {praxis}

    <h2>References</h2>
    <ol class="refs">{refs}</ol>
    <p><em>{e(REFERENCES_NOTE)}</em></p>

    <div class="pager">
        <a href="/ai-security/"><span class="dir">Back to</span><span class="t">AI Security Practice</span></a>
        <a href="{BASE}/{CORES[0]['slug']}/" class="next"><span class="dir">Start with</span><span class="t">{e(CORES[0]['code'])}: {e(CORES[0]['title'])}</span></a>
    </div>
</div>
</main>"""

    program_ld = (
        '{"@context":"https://schema.org","@type":"EducationalOccupationalProgram",'
        f'"name":"{html.escape(PILLAR["title"], quote=True)}",'
        f'"description":"{html.escape(PILLAR["meta"], quote=True)}",'
        f'"url":"{url}",'
        '"programType":"Doctoral-level curriculum",'
        '"educationalCredentialAwarded":"None. Published as a reference body of knowledge.",'
        '"occupationalCategory":["AI Red Team Analyst","Adversarial Machine Learning Researcher",'
        '"Machine Learning Security Architect","AI Governance and Assurance Lead"],'
        f'"author":{{"@type":"Person","name":"{AUTHOR["name"]}","url":"{SITE}/#about"}},'
        f'"provider":{{"@type":"Organization","name":"Waypoint Compliance Advisory, LLC","url":"{SITE}"}},'
        '"hasCourse":[' + ",".join(
            '{"@type":"Course","name":"%s","url":"%s%s/%s/","provider":{"@type":"Organization",'
            '"name":"Waypoint Compliance Advisory, LLC","url":"%s"}}'
            % (html.escape(c["title"], quote=True), SITE, BASE, c["slug"], SITE) for c in CORES)
        + "]}"
    )
    return page(url=url, title=PILLAR["page_title"], meta=PILLAR["meta"],
                body=body, ld_blocks=[program_ld, breadcrumb_ld()])


# ── Spokes ──────────────────────────────────────────────────────────────────

def syllabus_html() -> str:
    s = SYLLABUS
    out = [f'<h2>Full syllabus</h2><p class="lede">{e(s["meta_line"])}</p>']
    out.append("<h3>Course description</h3>" + "".join(s["description"]))
    out.append("<h3>Prerequisites</h3>" + ul(e(x) for x in s["prerequisites"]))
    out.append("<h3>Learning outcomes</h3><p>On successful completion, students can:</p>"
               + ol(e(x) for x in s["outcomes"]))
    out.append("<h3>Course environment and tooling</h3>" + "".join(s["environment"])
               + f"<pre><code>{e(s['venv'])}</code></pre>" + "".join(s["environment_after"]))
    out.append("<h3>Required frameworks and readings</h3>" + s["anchors_intro"]
               + ul(s["anchors"]) + s["anchors_after"])

    sched = "<h3>Weekly schedule</h3>"
    for unit, weeks in s["schedule"]:
        sched += f"<h4 style='font-weight:700;color:var(--navy);margin:1.5rem 0 0.75rem;'>{e(unit)}</h4>"
        for wk, title, detail, lab in weeks:
            lab_html = f'<span class="lab">{e(lab)}</span>' if lab else ""
            sched += (f'<div class="weekrow"><span class="wk">{e(wk)}.</span> '
                      f'<span class="wt">{e(title)}</span> {e(detail)}{lab_html}</div>')
    out.append(sched)

    rows = "".join(f"<tr><td>{e(c)}</td><td>{w}</td><td>{e(d)}</td></tr>"
                   for c, w, d in s["assessment"])
    out.append("<h3>Assessment</h3>" + s["assessment_intro"]
               + f'<table class="tbl"><thead><tr><th>Component</th><th>Weight</th>'
                 f'<th>What it demonstrates</th></tr></thead><tbody>{rows}</tbody></table>'
               + s["assessment_after"])

    out.append("<h3>Capstone rubric</h3>" + s["rubric_intro"]
               + ol(f"<strong>{e(t)}.</strong> {e(d)}" for t, d in s["rubric"]))
    out.append("<h3>Ethics and legal policy</h3>" + s["ethics_intro"] + ul(e(x) for x in s["ethics"]))
    return "".join(out)


def build_core(c, prev, nxt) -> str:
    url = f"{SITE}{BASE}/{c['slug']}/"
    body_parts = [
        f'<h2>Description</h2><p>{c["description"]}</p>',
        f'<h2>Outcomes</h2>{ul(e(x) for x in c["outcomes"])}',
        f'<h2>Modules</h2>{ol(e(x) for x in c["modules"])}',
        f'<h2>Signature lab</h2><p>{c["lab"]}</p>',
    ]
    if c["reading"]:
        body_parts.append(f'<h2>Reading anchors</h2>{ul(c["reading"])}')
    body_parts.append(f'<h2>Research thread</h2><p>{e(c["thread"])}</p>')
    if c.get("flagship"):
        body_parts.append(syllabus_html())

    pager = '<div class="pager">'
    pager += (f'<a href="{BASE}/{prev["slug"]}/"><span class="dir">Previous</span>'
              f'<span class="t">{e(prev["code"])}: {e(prev["title"])}</span></a>' if prev else
              f'<a href="{BASE}/"><span class="dir">Back to</span>'
              f'<span class="t">Curriculum overview</span></a>')
    pager += (f'<a href="{BASE}/{nxt["slug"]}/" class="next"><span class="dir">Next</span>'
              f'<span class="t">{e(nxt["code"])}: {e(nxt["title"])}</span></a>' if nxt else
              f'<a href="{BASE}/" class="next"><span class="dir">Back to</span>'
              f'<span class="t">Curriculum overview</span></a>')
    pager += "</div>"

    body = f"""<main id="main-content">
<section class="hero">
    <div class="hero-content" style="grid-template-columns:1fr;">
        <div class="hero-text" style="max-width:860px;">
            <div class="hero-eyebrow"><span class="dot" aria-hidden="true"></span>{e(c['code'])}{' | Security spine' if c['spine'] else ''}</div>
            <h1>{e(c['title'])}</h1>
        </div>
    </div>
</section>

{crumbs(c)}

<div class="doc">
    <p><a href="{BASE}/">Part of the Applied AI Security and Assurance curriculum</a>,
    authored by {e(AUTHOR['name'])}, {e(AUTHOR['creds'])}. Published as a reference, not an
    enrollable course.</p>

    {''.join(body_parts)}

    {pager}
</div>
</main>"""

    course_ld = (
        '{"@context":"https://schema.org","@type":"Course",'
        f'"name":"{html.escape(c["title"], quote=True)}",'
        f'"description":"{html.escape(c["meta"], quote=True)}",'
        f'"url":"{url}",'
        f'"courseCode":"{c["code"]}",'
        '"educationalLevel":"Doctoral",'
        '"numberOfCredits":4,'
        '"teaches":[' + ",".join(f'"{html.escape(o, quote=True)}"' for o in c["outcomes"]) + '],'
        f'"author":{{"@type":"Person","name":"{AUTHOR["name"]}","url":"{SITE}/#about"}},'
        f'"provider":{{"@type":"Organization","name":"Waypoint Compliance Advisory, LLC","url":"{SITE}"}},'
        f'"isPartOf":{{"@type":"EducationalOccupationalProgram",'
        f'"name":"{html.escape(PILLAR["title"], quote=True)}","url":"{SITE}{BASE}/"}}}}'
    )
    return page(url=url, title=c["page_title"], meta=c["meta"],
                body=body, ld_blocks=[course_ld, breadcrumb_ld(c)])


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    written = []

    (OUT / "index.html").write_text(build_pillar())
    written.append((f"{BASE}/", PILLAR["page_title"]))

    for i, c in enumerate(CORES):
        prev = CORES[i - 1] if i > 0 else None
        nxt = CORES[i + 1] if i < len(CORES) - 1 else None
        d = OUT / c["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(build_core(c, prev, nxt))
        written.append((f"{BASE}/{c['slug']}/", c["page_title"]))

    for path, title in written:
        print(f"  {path:<62} {title[:56]}")
    print(f"\n{len(written)} pages written to {OUT.relative_to(ROOT)}")

    # House style is enforced, not assumed.
    bad = [p for p in OUT.rglob("*.html") if "—" in p.read_text()]
    if bad:
        print("ERROR: em dash found in:", [str(b) for b in bad])
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
