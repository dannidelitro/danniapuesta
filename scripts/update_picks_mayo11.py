import re
import os

html_path = r"c:\Users\dany\Documents\GitHub\danniapuesta\index.html"

picks_js = """const PICKS_DATA = [
  {
    liga: "🇮🇹 Serie A",
    partido: "SSC Napoli vs Bologna",
    fecha: "11 de mayo de 2026",
    pronostico: "1X (Gana Napoli o Empate)",
    cuota: "1.25",
    prob: 84,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. BASTIÓN LOCAL:</strong><br>Napoli ha perdido solo 1 de sus 17 partidos en el Diego Maradona esta temporada, ostentando la cuarta mejor defensa de toda Italia.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. SEQUÍA VISITANTE:</strong><br>El Bologna atraviesa una profunda crisis ofensiva, acumulando cuatro partidos oficiales consecutivos sin lograr anotar un solo gol.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>84% de seguridad algorítmica. Un Banker absoluto para apuntalar cualquier apuesta combinada.</div>"
  },
  {
    liga: "🇸🇪 Allsvenskan",
    partido: "IK Sirius vs Örgryte IS",
    fecha: "11 de mayo de 2026",
    pronostico: "Victoria de IK Sirius",
    cuota: "1.45",
    prob: 82,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DOMINIO APLASTANTE:</strong><br>Sirius lidera la tabla con un arranque arrollador de 16 puntos sobre 18 y un demoledor diferencial de +10 goles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DEFENSA COLAPSADA:</strong><br>El visitante Örgryte se encuentra penúltimo y ya ha encajado la brutal cifra de 16 goles en apenas 6 encuentros ligueros.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Pick con un altísimo 82% de probabilidad real (EV+). La enorme asimetría de talento dictará sentencia rápidamente.</div>"
  },
  {
    liga: "🇵🇹 Primeira Liga",
    partido: "Benfica vs Sporting Braga",
    fecha: "11 de mayo de 2026",
    pronostico: "Más de 0.5 Goles Local",
    cuota: "1.12",
    prob: 81,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. INVENCIBILIDAD RÉCORD:</strong><br>Benfica es el único equipo invicto en toda la liga portuguesa tras 32 jornadas, promediando 2.44 goles a favor cuando juega en Da Luz.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA TÁCTICA:</strong><br>Braga tiene poderío ofensivo, lo que forzará al Benfica a atacar y no especular. Ambos equipos anotan en el 80% de los últimos juegos del Benfica.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>81% de fiabilidad para que el equipo local marque al menos un gol. Apuesta de base perfecta.</div>"
  },
  {
    liga: "🇵🇹 Primeira Liga",
    partido: "Benfica vs Sporting Braga",
    fecha: "11 de mayo de 2026",
    pronostico: "Más de 9.5 Corners Totales",
    cuota: "1.50",
    prob: 78,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DESBORDE LATERAL:</strong><br>Benfica somete a sus rivales promediando 7.1 corners por partido en casa, utilizando transiciones rápidas por las bandas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. RESPUESTA VISITANTE:</strong><br>Braga no es un equipo que se encierre; genera un promedio de 5.3 corners por encuentro, aportando volumen periférico.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Con un 78% de probabilidad geométrica, este choque directo por la parte alta promete juego ancho y saques de esquina constantes.</div>"
  },
  {
    liga: "🇪🇸 La Liga",
    partido: "Rayo Vallecano vs Girona",
    fecha: "11 de mayo de 2026",
    pronostico: "1X (Gana Rayo o Empate)",
    cuota: "1.40",
    prob: 77,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FORTÍN VALLECANO:</strong><br>El Rayo no conoce la derrota en casa desde enero y, lo que es clave, no ha perdido un solo partido este año tras anotar el primer gol.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DEBACLE CATALANA:</strong><br>El Girona atraviesa una severa crisis, sumando tres derrotas consecutivas y sin lograr una victoria de visitante en todo el 2026.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Probabilidad del 77% (EV+ Alto). La solidez anímica del Rayo contrasta con el desplome absoluto del Girona en este tramo final.</div>"
  },
  {
    liga: "🇷🇺 Russian Premier",
    partido: "Dinamo Moscú vs Krasnodar",
    fecha: "11 de mayo de 2026",
    pronostico: "X2 (Empate o Krasnodar)",
    cuota: "1.38",
    prob: 76,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. LÍDERES METÓDICOS:</strong><br>El Krasnodar domina la liga sustentado en la mejor defensa del país, habiendo concedido apenas 21 goles en todo el campeonato.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. INCONSISTENCIA MOSCOVITA:</strong><br>El Dinamo es capaz de anotar, pero su debilidad atrás (38 goles en contra) es su talón de Aquiles ante rivales de élite.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>76% de fiabilidad para la visita. Krasnodar pelea el título palmo a palmo y su muralla defensiva asegura al menos puntuar.</div>"
  },
  {
    liga: "🇵🇹 Primeira Liga",
    partido: "Rio Ave vs Sporting CP",
    fecha: "11 de mayo de 2026",
    pronostico: "Más de 1.5 Goles Totales",
    cuota: "1.20",
    prob: 76,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. PÓLVORA EN ATAQUE:</strong><br>Sporting cuenta con el pichichi Luis Suárez (26 goles) y ha anotado un impresionante promedio de 2.6 goles por partido este año.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. TENDENCIA H2H:</strong><br>Sporting CP ha superado al Rio Ave en sus últimos 5 enfrentamientos directos anotando un promedio de 2.8 goles en cada cruce.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>76% de probabilidad matemática. Mercado altamente confiable dada la explosividad del líder ofensivo portugués.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Tottenham vs Leeds United",
    fecha: "11 de mayo de 2026",
    pronostico: "Más de 1.5 Goles Totales",
    cuota: "1.22",
    prob: 74,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DÉFICIT DEFENSIVO LOCAL:</strong><br>Las lesiones en la zaga central del Tottenham provocan desajustes. El 75% de sus últimos 12 juegos terminaron en Over de goles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. FACTOR CALVERT-LEWIN:</strong><br>El ariete del Leeds llega encendido (12 goles). Los últimos 7 enfrentamientos entre estos clubes superaron holgadamente la línea.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Modelo predictivo del 74%. Expectativa de partido abierto, roto tácticamente y con transiciones veloces de área a área.</div>"
  },
  {
    liga: "🇩🇰 Superliga",
    partido: "Randers FC vs Odense BK",
    fecha: "11 de mayo de 2026",
    pronostico: "Más de 1.5 Goles Totales",
    cuota: "1.25",
    prob: 74,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. MATEMÁTICA NÓRDICA:</strong><br>La liga danesa es una de las más dinámicas de Europa, promediando más de 3.04 goles por partido durante esta temporada.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. VOLUMEN ESTADÍSTICO:</strong><br>El Over 1.5 goles ha sucedido en el 74% de la totalidad de los partidos jugados en esta liga. Son números inquebrantables.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Probabilidad algorítmica calcada al promedio de la liga (74%). Choque físico y directo que garantiza ocasiones continuas.</div>"
  },
  {
    liga: "🇵🇱 Ekstraklasa",
    partido: "Cracovia vs Radomiak Radom",
    fecha: "11 de mayo de 2026",
    pronostico: "X2 (Empate o Radomiak)",
    cuota: "1.55",
    prob: 62,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ESTADO DE FORMA:</strong><br>Radomiak llega con impulso tras ganar 3 de sus últimos 5 encuentros, mostrando gran cohesión defensiva y contraataque.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ESTANCAMIENTO LOCAL:</strong><br>Cracovia es el rey de las igualadas (12 empates en 31 jornadas) y sufre muchísimo para generar juego ofensivo sostenido en casa.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>62% de éxito estimado frente a un mercado de cuotas equivocado. El mayor Valor Esperado (EV+) detectado en la jornada de hoy.</div>"
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

print("Picks data updated successfully for May 11!")
