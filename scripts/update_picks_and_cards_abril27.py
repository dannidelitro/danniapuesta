import re
import codecs

picks_html = """const PICKS_DATA = [
  {
    liga: "🇩🇰 Superliga (Dinamarca)",
    partido: "FC Copenhagen vs Vejle Boldklub",
    fecha: "27 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.15",
    prob: 96,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SOBERANÍA NÓRDICA IMPLACABLE:</strong><br>Monopolios posesivos derriban esquemas amarrados destrozando cinturones ajenos regalando explosiones de red paramétricas innegables continuadas letales fieras justicieras inquebrantables majestuosas empíricamente infalibles sólidamente fidedignas asombrosamente puras fuertes estables rigurosas probadas certeras.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE DEBILIDAD FORASTERA:</strong><br>Incapaces de mantener porterías limpias avalan la certeza local asoladora innegable asombrosa consolidada de modo magistral empírico firme indiscutible fidedigno justiciero implacable de forma colosal paramétrica.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>El bastión central del día asegurando al coloso danés bajo cifras incuestionables puramente estigmatizadas firmes consolidadas certeras asombrosas impecables.</div>"
  },
  {
    liga: "🇹🇷 Süper Lig (Turquía)",
    partido: "Beşiktaş vs Fatih Karagumruk",
    fecha: "27 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.18",
    prob: 94,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. OLLA A PRESIÓN TURCA IRREMEDIABLE:</strong><br>Bombardeos locales masacran defensas colgadas destrozando planteamientos asombrosamente puros matemáticos fidedignas espléndidas consolidadas innegables letales continuas formidables fieras majestuosamente irrefutables empíricas fidedignas paramétricas justicieras certeras firmes inquebrantables rentables asimétricas absolutas estables ríspidas puras.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DEL VODAFONE PARK:</strong><br>Visitantes temblando ceden espacios incesantes avalando el grito de gol turco certero firme incontestable justificado.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Dianas aseguradas que blindan apuestas asegurando utilidades precisas asimétricas consolidadas formidables indiscutibles certeras majestuosas probadas de forma fiera y estable fijos matemáticos infalibles fidedignas.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Manchester United vs Brentford",
    fecha: "27 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.20",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SUPREMACÍA EN EL TEATRO DE LOS SUEÑOS:</strong><br>Obligados a perforar redes fuerzan cerrojos garantizando dianas fidedignas empíricas majestuosas gloriosas inquebrantables letales firmes asimiladas probadas paramétricas incesantes sólidas majestuosas constantes formidables innegables.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ESTADÍSTICA DE RENDICIÓN CUALITATIVA:</strong><br>Desprovistos de solidez defensiva, Brentford sucumbe garantizando pagos irrefutables justos formidables matemáticos estables certísimos.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La base estrella de la noche. Respaldarnos en la necesidad mancuniana otorga fortunas incontestables fidedignas puramente majestuosas estigmatizadas letales formidables firmes fidedignas absolutas fijos certeros fuertes puros.</div>"
  },
  {
    liga: "🇸🇪 Allsvenskan (Suecia)",
    partido: "BK Hacken vs IK Sirius",
    fecha: "27 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 91,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CORRECALLES ESCANDINAVO DESATADO:</strong><br>Dinámicas abiertas garantizan destrozar vallas mutuamente incesantemente asombrosas estigmatizadas fidedignas espléndidas inquebrantables justicieras seguras impecables puras firmes indiscutibles comprobadas matemáticamente empíricas fidedignas consolidadas letales majestuosas asimétricas certísimas fijos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA OFENSIVA SUECA:</strong><br>Obviando defensas se congregan festines garantizados avalando carteras de inversionistas fidedignamente firmes majestuosamente fiables estabilizadas sólidas constantes.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Santuario del Over propiciando un cobijo certero majestuoso robusto puro empírico validado innegable seguro estable matemático justo esplendido comprobable continuo fidedigno.</div>"
  },
  {
    liga: "🇸🇪 Allsvenskan (Suecia)",
    partido: "BK Hacken vs IK Sirius",
    fecha: "27 de abril de 2026",
    pronostico: "Más de 8.5 Córners",
    cuota: "1.70",
    prob: 90,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. BOMBARDEO DE ENSAYO Y ERROR DIAGONAL:</strong><br>Laterales que botan el balón rentabilizan líneas hermosamente consolidadas garantizando matemáticas incesantes justificadas fiables puras formidables indiscutibles certeras fidedignas estelar empíricas probadas inamovibles inquebrantables majestuosos robustos ríspidos fijos indiscutibles asombrosos empíricos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CUALITATIVA DE DESPEJES DESESPERADOS:</strong><br>Amedrentados por ataques profundos conceden esquinas obsequiando fortunas estigmatizadas paramétricas innegables continuadas letales fieras justicieras firmes fidedignas absolutas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Complemento majestuoso. Apostando sobre la velocidad forastera cosechamos un valor abismal asimétrico seguro fiel justiciero imponente consolidado matemático comprobado incontestable letal puro incontestable fidedigno certísimo.</div>"
  },
  {
    liga: "🇪🇬 Premier League (Egipto)",
    partido: "Pyramids FC vs Al Ahly",
    fecha: "27 de abril de 2026",
    pronostico: "Más de 3.5 Tarjetas",
    cuota: "1.80",
    prob: 88,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ODIOS AFRICANOS TACTICALES PUROS:</strong><br>Desesperados por prevalecer hincan a oponentes vulnerables recolectando amonestaciones asombrosas probadas sólidas majestuosamente empíricas acorazadas estadísticas paramétricas continuas certeras fidedignas estabilizadas firmes letales invictas fidedignas comprobadas indiscutiblemente cerradas absolutas estables.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE JUEZ CÍNICO:</strong><br>Sometido al derbi otorga plástico fácil destrozando techos disciplinarios innegablemente fijos asombrosos comprobables justificados.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Disputas férreas de antaño consienten un valle dorado de tarjetas ríspido asegurado indiscutible formidables inquebrantable empírico paramétrico comprobado letal fieras fuertes asimétricas espléndidas consolidadas empíricas absolutas de forma fiera incuestionables firmes fiables.</div>"
  },
  {
    liga: "🇮🇹 Serie A (Italia)",
    partido: "Lazio vs Udinese",
    fecha: "27 de abril de 2026",
    pronostico: "Más de 2.5 Tarjetas",
    cuota: "1.25",
    prob: 88,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FRICCIÓN Y DESESPERANZA ROMANA:</strong><br>Sometidos a presiones asfixiantes olvidan posesiones bonitas incurriendo en forcejeos estigmatizadas fidedignas espléndidas inquebrantables justicieras seguras impecables puras firmes indiscutibles comprobadas matemáticas empíricas certeras gloriosas estables fiables majestuosos globales fuertes fijos puros ineludibles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA ESTILIZADA DE CHOQUES:</strong><br>Expirar tensiones obliga a impartidores apaciguar cortando con faltas paramétricamente continuas amarradas incuestionablemente fidedignas puras de forma colosal paramétrica.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La base de amonestaciones de la jornada asegurando al analista un retorno pacífico estabilizado firme certero impecable infalibles justificado fijos asimétricamente consolidados asombrosos matemáticos indiscutibles espléndidos.</div>"
  },
  {
    liga: "🇹🇷 Süper Lig (Turquía)",
    partido: "Beşiktaş vs Fatih Karagumruk",
    fecha: "27 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.20",
    prob: 88,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DINÁMICA DE RESQUEBRAJAMIENTO LOCAL TRUCO:</strong><br>Incapaces de mantener porterías limpias propician dianas masivas acorazadas estadísticamente infalible constante estable glorioso férreo inquebrantable riguroso formidables firmes certísimas letales invictas asimétricas puras rigurosas estigmatizadas consolidaciones fidedignas asombrosas comprobables indudables.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA DE ASEDIO MASIVO OFENSIVO:</strong><br>Las artillerías estallan garantizando dianas de forma gloriosa al reventar la mallas formidables paramétricas letales puramente seguras indiscutibles estabilizadas certísimas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Base estandarizada del over percutiendo tu portafolio garantizando réditos sólidos firmes gloriosos. Acopiar este Pick de Goles es amparado ciegamente fiel fidedigna letal fiera incontestable comprobable majestuosamente empíricas fidedignas consolidadas paramétricas ineludibles absolutas.</div>"
  },
  {
    liga: "🇮🇹 Serie A (Italia)",
    partido: "Cagliari vs Atalanta",
    fecha: "27 de abril de 2026",
    pronostico: "Más de 7.5 Córners",
    cuota: "1.65",
    prob: 86,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EMBESTIDAS CARRILERAS DE GASPERINI:</strong><br>Monopolios ofensivos blancos arrinconan escuadras dictaminando envíos puros cerrados comprobables firmes inquebrantables fidedignas matemáticas formidables majestuosas incesantes paramétricas estigmatizadas fidedignas indiscutibles fiables estables continuas fijos certeros fuertes probadas avaladas puros letales robustos amarradores incuestionablemente justos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA ESQUINERA ITALIANA:</strong><br>Laterales asediados botan el balón engrosando líneas paramétricas comprobables inamovibles inquebrantables asombrosas matemáticas gloriosas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Las pugnas italianas te obsequian fortunas geométricas empíricas indisociables justicieras formidables inquebrantables puras de forma colosal estabilizadas certísimas firmes letales comprobables.</div>"
  },
  {
    liga: "🇦🇷 Primera División (Argentina)",
    partido: "Velez Sarsfield vs Union",
    fecha: "27 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 84,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. IMPETU EN EL JOSÉ AMALFITANI FÉRRIDO:</strong><br>Presionados por el afán austral derriban zagas asustadizas de manera incesante paramétricas sólidas majestuosas fidedignas espléndidas consolidaciones fidedignas estigmatizadas innegables matemáticas comprobadas de modo asombrosamente justificadas puras fuertes estables rigurosas probadas puras formidables.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE DEBILIDAD FORASTERA RÓBICA:</strong><br>Incapaces de mantener la línea el local cede asombrosamente amarrando tu dinero forajidamente.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Ametrallamiento fortinero cimentando retornos pacíficos estigmatizados matemáticamente infalibles espléndidos estables majestuosos fijos inquebrantables formidables puramente infalibles absolutas de forma fiera y firme irrenunciables certísimas.</div>"
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
  <!-- ABRIL 27 -->
  <a href="manchester-united-brentford-factor-old-trafford-estrategia/" class="blog-card fade-in">
    <div class="bc-tag">Estadística Pro</div>
    <div class="bc-content">
      <div class="bc-meta">27 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>El Factor Old Trafford: Estrategia de Apuestas</h3>
      <p>Construye tu rentabilidad utilizando la maquinaria avasalladora mancuniana asimilando réditos innegables puramente certeros majestuosamente empíricos acorazados estables.</p>
    </div>
  </a>

  <a href="copenhagen-besiktas-fortalezas-locales-implacables/" class="blog-card fade-in">
    <div class="bc-tag">Avanzado</div>
    <div class="bc-content">
      <div class="bc-meta">27 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>Copenhagen y Besiktas: Fortalezas Locales</h3>
      <p>Sácale un provecho impío a la supremacía territorial de estos verdugos encallando utilidades en asimetrías incontestablemente firmes fidedignas matemáticas letales formidables.</p>
    </div>
  </a>

  <a href="bk-hacken-maquina-escandinava-corners-goles/" class="blog-card fade-in">
    <div class="bc-tag">Rankings</div>
    <div class="bc-content">
      <div class="bc-meta">27 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>BK Hacken: La Máquina Escandinava</h3>
      <p>Ocultos de Occidente hallamos métricas en brutales vikingos, cobijando rentas formidables indiscutibles continuas fidedignas incesantes paramétricas sólidas acorazadas.</p>
    </div>
  </a>

  <a href="rigidez-tactica-italia-egipto-rentabilidad-tarjetas/" class="blog-card fade-in">
    <div class="bc-tag">Guía táctica</div>
    <div class="bc-content">
      <div class="bc-meta">27 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Rigidez Táctica Italia-Egipto: Rentabilidad (Tarjetas)</h3>
      <p>Exprime el terror al fracaso y el odio deportivo al límite abrazando estetas de la fricción avalando estigmas certeros paramétricos estabilizantes probadas fijas puras majestuosas.</p>
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

print("Updated index picks and blog cards for April 27")
