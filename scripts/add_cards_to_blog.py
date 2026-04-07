import sys
import codecs

file_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\index.html"

with codecs.open(file_path, "r", "utf-8") as f:
    html = f.read()

new_cards = """
          <a class="post-card" href="/blog/analisis-xg-real-madrid-bayern/">
            <div class="post-top">
              <span class="post-tag">Champions League</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>El Valor del xG en Champions: Real Madrid vs Bayern</h3>
            <p>Análisis matemático y estadístico (xG) para exprimir rentabilidad ofensiva en la UCL apoyándose en el volumen ofensivo abrumador y los modelos bivariados.</p>
            <div class="post-meta">
              <span>⏱ 5 min</span>
              <span>📌 Artículo</span>
            </div>
          </a>

          <a class="post-card" href="/blog/apuestas-altitud-always-ready/">
            <div class="post-top">
              <span class="post-tag">Guía táctica</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>El Factor Altura en Apuestas: El Caso Always Ready</h3>
            <p>Cómo la barrera de los 4.150 metros impone una deformación irreversible del modelo táctico visitante resultando en un 98% de probabilidad matemática pura para los goles locales.</p>
            <div class="post-meta">
              <span>⏱ 4 min</span>
              <span>📌 Táctica</span>
            </div>
          </a>

          <a class="post-card" href="/blog/mercado-tarjetas-sporting-arsenal/">
            <div class="post-top">
              <span class="post-tag">Estrategia</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Apostar en el Mercado de Tarjetas y Árbitros</h3>
            <p>Desglose analítico de Booking Points en eliminatorias tensiones. Rentabilidad y Closing Line Value superior al apostar en referís con perfiles disciplinarios estrictos.</p>
            <div class="post-meta">
              <span>⏱ 5 min</span>
              <span>📌 Estrategia</span>
            </div>
          </a>

          <a class="post-card" href="/blog/corners-btts-ligas-menores/">
            <div class="post-top">
              <span class="post-tag">Córners</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Extraer Value en Córners y BTTS: Torneos Menores</h3>
            <p>El oro oculto de Polonia y Gales para los inversores estadísticos de tiros de esquina y BTTS sin la volatilidad extrema ni los spreads ajustados de las grandes ligas europeas.</p>
            <div class="post-meta">
              <span>⏱ 4 min</span>
              <span>📌 Córners</span>
            </div>
          </a>
"""

# Insert right after <div class="posts-grid">
target = '<div class="posts-grid">'
if target in html:
    html = html.replace(target, target + "\n" + new_cards)
    with codecs.open(file_path, "w", "utf-8") as f:
        f.write(html)
    print("Success")
else:
    print("Error: Target not found")
