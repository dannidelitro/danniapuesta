import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Série B (BRA)", partido: "Vila Nova vs Náutico", fecha: "20 Junio", pronostico: "1X (Local o Empate)", cuota: "1.25", prob: "89%", explicacion: "Vila Nova llega con gran inercia ganadora en casa; Náutico sufre una tasa de derrota del 50% de visitante." },
  { liga: "USL Champ (USA)", partido: "Monterey Bay vs El Paso", fecha: "20 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.30", prob: "88%", explicacion: "El Paso promedia 1.92 goles a favor de visita; Monterey encaja 1.73 en casa. El modelo proyecta alto marcador." },
  { liga: "Série B (BRA)", partido: "Ceará SC vs Botafogo SP", fecha: "20 Junio", pronostico: "1X (Local o Empate)", cuota: "1.22", prob: "84%", explicacion: "Ceará anota en el 80% de sus compromisos como local; Botafogo SP muestra serios problemas defensivos a domicilio." },
  { liga: "USL Champ (USA)", partido: "Monterey Bay vs El Paso", fecha: "20 Junio", pronostico: "Visita +0.5 Goles", cuota: "1.28", prob: "82%", explicacion: "Consistencia ofensiva abrumadora de El Paso frente a una de las peores tasas de portería a cero de la liga local." },
  { liga: "Série B (BRA)", partido: "Londrina vs Athletic Club", fecha: "20 Junio", pronostico: "X2 (Visita o Empate)", cuota: "1.38", prob: "80%", explicacion: "Athletic Club es sólido y casi invencible esta temporada; Londrina es colista crónico con gravísimas deficiencias." },
  { liga: "USL Champ (USA)", partido: "Monterey Bay vs El Paso", fecha: "20 Junio", pronostico: "Más de 2.5 Goles", cuota: "1.65", prob: "76%", explicacion: "Las transiciones rápidas y la debilidad del bloque bajo proyectan un escenario propicio para el over total." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 20.")
