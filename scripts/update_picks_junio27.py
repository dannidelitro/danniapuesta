import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Veikkausliiga (FIN)", partido: "IF Gnistan vs VPS", fecha: "27 Junio", pronostico: "Más de 8.5 Corners", cuota: "1.18", prob: "95%", explicacion: "Extrema paridad, juego de desborde lateral continuo. La proyección estructural apunta a superar esta línea con comodidad absoluta." },
  { liga: "Superettan (SUE)", partido: "United Nordic vs Oddevold", fecha: "27 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.25", prob: "88%", explicacion: "Ambos clubes promedian en torno a 2 goles por partido, presentando altas carencias defensivas e inercia ofensiva cruzada." },
  { liga: "Série B (BRA)", partido: "Criciúma vs São Bernardo", fecha: "27 Junio", pronostico: "Más de 3.5 Tarjetas", cuota: "1.30", prob: "86%", explicacion: "São Bernardo es extremadamente brusco. Además, el árbitro Bruno Arleu promedia la brutalidad de 6.44 amarillas por encuentro." },
  { liga: "Veikkausliiga (FIN)", partido: "IF Gnistan vs VPS", fecha: "27 Junio", pronostico: "Más de 3.5 Tarjetas", cuota: "1.35", prob: "84%", explicacion: "Duelo directo en la parte alta de la tabla; la fricción para la recuperación en bloque medio garantiza abundantes faltas tácticas." },
  { liga: "Série B (BRA)", partido: "Criciúma vs São Bernardo", fecha: "27 Junio", pronostico: "1X (Local o Empate)", cuota: "1.22", prob: "82%", explicacion: "Criciúma se mantiene imbatido de local (3 victorias, 2 empates) frente a un São Bernardo que muestra irregularidad crónica de visita." },
  { liga: "Premier Div (IRL)", partido: "Sligo Rovers vs Shelbourne", fecha: "27 Junio", pronostico: "Menos de 2.5 Goles", cuota: "1.45", prob: "80%", explicacion: "Sligo sufre bajas críticas en la creación y no anota hace 3 juegos; Shelbourne no cuenta con su máximo goleador Sean Boyd." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 27.")
