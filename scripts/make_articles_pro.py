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
    html = re.sub(r'<span>\d+ de \w+ de 2026</span>', '<span>11 de abril de 2026</span>', html)
    html = re.sub(r'<span>⏱.*?</span>', f'<span>⏱ {read_time} min de lectura</span>', html)
    
    body_pattern = r"<h1>.*?</h1>.*?<div class=\"cta-box\">"
    new_body = f"<h1>{title}</h1>\n{html_content}\n      <div class=\"cta-box\">"
    html = re.sub(body_pattern, new_body, html, flags=re.DOTALL)
    
    os.makedirs(fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}", exist_ok=True)
    path = fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}\index.html"
    with codecs.open(path, "w", "utf-8") as f:
        f.write(html)

html_1 = """
<p class="lead">El imaginario popualar asevera que "en los clásicos no existen favoritos" y que "cualquier cosa puede pasar". Pero a la hora de invertir capital real en mercados disciplinarios, de goles o victoria seca, los Derbis Desiguales (o clásicos de ciudad con enorme brecha presupuestaria) son ecosistemas predecibles con márgenes fantásticos de Edge Matemático (+EV).</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Mito del "Partido Parejo"</li>
  <li>Déficit Táctico y el Exceso de Fricción</li>
  <li>Estrategia del Handicap Subestimado</li>
  <li>Pro-Tips: Líneas Disciplinarias Infladas</li>
  <li>Preguntas Frecuentes (FAQ)</li>
</ul>
</div>

<h2>El Mito del "Partido Parejo"</h2>
<p>Cuando un gigante global, usualmente acaudalado y dueño hegemónico de su país, se enfrenta al eterno rival de su propia ciudad que sobrevive en la medianía de la tabla (ejemplos claros abundan en Cataluña, Turín o Manchester a principios de la década pasada), el aficionado común prevé un combate gladiador de igual a igual. Las matemáticas afirman lo contrario.</p>
<p>La tensión emocional de la grada empuja al cuadro débil a abandonar su sistema primario de contención defensiva. En vez de "aparcar el autobús" de forma organizada y gélida como haría un colista normal, la presión territorial les incita a salir a presionar inicuamente y dejar autopistas destapadas al super-plantel rival. Es por esto que los derbis urbanos desiguales terminan históricamente, en más del 72% de ocasiones, en abultadas goleadas y marcadores Over 2.5 muy fáciles.</p>

<h2>Déficit Táctico y el Exceso de Fricción</h2>
<p>Mientras la técnica de posesión impera intocable en el esquema del 'Goliat' local, el "David" de ciudad sufre el desgaste de perseguir sombras. Esta privación del esférico sumada al fervor barrial conlleva a detenciones bruscas del contragolpe. Los Derbis Desiguales son minas de platino para el <strong>Mercado Disciplinario</strong>.</p>
<ul style="margin-left: 20px; color: #a9bfdc; margin-bottom: 20px;">
  <li><strong>Liderazgo de Amarillas en la Visita:</strong> El mercado de 'Quien recibe más Tarjetas' (Card Match Bet) paga espectacularmente bien hacia el equipo inferior, quien estadísticamente monopolizará el 65% o más de las infracciones tácticas.</li>
  <li><strong>Rojas Directas Temporales:</strong> Si el bloque grande golea temprano (2-0 al minuto 25), la frustración psicológica del derbi dispara las agresiones por inoperancia, convirtiendo la Cuota de "Expulsión en el Partido: SÍ" en un valor fundamental.</li>
</ul>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Apostando al Handicap Subestimado</strong><br>
  En derbis desiguales, el mercado público tiene pánico al Handicap Asiático (-1.5 o -2) del gran favorito porque creen erróneamente en "el milagro del clásico". Esta inyección masiva de dinero al Empate o Victoria del humilde, obliga a las casas a subir la cuota de la goleada local para equilibrar el libro mayor (Book). Esta fisura artificial de mercado es exactamente donde asestar tu apuesta.
</div>

<h2>Preguntas Frecuentes (FAQ)</h2>
<h3>¿Vale la pena el Ambos Anotan en un derbi tan desigual?</h3>
<p>Excepcionalmente. La mayoría de Derbis Asimétricos (como Juve-Torino, o derbis catalanes) se caracterizan porque la superioridad defensiva del líder asfixia mentalmente a los delanteros vecinos. Las victorias "A cero" (To Win to Nil) ofrecen un refugio mucho más estable que rogar por un solitario milagro del colista urbano.</p>
"""

html_2 = """
<p class="lead">¿Qué diferencia estructural poseen campeonatos mundiales como la MLS (Estados Unidos) o la A-League (Australia) con el rigor militar europeo? La ausencia absoluta del precipicio llamado "Descenso de Categoría". Esta sutil diferencia de burocracia directiva transforma dichos torneos en los santuarios más prolíficos para apostar al mercado de Goles.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Terror al Descenso vs. El Entretenimiento de Franquicia</li>
  <li>La Matemática de las Ligas Abiertas (xG Promedio)</li>
  <li>Por Qué el Over 1.5 es un Trámite Administrativo</li>
  <li>Pro-Tips: Aprovecha los Primeros Tiempos Extremos</li>
</ul>
</div>

<h2>El Terror al Descenso vs. El Entretenimiento de Franquicia</h2>
<p>En España, Inglaterra o Italia, cuando el vigésimo de la tabla recibe al poderoso líder, el equipo modesto implanta formaciones del lúgubre 5-4-1, asumiendo su mediocridad a fin de rescatar un empate 0-0 de oro sólido que evite su irremediable caída a las catacumbas financieras. Juegan literalmente por las nóminas salariales de sus familias.</p>
<p>En el modelo de Norteamérica o de los canguros australianos rige el hermetismo corporativo: franquicias exclusivas sin descenso garantizado por estatutos. El peor de la tabla, gane o pierda, sigue cobrando dividendos de televisión y permanece en Primera. No existe un pánico fundacional por rascar puntos; la directiva prefiere vender "Espectáculo". Esto propicia cuadros plagados de atacantes mediáticos con mediocampistas de poca presión (defensas extremadamente laxas y desconcentradas).</p>

<h2>La Matemática de las Ligas Abiertas (xG Promedio)</h2>
<p>Consecuencia directa: ligas donde la asimetría posicional abunda. Cuanto menor preocupación táctica existe por resguardar bloqueos bajos impenetrables, más expuestos quedan los espacios transicionales. Ligas franquicia exhiben consistentemente los promedios más bestiales de <strong>Goles Esperados (Expected Goals / xG)</strong> de toda la base medular futbolística global.</p>
<ul style="margin-left: 20px; color: #a9bfdc; margin-bottom: 20px;">
  <li><strong>Over 1.5 como Rutina:</strong> Lograr más de una diana pasa de ser pronóstico a ser certidumbre en un abrumador 85-88% de los cotejos pautados.</li>
  <li><strong>Tiros Efectivos:</strong> El índice de tiros francos al marco superior a los estándares UEFA obliga a los guardametas mediocres a constantes reanudaciones.</li>
</ul>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Disparidad de las Reglas Salariales (DPs)</strong><br>
  En torneos como Norteamérica se permiten figuras Designated Players (sueldos astronómicos), que en su abrumadora y soberbia mayoría se dirigen por puro marketing a la zona ofensiva (Nueves y creadores), mientras la línea defensiva se conforma por jugadores con topes salariales universitarios. Delanteros de élite castigando zagas semi-profesionales = Over inminente.
</div>
"""

html_3 = """
<p class="lead">Dentro del ecosistema de Córners hemos hablado extensamente sobre la maravilla de los desbordes tácticos perimetrales. Pero hoy nos metemos al lodo técnico, analizando la principal fuente generadora de tiros angulares del mundo actual: el choque mortal contra los <strong>Sistemas Tácticos Defensivos de Tres Centrales (3-5-2 o 3-4-3)</strong>.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>La Falacia del Cerrojo Central</li>
  <li>El Castigo Severo de los Carrileros Exclusivos</li>
  <li>Por Qué el 3-5-2 Italiana Regala Despejes</li>
  <li>Pro-Tips: Analizando las Bajas en el Tridente</li>
  <li>Preguntas Frecuentes</li>
</ul>
</div>

<h2>La Falacia del Cerrojo Central</h2>
<p>Observar que una escuadra se para con una muralla de tres zagueros corpulentos acompañados de dos carrileros hundidos (defensa de cinco) atemoriza el pulso de quienes apuestan a Goles. Tienen toda la razón, suelen ser bloqueos infames para la creación por el embudo, pero en ese fango central florece paradójicamente el paraíso inmaculado del apostador a <strong>Over Córners</strong> o Tiros de Esquina.</p>

<h2>Por Qué el 3-5-2 Regala Despejes</h2>
<p>Al alinear tres rocas defensivas netísimamente pesadas focalizadas brutalmente en proteger el área chica y la penal, toda la responsabilidad del desborde exterior recae en los espinales y carrileros-volantes. Cuando un rival ágil que emplea un agresivo 4-3-3 ensancha la cancha, obliga al carrilero solitario a hundirse, dejándole inferioridad geométrica ante el lateral y extremo visitantes.</p>
<ul style="margin-left: 20px; color: #a9bfdc; margin-bottom: 20px;">
  <li><strong>El Rechazo como Salvavidas:</strong> Superado el carrilero defensivamente, el zaguero central escorado al costado saldrá despavorido al cruce al borde del área. Al ser corpulentos y faltos de sutileza, el porcentaje de extirpado directo al tiro de esquina lateral frente a escaramusas supera la monumental cifra del 60% por eventualidad.</li>
  <li><strong>Volea Exterior:</strong> La defensa de 5 obliga a los volantes visitantes a intentar disparar cañonazos ciegos desde la frontal, embistiendo una muralla densa de pantorrillas propiciando rebotes por línea de fondo.</li>
</ul>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Identifica el Agobio Final del 5-3-2</strong><br>
  Los sistemas italianos clásicos cimentados sobre este sistema táctico ceden el control deliberadamente como estrategia. Monopolizar y tolerar presión es su sello. Apostar en un Live al Over de Córners cuando el equipo italiano va sacando favorablemente 1-0 en las horas finales contra un equipo ofensivo desesperado, es una de las proezas tácticas más exquisitamente rentables que la estadística ha validado jamás.
</div>
"""

html_4 = """
<p class="lead">Existe una paradoja técnica que vuelve completamente locos a los inversores incautos: apostar a que un cuadro de proporciones galácticas que amasará el 75% de la tenencia del esférico asfixiará al oponente y, por supuesto, jamás encajará un gol. Desglocemos por qué el "Tiki Taka" extremo y las transiciones lentas y abrumadoras son la carnada perfecta para el <strong>Mercado de Ambos Anotan (BTTS)</strong>.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Efecto Soporífero de la Tenencia Estéril</li>
  <li>Transición Quirúrgica: Por qué te Hacen Daño de la Nada</li>
  <li>Líneas Adelantadas (La Trampa del Fuera de Juego)</li>
  <li>Pro-Tips: Analizando las Fugas Tácticas</li>
  <li>Preguntas Frecuentes</li>
</ul>
</div>

<h2>El Efecto Soporífero de la Tenencia Estéril</h2>
<p>Clubes titánicos aferrados a la dogmática de pase interminable, que marean el balón horizontalmente al borde de los dominios ajenos, desarrollan inexorablemente un espejismo ilusorio de dominancia absoluta. La cruda realidad y bitácora estadística resalta que, cuando una cuadrilla acampar permanentemente en área minada durante largos pasajes sin finalizar la jugada, sus retaguardas (los dos centrales que merodean el mediocampo solitarios) se enfrían cognitiva y muscularmente a unos ritmos fatales.</p>

<h2>Transición Quirúrgica: Por qué te Hacen Daño de la Nada</h2>
<p>Cuando apuestas al Ambos Marcan en cotejos de este perfil, confías ciegamente en el gol certero o los embates múltiples incesables del escuadrón favorito. La variable que requieres, que marca la diferencia, es ese chispazo esporádico (Counter-Pressing o Transición Rapida Defensiva-Ofensiva). Cuando un equipo dominado roba la redonda cerca a su cancerbero local, encuentra enfrente a un gigante expuesto, tendido de bruces sin contención lateral alguna que logre retroceder sesenta abismales metros de césped verde.</p>
<ul style="margin-left: 20px; color: #a9bfdc; margin-bottom: 20px;">
  <li><strong>Efectividad del Rival Sometido:</strong> El oponente sometido, que promediaría habitualmente un ínfimo y vergonzoso 0.40 xG de generación en posesiones normales, eleva su ratio de eficacia porque las escasas dos llegadas en largo que logra atinar durante 90 minutos se resuelven en crueles batallas directas 1 contra 1 frente al guardametas atónito del titán poseedor.</li>
</ul>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: El Factor "Portería Fría" y Los Centrales Pesados</strong><br>
  No subestimes esta falla geométrica. Los arqueros de grandes oncenas asfixiantes sufren horrores bajo los tres palos porque pasan una hora de reloj inactivos, perdiendo reflejos corporales primarios; cuando finalmente son embestidos por un delantero galopante, sus intervenciones resultan muy frecuentemente en atajadas defectuosas. Si además, los centrales locales no poseen estallido veloz, el <strong>BTTS (Both Teams to Score)</strong> ostenta en plataformas cuotas de 1.90 absurdamente regaladas por la ceguera algorítmica y la adoración fanática.
</div>
"""

create_article("derbis-desiguales-estrategia", "Derbis Desiguales: Estrategia de Apuestas en Clásicos de Ciudad", "Análisis exhaustivo del espejismo psíquico en el que el fervor urbano destroza planteamientos tácticos generando masacres disciplinarias y de gol.", "Derbis locales", "7", html_1)
create_article("ligas-franquicia-sin-descenso", "Ligas sin Descenso: La Mina de Oro para el Mercado Over Goles", "Una inmersión paramétrica de cómo las franquicias corporativas sin miedo a descender desprotegen sus defensas e inflan métricas mundiales del Under Goles.", "Estadísticas", "8", html_2)
create_article("analitica-corners-tres-centrales", "Analítica de Córners Contra Sistemas de Tres Centrales (3-5-2)", "Refugio oculto del apostador esquinero para doblegar y exprimir algorítmicamente y en vivo a los sólidos candados italianos valiéndose en la estadística periférica.", "Córners", "8", html_3)
create_article("paradoja-posesion-btts", "La Paradoja de la Posesión: Por Qué los Gigantes Regalan Transiciones Lentas", "La fisura maestra psicológica y topográfica detrás del incomprensible colapso de porterías gélidas para atrapar cuotas doradas en Ambos Equipos Anotan.", "Estrategia", "7", html_4)

print("done")
