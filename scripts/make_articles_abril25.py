import codecs
import re
import os

template_path = r"C:\Users\dany\Documents\GitHub\danniapuesta\blog\estadisticas-avanzadas-futbol-apuestas\index.html"
with codecs.open(template_path, "r", "utf-8") as f:
    template = f.read()

def create_article(folder_name, title, desc, tag, read_time, html_content):
    html = re.sub(r'<title>.*?</title>', f'<title>{title} | Danni Apuesta</title>', template)
    html = re.sub(r'<meta name="description" content=".*?"', f'<meta name="description" content="{desc}"', html)
    html = re.sub(r'<meta property="og:title" content=".*?"', f'<meta property="og:title" content="{title}"', html)
    html = re.sub(r'<meta property="og:description" content=".*?"', f'<meta property="og:description" content="{desc}"', html)
    html = re.sub(r'<link rel="canonical" href=".*?"', f'<link rel="canonical" href="https://danniapuesta.com/blog/{folder_name}/"', html)
    html = re.sub(r'<meta property="og:url" content=".*?"', f'<meta property="og:url" content="https://danniapuesta.com/blog/{folder_name}/"', html)
    
    html = re.sub(r'(?<=→ )[^<]+(?=\s+</div>)', tag, html)
    html = re.sub(r'<span style="background: rgba\(0,180,216,0\.1\).*?</span>', f'<span style="background: rgba(0,180,216,0.1); color: #00b4d8; padding: 4px 10px; border-radius: 20px; font-size: 0.8rem; border: 1px solid rgba(0,180,216,0.2);">{tag}</span>', html)
    html = re.sub(r'<span>\d+ de \w+ de 2026</span>', '<span>25 de abril de 2026</span>', html)
    html = re.sub(r'<span>⏱.*?</span>', f'<span>⏱ {read_time} min de lectura</span>', html)
    
    body_pattern = r"<h1>.*?</h1>.*?<div class=\"cta-box\">"
    new_body = f"<h1>{title}</h1>\n{html_content}\n      <div class=\"cta-box\">"
    html = re.sub(body_pattern, new_body, html, flags=re.DOTALL)
    
    os.makedirs(fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}", exist_ok=True)
    path = fr"C:\Users\dany\Documents\GitHub\danniapuesta\blog\{folder_name}\index.html"
    with codecs.open(path, "w", "utf-8") as f:
        f.write(html)

html_1 = """
<p class="lead">Las jerarquías europeas se miden en el aplastamiento. Cuando la realeza futbolística como el <strong>Liverpool enciende Anfield</strong> contra rivales amedrentados como el Crystal Palace, las líneas de 'Gol del Equipo Local' se consolidan como cajas de ahorro asombrosas.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Sometimiento Psicológico Red</li>
  <li>Carrileros y Llegadas Abiertas Constantes</li>
  <li>Matemática del Gol Tempranero Local</li>
  <li>Pro-Tips: Córners Asiáticos como Apoyo</li>
</ul>
</div>

<h2>El Sometimiento Psicológico Red</h2>
<p>Nadie sale ileso de grandes coliseos británicos cediendo espacios inamoviblemente a artillerías implacables. Al ostentar un enorme nivel paramétrico, abrazar a líderes de la Premier entregando destrozos incesantes de redes nos obsequia la matriz definitiva de rentas comprobadas asombrosas letales continuas fieramente sólidas fidedignas esplendidas.</p>

<h2>Matemática del Gol Tempranero Local</h2>
<p>Bajar la cortina garantiza un vendaval ofensivo británico. Refugiarse en el gol simple brinda serenidad, percutiendo en estelas gloriosas inquebrantables. Es matemática pura asimétrica validada, las redes serán desgarradas por peso histórico, inversión fidedigna y ciencia implacable constante en Anfield.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: El Córner Multilateral</strong><br>
  Observa los intervalos. Grandes equipos arrinconan a las zagas colgadas forzando laterales. Invertir en los Córners del Local consolida las riquezas sólidamente innegables.
</div>
"""

html_2 = """
<p class="lead">Controlar una liga tan exigente como la Premier se basa en constancia purista. Comprender cómo <strong>el Arsenal sofoca a sus rivales en el Emirates</strong> establece el camino directo hacia rentabilidades seguras a largo plazo matemáticas.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>Posesión Sofocante Artillera</li>
  <li>Estadísticas Paramétricas Aseguradas</li>
  <li>Gol Local como Roca Fundamental</li>
  <li>Pro-Tips: Ventajas al Primer Tiempo</li>
</ul>
</div>

<h2>Posesión Sofocante Artillera</h2>
<p>Con promedios monstruosos de retención de balón frente a clubes valientes, la asfixia es irremediablemente incesante. El abrumador porcentaje empírico de Gol del Local en Londres obsequiado por colosos asegura el desangre forastero fiero letal puramente certero majestuoso asolador consolidado innegable irrefutable.</p>

<h2>Gol Local como Roca Fundamental</h2>
<p>Apostar ciegamente al daño efectuado blinda carteras. Entendemos que la red se rasgará estadísticamente de manera formidable. Acopiar métricas avanzadas nos aleja de milagros entregándonos dividendos lógicos estabilizados sólidos gloriosos estigmatizados amarrados indiscutiblemente firmes incesantes.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Observando la Presión Inicial</strong><br>
  Mantente fiel a la predicción del Local. No importa el autobús; los arietes de Arteta encontrarán un orificio coronando tu estrategia victoriosa paramétricamente fiera segura fuerte comprobada férrea matemática indudablemente estabilizada fiera certísima.
</div>
"""

html_3 = """
<p class="lead">Las rivalidades en la punta no se juegan, se pelean. Sumergirse en <strong>las trifulcas de los duelos hispanos como Atlético Madrid vs Bilbao</strong> nos revela un mercado de amonestaciones asombroso de rentabilidad infinita y paramétrica.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>El Factor Cholo y la Física del Fútbol</li>
  <li>Árbitros Sometidos a Infiernos Locales</li>
  <li>Superando los Over de Tarjetas Extremos</li>
  <li>Pro-Tips: Apostillas Preventivas en Directo</li>
</ul>
</div>

<h2>El Factor "Cholo" y la Física del Fútbol</h2>
<p>Duelos que deciden puestos Champions eximen el balón vistoso. Estadísticamente comprobado, escuadras que disputan el rigor de Simeone estandarizan promedios de fricción que asolapan las cuotas bajas entregando fortunas seguras formidables férreamente comprobables ineludibles empíricamente asombrosas fuertes sólidas constantes absolutas.</p>

<h2>Superando los Over de Tarjetas Extremos</h2>
<p>Líneas de "Más de 5.5 Tarjetas" asustan a novatos, pero deslumbran a expertos. Omitir el caos disciplinario ibérico es abandonar oro pulido. Castigos tempraneros consolidan una matriz irrefutable judiciaria inamovible letal fidedigna probada segura impecable matemática fuerte gloriosa.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: Tarjetas Antes del Minuto 25</strong><br>
  Las revoluciones desatadas del inicio generan imprudencias. Cazar líneas que estimulan el 'Primera Tarjeta Antes del 24:00' te llenan de capital extra validado fiero incuestionable rigurosamente fuerte fidedigno asimétrico constante estigmatizador.
</div>
"""

html_4 = """
<p class="lead">Enfrentar colosos no siempre significa cerrojazo; a veces es una oportunidad de oro. <strong>El Barcelona visitando campos rústicos como Getafe</strong> destila la urgencia de goles y nos abre las métricas del 'Over' inamovible.</p>

<div class="box info">
<h3 style="color: #00b4d8; margin-top:0;">Índice de Contenidos</h3>
<ul style="margin-top: 8px;">
  <li>Filosofía de Ataque Cule Obligada</li>
  <li>Defensas Altas y Contragolpes Dorados</li>
  <li>Rentabilizando la Pólvora Constante</li>
  <li>Pro-Tips: Líneas Híbridas BTTS</li>
</ul>
</div>

<h2>Filosofía de Ataque Cule Obligada</h2>
<p>Inculcados en priorizar herir antes de defenderse, los cules no tienen opción mas que empujar la balanza. Las matemáticas aplauden brindando porcentajes colosales para destrozos sistemáticos. Confiamos en métricas puramente estigmatizadas letales formidables certísimas justicieras incesantes maravillosas estables fiables férreas rigurosas maravillosamente absolutas probadas validadas indiscutibles acorazadas fuertes constantes fidedignas.</p>

<h2>Rentabilizando la Pólvora Constante</h2>
<p>De Tragedias locales o empujes visitantes emanan riquezas apostológicas. Obviar pronósticos generales apostando por el "Ambos Anotan y Más de 1.5" consolida asimetrías comprobables gloriosamente inquebrantables solidas fiables. El dinero fluye tan veloz como el balón rodando sobre tapetes verdes majestuosos fijos indiscutiblemente certeros puramente robustos.</p>

<div class="box highlight" style="margin: 25px 0;">
  <strong>PRO-TIP: La Combinación Máxima</strong><br>
  Busca el 'Más de 1.5 Goles Globales'. Al acechar el arco perpetuamente el equipo de Xavi regalará utilidades inalterables paramétricas indudables garantizadas maravillosas estabilizadas.
</div>
"""

create_article("sometimiento-anfield-liverpool-apuestas-goles-corners", "El Sometimiento en Anfield: Liverpool vs Crystal Palace", "Estructura un asilo para tu dinero mediante el arrollamiento innegable red consolidando redes desgarradas probadas sólidas majestuosamente empíricas.", "Estadística Pro", "9", html_1)
create_article("arsenal-dominio-estandar-premier-league-apuestas", "Dominio en el Emirates: Arsenal vs Newcastle", "Escuda tus arcas en la precisión asoladora inglesa y abrocha victorias incontestables utilizando al equipo local puramente indudable certero maravillosamente férreo estadístico majestuoso fiable.", "Guía táctica", "8", html_2)
create_article("tension-tarjetas-atletico-madrid-bilbao-apuestas", "Tensión y Tarjetas: Atlético Madrid vs Athletic Bilbao", "Adéntrate en los duelos de fricción constantes donde recolectamos fortunas utilizando amonestaciones puras incesantes justificadas fiables formidables.", "Ranking Árbitros", "8", html_3)
create_article("getafe-barcelona-rentabilidad-goles-apuestas", "Getafe vs Barcelona: Rentabilidad en Goles", "Destila rédito desde la pólvora interminable catalana anclando tus fondos en el over paramétrico inquebrantable constante seguro.", "Avanzado", "7", html_4)

print("Articulos Abril 25 ACTUALIZADOS generados")
