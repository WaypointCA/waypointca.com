#!/usr/bin/env python3
"""Render one single-page PDF capability statement per market.

Usage:  python3 build.py [--market Federal] [--keep-html]

Content lives in content.py. This file only handles layout and rendering.
PDFs are written straight into ../assets/ where index.html links them.
Rendering uses headless Chrome, which is already on this machine; no pip
installs required.
"""

import argparse
import base64
import html
import shutil
import subprocess
import sys
from pathlib import Path

from content import COMMON, MARKETS, PAST_PERFORMANCE

HERE = Path(__file__).parent
ASSETS_OUT = HERE.parent / "assets"
BUILD = HERE / "build"

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

NAVY = "#1f4e79"
NAVY_DARK = "#16395a"
GOLD = "#b79740"
SIDEBAR_BG = "#eef1f5"


def data_uri(path: Path) -> str:
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()


def e(text: str) -> str:
    return html.escape(text, quote=False)


def build_html(market: str, cfg: dict) -> str:
    logo = data_uri(HERE / "assets" / "logo.jpg")
    headshot = data_uri(HERE / "assets" / "headshot.jpg")

    contact_rows = ""
    for text, kind in COMMON["contact"]:
        cls = {"name": "c-name", "role": "c-role"}.get(kind, "c-plain")
        contact_rows += f'<div class="{cls}">{e(text)}</div>'

    cred_rows = "".join(
        f'<div class="row">{e(name)}{f" — {e(issuer)}" if issuer else ""}</div>'
        for name, issuer in COMMON["credentials"]
    )

    metric_rows = "".join(
        f'<div class="row"><span class="num">{e(num)}</span> {e(label)}</div>'
        for num, label in COMMON["metrics"]
    )

    naics_rows = "".join(
        f'<div class="row"><span class="num">{e(code)}</span> {e(desc)}</div>'
        for code, desc in COMMON["naics"]
    )

    company_rows = "".join(f'<div class="row">{e(line)}</div>' for line in COMMON["company_data"])

    comp_rows = "".join(
        f'<div class="item"><span class="lead">{e(title)}:</span> {e(body)}</div>'
        for title, body in cfg["competencies"]
    )

    pp_rows = ""
    for key in cfg["pp_order"]:
        client, body, result = PAST_PERFORMANCE[key]
        pp_rows += (
            f'<div class="item"><span class="lead">{e(client)}</span> — {e(body)}'
            f'<div class="result">&#8594; {e(result)}</div></div>'
        )

    why_rows = "".join(
        f'<div class="item"><span class="lead">{e(title)}:</span> {e(body)}</div>'
        for title, body in cfg["why"]
    )

    teaming_rows = "".join(
        f'<div class="item"><span class="lead">{e(title)}:</span> {e(body)}</div>'
        for title, body in cfg["teaming"]
    )

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{e(COMMON["company"])} — {e(market)} Capability Statement</title>
<style>
  @page {{ size: letter; margin: 0; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: Helvetica, Arial, sans-serif;
    font-size: 7.6pt;
    line-height: 1.34;
    color: #1a1a1a;
    width: 8.5in; height: 11in;
    display: flex; flex-direction: column;
  }}

  /* ── Masthead ─────────────────────────────── */
  .masthead {{
    background: {NAVY_DARK};
    color: #fff;
    display: flex; align-items: center;
    padding: 10px 14px;
    gap: 14px;
  }}
  .masthead img.logo {{ width: 52px; height: 52px; object-fit: contain; flex-shrink: 0; }}
  .masthead img.face {{ width: 52px; height: 52px; object-fit: cover; flex-shrink: 0; }}
  .masthead .title {{ flex: 1; text-align: center; }}
  .masthead h1 {{ font-size: 15pt; font-weight: bold; letter-spacing: 0.4px; }}
  .masthead .tagline {{ font-size: 7.6pt; margin-top: 3px; color: #d9e2ec; }}

  .band {{
    background: {GOLD}; color: #fff;
    text-align: center; padding: 3.5px;
    font-size: 7.4pt; font-weight: bold; letter-spacing: 0.5px;
  }}
  .doctype {{
    background: {NAVY}; color: #fff;
    text-align: center; padding: 4.5px;
    font-size: 10pt; font-weight: bold; letter-spacing: 1.6px;
  }}

  /* ── Body columns ─────────────────────────── */
  .cols {{ display: flex; flex: 1; min-height: 0; }}
  .sidebar {{ width: 2.0in; background: {SIDEBAR_BG}; padding: 0 0 8px; flex-shrink: 0; }}
  .main {{ flex: 1; padding: 0 12px 8px; }}

  .shead {{
    background: {NAVY}; color: #fff;
    font-size: 7.4pt; font-weight: bold; letter-spacing: 0.6px;
    padding: 2.5px 8px; margin-bottom: 5px;
  }}
  .sidebar .sblock {{ margin-bottom: 9px; }}
  .sidebar .row {{ padding: 0 8px 2px; font-size: 7.1pt; }}
  .sidebar .num {{ color: {NAVY}; font-weight: bold; }}
  .sidebar .c-name {{ padding: 0 8px; font-size: 9pt; font-weight: bold; color: {NAVY_DARK}; }}
  .sidebar .c-role {{ padding: 0 8px 2px; font-size: 7.1pt; }}
  .sidebar .c-plain {{ padding: 0 8px 1px; font-size: 7.1pt; }}

  .mhead {{
    background: {NAVY}; color: #fff;
    font-size: 7.6pt; font-weight: bold; letter-spacing: 0.6px;
    padding: 2.5px 8px; margin: 0 0 5px;
  }}
  .mblock {{ margin-bottom: 9px; }}
  .overview {{ text-align: justify; }}
  .item {{ margin-bottom: 4.5px; }}
  .item .lead {{ color: {NAVY}; font-weight: bold; }}
  .item .result {{ color: #4a5568; padding-left: 11px; margin-top: 1px; }}

  /* ── Footer ───────────────────────────────── */
  footer {{
    background: {NAVY_DARK}; color: #fff;
    display: flex; justify-content: space-between;
    padding: 5px 14px; font-size: 6.8pt;
    margin-top: auto;
  }}
</style></head><body>

<div class="masthead">
  <img class="logo" src="{logo}" alt="">
  <div class="title">
    <h1>{e(COMMON["company"])}</h1>
    <div class="tagline">{e(cfg["tagline"])}</div>
  </div>
  <img class="face" src="{headshot}" alt="">
</div>
<div class="band">{e(COMMON["cert_band"])}</div>
<div class="doctype">CAPABILITY STATEMENT</div>

<div class="cols">
  <aside class="sidebar">
    <div class="sblock"><div class="shead">CONTACT</div>{contact_rows}</div>
    <div class="sblock"><div class="shead">CREDENTIALS</div>{cred_rows}</div>
    <div class="sblock"><div class="shead">PERFORMANCE METRICS</div>{metric_rows}</div>
    <div class="sblock"><div class="shead">NAICS CODES</div>{naics_rows}</div>
    <div class="sblock"><div class="shead">COMPANY DATA</div>{company_rows}</div>
  </aside>

  <main class="main">
    <div class="mblock">
      <div class="mhead">COMPANY OVERVIEW</div>
      <div class="overview">{e(cfg["overview"])}</div>
    </div>
    <div class="mblock"><div class="mhead">CORE COMPETENCIES</div>{comp_rows}</div>
    <div class="mblock"><div class="mhead">PAST PERFORMANCE</div>{pp_rows}</div>
    <div class="mblock"><div class="mhead">WHY WAYPOINT</div>{why_rows}</div>
    <div class="mblock"><div class="mhead">TEAMING &amp; ENGAGEMENT</div>{teaming_rows}</div>
  </main>
</div>

<footer>
  <span>{e(COMMON["footer_left"])}</span>
  <span>{e(COMMON["footer_right"])}</span>
</footer>

</body></html>"""


def render(html_path: Path, pdf_path: Path) -> None:
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", f"file://{html_path}"],
        check=True, capture_output=True,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--market", help="build only this market (default: all)")
    ap.add_argument("--keep-html", action="store_true", help="leave intermediate HTML in build/")
    args = ap.parse_args()

    if not Path(CHROME).exists():
        print(f"error: Chrome not found at {CHROME}", file=sys.stderr)
        return 1

    markets = {args.market: MARKETS[args.market]} if args.market else MARKETS
    BUILD.mkdir(exist_ok=True)
    ASSETS_OUT.mkdir(exist_ok=True)

    for market, cfg in markets.items():
        html_path = BUILD / f"{market.lower()}.html"
        html_path.write_text(build_html(market, cfg))
        pdf_path = ASSETS_OUT / cfg["filename"]
        render(html_path, pdf_path)
        print(f"{market:<12} → assets/{cfg['filename']}  ({pdf_path.stat().st_size // 1024} KB)")

    if not args.keep_html:
        shutil.rmtree(BUILD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
