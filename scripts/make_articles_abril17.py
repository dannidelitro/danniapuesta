import codecs
import re
import os

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
    html = re.sub(r'<span>\d+ de \w+ de 2026</span>', '<span>17 de abril de 2026</span>', html)
    html = re.sub(r'<span>⏱.*?</span>', f'<span>⏱ {read_time} min de lectura</span>', html)
    
    body_pattern = r"<h1>.*?</h1>.*?<div class=\"cta-box\">"
    new_body = f"<h1>{title}</h1>\n{html_content}\n      <div class=\"cta-box\">"
    html = re.sub(body_pattern, new_body, html, flags=re.DOTALL)
    
    os.makedirs(fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}", exist_ok=True)
    path = fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}\index.html"
    with codecs.open(path, "w", "utf-8") as f:
        f.write(html)

html_1 = """
<p class="lead">La segunda división de los Países Bajos (Eerste Divisie) es secretamente el nicho de mayor productividad ofensiva del mundo. Entender cómo los equipos filiales actúan como <strong>Laboratorios de Goles</strong> es el Santo Grial de las cuotas 'Over'.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>La Filosofía de Academias (Ajax y PSV)</li>
  <li>Ausencia Absoluta de Miedo Defensivo</li>
  <li>Rachas Sostenidas del Over 1.5 y 2.5</li>
  <li>Pro-Tips: Apostar Exclusivamente en Segundas Mitades</li>
</ul>
</div>

<h2>La Filosofía de Academias</h2>
<p>Equipos identificados como 'Jong' (Jóvenes) en los Países Bajos (ej: Jong Ajax, Jong PSV) utilizan estos partidos en la Eerste Divisie pura y exclusivamente para probar esquemas tácticos hiperagresivos. El resultado de la tabla importa menos que la formación ofensiva de sus canteranos, lo cual provoca formaciones donde prima el asalto constante.</p>

<h2>Ausencia de Miedo Defensivo</h2>
<p>Al no poder ascender a la primera división de manera oficial, los clubes cantera suelen prescindir del juego estructurado en la retaguardia. Ceder 70 goles por temporada es habitual. Combinando dos clubes canteranos se amalgaman XG combinados absurdos superiores a 3.2, asegurándonos probabilidades matemáticas cercanas al 90% para líneas base de Goles (Over 1.5) e inversiones fuertes de BTTS.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: El Clímax de la Segunda Mitad</strong><br>
  Los sistemas juveniles suelen agotar stamina temprana. Para el minuto 60, las líneas se elongan más de 40 metros. Si al medio tiempo no hay festín goleador en Holanda, entra fuerte al mercado "Más de 1.5 goles en el partido" ya que las piernas flaquearán permitiendo lluvias en los instantes finales.
</div>
"""

html_2 = """
<p class="lead">El análisis de córners obedece puramente a leyes geométricas y territoriales del campo. Cuando fuerzas acorraladoras como <strong>el Inter de Serie A o el Fenerbahçe en Turquía</strong> aplastan bajo asedios, la bandera de esquina es la mina de oro subyacente.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>Asedio del Dominador (El Factor Campeonato)</li>
  <li>Carrileros Profundos y la Barrida Desesperada</li>
  <li>Mercados Asiáticos de Córners Unilaterales</li>
  <li>Pro-Tips: Evitar Ligas Centralizadas</li>
</ul>
</div>

<h2>Asedio del Dominador (El Factor Campeonato)</h2>
<p>En ligas donde un club se juega el título milimétricamente no existen minutos conservadores. Frente a rivales sotaneros con bloques bajos (defensivos), equipos estelares anidan el 70% del balón en la zona de castigo. Ante la estrechez interior, la pelota fluye hacia carrileros que envían metralla en forma de centros, culminando irremediablemente en rechaces defensivos para saque de esquina.</p>

<h2>Carrileros Profundos y la Serie A</h2>
<p>El Inter maneja un sistema que empuja laterales al ataque fulgurante forzando rechaces a sus centros violentos. Estas estadísticas no mienten: un solo club puede cosechar 9 córners bajo presión en 45 minutos. En estos escenarios, operar líneas globales de Over 8.5 representa apuestas de valor intrínseco blindadas ante sorpresas trágicas.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Línea de Tiempo del Asedio</strong><br>
  La regla de oro dicta que la balanza de tiros de esquina es proporcional al marcador. Si el equipo dominador no logra anotar en la primera media hora, apostar al "Córner del Dominador" en vivo duplica el margen de ingresos debido a la frustración e intensidad redoblada rumbo al medio tiempo.
</div>
"""

html_3 = """
<p class="lead">Las transiciones fugaces y laxas retaguardias hacen de Australia una región invaluable. Entender las métricas ocultas de la <strong>A-League Australiana</strong> dota a inversores madrugadores de un flujo letal antes del medio día.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Estilo Correcalles Oceánico</li>
  <li>Asimetría de Plantillas Físicas</li>
  <li>Eficiencia ante Alta Vulnerabilidad Ofensiva</li>
  <li>Pro-Tips: BTTS en Partidos Matutinos</li>
</ul>
</div>

<h2>El Estilo Correcalles Oceánico</h2>
<p>La escuela táctica asimilada por la liga australiana (A-League) antepone el entretenimiento familiar del ida y vuelta a los cerrojos de las ligas itálicas o sudamericanas. Las recuperaciones de pelota originan estampidas directas al marco contrario lo cual deriva en paradas continuas y disparos francos muy tempranos. El XG combinado suele rondar frecuentemente los 3.7 esperados por compromiso.</p>

<h2>Eficiencia y Alta Vulnerabilidad</h3>
<p>Frente a ritmos veloces, es habitual que tanto ganadores como perdedores de un encuentro tengan conversiones del 12% o superior debido al espacio cedido. Esto certifica un ecosistema natural y estandarizado de goles fijos paramétricos respaldados al 85% haciendo inversiones sólidas mediante Parlays de base (Over 1.5 Goles Global).</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Inclinación por el Local</strong><br>
  Añadido a la suma de dianas, la geografía australiana afecta al visitante fuertemente. Escoge siempre inclinar tu balanza al <i>"Gol Temprano del Local"</i>, quien asimila mejor el impacto horario en el vasto continente obteniendo los primeros frutos de los desajustes defensivos forasteros.
</div>
"""

html_4 = """
<p class="lead">El derbi en países nórdicos o encuentros directos entre coleros escuece no por el talento, sino por <strong>El factor humano en el silbato</strong>. Cruzar el perfil psicológico del árbitro con rivalidades es el santo reino de los plásticos.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Árbitro Tarjetero de Cero Tolerancia</li>
  <li>Derbis Nacionales en Escandinavia (Allsvenskan)</li>
  <li>Puntos Desesperados y Lucha de Descenso</li>
  <li>Pro-Tips: Minutos Finales del Derbi</li>
</ul>
</div>

<h2>El Árbitro de Cero Tolerancia</h2>
<p>El mercado de amonestaciones requiere inteligencia de inteligencia externa. Árbitros precisos como el sueco Fredrik Klitte ostentan registros brutales promedio de más de 3.5 amonestaciones de saque, cortando brúscamente fricciones para salvaguardar su orden autoritario. Este rasgo garantiza rentabilidad al sobrepasar cualquier línea reservada de tarjetas propuesta por la casa.</p>

<h2>Derbis y Descenso: Ecosistema Perfecto</h2>
<p>Cuando un colegiado estricto es enviado a gobernar disputas de descenso o clásicos candentes, el cóctel garantiza eclosión técnica de infracciones. Hachazos en la medular surgen fruto de la desesperación por escapar de la B y salvar prestigios caídos. Con medias superando proyecciones de 74%, la cartulina encierra la inversión pasiva más exquisita conocida.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Amonestaciones de Desespero</td>
  La segunda amarilla o roja surge predominantemente por interrupciones tácticas y frustraciones orales superando el minuto setenta. Inyecta capital sobre un Over adicional del <i>Live Betting</i> cerrando el partido con equipos amargados forzados al impacto corporal para impedir goleadas inminentes.
</div>
"""

create_article("laboratorio-goles-jong-eerste-divisie-apuestas", "El Laboratorio: La Eerste Divisie y Equipos Filiales", "Entiende cómo dominar probabilísticamente el nicho más goleador de Europa amparado enteramente por desajustes tácticos de las academias juveniles de Holanda.", "Avanzado", "9", html_1)
create_article("corners-asedio-dominador-fenerbahce-inter", "Asedios del Dominador: Córners en Turquía y Serie A", "Analiza el despligue métrico esquinero originado intrínsecamente del hostigamiento férreo por carreras titánicas campeonables frente a muros conservadores.", "Guía táctica", "8", html_2)
create_article("a-league-australiana-vulnerabilidad-goles", "Vulnerabilidad y Goles en la A-League Australiana", "Benefíciate de ritmos veloces insostenibles a horas tempranas forjando selecciones inquebrantables de Overs sobre retaguardias descuidadas.", "Estadística Pro", "8", html_3)
create_article("perfil-arbitraje-riguroso-allsvenskan-apuestas", "Arbitraje Riguroso en Clásicos (Allsvenskan)", "Estudia psicológicamente la tendencia letal de colegiados impositivos envueltos en ecosistemas hostigantes o choques acérrimos para extraer tu margen ganador.", "Ranking Árbitros", "7", html_4)

print("Articulos Abril 17 generados")
