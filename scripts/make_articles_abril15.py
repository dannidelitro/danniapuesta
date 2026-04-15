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
    html = re.sub(r'<span>\d+ de \w+ de 2026</span>', '<span>15 de abril de 2026</span>', html)
    html = re.sub(r'<span>⏱.*?</span>', f'<span>⏱ {read_time} min de lectura</span>', html)
    
    body_pattern = r"<h1>.*?</h1>.*?<div class=\"cta-box\">"
    new_body = f"<h1>{title}</h1>\n{html_content}\n      <div class=\"cta-box\">"
    html = re.sub(body_pattern, new_body, html, flags=re.DOTALL)
    
    os.makedirs(fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}", exist_ok=True)
    path = fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}\index.html"
    with codecs.open(path, "w", "utf-8") as f:
        f.write(html)

html_1 = """
<p class="lead">Las Ligas Emergentes, específicamente la <strong>Liga Profesional Saudí</strong>, ofrecen hoyos estadísticos gigantescos gracias a asimetrías económicas donde equipos apoyados por fondos soberanos arrollan vilmente a plantillas semi-amateurs de media y baja tabla.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>La Inyección Económica Dispar</li>
  <li>Minando el "Over 1.5" y "Team Goals" en Ligas Árabes</li>
  <li>El Factor Motivacional de las Superestrellas</li>
  <li>Pro-Tips: Evitar Ligas Extremadamente Defensivas</li>
</ul>
</div>

<h2>La Inyección Económica Dispar</h2>
<p>Diferente a las ligas Top Europeas donde existe un 'Fair Play' que equilibra talentos, la liga Saudita inyectó multimillonarios exclusivamente en los "4 Grandes" (Ej: Al Nassr, Al Hilal). Esto gestó un ecosistema donde delanteros élite como Mané o Ronaldo confrontan defensas cuyo valor de mercado combinado no supera el millón de euros. El resultado es un XG inmedible a favor del local adinerado.</p>

<h2>Minando el "Over" en Ligas Árabes</h2>
<p>El mercado tardó en reaccionar, pero la pauta se asienta. Apostar no solo al "Gana Local", sino al "Equipo Local anotará Más de 1.5 goles" genera márgenes de win rate superior al 90%. Los rivales visitantes suelen desplomarse anímicamente y físicamente tras recibir la primera anotación de figuras internacionales. La goleada abultada se torna un parámetro seguro, transformando estas justas dispares en la incubadora perfecta de ganancias compuestas.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Calendario Vacacional y Ramadán</strong><br>
  El único detractor visible de la liga Saudí reside en los bajones físicos severos durante las semanas del Ramadán. Si apuestas en medio de estos hitos religiosos, sé cauteloso con transiciones lentas en horarios diurnos. No obstante, en jornadas nocturnas plenas el asedio goleador retorna implacablemente intacto.
</div>
"""

html_2 = """
<p class="lead">Nada doblega el algoritmo algorítmico norteamericano como <strong>El Peso Físico de "La 12" en La Bombonera</strong>. Los recintos sagrados de Sudamérica influyen contundentemente en los jugadores rivales e inclinan inexplicablemente las decisiones arbitrales, generando un mercado muy rentable en el "Triunfo en Casa".</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>Más de Once Hombres: La Psicosis del Rival</li>
  <li>Árbitros Acostumbrados a la Histeria</li>
  <li>Data Empírica: Invictos Intercontinentales</li>
  <li>Pro-Tips: Líneas de Córners Excesivas Locales</li>
</ul>
</div>

<h2>Más de Once Hombres: La Psicosis del Rival</h2>
<p>Cuando un club ecuatoriano, peruano o foráneo pisa tierras como el coliseo porteño de Boca Juniors, existe un desgaste mental. Equipos débiles fuera de casa intentan cerrarse perdiendo totalmente el impulso vertical; sus posesiones suelen durar escasos segundos, lo cual aboca de forma absoluta el desarrollo de juego en única vía hacia su misma portería, asegurando estadísticamente un gol que destruye su planteamiento pálido.</p>

<h2>Árbitros Acostumbrados a la Histeria</h2>
<p>La presión popular desatará que balones divididos al borde del área se señalen con tendencia local. La rentabilidad yace en que incluso el empate prolongado sucumbirá en el ocaso del encuentro vía la insistencia aérea, convirtiendo el "Gol Local" en La Libertadores en uno de los boletos paramétricos preferidos y blindados de América.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Córners Inducidos</strong><br>
  Añadido a la apuesta directa al goleo local, escrutiniza las esquinas. En estadios hostiles (con gradas inclinadas sobre el césped), el defensor no despejará calculando las bandas, sino que mandará pelotazos apurados cediendo de manera desproporcionada entre 7 a 9 tiros de córner favoreciendo el dominio local incesante.
</div>
"""

html_3 = """
<p class="lead">Las seminales a doble combate donde chocan la élite pura alemana u española (Ej: Bayern Múnich) son históricamente ajedrez de pizarrón que a la mínima fisura estallan transformándose en encuentros demenciales y propicios para el <strong>Mercado de "Ambos Equipos Anoran" (BTTS)</strong>.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Factor Calidad vs Conservadurismo</li>
  <li>Transiciones Ligeras Post Gol</li>
  <li>La Eliminación de Tácticas en Fase Crítica</li>
  <li>Pro-Tips: Amarillas Inevitables en Contragolpes</li>
</ul>
</div>

<h2>El Factor Calidad vs Conservadurismo</h2>
<p>Un Clásico de Champions no es una liga dominical; las nóminas ofensivas están armadas para herir independientemente de que los entrenadores propongan esquemas cautelosos. Ajenas dependencias posicionales, las individualidades destrozan cerrojos originando goles excepcionales. Basta una sola fisura temprana para que todo el pizarrón conservador implosione desatando respuestas furibundas y empates exprés (Ambos Marcan Sí).</p>

<h2>La Eliminación de Tácticas Críticas</h2>
<p>Acotadas al mercado del BTTS, estas justas nos desvinculan del sufrimiento apostando al ganador final donde todo reside en la diosa fortuna o el tiempo extra. Solo buscamos dos punzadas asertivas que estadísticamente gozan de un 75% a 85% de frecuencia en eliminatorias que comprometen colosales reputaciones. </p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: La Regla de la Paridad Extrema</strong><br>
  Invertir en "Ambos Marcan" es más voluble a medida que se acerca el pitazo final. Si ambos mantienen calidad en las bancas, refuerza el ticket sumando un mercado estadístico férreo como "Más de 4.5 Tarjetas", pues las defensas optarán sin escrúpulos incurrir en faltas técnicas destructivas y dolorosas contra la magia ajena evitando colapsar catastróficamente.
</div>
"""

html_4 = """
<p class="lead">Alejada de los flashes mediáticos de los domingos se corona <strong>La Liga Eliteserien de Noruega</strong>. El balompié escandinavo es un paraíso silente e invaluable donde la filosofía ultragoleadora domina todo paradigma, obsequiando métricas absurdamente bellas de Overs perimetrales de Goles y Córners.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Bodo/Glimt y el Sistema Perimetral Goleador</li>
  <li>Defensas Rústicas, Delanteros Ágiles</li>
  <li>Promedios Elevados Excesivos de Saques de Esquina</li>
  <li>Pro-Tips: Aprovechar el Clima Escandinavo Blando</li>
</ul>
</div>

<h2>El Bodo/Glimt y el Sistema Perimetral</h2>
<p>A diferencia de ligas tácticas donde se prohíbe equivocar en zona baja, las instrucciones nórdicas enfatizan transitar la medular rápidamente en una vocación por entretener las escasas comunidades locales. Escudos imperiales de dicha región (Bodo/Glimt) implementaron módulos de extremos agresivos ocasionando promedios espectaculares muy por encima de los 2.0 goles por jornada. Aislar estos equipos engrosa cuotas "Over".</p>

<h2>Promedios Elevados Excesivos de Esquinas</h2>
<p>Suplementario a la fiesta artillera, su modo de juego es vertical mediante centros. Generar un <i>Over 10.5 Córners</i> puede parecer irracional en América, pero en Noruega y con equipos orientados puramente por las rayas al borde perimetral, la contabilidad asciendo a cotas gloriosas entre los 11 y 15 banderines por tarde. Los laterales prefieren rifar balón a línea de tiza exterior promoviendo rentabilidades de oro para el sabio estadístico.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Condiciones Sintéticas Rápidas</strong><br>
  Debido al ambiente rudo escandinavo, un grueso de las escuadras emplea canchas sintéticas inmaculadas en estadios reducidos. Esta fricción veloz acelera los pases, empobrece los cierres defensivos, y promueve trayectorias rápidas que siempre culminarán estrelladas en manotazos de porteros o piernas de zagueros yéndose al tiro de esquina imparable.
</div>
"""

create_article("ligas-emergentes-arabia-saudita-goles-apuestas", "Ligas Emergentes (Arabia Saudita): Disparidades de Oro", "Conoce la minería técnica oculta detrás de la liga Saudí y por qué el abismo salarial forja ventajas irreales enfocadas enteramente al mercado goleador Over.", "Value Bet", "8", html_1)
create_article("la-bombonera-localia-libertadores-prediccion", "El Poder de la Localía Feroz: Copas Sudamericanas", "Un algoritmo cualitativo enseñando los beneficios lucrativos prenatales apostando exclusivamente a la victoria forzosa impulsada en plazas con entornos hostiles masivos.", "Estadística Pro", "7", html_2)
create_article("btts-semifinales-champions-league-apuestas", "Choque de Titanes: El Beneficio del BTTS (Ambos Marcan)", "Evadir tensiones a ganador directo sobre clásicos europeos utilizando márgenes altamente validados enfocados al colapso mutuo en las porterías bajo élites supremas.", "Guía táctica", "8", html_3)
create_article("liga-noruega-eliteserien-corners-over-goles", "El Paraíso Noruego (Eliteserien): Lluvia Constante de Córners", "La mina de diamantes definitiva que las grandes compañías encubren. Utiliza formaciones verticales abocadas a sumar un frenesí esquinero sin compasiones tácticas.", "Inbound", "7", html_4)

print("Articulos Abril 15 generados")
