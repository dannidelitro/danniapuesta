import os
import re
import json

articles = [
    {
        "slug": "filtro-dixon-coles-apuestas-probabilidades",
        "title": "Filtro Dixon-Coles: Ajustando probabilidades en partidos cerrados",
        "desc": "Descubre cómo el modelo Dixon-Coles penaliza rachas goleadoras y ajusta el Valor Esperado en partidos de alta fricción defensiva.",
        "h1": "Dixon-Coles: La Llave de los Partidos Cerrados",
        "body": """
        <p>En el mundo del modelamiento predictivo, asumir que los promedios de goles se comportan de manera lineal es uno de los errores más comunes. El <strong>Filtro de Dixon-Coles</strong> nace precisamente para corregir esta desviación, especialmente en encuentros marcados por una estricta rigidez táctica.</p>
        <h2>El Peligro de las Rachas Artificiales</h2>
        <p>A menudo, un equipo puede llegar a un encuentro promediando más de 2 goles por partido debido a goleadas puntuales contra rivales débiles. Sin el ajuste de Dixon-Coles, los modelos básicos proyectarían erróneamente un partido abierto. Este filtro aplica una penalización matemática que reduce la probabilidad de un <em>Ambos Equipos Marcan (BTTS)</em> cuando se cruzan frente a un esquema defensivo sólido.</p>
        <h2>Ajuste de Correlación de Bajos Goles</h2>
        <p>La verdadera magia de Dixon-Coles reside en ajustar las probabilidades de marcadores como 0-0, 1-0 o 0-1. Entiende que si un equipo no logra abrir el marcador temprano, la tendencia a arriesgar disminuye exponencialmente, incrementando el valor del mercado <em>Under (Menos de 2.5 goles)</em>.</p>
        <h2>Aplicación Práctica en Ligas Duras</h2>
        <p>Este modelo es extraordinariamente rentable en ligas de alta fricción (como la Premier Division de Irlanda o el fútbol sudamericano). Invertir respaldado por Dixon-Coles significa apostar con el escudo del rigor matemático.</p>
        """
    },
    {
        "slug": "tendencias-goles-ligas-escandinavas-allsvenskan-eliteserien",
        "title": "Apuestas en Ligas Escandinavas: Tendencias de Goles y xG",
        "desc": "Análisis de Goles Esperados (xG) y tendencias ofensivas en torneos escandinavos como la Allsvenskan y la Eliteserien.",
        "h1": "Ligas Escandinavas: El Paraíso del BTTS y el Over",
        "body": """
        <p>Las competiciones nórdicas como la <strong>Allsvenskan</strong> sueca y la <strong>Eliteserien</strong> noruega presentan un ecosistema fascinante para el inversor deportivo. Su calendario y vocación ofensiva generan tendencias de goles (xG) que desafían las medias del resto de Europa.</p>
        <h2>La Naturaleza Ofensiva Nórdica</h2>
        <p>A diferencia de ligas latinas, el fútbol escandinavo prioriza las transiciones rápidas y el juego por las bandas. Esto eleva drásticamente el porcentaje de éxito en los mercados de <em>Ambos Equipos Marcan (BTTS)</em> y <em>Over 2.5 Goles</em>.</p>
        <h2>Goles Esperados (xG) y Superficies</h2>
        <p>El uso extensivo de césped artificial acelera la circulación del balón, lo que infla los Goles Esperados de los locales. Apostar al BTTS en estadios sintéticos suele arrojar un <strong>Valor Esperado (EV+)</strong> muy consistente.</p>
        <h2>Identificando Defensas Endebles</h2>
        <p>El contraste es brutal: los equipos de baja tabla sufren de desorden defensivo estructural, encajando gol en casi todas sus localías. Detectar estos agujeros estadísticos es el primer paso para capitalizar en Escandinavia.</p>
        """
    },
    {
        "slug": "estrategia-doble-oportunidad-equipos-crisis-defensiva",
        "title": "Doble Oportunidad: Apostar contra equipos en crisis",
        "desc": "Aprende a proteger tu inversión usando la Doble Oportunidad cuando te enfrentas a equipos locales con rachas negativas.",
        "h1": "La Doble Oportunidad: Resguardo Matemático Total",
        "body": """
        <p>Una de las estrategias de mitigación de riesgo más infravaloradas es el mercado de <strong>Doble Oportunidad (1X / X2)</strong>. Su poder contra la varianza se hace evidente al operar contra equipos sumidos en crisis defensivas crónicas.</p>
        <h2>Aislando la Varianza del Empate</h2>
        <p>Apostar a la victoria seca de un visitante acarrea el peligro de un empate fortuito. La Doble Oportunidad X2 absorbe el 66.6% de los resultados posibles, elevando la tasa de éxito a largo plazo.</p>
        <h2>Identificando la Crisis Estructural</h2>
        <p>¿Cuándo usarla? Cuando el equipo local acumula una racha de partidos encajando goles constantemente. Si el sistema defensivo del local está roto, las probabilidades de que gane sin encajar caen radicalmente.</p>
        <h2>Rentabilidad y Apuestas Combinadas</h2>
        <p>Seleccionar cuotas de Doble Oportunidad es la base perfecta para construir apuestas múltiples o combinadas, generando un escudo estadístico casi inquebrantable.</p>
        """
    },
    {
        "slug": "mercado-corners-analisis-ataque-bandas",
        "title": "Mercado de Córners: Identificando valor en el juego por bandas",
        "desc": "Guía táctica para leer partidos de alto flujo de bandas y proyectar ganancias consistentes en el mercado de saques de esquina.",
        "h1": "Mercado de Córners: La Mina de Oro del Juego Exterior",
        "body": """
        <p>La predicción de goles está plagada de varianza. Sin embargo, el <strong>mercado de Córners (Saques de Esquina)</strong> ofrece un flujo de datos mucho más predecible, directamente ligado al esquema táctico de los equipos.</p>
        <h2>El ADN de un Partido Over Córners</h2>
        <p>Los equipos que basan su ofensiva en extremos puros y laterales de amplio recorrido son imanes para los saques de esquina. El balón viaja a la línea de fondo, forzando despejes continuos.</p>
        <h2>Evadiendo la Posesión Estéril</h2>
        <p>Los equipos que monopolizan el balón por el centro mediante pases cortos producen muy pocos córners. El verdadero <strong>Valor Esperado (EV+)</strong> se halla en duelos de ida y vuelta.</p>
        <h2>El Factor del Marcador Adverso</h2>
        <p>El asedio total de un favorito perdiendo en casa incrementa la frecuencia de saques de esquina en un 40%. Saber identificar estos escenarios separa al aficionado del inversor profesional.</p>
        """
    },
    {
        "slug": "valor-esperado-ev-rentabilidad-mercados-btts",
        "title": "Valor Esperado (EV+): Rentabilidad real en mercados BTTS",
        "desc": "Comprende el concepto matemático de Valor Esperado Positivo aplicado al mercado de Ambos Equipos Marcan.",
        "h1": "Valor Esperado (EV+): La Base del Trading Deportivo",
        "body": """
        <p>La diferencia fundamental entre un apostador recreacional y un inversor cuantitativo es el dominio absoluto del concepto de <strong>Valor Esperado (EV)</strong>.</p>
        <h2>La Fórmula del Éxito</h2>
        <p>El EV+ se calcula con una simple ecuación: <code>EV = (Probabilidad Real × Cuota) - 1</code>. Un modelo estadístico cruza métricas como Goles Esperados (xG) para establecer esta probabilidad real, desnuda de emociones.</p>
        <h2>Ignorando la Intuición</h2>
        <p>El mercado infla cuotas basándose en popularidad o rachas engañosas. Detectar cuando una casa de apuestas subestima la probabilidad real es la base de las apuestas inteligentes.</p>
        <h2>El Mercado BTTS</h2>
        <p>Encontrar asimetrías entre la cuota ofrecida y el poderío ofensivo real es la verdadera clave para generar un bankroll sostenible a largo plazo en el mercado de Ambos Anotan.</p>
        """
    },
    {
        "slug": "futbol-islandes-over-de-goles-apuestas",
        "title": "Fútbol Islandés: El paraíso estadístico del Over de Goles",
        "desc": "Por qué la liga de Islandia (Besta deildin) registra promedios de anotación brutales y cómo sacar partido del over 2.5 goles.",
        "h1": "Fútbol Islandés: El Festín de los Goles",
        "body": """
        <p>Dentro del mapa europeo de apuestas, la <strong>Besta deildin karla</strong> (primera división de Islandia) brilla con luz propia como un ecosistema donde el gol no es la excepción, sino la regla.</p>
        <h2>El Componente Táctico Despreocupado</h2>
        <p>El fútbol en Islandia a menudo adolece del rigor táctico defensivo que asfixia a otras ligas de mayor renombre. Las estructuras de los equipos suelen ser hiperofensivas, con líneas adelantadas que dejan inmensos espacios a la espalda de los defensores.</p>
        <h2>Cifras Escandalosas (BTTS del 100%)</h2>
        <p>Es común encontrar equipos como el KR Reykjavík que pueden registrar tendencias perfectas de <em>Ambos Equipos Marcan (BTTS)</em> a lo largo de varias jornadas. Cuando combinamos un equipo que promedia más de 3 goles a favor con uno que encaja más de 2 por partido, el modelo matemático casi garantiza el Over 2.5.</p>
        <h2>El Valor del Over en Cuotas Ajustadas</h2>
        <p>Aunque las casas de apuestas saben que habrá goles y castigan las cuotas, el volumen de anotación es tan alto que el mercado de <em>Más de 1.5 goles</em> en la primera mitad, o líneas alternativas (Over 3.5), siguen ofreciendo un <strong>Valor Esperado (EV) abismalmente positivo</strong>.</p>
        """
    },
    {
        "slug": "fortalezas-europa-del-este-apuestas-locales",
        "title": "Fortalezas Inexpugnables: El dominio local en Europa del Este",
        "desc": "Análisis táctico y estadístico de por qué los equipos punteros de Europa del Este (Bosnia, Serbia, Croacia) son casi imbatibles en casa.",
        "h1": "Europa del Este: El Resguardo de las Localías",
        "body": """
        <p>Las ligas de Europa del Este, como la Premijer Liga de Bosnia o la Superliga Serbia, esconden uno de los secretos a voces más rentables del trading deportivo: <strong>el peso desmesurado de la localía</strong>.</p>
        <h2>Condiciones Hostiles y Bloques Rocosos</h2>
        <p>Jugar de visitante en estas ligas conlleva lidiar con viajes complejos, estadios volcánicos y campos de juego que a menudo benefician el juego de destrucción. Equipos punteros (como el Borac Banja Luka o Estrella Roja) construyen bloques defensivos monumentales en su feudo.</p>
        <h2>Estadísticas de Imbatibilidad</h2>
        <p>Es estadísticamente recurrente que los líderes de estos campeonatos registren más de un 80% de victorias locales, con altísimas tasas de valla invicta (portería a cero). Las brechas de talento y presupuesto entre los líderes y los equipos de baja tabla son abismales.</p>
        <h2>Mercados Rentables</h2>
        <p>Apostar a la victoria local simple a veces no tiene cuota, pero utilizar mercados combinados como <em>Gana Local + Más de 0.5 goles</em>, o apostar a que el equipo visitante no anota, son estrategias probadas que minimizan la varianza técnica.</p>
        """
    }
]

def generate_article_html(art, all_articles):
    # Generar JSON-LD
    json_ld = {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": art["title"],
      "description": art["desc"],
      "author": {
        "@type": "Organization",
        "name": "Danni Apuesta"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Danni Apuesta",
        "logo": {
          "@type": "ImageObject",
          "url": "https://danniapuesta.com/logo.png"
        }
      },
      "url": f"https://danniapuesta.com/blog/{art['slug']}/"
    }

    # Seleccionar 3 articulos relacionados (diferentes al actual)
    related = [a for a in all_articles if a['slug'] != art['slug']][:3]
    related_html = ""
    for r in related:
        related_html += f"""
        <a href="/blog/{r['slug']}/" class="related-card">
            <h4>{r['title']}</h4>
            <p>{r['desc'][:80]}...</p>
        </a>"""

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{art['desc']}" />
  
  <!-- Open Graph Meta Tags -->
  <meta property="og:title" content="{art['title']} | Danni Apuesta" />
  <meta property="og:description" content="{art['desc']}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://danniapuesta.com/blog/{art['slug']}/" />
  <meta property="og:site_name" content="Danni Apuesta" />
  <meta property="og:image" content="https://danniapuesta.com/hero_bg2.png" />
  
  <title>{art['title']} | Danni Apuesta</title>
  
  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
    {json.dumps(json_ld, ensure_ascii=False, indent=2)}
  </script>

  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;700;900&display=swap" rel="stylesheet">
  <style>
    :root {{ --verde: #00e676; --rojo: #ff1744; --amarillo: #ffd600; --bg: #05080c; --card: rgba(18,24,35,0.65); --border: rgba(255,255,255,0.08); --text: #e8f0fe; --muted: #7d98bd; --accent: #00d0f7; }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'DM Sans', sans-serif; background: var(--bg) url('../../dash_bg.png') center/cover no-repeat fixed; color: var(--text); line-height: 1.7; position: relative; }}
    body::before {{ content: ''; position: fixed; inset: 0; background: radial-gradient(circle at 15% 50%, rgba(0, 180, 216, 0.12), transparent 40%), radial-gradient(circle at 85% 30%, rgba(0, 230, 118, 0.08), transparent 40%), rgba(5,8,12,0.88); z-index: -2; }}
    a {{ text-decoration: none; color: inherit; }}
    header {{ background: rgba(10,15,22,0.85); backdrop-filter: blur(15px); border-bottom: 1px solid var(--border); padding: 1rem 2rem; display: flex; align-items: center; justify-content: space-between; position: sticky; top: 0; z-index: 100; }}
    .logo {{ font-family: 'Bebas Neue'; font-size: 2rem; color: #fff; letter-spacing: 2px; text-shadow: 0 0 10px rgba(0,208,247,0.5); }}
    .back-btn {{ font-size: 0.9rem; color: var(--accent); border: 1px solid var(--accent); padding: 5px 15px; border-radius: 20px; transition: all 0.3s; }}
    .back-btn:hover {{ background: var(--accent); color: #000; box-shadow: 0 0 15px var(--accent); }}
    
    .article-container {{ max-width: 800px; margin: 3rem auto; padding: 2.5rem; background: var(--card); backdrop-filter: blur(16px); border: 1px solid var(--border); border-radius: 24px; box-shadow: 0 15px 40px rgba(0,0,0,0.3); }}
    .article-header {{ text-align: center; margin-bottom: 3rem; }}
    .article-tag {{ background: rgba(0,208,247,0.1); color: var(--accent); padding: 4px 12px; border-radius: 4px; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; display: inline-block; margin-bottom: 1rem; border: 1px solid rgba(0,208,247,0.3); }}
    h1 {{ font-family: 'Bebas Neue'; font-size: 3.5rem; line-height: 1.1; margin-bottom: 1rem; letter-spacing: 1px; text-shadow: 0 4px 10px rgba(0,0,0,0.5); }}
    .article-meta {{ color: var(--muted); font-size: 0.9rem; }}
    
    .article-content h2 {{ font-family: 'Bebas Neue'; font-size: 2.2rem; color: var(--accent); margin: 2.5rem 0 1rem; letter-spacing: 1px; border-bottom: 1px solid var(--border); padding-bottom: 10px; }}
    .article-content p {{ margin-bottom: 1.5rem; font-size: 1.05rem; color: #a5b9d4; }}
    .article-content ul {{ margin: 0 0 1.5rem 2rem; color: #a5b9d4; }}
    .article-content li {{ margin-bottom: 0.5rem; }}
    .article-content strong {{ color: #fff; background: rgba(255,255,255,0.05); padding: 0 4px; border-radius: 4px; }}
    
    .cta-box {{ background: linear-gradient(145deg, rgba(0,230,118,0.1), rgba(0,0,0,0.5)); border: 1px solid rgba(0,230,118,0.3); padding: 2rem; border-radius: 16px; text-align: center; margin-top: 3rem; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }}
    .cta-box h3 {{ font-family: 'Bebas Neue'; font-size: 2rem; margin-bottom: 1rem; color: #fff; letter-spacing: 1px; }}
    .cta-btn {{ display: inline-block; background: var(--verde); color: #000; font-weight: 900; padding: 15px 35px; border-radius: 30px; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 2px; transition: all 0.3s; box-shadow: 0 10px 25px rgba(0,230,118,0.4); }}
    .cta-btn:hover {{ transform: translateY(-3px) scale(1.05); box-shadow: 0 15px 35px rgba(0,230,118,0.6); }}
    
    .related-section {{ margin-top: 4rem; border-top: 1px solid var(--border); padding-top: 2rem; }}
    .related-section h3 {{ font-family: 'Bebas Neue'; font-size: 2rem; color: #fff; margin-bottom: 1.5rem; letter-spacing: 1px; }}
    .related-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; }}
    .related-card {{ background: rgba(0,0,0,0.3); border: 1px solid var(--border); padding: 1.5rem; border-radius: 12px; transition: all 0.3s; display: block; }}
    .related-card:hover {{ transform: translateY(-5px); border-color: var(--accent); background: rgba(0,208,247,0.05); }}
    .related-card h4 {{ color: var(--accent); font-family: 'DM Sans'; font-size: 1rem; margin-bottom: 0.5rem; }}
    .related-card p {{ color: var(--muted); font-size: 0.85rem; line-height: 1.4; }}

    @media(max-width: 768px) {{
      .article-container {{ margin: 1rem; padding: 1.5rem; }}
      h1 {{ font-size: 2.5rem; }}
      .article-content h2 {{ font-size: 1.8rem; }}
    }}
  </style>
</head>
<body>
  <header>
    <a href="/" class="logo">DANNI APUESTA</a>
    <a href="/blog/" class="back-btn">Volver al Blog</a>
  </header>
  
  <main class="article-container">
    <div class="article-header">
      <span class="article-tag">Teoría VIP</span>
      <h1>{art['h1']}</h1>
      <div class="article-meta">Por Danni Apuesta | Análisis Cuantitativo</div>
    </div>
    
    <div class="article-content">
      {art['body']}
    </div>
    
    <div class="cta-box">
      <h3>¿Listo para aplicar estas estrategias?</h3>
      <p style="margin-bottom: 1.5rem; color: #a5b9d4;">Aprovecha el bono VIP y comienza a rentabilizar tu conocimiento en ligas de alta fricción.</p>
      <a href="javascript:void(0)" onclick="window.goNovibet()" class="cta-btn">RECLAMAR BONO VIP</a>
    </div>

    <div class="related-section">
      <h3>Sigue aprendiendo</h3>
      <div class="related-grid">
        {related_html}
      </div>
    </div>
  </main>
  
  <script>
    window.goNovibet = async function() {{
      window.open('https://pro.cl.novibet.com/apuestas-deportivas/chilean200/?btag=2007720_8533518657&utm_source=2007720_&utm_medium=affiliate&utm_campaign=CHILEAN200');
    }};
  </script>
</body>
</html>"""

base_dir = r"..\blog"
os.makedirs(base_dir, exist_ok=True)

# Generate or update all 7 articles
for art in articles:
    slug_dir = os.path.join(base_dir, art['slug'])
    os.makedirs(slug_dir, exist_ok=True)
    
    html_content = generate_article_html(art, articles)
    
    file_path = os.path.join(slug_dir, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Updated/Created article: {art['slug']}")

# Update blog/index.html to include all 7 links cleanly
blog_index_path = os.path.join(base_dir, "index.html")
with open(blog_index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

# Replace the entire posts grid with the newly generated list
new_links = []
for art in articles:
    link_html = f"""          <a class="post-card" href="/blog/{art['slug']}/">
            <div class="post-top">
              <span class="post-tag">Teoría VIP</span>
              <span class="post-date">Evergreen</span>
            </div>
            <h3 class="post-title">{art['title']}</h3>
            <p class="post-excerpt">{art['desc']}</p>
          </a>"""
    new_links.append(link_html)

grid_pattern = r'<div class="posts-grid">.*?</div>\s*</main>'
replacement = '<div class="posts-grid">\n' + "\n".join(new_links) + '\n        </div>\n  </main>'
idx_content = re.sub(grid_pattern, replacement, idx_content, flags=re.DOTALL)

with open(blog_index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("Blog index updated with all 7 Evergreen articles.")
