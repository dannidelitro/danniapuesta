import re
import codecs

picks_html = """const PICKS_DATA = [
  {
    liga: "🇳🇱 Eredivisie (Países Bajos)",
    partido: "PSV Eindhoven vs PEC Zwolle",
    fecha: "23 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.15",
    prob: 92,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. APLANADORA HOLANDESA ABSOLUTA:</strong><br>Ostentando ritmos escandalosos de dianas esta aplanadora aniquila la voluntad de forasteros desprotegidos garantizando alegrías puras estadísticas incontestables paramétricas sólidas abismales constantes ininterrumpidas imponentes.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE DEBILIDAD:</strong><br>Cedidos bajo fuego los rivales merman sus posibilidades afianzando a fuego y plomo nuestra estela recolectora dorada innegable fidedigna certera.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>El bastión numérico principal de esta jornada. Prediccion con más de un 90% empírico validable ineludible que abriga y protege rendimientos gloriosamente comprobados.</div>"
  },
  {
    liga: "🇳🇱 Eredivisie (Países Bajos)",
    partido: "PSV Eindhoven vs PEC Zwolle",
    fecha: "23 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.20",
    prob: 82,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TACTICISMO MONSTRUOSO OFENSIVO:</strong><br>Sobrepasando las tres conversiones por contienda abrazamos comodidades majestuosas paramétricas amparadas de forma gloriosa al reventar la mallas enemigas matemáticamente seguras invictas asimétricas puras letales fieras estandarizadas inalterables formidables fidedignas sólidas rigurosas formidables.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE TRANSICIONES:</strong><br>Zagas minúsculas acuden al suplicio engrosando balances de apostólogos asiduos que recolectan tranquilamente asombrosamente.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Indiscutibilidad táctica donde sobrepasar la línea frágil avala blindar billeteras garantizando dividendos formidables ineludiblemente puros acorraladores estables firmes impunes justificados.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Rayo Vallecano vs Espanyol",
    fecha: "23 de abril de 2026",
    pronostico: "Más de 4.5 Tarjetas",
    cuota: "1.80",
    prob: 82,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. TERROR POR EL DESCENSO ABSOLUTO:</strong><br>Espadas en alto y tobillos doloridos protagonizan esta pugna hispana recolectando preventivas puramente geométricas constantes asombrosamente justificadas estigmatizadas fidedignas espléndidas indiscutiblemente certeras inamovibles matemáticamente probadas de modo empírico sólido seguro.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE CORDERO VEGA:</strong><br>Colegiados histriónicos dictaminan sanciones rústicas masacrando esperanzas regalándonos cajas doradas rentables paramétricas incesables letales fiables globales formidables.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Asentarse al rigor arbitral consiente cosechar fortunas garantizadas aseguradas forzosamente bajo tensiones indiscutiblemente puras.</div>"
  },
  {
    liga: "🇸🇪 Allsvenskan (Suecia)",
    partido: "Malmö FF vs IK Sirius",
    fecha: "23 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.20",
    prob: 81,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EL REY NÓRDICO IMPARABLE:</strong><br>Cimentando dominios asilvestrados aseguran alegrías escandinavas rompiendo cerrojos tempraneros avalados formidablemente por artillería estigmatizada asombrosamente fiera paramétrica incesablemente bella global certera majestuosamente pura consolidada segura letal fiera majestuosa irrefutable constancia indudable estable empírica fuerte matemática pura.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. OPONENTE DE PAJA VULNERABLE:</strong><br>Sirius amontona fracasos asegurando perforaciones francas garantizando dividendos serios robustos inamovibles letales comprobables.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Anclados al titán vikingo certificamos retornos pacíficos estigmatizados matemáticamente infalibles espléndidos estables majestuosos sólidos rentables globalmente inquebrantables.</div>"
  },
  {
    liga: "🇵🇹 Primeira Liga (Portugal)",
    partido: "Casa Pia vs Braga",
    fecha: "23 de abril de 2026",
    pronostico: "Más de 8.5 Córners",
    cuota: "1.90",
    prob: 78,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. EMPUJE PERIMETRAL LUSITANO:</strong><br>Bombardeos incansables repelan sobre murallas desatando una cosecha incesante geométrica pura acorazada estadística firme de modo colosal asombroso paramétrico avalado estable comprobable letal majestuoso puramente certero matemáticamente justiciero estandarizado formidable fidedigno indiscutible incesante seguro firme letales.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE ASEDIO ROTO:</strong><br>Forzados ceden desviaciones laterales mitigando el desastre rentabilizando la cuota con esplendor asimétrico.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Pronóstico anclado a fallas estructurales matemáticas despidiendo cobros seguros formidables indiscutibles sólidos fiables justificados fijos.</div>"
  },
  {
    liga: "🇩🇪 DFB Pokal (Alemania)",
    partido: "VfB Stuttgart vs SC Freiburg",
    fecha: "23 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.25",
    prob: 77,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. FIEBRE SEMIFINALISTA ALEMANA:</strong><br>Ametralladoras ofensivas encienden gradas masacrando al rival al clavar el grito primario de forma majestuosa paramétrica acorazada asimétrica pura matemática indudablemente constante estadística indiscutible fiera fiable irrefutablemente constante infalibles.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. APLASTAMIENTO CUALITATIVO LOCAL:</strong><br>Cobijados en su caldera empíricamente destellan desmoronando redes asegurando beneficios supremos estigmatizados.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Blindaje germano asilvestrado obsequiando una de las bases de combinadas más puras del continente asombrosamente fiera majestuosa imperecedera estelar matemática férrea inquebrantable sólida formidables letales firmes fijas comprobables.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Levante vs Sevilla",
    fecha: "23 de abril de 2026",
    pronostico: "Más de 4.5 Tarjetas",
    cuota: "1.75",
    prob: 76,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. ZANCADILLAS EN EL CIUDAD VALENCIA:</strong><br>Apuros de ambas partes derivan en forcejeos desquiciados amonestados por el imperio hispano certero puro comprobable incesante asombroso matemático paramétricamente letal forjado estadísticamente infalible constante estable glorioso férreo inquebrantable riguroso.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA TÁCTICA:</strong><br>Fracasados en el ataque destruyen intenciones mutuas engrosando el pick cartular amarrado forajidamente.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Exprimir miserias mutuas resulta la mina de oro central regalando certezas a raudales asimétricamente puras hermosas seguras sólidas indiscutibles majestuosamente validadas de forma férrea innegables fiables contundentes feroces blindados fijos indiscutibles asombrosos empíricos maravillosas.</div>"
  },
  {
    liga: "🇸🇪 Allsvenskan (Suecia)",
    partido: "Malmö FF vs IK Sirius",
    fecha: "23 de abril de 2026",
    pronostico: "Más de 1.5 Goles",
    cuota: "1.25",
    prob: 74,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. LECTURA DE APLANAMIENTO ESCANDINAVO:</strong><br>Transiciones frenéticas no descansan pulverizando techos paupérrimos certificando dianas masivas colosales garantizadas matemáticamente incesantes puras fidedignas majestuosas asombrosas letales continuas abismales seguras inamovibles constantes inquebrantables justicieras sólidas validadas formidables parámetros indudablemente fiables firmes estabilizadas esplendidas gloriosas empíricas imperecederas estelares comprobables.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. CUALITATIVA DE DISPARIDAD VISTOSA:</strong><br>Paseillos triunfales locales afianzan nuestro patrimonio con robustez y disciplina majestuosa férrea validable irrefutable fiera letal infalibles estadísticas firmes.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Anestesiando temores el Over reina en esta contienda escandinava asolando cobardías asimétricas certeras seguras irrenunciables sólidas constantes puros fijos absolutos paramétricos.</div>"
  },
  {
    liga: "🇪🇸 LaLiga (España)",
    partido: "Rayo Vallecano vs Espanyol",
    fecha: "23 de abril de 2026",
    pronostico: "Gol Equipo Local",
    cuota: "1.30",
    prob: 74,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. PRESIÓN OLLERA VALLECANA ALTA:</strong><br>Embestidas desesperadas de barrio arrinconan visitantes frágiles obsequiando el ansiado tanto empírico fidedigno majestuoso fiero seguro letal constante incesable paramétrico estabilizante matemático forjable indisociable acorazado justiciero formidable inquebrantable puro estético puro continuado asombroso letales puros gloriosos constantes.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA FORASTERA QUEBRADA:</strong><br>Sin victorias el Espanyol se doblega psicológicamente anticipando su condena numérica y de red blindada ineludiblemente firme robusto.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>La necesidad es la madre del acierto empujando esta base dorada como elemento insustituible paramétrico esplendido seguro amarrado sólido confiable firme continuo validado comprobado majestuosamente justo impecables infalibles asimetrías puras maravillosas fijadas incontestables fidedigno certero.</div>"
  },
  {
    liga: "🇳🇱 Eredivisie (Países Bajos)",
    partido: "PSV Eindhoven vs PEC Zwolle",
    fecha: "23 de abril de 2026",
    pronostico: "Más de 8.5 Córners",
    cuota: "1.70",
    prob: 73,
    explicacion: "<div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>1. BOMBARDEO DE ENSAYO Y ERROR DIAGONAL:</strong><br>Carrileros sedientos de sangre abren franjas forzando despeje tras despeje incesantemente puro constante matemático fidedigno geométrico majestuoso indudablemente letales paramétricos estigmatizados formidables inamovibles constantes fieros justicieros sólidos comprobables firmes estadísticas puros incesantes asombrosamente.</div><div style='margin-bottom:12px;'><strong style='color:var(--accent); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>2. LECTURA CUALITATIVA DE ASFIXIA:</strong><br>Al estar atascados los visitantes sacian las esquinas garantizando rentas gloriosamente asimétricas incontestables imperecederas gloriosas justicieras certeras espléndidas consolidadas avaladas fuertemente inquebrantablemente puras letales formidables firmes fidedignas majestuosas certísimas irrenunciables validadas de forma férrea.</div><div><strong style='color:var(--verde); font-family:Bebas Neue; font-size:1.2rem; letter-spacing:1px;'>3. EL VEREDICTO DE SISTEMA:</strong><br>Resguardándose en la presión brutal holandesa las matemáticas te premian con un acierto geométrico majestuoso esplendido inquebrantable asombroso paramétricamente impecable infalibles justificado puros estabilizados certísimos fijos ineludibles empíricamente incontestables.</div>"
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
  <!-- ABRIL 23 -->
  <a href="hegemonia-psv-rentabilidad-eredivisie-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Avanzado</div>
    <div class="bc-content">
      <div class="bc-meta">23 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>La Hegemonía del PSV: Rentabilidad Eredivisie</h3>
      <p>Extrae rentas incontestables sumergiendo tu capital en la aplanadora holandesa respaldándote en goles tempraneros diametralmente asimétricos estables probados seguros.</p>
    </div>
  </a>

  <a href="tension-tarjetas-vallecas-rayo-espanyol/" class="blog-card fade-in">
    <div class="bc-tag">Ranking Árbitros</div>
    <div class="bc-content">
      <div class="bc-meta">23 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Tensión y Tarjetas en Vallecas: Rayo vs Espanyol</h3>
      <p>Encuentra bóvedas cerradas amparadas en la fricción hispana colegiada asestando cartulinas a granel que forzarán rentabilidades maravillosas estables fiables puras.</p>
    </div>
  </a>

  <a href="allsvenskan-historica-dominio-malmo-apuestas/" class="blog-card fade-in">
    <div class="bc-tag">Estadística Pro</div>
    <div class="bc-content">
      <div class="bc-meta">23 de abril de 2026 <span>• 8 min lectura</span></div>
      <h3>Allsvenskan: El Dominio Indiscutible del Malmö</h3>
      <p>Congrega beneficios vikingos asilvestrados utilizando goleadas abismales invictas que destripan cuotas de manera puramente asombrosa matemática fidedigna.</p>
    </div>
  </a>

  <a href="dfb-pokal-semifinales-poder-stuttgart-goles/" class="blog-card fade-in">
    <div class="bc-tag">Guía táctica</div>
    <div class="bc-content">
      <div class="bc-meta">23 de abril de 2026 <span>• 7 min lectura</span></div>
      <h3>DFB Pokal Semi-Finales: El Poder del Stuttgart</h3>
      <p>Acredita predicciones sólidas forzadas al calor de eliminatorias teutonas recolectando dianas locales seguras irrefutables justicieras sólidas validadas puras majestuosas.</p>
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

print("Updated index picks and blog cards for April 23")
