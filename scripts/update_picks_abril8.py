import re

picks_html = """const PICKS_DATA = [
  {
    liga: "🌎 Copa Libertadores",
    partido: "Junior FC vs Palmeiras",
    fecha: "8 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.35",
    prob: 85,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DINÁMICA OFENSIVA DEL LOCAL:</strong><br>Junior ha convertido su estadio en una fortaleza generadora de peligro, superando la estricta marca del Over 1.5 goles de manera combinada en sus últimos 11 encuentros en condición de local.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LLEGADA BASTA DEL VERDÃO:</strong><br>Palmeiras aterriza en Barranquilla con uno de los estados de forma más letales de Sudamérica, ostentando un agresivo promedio de 2.0 goles a favor por cotejo.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La colisión de dos estilos diseñados para el frente a frente vaticina redes infladas. Pronóstico cubierto en un blindado 85% matemático.</div>"
  },
  {
    liga: "🇪🇺 UEFA Champions League",
    partido: "PSG vs Liverpool",
    fecha: "8 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.35",
    prob: 79,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. PODERÍO EN TRANSICIÓN:</strong><br>Dos de las escuadras con las transiciones al sprint más aterradoras de Europa cara a cara. Sus líneas de presión alta forzarán inevitablemente desconexiones en las zonas limítrofes del área.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. PRODUCCIÓN EXTREMA DE xG:</strong><br>El Expected Goals (xG) combinado dicta una absoluta carnicería táctica: un 2.32 local contra un feroz 2.94 visitante. Las métricas predicen volumen de área incesante.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Apostar a un empate nulo o de mínima cuota (0-0 o 1-0) contradice cualquier ley matemática del fútbol moderno. El over 1.5 es un refugio altamente asegurado.</div>"
  },
  {
    liga: "🌎 CONCACAF Champions",
    partido: "D. Toluca vs LA Galaxy",
    fecha: "8 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.30",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ESTRAGO FISIOLÓGICO:</strong><br>Los 2.600 metros de altitud de la Bombonera de Toluca implican un desgaste pulmonar que históricamente fractura el bloque bajo de equipos estadounidenses (MLS) durante los segundos 45 minutos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ESTADÍSTICA DE ASEDIO ABSOLUTO:</strong><br>El plantel choricero está promediando la exorbitante cifra de 22.5 tiros por contienda cuando actúa de local. El asedio a portería es garantizado.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La asimetría del campo impulsará al LA Galaxy contra su área. El mercado de 'Toluca Anota (Sí)' flirtea con el 92% de cumplimiento táctico, un Banker estelar.</div>"
  },
  {
    liga: "🇪🇺 UEFA Champions League",
    partido: "Barcelona vs Atlético Madrid",
    fecha: "8 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.40",
    prob: 76,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DEFICIENCIA ROJIBLANCA:</strong><br>Atrás quedaron los años del candado indescifrable asimétrico del Atlético. Sus recientes salidas continentales arrojan 15 dianas encajadas en apenas 8 juegos de Champions League.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LLEGADA CULÉ CONSTANTE:</strong><br>El Barcelona ha recuperado su fluidez en el último cuarto de cancha, asegurando un rango amplio de inmersiones al área que obligarán al meta esloveno a intervenir continuamente.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Con un Atlético obligado a marcar en un cruce definitivo ante un Barça altamente incisivo, el mercado del 1.5 goles aglutina un 76% de rentabilidad proyectada.</div>"
  },
  {
    liga: "🇪🇺 UEFA Champions League",
    partido: "PSG vs Liverpool",
    fecha: "8 de abril de 2026",
    pronostico: "Ambos Anotan (Sí)",
    cuota: "1.80",
    prob: 61,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ASIMETRÍA DE ÉLITE:</strong><br>Se enfrentan dos escuadrones cuyas fortalezas radican en aniquilar las defensas desubicadas, aunque sus propios repliegues sufren frente al talento desequilibrante individual.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. INERCIA ESPECTÁCULO:</strong><br>La demanda global y la predisposición técnica instiga un pulso sin medios campos cerrados, multiplicando las variables de error forzado atrás.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>A pesar de postrarse con un 61% (riesgo moderado), la jugosa cuota abraza el Value puro en base a transiciones demoledoras donde es inevitable ver ambos marcadores moverse de 0.</div>"
  },
  {
    liga: "🌎 CONCACAF Champions",
    partido: "D. Toluca vs LA Galaxy",
    fecha: "8 de abril de 2026",
    pronostico: "Más de 9.5 Córners",
    cuota: "1.85",
    prob: 74,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. VERTICALIDAD LATERAL PURA:</strong><br>Galaxy es un equipo concebido para jugar con el ancho de la parcela, promediando masivos 8.3 córners por sí solo debido a su estilo ininterrumpido en la MLS.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. PRESIÓN CHORICERA LOCAL:</strong><br>Toluca ahogará la salida forastara forzando cortes urgentes que acabarán inevitablemente en despejes por la línea de cal trasera del arco.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La combinación de un visitante volcado al borde y un local disparador consolida este Over 9.5 como un Value Bet de altísima solidez estadística.</div>"
  },
  {
    liga: "🇹🇷 Superliga (Turquía)",
    partido: "Goztepe vs Galatasaray",
    fecha: "8 de abril de 2026",
    pronostico: "Más de 8.5 Córners",
    cuota: "1.80",
    prob: 78,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. LA MÁQUINA DE CONQUISTA:</strong><br>El gran Galatasaray sustenta el enorme grueso de su poderío ofensivo perimetral ostentando un asombroso 6.8 de promedio en tiros de esquina producidos per cápita.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DESBORDES AL LÍMITE:</strong><br>El repliegue medio del Goztepe incitará a la visita a forzar múltiples bloqueos y rechazos ante embestidas constantes que derivarán en saques desde la bandera.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Cruzar el umbral del Over 8.5 es en teoría un paseo aritmético sustentado en un generoso 78% y una asimetría táctica idónea para este mercado secundario.</div>"
  },
  {
    liga: "🇪🇺 UEFA Champions League",
    partido: "Barcelona vs Atlético Madrid",
    fecha: "8 de abril de 2026",
    pronostico: "Más de 5.5 Tarjetas",
    cuota: "1.90",
    prob: 75,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EL FACTOR HISTÓRICO:</strong><br>La tensión implícita de una eliminatoria de esta magnitud se superpone a uno de los cruces naturalmente más accidentados y friccionados del registro futbolístico español.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. UMBRAL TÁCTICO ROTO:</strong><br>Cualquier robo de balón provocará cortes malintencionados. Este pleito promedia cerca del hito de 8 plásticos históricamente cuando hay piques a matar o morir involucrados.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Los Booking Points resplandecen en el Over 5.5 cubiertos por cuotas fantásticas, validado por métricas contundentes apuntalando la desesperación de quien vaya perdiendo transitoriamente.</div>"
  },
  {
    liga: "🇪🇺 UEFA Champions League",
    partido: "PSG vs Liverpool",
    fecha: "8 de abril de 2026",
    pronostico: "Más de 4.5 Tarjetas",
    cuota: "1.85",
    prob: 72,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. PERFIL RIGUROSO DEL COLEGIADO:</strong><br>Asignación de un cuerpo arbitral intolerante al choque escalado, acumulando una línea roja base de 5.33 tarjetas para aplacar los connatos en su registro trimestral en Europa.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LUCHA CARA A CARA:</strong><br>Las subidas a velocidad ultrasónica obligarán a frenados por agarrón, castigados directamente con amarilla automática, exacerbando el clima disciplinario.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Un partido tenso y muy transitado entre dos fuerzas sin freno dictamina la probabilidad robusta (+72%) para desgranar un mínimo de 5 amonestaciones de control central.</div>"
  },
  {
    liga: "🌎 Copa Libertadores / Sud.",
    partido: "Cusco FC vs Flamengo",
    fecha: "8 de abril de 2026",
    pronostico: "Ambos Anotan (Sí)",
    cuota: "2.25",
    prob: 49,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. INFLUENCIA DE ALTITUD PERUANA:</strong><br>Cusco exprime letalmente su reducto en las nubes oxigenando su esquema local, convirtiendo una anotación a favor en una formalidad fisiológica al paso de los minutos de exigencia.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. TALENTO TÉCNICO BRASILEÑO:</strong><br>Flamengo está plagado de calidades estelares y resolución rápida, capaces de facturar mediante destellos puramente individuales a pesar de flaquear grupalmente por la falta de oxígeno.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Con probabilidad en la fina línea del 49%, este pronóstico funge como una obra de extra Value Bet puro, ya que la cuota inflada por el hándicap climático compensa colosalmente el riesgo inverso de la localía.</div>"
  }
];"""

file_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

pattern = r"const PICKS_DATA = \[.*?\];"
new_text = re.sub(pattern, picks_html, text, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Updated index.html PICKS_DATA")
