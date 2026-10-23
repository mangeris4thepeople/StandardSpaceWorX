#!/usr/bin/env python3
"""Static site generator for standardspaceworx.space.

Run:  python3 tools/build.py
Writes every public page, robots.txt, sitemap.xml and site.webmanifest
into the repository root. Page content lives in tools/content.py.

Proprietary to Standard Data Company. All rights reserved.
"""
import json
import os
import re
import sys
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import PAGES, POSTS, SITE, LASTMOD, ORG, GTM_ID, GA4_ID  # noqa: E402

# Strings that must never appear in output: the em dash, a competitor name, and a Space Force program name.
BANNED = [chr(0x2014), "Orbital " + "Reclamation", "Space" + "WERX", "SPACE" + "WERX"]

NAV = [
    ("/technology/terrier/", "Terrier"),
    ("/mission/", "Mission"),
    ("/investors/", "Investors"),
    ("/about/", "About"),
    ("/news/", "News"),
    ("/contact/", "Contact"),
]


def abs_url(path):
    return SITE.rstrip("/") + path


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


def breadcrumb_schema(crumbs):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": abs_url(path)} for i, (path, name) in enumerate(crumbs)
        ],
    }


def gtm_head():
    if not GTM_ID:
        return ""
    # The container is injected after the window load event so the tag payload
    # does not compete with the hero render on slow mobile connections.
    return (
        "<script>window.dataLayer=window.dataLayer||[];"
        "(function(w,d,s,l,i){function g(){w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
        "var f=d.getElementsByTagName(s)[0],j=d.createElement(s);j.async=true;"
        "j.src='https://www.googletagmanager.com/gtm.js?id='+i;f.parentNode.insertBefore(j,f);}"
        "if(d.readyState==='complete'){g();}else{w.addEventListener('load',g);}})"
        "(window,document,'script','dataLayer','" + GTM_ID + "');</script>\n"
    )


def gtm_body():
    if not GTM_ID:
        return ""
    return (
        '<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=' + GTM_ID
        + '" height="0" width="0" style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>\n'
    )


def ga4_head():
    if not GA4_ID or GTM_ID:
        return ""
    return (
        '<script async src="https://www.googletagmanager.com/gtag/js?id=' + GA4_ID + '"></script>\n'
        "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','"
        + GA4_ID + "');</script>\n"
    )


def head(p):
    url = abs_url(p["path"])
    og_image = abs_url(p.get("og_image", "/assets/img/og-default.png"))
    robots = p.get("robots", "index,follow,max-image-preview:large,max-snippet:-1")
    schemas = p.get("schemas", [])
    parts = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        "<title>" + escape(p["title"]) + "</title>",
        '<meta name="description" content="' + escape(p["description"]) + '">',
        '<meta name="robots" content="' + robots + '">',
        '<link rel="canonical" href="' + url + '">',
        '<meta name="theme-color" content="#0B1020">',
        '<link rel="icon" href="/favicon.ico" sizes="32x32">',
        '<link rel="icon" type="image/svg+xml" href="/assets/img/icon.svg">',
        '<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">',
        '<link rel="manifest" href="/site.webmanifest">',
        '<meta property="og:type" content="' + p.get("og_type", "website") + '">',
        '<meta property="og:site_name" content="Standard SpaceWorX">',
        '<meta property="og:locale" content="en_US">',
        '<meta property="og:url" content="' + url + '">',
        '<meta property="og:title" content="' + escape(p.get("og_title", p["title"])) + '">',
        '<meta property="og:description" content="' + escape(p["description"]) + '">',
        '<meta property="og:image" content="' + og_image + '">',
        '<meta property="og:image:secure_url" content="' + og_image + '">',
        '<meta property="og:image:type" content="image/png">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:image:alt" content="' + escape(p.get("og_alt", "Standard SpaceWorX wordmark over a dark orbital graphic")) + '">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="' + escape(p.get("og_title", p["title"])) + '">',
        '<meta name="twitter:description" content="' + escape(p["description"]) + '">',
        '<meta name="twitter:image" content="' + og_image + '">',
        '<meta name="twitter:image:alt" content="' + escape(p.get("og_alt", "Standard SpaceWorX wordmark over a dark orbital graphic")) + '">',
    ]
    if p.get("article"):
        a = p["article"]
        parts += [
            '<meta property="article:published_time" content="' + a["published"] + 'T09:00:00-06:00">',
            '<meta property="article:modified_time" content="' + a.get("modified", a["published"]) + 'T09:00:00-06:00">',
            '<meta property="article:author" content="' + escape(ORG["founder"]) + '">',
            '<meta property="article:section" content="' + escape(a.get("section", "News")) + '">',
        ]
    parts += [
        '<link rel="preload" href="/assets/fonts/barlow-condensed-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>',
        '<link rel="preload" href="/assets/fonts/barlow-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>',
        '<link rel="stylesheet" href="/assets/site.css">',
    ]
    parts += [jsonld(s) for s in schemas]
    parts.append(gtm_head() + ga4_head() + "</head>")
    return "\n".join(parts) + "\n"


def nav(current):
    items = []
    for path, label in NAV:
        cur = ' aria-current="page"' if current == path or (path != "/" and current.startswith(path)) else ""
        items.append('<li><a href="' + path + '"' + cur + ">" + label + "</a></li>")
    return (
        '<a class="skip" href="#main">Skip to content</a>\n'
        '<header class="nav">\n  <div class="wrap">\n'
        '    <a class="logo" href="/" aria-label="Standard SpaceWorX home">Standard Space<b>WorX</b></a>\n'
        '    <button class="toggle" type="button" aria-expanded="false" aria-controls="primary-nav" onclick="var n=document.getElementById(\'primary-nav\');var o=n.classList.toggle(\'open\');this.setAttribute(\'aria-expanded\',o)">Menu</button>\n'
        '    <nav aria-label="Primary"><ul id="primary-nav">\n      ' + "\n      ".join(items) + "\n    </ul></nav>\n  </div>\n</header>\n"
    )


FOOTER = (
    "<footer>\n  <div class=\"wrap\">\n"
    "    <div>\n      <div class=\"logo\" style=\"font-size:18px\">Standard Space<b style=\"color:var(--orange)\">WorX</b></div>\n"
    "      <p style=\"margin-top:8px\">Reusable satellites for active debris removal. Standard SpaceWorX is a Standard Data Company venture based in Loveland, Colorado.</p>\n"
    "      <p style=\"margin-top:8px\">(c) 2026 Standard Data Company. All rights reserved.</p>\n    </div>\n"
    "    <div>\n      <div class=\"ft-h\">Company</div>\n      <ul>\n        <li><a href=\"/technology/terrier/\">The Terrier</a></li>\n        <li><a href=\"/mission/\">Mission</a></li>\n        <li><a href=\"/investors/\">Investors</a></li>\n        <li><a href=\"/about/\">About</a></li>\n        <li><a href=\"/news/\">News and updates</a></li>\n      </ul>\n    </div>\n"
    "    <div>\n      <div class=\"ft-h\">Contact</div>\n      <ul>\n        <li>Loveland, Colorado, USA</li>\n        <li><a href=\"mailto:contact@standardspaceworx.space\">contact@standardspaceworx.space</a></li>\n        <li><a href=\"/contact/\">Contact form</a></li>\n      </ul>\n    </div>\n"
    "  </div>\n</footer>\n"
)

ANALYTICS = (
    "<script>window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };</script>\n"
    '<script defer src="/_vercel/insights/script.js"></script>\n'
)


def crumbs_html(crumbs):
    if not crumbs or len(crumbs) < 2:
        return ""
    items = []
    for i, (path, name) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append('<li aria-current="page">' + escape(name) + "</li>")
        else:
            items.append('<li><a href="' + path + '">' + escape(name) + "</a></li>")
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(items) + "</ol></nav>\n"


def render(p):
    crumbs = p.get("crumbs")
    schemas = list(p.get("schemas", []))
    if crumbs and len(crumbs) > 1:
        schemas.append(breadcrumb_schema(crumbs))
    p = dict(p, schemas=schemas)
    body = p["body"]
    if "{crumbs}" in body:
        body = body.replace("{crumbs}", crumbs_html(crumbs))
    html = head(p) + "<body>\n" + gtm_body() + nav(p["path"]) + '<main id="main">\n' + body + "\n</main>\n" + FOOTER + ANALYTICS + "</body>\n</html>\n"
    for b in BANNED:
        if b in html:
            raise SystemExit("Banned string %r found in %s" % (b, p["path"]))
    assert len(p["title"]) <= 61, (p["path"], len(p["title"]))
    assert len(p["description"]) <= 155, (p["path"], len(p["description"]))
    assert html.count("<h1") == 1, (p["path"], html.count("<h1"))
    return html


def write(path, text):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", path)


def main():
    all_pages = PAGES + POSTS
    for p in all_pages:
        out = p["path"] + "index.html" if p["path"].endswith("/") else p["path"]
        write(out, render(p))

    # robots.txt
    write("/robots.txt", "User-agent: *\nAllow: /\nDisallow: /contact/thanks/\n\nSitemap: " + abs_url("/sitemap.xml") + "\n")

    # sitemap.xml
    urls = []
    for p in all_pages:
        if "noindex" in p.get("robots", ""):
            continue
        lm = p.get("lastmod", LASTMOD)
        pr = p.get("priority", "0.7")
        cf = p.get("changefreq", "monthly")
        urls.append("  <url>\n    <loc>" + abs_url(p["path"]) + "</loc>\n    <lastmod>" + lm + "</lastmod>\n    <changefreq>" + cf + "</changefreq>\n    <priority>" + pr + "</priority>\n  </url>")
    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")

    # manifest
    write("/site.webmanifest", json.dumps({
        "name": "Standard SpaceWorX",
        "short_name": "SpaceWorX",
        "description": ORG["description"],
        "start_url": "/",
        "display": "browser",
        "background_color": "#0B1020",
        "theme_color": "#0B1020",
        "icons": [
            {"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }, indent=2) + "\n")

    # 404
    nf = {
        "path": "/404.html",
        "title": "Page not found | Standard SpaceWorX",
        "description": "The page you requested does not exist on standardspaceworx.space.",
        "robots": "noindex,follow",
        "body": '<section class="page-hero"><div class="wrap narrow"><div class="eyebrow">404</div><h1>Page not found</h1><p class="lede">That address does not resolve. Try the <a href="/">homepage</a>, the <a href="/technology/terrier/">Terrier program</a>, or <a href="/contact/">contact us</a>.</p></div></section>',
    }
    write("/404.html", render(nf))
    print("done")


if __name__ == "__main__":
    main()
