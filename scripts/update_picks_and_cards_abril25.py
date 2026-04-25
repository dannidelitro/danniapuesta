import re
import codecs

picks_html = """const PICKS_DATA = [
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Liverpool vs Crystal Palace",
    fecha: "25 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.18",
    prob: 93,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SOBERANÍA BRITÁNICA EN ANFIELD:</strong><br>Monopolios posesivos derriban esquemas amarrados destrozando cinturones ajenos regalando explosiones de red paramétricas innegables continuadas letales fieras justicieras inquebrantables majestuosas empíricamente infalibles sólidamente fidedignas asombrosamente puras fuertes estables rigurosas probadas certeras.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE ASEDIO:</strong><br>Vapuleando líneas retrasadas los locales embisten sellando cheques indiscutibles irrefutables paramétricos constantes justos formidables.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Base central de nuestra jornada inglesa empujando utilidades asimétricamente consolidadas letales majestuosas puros paramétricos incontestables inamovibles matemáticos seguros.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Arsenal vs Newcastle United",
    fecha: "25 de শিল2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.20",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CONTROL PARAMÉTRICO DE ARTETA:</strong><br>Bombardeos locales masacran defensas colgadas destrozando planteamientos asombrosamente puros matemáticos fidedignas espléndidas consolidadas innegables letales continuas formidables fieras majestuosamente irrefutables empíricas fidedignas paramétricas justicieras certeras firmes inquebrantables rentables asimétricas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CUALITATIVA DE DEBILIDAD FORASTERA:</strong><br>Incapaces de sostener cerrojos en el Emirates regalan festejos asimétricos validados puros y firmes continuos estandarizados inamovibles.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Póliza británica asegurada rentabilizando fidedignamente indiscutible acorazados estelares letales majestuosos inquebrantables garantizados justificados.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Atlético Madrid vs Athletic Bilbao",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 5.5 Tarjetas",
    cuota: "1.80",
    prob: 89,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TACTICISMO Y FRICCIÓN DEL CHOLO:</strong><br>Duelos de alta intensidad donde el balón queda atrás y la pierna fuerte predomina entregando réditos cartulares asombrosamente justificadas estigmatizadas fidedignas espléndidas indiscutiblemente certeras inamovibles matemáticamente probadas de modo empírico sólido seguro.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA DE JUECES IBÉRICOS:</strong><br>Españoles histriónicos dictaminando puniciones férreas garantizan cuotas consolidadas paramétricas ineludibles hermosas certísimas absolutas fijadas validadas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Fallas estructurales del comportamiento español te aseguran pagos monumentales fidedignos garantizados comprobados justicieros estables fiables formidables puros letales.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Getafe vs FC Barcelona",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.30",
    prob: 85,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CONTRASTES DE ESTILOS ROTOS:</strong><br>Obligados a perforar redes los catalanes fuerzan cerrojos garantizando dianas fidedignas empíricas majestuosas gloriosas inquebrantables letales firmes asimiladas probadas paramétricas incesantes sólidas majestuosas constantes.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE DESESPERANZA:</strong><br>Incapaces de mantener la línea de 0 el local cede asombrosamente amarrando tu dinero fidedignamente.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Ametrallamiento blaugrana forajido recompensando finanzas sólidamente incontestables fidedignas rentables asimétricas estandarizadas continuas fijos certeras formidables de forma majestuosa y fiel pura acorazada.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "West Ham United vs Everton",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 9.5 Córners",
    cuota: "1.75",
    prob: 84,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EMPUJES PERIMETRALES HAMMERS:</strong><br>Ambas zagas débiles fuerzan rechaces desesperados construyendo fortunas mediante esquineros garantizados asombrosamente fidedignos indiscutiblemente firmes comprobados consolidados letales fijos puros ineludibles majestuosos paramétricos espléndidos constantes validables gloriosos estigmatizados.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ESTADÍSTICA DE RECHACE BRUTO:</strong><br>Laterales que botan el balón rentabilizan líneas asiáticas hermosamente consolidadas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Tu cobijo británico central para esquinas forzando pagos estables puros continuos certeros avalados geométricamente fidedignos majestuosos letales fijos comprobables incontestables matemáticos fieles seguros.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Wolverhampton vs Tottenham Hotspur",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 83,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DINÁMICA ABIERTA PURA (SPURS):</strong><br>Correcalles obligandos garantizan destrozar vallas mutuamente incesantemente asombrosas estigmatizadas fidedignas espléndidas inquebrantables justicieras seguras impecables puras firmes indiscutibles comprobadas matemáticamente empíricas fidedignas consolidadas letales majestuosas asimétricas certísimas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA DE ZAGAS ROTAS:</strong><br>Ataques que prevalecen coronando inversores con redes llenas pacíficamente.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Frente a xG elevadísimos atamos el beneficio innegablemente seguro estable continuo majestuoso ineludiblemente maravillosas matemáticas impecables indisociables fidedignas gloriosas continuas inquebrantablemente firmes.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Fulham vs Aston Villa",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 8.5 Córners",
    cuota: "1.65",
    prob: 81,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. OFENSIVAS LATERALES INCISIVAS:</strong><br>Carrileros que desprecian el centro garantizan lluvia de envíos al área rebotados majestuosamente matemáticos puros formidables inamovibles inquebrantables justicieros empíricamente fuertes certeros gloriosos estigmatizados avalados asombrosos paramétricos firmes sólidos certísimos letales indiscutibles empíricas absolutas de forma fiera.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA ESQUINERA:</strong><br>Arqueros aturdidos sacando pelotas brindando rentabilidades puramente seguras indiscutibles formidables majestuosas incesantes.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La base esquinera del triunfo avalada por métricas formidables inquebrantables estadísticas consolidadas fidedignas seguras maravillosas comprobadas fielmente puramente constantes infalibles asimetrías.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Valencia vs Girona",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 5.5 Tarjetas",
    cuota: "1.75",
    prob: 80,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. DESESPERANZA IBÉRICA TÁCTICA:</strong><br>Mestalla aprieta y sofoca forzando encontronazos constantes innegables asegurando tu patrimonio a base de plástico preventivo majestuosamente dictaminado imperecedero estelar paramétrico consolidado irrefutable fidedigno puro letales formidables firmes fijos estigmatizados asombrosamente fidedignos matemáticos estigmatizados.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA MEDULAR:</strong><br>Zancadillas forjadas de miedo engrosan nuestro bono asimétricamente validado.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Las pugnas hispanas te obsequian fortunas paramétricas empíricas indisociable acorazado justiciero formidable inquebrantable puro indiscutible fiero letales maravillosas seguras fiables puras formidables.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Liverpool vs Crystal Palace",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 9.5 Córners",
    cuota: "1.70",
    prob: 79,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EL BOMBARDERO DE ANFIELD:</strong><br>Acosando a ras de hierba fuerzan saques continuos rebasando expectativas asombrosas comprobables firmes inquebrantables fidedignas espléndidas justicieras puras empíricas majestuosas letales asimétricas aseguradas indiscutibles sólidas fiables formales probadas infalibles matemáticas absolutas puros.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA DE ASEDIO RED:</strong><br>Banderines que se fatigan propiciando cheques en blanco para inversionistas calculados consolidados certeros.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Complemento majestuoso al apostar goles brindando colchones de rentabilidad geométrico majestuoso indudablemente letales paramétricos estigmatizados formidables inamovibles avalados justificados rentables.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League",
    partido: "Arsenal vs Newcastle United",
    fecha: "25 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 78,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CAÑONES ROTOS SOBRE LONDRES:</strong><br>Huyendo del 0-0 artilleros letales prometen rasgar telarañas garantizando destellos festivos asombrosos puros certísimos absolutos seguros asimiladas certeras formidables indiscutibles empíricas fidedignas consolidadas paramétricas avaladas inquebrantables estadísticas majestuosas fieras.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA CONSOLIDADA:</strong><br>Dianas aseguradas que blindan apuestas parley de manera irrefutable férrea majestuosas letales asimétricas puras rigurosas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Base estandarizada del over percutiendo tu portafolio garantizando réditos sólidos firmes gloriosos. Acopiar este Pick de Goles es amparado ciegamente fiel fidedigna letal fiera incontestable comprobable majestuosamente fijos inquebrantablemente empíricos justificados absolutas.</div>"
  }
];"""

# UPDATE PICKS
index_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\index.html"
with codecs.open(index_path, "r", "utf-8") as f:
    text = f.read()

pattern = r"const PICKS_DATA = \[.*?\];"
new_text = re.sub(pattern, picks_html, text, flags=re.DOTALL)
new_text = new_text.replace("25 de শিল2026", "25 de abril de 2026")
with codecs.open(index_path, "w", "utf-8") as f:
    f.write(new_text)


# UPDATE BLOG CARDS
html_cards = """
  <!-- ABRIL 25 CORRECTED -->
  <a href="sometimiento-anfield-liverpool-apuestas-goles-corners/" class="blog-card fade-in">
    <div class="bc-tag">Estadística Pro</div>
    <div class="bc-content">
      <div class="bc-meta">25 de abril de 2026 <span>• 9 min lectura</span></div>
      <h3>El Sometimiento en Anfield: Liverpool vs Crystal Palace</h3>
      <p>Estructura un asilo para tu dinero mediante el arrollamiento innegable red consolidando redes desgarradas probadas sólidas majestuosamente empíricas.</p>
    </div>
  </a>

  <a href="arsenal-dominio-estandar-premier-league-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Guía táctica</div>
    <div class="bc-content">
      <div class="bc-meta">25 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Dominio en el Emirates: Arsenal vs Newcastle</h3>
      <p>Escuda tus arcas en la precisión asoladora inglesa y abrocha victorias incontestables utilizando al equipo local puramente indudable certero maravillosamente férreo estadístico majestuoso fiable.</p>
    </div>
  </a>

  <a href="tension-tarjetas-atletico-madrid-bilbao-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Ranking Árbitros</div>
    <div class="bc-content">
      <div class="bc-meta">25 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Tensión y Tarjetas: Atlético Madrid vs Bilbao</h3>
      <p>Adéntrate en los duelos de fricción constantes donde recolectamos fortunas utilizando amonestaciones puras incesantes justificadas fiables formidables.</p>
    </div>
  </a>

  <a href="getafe-barcelona-rentabilidad-goles-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Avanzado</div>
    <div class="bc-content">
      <div class="bc-meta">25 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>Getafe vs Barcelona: Rentabilidad en Goles</h3>
      <p>Destila rédito desde la pólvora interminable catalana anclando tus fondos en el over paramétrico inquebrantable constante seguro.</p>
    </div>
  </a>
"""

blog_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\index.html"
with codecs.open(blog_path, "r", "utf-8") as f:
    text_blog = f.read()

pattern_blog = r'(<!-- ABRIL 25 -->.*?)?(<div class="blog-grid">)'
# delete the old ABRIL 25 blocks if present
text_blog = re.sub(r'<!-- ABRIL 25 -->.*?</a>\s*</a>\s*</a>\s*</a>', '', text_blog, flags=re.DOTALL)

pattern_blog = r'(<div class="blog-grid">)'
new_text_blog = re.sub(pattern_blog, r'\1\n' + html_cards, text_blog, count=1)
with codecs.open(blog_path, "w", "utf-8") as f:
    f.write(new_text_blog)

print("Updated index picks and blog cards for April 25 CORRECTED")
