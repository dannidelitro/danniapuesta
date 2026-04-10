import sys
import codecs

file_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\index.html"

with codecs.open(file_path, "r", "utf-8") as f:
    html = f.read()

new_cards = """
          <a class="post-card" href="/blog/estrategia-david-vs-goliat-favoritos/">
            <div class="post-top">
              <span class="post-tag">Guía táctica</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>El Factor Goliat: Cómo Rentabilizar Apostando a Grandes Favoritos</h3>
            <p>Estrategia matemática profunda para comprender el diferencial neto (xGD) y capitalizar con asimetrías extremas en duelos dispares de las Grandes Ligas europeas.</p>
            <div class="post-meta">
              <span>⏱ 7 min</span>
              <span>📌 Estadística</span>
            </div>
          </a>

          <a class="post-card" href="/blog/defensas-rotas-estrategia-over-goles/">
            <div class="post-top">
              <span class="post-tag">Análisis</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Defensas Rotas: El Secreto Definitivo para el Mercado de Over Goles</h3>
            <p>Rompe con el engaño de los delanteros élite y domina el análisis de zagas kamikazes y porteros vulnerables para multiplicar tu Win Rate absoluto en goles totales.</p>
            <div class="post-meta">
              <span>⏱ 8 min</span>
              <span>📌 Value Bet</span>
            </div>
          </a>

          <a class="post-card" href="/blog/carrileros-bandas-value-corners/">
            <div class="post-top">
              <span class="post-tag">Córners</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Carrileros y Córners: Identificando Ligas Abiertas Periféricas</h3>
            <p>Examen riguroso táctico para explotar el mercado de Tiros de Esquina a través del desborde incesante (Wing Play) y la desesperación de los defensas centrales limitados.</p>
            <div class="post-meta">
              <span>⏱ 7 min</span>
              <span>📌 Córners</span>
            </div>
          </a>

          <a class="post-card" href="/blog/tensión-derbis-analisis-booking-points/">
            <div class="post-top">
              <span class="post-tag">Estrategia</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Apuestas Disciplinarias: El Psicoanálisis de los Derbis (Tarjetas)</h3>
            <p>Domina y exprime agresivamente el circuito periférico prediciendo los cartones amarillos mediante la tolerancia de los arbitrajes severos y la rivalidad de descenso.</p>
            <div class="post-meta">
              <span>⏱ 8 min</span>
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
