import re

picks_html = """const PICKS_DATA = [
  {
    liga: "🇩🇪 Bundesliga (Alemania)",
    partido: "VfB Stuttgart vs Hamburg SV",
    fecha: "12 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.30",
    prob: 82,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. MONSTRUO LOCAL:</strong><br>Stuttgart es un león indomable en casa, garantizando volumen con sus abrumadores 2.3 goles promedio a su favor bajo el cobijo de su grada perimetral.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. BAJAS CRÍTICAS DEL HAMBURGO:</strong><br>La escuadra visitante viaja profundamente accidentada en su bloque inferior, perdiendo la estructura de cierre en la zaga.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Un festín táctico a merced del local donde observar menos de dos tantos asomaría como una rareza matemática inconcebible hoy.</div>"
  },
  {
    liga: "🇳🇱 Eredivisie (Países Bajos)",
    partido: "PSV Eindhoven vs Sparta",
    fecha: "12 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 93,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SUPREMACÍA ABSOLUTA:</strong><br>Ningún adjetivo describe mejor el dominio del PSV; su inercia letal le impulsa a quebrar la portería enemiga más de 3 veces por aparición en promedio.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. SUMISIÓN DEL SPARTA:</strong><br>Visitar Eindhoven para ellos significa un muro inquebrantable donde aguantar el arco a cero radica fuera del terreno de la realidad empírica.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Un Banker mayúsculo; 93% de probabilidad consolida la inyección de capital sobrevolando este suceso aislado infalible.</div>"
  },
  {
    liga: "🇳🇱 Eredivisie (Países Bajos)",
    partido: "Fortuna Sittard vs NAC Breda",
    fecha: "12 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.30",
    prob: 90,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. LA RACHA DORADA:</strong><br>El Fortuna acarrea consigo la anomalía estadística del año: 14 jornadas al hilo cruzando el espectro de dos o más dianas con una precisión ridícula.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. SISTEMAS ROTOS:</strong><br>Junto al Breda promueven un juego fracturado exento de la media cancha que empuja todo asedio invariablemente hacia ambos extremos guardametas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Una probabilidad paramétrica por encima del 90%. No hay forma concebible de que las porterías cierren frías esta cita pactada.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Chelsea vs Manchester City",
    fecha: "12 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.35",
    prob: 77,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CONFRONTACIÓN ELITE (XG):</strong><br>Se enfrentan dos plantillas que atesoran un Expected Goals combinado monumental ascendente a 3.71, cifras dignas de ligas lúdicas, no del rigor inglés.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. FULGOR OFFENSIVO:</strong><br>La presencia amenazante de Haaland y las variables rápidas por banda de Stamford Bridge aseguran castigo irrebatible sobre las áreas penalizadas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Superar los 2 goles en un choque de tildes absolutos recubre una alta rentabilidad que jamás depara defensivas estáticas (77%).</div>"
  },
  {
    liga: "🇫🇷 Ligue 1 (Francia)",
    partido: "O. Lyon vs Lorient",
    fecha: "12 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.35",
    prob: 76,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TENDENCIA VERTICAL ALTA:</strong><br>El Olympique factura invariablemente en los dominios de su estadio, sometiendo agresivamente la tibia contención mostrada constantemente por Lorient.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA OFENSIVA (xG):</strong><br>Las escapadas periféricas lionenses se asoman determinantes forzando la apertura rápida y prematura en un duelo con inclinaciones asimétricas galas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Teniendo defensas propensas a sucumbir por empuje mediático, la cuota abraza gran valor encestando matemáticamente lo presupuestado.</div>"
  },
  {
    liga: "🇮🇹 Serie A (Italia)",
    partido: "Inter Milán vs Como 1907",
    fecha: "12 de abril de 2026",
    pronostico: "Más Córners (Inter Empate Apuesta No Válida)",
    cuota: "1.80",
    prob: 79,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ASEDIO AL BLOQUE BAJO:</strong><br>Inter ancla y empuja al rival en su propia telaraña. Su dominio de bandas resulta lógicamente aplastante frente al conservador repliegue cerrojo propuesto por Como 1907.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. EXCESO ASIMÉTRICO DE DESPEJES:</strong><br>Con todo el equipo visitante encerrado, cualquier disparo milanista generará cortes a la desesperada arrojando múltiples cobros esquineros exclusivamente para los dueños.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Inter dominando estadísticas de tiros perimetrales bajo un hándicap es la apuesta estelar de altísima probabilidad hoy, evadiendo fallos tontos de marcador.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Mallorca vs Rayo Vallecano",
    fecha: "12 de abril de 2026",
    pronostico: "Más de 9.5 Córners",
    cuota: "1.85",
    prob: 77,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FACTORÍA DE BANDA ABSOLUTA:</strong><br>Rayo Vallecano empuña un historial dantesco cobrando por encima de este espectro en 25 de unas 27 citas, producto de desbordes sistemáticos de sus aleros madrileños.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. COLISIÓN ISLEÑA:</strong><br>En Son Moix se fraguará un juego denso lateral; Mallorca obligará incesantemente rechazos que nutren maravillosamente las estadísticas angulares requeridas por el parlay.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Es el diamante de Tiros de Esquina paramétrico; la racha española raya lo surreal y las casas aún temen endurecer la línea base (77%).</div>"
  },
  {
    liga: "🇵🇹 Primeira Liga (Portugal)",
    partido: "Benfica vs Nacional",
    fecha: "12 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 90,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TACTICISMO HEGEMÓNICO:</strong><br>Las águilas sostienen el misticismo impoluto del invicto de local aplastando inescrupulosamente cualquier propuesta visitante con arsenal pesado constante.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA FRAGMENTADA:</strong><br>Nacional no compite en métricas ofensivas ni defensivas contra el coloso luso. Ceder un gol se traduce como el mal menor presupuestado desde el pitazo.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Firmeza del 90%. Una perla puramente consolidada para armar boletas robustas aniquilando incertidumbres matemáticas en el proceso.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Athletic Club vs Villarreal",
    fecha: "12 de abril de 2026",
    pronostico: "Más de 5.5 Tarjetas",
    cuota: "1.90",
    prob: 85,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FISURA SANCIONADORA (ÁRBITRO):</strong><br>Se cuenta con la adjudicación imperiosa de un colegiado caracterizado formalmente por su gatillo veloz superando medias de 5.5 cobros en cartulinas históricas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. VERTIGINOSIDAD VASCA:</strong><br>San Mamés dicta choques frenéticos; el empuje del submarino amarillo incitará a fricciones agresivas directas al botín para destrabar embates contragolpeadores de los Leones.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Un partido encadenado obligatoriamente por el perfil clínico del juzgador. Línea de altísimo valor que garantiza recolectar booking points desde la hora inicial.</div>"
  },
  {
    liga: "🇳🇱 Eredivisie (Países Bajos)",
    partido: "Fortuna Sittard vs NAC Breda",
    fecha: "12 de abril de 2026",
    pronostico: "Ambos Anotan (Sí)",
    cuota: "1.80",
    prob: 78,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SINCRONÍA DEL CAOS:</strong><br>El bloque Sittard arrastra el maleficio irrenunciable: tal cual perforan impunemente las redes frontales, sufren de igual proporción los castigos a su portero solitario de retrocesos nulos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA RECTIFICADORA:</strong><br>Breda asiste pertrechado a vulnerar flancos desguarnecidos, forzando la apertura holandesa a la estridencia de un toma y daca continuo que garantiza dianas a cada extremo.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Estadística purpura holandesa. El Both Teams To Score descansa plácidamente protegido bajo la sombrilla del valor en esta liga propiciadora.</div>"
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
