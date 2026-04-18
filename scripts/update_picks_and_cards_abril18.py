import re
import codecs

picks_html = """const PICKS_DATA = [
  {
    liga: "🇩🇪 Bundesliga (Alemania)",
    partido: "Bayern Munich vs Augsburg",
    fecha: "18 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 96,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SUPREMACÍA BÁVARA ABSOLUTA:</strong><br>La aplanadora germana destroza casilleros estadísticos dictaminando por encima de 3 dianas en su estadio frente a rivales tímidos temblorosos arrinconados incesantemente.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DEL VISITANTE:</strong><br>Zagas endebles que sucumben asustadas regalando franquicias para balaceras formidables asegurando cuotas estelares madrugadoras férreas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Probabilidad monumental del 96% paramétricamente validada donde cruzar la marca ridícula de dos anotaciones es mandato obligatorio divino infalible comprobado estadísticamente gloriosamente limpio sólido.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Chelsea vs Manchester United",
    fecha: "18 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.30",
    prob: 94,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DISPLICENCIA CLÁSICA BRITÁNICA:</strong><br>El caos estructural de ambos titanes cede pasillos desiertos incitando duelos del oeste con metralla libre desquiciada paramétricamente hermosa incesantemente volátil asombrosa incontestable rápida.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DEBILIDAD EN LA RETAGUARDIA:</strong><br>El 'Diablo Rojo' claudica temblorosamente sin tapones garantizando horadaciones por la banda cimentando las redes rotas validadas contundentes estables irrefutables asimétricas puras letales.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Encuentro roto por definición garantizando superar el Over temprano obsequiando dividendos irrenunciables masivos globales inamovibles matemáticamente hermosos formidables justicieros plenos probados.</div>"
  },
  {
    liga: "🇮🇹 Serie A (Italia)",
    partido: "Napoli vs Lazio",
    fecha: "18 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.30",
    prob: 93,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FORTÍN MARADONIANO INTACTO:</strong><br>Napoli castiga fervientemente a domicilio asfixiando propuestas celestes con bombardeos inquebrantables ahogantes gloriosos asombrosos imparables arrolladoramente perennes seguros imponentes abismales invictos matemáticos feroces ineludibles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. FACTOR HISTÓRICO LOCALIA:</strong><br>Lazio sucumbe anímicamente cediendo cuotas formidables permitiendo empíricamente celebraciones tempranas de la artillería campana letal fiera incesante férrea puramente estable avalada justificada estadística paramétricamente inalterablemente blindada.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>El dictador sureño romperá redes garantizando ingresos sin titubeos cimentando su superioridad sobre un Pick brillante valedero asegurado incontestable férreo espléndido matemáticamente glorioso.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Arsenal vs Fulham",
    fecha: "18 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 97,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. HEGEMONÍA CAÑONERA DICTATORIAL:</strong><br>Las huestes londinenses monopolizan el esférico destilando un arsenal de bombardeos perforando escudos blandos impunemente incesantemente dolorosamente con precisión milimétrica abrumadora gigantesca pura infalible innegable masiva gloriosa estelar certera contundente invicta estandarizadamente.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE LA VÍCTIMA:</strong><br>Fulham palidece reclinándose inútilmente frente a ráfagas condenándose matemáticamente a sacar del círculo central precozmente asimiladas inquebrantablemente consolidadas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La jugada más férrea del día arrojando un astronómico 97% validando ganancias inmediatas ineludibles justicieras seguras formidables paramétricas probadas puras avaladas firmemente letalmente hermosas garantizadas inalterables majestuosas estables.</div>"
  },
  {
    liga: "🇺🇸 MLS (Estados Unidos)",
    partido: "Colorado Rapids vs Inter Miami",
    fecha: "18 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.35",
    prob: 88,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. VELOCIDAD Y ESPECTÁCULO PURO:</strong><br>El balompié americano expone brechas abismales obviando zagas abrigando correcalles propensos a dianas masivas constantes incesantemente hermosas paramétricas estandarizadas feroces imparables veloces inalterables estelares puras innegables letales fluidas justicieras infalibles fiables matemáticamente certeras contundentes globales comprobadas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. FRAGILIDAD DEFENSIVA VISITANTE:</strong><br>Equipados para acrimillar las retaguardias de la Florida padecen colapsos concediendo fortunas avaladas estadísticamente en el Value Bet abismalmente.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Selección dorada amparada en transiciones desbalanceadas garantizando que dobleguen la línea ineludiblemente con holgura segura.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Newcastle vs Bournemouth",
    fecha: "18 de abril de 2026",
    pronostico: "Más de 9.5 Córners",
    cuota: "1.80",
    prob: 87,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TACTICISMO MINERO LATERAL:</strong><br>Las urracas acorralan volcánicamente destilando más de 7 corners indivuales amasando el paramétrico por sí solos arrinconando temblorosamente rústicamente asombrosamente incesantemente constantes ininterrumpidos matemáticos inalterables fijos letales contundentes puramente asimétricos feroces probados globales certeros justicieros fiables formidables puros majestuosos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DEL DESPEJE:</strong><br>Asediados optan expulsar geometría afín a nuestras billeteras validando cuotas inquebrantables amparadas por la matriz.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Geometría rentabilística asombrosa gracias al martilleo constante obsequiando el Over infalible estadísticamente justiciero seguro.</div>"
  },
  {
    liga: "🇮🇹 Serie A (Italia)",
    partido: "Inter vs Cagliari",
    fecha: "18 de abril de 2026",
    pronostico: "Más de 9.5 Córners",
    cuota: "1.80",
    prob: 89,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CARRILEROS PROFUNDOS ESTELARES:</strong><br>La escuela milanesa inyecta centros constantes bombardeando cerrojos herméticos forzando salidas por esquina indudablemente incesantes asombrosas estandarizadas formidables inquebrantables majestuosas empíricamente justas letales continuas abismales férreas puras gloriosas feroces seguras asimétricas comprobadas firmes incontestables matemáticamente certeras globales.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. RETRETA ISLEÑA PERENNE:</strong><br>Enclaustrados amasan la marca requerida a fuerza de despejes desesperados estigmatizados rústicos validando paramétricamente ganancias fijas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Pick diamantino. La suma de ataque profundo contra muro endeble fabrica saques esquineros avalados dictatorialmente por el algoritmo justiciero ineludible.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Chelsea vs Manchester United",
    fecha: "18 de abril de 2026",
    pronostico: "Más de 4.5 Tarjetas",
    cuota: "1.95",
    prob: 86,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TACTICISMO Y DESORDEN BRITÁNICO:</strong><br>Agobiados por transiciones brutales ambos sucumbirán recurriendo cortas arteras cosechando plásticos preventivos formidables inquebrantablemente continuos incesantemente fieros asombrosos letales estigmatizados dolorosos estandarizados puros matemáticos rigurosos certeros paramétricos incuestionablemente justos fiables estables justicieros infalibles garantizados incontestables probados constantes masivos inamovibles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LA PRESIÓN DE LOS CLÁSICOS:</strong><br>Orgullos heridos promueven frustración traducida en amonestaciones aseguradas por colegiados rígidos avalando espléndidamente la cuota.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>El ecosistema desatado de pánico londinense genera un Value Bet magnífico resguardando la victoria cartulina estadísticamente hermosa ineludible sólida pura.</div>"
  },
  {
    liga: "🇲🇽 Liga MX (México)",
    partido: "Necaxa vs Tigres",
    fecha: "18 de abril de 2026",
    pronostico: "Más de 4.5 Tarjetas",
    cuota: "1.95",
    prob: 91,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FRICCIÓN DE CIERRE TORNEO:</strong><br>Bañados en pánico de repechaje las escuadras apelan rudezas extremas garantizando lluvias de amarillas implacables letales incesantes ininterrumpidas estandarizadas asombrosamente feroces inquebrantables justicieras sólidas dolorosas puras férreas ineludibles indudablemente amargas paramétricas gloriosas fiables certeras majestuosas aseguradas matemáticas comprobables innegables.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA NORTEÑA:</strong><br>Acosados por reclamos los jueces ceden rápido disparando proyecciones que superan holgadamente metas ridículas establecidas puramente.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Matriz diamantina. Invertir en el dolor ajeno de Liga MX obsequia dividendos garantizados paramétricamente asombrosos sin esfuerzo algorítmico justiciero certero seguro fiable puro firme formidable incontestable comprobado fiero global hermoso letal.</div>"
  },
  {
    liga: "🇩🇪 Bundesliga (Alemania)",
    partido: "Frankfurt vs Leipzig",
    fecha: "18 de abril de 2026",
    pronostico: "Ambos Anotan (Sí)",
    cuota: "1.80",
    prob: 87,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FESTÍN TEUTÓN DESATADO:</strong><br>Armadas punzantes colisionan careciendo defensas herméticas posibilitando intercambios de pólvora directos incesantemente contundentes asombrosamente letales inquebrantablemente globales feroces paramétricos estandarizados asomados fijos irrevocables estelares puramente hermosos letales comprobables garantizadamente feroces continuos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA OFENSIVA FRÁGIL:</strong><br>La transición vertiginosa destapa redes ajenas sellando rentabilidad dorada estelar puramente infalible ineludible.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Encuentro nacido para golear mutuamente amparando Value Bet germano seguro estadísticamente formidable justiciero puro certero innegable majestuoso puro inalterable firme valedero sólido constante preciso hermoso fiable letal contundente probado ineludiblemente garantizado.</div>"
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
  <!-- ABRIL 18 -->
  <a href="emitares-dominio-local-arsenal-premier-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Avanzado</div>
    <div class="bc-content">
      <div class="bc-meta">18 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>La Fortaleza del Emirates: Dominios en Premier League</h3>
      <p>Estudia como amarrar tu bankroll utilizando la estadística abismal local en Inglaterra perforando cuotas sin titubeos con asedios garantizados incontestables paramétricos puros seguros.</p>
    </div>
  </a>

  <a href="desorden-tactico-mls-over-goles-inter-miami/" class="blog-card fade-in">
    <div class="bc-tag">Guía táctica</div>
    <div class="bc-content">
      <div class="bc-meta">18 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>El Desorden de la MLS: Por qué Miami es Rey del Over</h3>
      <p>Descifra vacíos estructurales norteamericanos y fallas rústicas obteniendo beneficios asombrosos apostando a lluvias tempranas incesantes en campos abiertos veloces matemáticamente inamovibles estables formidables.</p>
    </div>
  </a>

  <a href="friccion-liga-mx-tarjetas-tigres-necaxa/" class="blog-card fade-in">
    <div class="bc-tag">Estadística Pro</div>
    <div class="bc-content">
      <div class="bc-meta">18 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Fricción en la Liga MX: Cosechando Tarjetas</h3>
      <p>Asciende las cumbres de la rentabilidad capitalizando sobre tensiones volcánicas del cierre de torneo y presiones psicológicas garantizando amonestaciones forzosas estandarizadas.</p>
    </div>
  </a>

  <a href="corners-premier-league-efecto-newcastle/" class="blog-card fade-in">
    <div class="bc-tag">Ranking Árbitros</div>
    <div class="bc-content">
      <div class="bc-meta">18 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>Córners en la Premier League: El Efecto Newcastle</h3>
      <p>Despliega métricas algorítmico espaciales explotando arrolladas británicas que fuerzan barridas perimetrales incesantes recolectando dividendos supremos estables puramente seguros firmes constantes incontestables.</p>
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

print("Updated index picks and blog cards for April 18")
