import sys
import codecs

file_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\index.html"

with codecs.open(file_path, "r", "utf-8") as f:
    html = f.read()

new_cards = """
          <a class="post-card" href="/blog/estrategia-over-1-5-goles/">
            <div class="post-top">
              <span class="post-tag">Guía básica</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Por qué Apostar al Over 1.5 es la Inversión Más Segura</h3>
            <p>Descubre por qué la estrategia analítica del Over 1.5 garantiza éxito comprobado mitigando las volatilidades en fútbol moderno acudiendo directamente al xG (Expected Goals).</p>
            <div class="post-meta">
              <span>⏱ 5 min</span>
              <span>📌 Estadística</span>
            </div>
          </a>

          <a class="post-card" href="/blog/apuestas-futbol-factor-clima-altitud/">
            <div class="post-top">
              <span class="post-tag">Estadísticas</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Fisiología y Altitud: El Factor Invisible en Apuestas</h3>
            <p>Controla la matemática táctica del quiebre físico que sufren los equipos forasteros en la montaña y únete al mercado de apostadores expertos aprovechando las grietas del 2do tiempo.</p>
            <div class="post-meta">
              <span>⏱ 4 min</span>
              <span>📌 Fisiología</span>
            </div>
          </a>

          <a class="post-card" href="/blog/booking-points-analisis-tarjetas/">
            <div class="post-top">
              <span class="post-tag">Estrategia</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Ganar con Booking Points: La Táctica de las Tarjetas</h3>
            <p>Aprende a analizar perfiles arbitrales severos e ignora definitivamente el marcador final del partido capitalizando la frustración deportiva de torneos eliminatorios en Booking Points.</p>
            <div class="post-meta">
              <span>⏱ 6 min</span>
              <span>📌 Ranking Árbitros</span>
            </div>
          </a>

          <a class="post-card" href="/blog/corners-mercado-valor-secreto/">
            <div class="post-top">
              <span class="post-tag">Córners</span>
              <span class="badge-new">Nuevo</span>
            </div>
            <h3>Córners: El Paraíso Estadístico Oculto</h3>
            <p>El análisis inquebrantable para extraer Value Bet mediante despejes perimetrales descubriendo el ecosistema de las ligas y equipos asimétricos expertos en centros.</p>
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
    
    # Optionally remove the "Nuevo" strict tag from older ones just to keep realism, but omitting to save complexity.
    
    with codecs.open(file_path, "w", "utf-8") as f:
        f.write(html)
    print("Success cards added")
else:
    print("Error: Target not found")
