import re
import os

html_path = r"c:\Users\dany\Documents\GitHub\danniapuesta\index.html"

picks_js = """const PICKS_DATA = [
  {
    liga: "🇪🇸 La Liga",
    partido: "Real Betis vs Elche CF",
    fecha: "12 de mayo de 2026",
    pronostico: "1X (Gana Betis o Empata)",
    cuota: "1.22",
    prob: 88,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FORTALEZA EN LA CARTUJA:</strong><br>El Betis mantiene una racha impecable de 9 partidos invicto jugando en condición de local, consolidando una solidez defensiva letal en su feudo.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DESPLOME EN SEGUNDAS PARTES:</strong><br>El Elche ha encajado 21 goles en los segundos tiempos como visitante, evidenciando graves problemas de concentración en los cierres de partido.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>88% de fiabilidad para el 1X. Una base de altísima seguridad que permite anclar cualquier apuesta combinada con total tranquilidad.</div>"
  },
  {
    liga: "🇸🇦 Saudi Pro League",
    partido: "Al Nassr vs Al Hilal",
    fecha: "12 de mayo de 2026",
    pronostico: "Más de 1.5 Goles Totales",
    cuota: "1.25",
    prob: 88,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. PODERÍO OFENSIVO IDÉNTICO:</strong><br>Los dos colosos árabes promedian exactamente 2.6 goles por partido, cifras monstruosas impulsadas por astros como Cristiano Ronaldo y Benzema.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LUCHA POR EL TÍTULO:</strong><br>Separados por apenas 2 puntos en la cima, el empate sirve de poco, lo que obligará a ambos a tomar riesgos tácticos severos en las áreas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>88% de probabilidad real. Un mercado conservador (Over 1.5) para dos equipos diseñados exclusivamente para perforar redes.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scottish Prem.",
    partido: "Dundee Utd vs Livingston",
    fecha: "12 de mayo de 2026",
    pronostico: "Más de 8.5 Corners Totales",
    cuota: "1.40",
    prob: 88,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ESTILO NÓRDICO VERTICAL:</strong><br>El fútbol escocés en el grupo de descenso se vuelve extremadamente directo, saltando líneas y buscando centros constantes al área.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DESESPERACIÓN VISITANTE:</strong><br>Livingston está virtualmente descendido y necesita atacar con balones largos, lo que históricamente deriva en constantes saques de esquina a favor y en contra.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Valor gigantesco del 88%. El modelo estadístico de corners detecta aquí uno de los desajustes de cuotas más claros de la jornada europea.</div>"
  },
  {
    liga: "🇪🇸 La Liga",
    partido: "Celta Vigo vs Levante UD",
    fecha: "12 de mayo de 2026",
    pronostico: "Más de 0.5 Goles Local",
    cuota: "1.18",
    prob: 82,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FRAGILIDAD VISITANTE:</strong><br>Levante lucha por no descender pero su defensa concede una brutal media de 1.6 goles por partido, dejando enormes huecos al contragolpe.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. REGULARIDAD GALLEGA:</strong><br>A pesar de su irregularidad general, el Celta ha logrado anotar al menos un gol en el 82% de sus compromisos como local esta temporada.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Probabilidad del 82%. Apostar a que el Celta rompe el cero es estadísticamente casi seguro frente a un esquema defensivo colapsado.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scottish Prem.",
    partido: "Aberdeen vs St. Mirren",
    fecha: "12 de mayo de 2026",
    pronostico: "Más de 8.5 Corners Totales",
    cuota: "1.45",
    prob: 80,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. MÁQUINA DE SAQUES:</strong><br>St. Mirren pertenece a la élite de córners de la liga, promediando 5.7 saques de esquina a favor gracias a su amplitud de bandas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. INDISCIPLINA TÁCTICA:</strong><br>Aberdeen comete excesivas faltas y fuerza despejes constantes cerca de su banderín, elevando drásticamente la media periférica.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Con un 80% de EV+, este mercado es mucho más rentable y seguro que intentar adivinar quién se llevará los 3 puntos en un duelo tan trabado.</div>"
  },
  {
    liga: "🇿🇦 Premier S.L.",
    partido: "TS Galaxy vs M. Sundowns",
    fecha: "12 de mayo de 2026",
    pronostico: "Victoria Mamelodi Sundowns",
    cuota: "1.37",
    prob: 79,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SUPREMACÍA ABSOLUTA:</strong><br>Sundowns domina Sudáfrica a placer (68 puntos) y llega con un impecable invicto de 10 jornadas, asfixiando tácticamente a sus rivales.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ASIMETRÍA DE PLANTILLAS:</strong><br>El TS Galaxy, ubicado en la 12ª plaza, carece de las herramientas ofensivas necesarias para perforar la defensa visitante.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Probabilidad del 79% para el líder. Un pick clásico de apuesta por asimetría que ofrece una excelente cuota para combinadas de 2 o 3 eventos.</div>"
  },
  {
    liga: "🇪🇸 La Liga",
    partido: "Osasuna vs Atl. Madrid",
    fecha: "12 de mayo de 2026",
    pronostico: "Más de 0.5 Goles Local",
    cuota: "1.30",
    prob: 76,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. RACHA HISTÓRICA:</strong><br>El dato es demoledor: Osasuna ha marcado al menos un gol en todos y cada uno de sus últimos 38 partidos jugados en El Sadar.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ATLÉTICO MERMADO:</strong><br>Simeone llega con la moral tocada tras caer en Champions y con bajas defensivas críticas como la de Giménez que desajustan su línea de 5.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>76% de fiabilidad. Confiar en la increíble constancia goleadora rojilla en Pamplona tiene un inmenso valor ante un gigante herido.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scottish Prem.",
    partido: "Kilmarnock vs Dundee FC",
    fecha: "12 de mayo de 2026",
    pronostico: "Más de 2.5 Goles Totales",
    cuota: "1.65",
    prob: 75,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TENDENCIA MATEMÁTICA:</strong><br>Se han superado los 2.5 goles en 9 de los últimos 11 encuentros del Dundee FC, marcando un patrón de juego extremadamente roto.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LUCHA DE DESCENSO:</strong><br>En esta fase del Relegation Group escocés, especular equivale a descender, lo que genera partidos de ida y vuelta constantes y transiciones suicidas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>75% de confianza (EV+ Elevado). La cuota es muy alta para un partido donde el historial (últimos 3 H2H) siempre ha roto la barrera del Over.</div>"
  },
  {
    liga: "🇸🇦 Saudi Pro League",
    partido: "Al Nassr vs Al Hilal",
    fecha: "12 de mayo de 2026",
    pronostico: "Más de 9.5 Corners Totales",
    cuota: "1.55",
    prob: 72,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FUEGO CRUZADO LARRERAL:</strong><br>Los equipos grandes saudíes basan su juego en extremos rápidos. Al Hilal promedia 6.2 corners en solitario como visitante.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ASFIXIA EN EL ÁREA:</strong><br>El duelo de pistoleros entre Cristiano y Benzema asegura decenas de disparos a puerta que los porteros desviarán al banderín.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>72% de probabilidad. Un mercado alternativo excelente para quienes prefieren evadir la volatilidad del 1X2 en un derbi tan intenso.</div>"
  },
  {
    liga: "🇪🇬 Premier Egypt.",
    partido: "El Gouna vs K. Ismailia",
    fecha: "12 de mayo de 2026",
    pronostico: "Menos de 2.5 Goles Totales",
    cuota: "1.45",
    prob: 66,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EL CERROJO EGIPCIO:</strong><br>La liga egipcia es, junto a la marroquí, una de las ligas con menor promedio de goles del mundo, priorizando un juego táctico, denso y lento.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. SEQUÍA ESTRUCTURAL:</strong><br>Ambos equipos sufren de severos problemas creativos en el último tercio y suelen conformarse con empates 0-0 o 1-1 como visitantes.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>66% de fiabilidad detectada por RatingBet. El típico pick de paciencia que castiga a los apostadores que solo buscan overs emocionantes.</div>"
  }
];"""

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

new_html = re.sub(
    r"const PICKS_DATA = \[.*?\];", 
    picks_js, 
    html_content, 
    flags=re.DOTALL
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Picks data updated successfully for May 12!")
