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
    html = re.sub(r'<span>\d+ de \w+ de 2026</span>', '<span>12 de abril de 2026</span>', html)
    html = re.sub(r'<span>⏱.*?</span>', f'<span>⏱ {read_time} min de lectura</span>', html)
    
    body_pattern = r"<h1>.*?</h1>.*?<div class=\"cta-box\">"
    new_body = f"<h1>{title}</h1>\n{html_content}\n      <div class=\"cta-box\">"
    html = re.sub(body_pattern, new_body, html, flags=re.DOTALL)
    
    os.makedirs(fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}", exist_ok=True)
    path = fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}\index.html"
    with codecs.open(path, "w", "utf-8") as f:
        f.write(html)

html_1 = """
<p class="lead">Dentro del inmenso y a veces caótico mercado de los Goles (Over/Under), los apostadores profesionales no dependen de corazonadas ni del fanatismo de turno. Dependen exclusivamente del seguimiento estricto de la <strong>Ley de los Grandes Números</strong> y de las rachas de consistencia abrumadora. Hoy te enseñaremos cómo aprovechar formaciones y equipos que ostentan tendencias estadísticas irrompibles.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Significado Real de una "Tendencia Sólida"</li>
  <li>Rachas de Consecutividad: La Variable de Oro</li>
  <li>El Criterio del Expected Goals (xG) en Rachas</li>
  <li>Pro-Tips: Evita las Trampas Estadológicas</li>
  <li>Preguntas Frecuentes (FAQ)</li>
</ul>
</div>

<h2>El Significado Real de una "Tendencia Sólida"</h2>
<p>Cuando observamos a un equipo que ha superado la línea del "Más de 1.5 goles" en 14 partidos consecutivos, el apostador novato podría pensar: *"Es imposible que esto siga, matemáticamente pronto ocurrirá el 0-0"*. Esto se conoce como la 'Falacia del Apostador'. La estadística y las matemáticas puras nos demuestran que las rachas se construyen por condiciones sistémicas y tácticas permanentes, no por azar.</p>
<p>Si un equipo cruza el Over 1.5 en más del 85% de un torneo (Ejemplo: Holanda o Ligas Alemanas), no es coincidencia; se trata de una deficiencia defensiva de raíz acoplada a una ambición asimétrica por la verticalidad y el arco rival. Apostar de la mano con la tendencia prolongada es siempre el refugio más seguro a largo plazo.</p>

<h2>Rachas de Consecutividad: La Variable de Oro</h2>
<p>Localizar estas anomalías estadísticas toma tiempo, pero existen diamantes en bruto (como las ligas de Austria y de los Países Bajos). Clubes de tabla media asimilan tácticas de suicidio deportivo semana tras semana.</p>
<ul style="margin-left: 20px; color: #a9bfdc; margin-bottom: 20px;">
  <li><strong>Monitoreo de 10-Jornadas:</strong> Fija tu análisis exclusivamente en los últimos 10 encuentros. Cualquier dato superior a 6 meses de antigüedad carece de relevancia por el cambio de forma física y rotación de plantillas.</li>
  <li><strong>El Over Seguro (1.5):</strong> Renuncia al abrumador Over 2.5 en ligas cerradas e invierte agresivamente en el 1.5 en rachas abiertas; el Win-Rate aumenta del 55% al 82% solo reduciendo esa mínima muesca marginal de ambición.</li>
</ul>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: El Clima y la Nieve</strong><br>
  La tendencia más abismal se destruye por un factor externo que la computadora no prevé: Tormentas. Un partido plagado por lluvia torrencial, césped empapado y barro paralizará las transiciones del balón y anquilosará los músculos, provocando empates a ceros que despedazan parlays de "Equipos Goleadores" en invierno.
</div>

<h2>Preguntas Frecuentes (FAQ)</h2>
<h3>¿Cuándo se rompe una racha de Over Goles?</h3>
<p>Típicamente, el punto de quiebre estadístico ocurre al enfrentarse a escuadras denominadas "Esponjas" o Bloques muy hundidos que priorizan perder 0-1 defendiendo amontonados. O bien, ocurre con el despido del entrenador titular y la llegada de un "apagafuegos" táctico conservador interino.</p>
"""

html_2 = """
<p class="lead">Si existiera un libro de oro resguardado celosamente por los analistas deportivos mundiales, un capítulo imperioso recaería sobre cómo atacar la geométrica táctica del <strong>Bloque Bajo Defensivo</strong> empleando el infalible Mercado de los Tiros de Esquina a favor del conjunto dominante.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>Anatomía Defensiva del "Aparcar el Autobús"</li>
  <li>Densidad Poblacional y Rebotes de Choque</li>
  <li>Líneas Individuales de Equipo Córners</li>
  <li>Pro-Tips: Analizando los Laterales Cortos</li>
</ul>
</div>

<h2>Anatomía Defensiva del "Aparcar el Autobús"</h2>
<p>El "Bloque Bajo" o bloque profundo se concibe bajo el concepto único de asfixiar por completo los carriles interiores. Equipos inferiores alzan empalizadas de dos líneas ríspidas de cuatro y cinco hombres colgados patéticamente en la frontal del área de guardameta. Para la estadística de goles, esto es un veneno lúgubre, pero para los córners, es un billete abismal ganador hacia el éxito.</p>
<p>Ante una formación asfixiante por el embudo donde hasta doce piernas rechazan ciegamente remates al arco, se genera la estadística del espeso rebote forzado que sale despejado forzosamente hacia atrás del arco penal.</p>

<h2>Densidad Poblacional y Rebotes de Choque</h2>
<p>No debes conformarte con jugar al "Over Córners" global. Las cuotas más sofisticadas radican en seleccionar a un titán ofensivo y apostar por los <strong>"Córners Individuales"</strong> exclusivos de ellos (Ej: Equipo A supera los 6.5 córners él solo). Esto evade el riesgo de que el equipo humilde encerrado jamás logre siquiera pisar la otra mitad de la cancha, y te depriman arruinando el global del over final.</p>
<ul style="margin-left: 20px; color: #a9bfdc; margin-bottom: 20px;">
  <li><strong>Anchura contra Profundidad:</strong> Ligas italianas son maestras en este rigor geométrico; la desesperación del gran equipo asediador empuja el juego estrictamente al córner en porcentajes que ascienden al 70%.</li>
</ul>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: La Regla de los Primeros 25 Minutos</strong><br>
  No juegues un Under (Menos) córners en Live si un equipo favorito se adelanta pronto por un gol. Un solo tanto tempranero destraba la defensa y permite aperturas. El Over de Córners perfecto prospera y se infla masivamente en un angustiante 0-0 que se prolongue lúgubremente hasta los abismales minutos 80 o 90, donde la desesperación bombardea al área incesantemente desde los banderines laterales.
</div>
"""

html_3 = """
<p class="lead">El gremio de las plataformas operativas se afana infatigablemente por prever a los clubes peleadores, sin embargo, el veredicto definitivo tras una apuesta disciplinaria subyace exclusivamente bajo un único tirano en el campo verde: <strong>El Hombre del Silbato</strong>. El juez impone su idiosincrasia sicológica por encima de todas las barreras.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>¿Por qué el Análisis de Clubes NO es suficiente?</li>
  <li>Promedio Arbitral (Severity Rating)</li>
  <li>El Factor "Protagonista Localista"</li>
  <li>Pro-Tips: Límites y Tolerancia a Faltas</li>
  <li>Preguntas Frecuentes</li>
</ul>
</div>

<h2>¿Por qué el Análisis de Clubes NO es suficiente?</h2>
<p>Puedes congregar en el círculo central a dos oncenas reputadamente violentas que promedien más de 6 amarillas combinadas semanalmente, pero si el organismo rector de la liga programa un árbitro británico característico por "dejar jugar" (tolerancia física elevada sin intervenciones pausadas), tu esplendorosa apuesta de "Over 5.5 Tarjetas" mutará lamentablemente a un escueto saldo de dos amarillas de puro consuelo.</p>

<h2>Promedio Arbitral (Severity Rating)</h2>
<p>El perfil arbitral es numéricamente medible. Las plataformas de estadística forense dividen a los jueces por <i>Ratio de Faltas Dadas por Cartulina</i>.</p>
<ul style="margin-left: 20px; color: #a9bfdc; margin-bottom: 20px;">
  <li><strong>Colégios Estrictos:</strong> Árbitros del circuito Ibérico o Latino ostentan una sensibilidad febril a los reclamos (Gestos, aspavientos). Estas son penalizadas fulminantemente con amonestaciones de color, acelerando la meta que el inversor requiere. Si la media es de 5.5 cartulinas por aparición arbitral de un juez asignado en LaLiga, esa directriz se cumplirá fiel y ciegamente en el largo lapso probabilístico.</li>
</ul>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: El Historial Personal Juez vs Equipo</strong><br>
  Las rivalidades ocultas existen. Evalúa el registro o cruce individual de un juez particular con equipos tensos. Algunos árbitros promedian rojas directas inauditas en estadios con graderíos hostiles (por condicionamiento al ambiente sonoro estresante). El análisis psicométrico del colegiado es, literalmente, dinero y diamantes en el banco.
</div>
"""

html_4 = """
<p class="lead">En las trincheras del siglo XXI ya no se opina pasivamente sobre si un atacante "juega hermoso" o "luce estorboso". Los algoritmos modernos dictan rigor cuantitativo. Abordar partidos de ligas colosales, dotados de delanteros estratosféricos, demanda analizar fríamente las <strong>Métricas Avanzadas como los Goles Esperados (xG) y las Asistencias Esperadas (xA)</strong>.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>xG: La Fisiología Paramétrica del Gol</li>
  <li>xG Combinado en Duelos de Titanes Magnos</li>
  <li>Apostando en Jugadores Específicos (Mercado Player Props)</li>
  <li>Pro-Tips: Desviación Estándar y Forma de Atacante</li>
  <li>Preguntas Frecuentes</li>
</ul>
</div>

<h2>xG: La Fisiología Paramétrica del Gol</h2>
<p>La fórmula "XG" valora cada disparo ejecutado y lo dimensiona en probabilidad decimal. Entrar al ruedo de la Premier League sin valorar que dos potencias combinan un XG superior a 3.71, es como surcar los cielos con los parpados vendados. Los equipos élite que promedian esta barbaridad numérica no pueden ocultarse de un destino abismalmente marcado hacia presenciar balones hundidos en el blanco.</p>

<h2>xG Combinado en Duelos de Titanes Magnos</h2>
<p>Duelos magnos en Europa prometen ser ajedreces o fiestas frenéticas. Los analistas cruzan la generación del atacante local con las precariedades defensivas calculadas del adversario (xGA). Y aún más letal, contemplan el impacto de poseer a un "Outlier" estadístico; un individuo (Como Haaland, Lautaro o Mbappé) cuyas variables físicas logran sobrepasar la estadística de xG misma por puro mérito morfológico y letal implacable de remate y eficacia surrealista.</p>
<ul style="margin-left: 20px; color: #a9bfdc; margin-bottom: 20px;">
  <li><strong>Over Goles y Ambos Anotan:</strong> La conjunción de equipos top con ofensivas élite (superiores a 2.0 per cápita) empuja la línea del Over 1.5 a cuotas marginales, pero abre la compuerta gloriosa al "Marcador de Más de 2.5 y BTTS".</li>
</ul>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: El Mercado Alterno de Goleadores (Player Props)</strong><br>
  Cuando una máquina artillera como Haaland choca contra un equipo históricamente fracturado o con bajas masivas en su cerrojo, abandona el pronóstico general de 90 minutos y asalta el mercado individual de «Anotará en Cualquier Momento». La sobreexposición por centros medidos desde las bandas garantiza remates limpios que, multiplicados por el 'Killer Aspect' de la bestia atacante, rebozan las probabilidades efectivas por encima del 72% al día.
</div>
"""

create_article("tendencias-largas-rachas-over-goles", "La Ley de los Grandes Números: Rastreando Rachas en Over Goles", "Estrategia algorítmica para evitar la Falacia del Apostador y colgarse del tren imparable en anomalías goleadoras extremas de ligas medias.", "Guía táctica", "7", html_1)
create_article("Corners-asedio-bloque-bajo", "El Asedio al Bloque Bajo: Análisis Geométrico para el Over Córners", "La anatomía matemática de las líneas y despejes periféricos asfixiantes ejecutada para destrozar formaciones defensivas lúgubres del Underdog.", "Córners", "8", html_2)
create_article("analitica-severidad-juez-tarjetas", "La Importancia del Perfil Arbitral: Cómo el Juez Manda sobre el Campo", "Psicoanálisis táctico de la severidad (Severity Rating) y de cómo la procedencia de la autoridad rige irónicamente sobre las Inversiones Disciplinarias.", "Estrategia", "8", html_3)
create_article("xg-esperados-delanteros-elite", "Métricas Avanzadas (xG xA): Transformando Atacantes Élite en Ganancias", "Descifrando algoritmos modernos de Goles Esperados Combinados (xG) en colosos ofensivos y Outliers morfológicos en competiciones top.", "Value Bet", "7", html_4)

print("done")
