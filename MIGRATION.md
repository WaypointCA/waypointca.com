# Blog migration: blog.waypointca.com → waypointca.com/blog

Operational record for the subdomain-to-subdirectory move. Keep this file;
the Cloudflare rules below are the only part of the setup that does not live
in version control.

## Architecture

The site ships as one GitHub Pages artifact built by
`.github/workflows/deploy.yml`:

- Repo root (`index.html`, `404.html`, `ai-security/`, `assets/`, `CNAME`,
  `robots.txt`, sitemaps) is copied as-is.
- `blog-src/` is a Hugo site built into `/blog` with
  `--baseURL https://waypointca.com/blog/`.
- The workflow fails if any required root asset is missing from the artifact,
  including all five capability statement PDFs.

Pages source must be **GitHub Actions**, not "Deploy from a branch". Switching
back to branch-serve would publish `blog-src/` as raw files and 404 `/blog/`.

Hugo is pinned to **0.155.3** in the workflow, and `blog-src/hugo.toml`
declares a matching `module.hugoVersion` range so local and CI cannot drift.

## Cloudflare redirect rules

Both live under **Rules → Redirect Rules**. Order matters: the normalizer must
be evaluated first so slashless directory paths are corrected in a single hop
rather than being passed through and then normalized again by GitHub Pages.

`blog.waypointca.com` must remain a **Proxied (orange cloud)** DNS record. If
it is ever set to DNS-only, Cloudflare never sees the request and both rules
silently stop firing.

### Rule 1 — `blog subdomain trailing slash normalizer` (priority 1)

Adds the trailing slash for directory-style paths so the redirect lands on the
final URL directly. The excluded extensions are the complete set the blog
serves: `.css`, `.ico`, `.png`, `.txt`, `.xml`. Everything else Hugo emits is a
directory containing `index.html`.

Expression:

```
http.host eq "blog.waypointca.com"
and not ends_with(http.request.uri.path, "/")
and not ends_with(http.request.uri.path, ".xml")
and not ends_with(http.request.uri.path, ".txt")
and not ends_with(http.request.uri.path, ".css")
and not ends_with(http.request.uri.path, ".png")
and not ends_with(http.request.uri.path, ".ico")
```

Target URL (Dynamic):

```
concat("https://waypointca.com/blog", http.request.uri.path, "/")
```

Status: **301**. Preserve query string: **ON**.

### Rule 2 — `blog subdomain to /blog subdirectory` (priority 2)

Catches everything else: paths already ending in a slash, and the file-style
paths excluded above.

Expression:

```
http.host eq "blog.waypointca.com"
```

Target URL (Dynamic):

```
concat("https://waypointca.com/blog", http.request.uri.path)
```

Status: **301**. Preserve query string: **ON**.

## Rollback

The old blog repo (`WaypointCA/blog`), its Pages custom domain, and the DNS
record stay in place for 30 days. To roll back: disable both Cloudflare rules
and the subdomain serves its own content again immediately.

## Post-cutover

- Google Search Console: submit `https://waypointca.com/sitemap.xml`. Keep the
  `blog.waypointca.com` property; do not delete it, and use Change of Address
  is **not** applicable here (that tool is for domain moves, not
  subdomain-to-subdirectory). Monitor Coverage and the old property's
  Performance report as impressions migrate.
- Redirects stay in place indefinitely.
