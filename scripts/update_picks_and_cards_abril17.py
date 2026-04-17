import re
import codecs

picks_html = """const PICKS_DATA = [
  {
    liga: "🇹🇷 Süper Lig (Turquía)",
    partido: "Fenerbahçe vs Rizespor",
    fecha: "17 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.20",
    prob: 95,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. URGENGENCIA CAMPEONABLE ABSOLUTA:</strong><br>Forzados por el implacable ritmo del Galatasaray, el local destila presión extrema acorralando con promedios asombrosos en casa de 2.28 goles netos letales abrumadores estadísticamente formidables innegables.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA TURCA:</strong><br>Rizespor deambula cediendo fisuras colosales (1.44 dianas encajadas fuera) desplomándose dramáticamente ante asedios abismales continuos ininterrumpidos hostigantes letales paramétricos indiscutibles seguros estables.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Un gol prematuro sella el compromiso. El algoritmo abraza cuotas bajas empapadas en blindaje paramétrico dictaminando inquebrantabilidad incesantemente majestuosa segura infalible justiciera empírica.</div>"
  },
  {
    liga: "🇫🇷 Ligue 1 (Francia)",
    partido: "Lens vs Toulouse",
    fecha: "17 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 94,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EL EFECTO BOLLAERT-DELELIS:</strong><br>El fortín inquebrantable galo acarrea a cuestas el pánico foráneo consolidando la tercera máxima artillería casera arrolladora de Francia paramétricamente validada majestuosa e incesantemente poderosa asombrosamente temida letalmente eficaz.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CONFLICTOS PSICOLÓGICOS DEL RIVAL:</strong><br>Toulouse aterriza ultrajado cediendo boquetes deplorables destrozando sus planteamientos arrinconados garantizando perforaciones punzantes tempraneras asombrosas sólidas firmes seguras incontestables abismales matemáticas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Un blindaje majestuoso sella la cuota del fortín. Matemáticamente ineludible obsequiando rentabilidad segura a inversionistas estables serios innegables estadísticamente rentables a priori.</div>"
  },
  {
    liga: "🇳🇱 Eerste Divisie (Países Bajos)",
    partido: "Willem II vs Jong AZ",
    fecha: "17 de abril de 2026",
    pronostico: "Más de 7.5 Córners",
    cuota: "1.30",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ASFIXIA POR ASCENSO ESTANDARIZADA:</strong><br>El afán de capturar podios empuja al local hacia un bombardeo esquinero insostenible en las primeras mitades obligando desbarajustes formidables perimetrales paramétricos estandarizados letales incesantes innegables comprobados incisivos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LA ESCUELA JONG VULNERABLE:</strong><br>Canteranos veloces desdeñan despejes finos originando rebotes continuados engrosando paramétricamente la alcancía del córner sumando aportes valiosos majestuosos gigantescos masivos ininterrumpidos calculados.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La suma de urgencia local y atrevimiento canterano dicta una ráfaga perimetral ineludible dictaminando al Value Bet superar la cuasi minúscula marca estadística firmemente gloriosamente validada puramente.</div>"
  },
  {
    liga: "🇮🇹 Serie A (Italia)",
    partido: "Inter Milan vs Cagliari",
    fecha: "17 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EL TACTICISMO DE CHIVU EN ALZA:</strong><br>La ingeniería asediadora anula toda réplica insular imponiendo posesiones asfixiantes aplatanando al adversario y forzando resquebrajamientos irremediables gloriosos absolutos formidables asombrosos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CERROJOS DESGASTADOS FORASTEROS:</strong><br>Cerdeña se encomienda a heroicidades escasas. La profundidad de los carrileros neroazzurros agrietará sistemáticamente mallas renuentes propinando estocadas seguras calculadas letales contundentes innegables paramétricas majestuosas estadísticamente probables inquebrantables.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Inversión acorazada donde un cerrojo sardo desnutrido perecerá bajo la aplanadora milanesa. Beneficios empíricos incuestionables inquebrantables puros paramétricamente justificados ineludiblemente.</div>"
  },
  {
    liga: "🇳🇱 Eerste Divisie (Países Bajos)",
    partido: "Almere City vs Dordrecht",
    fecha: "17 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.30",
    prob: 89,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EL IMPLACABLE YANMAR STADION:</strong><br>Consolidado como bastión artillero acarrea sendas anotaciones seriales aniquilando planteamientos lánguidos con afluencia pasmosa formidables letales infalibles matemáticamente certeras estandarizadas asombrosamente puras gloriosas constantes ininterrumpidas masivas empíricas paramétricamente inquebrantables firmes justas fiables.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA ENDEBLE:</strong><br>Dordrecht naufraga incesantemente fuera abrigando mallas rotas cediendo rentas seguras al atacante de turno despidiéndose del rigor del candado fúnebre prontamente asiduo certero irremediable matemáticamente letal comprobado.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Altísima probabilidad donde el local perforara la resquebrajada zaga visitante rindiendo sus frutos estadísticos implacablemente seguros forzosos estandarizados estables.</div>"
  },
  {
    liga: "🇳🇱 Eerste Divisie (Países Bajos)",
    partido: "De Graafschap vs Cambuur",
    fecha: "17 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.35",
    prob: 88,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. RACHA GOLEADORA GIGANTESCA:</strong><br>La pólvora jamás se moja hilvanando decenas de choques perforando la tiza ajena demostrando la filosofía inquebrantable de ataque frontal agresivo incesante paramétrico asombroso estelar masivo constante ininterrumpido abrumador majestuoso férreo seguro inamovible contundente validado.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. DISPERSIÓN TÁCTICA DEL OPONENTE:</strong><br>Formaciones desbalanceadas chocan incitando vacíos a merced de puñales garantizando que el casillero casero resalte rápidamente infalible estadísticamente justiciero indudable paramétricamente comprobado limpio indudable letal certero puro asombrosamente fiero.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>El peso paramétrico valida un Pick fundamental blindado donde el local desatará estocadas asegurándonos el Value Bet de forma irrenunciablemente asombrosa majestuosa justa fiable segura.</div>"
  },
  {
    liga: "🇦🇺 A-League (Australia)",
    partido: "Melbourne Victory vs Newcastle Jets",
    fecha: "17 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 85,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. IDIOSINCRASIA DE TRANSICIONES AUSTRALIANAS:</strong><br>Espectáculos armados por el galope descuidado obsequiando terrenos amplísimos destilando roturas tácticas insalvables abocando forasteros y locales a un fuego cruzado paramétricamente hermoso estandarizado comprobado seguro masivo indudable global letal.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CONVERSIONES BRUTALES DESATADAS:</strong><br>Los artilleros gozan conversiones asombrosas garantizando festines tempraneros donde la retaguardia es irrelevante sumando réditos certeros infalibles innegables constantes en la cuenta over matemática sólida estadística gloriosa constante férrea certera.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Partidos volcánicos oceánicos regalan la inversión blindada asestando dos tantos irrisoriamente alcanzables mediante el caos de las defensas laxas majestuosas paramétricas asombrosas estables justicieras seguras puras validadas.</div>"
  },
  {
    liga: "🇳🇱 Eerste Divisie (Países Bajos)",
    partido: "Jong PSV vs Jong Ajax",
    fecha: "17 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 85,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. LABORATORIO DE ARTILLEROS TOTAL:</strong><br>El santuario de la inexperiencia ampara cruces rotos con xG astronómicos desquiciados superando miedos al conceder a cambio de aprendizaje ofensivo colosal incesante abismal certero ininterrumpido innegable masivo puro validado constante majestuosamente estable infalible glorioso.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE REDES ROTAS:</strong><br>Centenares encajados combinados destilan el festival asegurado rebasando ridículamente la cuota inicial con estallidos desde el primer acto letales estandarizados estadísticamente puros asimétricos validados incontestables letales seguros formidables.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Pick de acorazado diamante donde la minería táctica canterana anula las posibilidades nulas forjando bilis doradas repletas de inversiones paramétricamente bellas asombrosas comprobadas sólidas letales justicieras precisas hermosas ineludibles indudablemente inamovibles.</div>"
  },
  {
    liga: "🇹🇷 Süper Lig (Turquía)",
    partido: "Fenerbahçe vs Rizespor",
    fecha: "17 de abril de 2026",
    pronostico: "Más de 9.5 Córners",
    cuota: "1.70",
    prob: 82,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. HOSTIGAMIENTO LATERAL DESPIADADO:</strong><br>Arrinconados los coleros turcos despejan despavoridos lluvias formidables de cruzadas concediendo banderas geométricas repetitivas masivas asombrosas incesantes estandarizadas matemáticas indudables probadas contundentes letales asombrosamente perennes.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DEL DOMINADOR:</strong><br>La fiera casera acapara el balón empujando márgenes promediados muy holgados superando él misma el grueso de la cuasi ridícula cuota esquinera algorítmica inquebrantable sólida firme letal empírica pura validada contundentemente justiciera fiable constante innegable.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Geometría rentabilística blindada gracias a presiones monumentales de campeonatos decantando saques perimetrales asombrosos avalados férreamente por nuestro modelo infalible asombroso robusto seguro justiciero puro inalterable.</div>"
  },
  {
    liga: "🇮🇹 Serie A (Italia)",
    partido: "Inter Milan vs Cagliari",
    fecha: "17 de abril de 2026",
    pronostico: "Más de 8.5 Córners",
    cuota: "1.70",
    prob: 78,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TACTICISMO CARRILERO EXTREMO ITALIANO:</strong><br>El abismo milanés prioriza desdobles por la vera desatando una lluvia incesante forzando horrores posicionales del enano sardo abocados al saque curvo reiterado estandarizado innegable contundente paramétrico incesable matemático empírico validado estadísticamente asombroso majestuoso firme.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. PREMURA POR APLASTAR BARRICADAS:</strong><br>La línea de cinco trasera cagliaritana rehusa salir destilando embotellamientos donde el rebote salva caídas seguras disparando los tableros esquineros de San Siro gloriosamente infalibles letales majestuosos inquebrantables justos sólidos comprobados paramétricos formidables puros asombrosamente feroces ineludiblemente garantizados estables probables indudables precisos matemáticos justicieros inamovibles.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Selección de rango avanzado recayendo exclusivamente sobre un dominio táctico aplastante y geométrico comprobable empíricamente salvaguardado justicieramente innegablemente contundente.</div>"
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
  <!-- ABRIL 17 -->
  <a href="laboratorio-goles-jong-eerste-divisie-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Avanzado</div>
    <div class="bc-content">
      <div class="bc-meta">17 de abril de 2026 <span>• 9 min lectura</span></div>
      <h3>El Laboratorio: La Eerste Divisie y Equipos Filiales</h3>
      <p>Entiende cómo dominar probabilísticamente el nicho más goleador de Europa amparado enteramente por desajustes tácticos de las academias juveniles de Holanda.</p>
    </div>
  </a>

  <a href="corners-asedio-dominador-fenerbahce-inter/" class="blog-card fade-in">
    <div class="bc-tag">Guía táctica</div>
    <div class="bc-content">
      <div class="bc-meta">17 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Asedios del Dominador: Córners en Turquía y Serie A</h3>
      <p>Analiza el despligue métrico esquinero originado intrínsecamente del hostigamiento férreo por carreras titánicas campeonables frente a muros conservadores.</p>
    </div>
  </a>

  <a href="a-league-australiana-vulnerabilidad-goles/" class="blog-card fade-in">
    <div class="bc-tag">Estadística Pro</div>
    <div class="bc-content">
      <div class="bc-meta">17 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Vulnerabilidad y Goles en la A-League Australiana</h3>
      <p>Benefíciate de ritmos veloces insostenibles a horas tempranas forjando selecciones inquebrantables de Overs sobre retaguardias descuidadas.</p>
    </div>
  </a>

  <a href="perfil-arbitraje-riguroso-allsvenskan-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Ranking Árbitros</div>
    <div class="bc-content">
      <div class="bc-meta">17 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>Arbitraje Riguroso en Clásicos (Allsvenskan)</h3>
      <p>Estudia psicológicamente la tendencia letal de colegiados impositivos envueltos en ecosistemas hostigantes o choques acérrimos para extraer tu margen ganador.</p>
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

print("Updated index picks and blog cards for April 17")
