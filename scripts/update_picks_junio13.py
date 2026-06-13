import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "USL (USA)", partido: "Tampa Bay vs Hartford", fecha: "13 Junio", pronostico: "Local o Empate (1X)", cuota: "1.20", prob: "93%", explicacion: "Tampa Bay está invicto en casa (8 victorias); Hartford no funciona de visita." },
  { liga: "USL (USA)", partido: "Charleston vs FC Tulsa", fecha: "13 Junio", pronostico: "Local o Empate (1X)", cuota: "1.22", prob: "91%", explicacion: "Charleston domina la posesión; Tulsa tiene la peor precisión de pases (73%)." },
  { liga: "Primera Div (CHI)", partido: "Colo-Colo vs Cobresal", fecha: "13 Junio", pronostico: "Local o Empate (1X)", cuota: "1.18", prob: "90%", explicacion: "Colo-Colo anula en el llano de Santiago a un Cobresal que depende de la altura." },
  { liga: "USL (USA)", partido: "Louisville vs Brooklyn FC", fecha: "13 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.25", prob: "88%", explicacion: "Equipos hiper-ofensivos y frágiles; ambos promedian más de 1.5 goles a favor y en contra." },
  { liga: "Primera Nac (ARG)", partido: "Defensores vs Colón", fecha: "13 Junio", pronostico: "Menos de 2.5 Goles", cuota: "1.45", prob: "84%", explicacion: "Extrema fricción; Defensores promedia 0.63 goles y los H2H recientes son muy bajos." },
  { liga: "Veikkausliiga (FIN)", partido: "Inter Turku vs AC Oulu", fecha: "13 Junio", pronostico: "Más de 8.5 Corners", cuota: "1.55", prob: "82%", explicacion: "Transiciones rápidas escandinavas por bandas disparan los despejes de Oulu." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 13.")
