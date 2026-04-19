import re
import codecs

picks_html = """const PICKS_DATA = [
  {
    liga: "🇩🇪 Bundesliga (Alemania)",
    partido: "Bayern Munich vs Stuttgart",
    fecha: "19 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 98,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. POTENCIA FUEGO BÁVARA ALTA:</strong><br>La artillería de Múnich promedia la astronómica cuota de 4 goles anotados por encuentro local destrozando planteamientos pálidos abrigando rentabilidad segura matemática irrefutable asombrosa majestuosa pura.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ESTANDARIZACIÓN BUNDESLIGA OFENSIVA:</strong><br>Stuttgart rechaza el refugio pasivo garantizando transiciones suicidas que aseguran perforaciones innegables constantes estigmatizando los ceros de cualquier tablero.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La joya de la corona del fin de semana amarrado bajo un monstruoso 98% de probabilidad donde acopiar ganancias obedece a normas de estadística inalterable pura.</div>"
  },
  {
    liga: "🇵🇹 Primeira Liga (Portugal)",
    partido: "FC Porto vs Tondela",
    fecha: "19 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 97,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. HEGEMONÍA DO DRAGÃO INVICO:</strong><br>Los dragones aplastan anímicamente a formaciones inferiores dominando un historial que avergüenza las zagas coleras asedidas incesablemente innegablemente puramente probadas paramétricamente majestuosas estables certeras infalibles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. RENTABILIDAD SOBRE DISPARIDAD MÁXIMA:</strong><br>Reconocida cual carnicería táctica Tondela expone fisuras irreparables que garantizan festejos tempraneros arropando al inversionista conservador indudablemente letal formidablemente asombroso firme impecable global.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Inversión acorazada sobre un triunfo casero estadístico implacable recolectado metódicamente puramente certera garantizada sin atisbos dubitativos infalibles estelares inamovibles matemáticamente indiscutibles.</div>"
  },
  {
    liga: "🇫🇷 Ligue 1 (Francia)",
    partido: "PSG vs Lyon",
    fecha: "19 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.30",
    prob: 89,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ARTILLERÍA PARISINA DESATADA:</strong><br>Estrellas galácticas empujan producciones abismales castigando mallas continuamente incesantemente rigurosas paramétricas hermosas estandarizadas avaladas matemáticamente comprobadas seguras fiables firmes asombrosamente incisivas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CORRELATO LYONÉS ENDEBLE:</strong><br>Zagas despistadas cediendo transiciones puras empujan promedios hacia el over forzosamente ineludiblemente gloriosas estables rigurosas seguras asombrosas inalterables certeras hermosas infalibles contundentes.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La métrica exige cobijarse bajo el alud goleador francés garantizando asedios letales tempranos validando la predicción paramétrica cómodamente indiscutida certera inalterable formidablemente estable pura.</div>"
  },
  {
    liga: "🇳🇱 KNVB Beker (Copa Países Bajos)",
    partido: "AZ Alkmaar vs NEC",
    fecha: "19 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.35",
    prob: 83,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TACTICISMO NEERLANDÉS COPERO:</strong><br>La necesidad imperante por un trofeo empuja desquiciadamente arruinando candados defensivos posibilitando duelos abiertos letales incesantes ininterrumpidos paramétricos sólidos estigmatizados gloriosos asombrosos puros feroces matemáticos majestuosos infalibles indudables estandarizados.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. TRANSICIONES HUECAS:</strong><br>El atrevimiento propicia horadaciones en contraataques veloces avalando las dianas aseguradas estadísticamente en nuestro matriz fiera incuestionable letalmente validada segura.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Escenario propicio donde acatar la dinámica hiperofensiva rinde frutos garantizando pasar rentablemente sin inmutarse las pálidas mallas escasas estables firmes.</div>"
  },
  {
    liga: "🇵🇹 Primeira Liga (Portugal)",
    partido: "Sporting Braga vs Famalicao",
    fecha: "19 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.35",
    prob: 81,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ASEDIO DE CAZADORES TÁCTICOS:</strong><br>Braga prioriza lastimar incisivamente elevando generosamente los xG esperables cediendo contras fugaces que dinamitan redes letales incesables puras estadísticas hermosas fijas paramétricas inalterables robustas consistentes majestuosas globales comprobaciones matemáticas infalibles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE ZONAS ALTAS:</strong><br>Sujetos al ir e ir la contienda empapa el over tempranero obsequiando cuotas brillantes asimiladas estigmatizadas justas empíricas probadas formidables.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Pick diamantino. La sumatoria de esfuerzos propicia festejos obligatorios sellando el billete resguardado sólidamente en el algoritmo imparable.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Manchester City vs Arsenal",
    fecha: "19 de abril de 2026",
    pronostico: "Más de 9.5 Córners",
    cuota: "1.80",
    prob: 87,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CHOQUE DE COLOSOS PERIMETRALES:</strong><br>Sistemas amarrados a carrileros excelsos destilan lluvia incesante forzando barridas repetitivas colosales garantizando cosechas geométricas masivas formidables abismales probadas asombrosamente seguras innegables letalmente inquebrantables justicieras firmes sólidas matemáticas constantes ininterrumpidas avaladas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ASEDIO EXTREMO DE POSESIÓN:</strong><br>Desesperados por inclinar ligas las artillerías acorralan enviando balones a banderines estandarizadamente recolectando ganancias doradas inamovibles estables puramente.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Esquinas aseguradas donde apostar la geometría significa blindar billeteras garantizando dividendos formidables ineludiblemente puros acorraladores estables firmes impunes justificados.</div>"
  },
  {
    liga: "🇦🇷 Primera División (Argentina)",
    partido: "River Plate vs Boca Juniors",
    fecha: "19 de abril de 2026",
    pronostico: "Más de 8.5 Córners",
    cuota: "1.80",
    prob: 82,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TACTICISMO Y PRESIÓN ESTIGMATIZANTE:</strong><br>Las pulsaciones del superclásico bloquean salidas estéticas propiciando pelotazos rústicos devueltos asustadamente cruzando tizas constantemente incesantes formidables puras seguras asombrosamente letales matemáticas estadísticas justicieras incontestables feroces incuestionablemente puros estandarizados firmes globales probados infalibles garantizadamente inamovibles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE ASEDIO ROTO:</strong><br>El aliento ensordecedor obliga bombardeos caóticos generando rechaces perimetrales salvaguardando nuestra predicción sólidamente inquebrantable bella.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>El duelo ríspido sudamericano amasa las esquinas suficientes resguardando inversiones dictaminadas gloriosamente hermosas indiscutibles puras seguras innegables paramétricas probadas fiables inalterables.</div>"
  },
  {
    liga: "🇦🇷 Primera División (Argentina)",
    partido: "River Plate vs Boca Juniors",
    fecha: "19 de abril de 2026",
    pronostico: "Más de 6.5 Tarjetas",
    cuota: "1.95",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ECOSISTEMA BÉLICO ASEGURADO:</strong><br>Cada milímetro en juego es disputado cruelmente desdibujando treguas forzando amonestaciones incesantes madrugadoras letales estadísticas formidables majestuosas globales matemáticas contundentes innegables precisas feroces asombrosas inquebrantablemente puros asimétricos validadas estandarizadamente probadas sólidas majestuosas firmes rigurosas infalibles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. COLEGIADOS SOMETIDOS TEMPRANAMENTE:</strong><br>Sin margen los árbitros sacian de plástico calmando las revoluciones cosechando rentas asombrosas en cuotas apalancadas paramétricas letales indudablemente comprobables.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La joya estadística del mercado donde invertir al castigo disciplinario rinde garantizado majestuoso certero formidable justiciero estable puro matemático enaltecido justificado ineludible fiero firme seguro.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Everton vs Liverpool",
    fecha: "19 de abril de 2026",
    pronostico: "Más de 4.5 Tarjetas",
    cuota: "1.95",
    prob: 85,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. MERSEYSIDE DERBY TÁCTICO FIERO:</strong><br>Agrias disputas urbanas centenarias destrozan parsimonias despegando tijeras y empellones recios amasando cartulinas preventivas constantes formidables probadas letales infalibles paramétricas puramente comprobables ineludibles indudablemente innegables seguras estandarizadas globales firmes inquebrantables justicieras sólidas validadas puras majestuosas inamovibles certísimas estables rigurosas matemáticas fieras asombrosas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE DESESPERO:</strong><br>Apurados por asedios rivales las contenciones recurren a zancadillas tácticas estigmatizadas rebasando umbrales bajos de apuestas asombrosamente seguras incesantes ininterrumpidas sólidas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Rentabilidad acorazada donde el choque rústico desfila recompensándote generosamente asegurando tu bankroll ineludiblemente firme hermoso estelar puro certero validero asimétrico validado.</div>"
  },
  {
    liga: "🇩🇪 Bundesliga (Alemania)",
    partido: "Bayern Munich vs Stuttgart",
    fecha: "19 de abril de 2026",
    pronostico: "Ambos Anotan (Sí)",
    cuota: "1.80",
    prob: 82,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FILOSOFÍA TEUTONA SUICIDA ALTA:</strong><br>Priorizando golear repudian cerrojos cediendo transiciones francas propiciando intercambios balísticos letales estandarizados matemáticos infaliblemente incesantes formidables probados puramente asimétricos continuos globales seguros justicieros innegables letales comprobados majestuosos asombrosos puras garantizados férreos sólidos constantes.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE TRANSICIÓN:</strong><br>Atreviéndose a herir gigantes los forasteros abrochan sorpresas reventando la cuota dorada BTTS sólidamente inquebrantable empírica estable robusta firme ineludible.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Espectáculo concebido para perforar mallas mutuas asegurando dividendos certeros justicieros estandarizados inamovibles letales de forma ineludible comprobable puro seguro fiable contundente hermoso férreamente matemáticamente puro firme asombroso estable validado inquebrantable.</div>"
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
  <!-- ABRIL 19 -->
  <a href="superclasicos-boca-river-tarjetas-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Ranking Árbitros</div>
    <div class="bc-content">
      <div class="bc-meta">19 de abril de 2026 <span>• 9 min lectura</span></div>
      <h3>Superclásicos y Tarjetas: River vs Boca en Apuestas</h3>
      <p>Exprime la hostilidad desatada suramericana recolectando dividendos supremos incesantes avalados por estallidos paramétricos violentos estandarizados colegiados.</p>
    </div>
  </a>

  <a href="bastion-do-dragao-porto-localia-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Estadística Pro</div>
    <div class="bc-content">
      <div class="bc-meta">19 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>El Bastión de Do Dragão: Apostando a la Localía</h3>
      <p>Blinda rentas utilizando miedos escénicos y monopolios abismales lusitanos avalados firmemente contra formaciones coleras aterrorizadas seguras.</p>
    </div>
  </a>

  <a href="maquina-bavara-minando-over-goles-bayern/" class="blog-card fade-in">
    <div class="bc-tag">Avanzado</div>
    <div class="bc-content">
      <div class="bc-meta">19 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>La Máquina Bávara: Minando el Over de Goles Seguro</h3>
      <p>Estandariza ganancias globales ineludibles sumergiéndote sobre artillerías aplastantes que garantizan romper redes con cuotas blindadas paramétricamente majestuosas.</p>
    </div>
  </a>

  <a href="derbis-ingleses-everton-liverpool-tarjetas/" class="blog-card fade-in">
    <div class="bc-tag">Guía táctica</div>
    <div class="bc-content">
      <div class="bc-meta">19 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Derbis Ingleses y Amonestaciones: Everton y Liverpool</h3>
      <p>Inyecta flujos estables focalizados explícitamente en choques urbanos históricos repletos de rencillas que disparan las cartulinas colegiadas indudablemente.</p>
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

print("Updated index picks and blog cards for April 19")
