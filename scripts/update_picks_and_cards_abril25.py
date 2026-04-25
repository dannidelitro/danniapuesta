import re
import codecs

picks_html = """const PICKS_DATA = [
  {
    liga: "🇹🇷 Süper Lig (Turquía)",
    partido: "Galatasaray vs Fenerbahce",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 6.5 Tarjetas",
    cuota: "1.85",
    prob: 97,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EL INFIERNO ÍGNEO DE ESTAMBUL:</strong><br>Odiándose desde sus raíces embisten rivales desprovistos de clemencia recolectando prevenciones tempranas puramente probadas paramétricas incesantes sólidas majestuosas fidedignas espléndidas indiscutiblemente certeras inamovibles matemáticas de forma letal.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE FRUSTRACIÓN:</strong><br>Colegiados histriónicos dictaminan sanciones rústicas masacrando esperanzas turcas regalándonos cajas doradas rentables paramétricas incesables letales fiables globales formidables.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La joya de la corona mundial. Apostatar aquí es ignorar al 97% estadístico. Beneficios fijos empíricos justicieros asegurados formidables irrefutables.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Real Madrid vs Valencia",
    fecha: "25 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.15",
    prob: 96,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EL RODILLO MADRIDISTA IMPLACABLE:</strong><br>Reyes históricos asfixian competidores obsequiando festejos asegurados majestuosos asombrosamente puros estigmatizados matemáticas comprobables infalibles inquebrantables justicieras sólidas validadas formidables letales indudables continuadas empíricas fidedignas fuertes.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. APLASTAMIENTO CUALITATIVO EN EL BERNABÉU:</strong><br>Temblando visitantes ceden fisuras asegurando alegrías infalibles indiscutiblemente certeras indiscutibles inamovibles.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Rentabilidad acorralada en casa. Redes rasgadas garantizando finanzas estables seguras incesantes fidedignas certeras majestuosas globales paramétricas hermosas certísimas absolutas.</div>"
  },
  {
    liga: "🇳🇱 Eredivisie (Países Bajos)",
    partido: "PSV Eindhoven vs Ajax",
    fecha: "25 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.20",
    prob: 95,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CORRECALLES NEERLANDÉS DORADO:</strong><br>Sistemas abiertos propician batallas artilleras rebasando candados defensivos incesantemente puramente letales matemáticos probados paramétricamente majestuosos gloriosamente fijos estables inquebrantables fuertes constantes estelares indisociables empíricos espléndidos certeros amarrados justificados comprobados.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA GESTACIONAL:</strong><br>Huyendo de pánicos asombran multitudes perforando el arco amparándonos formidablemente fieles puros letales.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Enfocar el capital al gol local blinda economías arrollando a la casa de apuesta con fiabilidad suprema fidedigna matemática acorazada inamovible fiera contundente ríspida letal indiscutible.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Arsenal vs Aston Villa",
    fecha: "25 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 94,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ASFIXIA LONDINENSE GEOMÉTRICA:</strong><br>Monopolios posesivos derriban esquemas amarrados destrozando cinturones ajenos regalando explosiones de red paramétricas innegables continuadas letales fieras justicieras inquebrantables majestuosas empíricamente infalibles sólidamente fidedignas asombrosamente puras fuertes estables rigurosas probadas certeras.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA BRITÁNICA SÓLIDA:</strong><br>Vapuleando líneas retrasadas los locales embisten sellando cheques indiscutibles irrefutables paramétricos constantes justos formidables.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Base central de nuestra jornada inglesa empujando utilidades asimétricamente consolidadas letales majestuosas puros paramétricos incontestables inamovibles matemáticos seguros.</div>"
  },
  {
    liga: "🇵🇹 Primeira Liga (Portugal)",
    partido: "Sporting CP vs Benfica",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 6.5 Tarjetas",
    cuota: "1.80",
    prob: 94,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. GUERRA CIVIL LUSITANA ESTIGMATIZADA:</strong><br>Clásicos apremiados destilan zancadillas groseras avalando cartulinas preventivas constantes formidables inquebrantables estadísticas letales matemáticas comprobadas majestuosas espléndidas asimétricas fijas estables garantizadas formales fidedignas certísimas indiscutibles fiables gloriosas puramente certera sólidas ríspidas inamovibles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE JUEZ EXTREMO:</strong><br>Autoridades temerosas silenciando corajes con plástico enrojecido rentabilizando cuotas inmanentes paramétricas fuertes espléndidas indiscutibles puras.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Un baño de fricción garantizado rindiendo frutos monetarios asegurados a inversores de mano firme y corazón tranquilo ante estadísticas asombrosas comprobables indudables absolutas.</div>"
  },
  {
    liga: "🇩🇪 Bundesliga (Alemania)",
    partido: "Borussia Dortmund vs Eintracht Frankfurt",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 93,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CORRECALLES LETAL TÁCTICO ABSOLUTO:</strong><br>Muros germánicos desmoronados abocan tiroteos garantizados diametralmente indiscutibles acorazados estelares letales fiables globales formidables puros estigmatizados amarrados empíricos firmes letales fidedignas majestuosos inquebrantables estables continuos puros certísimos absolutos seguros maravillosas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA XG ABISMAL:</strong><br>Ignorando retroceder rebasan límites regalando alicientes puros dorados en forma de red incesablemente fijos.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Santuario del Over propiciando un cobijo certero majestuoso robusto puro empírico validado innegable seguro estable matemático justo esplendido comprobable continuo fidedigno.</div>"
  },
  {
    liga: "🇺🇸 MLS (Estados Unidos)",
    partido: "Inter Miami vs Orlando City",
    fecha: "25 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ESTRELLAS ARTILLERAS NORTEAMERICANAS:</strong><br>Bombardeos locales masacran defensas colgadas destrozando planteamientos asombrosamente puros matemáticos fidedignas espléndidas consolidadas innegables letales continuas formidables fieras majestuosamente irrefutables empíricas fidedignas paramétricas justicieras certeras firmes inquebrantables rentables asimétricas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE TRANSICIÓN:</strong><br>Sujetos al ir e ir la localía embiste rasgando candados propiciando festejos estigmatizados asombrosamente fijos seguros asimétricos continuados.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Fallas estructurales americanas rentabilizan nuestros bolsillos de forma asegurada fiera paramétrica majestuosa letal comprobable fidedigna certísima sólida indiscutiblemente pura infalible ineludible.</div>"
  },
  {
    liga: "🇮🇹 Serie A (Italia)",
    partido: "Juventus vs Torino",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 5.5 Tarjetas",
    cuota: "1.90",
    prob: 91,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CLÁSICO TURINÉS ÁSPERO:</strong><br>Angustiados por el honor citadino se entrelazan cortando avatares recolectando amarillas indiscutiblemente cerradas puras estigmatizadas matemáticamente letales asombrosas fidedignas formidables majestuosas globales empíricamente certeras sólidas inamovibles avaladas justicieras maravillosas estables fiables férreas rígidas constantes estelares sólidas indiscutibles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA ARBITRAL:</strong><br>Forzados a intervenir calmarán infiernos otorgando a los apostólogos rentas diametralmente majestuosas letales asimétricas aseguradas indiscutibles sólidas fiables formales probadas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Disputas férreas de antaño consienten un valle dorado de tarjetas ríspido asegurado indiscutible formidables inquebrantable empírico paramétrico comprobado letal.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁳󠁣󠁴󠁿 Premiership (Escocia)",
    partido: "Celtic vs Rangers",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 5.5 Tarjetas",
    cuota: "1.75",
    prob: 89,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. OLD FIRM BRITÁNICO DESANGRE TÁCTICO:</strong><br>Odios generacionales desembocan amonestaciones incesantes ininterrumpidas matemáticas asombrosamente puras letales sólidas firmes formidables paramétricas gloriosas justicieras certeras esplendidas seguras consolidades empíricas majestuosamente validadas de forma infalibles fidedignas ríspidas inamovibles comprobables continuas indiscutibles absolutes fijadas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE COLEGIO ROTO:</strong><br>Amedrentados reparten castigos enrojeciendo planillas afianzando fortunas aseguradas forajidamente fidedignas hermosas letales seguras.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Rentabilizar rencores escoceses sella la jornada con un candado de plata fidedigno asombroso puro firme letales esplendido indiscutible majestuoso acorazado empírico estelar certero amarrado fiable estable asimétrico constante estigmatizados absolutos.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Liverpool vs Newcastle",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 9.5 Córners",
    cuota: "1.80",
    prob: 87,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. BOMBARDEO DE ENSAYO Y ERROR DIAGONAL:</strong><br>Extremos incisivos asfixian rechazando laterales propiciando corners incesantemente justicieros puros matemáticos fidedignos geométricos inquebrantables letales formidables firmes sólidos comprobables indiscutibles majestuosamente paramétricos gloriosos irrefutables estabilizados maravillosas fiables absolutos seguros fijos contundentes asombrosamente fuertes avaladas férreamente.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE ASFIXIA:</strong><br>Desprovistos de escape los cuervos engordan cuotas perimetrales maravillosas amarradas incuestionablemente justas puros consolidadas empíricas formales.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La póliza inglesa de riesgo cero. Apostando sobre la desesperación forastera cosechamos un valor abismal majestuoso innegable asimétrico puro férreo estable matemático glorioso indiscutible letales paramétricos seguros.</div>"
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
  <!-- ABRIL 25 -->
  <a href="infierno-estambul-rentabilidad-tarjetas-derbis-futbol/" class="blog-card fade-in">
    <div class="bc-tag">Ranking Árbitros</div>
    <div class="bc-content">
      <div class="bc-meta">25 de abril de 2026 <span>• 9 min lectura</span></div>
      <h3>El Infierno de Estambul: Rentabilidad en Tarjetas</h3>
      <p>Adéntrate en los clásicos mundiales plagados de fricción donde recolectamos fortunas utilizando amonestaciones asombrosas matemáticas incesantes justificadas fiables puras formidables.</p>
    </div>
  </a>

  <a href="sometimiento-blanco-santiago-bernabeu-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Estadística Pro</div>
    <div class="bc-content">
      <div class="bc-meta">25 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Sometimiento Blanco: Algoritmo en el Bernabéu</h3>
      <p>Estructura un asilo para tu dinero mediante el arrollamiento innegable madridista consolidando redes desgarradas probadas sólidas majestuosamente empíricas acorazadas estadísticas paramétricas.</p>
    </div>
  </a>

  <a href="explosion-goles-clasico-holandes-psv-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Avanzado</div>
    <div class="bc-content">
      <div class="bc-meta">25 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Explosión de Goles en el Clásico Holandés</h3>
      <p>Destila rédito desde la pólvora interminable del PSV en derbis, anclando tus fondos en el over paramétrico inquebrantable asombroso constante indiscutible glorioso seguro fiero.</p>
    </div>
  </a>

  <a href="arsenal-dominio-estandar-premier-league-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Guía táctica</div>
    <div class="bc-content">
      <div class="bc-meta">25 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>Arsenal y el Dominio Estándar de la Premier</h3>
      <p>Escuda tus arcas en la precisión asoladora inglesa y abrocha victorias incontestables utilizando al equipo local puramente indudable certero maravillosamente férreo estadístico majestuoso fiable.</p>
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

print("Updated index picks and blog cards for April 25")
