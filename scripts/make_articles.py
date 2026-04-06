import codecs
import re

template_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\estadisticas-avanzadas-futbol-apuestas\index.html"
with codecs.open(template_path, "r", "utf-8") as f:
    template = f.read()

def create_article(folder_name, title, desc, tag, read_time, html_content):
    html = re.sub(r'<title>.*?</title>', f'<title>{title} | Danni Apuesta</title>', template)
    html = re.sub(r'<meta name="description" content=".*?"', f'<meta name="description" content="{desc}"', html)
    html = re.sub(r'<meta property="og:title" content=".*?"', f'<meta property="og:title" content="{title}"', html)
    html = re.sub(r'<meta property="og:description" content=".*?"', f'<meta property="og:description" content="{desc}"', html)
    html = re.sub(r'<link rel="canonical" href=".*?"', f'<link rel="canonical" href="https://danniapuesta.com/blog/{folder_name}/"', html)
    html = re.sub(r'<meta property="og:url" content=".*?"', f'<meta property="og:url" content="https://danniapuesta.com/blog/{folder_name}/"', html)
    
    html = re.sub(r'(?<=→ )[^<]+(?=\s+</div>)', tag, html)
    
    html = re.sub(r'<span style="background: rgba\(0,180,216,0\.1\).*?</span>', f'<span style="background: rgba(0,180,216,0.1); color: #00b4d8; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; border: 1px solid rgba(0,180,216,0.2);">{tag}</span>', html)
    html = re.sub(r'<span>29 de marzo de 2026</span>', '<span>6 de abril de 2026</span>', html)
    html = re.sub(r'<span>⏱.*?</span>', f'<span>⏱ {read_time} min de lectura</span>', html)
    
    body_pattern = r"<h1>.*?</h1>.*?<div class=\"cta-box\">"
    new_body = f"<h1>{title}</h1>\n{html_content}\n      <div class=\"cta-box\">"
    html = re.sub(body_pattern, new_body, html, flags=re.DOTALL)
    
    path = fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}\index.html"
    with codecs.open(path, "w", "utf-8") as f:
        f.write(html)

html_1 = """
<p class="lead">La evolución del análisis estadístico aplicado al fútbol profesional ha transformado la manera en que los analistas evalúan el rendimiento y proyectan resultados futuros. El análisis predictivo moderno ya no se fundamenta únicamente en los resultados históricos brutos.</p>
<p>Estos últimos suelen estar influenciados por anomalías de varianza y factores aleatorios inherentes a una muestra pequeña de partidos. En su lugar, el modelado matemático avanzado recurre a métricas de expectativa, como los <strong>goles esperados (xG)</strong> y los goles en contra esperados, para normalizar el rendimiento y aislar la verdadera capacidad de producción ofensiva.</p>
<div class="box highlight">
<p><strong>Distribución de Poisson Bivariada:</strong> Este modelo parte de la premisa de que los goles ocurren de manera independiente y aleatoria basándose en una tasa (lambda). Permite trazar probabilidades para marcadores exactos comparando el poder ofensivo vs defensivo de ambos equipos.</p>
</div>
<h2>Mercados de Córners y Tarjetas</h2>
<p>La proyección de mercados secundarios requiere de un análisis multifactorial. Los córners están intrínsecamente ligados al volumen de ataques peligrosos y la tendencia a centrar. Equipos con bloques bajos conceden más tiros de esquina debido a la frecuencia de despejes forzados por la línea de fondo.</p>
<p>En cuanto a las tarjetas, el modelado se apoya en regresiones logísticas que evalúan las faltas promedio de ambos conjuntos, el perfil de severidad del árbitro y la tensión de la tabla de posiciones. Solo integrando estas variables dinámicas se alcanza una rentabilidad superior al 65% de win rate.</p>
"""

html_2 = """
<p class="lead">El compromiso más trascendental de la jornada 31 en la máxima categoría del fútbol italiano se disputará en el Estadio Diego Armando Maradona, donde el Nápoles recibirá al AC Milán. Ambos luchan directamente por el subcampeonato.</p>
<h2>Nápoles frente a AC Milán</h2>
<p>El Nápoles bajo Antonio Conte ha consolidado un modelo de juego basado en agresividad vertical. Tienen el récord de más goles en los primeros 15 minutos en Serie A. Su capacidad para sostener ventajas es notable. Por el lado del Milán, priorizan el equilibrio defensivo con solo 23 goles encajados en 30 partidos y ataques letales con Rafael Leão.</p>
<div class="mini-grid">
  <div class="mini-card"><strong>Nápoles</strong><br><span style="color:#b7c9e4">46 Goles a Favor | 30 en Contra</span></div>
  <div class="mini-card"><strong>AC Milán</strong><br><span style="color:#b7c9e4">47 Goles a Favor | 23 en Contra</span></div>
</div>
<p>El árbitro Daniele Doveri introduce un parámetro crítico para amonestaciones con historial severo en choques directos. La incompatibilidad ofensiva dispara la probabilidad del <strong>Más de 1.5 Goles</strong> y <strong>Ambos Equipos Anotan</strong>.</p>
"""

html_3 = """
<p class="lead">Analizamos dos focos cruciales en Europa: La Juventus consolidando su solidez de local y una guerra por el descenso entre el Lecce y un Atalanta hambriento de Champions en la Serie A.</p>
<h2>Juventus de Turín frente a Génova</h2>
<p>La balanza se inclina abrumadoramente hacia los locales con una racha de 9 partidos invictos ante el Génova. Juventus promedia 2 goles mientras recibe solo 0.87 en casa, liderados por el joven Kenan Yildiz. El Génova concede hasta 1.5 goles de visita y acumulan 53 amonestaciones, anticipando la necesidad de faltas tácticas de contención.</p>
<div class="box warning">
<p>A pesar del bajo promedio de córners de la Juventus (3.6), la acumulación de la zaga genovesa disparará los despejes, convirtiendo el mercado de "Over Córners" en una de las mayores gemas estadísticas de la jornada.</p>
</div>
<h2>Lecce contra Atalanta</h2>
<p>Un choque de realidades: Lecce 17° luchando por sobrevivir frente al Atalanta en la 7ma plaza buscando escalar. Lecce concede estrepitosamente goles (40), frente a un Atalanta que destruye sus xG anotando 41 goles frente a 20 esperados. Esta combinación casi asegura goles para los visitantes y un exceso de amonestaciones locales.</p>
"""

html_4 = """
<p class="lead">Más allá de las superpotencias, identificamos valor masivo de inversión en cruces tácticos dispares de LaLiga Española y métricas puras de goles en la League Championship Inglesa.</p>
<h2>Girona frente a Villarreal en LaLiga</h2>
<p>El Girona experimenta modesta defensa concediendo hasta 14.2 tiros por partido, mientras el Villarreal prioriza un repliegue ordenado y contragolpes fulminantes (1.7 goles/partido con apenas 43% de posesión). La fragilidad del submarino a domicilio empuja los análisis inequívocos al <strong>Ambos Equipos Anotan</strong> y la superación de líneas estándar de córners (más de 8.5 combinados).</p>
<h2>Ipswich Town frente a Birmingham City</h2>
<p>La EFL Championship es el paraíso de la transición rápida. Ipswich 3° (1.8 goles pp) se enfrenta al Birmingham City que sufre defensivamente con 30 goles encajados fuera de casa (1.5 pp). Una anomalía asimétrica perfecta.</p>
<div class="mini-grid">
  <div class="mini-card"><strong>Ipswich (Local)</strong><br><span style="color:#b7c9e4">Ataque letal de banda, media 1.8 G.</span></div>
  <div class="mini-card"><strong>Birmingham</strong><br><span style="color:#b7c9e4">Permeabilidad defensiva del 1.5 G.</span></div>
</div>
<p>El 80% de probabilidad de generar más de 1.5 goles en este partido subraya por qué la Championship representa el núcleo operativo de rentabilidad en apuestas deportivas contemporáneas.</p>
"""

create_article("modelado-predictivo-cuantitativo", "Modelado Predictivo Cuantitativo", "Descubre cómo los analistas profesionales predicen con Poisson y xG", "Metodología", "6", html_1)
create_article("analisis-napoles-milan-serie-a", "Análisis Profundo Serie A: Nápoles vs AC Milán", "Estadística cruzada y picks para el partidazo italiano de la jornada 31.", "Serie A", "4", html_2)
create_article("juventus-genova-lecce-atalanta", "Dinámica Táctica: Juventus sólida y Guerra por el Descenso", "Radiografía estadística de Juventus vs Genoa y Lecce vs Atalanta.", "Serie A", "5", html_3)
create_article("girona-villarreal-ipswich-championship", "Transiciones Letales en España e Inglaterra", "El valor puramente cuantitativo aplicado a LaLiga y la EFL Championship.", "Multiliga", "5", html_4)
print("done")
