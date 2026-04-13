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
    html = re.sub(r'<span>\d+ de \w+ de 2026</span>', '<span>13 de abril de 2026</span>', html)
    html = re.sub(r'<span>⏱.*?</span>', f'<span>⏱ {read_time} min de lectura</span>', html)
    
    body_pattern = r"<h1>.*?</h1>.*?<div class=\"cta-box\">"
    new_body = f"<h1>{title}</h1>\n{html_content}\n      <div class=\"cta-box\">"
    html = re.sub(body_pattern, new_body, html, flags=re.DOTALL)
    
    os.makedirs(fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}", exist_ok=True)
    path = fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}\index.html"
    with codecs.open(path, "w", "utf-8") as f:
        f.write(html)

html_1 = """
<p class="lead">Las Ligas Menores y los Torneos Filiales ("Jong", "Sub-23") esconden el oro puro de las casas de apuestas deportivas. Hoy desmenuzaremos la inmensa anomalía detrás de las escuelas formadoras en países bajos y la estrategia empírica para amasar rentabilidad mediante el mercado de "Over de Goles".</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Principio de la Cantera Táctica</li>
  <li>Ligas Menores Holandesas: Minería del Over 1.5</li>
  <li>Psicología del Defensor Juvenil y el BTTS</li>
  <li>Pro-Tips: Evitar los "Días de Convocatorias Internacionales"</li>
  <li>FAQ</li>
</ul>
</div>

<h2>El Principio de la Cantera Táctica</h2>
<p>Diferente a un Club que pelea descensos al borde de la bancarrota (con técnicos paranoicos jugando 0-0), en los campeonatos de filiales (Como la <i>Eerste Divisie</i> de Países Bajos), las academias prohíben el "juego feo" destructivo. Las escuadras como "Jong Ajax" o "Jong AZ" rigen su desempeño bajo un manual donde atacar vertiginosamente a través de transiciones verticales constituye el 100% de la formación de los jóvenes. El retroceso y la asfixia son conceptualizaciones secundarias. </p>

<h2>Ligas Menores Holandesas: Minería del Over 1.5</h2>
<p>Apostar que un partido entre fuerzas juveniles rebasará los 2 goles es la inversión con mayor Win Rate a nivel internacional de los apostadores en Asia ("Over Asiático"). Las proezas perimetrales alcanzan hitos lúgubres para porteros donde rachas monstruosas exhiben 18 partidos ininterrumpidos reventando las porterías contrarias. La ingenuidad táctica de los centrales sumados a transiciones frenéticas abren el partido a un correcalles irreversible.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Convocatorias al Primer Equipo</strong><br>
  El mayor talón de Aquiles para esta apuesta yace en no revisar las redes oficiales de las canteras. Ocasionalmente, la plantilla estelar sufre una horda de lesiones y suben temporalmente de urgencia a los goleadores del Jong al fin de semana, dejando al filial huérfano de peso artillero y arruinando el esperado festín goleador dominical.
</div>
"""

html_2 = """
<p class="lead">Las casas comerciales de América cuantifican brutalmente cada factor contextual, salvo un fantasma silente implacable: <strong>El Agotamiento por Altitud y el Calor Agobiante</strong>. Desgranamos por qué el Local Invencible es una falacia y por qué es una certeza rentable al apoyarse meteorológicamente con la estadística de gol cerrado.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>Más allá del Muro de los Aficionados</li>
  <li>La Ventaja Fisiológica de los Metros Sobre el Nivel del Mar</li>
  <li>Aplicación Matemática del "Gol De Equipo Local"</li>
  <li>Pro-Tips: El Horario Matinal Fúnebre</li>
</ul>
</div>

<h2>Más allá del Muro de los Aficionados</h2>
<p>Un equipo no arrastra 18 partidos o series titánicas de imbatibilidad porque todos posean talentos extraterrestres. Estadios enclavados como la cancha infernal toluqueña representan un hándicap que el mercado estándar de visitante jamás pondera acertadamente. El ahogo hipóxico aniquila la musculatura del adversario tras transcurridos los primeros plenos treinta minutos del duelo.</p>

<h2>La Ventaja Fisiológica</h2>
<p>El "Gol de Equipo Local" en estadios que gozan simultáneamente de altura, racha de dos dígitos invictos y horarios dominicales de sol punzante (12:00PM), suponen la cúspide matemática predictiva. El XG del local incrementa absurdamente en la fase agónica (Minuto 60 al 90) ya que enfrentan una línea de zagueros visitantes mermados por asfixia celular.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Coberturas Combinadas</strong><br>
  No ciegues tu presupuesto con solo gol, anida de igual manera la inversión "Gana Cualquier Mitad" a favor del monstruo local aclimatado; si de forma extraña sucumben pronto, sus abismales remontadas en la altitud suelen asegurar ganar contundentemente la segunda etapa física al arrinconar al contrincante agónico.
</div>
"""

html_3 = """
<p class="lead">Huir del mercado sobre "Ganador Directo" ante un derbi fiero de proporciones geopolíticas tensas es el acto sagrado de la prudencia. La inversión táctica superior anida perennemente sobre el caótico <strong>Mercado del "Total de Tarjetas"</strong> en regiones ríspidas balcánicas o estepas orientales.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>Derbis Históricos: La Sangre Domina Toda Táctica</li>
  <li>La Cuantificación del Mercado Búlgaro y Balcánico</li>
  <li>Los Colegiados Presionados</li>
  <li>Pro-Tips: "No Terminarán 11 Contendientes"</li>
</ul>
</div>

<h2>Derbis Históricos: La Sangre Domina Toda Táctica</h2>
<p>Encuentros polarizados desde antaño, donde la demografía e idiosincrasias religiosas confluyen en conatos violentos; es la premisa empírica superior del 'Over Booking' (exceso de cartulinas). El fútbol en los balcanes traslada formaciones frías e incorpora factores psicológicos del orgullo regional superando por mera estadística el XG disciplinario proyectado para Ligas Convencionales.</p>

<h2>Los Colegiados Presionados</h2>
<p>Es un suicidio para un árbitro de la confederación balcánica intentar perdonar pisotones arteros iniciales amparado por un discurso conciliador "british". Los ambientes del fuego pirotécnico fuerzan el silbato de acero y el desenfunde prematuro. Con líneas irrisorias estipuladas entre 5.5 o 6 tarjetas, el porcentaje de acierto por encima del umbral cruza la robusta validación del +85% en data histórica confirmada.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: La Inversión Complementaria de la Roja</strong><br>
  Al invertir sobre un "Over Violento", adjunta al plan algorítmico una mínima fracción presupuestal respaldando firmemente el mercado "¿Habrá Tarjeta Roja? -> SÍ". Cuotas por encima de 2.20 recompensan exponencialmente el caos desenfrenado cuando las amarillas múltiples maduran indefectiblemente en expulsiones obligadas.
</div>
"""

html_4 = """
<p class="lead">Las plataformas encubren tesoros bajo capas laberínticas, siendo sus diamantes pulidos apuestas de márgenes ignorados, entre estos destaca el "Mercado de Tiros de Esquina <strong>Exclusivamente por Equipo Individual</strong>", esquivando dependencias fútiles.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Peligro del 'Over Combinado' Clásico</li>
  <li>El Dominador Monopolista (Team Corners)</li>
  <li>Anatomía de los Despejes Rotos Lentos</li>
  <li>Pro-Tips: Transiciones por Extremos Argentinos</li>
</ul>
</div>

<h2>El Peligro del 'Over Combinado' Clásico</h2>
<p>La inmensa mayoría acude religiosamente al "Over 9.5 Córners". Sin embargo, frente a disparidades abismales entre colosos asediadores de banda y rivales colistas arrinconados; requieres ciegamente colaboración esquina por parte de un visitante pálpido y hundido que jamás rebasará ni el círculo mediano, colapsando frustrantemente el monto final.</p>

<h2>El Dominador Monopolista (Team Corners)</h2>
<p>La cura universal proviene del <i>Asimétrico Individual</i>: El apostante aísla matemáticamente al Goliat hegemónico (ej. River Plate o Bayern Múnich) e impone una rentabilidad sobre una barrera estúpidamente ridícula para ellos (Ej: Más de 3.5 Córners Exclusivamente para el gigante). El Gigante arquetípico empuja al rival forzando barridas al banderín de forma reiterativa independientemente de cualquier auxilio ofensivo opositor, blindando un ticket rentable en extremo.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Laterales y Perfiles A Pierna Cambiada</strong><br>
  No toda súper maquinaria genera un asedio esquinero. Estudia la plantilla; si el equipo arrollador asienta perfiles 'A pierna cambiada' dictos a acortar hacia adentro penal (recortes diagonales buscando portería frontal), los tiros perimetrales caerán. El over córner florece bajo conjuntos provistos de flechas veloces, laterales y carrileros obstinados en rasgar perpendicularmente buscando inyectar balones en centros altos hacia el área chica.
</div>
"""

create_article("apuestas-ligas-filiales-jong-goles", "Apuestas en Ligas Filiales (Jong): Minería del Futbol Ofensivo", "Estrategia asiática secreta para obtener un asombroso Win-Rate mediante el mercado Goleador Over 1.5 analizando escuelas formativas holandesas.", "Guía táctica", "7", html_1)
create_article("clima-altura-gol-equipo-local", "El Factor Fortaleza: Rachas Locales y la Fisiología de la Altura", "Aprovechando ventajas atmosféricas y agónicas para apostar científicamente al 'Gol de Equipo Local' y aniquilar falacias de estadios difíciles.", "Estadística Pro", "8", html_2)
create_article("derbis-este-europa-tarjetas-apuestas", "Derbis Balcánicos del Este: El Paraíso de Apuestas por Tarjetas", "Beneficiándose financieramente de rivalidades históricas de choque y del comportamiento forense sancionador bajo árbitros condicionados de alta letalidad.", "Ranking Árbitros", "8", html_3)
create_article("corners-asimetricos-individual-equipo", "Córners Asimétricos o de Equipo: Evadiendo a los Rivales Inútiles", "Aísla el XG perimetral del gran dominador dictaminando la destrucción y despejes constantes hacia el córner usando la táctica del Team Corner Individual.", "Value Bet", "7", html_4)

print("done")
