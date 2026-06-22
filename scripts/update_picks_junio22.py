import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Besta deildin (ISL)", partido: "KR Reykjavik vs IA Akranes", fecha: "22 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.18", prob: "94%", explicacion: "KR Reykjavik promedia 3.45 goles a favor y 2.27 en contra. El 100% de sus partidos superó esta línea." },
  { liga: "Virsliga (LVA)", partido: "RFS vs Ogre United", fecha: "22 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.15", prob: "93%", explicacion: "Enorme asimetría. El líder promedia más de 2.3 goles ante una de las peores defensas del campeonato." },
  { liga: "Premier Div (IRL)", partido: "Shamrock Rovers vs Derry City", fecha: "22 Junio", pronostico: "1X (Local o Empate)", cuota: "1.25", prob: "88%", explicacion: "Shamrock Rovers registra un 90% de imbatibilidad en su estadio. Derry City sufre mucho jugando a domicilio." },
  { liga: "Superettan (SUE)", partido: "IK Oddevold vs Ljungskile SK", fecha: "22 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.22", prob: "88%", explicacion: "Los juegos de Oddevold promedian 3.50 goles totales; Ljungskile recibe gran volumen de anotaciones fuera." },
  { liga: "A Lyga (LTU)", partido: "FK Riteriai vs FC Hegelmann", fecha: "22 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.28", prob: "82%", explicacion: "Choque con alta dinámica ofensiva contrastada que supera las proyecciones más conservadoras de la liga." },
  { liga: "Premier Div (IRL)", partido: "Shamrock Rovers vs Derry City", fecha: "22 Junio", pronostico: "Más de 8.5 Córneres", cuota: "1.45", prob: "82%", explicacion: "Ritmo vertiginoso por las bandas. Ambos equipos generan un promedio combinado de 10.9 córneres por partido." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 22.")
