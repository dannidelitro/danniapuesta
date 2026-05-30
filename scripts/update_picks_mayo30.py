import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "UEFA Champions League", partido: "Paris Saint-Germain vs Arsenal FC", fecha: "30 Mayo", pronostico: "Gana PSG", cuota: "2.30", prob: "43%", explicacion: "La final de Budapest. Ligero favoritismo parisino debido a su mayor frescura física y experiencia en estas instancias." },
  { liga: "Série A (BRA)", partido: "Bahia vs Botafogo RJ", fecha: "30 Mayo", pronostico: "Más de 2.5 Goles", cuota: "1.75", prob: "78%", explicacion: "Altísima expectativa de goles (Poisson lambda = 3.4). El modelo proyecta un duelo ofensivo y vistoso." },
  { liga: "LaLiga 2 (ESP)", partido: "Granada CF vs Sporting Gijón", fecha: "30 Mayo", pronostico: "Gana Granada", cuota: "1.72", prob: "58%", explicacion: "Los modelos otorgan 58% de probabilidad de victoria al local amparado en la presión del Estadio Nuevo Los Cármenes." },
  { liga: "LaLiga 2 (ESP)", partido: "Granada CF vs Sporting Gijón", fecha: "30 Mayo", pronostico: "Ambos Marcan (Sí)", cuota: "1.78", prob: "56%", explicacion: "Sporting llega encadenando victorias y promediando altos tiros a puerta, estimando un BTTS fuerte." },
  { liga: "Série A (BRA)", partido: "Grêmio vs Corinthians", fecha: "30 Mayo", pronostico: "Menos de 2.5 Goles", cuota: "1.55", prob: "75%", explicacion: "Duelo de altísima tensión táctica. Ambos equipos cuentan con arqueros top en porterías a cero." },
  { liga: "Amistosos FIFA", partido: "Escocia vs Curaçao", fecha: "30 Mayo", pronostico: "Gana Escocia y +1.5 Goles", cuota: "1.35", prob: "86%", explicacion: "Favoritismo absoluto (cuota 1.16) para Escocia ante un rival caribeño inferior tácticamente." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for May 30.")
