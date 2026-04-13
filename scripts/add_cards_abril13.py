import codecs
import re

html_cards = """
  <!-- ABRIL 13 -->
  <a href="apuestas-ligas-filiales-jong-goles/" class="blog-card fade-in">
    <div class="bc-tag">Guía táctica</div>
    <div class="bc-content">
      <div class="bc-meta">13 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>Apuestas en Ligas Filiales (Jong): Minería del Futbol Ofensivo</h3>
      <p>Estrategia asiática secreta para obtener un asombroso Win-Rate mediante el mercado Goleador Over 1.5 analizando escuelas formativas holandesas.</p>
    </div>
  </a>

  <a href="clima-altura-gol-equipo-local/" class="blog-card fade-in">
    <div class="bc-tag">Estadística Pro</div>
    <div class="bc-content">
      <div class="bc-meta">13 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>El Factor Fortaleza: Rachas Locales y la Fisiología de la Altura</h3>
      <p>Aprovechando ventajas atmosféricas y agónicas para apostar científicamente al 'Gol de Equipo Local' y aniquilar falacias de estadios difíciles.</p>
    </div>
  </a>

  <a href="derbis-este-europa-tarjetas-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Ranking Árbitros</div>
    <div class="bc-content">
      <div class="bc-meta">13 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Derbis Balcánicos del Este: El Paraíso de Apuestas por Tarjetas</h3>
      <p>Beneficiándose financieramente de rivalidades históricas de choque y del comportamiento forense sancionador bajo árbitros condicionados de alta letalidad.</p>
    </div>
  </a>

  <a href="corners-asimetricos-individual-equipo/" class="blog-card fade-in">
    <div class="bc-tag">Value Bet</div>
    <div class="bc-content">
      <div class="bc-meta">13 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>Córners Asimétricos o de Equipo: Evadiendo a los Rivales Inútiles</h3>
      <p>Aísla el XG perimetral del gran dominador dictaminando la destrucción y despejes constantes hacia el córner usando la táctica del Team Corner Individual.</p>
    </div>
  </a>
"""

path = r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\index.html"
with codecs.open(path, "r", "utf-8") as f:
    text = f.read()

pattern = r'(<div class="blog-grid">)'
# Inject immediately after <div class="blog-grid">
new_text = re.sub(pattern, r'\1\n' + html_cards, text, count=1)

with codecs.open(path, "w", "utf-8") as f:
    f.write(new_text)

print("Updated blog/index.html")
