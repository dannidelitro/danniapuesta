import re
import os

html_path = r"c:\Users\dany\Documents\GitHub\danniapuesta\index.html"

picks_js = """const PICKS_DATA = [
  {
    liga: "🇪🇸 La Liga",
    partido: "Real Madrid vs Real Oviedo",
    fecha: "14 de mayo de 2026",
    pronostico: "1X (Gana Madrid o Empata)",
    cuota: "1.06",
    prob: 96,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SUPREMACÍA BLANCA:</strong><br>El Madrid ha ganado 14 de sus 17 partidos en el Bernabéu esta temporada. La diferencia de jerarquía frente al colista de LaLiga es insalvable.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. SEQUÍA DEL OVIEDO:</strong><br>El equipo asturiano solo ha ganado 1 de 14 partidos como visitante y lleva dos jornadas sin poder anotar un solo gol.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>96% de probabilidad. El pick más seguro de toda la jornada. Ideal para usar como \"banker\" en combinadas de bajo riesgo.</div>"
  },
  {
    liga: "🇺🇸 MLS",
    partido: "FC Cincinnati vs Inter Miami",
    fecha: "14 de mayo de 2026",
    pronostico: "Ambos Equipos Marcan",
    cuota: "1.30",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TENDENCIA ABSOLUTA:</strong><br>Cincinnati presenta un registro perfecto: el 100% de sus partidos en casa han terminado con goles de ambos equipos esta temporada.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. EL FACTOR MESSI:</strong><br>Miami tiene un ataque demoledor pero sufre mucho atrás, concediendo 2.0 goles por partido como visitante. Intercambio de golpes garantizado.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Fiabilidad extrema del 92%. Duelo eléctrico en la Conferencia Este con alta proyección de xG para ambos conjuntos.</div>"
  },
  {
    liga: "🇨🇭 Superliga Suiza",
    partido: "FC Thun vs Young Boys",
    fecha: "14 de mayo de 2026",
    pronostico: "Ambos Equipos Marcan",
    cuota: "1.36",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CAMPEÓN RELAJADO:</strong><br>El FC Thun ya aseguró el título. Jugar sin presión defensiva suele derivar en partidos abiertos y marcadores muy abultados.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. PROYECCIÓN xG:</strong><br>El modelo estadístico proyecta 3.53 goles esperados para este encuentro, marcando una fuerte tendencia hacia el BTTS (Ambos Anotan).</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>92% de éxito estimado. El Young Boys buscará herir al campeón en un partido donde las defensas pasarán a un segundo plano.</div>"
  },
  {
    liga: "🇧🇾 Vysshaya Liga",
    partido: "FC Gomel vs Baranovichi",
    fecha: "14 de mayo de 2026",
    pronostico: "1X (Gana Gomel o Empata)",
    cuota: "1.18",
    prob: 89,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. MERCADOS OCULTOS:</strong><br>Las ligas de Europa del Este ofrecen gran rentabilidad porque los mercados globales no ajustan sus cuotas con la misma precisión que en las ligas top.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. SOLIDEZ LOCAL:</strong><br>El Gomel presenta un claro dominio estructural y una racha ofensiva superior en sus últimos 5 encuentros ligueros.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Probabilidad del 89%. Un ancla de seguridad fantástica extraída mediante análisis profundo de ligas secundarias.</div>"
  },
  {
    liga: "🇪🇸 La Liga",
    partido: "Real Madrid vs Real Oviedo",
    fecha: "14 de mayo de 2026",
    pronostico: "Más de 8.5 Corners Totales",
    cuota: "1.55",
    prob: 85,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ASEDIO MERENGUE:</strong><br>El Madrid promedia 16.5 tiros por partido. Este volumen de ataque constante generará múltiples despejes del portero y defensas al banderín.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LLEGADAS POR BANDA:</strong><br>Con extremos desequilibrantes buscando línea de fondo, el equipo blanco suele superar la línea de 10 corners en casa con suma facilidad.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>85% de confianza (EV+ Elevado). Excelente alternativa a las bajas cuotas de victoria directa del Real Madrid.</div>"
  },
  {
    liga: "🇸🇦 Saudi Pro League",
    partido: "Al Ettifaq vs Al Ittihad",
    fecha: "14 de mayo de 2026",
    pronostico: "Más de 1.5 Goles Totales",
    cuota: "1.18",
    prob: 83,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CHOQUE DE TRENES:</strong><br>El Ettifaq de Gerrard viene de ganar 5-0 y choca contra un Ittihad con mayor profundidad de plantilla internacional. Promedios goleadores muy altos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CALOR EXTREMO:</strong><br>A pesar de que los 39°C previstos ralentizarán el ritmo, la fatiga térmica multiplicará los errores defensivos en la segunda mitad.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>83% de viabilidad para una cuota base muy consistente. La pólvora ofensiva en Arabia garantiza movimiento en el marcador.</div>"
  },
  {
    liga: "🇺🇸 MLS",
    partido: "Seattle Sounders vs San Jose",
    fecha: "14 de mayo de 2026",
    pronostico: "1X (Gana Seattle o Empata)",
    cuota: "1.28",
    prob: 82,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. MURO DEFENSIVO:</strong><br>Seattle ha convertido su estadio en un fortín, concediendo apenas 0.50 goles por partido y secando a los ataques rivales.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CRISIS VISITANTE:</strong><br>San Jose tiene un 0% de victorias como visitante esta temporada, con una paupérrima media de 0.33 goles anotados a domicilio.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>82% de probabilidad estadística. Es muy difícil imaginar a San Jose marcando un gol, lo que asegura el empate o victoria local.</div>"
  },
  {
    liga: "🇨🇭 Superliga Suiza",
    partido: "FC Sion vs FC Lugano",
    fecha: "14 de mayo de 2026",
    pronostico: "1X (Gana Sion o Empata)",
    cuota: "1.35",
    prob: 78,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DUELO DIRECTO:</strong><br>Cuarto contra Tercero. Sion llega con la inercia a tope tras vencer al campeón (Thun), mostrando un nivel altísimo de confianza.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. FISURAS EN LUGANO:</strong><br>El equipo visitante ha mostrado debilidades defensivas tras su reciente derrota, lo que reduce drásticamente sus opciones de ganar fuera de casa.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>78% de fiabilidad para proteger el bankroll. El equipo local cuenta con mejores métricas tácticas en este momento de la temporada.</div>"
  },
  {
    liga: "🇪🇸 La Liga",
    partido: "Real Madrid vs Real Oviedo",
    fecha: "14 de mayo de 2026",
    pronostico: "Más de 3.5 Tarjetas Totales",
    cuota: "1.65",
    prob: 77,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FRUSTRACIÓN VISITANTE:</strong><br>El Oviedo es el equipo más indisciplinado del torneo con 10 rojas esta temporada. La desesperación defensiva generará múltiples faltas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. FALTAS TÁCTICAS:</strong><br>Para evitar ser goleados al contragolpe por los extremos veloces del Madrid, los defensores asturianos tendrán que recurrir al juego brusco repetidamente.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>Gran valor (77% prob). Una línea de 3.5 tarjetas es muy baja para el contexto de presión al que estará sometida la zaga visitante.</div>"
  },
  {
    liga: "🇺🇸 MLS",
    partido: "Seattle Sounders vs San Jose",
    fecha: "14 de mayo de 2026",
    pronostico: "Más de 9.5 Corners Totales",
    cuota: "1.60",
    prob: 75,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. PATRÓN VISITANTE:</strong><br>San Jose compensa su terrible falta de gol abusando de los centros laterales. Promedian un brutal volumen de 7.3 saques de esquina a favor.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DESPEJES DEL MURO:</strong><br>Seattle se encerrará si toma ventaja y se dedicará a despejar los tibios embates de San Jose hacia la línea de fondo.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DEL SISTEMA:</strong><br>75% de confianza. Un pick inteligente que aprovecha un patrón oculto en un equipo perdedor pero muy activo en las bandas.</div>"
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

print("Picks data updated successfully for May 14!")
