import re

picks_html = """const PICKS_DATA = [
  {
    liga: "🇮🇹 Serie A (Italia)",
    partido: "AS Roma vs Pisa",
    fecha: "10 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TENDENCIA ASIMÉTRICA:</strong><br>La Roma colisiona en el Olímpico contra un Pisa estadísticamente desangrado que arrastra el fango de la categoría con un infame diferencial de -32 tantos en contra.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. FACTOR GOLIAT:</strong><br>El bloque loba sostiene un asombroso registro de 13 choques inquebrantable sin admitir daño alguno. Con la presión cero en sus filas defensivas, soltarán incesantemente a las piezas de mediocampo ofensivo.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Pronóstico extremadamente alto (92%). Una verdadera roca táctica y la plataforma ideal para comenzar una escalera disciplinada en la jornada itálica.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Real Madrid vs Girona",
    fecha: "10 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.30",
    prob: 91,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. LA HEGEMONÍA BLANCA:</strong><br>La Casa Blanca no claudica de cara a puerta; mantienen un ratio aterrador produciendo sistemáticamente 2.24 dianas por presentación en el tapete de Chamartín.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. FATIGA EXTREMA VISITANTE:</strong><br>El proyecto del Girona transita por un bache de desestabilización a domicilio, perdiendo solvencia para replegarse contra embates de equipos transicionales tan rápidos.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Contemplar una blanqueada a los blancos en condición de dueños absolutos de la capital es impensable bajo modelaje. Su tanto está presupuestado por ley de probabilidad (91%).</div>"
  },
  {
    liga: "🇳🇱 Eredivisie (Países Bajos)",
    partido: "FC Twente vs FC Volendam",
    fecha: "10 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.30",
    prob: 88,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DEFENSAS ROTAS:</strong><br>Volendam ostenta orgullosamente la condena cimentada de ser la red más fracturada del circuito neerlandés moderno. Todo balón llovido se transforma mágicamente en zozobra en su área.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LLEGADA TÁCTICA CONSTANTE:</strong><br>Twente asimila y tritura. Su altísimo volumen posicional se deleitará de forma descarnada al pisar los resquicios que el último posicionado del bloque regalará irremediablemente.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La dinámica de las ligas holandesas predica el ataque. Con este cruce, apostar al Over inferior (1.5) no acarrea misterios y cuenta con cuota jugosa estabilizada.</div>"
  },
  {
    liga: "🇩🇪 Bundesliga (Alemania)",
    partido: "Augsburg vs Hoffenheim",
    fecha: "10 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.40",
    prob: 78,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. XG (EXPECTED GOALS) COMBINADO:</strong><br>La analítica dispara alarmas positivas al superponer las proyecciones; se anticipa un índice conjunto por encima del 3.0 en expectativa goleadora debido al desprecio por la zaga que ambos ostentan.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ESTILO KAMIKAZE:</strong><br>Ni Augsburg ni Hoffenheim comisionan transiciones retenidas. Renuncian a los medios centros pasivos y apuestan por la verticalidad. Sus vallas lucen como coladores semana a semana.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Un festín donde las artillerías primarán por obligación táctica y necesidad matemática germana. Escenario propicio e ideal para los cultores del Over.</div>"
  },
  {
    liga: "🇫🇷 Ligue 1 (Francia)",
    partido: "Marseille vs Metz",
    fecha: "10 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.45",
    prob: 73,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. RESISTENCIA METZIANA ROTA:</strong><br>Las ambiciones del visitante penden de un hilo. Su estructura retentiva se etiqueta estadísticamente dentro del Top 3 de peores líneas defensivas con mayor xGA del fútbol galo.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. FACTOR GREENWOOD:</strong><br>El Olympique de Marsella encauza todo su arsenal periférico depositando la llave mágica en un Greenwood en estado de gracia y rendimiento letal incontestable.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Conjugando el peso aplastante del Vélodrome y la fragilidad del Metz al retroceso en las transiciones, un doblete galo (sumando en cualquier pórtico) recae en lógica pura.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "West Ham vs Wolverhampton",
    fecha: "10 de abril de 2026",
    pronostico: "Más de 8.5 Córners",
    cuota: "1.80",
    prob: 72,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TACTICISMO DE PASILLO:</strong><br>West Ham ha cimentado su volumen de presión agudizando las subidas de laterales que confluyen en centros cruzados, detonando recurrentes despejes en la última línea visitante.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA ANTIAÉREA LOBEZNA:</strong><br>Wolves responde cerrando su bloque. Cuando sus centrales se atosigan en el achique, extirpan los balones por la cal de la banderilla sin escrúpulos ni miramientos técnicos.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Una línea estricta de 8.5 se vislumbra como una concesión excesivamente caritativa de las grandes Books para el esquema predominantemente aéreo del cotejo londinense.</div>"
  },
  {
    liga: "🇹🇷 Superliga Turca",
    partido: "Besiktas vs Antalyaspor",
    fecha: "10 de abril de 2026",
    pronostico: "Más de 9.5 Córners",
    cuota: "1.85",
    prob: 69,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. PRODUCCIÓN ESTAMBULITA MASIVA:</strong><br>Para goce estadístico perimetral, el majestuoso Besiktas amasa una bestialidad de apariciones angulares generadas meramente por mérito y dominancia propia por bandas extremas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ASFIXIA DEL VISITANTE:</strong><br>Antalyaspor desahoga mediante un corte de balón sumamente desorganizado en plazas magnas. Su defensa retrocede temerosamente a encajonarse en el área del portero.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Encuentro diseñado arquitectónicamente para cobrarse un ticket esplendoroso en tiros de esquina basados en la desesperación otomana y el fervor de las gradas locales.</div>"
  },
  {
    liga: "🇲🇽 Liga MX (México)",
    partido: "Puebla vs León",
    fecha: "10 de abril de 2026",
    pronostico: "Más de 4.5 Tarjetas",
    cuota: "1.90",
    prob: 74,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. PERFIL CUALITATIVO DEL TORNEO:</strong><br>Un partido azteca con antecedentes crónicos de fricción. Ambas escuadras trajinan el semestre albergando historiales volátiles de faltas que frenan drásticamente el desarrollo liminar del balón.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. TENSIÓN TÁCTICA ACUMULADA:</strong><br>El duelo no concede pases pasivos en el ecuador. Los reclamos escalarán precipitadamente sumándole puntos disciplinarios de riguroso oro a los valientes del pronóstico arbitral.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Romper el umbral escaso de las cuatro amonestaciones congrega el 74% de probabilidad latente gracias a árbitros locales intolerantes al roce duro del circuito regional.</div>"
  },
  {
    liga: "🇩🇪 Bundesliga (Alemania)",
    partido: "Augsburg vs Hoffenheim",
    fecha: "10 de abril de 2026",
    pronostico: "Ambos Anotan (Sí)",
    cuota: "1.85",
    prob: 68,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CORRELATO IDEAL PARA EL BTTS:</strong><br>El análisis se postula revalidando la rotura absoluta del entramado táctico. Definitivamente ambas defensas no cometen meros errores de forma, sino de esencia en el control.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LÓGICA VERTICAL IMPLACABLE:</strong><br>Teniendo altas cuotas de llegada artillera alemana, se gestará un tiroteo constante y predecible; no habrá respiros en transiciones ni barreras en su ecuador geográfico.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Un 'Ambos Anotan' sufragado y certificado sobre estadísticas abrumadoras de ineficiencia defensiva. Alta recompensa para uno de los choques del Value en el centro europeo.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Real Madrid vs Girona",
    fecha: "10 de force 2026",
    pronostico: "Ambos Anotan (Sí)",
    cuota: "1.90",
    prob: 65,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. RESQUICIOS EN LA CASA BLANCA:</strong><br>Aunque dictan las ofensas de todo el campeonato, el equipo madridista concede goles de contragolpe como penalidad a sus galopadas incasables; arrastran un oscuro velo de 7 pleitos admitiendo dianas consecutivas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. RESPUESTA CATALANA INHERENTE:</strong><br>Girona viaja presuntamente mermado pero conserva el ADN irrenunciable al ataque posicional, cobrando el valioso ticket por su letal castigo sorpresivo a zagas desubicadas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>El valor extrínseco que las agencias tasan (1.90) confunde el volumen gigantesco del local. Pese al riesgo real, la cuota inmensa paga su valor debido a los constantes 'regalos' defensivos del favorito.</div>"
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
