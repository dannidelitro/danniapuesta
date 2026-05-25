import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Allsvenskan", partido: "IFK Göteborg vs Mjällby AIF", fecha: "25 Mayo", pronostico: "Mjällby o Empate (X2)", cuota: "1.30", prob: "82%", explicacion: "Hegemonía táctica del Mjällby (3 victorias directas). Göteborg acumula 11 juegos encajando goles." },
  { liga: "Premier Division", partido: "Derry City vs Shelbourne", fecha: "25 Mayo", pronostico: "Derry City o Empate (1X)", cuota: "1.25", prob: "80%", explicacion: "El modelo Dixon-Coles proyecta un partido cerrado. Derry encadena 4 empates en casa con solidez." },
  { liga: "Allsvenskan", partido: "IF Elfsborg vs BK Häcken", fecha: "25 Mayo", pronostico: "Ambos Marcan (BTTS)", cuota: "1.57", prob: "78%", explicacion: "Häcken promedia 2 goles a favor por juego, y Elfsborg 2.57 en casa. Duelo directo por Europa." },
  { liga: "Eliteserien", partido: "Sarpsborg 08 vs Molde FK", fecha: "25 Mayo", pronostico: "Ambos Marcan (BTTS)", cuota: "1.44", prob: "78%", explicacion: "Nula solidez defensiva del Sarpsborg (encaja en el 100% de localías) ante la potente ofensiva del Molde." },
  { liga: "Allsvenskan", partido: "IF Elfsborg vs BK Häcken", fecha: "25 Mayo", pronostico: "Más de 9.5 Córners", cuota: "1.50", prob: "82%", explicacion: "Juego directo por bandas proyectado fuertemente por la IA. Ambos equipos dependen del desborde." },
  { liga: "Premier Division", partido: "Bohemians vs Shamrock Rovers", fecha: "25 Mayo", pronostico: "Ambos Marcan (BTTS)", cuota: "1.65", prob: "66%", explicacion: "Clásico irlandés de alta fricción. El historial directo potencia las transiciones de ambos conjuntos." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for May 25.")
