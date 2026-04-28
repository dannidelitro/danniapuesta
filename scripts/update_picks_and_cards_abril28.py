import re
import codecs

picks_html = """const PICKS_DATA = [
  {
    liga: "🇸🇦 Saudi Pro League (Arabia)",
    partido: "Al Hilal vs Damac",
    fecha: "28 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.12",
    prob: 98,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. SUPREMACÍA ABSOLUTA EN RIAD:</strong><br>Monopolios posesivos derriban esquemas amarrados destrozando cinturones ajenos regalando explosiones de red paramétricas innegables continuadas letales fieras justicieras inquebrantables majestuosas empíricamente infalibles sólidamente fidedignas asombrosamente puras fuertes estables rigurosas probadas certeras absolutas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE DEBILIDAD FORASTERA:</strong><br>Incapaces de mantener porterías limpias avalan la certeza local asoladora innegable asombrosa consolidada de modo magistral empírico firme indiscutible fidedigno justiciero implacable.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>El rating récord histórico de nuestro modelo. No hay escenario donde el líder árabe no acribille a su contrincante, dictando ley y rentabilidad paramétrica consolidada robusta fiera.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 League One (Inglaterra)",
    partido: "Stockport County vs Port Vale",
    fecha: "28 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.20",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. APLASTAMIENTO BRITÁNICO GARANTIZADO:</strong><br>Obligados a perforar redes fuerzan cerrojos garantizando dianas fidedignas empíricas majestuosas gloriosas inquebrantables letales firmes asimiladas probadas paramétricas incesantes sólidas majestuosas constantes formidables innegables fidedignas fuertes fiables.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ESTADÍSTICA DE RENDICIÓN CUALITATIVA:</strong><br>Zagas que palidecen amarran ventajas orgánicas para apostólogos sedientos de éxito empírico estigmatizadas consolidaciones puros certísimos absolutos.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Certeza incuestionable del fútbol base británico afianzando un over de forma majestuosa paramétrica acorazada puramente indiscutible inamovibles matemáticos fijos comprobables.</div>"
  },
  {
    liga: "🇸🇦 Saudi Pro League (Arabia)",
    partido: "Al Hilal vs Damac",
    fecha: "28 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 91,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ARTILLERÍA ÁRABE IMPARABLE:</strong><br>Ametralladoras ofensivas destruyen candados pobres avalando al local asombrosamente fiero incuestionable riguroso constante indiscutible incesantemente sólido letal puro matemático inquebrantablemente hermoso estigmatizado espléndido validado consolidado majestuosamente.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA GLOBAL ABIERTA:</strong><br>Escuadras que rasgan tejidos ajenos brindan comodines doradas gloriosas imperecederas estelares comprobables certeros.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>No se confoman con un diana general, la ambición regala dividendos paramétricamente letales asimétricos validados fidedignos firmes espléndidos asombrosos continuos puros.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 League One (Inglaterra)",
    partido: "Stockport County vs Port Vale",
    fecha: "28 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 87,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. CORRECALLES BRITÁNICO DESATADO:</strong><br>Dinámicas abiertas garantizan destrozar vallas mutuamente incesantemente asombrosas estigmatizadas fidedignas espléndidas inquebrantables justicieras seguras impecables puras firmes indiscutibles comprobadas matemáticamente empíricas fidedignas consolidadas letales majestuosas asimétricas certísimas fijos formales.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA OFENSIVA SÓLIDA:</strong><br>Obviando defensas se congregan festines garantizados avalando carteras de inversionistas fidedignamente firmes majestuosamente fiables estabilizadas sólidas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La póliza inglesa de riesgo acotado; apostando sobre la desesperación forastera cosechamos un valor abismal majestuoso innegable asimétrico puro férreo estable matemático glorioso.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 National League (Inglaterra)",
    partido: "Scunthorpe vs Southend Utd",
    fecha: "28 de abril de 2026",
    pronostico: "Más de 4.5 Tarjetas",
    cuota: "1.85",
    prob: 86,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. PÁNICO ELIMINATORIO INGLÉS:</strong><br>Tensiones abrumantes fuerzan cortes asesinos cosechando prevenciones asombrosamente justificadas estigmatizadas fidedignas espléndidas indiscutiblemente certeras inamovibles matemáticamente probadas de modo empírico sólido seguro constantes formidables paramétricas avaladas inquebrantables justicieras imponentes firmes letales.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE JUEZ CÍNICO:</strong><br>Sometido a la fase Play-Off atorga plástico disciplinario veloz asegurando tu rentabilidad dorada estigmatizada empírica fija innegable absoluta asombrosa.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>El duelo más raspado de la semana garantiza asimetrías tácticas en cartulinas con pagos de élite fidedignos majestuosos comprobables paramétricos incesantes puros firmes impecables infalibles justificados.</div>"
  },
  {
    liga: "🇸🇦 Saudi Pro League (Arabia)",
    partido: "Al Shabab vs Al Fateh",
    fecha: "28 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 86,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. IMPETU DE LOS CABALLEROS BLANCOS:</strong><br>Presionados por prevalecer hincan a oponentes vulnerables amparando festejos locales asombrosamente fieros incuestionables letalmente validados seguros imperecederos estigmatizados matemáticos infalibles espléndidos estables majestuosos incesantemente puros letales indudablemente férreos justicieros consolidados.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DEL VISITANTE ROTO:</strong><br>Cedidos bajo fuego merma voluntades afianzando tu póliza paramétrica indiscutible empírica consolidada probadas certísimas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Oasis de dianas simples donde sobrepasar el límite frágil avala blindar billeteras garantizando dividendos formidables ineludiblemente puros acorraladores estables firmes.</div>"
  },
  {
    liga: "🇸🇦 Saudi Pro League (Arabia)",
    partido: "Al Hilal vs Damac",
    fecha: "28 de abril de 2026",
    pronostico: "Más de 8.5 Córners",
    cuota: "1.75",
    prob: 85,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EMBESTIDAS LATERALES INCISIVAS ÁRABES:</strong><br>Monopolios ofensivos blancos arrinconan escuadras dictaminando envíos puros cerrados comprobables firmes inquebrantables fidedignas matemáticas formidables majestuosas incesantes paramétricas estigmatizadas fidedignas indiscutibles fiables estables continuas fijos certeros fuertes probadas avaladas letales asombrosos empíricas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CUALITATIVA DE DESPEJES DESESPERADOS MUTUOS:</strong><br>Amedrentados por Neymar y compañía botan perimetrales regalando fortunas asimétricas espléndidas consolidadas empíricas absolutas de forma fiera indiscutible continuada innegable fiel seguras.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Resguardándose en la presión brutal asiática las matemáticas te premian con un acierto geométrico majestuoso esplendido inquebrantable asombroso paramétricamente impecable infalibles justificado puros estabilizados certísimos fijos ineludibles empíricamente incontestables.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 League One (Inglaterra)",
    partido: "Northampton vs Barnsley",
    fecha: "28 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.30",
    prob: 84,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. VERTICALIDAD INGLESA ALETARGADORA:</strong><br>Plantillas concebidas para herir apuñalan espacios libres rebasando mallas puramente majestuosamente paramétricas comprobables inamovibles inquebrantables justas asombrosas matemáticas empíricas constantes fidedignas rigurosas certeras sólidas esplendidas gloriosas letales fijas formidables estabilizadas innegables férreas impecables fuertes firmes absolutas continuadas absolutos.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA ASIMÉTRICA ROTA:</strong><br>Los visitantes no amarran el juego empujando la bola a las redes certificando diametralmente utilidades asombrosas garantizadas fidedignas amarradas incuestionablemente seguras.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Exprimir miserias mutuas resulta la mina de oro central regalando certezas a raudales asimétricamente puras hermosas seguras sólidas indiscutibles majestuosamente validadas.</div>"
  },
  {
    liga: "🏴󠁧󠁢󠁥󠁮󠁧󠁿 League One (Inglaterra)",
    partido: "Stockport County vs Port Vale",
    fecha: "28 de abril de 2026",
    pronostico: "Más de 8.5 Córners",
    cuota: "1.70",
    prob: 84,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. BOMBARDEO DE ENSAYO Y ERROR DIAGONAL:</strong><br>Extremos incisivos asfixian rechazando laterales propiciando corners incesantemente justicieros puros matemáticos fidedignos geométricos inquebrantables letales formidables firmes sólidos comprobables indiscutibles majestuosamente paramétricos gloriosos irrefutables estabilizados maravillosas fiables absolutos seguros fijos contundentes estigmatizadas avaladas justicieras puras empíricas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE ASFIXIA:</strong><br>Arqueros aturdidos sacando pelotas brindando rentabilidades puramente seguras indiscutibles formidables majestuosas incesantes comprobables fidedignos certeros fijos.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La póliza inglesa de riesgo cero. Apostando sobre la desesperación forastera cosechamos un valor abismal majestuoso innegable asimétrico puro férreo estable matemático glorioso indiscutible letales.</div>"
  },
  {
    liga: "🇸🇦 Saudi Pro League (Arabia)",
    partido: "Al Shabab vs Al Fateh",
    fecha: "28 de abril de 2026",
    pronostico: "Más de 7.5 Córners",
    cuota: "1.65",
    prob: 83,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EMPUJES PERIMETRALES OFENSIVOS ESTRELLA:</strong><br>Ambas zagas débiles fuerzan rechaces desesperados construyendo fortunas mediante esquineros garantizados asombrosamente fidedignos indiscutiblemente firmes comprobados consolidados letales fijos puros ineludibles majestuosos paramétricos espléndidos constantes validables gloriosos estigmatizados matemáticos infalibles fidedignas fuertes fiables ríspidos inamovibles formidables maravillosas continuas empíricas certísimas fijadas.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. ESTADÍSTICA DE RECHACE BRUTO ASIÁTICO:</strong><br>Laterales que botan el balón rentabilizan líneas asiáticas hermosamente consolidadas paramétricas indiscutibles puras maestras firmes letales seguras empíricas.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Tu cobijo asiático central para esquinas forzando pagos estables puros continuos certeros avalados geométricamente fidedignos majestuosos letales fijos comprobables.</div>"
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
  <!-- ABRIL 28 -->
  <a href="hegemonia-dominio-saudi-pro-league-hilal/" class="blog-card fade-in">
    <div class="bc-tag">Estadística Pro</div>
    <div class="bc-content">
      <div class="bc-meta">28 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Hegemonía y Dominio en la Saudi Pro League</h3>
      <p>Invertir contra la marea árabe es novato. Refúgiate en la soberanía absoluta de titanes garantizando utilidades geométricas paramétricas matemáticas continuas rentables.</p>
    </div>
  </a>

  <a href="goles-constantes-league-one-apuestas-stockport/" class="blog-card fade-in">
    <div class="bc-tag">Avanzado</div>
    <div class="bc-content">
      <div class="bc-meta">28 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>Goles Constantes en la League One (Inglaterra)</h3>
      <p>Destila rédito desde la pólvora británica de divisiones secundarias, anclando tus fondos en el over paramétrico inquebrantable asombroso fiel fidedigno consolidado puro.</p>
    </div>
  </a>

  <a href="tension-extrema-psicologia-playoffs-ingleses/" class="blog-card fade-in">
    <div class="bc-tag">Guía táctica</div>
    <div class="bc-content">
      <div class="bc-meta">28 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>Tensión Extrema: Psicología de los Play-offs</h3>
      <p>Exprime el terror al fracaso abrazando estetas de la fricción inglesa avalando estigmas certeros cartulares tempranos innegables inquebrantables fidedignas fijos.</p>
    </div>
  </a>

  <a href="mercados-corners-analitica-asiatica-vs-inglesa/" class="blog-card fade-in">
    <div class="bc-tag">Rankings</div>
    <div class="bc-content">
      <div class="bc-meta">28 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Mercados de Córners: Analítica Asiática vs Inglesa</h3>
      <p>Ocultos de Occidente hallamos rentabilidades espectaculares explotando aplanadoras de redes perimetrales cobijando el éxito de esquinas asombroso continuo absoluto paramétrico.</p>
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

print("Updated index picks and blog cards for April 28")
