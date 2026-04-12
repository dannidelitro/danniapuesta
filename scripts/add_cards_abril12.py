import sys
import codecs

file_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\index.html"

with codecs.open(file_path, "r", "utf-8") as f:
    html = f.read()

new_cards = """
          <a class="post-card" href="/blog/tendencias-largas-rachas-over-goles/">
            <div class="post-top">
              <span class="post-tag">Guía táctica</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>La Ley de los Grandes Números: Rastreando Rachas Largas</h3>
            <p>Estrategia algorítmica para evitar la Falacia del Apostador y colgarse del tren imparable en anomalías goleadoras extremas de ligas medias.</p>
            <div class="post-meta">
              <span>⏱ 7 min</span>
              <span>📌 Estadística</span>
            </div>
          </a>

          <a class="post-card" href="/blog/Corners-asedio-bloque-bajo/">
            <div class="post-top">
              <span class="post-tag">Córners</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>El Asedio al Bloque Bajo: Análisis Geométrico en Córners</h3>
            <p>La anatomía matemática de las líneas y despejes periféricos asfixiantes ejecutada para destrozar formaciones defensivas lúgubres del Underdog.</p>
            <div class="post-meta">
              <span>⏱ 8 min</span>
              <span>📌 Táctica</span>
            </div>
          </a>

          <a class="post-card" href="/blog/analitica-severidad-juez-tarjetas/">
            <div class="post-top">
              <span class="post-tag">Estrategia</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>La Importancia del Perfil Arbitral: Cómo el Juez Manda</h3>
            <p>Psicoanálisis táctico de la severidad (Severity Rating) y de cómo la procedencia de la autoridad rige irónicamente sobre las Inversiones Disciplinarias.</p>
            <div class="post-meta">
              <span>⏱ 8 min</span>
              <span>📌 Ranking Árbitros</span>
            </div>
          </a>

          <a class="post-card" href="/blog/xg-esperados-delanteros-elite/">
            <div class="post-top">
              <span class="post-tag">Value Bet</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Métricas Avanzadas (xG xA): Transformando Atacantes en Ganancias</h3>
            <p>Descifrando algoritmos modernos de Goles Esperados Combinados (xG) en colosos ofensivos y Outliers morfológicos en competiciones top absolutas.</p>
            <div class="post-meta">
              <span>⏱ 7 min</span>
              <span>📌 Estadística Pro</span>
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
