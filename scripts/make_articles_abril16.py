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
    html = re.sub(r'<span>\d+ de \w+ de 2026</span>', '<span>16 de abril de 2026</span>', html)
    html = re.sub(r'<span>⏱.*?</span>', f'<span>⏱ {read_time} min de lectura</span>', html)
    
    body_pattern = r"<h1>.*?</h1>.*?<div class=\"cta-box\">"
    new_body = f"<h1>{title}</h1>\n{html_content}\n      <div class=\"cta-box\">"
    html = re.sub(body_pattern, new_body, html, flags=re.DOTALL)
    
    os.makedirs(fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}", exist_ok=True)
    path = fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}\index.html"
    with codecs.open(path, "w", "utf-8") as f:
        f.write(html)

html_1 = """
<p class="lead">Huir de las luces cegadoras de la Premier League para refugiarse en el lodo de la <strong>League One (Tercera División)</strong> es un salto cuántico hacia la rentabilidad algorítmica gracias a la desorganización defensiva endémica de sus clubes.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Vértigo Inferior: Menos Cerebro, Más Piernas</li>
  <li>Minando el "Over 1.5" entre Equipos Menores</li>
  <li>Las Rachas de Dos Dígitos (Peterborough Mágico)</li>
  <li>Pro-Tips: Evitar Lunes y Martes</li>
</ul>
</div>

<h2>El Vértigo Inferior: Menos Cerebro, Más Piernas</h2>
<p>En el Championship y la League One el aspecto táctico sufre deficiencias severas que se compensan con pulmón y corazón británico puro. Los entrenadores fomentan bombazos al área desde el pitazo inicial, marginando las transiciones limpias. Esto origina 90 minutos ininterrumpidos donde los centrales desordenados son fusilados repetitivamente, transformando el partido en un "ida y vuelta" irresponsable.</p>

<h2>Minando el "Over 1.5" y Rachas Sostenidas</h2>
<p>Clubes como Peterborough acarrean historiales anómalos estadísticamente (ej. 13 partidos consecutivos superando la barrera de 2 goles). Aislar este parámetro del fango y emparejarlo en cuotas de inversión simple gesta márgenes gananciales del 96% paramétrico. El "Over 1.5" se convierte entonces en un vehículo defensivo financiero envidiable.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Cansancio Semanal</strong><br>
  Las Ligas de Ascenso encallan en agendas criminales (jugando Domingo, Martes y Viernes). Apuesta con vehemencia a goles al final de la jornada británica (Sábado/Domingo). Para entonces, las pesadas y rústicas piernas defensivas sufren colapsos musculares facilitando penetraciones incisivas de atacantes descansados.
</div>
"""

html_2 = """
<p class="lead">Las plazas sudamericanas cobijan monstruosos dictadores asimétricos; sin embargo, pocos imponen condiciones feudales de rentabilidad como el <strong>Poderío Paulista en suelo Brasileño</strong> ante rivales continentales de menor investidura.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Dictador Verde (Efecto Palmeiras)</li>
  <li>Hibridación del Gol Local Seguro</li>
  <li>Césped Sintético Paulista</li>
  <li>Pro-Tips: Apuesta al Descanso</li>
</ul>
</div>

<h2>El Dictador Verde (Efecto Palmeiras)</h2>
<p>Enfrentar formaciones de élite paulista bajo su techo es sinónimo de suplicio continental. La abismal diferencia de derechos televisivos permite a estos gigantes ostentar banquillos internacionales. Mientras un modesto equipo del Pacífico o los Andes reniega con presupuestos frágiles, el local lo aniquila a puro recambio y asfixia vertical.</p>

<h2>Césped Sintético Paulista y Velocidad</h2>
<p>A diferencia de la mayoría de terrenos irregulares sudamericanos, las alfombras sintéticas instaladas por los colosos (como el Allianz Parque) aceleran la pelota a velocidades indescifrables para defensores habituados al freno de pasto grueso. Esto induce autogoles, tropiezos y centros raudos imposibles de cortar. Apostar religiosamente al 'Gol Local' en estos menesteres supera el 95% de garantías puras.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Coberturar en la Primera Mitad</strong><br>
  El avasallamiento arranca desde el pitido del colegiado. Si la cuota por Gol Local está sumamente desplomada, arriésgate con cabeza en la proposición <i>"Gol del Equipo Local en la Primera Mitad"</i>. La intensidad estrangula al visitante casi invariablemente alrededor del minuto 25.
</div>
"""

html_3 = """
<p class="lead">Nada quiebra los moldes paramétricos en Europa como un encuentro donde el reloj asfixia a un bando condicionado por la deshonra de una masacre en el partido de Ida. <strong>La Psicología de ir cayendo (0-3)</strong> derroca todo protocolo apostador.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Suicidio Táctico Obligado (Remontada Imposible)</li>
  <li>Métricas de Córners y Desesperación</li>
  <li>Apostando en la Herida Abierta</li>
  <li>Pro-Tips: Ignorar al Oponente Defensor</li>
</ul>
</div>

<h2>El Suicidio Táctico Obligado</h2>
<p>Ingresar a tu estadio sabiendo que posees una factura letal de tres anotaciones arrastra a estrategas a emplear formaciones aberrantes, plantando defensores en la medular cual falsos delanteros. Este acto de rebeldía anárquica garantiza boquetes insólitos para el contraataque, desangrando la estadística histórica en un carnaval de 'Over de Goles' casi insano.</p>

<h2>Métricas de Córners y Desespero</h2>
<p>Cegado por el estruendo de la fanaticada, el ataque recae en oleadas por las bandas sin fineza. Esto se traduce paramétricamente en incesables desvíos esquineros. Cuando el AZ, en su ahogo, dispara contra bloques tapiados de hormigón (Ej: Shakhtar), el balón abandona impunemente la zona por el córner de manera continua catapultando la cuota del Value Bet por cielos europeos gloriosos.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Emparejamiento Multi-Mercado</strong><br>
  No subestimes el suicidio. Engloba en tu billete una combinación "Over de Goles" junto al "Over de Saques de Esquina del equipo desesperado". La correlación causa-efecto se alimenta de la misma fuente táctica al mismo instante.
</div>
"""

html_4 = """
<p class="lead">Las cartulinas en el césped rara vez se rigen exclusivamente por la ira de los jugadores. Se requiere descifrar con frialdad forense <strong>El Perfil del Árbitro en Escenarios Eliminatorios de la UEFA</strong> para extraer de sus sentencias una fortuna rentable.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>La Mano Dura de los Referees Estelares</li>
  <li>El Minutero Fatal: Fricción en Fase K.O.</li>
  <li>Frustración de Eliminados Locales</li>
  <li>Pro-Tips: Analizar la Tasa Promedio del Árbitro</li>
</ul>
</div>

<h2>La Mano Dura en UEFA</h2>
<p>En instancias concluyentes (Conference, Europa o Champions League), el colegio arbitral envía a delegados 'Tarjeteros' para purgar posibles trifulcas. Colegiados designados para duelos candentes mediterráneos (Italia, España) no otorgan concesiones; se acudan en plásticos tempranos cortando con bisturí cualquier intención de amotinamiento. </p>

<h2>Frustración de Eliminados</h2>
<p>Los duelos (Ej: Fiorentina vs Crystal Palace o Celta ante alemanes) amasan rencor conforme avanza la manecilla al minuto sesenta. La desesperanza de caer eliminados en propio terreno enciende una amargura en las piernas transformando interceptaciones limpias en hachazos frontales dolorosos. Amarrar al Over 4.5 Tarjetas a cuotas elevadas premia este colapso mental de los contendientes.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Las Bases de Datos Arbitrales</strong><br>
  Antes de ingresar al mercado, cruza siempre el nombre del árbitro (Tasa Amarilla por partido) designado el martes por UEFA, vis a vis con el historial de rojas históricas del torneo. Árbitros del este Europeo o Ibéricos dictaminan sentencias letales que aseguran la victoria estadística sin vacilación.
</div>
"""

create_article("ligas-ascenso-league-one-inglesa-apuestas", "Ligas de Ascenso (League One): El Paraíso Poroso", "Descifra por qué las carencias tácticas y calendarios brutales destapan rentabilidades infalibles en el Over mediante formaciones británicas descuidadas.", "Estadística Pro", "9", html_1)
create_article("palmeiras-localia-brasil-sudamericana-apuestas", "El Coloso Brasileño: Inversiones Seguras en Localías", "La minería oculta para resguardar presupuestos paramétricos aprovechando estadios intimidantes y césped sintético rápido de la élite de São Paulo.", "Guía táctica", "7", html_2)
create_article("psicologia-remontadas-imposibles-over-corners", "Psicología de la Goleada Global: Apostar a la Desesperación", "Extrae rentabilidades escondidas invirtiendo en el caos geométrico de saques de esquina avalados por esquemas suicidas forzados por el afán de remontar.", "Value Bet", "8", html_3)
create_article("perfil-arbitro-tarjetero-eliminatorias-uefa", "El Perfil del Árbitro Tarjetero en Eliminatorias UEFA", "La clave algorítmica y conductual para operar financieramente en escenarios K.O. pronosticando oleadas de amonestaciones y rojas dictaminadas estratégicamente.", "Ranking Árbitros", "8", html_4)

print("Articulos Abril 16 generados")
