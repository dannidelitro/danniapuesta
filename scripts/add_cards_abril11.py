import sys
import codecs

file_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\index.html"

with codecs.open(file_path, "r", "utf-8") as f:
    html = f.read()

new_cards = """
          <a class="post-card" href="/blog/derbis-desiguales-estrategia/">
            <div class="post-top">
              <span class="post-tag">Derbis locales</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Derbis Desiguales: Estrategia de Apuestas en Clásicos de Ciudad</h3>
            <p>Análisis exhaustivo del espejismo psíquico en el que el fervor urbano destroza planteamientos tácticos generando masacres disciplinarias y de gol que el Apostador Inteligente debe capitalizar.</p>
            <div class="post-meta">
              <span>⏱ 7 min</span>
              <span>📌 Estadística</span>
            </div>
          </a>

          <a class="post-card" href="/blog/ligas-franquicia-sin-descenso/">
            <div class="post-top">
              <span class="post-tag">Estadísticas</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Ligas sin Descenso: La Mina de Oro para el Mercado Over Goles</h3>
            <p>Una inmersión paramétrica de cómo las franquicias corporativas en torneos sin pánico a descender desprotegen sus defensas e inflan las métricas mundiales del Mercado de Goles.</p>
            <div class="post-meta">
              <span>⏱ 8 min</span>
              <span>📌 Análisis</span>
            </div>
          </a>

          <a class="post-card" href="/blog/analitica-corners-tres-centrales/">
            <div class="post-top">
              <span class="post-tag">Córners</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Analítica de Córners Contra Sistemas de Tres Centrales (3-5-2)</h3>
            <p>Refugio oculto del apostador esquinero para doblegar y exprimir algorítmicamente a los sólidos candados defensivos valiéndose en la desesperación lateral de la estadística periférica.</p>
            <div class="post-meta">
              <span>⏱ 8 min</span>
              <span>📌 Value Bet</span>
            </div>
          </a>

          <a class="post-card" href="/blog/paradoja-posesion-btts/">
            <div class="post-top">
              <span class="post-tag">Estrategia</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>La Paradoja de la Posesión: Por Qué los Gigantes Regalan Goles</h3>
            <p>La fisura maestra psicológica y topográfica detrás del incomprensible colapso de porterías gélidas para atrapar cuotas doradas infalibles en el mercado de Ambos Equipos Anotan.</p>
            <div class="post-meta">
              <span>⏱ 7 min</span>
              <span>📌 Estrategia</span>
            </div>
          </a>
"""

# Insert right after <div class="posts-grid">
target = '<div class="posts-grid">'
if target in html:
    html = html.replace(target, target + "\n" + new_cards)
    
    with codecs.open(file_path, "w", "utf-8") as f:
        f.write(html)
    print("Success cards added")
else:
    print("Error: Target not found")
