import html
import re
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOG_DIR = ROOT / "blog"
INDEX_FILE = BLOG_DIR / "index.html"
SITEMAP_FILE = ROOT / "sitemap.xml"
BASE_URL = "https://danniapuesta.com"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def extract_title(content: str, slug: str) -> str:
    m = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
    if not m:
        return slug.replace("-", " ").title()
    title = re.sub(r"\s*\|\s*Danni Apuesta!?$", "", m.group(1).strip(), flags=re.IGNORECASE)
    return title.strip()


def extract_description(content: str) -> str:
    patterns = [
        r'<meta\s+name="description"\s+content="(.*?)"\s*/?>',
        r"<meta\s+name='description'\s+content='(.*?)'\s*/?>",
    ]
    for pattern in patterns:
        m = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if m:
            return " ".join(m.group(1).strip().split())
    return "Guía práctica de apuestas deportivas en Danni Apuesta."


def extract_canonical(content: str, slug: str, article_file: Path) -> str:
    m = re.search(r'<link\s+rel="canonical"\s+href="(.*?)"\s*/?>', content, re.IGNORECASE | re.DOTALL)
    if m:
        url = m.group(1).strip()
        if not url.endswith('/'):
            url += '/'
            new_content = content[:m.start(1)] + url + content[m.end(1):]
            article_file.write_text(new_content, encoding="utf-8", errors="ignore")
        return url
    return f"{BASE_URL}/blog/{slug}/"


def shorten(text: str, limit: int = 145) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].strip()
    return cut + "..."


def infer_tag(slug: str, title: str) -> str:
    s = slug.lower()
    t = title.lower()

    if any(x in s for x in ["bankroll", "poco-dinero", "stake", "gestion"]):
        return "Gestión"
    if any(x in s for x in ["value", "estrategia", "reto", "vivo"]):
        return "Estrategia"
    if any(x in s for x in ["roi", "win-rate", "metric", "estad"]):
        return "Estadísticas"
    if any(x in s for x in ["over", "under", "btts", "handicap"]):
        return "Tipos de apuesta"
    if any(x in s for x in ["como", "errores", "control", "leer", "mejores-ligas"]):
        return "Guía básica"
    if "value" in t:
        return "Estrategia"
    return "Artículo"


def infer_label(slug: str, title: str) -> str:
    s = slug.lower()
    if "value" in s:
        return "📌 Value Bet"
    if "btts" in s:
        return "📌 BTTS"
    if "under-2-5" in s:
        return "📌 Under 2.5"
    if "over-2-5" in s:
        return "📌 Over 2.5"
    if "over-1-5" in s:
        return "📌 Over 1.5"
    if "bankroll" in s:
        return "📌 Bankroll"
    if "errores" in s:
        return "📌 Errores"
    if "cuotas" in s:
        return "📌 Cuotas"
    if "vivo" in s:
        return "📌 En vivo"
    if "handicap" in s:
        return "📌 Handicap Asiático"
    if "reto" in s:
        return "📌 Reto escalera"
    if "control" in s:
        return "📌 Control"
    if "ligas" in s:
        return "📌 Ligas"
    if "estrategia" in s:
        return "📌 Estrategia"
    if "poco-dinero" in s:
        return "📌 Bankroll"
    return "📌 Artículo"


def git_lastmod(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", rel],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        date_str = result.stdout.strip()
        if date_str:
            return date_str
    except Exception:
        pass
    return datetime.utcnow().strftime("%Y-%m-%d")


def discover_posts():
    posts = []

    for folder in BLOG_DIR.iterdir():
        if not folder.is_dir():
            continue

        article_file = folder / "index.html"
        if not article_file.exists():
            continue

        slug = folder.name
        content = read_text(article_file)
        title = extract_title(content, slug)
        description = extract_description(content)
        canonical = extract_canonical(content, slug, article_file)
        lastmod = git_lastmod(article_file)

        posts.append({
            "slug": slug,
            "title": html.escape(title),
            "description": html.escape(shorten(description)),
            "url": canonical,
            "lastmod": lastmod,
            "tag": html.escape(infer_tag(slug, title)),
            "label": html.escape(infer_label(slug, title)),
        })

    posts.sort(key=lambda p: (p["lastmod"], p["slug"]), reverse=True)
    return posts


def build_cards(posts):
    cards = []

    for i, post in enumerate(posts):
        badge = '<span class="badge-new">Nuevo</span>' if i < 4 else ""
        cards.append(f"""
          <a class="post-card" href="/blog/{post['slug']}/">
            <div class="post-top">
              <span class="post-tag">{post['tag']}</span>
              {badge}
            </div>
            <h3>{post['title']}</h3>
            <p>{post['description']}</p>
            <div class="post-meta">
              <span>⏱ 6 min</span>
              <span>{post['label']}</span>
            </div>
          </a>
        """.rstrip())

    return "\n".join(cards)


def build_blog_index(posts):
    cards_html = build_cards(posts)

    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Blog de Apuestas Deportivas | Danni Apuesta</title>
  <meta name="description" content="Guías prácticas sobre apuestas deportivas de fútbol. Aprende sobre bankroll, ROI, value bet, BTTS, under 2.5, handicap asiático y más con Danni Apuesta." />
  <link rel="canonical" href="{BASE_URL}/blog/" />

  <meta property="og:title" content="Blog de Apuestas Deportivas | Danni Apuesta" />
  <meta property="og:description" content="Artículos prácticos para entender apuestas deportivas, mejorar tu análisis y controlar tu bankroll." />
  <meta property="og:url" content="{BASE_URL}/blog/" />
  <meta property="og:type" content="website" />

  <meta name="google-site-verification" content="XeVUGWBRjZH5mjTWQJiAL7mJFJ27vopU9fFpLLbrD8k" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet" />

  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}

    body {{
      font-family: 'DM Sans', sans-serif;
      background: #080c10;
      color: #8099bb;
      line-height: 1.7;
    }}

    a {{ text-decoration: none; color: inherit; }}

    .container {{
      width: min(1180px, 92%);
      margin: 0 auto;
    }}

    .site-header {{
      border-bottom: 1px solid #1e2d42;
      background: rgba(8, 12, 16, 0.95);
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(10px);
    }}

    .header-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      min-height: 78px;
    }}

    .logo {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-family: 'Bebas Neue', sans-serif;
      letter-spacing: 0.6px;
      color: #e8f0fe;
      font-size: 2rem;
    }}

    .logo-mark {{
      color: #00b4d8;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .header-link {{
      color: #c7d8f0;
      font-weight: 500;
    }}

    .header-cta {{
      background: linear-gradient(135deg, #00b4d8, #0077b6);
      color: #04121c;
      font-weight: 700;
      padding: 12px 18px;
      border-radius: 999px;
    }}

    .hero {{
      padding: 54px 0 28px;
      text-align: center;
    }}

    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 14px;
      border: 1px solid #1e2d42;
      border-radius: 999px;
      background: #101823;
      color: #9fc2eb;
      margin-bottom: 18px;
      font-size: 0.92rem;
    }}

    .hero h1 {{
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(2.8rem, 7vw, 4.8rem);
      line-height: 0.95;
      letter-spacing: 0.8px;
      color: #e8f0fe;
      margin-bottom: 14px;
    }}

    .hero p {{
      max-width: 780px;
      margin: 0 auto;
      font-size: 1.05rem;
      color: #a9bfdc;
    }}

    .featured-strip {{
      margin: 28px auto 10px;
      max-width: 980px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
    }}

    .featured-box {{
      background: #111926;
      border: 1px solid #1e2d42;
      border-radius: 14px;
      padding: 16px;
      text-align: left;
    }}

    .featured-box strong {{
      display: block;
      color: #e8f0fe;
      margin-bottom: 6px;
      font-size: 0.98rem;
    }}

    .featured-box span {{
      color: #8ea8ca;
      font-size: 0.92rem;
    }}

    .blog-section {{
      padding: 22px 0 60px;
    }}

    .section-head {{
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 22px;
    }}

    .section-head h2 {{
      font-family: 'Bebas Neue', sans-serif;
      color: #00b4d8;
      font-size: 2.3rem;
      letter-spacing: 0.6px;
    }}

    .section-head p {{
      color: #91aacc;
      max-width: 760px;
    }}

    .posts-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 18px;
    }}

    .post-card {{
      display: block;
      background: #161f2e;
      border: 1px solid #1e2d42;
      border-radius: 18px;
      padding: 20px;
      transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
      overflow: hidden;
    }}

    .post-card:hover {{
      transform: translateY(-3px);
      border-color: #2a4364;
      box-shadow: 0 14px 30px rgba(0,0,0,0.22);
    }}

    .post-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 14px;
    }}

    .post-tag {{
      display: inline-flex;
      align-items: center;
      padding: 6px 10px;
      border-radius: 999px;
      background: #0f1824;
      border: 1px solid #1f3249;
      color: #97b7df;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}

    .badge-new {{
      display: inline-flex;
      align-items: center;
      padding: 5px 9px;
      border-radius: 999px;
      background: rgba(0,180,216,0.14);
      color: #00d0f7;
      border: 1px solid rgba(0,180,216,0.34);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.4px;
      text-transform: uppercase;
      flex-shrink: 0;
    }}

    .post-card h3 {{
      font-family: 'Bebas Neue', sans-serif;
      color: #e8f0fe;
      font-size: 1.9rem;
      line-height: 1.02;
      letter-spacing: 0.45px;
      margin-bottom: 12px;
      word-break: break-word;
    }}

    .post-card p {{
      color: #9ab1d1;
      margin-bottom: 16px;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .post-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      color: #7d98bd;
      font-size: 0.9rem;
    }}

    .post-meta span {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .cta-section {{
      padding: 0 0 64px;
    }}

    .cta-box {{
      background: linear-gradient(135deg, #0f1722, #10273a);
      border: 1px solid #1d3a55;
      border-radius: 22px;
      padding: 30px;
      text-align: center;
    }}

    .cta-box h2 {{
      font-family: 'Bebas Neue', sans-serif;
      color: #e8f0fe;
      font-size: 2.5rem;
      letter-spacing: 0.5px;
      margin-bottom: 10px;
    }}

    .cta-box p {{
      max-width: 760px;
      margin: 0 auto 18px;
      color: #a8c0e0;
    }}

    .cta-button {{
      display: inline-block;
      background: #00b4d8;
      color: #04121c;
      font-weight: 700;
      padding: 13px 20px;
      border-radius: 999px;
    }}

    .site-footer {{
      border-top: 1px solid #1e2d42;
      padding: 28px 0 36px;
      color: #89a2c2;
    }}

    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      margin-top: 10px;
    }}

    .footer-links a {{
      color: #b5cae8;
    }}

    @media (max-width: 940px) {{
      .featured-strip {{
        grid-template-columns: repeat(2, 1fr);
      }}

      .posts-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    @media (max-width: 640px) {{
      .header-inner {{
        padding: 12px 0;
      }}

      .logo {{
        font-size: 1.7rem;
      }}

      .header-actions {{
        gap: 10px;
      }}

      .header-cta {{
        padding: 10px 14px;
      }}

      .hero {{
        padding-top: 34px;
      }}

      .featured-strip {{
        grid-template-columns: 1fr;
      }}

      .post-card h3 {{
        font-size: 1.6rem;
      }}
    }}
  </style>

  <script type="application/ld+json">
  {{
    "@context":"https://schema.org",
    "@type":"Blog",
    "name":"Blog de Apuestas Deportivas | Danni Apuesta",
    "url":"{BASE_URL}/blog/",
    "description":"Guías prácticas sobre apuestas deportivas de fútbol. Aprende sobre bankroll, ROI, value bet, BTTS, under 2.5, handicap asiático y más con Danni Apuesta.",
    "inLanguage":"es",
    "publisher":{{
      "@type":"Organization",
      "name":"Danni Apuesta"
    }}
  }}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="{BASE_URL}" class="logo"><span class="logo-mark">⚽</span> Danni Apuesta!</a>
      <div class="header-actions">
        <a class="header-link" href="{BASE_URL}/blog/">Blog</a>
        <a class="header-cta" href="{BASE_URL}">Usar la App →</a>
      </div>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="container">
        <div class="hero-badge">📚 Blog de Apuestas Deportivas</div>
        <h1>Aprende a apostar con más cabeza y menos impulso</h1>
        <p>
          Guías prácticas para entender mejor los mercados, controlar tu bankroll, analizar estadísticas y evitar errores comunes en apuestas deportivas de fútbol.
        </p>

        <div class="featured-strip">
          <div class="featured-box">
            <strong>Tipos de apuesta</strong>
            <span>BTTS, Under 2.5, Over 2.5, Handicap Asiático y más.</span>
          </div>
          <div class="featured-box">
            <strong>Gestión</strong>
            <span>Controla tu bankroll, ROI y resultados reales.</span>
          </div>
          <div class="featured-box">
            <strong>Estrategia</strong>
            <span>Aprende a detectar value bets y apostar mejor.</span>
          </div>
          <div class="featured-box">
            <strong>Guías básicas</strong>
            <span>Contenido claro para principiantes y apostadores en crecimiento.</span>
          </div>
        </div>
      </div>
    </section>

    <section class="blog-section">
      <div class="container">
        <div class="section-head">
          <div>
            <h2>Últimos artículos</h2>
            <p>Los artículos más nuevos aparecen primero. El blog se actualiza automáticamente cuando subes un nuevo artículo.</p>
          </div>
        </div>

        <div class="posts-grid">
{cards_html}
        </div>
      </div>
    </section>

    <section class="cta-section">
      <div class="container">
        <div class="cta-box">
          <h2>Controla tus apuestas con Danni Apuesta</h2>
          <p>
            Registra tus picks, analiza tu ROI, cuida tu bankroll y descubre qué estrategias te funcionan de verdad. Todo gratis y en un solo lugar.
          </p>
          <a class="cta-button" href="{BASE_URL}">USAR DANNI APUESTA GRATIS →</a>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>© 2026 <a href="{BASE_URL}">Danni Apuesta!</a> — Tracker gratuito de apuestas deportivas</p>
      <div class="footer-links">
        <a href="{BASE_URL}/blog/">Blog</a>
        <a href="{BASE_URL}/privacidad/">Privacidad</a>
        <a href="{BASE_URL}/terminos/">Términos</a>
        <a href="{BASE_URL}/contacto/">Contacto</a>
      </div>
      <p style="margin-top:10px;">Juega con responsabilidad. Las apuestas deportivas pueden generar adicción. +18.</p>
    </div>
  </footer>
</body>
</html>
"""
    INDEX_FILE.write_text(full_html, encoding="utf-8")


def build_sitemap(posts):
    extra_urls = [
        (f"{BASE_URL}/", datetime.utcnow().strftime("%Y-%m-%d")),
        (f"{BASE_URL}/blog/", datetime.utcnow().strftime("%Y-%m-%d")),
        (f"{BASE_URL}/privacidad/", datetime.utcnow().strftime("%Y-%m-%d")),
        (f"{BASE_URL}/terminos/", datetime.utcnow().strftime("%Y-%m-%d")),
        (f"{BASE_URL}/contacto/", datetime.utcnow().strftime("%Y-%m-%d")),
    ]

    items = []

    for url, lastmod in extra_urls:
        items.append(f"""  <url>
    <loc>{html.escape(url)}</loc>
    <lastmod>{lastmod}</lastmod>
  </url>""")

    for post in posts:
        items.append(f"""  <url>
    <loc>{html.escape(post["url"])}</loc>
    <lastmod>{post["lastmod"]}</lastmod>
  </url>""")

    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
""" + "\n\n".join(items) + """
</urlset>
"""

    SITEMAP_FILE.write_text(xml, encoding="utf-8")


def main():
    posts = discover_posts()
    build_blog_index(posts)
    build_sitemap(posts)
    print(f"Generated {len(posts)} blog posts.")


if __name__ == "__main__":
    main()
