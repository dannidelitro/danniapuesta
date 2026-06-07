import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "K League 2 (COR)", partido: "Seoul E-Land vs Cheongju", fecha: "7 Junio", pronostico: "Local o Empate (1X)", cuota: "1.25", prob: "90%", explicacion: "Seoul es fortísimo en casa frente a un Cheongju que empata el 76.9% de sus duelos." },
  { liga: "K League 2 (COR)", partido: "Gimpo FC vs Jeonnam", fecha: "7 Junio", pronostico: "Local Anota (Más 0.5)", cuota: "1.20", prob: "88%", explicacion: "Jeonnam es incapaz de dejar su portería a cero en el 92.3% de los partidos." },
  { liga: "Allsvenskan (SUE)", partido: "Häcken vs Djurgårdens", fecha: "7 Junio", pronostico: "Ambos Marcan (SÍ)", cuota: "1.45", prob: "88%", explicacion: "Choque ultra-ofensivo; ambos equipos conceden promedios superiores a 1.45 goles." },
  { liga: "Série B (BRA)", partido: "CRB vs São Bernardo", fecha: "7 Junio", pronostico: "Local o Empate (1X)", cuota: "1.30", prob: "81%", explicacion: "CRB promedia 1.80 goles en casa. Fuerte influencia de la localía en el Rei Pelé." },
  { liga: "CPL (CAN)", partido: "Inter Toronto vs Forge FC", fecha: "7 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.35", prob: "80%", explicacion: "Derbi canadiense de alto flujo; ambos superan la media ofensiva de 1 gol por partido." },
  { liga: "Primera Div (URU)", partido: "Cerro vs Peñarol", fecha: "7 Junio", pronostico: "Visita Anota (Más 0.5)", cuota: "1.18", prob: "77%", explicacion: "Brecha enorme de calidad; la jerarquía ofensiva de Peñarol romperá el cerrojo de Cerro." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 7.")
