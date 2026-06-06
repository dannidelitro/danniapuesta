import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Segunda Div (CHI)", partido: "Santiago City vs Colina", fecha: "6 Junio", pronostico: "Menos de 3.5 Goles", cuota: "1.15", prob: "94%", explicacion: "Colina registra un 100% de partidos under 2.5 frente a un local rígidamente defensivo e invicto." },
  { liga: "1. Deild (ISL)", partido: "Fylkir vs Thróttur", fecha: "6 Junio", pronostico: "Local Anota (Más 0.5)", cuota: "1.20", prob: "93%", explicacion: "Fylkir promedia 2.50 goles a favor por partido local en una liga de esquema hiperofensivo." },
  { liga: "Ettan South (SUE)", partido: "Jönköpings vs Trollhättan", fecha: "6 Junio", pronostico: "Local o Empate (1X)", cuota: "1.30", prob: "86%", explicacion: "El bloque defensivo del Jönköpings es inexpugnable en casa, encajando apenas 0.60 goles por juego." },
  { liga: "Ettan North (SUE)", partido: "Gefle vs Hammarby T.", fecha: "6 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.25", prob: "88%", explicacion: "El 83% del H2H directo superó la línea. Hammarby anota 2.40 goles promedio de visita." },
  { liga: "Ettan North (SUE)", partido: "Gefle vs Hammarby T.", fecha: "6 Junio", pronostico: "Visita o Empate (X2)", cuota: "1.35", prob: "82%", explicacion: "Hammarby supera la producción de puntos de Gefle en un 174%, proyectando un dominio territorial." },
  { liga: "CPL (CAN)", partido: "Vancouver FC vs Atl. Ottawa", fecha: "6 Junio", pronostico: "Local Anota (Más 0.5)", cuota: "1.40", prob: "85%", explicacion: "Vancouver aprovechará la fragilidad extrema de Ottawa, que concede 2.20 goles de visita." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 6.")
