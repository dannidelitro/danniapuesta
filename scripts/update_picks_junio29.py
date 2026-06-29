import re
import os

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Premier League (CAN)", partido: "Cavalry vs Supra du Quebec", fecha: "29 Junio", pronostico: "1X (Local o Empate)", cuota: "1.18", prob: "95%", explicacion: "Cavalry ostenta imbatibilidad perfecta en su estadio, encajando apenas 0.50 goles. Supra muestra nula capacidad como visitante." },
  { liga: "Serie C (BRA)", partido: "Ypiranga RS vs Confianca SE", fecha: "29 Junio", pronostico: "1X (Local o Empate)", cuota: "1.20", prob: "94%", explicacion: "Confianca registra 100% de derrotas en sus últimas 5 salidas. Ypiranga consolida fortaleza con 85% de imbatibilidad local." },
  { liga: "Virsliga (LET)", partido: "Auda vs Riga FC", fecha: "29 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.15", prob: "92%", explicacion: "Riga FC posee el ataque más letal (3.10 goles/partido de visita). Las transiciones rápidas superarán la defensa local." },
  { liga: "Betri deildin (FRO)", partido: "HB Torshavn vs Skala IF", fecha: "29 Junio", pronostico: "1X (Local o Empate)", cuota: "1.15", prob: "91%", explicacion: "Torshavn domina en casa frente a un Skala IF que cede por completo la posesión y registra 75% de caídas a domicilio." },
  { liga: "Ykkösliiga (FIN)", partido: "VJS Vantaa vs TPV Tampere", fecha: "29 Junio", pronostico: "1X (Local o Empate)", cuota: "1.25", prob: "88%", explicacion: "TPV Tampere acumula 4 derrotas consecutivas fuera de casa. La motivación local estabiliza fuertemente el mercado de doble oportunidad." },
  { liga: "Besta deild (ISL)", partido: "ÍA Akranes vs Fram", fecha: "29 Junio", pronostico: "Más de 8.5 Corners", cuota: "1.32", prob: "84%", explicacion: "Ambos equipos utilizan extremos abiertos. ÍA Akranes promedia 16 remates en casa y Fram genera casi 5 corners a domicilio." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 29.")
