import os

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
      <span class="article-tag">Modelamiento 25 Mayo</span>
      <h1>{h1}</h1>
      <div class="article-meta">Por Danni Apuesta | 25 de Mayo de 2026 | Análisis Predictivo VIP</div>
    </div>
    
    <div class="article-content">
      {body_content}
    </div>
    
    <div class="cta-box">
      <h3>¿Listo para multiplicar tu capital hoy?</h3>
      <p style="margin-bottom: 1.5rem; color: #a5b9d4;">Aprovecha las cuotas de esta jornada usando nuestros bonos exclusivos de registro. ¡No dejes dinero en la mesa!</p>
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
        "slug": "elfsborg-hacken-btts-seguro-apuestas",
        "title": "Elfsborg vs Häcken: Por qué el BTTS es la apuesta más segura",
        "desc": "Análisis estadístico del duelo Elfsborg vs BK Häcken en la Allsvenskan sueca y la alta probabilidad matemática de Ambos Equipos Marcan.",
        "h1": "Elfsborg vs BK Häcken: La Alta Probabilidad del BTTS",
        "body": """
        <p>El duelo estelar en la Allsvenskan sueca este 25 de mayo de 2026 nos presenta un enfrentamiento de altísimo octanaje en el Borås Arena entre el <strong>IF Elfsborg</strong> y el <strong>BK Häcken</strong>. Ambos conjuntos pelean la supremacía de las plazas europeas empatados a 16 puntos, pero es en las métricas de goles donde el valor de inversión resulta innegable.</p>
        
        <h2>El Poder Ofensivo en el Borås Arena</h2>
        <p>Según el cruce de datos y nuestra validación multifuente, el IF Elfsborg como local es una auténtica máquina de hacer goles. Su media histórica en el Borås Arena arroja la asombrosa cifra de <strong>2.57 goles anotados por encuentro</strong>. Frente a su afición, su esquema de ataque se despliega con transiciones fulgurantes que raramente terminan sin vulnerar el arco rival.</p>
        
        <h2>Häcken: Peligro y Concesiones</h2>
        <p>Por otro lado, el BK Häcken se erige como una de las ofensivas más peligrosas del campeonato. Sus últimos cinco partidos han producido 10 goles a favor, demostrando un poder de fuego envidiable. Sin embargo, su estructura defensiva en condición de visitante flaquea enormemente, concediendo una media de <strong>1.63 goles por salida</strong>.</p>
        
        <h2>Valor Esperado Positivo (EV+)</h2>
        <p>Nuestro modelo matemático le asigna una <strong>probabilidad real del 78%</strong> a que ambos equipos anoten (BTTS: Sí). Con cuotas rondando el 1.57, se genera un EV positivo de +0.22, consolidando este pick como uno de los movimientos financieros deportivos más sensatos de la jornada regular escandinava.</p>
        """
    },
    {
        "slug": "goteborg-crisis-mjallby-doble-oportunidad",
        "title": "IFK Göteborg en Crisis: Aprovechando la Doble Oportunidad del Mjällby",
        "desc": "Por qué el Mjällby AIF ofrece un Valor Esperado (EV+) altísimo frente a un IFK Göteborg hundido en crisis defensiva.",
        "h1": "Göteborg vs Mjällby: Explotando la Debilidad Defensiva",
        "body": """
        <p>La jornada del 25 de mayo de 2026 nos entrega un duelo de realidades diametralmente opuestas en la Allsvenskan. El histórico <strong>IFK Göteborg</strong> recibe al <strong>Mjällby AIF</strong> en medio de una crisis deportiva que los tiene relegados a la zona baja de la tabla con apenas 6 puntos. ¿Cómo puede el inversor deportivo capitalizar este escenario?</p>
        
        <h2>El Historial Directo (H2H)</h2>
        <p>Los registros no perdonan. Mjällby mantiene una hegemonía táctica absoluta sobre el Göteborg en sus últimos tres enfrentamientos directos, habiendo salido victorioso en cada uno de ellos, incluyendo un contundente 2-0 en su última visita al Gamla Ullevi. Esta paternidad psicológica y táctica es una variable de primer orden en el modelaje probabilístico.</p>
        
        <h2>Rotura Defensiva del Göteborg</h2>
        <p>La debilidad más flagrante del equipo local es su bloque bajo. El IFK Göteborg arrastra una terrible racha de <strong>11 partidos consecutivos de liga encajando al menos un gol</strong>. La incapacidad para sostener la portería a cero frente a la visita sólida (Mjällby tiene 14 puntos y pelea arriba) genera un escenario sumamente asimétrico.</p>
        
        <h2>La Protección de la Doble Oportunidad (X2)</h2>
        <p>Apostar a victoria seca de visitante siempre conlleva riesgos por factores extradeportivos, pero blindar la inversión con una <strong>Doble Oportunidad X2 (Empate o Gana Mjällby)</strong> eleva la probabilidad de acierto a un abrumador <strong>82%</strong>. Esta decisión protege el capital mientras explota eficientemente la inconsistencia del local.</p>
        """
    },
    {
        "slug": "sarpsborg-molde-xg-goles-noruega",
        "title": "Sarpsborg vs Molde: Análisis de Goles Esperados (xG) en Noruega",
        "desc": "El modelo predictivo para la Eliteserien arroja un altísimo potencial de BTTS en el partido Sarpsborg 08 vs Molde FK basado en métricas xG.",
        "h1": "Sarpsborg 08 vs Molde: Choque de Goles en Noruega",
        "body": """
        <p>Saltamos a la Eliteserien de Noruega, donde el análisis cuantitativo ha detectado una anomalía estadística muy favorable en el enfrentamiento del 25 de mayo entre <strong>Sarpsborg 08</strong> y el siempre potente <strong>Molde FK</strong>.</p>
        
        <h2>La Métrica de Goles Esperados (xG)</h2>
        <p>El Molde FK conserva una tasa de generación de goles esperados (xG) sumamente competitiva en condición de visitante, a pesar de ejecutar rotaciones en su once inicial. Tienen la jerarquía y las métricas necesarias para garantizar anotaciones ante bloques defensivos endebles.</p>
        
        <h2>El Sufrimiento Local del Sarpsborg</h2>
        <p>El argumento de mayor peso para este pick radica en el rendimiento del Sarpsborg en casa. Han encajado goles en el <strong>100% de sus partidos como local</strong> esta temporada. Su incapacidad crónica para consolidar cerrojos defensivos los obliga siempre a ir a buscar el gol para rascar puntos.</p>
        
        <h2>Proyección del Modelo</h2>
        <p>Integrando estos factores, el modelo estima un <strong>76% de probabilidad</strong> de que el mercado de Ambos Equipos Marcan (BTTS) se cumpla. Aprovechar esta tendencia antes de que el mercado ajuste la línea de cuotas es vital para un retorno de inversión saludable.</p>
        """
    },
    {
        "slug": "derry-city-shelbourne-dixon-coles-apuestas",
        "title": "Derry City vs Shelbourne: Fortaleza Local y el modelo Dixon-Coles",
        "desc": "Análisis profundo de la Premier Division de Irlanda usando el filtro de Dixon-Coles para blindar pronósticos en partidos de bajo xG.",
        "h1": "Derry City vs Shelbourne: El Orden Defensivo Táctico",
        "body": """
        <p>El fútbol irlandés (Premier Division) a menudo se caracteriza por encuentros de intensa fricción física y orden táctico estricto. El duelo entre <strong>Derry City</strong> y <strong>Shelbourne FC</strong> en el Brandywell Stadium este 25 de mayo es un ejemplo de manual para la aplicación del modelo <em>Dixon-Coles</em>.</p>
        
        <h2>Resiliencia en Brandywell</h2>
        <p>El Derry City ha convertido su estadio en un fortín, aunque no a base de victorias aplastantes, sino mediante una solidez inquebrantable. Han encadenado <strong>cuatro empates consecutivos</strong> como locales. Esto demuestra una capacidad enorme para evitar derrotas bajo cualquier circunstancia.</p>
        
        <h2>Aplicando el Filtro Dixon-Coles</h2>
        <p>El Shelbourne es efectivo en ataque, pero enfrentarse al bloque bajo del Derry suele neutralizar las líneas de pase. Nuestro algoritmo, mediante la corrección de dependencia de Dixon-Coles, impide que las rachas ofensivas previas de la visita inflen artificialmente la probabilidad de un partido abierto.</p>
        
        <h2>La Jugada Maestra</h2>
        <p>El modelo sitúa la probabilidad de victoria visitante o partido abierto muy a la baja (80% de probabilidades de menos de 3.5 goles). Por ello, el valor supremo reside en blindarse con la <strong>Doble Oportunidad 1X (Gana Derry o Empate)</strong>, con una solidez asombrosa del 80% frente a cualquier embate del Shelbourne.</p>
        """
    },
    {
        "slug": "mercado-corners-elfsborg-hacken-analisis",
        "title": "Mercado de Córners: El secreto táctico del duelo Elfsborg vs Häcken",
        "desc": "Descubre por qué la línea de más de 9.5 saques de esquina es la apuesta predictiva con mayor valor en la Allsvenskan sueca de hoy.",
        "h1": "Elfsborg vs Häcken: Explotando el Mercado de Córners",
        "body": """
        <p>A menudo, el mercado tradicional de Ganador del Partido (1X2) ofrece cuotas que no compensan el riesgo, especialmente en choques de alta tensión como el de <strong>IF Elfsborg</strong> y <strong>BK Häcken</strong> por las posiciones europeas de la Allsvenskan. Es aquí donde el modelador predictivo gira su vista hacia mercados alternativos de alto flujo.</p>
        
        <h2>El Patrón Táctico de las Bandas</h2>
        <p>La IA ha detectado un volumen masivo de juego directo por las bandas en ambos planteles. El Elfsborg empuja incesantemente a sus rivales hacia la línea de fondo, y el Häcken, jugando a la contra, responde forzando despejes de la defensa contraria. Esto infla drásticamente la frecuencia de tiros de esquina.</p>
        
        <h2>Números Puros</h2>
        <p>La media combinada proyectada entre estos dos equipos supera holgadamente los 11 córners. En los partidos del Häcken como visitante, el promedio se dispara hasta los 13 saques de esquina totales. </p>
        
        <h2>Riesgo Neutralizado</h2>
        <p>Evitando la incertidumbre de quién ganará el encuentro, dirigir la inversión hacia <strong>Más de 9.5 Córners Totales</strong> proyecta una increíble certeza del <strong>82%</strong>. Un mercado especializado para inversores inteligentes este 25 de mayo.</p>
        """
    }
]

base_dir = r"..\blog"
os.makedirs(base_dir, exist_ok=True)

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
              <span class="post-tag">Predictivo</span>
              <span class="post-date">25 Mayo 2026</span>
            </div>
            <h3 class="post-title">{art['title']}</h3>
            <p class="post-excerpt">{art['desc']}</p>
          </a>"""
    new_links.append(link_html)

blog_index_path = os.path.join(base_dir, "index.html")
with open(blog_index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

marker = '<div class="posts-grid">'
if marker in idx_content:
    insert_blocks = "\n".join(new_links) + "\n"
    idx_content = idx_content.replace(marker, marker + "\n" + insert_blocks)
    
    with open(blog_index_path, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("Blog index updated.")
else:
    print("Error: Could not find marker in blog/index.html")
