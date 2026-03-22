import os
import re
import html
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
BLOG_DIR = ROOT / "blog"
INDEX_FILE = BLOG_DIR / "index.html"
SITEMAP_FILE = ROOT / "sitemap.xml"
BASE_URL = "https://danniapuesta.com"


def extract_title(content):
    m = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else "Artículo"


def extract_description(content):
    m = re.search(r'<meta name="description" content="(.*?)"', content, re.IGNORECASE)
    return m.group(1).strip() if m else "Guía de apuestas deportivas"


def get_posts():
    posts = []
    for folder in BLOG_DIR.iterdir():
        if not folder.is_dir():
            continue

        file = folder / "index.html"
        if not file.exists():
            continue

        content = file.read_text(encoding="utf-8", errors="ignore")

        title = extract_title(content)
        desc = extract_description(content)
        slug = folder.name

        posts.append({
            "title": html.escape(title),
            "desc": html.escape(desc),
            "slug": slug,
            "date": datetime.now().strftime("%Y-%m-%d")
        })

    return sorted(posts, key=lambda x: x["date"], reverse=True)


def build_index(posts):
    cards = ""
    for p in posts:
        cards += f"""
<a class="post-card" href="/blog/{p['slug']}/">
  <div class="post-top">
    <span class="post-tag">Artículo</span>
    <span class="badge-new">Nuevo</span>
  </div>
  <h3>{p['title']}</h3>
  <p>{p['desc']}</p>
  <div class="post-meta">
    <span>⏱ 6 min</span>
  </div>
</a>
"""

    html_final = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Blog Danni Apuesta</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans&display=swap" rel="stylesheet">
<style>
body {{ background:#080c10; color:#8099bb; font-family:'DM Sans'; }}
.container {{ max-width:1000px; margin:auto; padding:20px; }}
h1 {{ font-family:'Bebas Neue'; color:white; }}
.post-card {{ display:block; background:#161f2e; padding:20px; margin:10px 0; border-radius:12px; }}
</style>
</head>
<body>
<div class="container">
<h1>Blog de Apuestas</h1>
{cards}
</div>
</body>
</html>"""

    INDEX_FILE.write_text(html_final, encoding="utf-8")


def build_sitemap(posts):
    urls = ""
    for p in posts:
        urls += f"""
<url>
<loc>{BASE_URL}/blog/{p['slug']}/</loc>
<lastmod>{p['date']}</lastmod>
</url>
"""

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>"""

    SITEMAP_FILE.write_text(xml, encoding="utf-8")


def main():
    posts = get_posts()
    build_index(posts)
    build_sitemap(posts)


if __name__ == "__main__":
    main()
