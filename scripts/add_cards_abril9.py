import sys
import codecs

file_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\index.html"

with codecs.open(file_path, "r", "utf-8") as f:
    html = f.read()

new_cards = """
          <a class="post-card" href="/blog/guia-ventaja-local-home-advantage/">
            <div class="post-top">
              <span class="post-tag">Guía táctica</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>La Fortaleza Local: El Análisis Matemático Oculto en Apuestas</h3>
            <p>Descubre las métricas analíticas profundas para dominar el mercado del Equipo Local utilizando la fisilogía y ventaja de las grandes ligas como refugio de Value Bet diario.</p>
            <div class="post-meta">
              <span>⏱ 7 min</span>
              <span>📌 Estadística</span>
            </div>
          </a>

          <a class="post-card" href="/blog/estrategia-maestra-mercado-corners/">
            <div class="post-top">
              <span class="post-tag">Córners</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Estrategia Maestra: El Mercado de Córners y el Desborde</h3>
            <p>La matemática estadística inquebrantable tras los saques perimetrales y transiciones ofensivas para ganar en tiros de esquina evadiendo el engaño de la posesión pasiva.</p>
            <div class="post-meta">
              <span>⏱ 8 min</span>
              <span>📌 Táctica Oculta</span>
            </div>
          </a>

          <a class="post-card" href="/blog/matematica-btts-ambos-anotan/">
            <div class="post-top">
              <span class="post-tag">Estadísticas</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>El Mercado BTTS y la Matemática Oculta de las Transiciones</h3>
            <p>Comprender la rentabilidad implícita en estructuras veloces vs asfixia pasiva y aprender a apostar al Ambos Equipos Anotarán de forma profesional evadiendo falsos favoritos.</p>
            <div class="post-meta">
              <span>⏱ 7 min</span>
              <span>📌 Análisis</span>
            </div>
          </a>

          <a class="post-card" href="/blog/oro-oculto-ligas-secundarias/">
            <div class="post-top">
              <span class="post-tag">Estrategia</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Value Bets Asimétricos: La Verdadera Fortuna de las Ligas Menores</h3>
            <p>Por qué los apostadores millonarios jamás arriesgan la bolsa en partidos populares de élite y buscan minas de oro ocultas en torneos periféricos donde el algoritmo falla habitualmente.</p>
            <div class="post-meta">
              <span>⏱ 6 min</span>
              <span>📌 Dinero Inteligente</span>
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
