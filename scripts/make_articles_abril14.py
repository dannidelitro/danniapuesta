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
    html = re.sub(r'<span>\d+ de \w+ de 2026</span>', '<span>14 de abril de 2026</span>', html)
    html = re.sub(r'<span>⏱.*?</span>', f'<span>⏱ {read_time} min de lectura</span>', html)
    
    body_pattern = r"<h1>.*?</h1>.*?<div class=\"cta-box\">"
    new_body = f"<h1>{title}</h1>\n{html_content}\n      <div class=\"cta-box\">"
    html = re.sub(body_pattern, new_body, html, flags=re.DOTALL)
    
    os.makedirs(fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}", exist_ok=True)
    path = fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}\index.html"
    with codecs.open(path, "w", "utf-8") as f:
        f.write(html)

html_1 = """
<p class="lead">Las Ligas Sudamericanas gozan de un prestigio mundial por su garra, sin embargo, la <strong>Copa Libertadores</strong> eleva el concepto de "juego brusco" a un arte milimétrico. Descubre cómo aprovechar económicamente este factor con el mercado de Tarjetas.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Factor Cultural: La Fricción como Táctica</li>
  <li>Árbitros Sudamericanos y el Control Teatral</li>
  <li>Paraguayos vs Colombianos: El Choque de Estilos</li>
  <li>Pro-Tips: Apostar a la Roja Directa</li>
</ul>
</div>

<h2>El Factor Cultural: La Fricción como Táctica</h2>
<p>A diferencia de la Champions League, donde impera la transición relámpago, en Sudamérica la retención del balón suele castigarse severamente. Enfrentamientos entre paraguayos (ej. Cerro Porteño) conocidos por el rigor aéreo y contacto, frente a equipos del caribe colombiano o brasileños habilidosos, originan embudos violentos en el medio campo y alas donde la destrucción es el único parámetro de defensa.</p>

<h2>Árbitros Sudamericanos y el Control Teatral</h2>
<p>La CONMEBOL posee un criterio arbitral extremadamente peculiar. Los árbitros son forzados a desenfundar cartulinas en los primeros 15 minutos solo para apaciguar reclamos desmedidos. Esto rompe la tranquilidad del Over 5.5 tempranamente sumando cuotas doradas a las carteras de los apostadores en línea.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Apostar a la Roja Directa</strong><br>
  No te limites a las Amarillas. Es matemáticamente prudente invertir el 10% de tu Stake diario del <i>Over Tarjetas</i> hacia el mercado secundario "Habrá Tarjeta Roja (SÍ)" debido a la histeria que se vive en los minutos finales (del 80 en adelante) buscando resultados heroicos.
</div>
"""

html_2 = """
<p class="lead">No todas las remontadas huelen a goles. A menudo se manifiestan en un gigantesco atropello territorial que genera un oro inadvertido para el analista asertivo: <strong>Un frenesí de Tiros de Esquina</strong>.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El "Efecto Remontada" Global</li>
  <li>Psicología del Equipo Defensor en UCL</li>
  <li>El Córner Monopolizado</li>
  <li>Pro-Tips: Carrileros a Pierna Natural</li>
</ul>
</div>

<h2>El "Efecto Remontada" Global</h2>
<p>Cuando un gigante europeo cae en el partido de ida (Ej. Psg vs Liverpool o Barcelona contra el Atlético), el partido de vuelta dicta que se debe empujar descaradamente hacia el bloque bajo del rival. Esto desencadena un bombardeo por los costados. En vez de chocar inútilmente por el centro, los equipos amplían el campo abocando a defensas a barrer el balón a las banderas de esquina.</p>

<h2>El Córner Monopolizado</h2>
<p>Las cuotas por "Over 9.5 Córners" se fracturan rápidamente y se cumplen sin requerir contribución alguna del equipo visitante o del bando asediado. Observarás cómo un solo club amasa cifras brutales como 12 saques de esquina aislados cimentando toda tu rentabilidad paramétrica.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Carrileros a Pierna Natural</strong><br>
  Si el club necesita un aluvión en el área chica, sus carrileros no recortarán hacia el centro; enviarán centros llovidos profundos. Asegúrate en las formaciones iniciales que coloquen extremos que dominen el pie natural de la banda (Ejemplo: Zurdo por izquierda) para multiplicar la estadística de rechaces.
</div>
"""

html_3 = """
<p class="lead">Pocos eventos brindan disparidades cualitativas tan abismales y mal calculadas como las <strong>Copas Domésticas (Ej: US Open Cup)</strong>, donde nóminas de 100 millones destrozan oncenas semi-profesionales, garantizando el preciado "Over Híbrido".</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Factor Motivacional de las Divisiones Inferiores</li>
  <li>Sistemas Abiertos vs Sistemas Conservadores</li>
  <li>Evadiendo al Bando Favorito Exhausto</li>
  <li>Pro-Tips: BTTS en Torneos de Copa</li>
</ul>
</div>

<h2>El Factor Motivacional de las Divisiones Inferiores</h2>
<p>En Copa, los clubes inexpugnables de la Segunda B o Ligas Regionales (Ej: Westchester en EEUU) saltan amparados por un exceso de éxtasis físico. Esta sobredosis aeróbica produce partidos rotos y sorpresas mayúsculas en los primeros 45 minutos. Los goles suben vertiginosamente al marcador forzando respuestas furiosas del equipo mayor.</p>

<h2>El Efecto Del Sistema Abierto (Rotaciones)</h2>
<p>Los colosos de la categoría premium suelen mezclar suplentes e improvisar parejas centrales que jamás han jugado minutos sumados. Este divorcio táctico provoca desbarajustes colosales concediendo el tanto a las divisiones pequeñas, haciendo que la apuesta <i>Ambos Anotan (Sí)</i> se pague exorbitantemente bien ignorando que las defensas son parches endebles temporales.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Evitar el Mercado a Ganador Directo</strong><br>
  Las reglas de la Copa y las rotaciones destrozan bancas incautas. Acude religiosamente al "Over 1.5 Cíclico" o "Más Goles", donde no importa qué suplente resbale catastróficamente; únicamente cuenta que se inflen las redes en partidos propensos para los atacantes estelares.
</div>
"""

html_4 = """
<p class="lead">Saber buscar donde el mundo no mira forja el imperio financiero apostador. Las ligas de Europa del Este ostentan un Rey hegemónico, y respaldarlo en el modesto mercado del <strong>Gol de Equipo Local</strong> encierra la receta secreta.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Hegemón de Liga (El Efecto Ferencváros)</li>
  <li>Disparidades de Nómina Faraónicas</li>
  <li>Cuotas Refugio y Stake Seguro</li>
  <li>Pro-Tips: Los Parones Invernales</li>
</ul>
</div>

<h2>El Hegemón de Liga (El Efecto Ferencváros)</h2>
<p>En campeonatos como Hungría, Croacia, República Checa o Escocia antigua, existen equipos diseñados presupuestalmente para disputar Fase de Grupos Europea. Este presupuesto masivo dictamina tiranía absoluta en su hogar contra el modesto noveno lugar de la tabla, con un XG proyectado sencillamente brutal e indetenible desde los primeros instantes.</p>

<h2>Disparidades de Nómina Faraónicas</h2>
<p>Al estudiar la plantilla de locales colosales se aprecia que su delantero estrella cuadruplica económicamente al plantel rival en pleno. Seleccionar "El Equipo Local Goleará en Cualquier Etapa (Más de 0.5)" ampara un margen paramétrico con un 92% a 95% de asertividad global infalible. Las casas no pueden bajar la cuota a menos de 1.10 y ello forma cimientos robustos si armamos apuestas combinadas calculadas seriamente (Parlays).</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Combinación Estratégica Conservadora</strong><br>
  Si descubres una cuota de 1.25 ante un dictador local, anéctala en conjunción con otro pronóstico seguro asiático (como un Over de Corners). Subirás el precio total cerca de un jugoso 2.0 y disfrutarás un ticket respaldado estadísticamente en un inmenso 90%.
</div>
"""

create_article("copa-libertadores-tarjetas-apuestas-rentabilidad", "Copa Libertadores y Tarjetas: Rentabilizando la Fricción", "Explota analíticamente las disputas feroces latinoamericanas mediante el Value Bet en los mercados profundos de las amonestaciones y rojas directas.", "Guía táctica", "8", html_1)
create_article("efecto-remontada-champions-over-corners", "El Efecto Remontada en Copas Europeas: Saques de Esquina", "Invierte con seguridad ante escenarios de eliminación directa y el bombardeo lateral apostando a líneas de Over Córnets Asimétricos y Totales.", "Avanzado", "7", html_2)
create_article("copas-domesticas-us-open-btts-goles", "Copas Domésticas (US Open/FA Cup): Explotando el BTTS", "Beneficiándose analíticamente de los esquemas rotativos suplentes de la primera división y el frenesí insostenible de los equipos inferiores buscando fama.", "Value Bet", "8", html_3)
create_article("hegemon-liga-menor-europa-este-local", "El Hegemón del Este: Minería Segura en el Gol Local", "Descubre las rentabilidades encubiertas operando financieramente sobre cuotas conservadoras ancladas a localías avasalladoras de las Ligas Menores.", "Inbound", "7", html_4)

print("Articulos Abril 14 generados")
