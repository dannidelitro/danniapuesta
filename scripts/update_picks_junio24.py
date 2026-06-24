import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "USL Champ (USA)", partido: "Charleston vs Loudoun Utd", fecha: "24 Junio", pronostico: "1X (Local o Empate)", cuota: "1.18", prob: "94%", explicacion: "Charleston está invicto en casa (2.67 pts/partido). Loudoun solo suma una victoria como visitante en la temporada." },
  { liga: "3. Divisjon (NOR)", partido: "Gamle Oslo vs Lokomotiv Oslo", fecha: "24 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.15", prob: "94%", explicacion: "Lokomotiv promedia la locura de 6.33 goles totales fuera de casa. El 100% de los juegos de Gamle de local superan la línea." },
  { liga: "Ettan Norra (SUE)", partido: "Karlbergs BK vs Piteå IF", fecha: "24 Junio", pronostico: "1X (Local o Empate)", cuota: "1.25", prob: "90%", explicacion: "El modelo local apoya fuertemente a Karlbergs frente a un Piteå hundido en la clasificación con graves fallos a domicilio." },
  { liga: "Ettan Norra (SUE)", partido: "Karlbergs BK vs Piteå IF", fecha: "24 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.22", prob: "88%", explicacion: "Piteå ostenta un historial implacable: el 96% de sus compromisos superan esta barrera por su constante laxitud defensiva." },
  { liga: "USL Champ (USA)", partido: "Charleston vs Loudoun Utd", fecha: "24 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.28", prob: "85%", explicacion: "El modelo proyecta que Charleston explotará los carriles centrales gracias a su xG de local de 1.93 frente a la frágil defensa rival." },
  { liga: "USL Champ (USA)", partido: "Colorado Springs vs San Antonio", fecha: "24 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.30", prob: "84%", explicacion: "Las métricas multifuente coinciden en una proyección de transiciones constantes que terminarán en un alto volumen de llegadas." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 24.")
