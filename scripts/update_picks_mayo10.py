import re
import os

html_path = r"c:\Users\dany\Documents\GitHub\danniapuesta\index.html"

picks_js = """const PICKS_DATA = [
  {
    liga: "🇫🇷 Ligue 1",
    partido: "Paris SG vs Brest",
    fecha: "10 de mayo de 2026",
    pronostico: "Más de 0.5 Goles Local",
    cuota: "1.10",
    prob: 93,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DOMINIO HISTÓRICO:</strong><br>El PSG no ha perdido contra el Brest en sus últimos 14 enfrentamientos, manteniendo una superioridad táctica aplastante en el Parc des Princes.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA OFENSIVA:</strong><br>Con un promedio de 2.8 goles anotados por partido frente al Brest, la maquinaria ofensiva parisina garantiza constante asedio al área rival.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Fiabilidad extrema del 93%. Pick ideal para usar como Banker sólido en cualquier estrategia de apuestas combinadas.</div>"
  },
  {
    liga: "🇪🇸 La Liga",
    partido: "FC Barcelona vs Real Madrid",
    fecha: "10 de mayo de 2026",
    pronostico: "1X (Gana Barça o Empate)",
    cuota: "1.30",
    prob: 91,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FORTALEZA EN EL CAMP NOU:</strong><br>El Barcelona ostenta un récord inmaculado de 17 victorias en 17 partidos como local esta temporada. Un bastión inexpugnable.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. FACTOR ESTRATÉGICO:</strong><br>Con la liga casi en el bolsillo, un empate sentencia virtualmente el título a favor del Barça, obligando al Madrid a tomar riesgos desmedidos.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Probabilidad del 91% frente a una cuota que implica 76%. Detectado un altísimo Valor Esperado (EV+) en este mercado de Doble Oportunidad.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "West Ham vs Arsenal",
    fecha: "10 de mayo de 2026",
    pronostico: "Más de 1.5 Goles Totales",
    cuota: "1.25",
    prob: 89,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EFICIENCIA OFENSIVA GUNNER:</strong><br>Arsenal lidera la liga y genera un xG (Goles Esperados) masivo de 20.0, demostrando una pegada letal en el último tercio del campo.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. URGENCIA LOCAL:</strong><br>West Ham, asfixiado por el descenso, está forzado a atacar. Esto abrirá espacios críticos que Arsenal destrozará mediante transiciones rápidas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>89% de éxito estadístico. Un choque donde la necesidad choca con la calidad, garantizando un ritmo vertical y goles.</div>"
  },
  {
    liga: "🇳🇱 Eredivisie",
    partido: "Feyenoord vs AZ Alkmaar",
    fecha: "10 de mayo de 2026",
    pronostico: "Más de 1.5 Goles Totales",
    cuota: "1.18",
    prob: 87,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TENDENCIA GOLEADORA:</strong><br>La liga de los Países Bajos promedia más de 3.1 goles por partido. Este duelo histórico es sinónimo de juego abierto e intercambio de golpes.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ARSENAL OFENSIVO:</strong><br>Feyenoord llega invicto en sus últimos 8 duelos directos y el AZ ha marcado 12 goles en sus últimos 5 juegos. Explosividad asegurada.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Validación del 87%. Un mercado de Over muy conservador para dos de los equipos con mayor fluidez ofensiva de Europa.</div>"
  },
  {
    liga: "🇪🇸 La Liga",
    partido: "FC Barcelona vs Real Madrid",
    fecha: "10 de mayo de 2026",
    pronostico: "Más de 5.5 Tarjetas Totales",
    cuota: "1.65",
    prob: 86,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TENSIÓN DE CLÁSICO:</strong><br>Más allá de la rivalidad histórica, este partido decide la corona de España. La intensidad y la fricción física estarán al límite desde el minuto 1.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ESTADÍSTICA DISCIPLINARIA:</strong><br>Los Clásicos decisivos rompen todos los promedios normales. Las frustraciones y faltas tácticas para frenar contragolpes dispararán las amonestaciones.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>86% de confianza matemática para el over de tarjetas. El mercado disciplinario ofrece un valor brutal en este escenario específico.</div>"
  },
  {
    liga: "🇮🇹 Serie A",
    partido: "AC Milan vs Atalanta",
    fecha: "10 de mayo de 2026",
    pronostico: "Menos de 3.5 Goles Totales",
    cuota: "1.35",
    prob: 84,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. PRAGMATISMO TÁCTICO:</strong><br>En el tramo final de la temporada, el Milan ha priorizado la solidez de su bloque bajo, cumpliendo el Under 2.5 en 9 de sus últimos 11 partidos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ATASCO OFENSIVO:</strong><br>El Milan ha fallado en marcar más de 2 goles en sus últimos 9 cruces contra Atalanta, marcando un patrón rítmico cerrado y denso.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Probabilidad del 84%. Un colchón de hasta 3 goles permite cubrirse ante escenarios de partidos asfixiados típicos del Calcio italiano.</div>"
  },
  {
    liga: "🇸🇦 Saudi Pro League",
    partido: "Al Ittihad vs Damac",
    fecha: "10 de mayo de 2026",
    pronostico: "Gana Local + Más de 1.5 Goles",
    cuota: "1.40",
    prob: 82,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ASIMETRÍA DE TALENTO:</strong><br>La disparidad de plantillas es gigantesca. Las estrellas internacionales del Al Ittihad enfrentan a una defensa estructuralmente muy frágil.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. RODILLO EN CASA:</strong><br>El equipo local promedia 2.3 goles a favor en su estadio, resolviendo gran parte de sus encuentros por goleada desde la primera mitad.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>82% de confianza. Combinar la victoria directa con un over mínimo infla la cuota ofreciendo gran rentabilidad con bajo riesgo.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Burnley vs Aston Villa",
    fecha: "10 de mayo de 2026",
    pronostico: "Más de 0.5 Goles Visitante",
    cuota: "1.15",
    prob: 81,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. AMBICIÓN EUROPEA:</strong><br>Aston Villa pelea por consolidar la quinta posición y muestra una alta eficiencia goleadora fuera de casa, promediando 1.58 goles como visitante.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DEBILIDAD LOCAL:</strong><br>El Burnley es penúltimo en la liga, promediando apenas 0.88 goles en casa y concediendo espacios graves en transiciones defensivas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Probabilidad algorítmica del 81%. El Villa encontrará inevitablemente el fondo de la red frente a un sistema colapsado.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scottish Prem.",
    partido: "Celtic vs Rangers",
    fecha: "10 de mayo de 2026",
    pronostico: "Más de 1.5 Goles Totales",
    cuota: "1.22",
    prob: 79,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EL OLD FIRM DECISIVO:</strong><br>Este derbi es una final anticipada por el título. La tensión empujará a ambos equipos a buscar el gol, ya que el empate beneficia a terceros.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. FUEGO CRUZADO:</strong><br>Rangers es el equipo más goleador del torneo (69 goles) pero es incapaz de mantener su puerta a cero, concediendo goles en sus últimos 5 juegos.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>79% de probabilidad para el over bajo en un entorno hostil donde las defensas sufrirán el ritmo vertical escocés.</div>"
  },
  {
    liga: "🇳🇱 Eredivisie",
    partido: "Ajax vs Utrecht",
    fecha: "10 de mayo de 2026",
    pronostico: "Más de 2.5 Goles Totales",
    cuota: "1.45",
    prob: 77,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FRENESÍ GOLEADOR:</strong><br>El Utrecht llega en una racha absolutamente desatada, con partidos recientes que han producido un total de 19 goles en solo 4 fechas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. HISTÓRICO DE OVER:</strong><br>Este duelo tradicional holandés acostumbra a romper líneas de goles. El Over 3.5 se ha cumplido en 4 de los últimos 6 enfrentamientos.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Valor detectado en el 77%. Choque sin complejos tácticos defensivos, idóneo para capitalizar la alta volatilidad de la Eredivisie.</div>"
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

print("Picks data updated successfully for May 10!")
