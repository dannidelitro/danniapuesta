import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "LaLiga 2 (ESP)", partido: "CD Leganés vs CD Mirandés", fecha: "31 Mayo", pronostico: "Ambos Marcan (Sí)", cuota: "1.85", prob: "63%", explicacion: "Mirandés está obligado a ganar para no descender y Leganés atraviesa una severa crisis defensiva." },
  { liga: "LaLiga 2 (ESP)", partido: "UD Almería vs Real Valladolid", fecha: "31 Mayo", pronostico: "Más de 1.5 Goles", cuota: "1.25", prob: "90%", explicacion: "El Almería de Arribas destroza defensas frágiles como la del Valladolid de visitante." },
  { liga: "LaLiga 2 (ESP)", partido: "CD Castellón vs SD Eibar", fecha: "31 Mayo", pronostico: "Más de 5.5 Tarjetas", cuota: "1.65", prob: "72%", explicacion: "Lucha a muerte por el play-off. Ambos equipos promedian altos índices de faltas tácticas." },
  { liga: "Série A (BRA)", partido: "Palmeiras vs Chapecoense", fecha: "31 Mayo", pronostico: "Palmeiras Hándicap -1.5", cuota: "1.70", prob: "80%", explicacion: "Asimetría total. Palmeiras arrasa en el Allianz Parque ante un colista que concede 2 goles por partido." },
  { liga: "Liga 1 (PER)", partido: "Cienciano vs Sporting Cristal", fecha: "31 Mayo", pronostico: "Cienciano o Empate (1X)", cuota: "1.45", prob: "75%", explicacion: "Factor altitud (3,400m en Cusco) brutal contra un Cristal mermado por las lesiones de figuras clave." },
  { liga: "LigaPro (ECU)", partido: "IDV vs Guayaquil City", fecha: "31 Mayo", pronostico: "Gana IDV a Cero (No BTTS)", cuota: "1.66", prob: "60%", explicacion: "Independiente del Valle lleva 9 partidos consecutivos con la valla invicta frente a este rival." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for May 31.")
