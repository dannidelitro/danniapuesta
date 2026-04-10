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
    html = re.sub(r'<span>\d+ de \w+ de 2026</span>', '<span>10 de abril de 2026</span>', html)
    html = re.sub(r'<span>⏱.*?</span>', f'<span>⏱ {read_time} min de lectura</span>', html)
    
    body_pattern = r"<h1>.*?</h1>.*?<div class=\"cta-box\">"
    new_body = f"<h1>{title}</h1>\n{html_content}\n      <div class=\"cta-box\">"
    html = re.sub(body_pattern, new_body, html, flags=re.DOTALL)
    
    os.makedirs(fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}", exist_ok=True)
    path = fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}\index.html"
    with codecs.open(path, "w", "utf-8") as f:
        f.write(html)

html_1 = """
<p class="lead">El fenómeno "David contra Goliat" es romántico en el periodismo, pero un suicidio financiero en el sector de las inversiones deportivas. Apostar contra gigantes de la liga que enfrentan a colistas o equipos hundidos en zonas de descenso exige matemáticas frías, no narrativas cinematográficas. Hoy diseccionamos el <strong>Factor Goliat</strong>.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El abismo de la Inversión en Grandes Ligas</li>
  <li>Mecanismos de Cuotas: Por qué el 1.20 tiene Valor Oculto</li>
  <li>Diferencial de Goles Neto (Expected Goal Difference)</li>
  <li>Pro-Tips: Evita las Rotaciones Peligrosas</li>
  <li>Preguntas Frecuentes (FAQ)</li>
</ul>
</div>

<h2>El abismo de la Inversión en Grandes Ligas</h2>
<p>Cuanto miramos divisiones top de Europa (Italia, España, Inglaterra), la brecha presupuestaria entre el Top 3 y el Bottom 3 es astronómica. Equipos élite no solo dominan la posesión per cápita promediando un escandaloso 65% de tenencia de balón general, sino que asfixian físicamente a plantillas confeccionadas con una fracción minúscula de los recursos físicos y técnicos.</p>
<p>Apostar al "Gol Local" de una superpotencia contra un visitante con diferencia negativa de goles (por ejemplo, aquellos conjuntos que arrastran un -15 o un -30 estrepitoso a mitad de campeonato) constituye el cimiento angular de cualquier apuesta del tipo Combinada (Parlay) de baja volatilidad.</p>

<h2>Mecanismos de Cuotas: Por qué el 1.20 tiene Valor Oculto</h2>
<p>La mente inexperta reniega de cuotas tildadas de "pobres" que rondan entre el 1.20 y el 1.30. La inexperiencia tacha de ilógico arriesgar 100 dólares para recolectar tan solo 20 o 30. No obstante, en la matemática pura y probabilística aplicada, si una cuota estipulada de 1.25 posee una probabilidad real de ejecución por encima del 90%, significa empíricamente que la casa de apuestas te está "regalando" margen (Positive Expected Value, +EV).</p>
<ul style="margin-left: 20px; color: #a9bfdc; margin-bottom: 20px;">
  <li><strong>Ruptura de Líneas Tempranas:</strong> Los súper favoritos tienden a fulminar la muralla visitante en los primeros 25 minutos.</li>
  <li><strong>El Factor "Clean Sheet" del Líder:</strong> Frecuentemente, el líder no solo golea, sino que ostenta rachas abrumadoras de local (Ej: 10 partidos sin recibir un solo gol), lo cual permite coberturas del estilo "Local Gana a Cero".</li>
</ul>

<h2>Diferencial de Goles Neto (Expected Goal Difference)</h2>
<p>La métrica angular reina sobre esta táctica: el xGD o Expected Goals Difference. Cuando el diferencial paramétrico entre la ofensiva local y la endeblez foránea supera la marca de los 2.0 goles teóricos, la contienda abandona la lógica deportiva y se sumerge en el monopolio. El Gol Local es, en estas condiciones asimétricas, una garantía inquebrantable.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Evita las Rotaciones Peligrosas (El Síndrome Pre-Champions)</strong><br>
  La kriptonita fatal para apostar tu Bankroll entero a favor del mega favorito contra el colista se detona única y exclusivamente cuando el gigante tiene programado un cruce vital de UEFA Champions League tres días después. Es vital verificar alineaciones, porque el entrenador top rotará a sus tres puntas artilleros, transformando el partido de una cuota "segura" de 1.20 en un somnífero 0-0 que devorará tu billete.
</div>

<h2>Preguntas Frecuentes (FAQ)</h2>
<h3>¿Es recomendable apostar al Over 2.5 en estos asimetrías absolutas?</h3>
<p>Pese a la creencia popular dictaminada por la masa, apostar al Over 2.5 porque "Van de locales y golean" entraña riesgos brutales de relajación posicional (Drop Off) en las instancias complementarias. El equipo marca dos goles tempraneros y desactiva motores para cuidar reservas físicas, estancando el duelo en un sólido e inamovible 2-0.</p>
"""

html_2 = """
<p class="lead">El mercado de los goles Over/Under (Específicamente las modalidades del Over 1.5 y Over 2.5) sufre de una epidemia diagnosticada en foros globales: apostar al instinto basados enteramente en los blasones artilleros. Irónicamente, el secreto inconfesable para reinar en goles rara vez mira de frente hacia el ataque. Se enfoca estrictamente en <strong>analizar las defensas más porosas, fracturadas y vulnerables</strong> de cada liga.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>Anatomía Estricta de una "Defensa Rota"</li>
  <li>xGA (Expected Goals Against) como Santo Grial</li>
  <li>Impacto del Ambos Anotan (BTTS)</li>
  <li>Pro-Tips: Analizando las Bajas Defensivas</li>
</ul>
</div>

<h2>Anatomía Estricta de una "Defensa Rota"</h2>
<p>Una defensa disfuncional no se identifica únicamente leyendo pasivamente la tabla de posiciones en la columna de "Goles en Contra". Existen deficiencias crónicas posicionales dictaminadas por esquemas de corte muy kamikaze (típico de escuadras alemanas o neerlandesas, reconocidas en todo el gremio por proponer bloques en extrema amplitud sin carrileros marcadores). Una escuadra que sale a presionar sin orden propicia autopistas hacia su guardameta.</p>
<p>Si convergen en la programación dominical dos conjuntos propensores a recibir estrepitosos contragolpes debido a un retroceso letárgico, la contienda huele inexorablemente a pólvora antes del pitido liminar.</p>

<h2>xGA (Expected Goals Against) como Santo Grial</h2>
<p>Dejemos el instinto corazonado en el bar de la esquina y acojámonos al número puro. El <strong>xGA</strong> (Goles Esperados en Contra) desnuda por completo a aquellos defensores que tuvieron aparente suerte temporal gracias a las intervenciones divinas de su portero estelar.</p>
<ul style="margin-left: 20px; color: #a9bfdc; margin-bottom: 20px;">
  <li><strong>Disparos Asimilados desde el Empalme Central:</strong> Equipos débiles consienten, en promedio de los peores del ciclo, más de 12 oportunidades explícitas generadas en el perímetro de su área de rigor (Danger Zone).</li>
  <li><strong>Colapso del Over 1.5:</strong> Cuando el xGA combinado de sendos escuadrones se remonta por encima de la marca teórica del 3.0, apostar a que se marquen mínimos dos tantos (Over 1.5 goles) se erige en una base de cimiento sólido y robusto.</li>
</ul>

<h2>Impacto del Ambos Anotan (BTTS)</h2>
<p>Cuando apuestas al Ambos Marcarán condicionado fundamentalmente a defensas rotas y de cristal, gozas de un doble apalancamiento. Careces de ansiedades frente a quién de los dos domine verdaderamente las riendas posicionales, ya que el equipo dominado, inevitablemente propiciará alguna arremetida fugaz donde la zaga contraria concederá inexplicablemente la deslucida diana del honor.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Revisa a los Porteros y Centrales Sancionados</strong><br>
  Antes de precipitarte inyectándole capital pesado a un "Over 2.5", revisa escrupulosamente los partes médicos del club en su defensa titular. Faltas de porteros titulares y del 'Perro de Presa' de campo rebajan inmediatamente el nivel retentivo general del equipo, transformándolos en coladores garantizados durante la coyuntura del inminente choque.
</div>
"""

html_3 = """
<p class="lead">Dentro del intrincado y fascinante ecosistema de los mercados periféricos deportivos, la especulación de Tiros de Esquina ha escalado gradualmente hasta adueñarse de la corona suprema del <i>Value Trading</i> táctico. Hoy dilucidaremos por qué los carrileros, los laterales ofensivos profundos y el volumen de bandas constituyen la brújula inquebrantable tras los pronósticos Over de Córners.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>Conceptos Basales: Rompiendo mitos de Posesión</li>
  <li>El Factor 'Alas' o Bandas Densas (Wing Play)</li>
  <li>Cómo afecta la debilidad foránea al Despeje al lateral</li>
  <li>Pro-Tips: Analítica Visual Periférica</li>
</ul>
</div>

<h2>Conceptos Basales: Rompiendo mitos de Posesión</h2>
<p>Incluso inversores consolidados caen regularmente atrapados en red de la falacia abismal de "Mayor Posesión significa obligatoriamente Mayores Córners". Una mentira absoluta que debe erradicarse. Numerosas escuadras dominan hasta un asfixiante 70% la pelota, dictando cátedra por el pasillo central, lo que deriva en remates francos que concluyen en gol directo o en intercepciones reanudadas por meta o portero, eliminando la aparición masiva de tiros angulares.</p>

<h2>El Factor 'Alas' o Bandas Densas (Wing Play)</h2>
<p>El santo grial subyace enteramente en el "Wing Play" o "Fluidez Perimetral". Los centros laterales propician invariablemente cabezazos rebotados en zagas en estado de pánico, y las galopadas por línea de fondo acaparan cortes milimétricos forzados de centrales barridos contra el abismo de meta.</p>
<ul style="margin-left: 20px; color: #a9bfdc; margin-bottom: 20px;">
  <li>Promedios por club: Busca clubes o franquicias que crucen la marca histórica de producir de media a solas la astronómica cifra de <strong>6.5 a 7.5 córners intencionales propios</strong>, basados en alas muy escurridizas.</li>
  <li>Rivales Cómplices: Cruza esta agresividad local con un modesto rival que padece un bloqueo mental defendiendo embates por aire, lo cual le obligará irremediablemente a revolear pelotas hacia afuera a la desesperada de espaldas.</li>
</ul>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: La Muerte del Marcador Favorable</strong><br>
  Nunca se te ocurra apostarle grandes magnitudes a un evento "Over" de Córners antes que empiece sí prevés que el mega favorito aplastará rápidamente abriendo el marcador 2 o 3 por cero antes del minuto veinte. Las embestidas disminuirán, los centros dejarán de emerger y acabarán tocándola amablemente al medio. Si el juego es asimétrico pero presumiblemente parejo y tenso, el over corner fluye con majestuosidad durante la larga noche táctica.
</div>
"""

html_4 = """
<p class="lead">Existen encuentros pacíficos amparados por un transitar límpido y de noble lidia. No obstante, al asomar los clásicos de rivalidad arraigada o las contiendas por subsistir donde la derrota infiere caída irremediable al abismo del descenso, el balón cede estelaridad y protagonismo ciego al roce humano y la contrición visceral: surge el lucrativo firmamento del <strong>Mercado Disciplinario</strong>.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>Apuestas de Cartulinas o Booking Points</li>
  <li>La Tempestad Emocional de Derbis y Clásicos Locales</li>
  <li>Perfil Arbitral: Jueces Impolutos</li>
  <li>Pro-Tips: Evade Partidos Resueltos</li>
  <li>Preguntas Frecuentes</li>
</ul>
</div>

<h2>Apuestas de Cartulinas o Booking Points</h2>
<p>Las plataformas y agencias catalogan masivamente esta modalidad como "Más/Menos (Over/Under) Tarjetas Globales" o "Puntos Disciplinarios (Booking Points)", donde un cartón amarillo equivale a 1 unidad y una expulsión directa a 2 (dependiendo rigurosamente del tabulador operante de cada Bookie individual).</p>
<p>Invertir cuantiosa o discretamente en mercados disciplinarios borra afortunadamente una preocupación fundamental de tu psique: a ti ya no te incumbe ni estresa quién alza el trofeo final, te importan las fricciones tácticas a ras de piso.</p>

<h2>La Tempestad Emocional de Derbis y Clásicos Locales</h2>
<p>América Latina (Copa Libertadores o Ligas Mex/Arg) se corona en el pedestal invencible a nivel mundial de sobre-exposición de amonestaciones. Cruces por historia o tensión táctica por escapar del último cupo de descenso transforman la cancha en un tablero en disputa aguerrida donde acumular 5 o 6 tarjetones en el consolidado de ambos planteles se tilda como una mañana sumamente "normal" y pacífica.</p>

<h2>Perfil Arbitral: Jueces Impolutos</h2>
<p>No basta identificar a planteles carniceros u oligarcas del roce. La varita mágica del dinero descansa implacable en el nombre del sujeto de negro que pitará. Las estadísticas revelan una brecha descomunal; existen jueces ingleses que promedian un ridículo marco de 2 tarjetas pacíficas por lidia, en contraposición severa de algunos jueces latinos u oriental-europeos que abren su caja de castigos promediando arriba de los picos teóricos de 6 por contienda.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: El Peligro Oculto del Cartón Subjetivo</strong><br>
  Se altamente vigilante; muchos apostadores y noveles del mercado creen que en partidos de goleada unilateral también saldrán cartulinas a relucir debido a la humillación ajena. Falso. Una vez el marcador sube al 3-0 irremediable y restan veinte minutos en agónica procesión perimetral, la frustración desaparece asimiendose como aceptación y el juez guardará celosamente sus amonestaciones, matando sin misericordia deportiva el Over tarjetas de quienes invertieron al filo del último minuto.
</div>

<h2>Preguntas Frecuentes</h2>
<h3>¿Las Tarjetas Rojas valen Doble en el mercado 'Más o Menos X Tarjetas'?</h3>
<p>Varía infinitamente de agencia en agencia. Algunas casas, dictaminan por reglamento base que una cartulina es una cartulina (equivaliendo tanto amarilla y roja a un mero punto sumatorio del contador Over/Under), mientras que en plataformas anglosajonas con Booking Points, una expulsión suma 25 formidables puntos disciplinarios de impacto. Leer las bases legales y reglas de tu plataforma es imperativo para los apostadores metódicos de disciplinas periféricas.</p>
"""

create_article("estrategia-david-vs-goliat-favoritos", "El Factor Goliat: Cómo Rentabilizar Apostando a Grandes Favoritos", "Estrategia profunda para comprender el diferencial neto y métricas asimétricas en duelos dispares de las Grandes Ligas europeas.", "Guía táctica", "7", html_1)
create_article("defensas-rotas-estrategia-over-goles", "Defensas Rotas: El Secreto Definitivo para el Mercado de Over Goles", "Rompe con el engaño de los delanteros élite y domina el análisis de defensas kamikazes (xGA) para multiplicar el Win Rate absoluto.", "Análisis", "8", html_2)
create_article("carrileros-bandas-value-corners", "Carrileros y Córners: Identificando Ligas Abiertas Periféricas", "Examen riguroso táctico para explotar el mercado de Tiros de Esquina a través del desborde incesante o Wing Play.", "Córners", "7", html_3)
create_article("tensión-derbis-analisis-booking-points", "Apuestas Disciplinarias: El Psicoanálisis de los Derbis (Tarjetas)", "Domina agresivamente el circuito periférico previendo los cartones, la tolerancia de los arbitrajes y la rivalidad de zonas de descenso.", "Estrategia", "8", html_4)

print("done")
