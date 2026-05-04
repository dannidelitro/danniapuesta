import re, codecs

picks_html = r"""const PICKS_DATA = [
  {
    liga: "🇸🇦 Saudi Pro League",
    partido: "Al Ittihad vs Al Kholood",
    fecha: "4 de mayo de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.12",
    prob: 94,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. xG PROYECTADO DE 3.59:</strong><br>El modelo de Goles Esperados proyecta 3.59 para este partido. Al Ittihad tiene un xGF en casa de 2.21, mientras que Al Kholood concede un xGA de visitante de 1.38. La convergencia ofensiva es abrumadora.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. INEFICIENCIA DE CUOTAS:</strong><br>El mercado asigna 89% de probabilidad, pero el modelo proyecta 94%. Esa diferencia de +5% es valor real. Al Kholood (14°, 30 pts) tiene ausencias defensivas que han provocado caída de cuotas Over de 1.58 a 1.40.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. VEREDICTO:</strong><br>Al Ittihad invicto en 7 de sus últimos 8 en casa. Uno de los picks con mayor valor esperado positivo de toda la jornada.</div>"
  },
  {
    liga: "🇵🇹 Liga Portugal",
    partido: "Sporting CP vs Vitória SC",
    fecha: "4 de mayo de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.12",
    prob: 93,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. 16 DE 16 PARTIDOS CON OVER 1.5:</strong><br>El Sporting ha superado la línea de 1.5 goles en sus últimos 16 partidos consecutivos. Con 73 goles en la temporada (2.48/partido) y Luis Suárez con 25 goles, la producción ofensiva es la más alta de Portugal.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. VITÓRIA CONCEDE EN EL 87% DE SUS PARTIDOS:</strong><br>Solo mantiene portería a cero en el 13% de los casos. Con una media de 1.39 goles concedidos y H2H recientes de 4-1, 2-0 y 4-4, este enfrentamiento siempre produce goles.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. VEREDICTO:</strong><br>93% de probabilidad. La racha más consistente de Over 1.5 en toda Europa. Sporting con 205 tiros a puerta acumulados esta temporada.</div>"
  },
  {
    liga: "🇳🇴 Eliteserien",
    partido: "Bodø/Glimt vs Molde",
    fecha: "4 de mayo de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.15",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. RÉCORD PERFECTO EN LA TEMPORADA:</strong><br>El 100% de los partidos del Bodø/Glimt esta temporada han superado 1.5 goles (6 de 6). Promedian 3.33 goles totales por encuentro, la cifra más alta de Escandinavia.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DOMINIO LOCAL ABSOLUTO:</strong><br>8 goles a favor y 0 en contra en sus últimos 2 partidos en casa. Ganan ambas mitades en el 67% de sus juegos. Posesión del 67% con 7.8 córners a favor por partido.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. VEREDICTO:</strong><br>Racha perfecta de 100% Over 1.5. El Molde (6°) es ofensivo, lo que alimenta aún más el volumen de goles. Pick con altísima fiabilidad.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scottish Premiership",
    partido: "Hearts vs Rangers",
    fecha: "4 de mayo de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.22",
    prob: 88,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. 17 PARTIDOS INVICTO EN CASA:</strong><br>El Hearts lidera la liga (73 pts) con la mejor racha local de Escocia. Promedia 1.88 goles en casa con solo 0.59 concedidos. Ha marcado en sus últimos 5 partidos consecutivos en Edimburgo.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CONTEXTO DE TÍTULO:</strong><br>Lucha directa por el campeonato (Hearts 73 pts vs Rangers 69 pts). La presión de no perder puntos en casa garantiza máximo esfuerzo ofensivo desde el inicio.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. VEREDICTO:</strong><br>88% de probabilidad. La eficiencia de conversión del 13.89% y la imbatibilidad local hacen de este uno de los picks más seguros del día.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Everton vs Manchester City",
    fecha: "4 de mayo de 2026",
    pronostico: "Gol Equipo Visitante",
    cuota: "1.18",
    prob: 87,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. HAALAND: 24 GOLES, 1.29/PARTIDO:</strong><br>Erling Haaland es el máximo goleador de la Premier con 24 goles y un promedio brutal de 1.29 por partido. Con el City persiguiendo al Arsenal (70 vs 76 pts), cada punto es crítico.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DOMINIO POSICIONAL DEL CITY:</strong><br>496 pases por partido con 86% de precisión generan un asedio constante. El Everton (11°, 47 pts) no tiene la estructura defensiva para resistir 90 minutos sin conceder.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. VEREDICTO:</strong><br>87% de probabilidad. El City necesita ganar para mantener la presión sobre Arsenal. La calidad individual de Haaland hace que el gol visitante sea casi inevitable.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Chelsea vs Nottingham Forest",
    fecha: "4 de mayo de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.30",
    prob: 81,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CONVERGENCIA OFENSIVA DE AMBOS:</strong><br>Chelsea xG de 1.92/partido con Joao Pedro (14 goles) y Cole Palmer (9 goles). El Forest llega en racha de 6 invicto (5-0 al Sunderland, 4-1 al Burnley). Ambos están en forma goleadora.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CHELSEA VULNERABLE EN CÓRNERS:</strong><br>Han concedido 11 goles desde saques de esquina esta temporada (peor cifra desde 1994/95). El Forest puede capitalizar esto. Combinado con 6.15 córners/partido del Chelsea, el volumen de oportunidades es alto.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. VEREDICTO:</strong><br>81.4% de probabilidad. H2H recientes: 3-2, 3-0, 1-1. Estos equipos siempre producen goles cuando se enfrentan.</div>"
  },
  {
    liga: "🇩🇰 Superligaen",
    partido: "Midtjylland vs Viborg",
    fecha: "4 de mayo de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.30",
    prob: 80,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. PRODUCCIÓN LOCAL CONSTANTE:</strong><br>El Midtjylland (2°, 58 pts) promedia 2.31 goles por partido. En la ronda de campeonato danesa, la intensidad competitiva eleva las cifras goleadoras respecto a la fase regular.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. VIBORG CON LIMITACIONES:</strong><br>El Viborg (4°, 43 pts) tiene una diferencia de 15 puntos con el Midtjylland. Probabilidad de victoria del Midtjylland: 52.86%. Over 8 córners: 63.56%.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. VEREDICTO:</strong><br>79.8% de probabilidad para Over 1.5. Cuota atractiva para una liga con patrones goleadores predecibles en inicio de temporada.</div>"
  },
  {
    liga: "🇮🇹 Serie A",
    partido: "Roma vs Fiorentina",
    fecha: "4 de mayo de 2026",
    pronostico: "Más de 3.5 Tarjetas",
    cuota: "1.55",
    prob: 78,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FIORENTINA LÍDER EN AMARILLAS:</strong><br>La Fiorentina es el equipo con más tarjetas amarillas de la Serie A 2025/26, con 2.26/partido. Como visitante mantiene 2.24. La Roma promedia 1.88, lo que proyecta una línea de 4.14 tarjetas por partido.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. TENSIÓN EN EL OLIMPICO:</strong><br>Roma (6°, 61 pts) pelea puestos europeos contra una Fiorentina (16°, 37 pts) que necesita puntos. La disparidad genera fricción táctica y faltas en transiciones.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. VEREDICTO:</strong><br>78% de probabilidad. Con la Fiorentina como líder de amarillas en Italia y el contexto del partido, Over 3.5 tarjetas tiene un valor esperado positivo claro.</div>"
  },
  {
    liga: "🇪🇸 LaLiga",
    partido: "Sevilla vs Real Sociedad",
    fecha: "4 de mayo de 2026",
    pronostico: "Más de 4.5 Tarjetas",
    cuota: "1.65",
    prob: 72,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SEVILLA: 96 AMARILLAS EN 33 PARTIDOS:</strong><br>Promedio de 2.9 tarjetas/partido, muy por encima de la media de LaLiga (2.24). Lucien Agoume lidera con 11 amarillas y 49 faltas. La frustración del 18° puesto se traduce en agresividad.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. REAL SOCIEDAD TAMBIÉN CONTRIBUYE:</strong><br>71 amarillas en la temporada. Jon Aramburu acumula 9 amarillas y 62 faltas. La combinación proyecta una línea de 4.8 tarjetas para el partido.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. VEREDICTO:</strong><br>72% de probabilidad con cuota de 1.65. El mejor pick de tarjetas de la jornada. El Sevilla solo necesita aportar su promedio habitual para superar la línea.</div>"
  },
  {
    liga: "🇮🇪 Premier Division",
    partido: "Shamrock Rovers vs Drogheda",
    fecha: "4 de mayo de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.35",
    prob: 71,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DOMINIO HISTÓRICO EN H2H:</strong><br>Shamrock Rovers ha ganado 5 de los últimos 6 enfrentamientos directos contra Drogheda. Probabilidad de victoria: 71%. Promedia 1.43 goles a favor con solo 0.79 concedidos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DROGHEDA CONCEDE 1.54 GOLES/PARTIDO:</strong><br>8° en la tabla, el Drogheda tiene una de las peores defensas de la liga irlandesa. Frente al líder destacado, las probabilidades de mantener la portería a cero son mínimas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. VEREDICTO:</strong><br>71.25% de probabilidad. Pick de liga menor con valor sólido. El liderato del Shamrock respalda la consistencia del gol local.</div>"
  }
];"""

index_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\index.html"
with codecs.open(index_path, "r", "utf-8") as f:
    text = f.read()

pattern = r"const PICKS_DATA = \[.*?\];"
new_text = re.sub(pattern, picks_html, text, flags=re.DOTALL)

with codecs.open(index_path, "w", "utf-8") as f:
    f.write(new_text)

print("Picks updated for May 4, 2026 - 10 picks across 8 leagues")
