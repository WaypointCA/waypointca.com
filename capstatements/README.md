# Capability Statements

Source for the four market capability statement PDFs linked from `index.html`.

Previously these existed only as finished PDFs with no source, so any edit meant
rebuilding the whole document by hand. Now the content is data and the layout is
a template.

## Editing

- **Content** — `content.py`. `COMMON` holds the blocks shared by all four
  statements (contact, credentials, metrics, NAICS, company data), so a
  credential change is a one-line edit that propagates everywhere. `MARKETS`
  holds the per-market overview, competencies, why, and teaming sections.
  `PAST_PERFORMANCE` is shared; each market re-orders it via `pp_order` to lead
  with its most relevant engagement.
- **Layout** — `build.py`, in the CSS block of `build_html()`.

## Building

```sh
python3 build.py                  # all four, straight into ../assets/
python3 build.py --market Defense # just one
python3 build.py --keep-html      # leave intermediate HTML in build/ for debugging
```

Rendering uses headless Chrome (already installed); no pip dependencies.

Each statement must stay **one page** — that is the APEX Accelerator convention
and buyers expect it. After editing content, confirm the page count:

```sh
python3 -c "import re;print(len(re.findall(rb'/Type\s*/Page[^s]',open('../assets/Waypoint_CapStmt_Defense.pdf','rb').read())))"
```

If content overflows to two pages, trim copy rather than shrinking the base font
below 7.6pt — it is already at the low end of readable when printed.
