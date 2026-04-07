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
    
    # Replace tag pill styling
    html = re.sub(r'<span style="background: rgba\(0,180,216,0\.1\).*?</span>', f'<span style="background: rgba(0,180,216,0.1); color: #00b4d8; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; border: 1px solid rgba(0,180,216,0.2);">{tag}</span>', html)
    # Update date
    html = re.sub(r'<span>\d+ de \w+ de 2026</span>', '<span>7 de abril de 2026</span>', html)
    html = re.sub(r'<span>⏱.*?</span>', f'<span>⏱ {read_time} min de lectura</span>', html)
    
    body_pattern = r"<h1>.*?</h1>.*?<div class=\"cta-box\">"
    new_body = f"<h1>{title}</h1>\n{html_content}\n      <div class=\"cta-box\">"
    html = re.sub(body_pattern, new_body, html, flags=re.DOTALL)
    
    path = fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}\index.html"
    with codecs.open(path, "w", "utf-8") as f:
        f.write(html)

html_1 = """
<p class="lead">Las métricas de Expected Goals (xG) y el rendimiento implícito en instancias eliminatorias de UEFA Champions League ofrecen una oportunidad monumental para mercados de goles. Un escenario representativo es el encuentro entre Real Madrid y Bayern Múnich.</p>
<h2>Volumen Ofensivo Sostenido</h2>
<p>El análisis cuantitativo revela que el Real Madrid genera un volumen de ataque devastador bajo presión, registrando un altísimo promedio. Han superado la línea de 1.5 goles en 28 de sus últimos 30 enfrentamientos (una absurdidad del 93.3% de impacto). Esta dinámica empuja el xG del Madrid a los márgenes superiores de 2.15 por juego.</p>
<div class="box highlight">
<p><strong>El Colapso de la Probabilidad Bivalente:</strong> Cuando dos equipos manejan niveles de xG superlativos (Bayern maneja 2.84), la probabilidad matemática pura de que rompan la barrera del "Ambos Anotan" se dispara hasta el 71%. Las debilidades posicionales a la contra del Bayern nutren directamente la letalidad de Vinicius y Rodrygo.</p>
</div>
<p>Invertir en ambos pronostican en cuotas cercanas a 1.20 - 1.30 y la combinada del BTTS representa uno de los movimientos matemáticamente más blindados del mercado europeo. Jamás apuestes en Champions guiándote por escudos, apóyate siempre en el valor puro del Expected Goal a mediano plazo.</p>
"""

html_2 = """
<p class="lead">El factor del campo y del clima son parámetros cualitativos recurrentes en las apuestas deportivas. Sin embargo, pocos ofrecen una alteración cuantitativa tan drástica sobre todas las probabilidades base como el fútbol jugado a más de 4.000 metros de altitud.</p>
<h2>Always Ready: Fortaleza Condicionada</h2>
<p>En el estadio Municipal de El Alto (a 4.150 metros de altura), el esfuerzo fisiológico asfixiante destruye el esquema táctico del visitante durante las segundas mitades. Esto es lo que justifica que cuadros como Always Ready acumulen una asombrosa racha de 22 partidos consecutivos anotando como locales en Bolivia.</p>
<div class="mini-grid">
  <div class="mini-card"><strong>Efecto Altitud</strong><br><span style="color:#b7c9e4">Aumenta la densidad de errores defensivos un 27% a partir del min 60.</span></div>
  <div class="mini-card"><strong>Always Ready Media</strong><br><span style="color:#b7c9e4">Alcanzan un descomunal promedio de 4.0 goles por partido en casa.</span></div>
</div>
<p>Visitas como LDU Quito, aunque históricamente preparadas, llegan a estas citas bajo severas bajas o caídas de rendimiento general. Un pronóstico de "Gol Equipo Local" con probabilidad de confianza al 98% no es una corazonada: es una ley estadística impuesta por un contexto donde la oxigenación inclina irreversiblemente el campo.</p>
"""

html_3 = """
<p class="lead">Dentro del ecosistema de predicciones de apuestas, los apostadores profesionales suelen encontrar mayor rentabilidad (Closing Line Value) en el mercado de tarjetas (Booking Points) que en el tradicional 1-X-2. Hoy observamos un caso de estudio primigenio: Sporting CP contra Arsenal en torneos continentales.</p>
<h2>Perfiles Disciplinarios y Tolerancia Arbitral</h2>
<p>El mercado de tarjetas no depende primariamente de los equipos, sino de una triangulación estadística: la necesidad de fricción defensiva, el estilo de recuperación de balón y vitalmente, el perfil histórico del árbitro designado.</p>
<p>Cuando un juego define clasificaciones vitales bajo árbitros que promedian más de 5 tarjetas por partido, apostar al "Over 3.5 o 4.5 Tarjetas" se convierte en una vía muy lucrativa, situando sus cuotas entre 1.70 y 1.90 de forma injustificadamente generosa por las casas de apuestas.</p>
<div class="box warning">
<p>En choques nórdicos como el Nordsjaelland frente al Brondby, la frustración por malas rachas ofensivas (Brondby) dispara exponencialmente el volumen de faltas no forzadas. Aquí radica la diferencia entre apostar ciego al ganador, o apostar a la desesperación medible en amarillas.</p>
</div>
"""

html_4 = """
<p class="lead">Mientras la liquidez excesiva inunda eventos como LaLiga o la Premier, mercados menos escrutados como divisiones secundarias de Polonia o Gales proporcionan agujeros de valor gigantes para el análisis métrico (Value Bets). Miedz Legnica o Wrexham son minas de oro.</p>
<h2>Miedz Legnica y la Inversión en Córners</h2>
<p>En el fútbol polaco, el Miedz lidera agresivamente su liga forzando un absurdo promedio de 7.04 córners por partido a solas. Un esquema fundamentado en explosión por bandas que convierte la cuota de "Over 10.5 Córners Combinados" (a rondando el 1.90) en una jugada estadística con 78% de cobertura intrínseca.</p>
<h2>La Fricción de la Championship y Goleadas en Gales</h2>
<p>El Wrexham sigue asombrando al mundo en su localía, anotando en 24 de sus últimos 25 compromisos. Sin embargo, sufren filtraciones severas que permiten recibir, en particular ante cuadros agresivos (como un eventual cruce de Copa ante estilo Southampton con BTTS garantizado al 69%).</p>
<p>No huyas de las ligas menores. Encuentra las tendencias irrefutables, compara la línea proyectada de Poisson con las casas de apuestas, e invierte sin piedad.</p>
"""

import os
# Create the folders if they don't exist
os.makedirs(r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\analisis-xg-real-madrid-bayern", exist_ok=True)
os.makedirs(r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\apuestas-altitud-always-ready", exist_ok=True)
os.makedirs(r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\mercado-tarjetas-sporting-arsenal", exist_ok=True)
os.makedirs(r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\corners-btts-ligas-menores", exist_ok=True)

create_article("analisis-xg-real-madrid-bayern", "El Valor del xG en Champions: Real Madrid vs Bayern", "Análisis matemático y estadístico (xG) para exprimir rentabilidad ofensiva en la UCL.", "Champions League", "5", html_1)
create_article("apuestas-altitud-always-ready", "El Factor Altura en Apuestas: El Caso Always Ready", "Cómo los 4.150 metros imponen un 98% de probabilidad matemática para el gol local.", "Guía táctica", "4", html_2)
create_article("mercado-tarjetas-sporting-arsenal", "Apostar en el Mercado de Tarjetas y Árbitros", "Desglose analítico de Booking Points en eliminatorias como Sporting vs Arsenal.", "Estrategia", "5", html_3)
create_article("corners-btts-ligas-menores", "Extraer Value en Córners y BTTS: Torneos Menores", "El oro oculto de Polonia y Gales para los inversores estadísticos de tiros de esquina.", "Córners", "4", html_4)

print("done")
