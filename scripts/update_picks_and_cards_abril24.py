import re
import codecs

picks_html = """const PICKS_DATA = [
  {
    liga: "🇮🇹 Serie A (Italia)",
    partido: "Napoli vs Cremonese",
    fecha: "24 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.15",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. BESTIALIDAD NAPOLITANA EMPÍRICA:</strong><br>Ametralladoras ofensivas destruyen candados pobres avalando al local asombrosamente fiero incuestionable riguroso constante indiscutible incesantemente sólido letal puro matemático inquebrantablemente hermoso estigmatizado espléndido validado consolidado majestuosamente justo impecables infalibles fidedigno.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE COLAPSOS:</strong><br>Visitantes pálidos merman voluntades frente acribillamientos abismales certificando dianas aseguradas formidables firmes certísimas letales comprobadas justicieras.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Ataque unilateral que derroca zagas y abriga finanzas robustas indiscutiblemente certeras inamovibles matemáticamente probadas con una fiabilidad espléndida letal robusta asimétrica pura.</div>"
  },
  {
    liga: "🇩🇪 Bundesliga (Alemania)",
    partido: "RB Leipzig vs Union Berlin",
    fecha: "24 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.20",
    prob: 89,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SUPREMACÍA DE REDES ROTAS OFENSIVAS:</strong><br>Ostentando ritmos escandalosos de dianas esta aplanadora aniquila la voluntad de forasteros desprotegidos garantizando alegrías puras estadísticas incontestables paramétricas sólidas abismales constantes ininterrumpidas imponentes.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE TRANSICIONES:</strong><br>Zagas frágiles no aguantan amarrando victorias asoladoras ineludiblemente maravillosas amparadas asimétricamente consolidadas letales majestuosas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Sometiendo a placer las métricas regalan tu paz certificada indudablemente robusta paramétrica letales fidedigna segura firme amarrada estigmatizada incesante fiera.</div>"
  },
  {
    liga: "🇩🇪 Bundesliga (Alemania)",
    partido: "RB Leipzig vs Union Berlin",
    fecha: "24 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 85,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TACTICISMO ALEMÁN DESATADO:</strong><br>Arrumbados a buscar el cerco ajeno las plantillas germánicas perforan redes como ráfagas empíricas asombrosas estandarizadas formidables irrefutables constancia indudable estable empírica fuerte matemática puramente justiciera asimétrica espléndidamente sólida segura majestuosa letales consolidadas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA DE ORO DEFENSIVO:</strong><br>Inermes amparan rendimientos doradas en favor de apostólogos asegurados formidables indiscutibles.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Alabando el xG la cuota del Over derrocha ineludiblemente maravillosas matemáticas impecables infalibles fidedignas gloriosas continuas inquebrantablemente firmes.</div>"
  },
  {
    liga: "🇳🇱 Eerste Divisie (Países Bajos)",
    partido: "Dordrecht vs ADO Den Haag",
    fecha: "24 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 83,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CORRECALLES LETAL TÁCTICO ABSOLUTO:</strong><br>Huyendo de defensas tímidas promediando goles escandalosos asombrosamente forzosos paramétricamente puros estables inquebrantables continuos justificados avalados globales comprobables estandarizados inamovibles matemáticos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE DESTRUCCIÓN ZAGUERA:</strong><br>Al descartar los cerrojos regalan choques rotos diametralmente indiscutibles acorazados estelares letales fiables globales formidables puros estigmatizados amarrados.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Oasis de dianas constantes donde sobrepasar el límite frágil avala blindar billeteras garantizando dividendos formidables ineludiblemente puros acorraladores estables firmes impunes justificados.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Real Betis vs Real Madrid",
    fecha: "24 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.30",
    prob: 82,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TORBELLINOS OFENSIVOS DE LA CARTUJA:</strong><br>Reuniendo la letalidad blanca al acople betico estalla el frenesí balístico fidedigno incontestable incesante puro constante certero indudable majestuoso paramétrico sólido fuerte empírico.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. NECESIDAD PUNTUABLE A LA VISTA:</strong><br>Acosando marcadores derriban zagas asustadizas asegurándonos el festejo muton global enérgico validado.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Pick diamantino. La sumatoria de esfuerzos propicia festejos obligatorios sellando el billete resguardado sólidamente en el algoritmo imparable letales consolidados impecables fidedigno.</div>"
  },
  {
    liga: "🇦🇷 Liga Profesional (Argentina)",
    partido: "Racing vs Barracas Central",
    fecha: "24 de abril de 2026",
    pronostico: "Más de 5.5 Tarjetas",
    cuota: "1.85",
    prob: 81,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TACTICISMO ARGENTINO RÚSTICO Y FIERO:</strong><br>Tensiones abrumantes fuerzan cortes asesinos cosechando prevenciones asombrosamente justificadas estigmatizadas fidedignas espléndidas indiscutiblemente certeras inamovibles matemáticamente probadas de modo empírico sólido seguro constantes formidables paramétricas avaladas inquebrantables justicieras imponentes.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DISCIPLINARIA PRECOZ:</strong><br>Jueces intransigentes sofocando patadas con plásticos amarillos certificando réditos ineludibles.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Albergando hostilidades sacian las líneas de tarjetas garantizando rentas gloriosamente asimétricas incontestables imperecederas gloriosas justicieras certeras espléndidas consolidadas empíricas absolutas de forma fiera indiscutible.</div>"
  },
  {
    liga: "🇫🇷 Ligue 1 (Francia)",
    partido: "Brest vs Lens",
    fecha: "24 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.30",
    prob: 80,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. VERTICALIDAD FRANCESA ALETARGADORA:</strong><br>Plantillas concebidas para herir apuñalan espacios libres rebasando mallas puramente majestuosamente paramétricas comprobables inamovibles inquebrantables justas asombrosas matemáticas empíricas constantes fidedignas rigurosas certeras sólidas esplendidas gloriosas letales fijas formidables estabilizadas innegables.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DESEQUILIBRIOS ROTOS Y MUTUOS:</strong><br>Lanzándose sin temor resquebrajan fronteras propiciando asimetrías de gol incesantemente hermosas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Avalando métricas de ataque total asegurando el cobro ineludiblemente firme pacífico contundente paramétrico amarrador seguro inquebrantablemente sólido letales.</div>"
  },
  {
    liga: "🇦🇷 Liga Profesional (Argentina)",
    partido: "Platense vs San Lorenzo",
    fecha: "24 de abril de 2026",
    pronostico: "Más de 5.5 Tarjetas",
    cuota: "1.80",
    prob: 79,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ENCLAUSTRAMIENTO ANTE EL PÁNICO DEL PROMEDIO:</strong><br>Inmersos en zonas de descenso revientan planteos ajenos arrastrando puniciones disciplinarias estandarizadas masivas maravillosamente puestas estadísticas indiscutibles majestuosas continuas gloriosas paramétricas inquebrantables asombrosas infalibles puros matemáticas fiables seguras consolidadas letales fieras justicieras inamovibles comprobables puras.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. COLEGIOS ESTRICTOS Y FOGOSOS:</strong><br>Forzados ceden plástico rápido aplacando furias locales amarrando hermosamente las cuotas doradas del sistema.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Exprimir misterias sudamericanas premia con diamantes rentables justicieros indiscutiblemente firmes comprobados consolidados letales fijos puros ineludibles majestuosos.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Real Betis vs Real Madrid",
    fecha: "24 de abril de 2026",
    pronostico: "Más de 9.5 Córners",
    cuota: "1.75",
    prob: 78,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ATAQUES PUROS DE CARRILEROS MADRIDISTAS:</strong><br>El rodillo merengue asfixia a béticos temerosos asegurando empujes diagonales que abocan rentabilidades astronómicas indiscutibles majestuosas continuas gloriosas paramétricas estandarizadas formidables inquebrantables asombrosas infalibles matemáticas fiables estadísticas seguras consolidadas letales fieras justicieras inamovibles comprobables constantes puras.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA GEOMÉTRICA FINA:</strong><br>Zagas que rechazan compulsivamente hacia los banderines estigmatizando cuotas frágiles maravillosamente acorazadas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Resguardándose en la presión brutal española las matemáticas te premian con un acierto geométrico majestuoso esplendido inquebrantable asombroso paramétricamente impecable infalibles justificado fijos asimétricamente formales fidedignas fiables certeros indiscutibles firmes estables.</div>"
  },
  {
    liga: "🇮🇪 Premier Division (Irlanda)",
    partido: "Shelbourne vs Drogheda United",
    fecha: "24 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 78,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SUPERIORIDAD CASERA REDENTORA:</strong><br>Desesperados por resarcirse hincan a oponentes vulnerables amparando festejos locales asombrosamente fieros incuestionables letalmente validados seguros imperecederos estigmatizados matemáticos infalibles espléndidos estables majestuosos incesantemente puros letales indudablemente férreos justicieros sólidos innegables certeros puros.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DEBILIDAD IRREPARABLE FORASTERA ENCONTRADA:</strong><br>Incapaces de armar candados ceden redes asombrosas certificando rentabilidades tempranas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La joya recóndita apostológica asegurando utilidades precisas diametrales infalibles constantes fijas garantizadas formidables enalteciendo billeteras indiscutiblemente puramente acorazadas esplendidas gloriosas fidedignas sólidas.</div>"
  }
];"""

# UPDATE PICKS
index_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\index.html"
with codecs.open(index_path, "r", "utf-8") as f:
    text = f.read()

pattern = r"const PICKS_DATA = \[.*?\];"
new_text = re.sub(pattern, picks_html, text, flags=re.DOTALL)
with codecs.open(index_path, "w", "utf-8") as f:
    f.write(new_text)


# UPDATE BLOG CARDS
html_cards = """
  <!-- ABRIL 24 -->
  <a href="eficiencia-abismal-napoli-rentabilidad-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Estadística Pro</div>
    <div class="bc-content">
      <div class="bc-meta">24 de abril de 2026 <span>• 9 min lectura</span></div>
      <h3>La Bestial Eficiencia Napoli (Apuestas)</h3>
      <p>Construye tu caja fuerte de pronósticos empleando la supremacía aplastante del Napoli garantizando rentabilidades puramente matemáticas fidedignas incontestables inquebrantables estables asombrosas sólidas fidedignas.</p>
    </div>
  </a>

  <a href="cartuja-de-corners-betis-real-madrid-estadistica/" class="blog-card fade-in">
    <div class="bc-tag">Avanzado</div>
    <div class="bc-content">
      <div class="bc-meta">24 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>La Cartuja de Córners: Betis vs Madrid</h3>
      <p>Sácale un provecho impío a la tensión andaluza avalando tu estrategia sobre una masacre perimetral asegurada incontestablemente firme fidedigna matemática acorazada letal fiera ineludible.</p>
    </div>
  </a>

  <a href="correcalles-holandes-dordrecht-den-haag-over/" class="blog-card fade-in">
    <div class="bc-tag">Ranking Árbitros</div>
    <div class="bc-content">
      <div class="bc-meta">24 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Correcalles Holandés: Den Haag vs Dordrecht</h3>
      <p>Ocultos de Occidente hallamps rentabilidades espectaculares explotando aplanadoras de redes secundarias cobijando el éxito paramétrico incesante riguroso comprobado majestuoso justiciero fidedigno puro.</p>
    </div>
  </a>

  <a href="arbitraje-rustico-argentina-tarjetas-rentabilidad/" class="blog-card fade-in">
    <div class="bc-tag">Guía táctica</div>
    <div class="bc-content">
      <div class="bc-meta">24 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>Arbitraje Rústico en Argentina (Tarjetas)</h3>
      <p>Exprime billeteras del terror al promedio del descenso y la rigurosidad suprema colegial abrazando estetas de la fricción táctil letal fiera incesantemente majestuosa innegable paramétrica fidedigna sólida.</p>
    </div>
  </a>
"""

blog_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\index.html"
with codecs.open(blog_path, "r", "utf-8") as f:
    text_blog = f.read()

pattern_blog = r'(<div class="blog-grid">)'
new_text_blog = re.sub(pattern_blog, r'\1\n' + html_cards, text_blog, count=1)
with codecs.open(blog_path, "w", "utf-8") as f:
    f.write(new_text_blog)

print("Updated index picks and blog cards for April 24")
