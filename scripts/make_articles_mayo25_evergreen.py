import os
import re

def generate_article_html(title, desc, h1, body_content, url_slug):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{desc}" />
  <title>{title} | Danni Apuesta</title>
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
      <span class="article-tag">Estrategia VIP</span>
      <h1>{h1}</h1>
      <div class="article-meta">Por Danni Apuesta | Teoría Cuantitativa</div>
    </div>
    
    <div class="article-content">
      {body_content}
    </div>
    
    <div class="cta-box">
      <h3>¿Listo para aplicar estas estrategias?</h3>
      <p style="margin-bottom: 1.5rem; color: #a5b9d4;">Aprovecha el bono VIP y comienza a rentabilizar tu conocimiento en ligas de alta fricción.</p>
      <a href="javascript:void(0)" onclick="window.goNovibet()" class="cta-btn">RECLAMAR BONO VIP</a>
    </div>
  </main>
  
  <script>
    window.goNovibet = async function() {{
      window.open('https://pro.cl.novibet.com/apuestas-deportivas/chilean200/?btag=2007720_8533518657&utm_source=2007720_&utm_medium=affiliate&utm_campaign=CHILEAN200');
    }};
  </script>
</body>
</html>"""

articles = [
    {
        "slug": "filtro-dixon-coles-apuestas-probabilidades",
        "title": "Filtro Dixon-Coles: Ajustando probabilidades en partidos cerrados",
        "desc": "Descubre cómo el modelo Dixon-Coles penaliza rachas goleadoras y ajusta el Valor Esperado en partidos de alta fricción defensiva.",
        "h1": "Dixon-Coles: La Llave de los Partidos Cerrados",
        "body": """
        <p>En el mundo del modelamiento predictivo, asumir que los promedios de goles se comportan de manera lineal es uno de los errores más comunes. El <strong>Filtro de Dixon-Coles</strong> nace precisamente para corregir esta desviación, especialmente en encuentros marcados por una estricta rigidez táctica.</p>
        
        <h2>El Peligro de las Rachas Artificiales</h2>
        <p>A menudo, un equipo puede llegar a un encuentro promediando más de 2 goles por partido debido a goleadas puntuales contra rivales débiles. Sin el ajuste de Dixon-Coles, los modelos básicos (como la distribución simple de Poisson) proyectarían erróneamente un partido abierto y de alta anotación. Este filtro aplica una penalización matemática que reduce la probabilidad de un <em>Ambos Equipos Marcan (BTTS)</em> cuando se cruzan frente a un esquema defensivo sólido.</p>
        
        <h2>Ajuste de Correlación de Bajos Goles</h2>
        <p>La verdadera magia de Dixon-Coles reside en ajustar las probabilidades de marcadores como 0-0, 1-0 o 0-1. Entiende que si un equipo no logra abrir el marcador temprano, la tendencia a arriesgar disminuye exponencialmente, incrementando el valor del mercado <em>Under (Menos de 2.5 goles)</em>.</p>
        
        <h2>Aplicación Práctica en Ligas Duras</h2>
        <p>Este modelo es extraordinariamente rentable en ligas de alta fricción (como la Premier Division de Irlanda o el fútbol sudamericano), donde el bloque bajo y la defensa en zona neutralizan el talento individual. Invertir respaldado por Dixon-Coles significa apostar con el escudo del rigor matemático.</p>
        """
    },
    {
        "slug": "tendencias-goles-ligas-escandinavas-allsvenskan-eliteserien",
        "title": "Apuestas en Ligas Escandinavas: Tendencias de Goles y xG",
        "desc": "Análisis de Goles Esperados (xG) y tendencias ofensivas en torneos escandinavos como la Allsvenskan y la Eliteserien.",
        "h1": "Ligas Escandinavas: El Paraíso del BTTS y el Over",
        "body": """
        <p>Las competiciones nórdicas como la <strong>Allsvenskan</strong> sueca y la <strong>Eliteserien</strong> noruega presentan un ecosistema fascinante para el inversor deportivo. Su calendario de primavera-otoño y la marcada vocación ofensiva de sus clubes generan tendencias de goles (xG) que desafían las medias del resto de Europa.</p>
        
        <h2>La Naturaleza Ofensiva Nórdica</h2>
        <p>A diferencia de ligas latinas más conservadoras, el fútbol escandinavo prioriza las transiciones rápidas y el juego por las bandas. Esto se traduce en un volumen altísimo de llegadas al área, elevando drásticamente el porcentaje de éxito en los mercados de <em>Ambos Equipos Marcan (BTTS)</em> y <em>Over 2.5 Goles</em>.</p>
        
        <h2>Goles Esperados (xG) y Superficies</h2>
        <p>Un factor crucial en estas ligas es el uso extensivo de césped artificial. Esta superficie acelera la circulación del balón y reduce los errores en pases cortos, lo que estadísticamente infla los Goles Esperados de los equipos locales. Apostar al BTTS en estadios sintéticos contra visitantes de élite suele arrojar un <strong>Valor Esperado (EV+)</strong> muy consistente.</p>
        
        <h2>Identificando Defensas Endebles</h2>
        <p>El contraste en estas ligas es brutal. Mientras que los ataques suelen ser efectivos, los equipos de media tabla y baja sufren de un desorden defensivo estructural (muchos clubes encajan gol en el 90-100% de sus localías). Detectar estos agujeros estadísticos es el primer paso para capitalizar en Escandinavia.</p>
        """
    },
    {
        "slug": "estrategia-doble-oportunidad-equipos-crisis-defensiva",
        "title": "Doble Oportunidad: Apostar contra equipos en crisis",
        "desc": "Aprende a proteger tu inversión usando la Doble Oportunidad cuando te enfrentas a equipos locales con rachas negativas.",
        "h1": "La Doble Oportunidad: Resguardo Matemático Total",
        "body": """
        <p>Una de las estrategias de mitigación de riesgo más infravaloradas en el trading deportivo es el mercado de <strong>Doble Oportunidad (1X / X2)</strong>. Su poder destructivo contra la varianza se hace especialmente evidente cuando se opera contra equipos sumidos en crisis defensivas crónicas.</p>
        
        <h2>Aislando la Varianza del Empate</h2>
        <p>Apostar a la victoria seca de un visitante siempre acarrea el peligro de un empate fortuito (un gol tardío, una expulsión injusta). La Doble Oportunidad X2 absorbe el 66.6% de los resultados posibles. Aunque la cuota disminuye, la tasa de éxito a largo plazo compensa sobradamente esta merma.</p>
        
        <h2>Identificando la Crisis Estructural</h2>
        <p>¿Cuándo es matemáticamente óptimo usar esta estrategia? Cuando el equipo local acumula una racha de partidos (5 o más) encajando goles constantemente. Si el sistema defensivo del local está roto, las probabilidades de que logre una victoria sin encajar caen por debajo del 15%.</p>
        
        <h2>Rentabilidad y Apuestas Combinadas</h2>
        <p>Seleccionar cuotas de Doble Oportunidad (que suelen rondar entre 1.25 y 1.40) es la base perfecta para construir apuestas múltiples o combinadas. Mezclar la superioridad táctica de un visitante con la inoperancia defensiva del local genera un escudo estadístico casi inquebrantable.</p>
        """
    },
    {
        "slug": "mercado-corners-analisis-ataque-bandas",
        "title": "Mercado de Córners: Identificando valor en el juego por bandas",
        "desc": "Guía táctica para leer partidos de alto flujo de bandas y proyectar ganancias consistentes en el mercado de saques de esquina.",
        "h1": "Mercado de Córners: La Mina de Oro del Juego Exterior",
        "body": """
        <p>En el modelado probabilístico moderno, la predicción de goles está plagada de varianza (un tiro al palo, una atajada espectacular). Sin embargo, el <strong>mercado de Córners (Saques de Esquina)</strong> ofrece un flujo de datos mucho más constante y predecible, directamente ligado al esquema táctico de los equipos.</p>
        
        <h2>El ADN de un Partido Over Córners</h2>
        <p>Los equipos que basan su sistema ofensivo en extremos puros y laterales de amplio recorrido son imanes estadísticos para los saques de esquina. Cuando el balón viaja repetidamente hacia la línea de fondo, la probabilidad de despejes forzados o centros bloqueados se dispara.</p>
        
        <h2>Evadiendo la Posesión Estéril</h2>
        <p>Por el contrario, los equipos que monopolizan el balón por el centro mediante pases cortos ("Tiki-Taka") suelen producir muy pocos saques de esquina. El modelo predictivo penaliza este tipo de esquemas. El verdadero <strong>Valor Esperado (EV+)</strong> se halla en duelos directos, de ida y vuelta, donde las transiciones dictan el ritmo del juego.</p>
        
        <h2>El Factor del Marcador Adverso</h2>
        <p>Una variable situacional clave en las apuestas en vivo es el marcador adverso de un equipo favorito jugando en casa. El asedio total en los últimos 20 minutos incrementa la frecuencia de saques de esquina en un 40%. Saber identificar estos escenarios separa al aficionado del inversor deportivo profesional.</p>
        """
    },
    {
        "slug": "valor-esperado-ev-rentabilidad-mercados-btts",
        "title": "Valor Esperado (EV+): Rentabilidad real en mercados BTTS",
        "desc": "Comprende el concepto matemático de Valor Esperado Positivo aplicado al mercado de Ambos Equipos Marcan.",
        "h1": "Valor Esperado (EV+): La Base del Trading Deportivo",
        "body": """
        <p>La diferencia fundamental entre un apostador recreacional y un inversor cuantitativo es el dominio absoluto del concepto de <strong>Valor Esperado (EV)</strong>. Aplicar esta fórmula matemática al mercado de <em>Ambos Equipos Marcan (BTTS)</em> es una de las estrategias más rentables a largo plazo.</p>
        
        <h2>La Fórmula del Éxito</h2>
        <p>El EV+ se calcula con una simple ecuación: <code>EV = (Probabilidad Real × Cuota) - 1</code>. Si el modelo estadístico determina que un partido tiene un 70% de probabilidades de BTTS, pero la casa de apuestas paga una cuota de 1.60, el cálculo es: (0.70 × 1.60) - 1 = +0.12. Esto significa un margen de beneficio teórico del 12% a largo plazo.</p>
        
        <h2>Ignorando la Intuición</h2>
        <p>El mercado a menudo infla cuotas basándose en la popularidad de los equipos o rachas engañosas de "arco en cero" contra rivales de nivel inferior. Un modelo predictivo frío cruza métricas como Goles Esperados (xG), historial directo y bajas defensivas para establecer la probabilidad real, desnuda de emociones.</p>
        
        <h2>El Mercado BTTS</h2>
        <p>El BTTS es particularmente sensible al EV+ porque depende de la fragilidad estructural de ambos contendientes. Un solo error defensivo cambia la dinámica del partido. Encontrar asimetrías entre la cuota ofrecida y el poderío ofensivo real es la verdadera clave para generar un bankroll sostenible en el tiempo.</p>
        """
    }
]

base_dir = r"..\blog"
os.makedirs(base_dir, exist_ok=True)

blog_index_path = os.path.join(base_dir, "index.html")
with open(blog_index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

bad_slugs = [
    "elfsborg-hacken-btts-seguro-apuestas",
    "goteborg-crisis-mjallby-doble-oportunidad",
    "sarpsborg-molde-xg-goles-noruega",
    "derry-city-shelbourne-dixon-coles-apuestas",
    "mercado-corners-elfsborg-hacken-analisis"
]

for slug in bad_slugs:
    pattern = r'<a class="post-card" href="/blog/' + slug + r'/">.*?</a>\s*'
    idx_content = re.sub(pattern, "", idx_content, flags=re.DOTALL)

new_links = []
for art in articles:
    slug_dir = os.path.join(base_dir, art['slug'])
    os.makedirs(slug_dir, exist_ok=True)
    
    html_content = generate_article_html(art['title'], art['desc'], art['h1'], art['body'], art['slug'])
    
    file_path = os.path.join(slug_dir, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Created article: {art['slug']}")
    
    link_html = f"""          <a class="post-card" href="/blog/{art['slug']}/">
            <div class="post-top">
              <span class="post-tag">Teoría VIP</span>
              <span class="post-date">Evergreen</span>
            </div>
            <h3 class="post-title">{art['title']}</h3>
            <p class="post-excerpt">{art['desc']}</p>
          </a>"""
    new_links.append(link_html)

marker = '<div class="posts-grid">'
if marker in idx_content:
    insert_blocks = "\n".join(new_links) + "\n"
    idx_content = idx_content.replace(marker, marker + "\n" + insert_blocks)
    
    with open(blog_index_path, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("Blog index updated with Evergreen articles.")
else:
    print("Error: Could not find marker in blog/index.html")
