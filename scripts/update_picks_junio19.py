import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "First Division (IRL)", partido: "Cork City vs Treaty Utd", fecha: "19 Junio", pronostico: "1X (Local o Empate)", cuota: "1.15", prob: "95%", explicacion: "Cork City es un bastión inexpugnable en casa; Treaty United es incapaz de ganar como visitante." },
  { liga: "Premier Div (IRL)", partido: "St Patrick's vs Sligo R.", fecha: "19 Junio", pronostico: "1X (Local o Empate)", cuota: "1.18", prob: "93%", explicacion: "Sligo llega con bajas clave en defensa y encajando 12 goles recientes. St Patrick's domina los remates al arco." },
  { liga: "1. Division (NOR)", partido: "Ranheim vs Lyn Oslo", fecha: "19 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.25", prob: "88%", explicacion: "Ranheim promedia 2.64 goles a favor y 2.18 en contra; el modelo Poisson proyecta más de 4 goles esperados." },
  { liga: "Premier Div (IRL)", partido: "Drogheda vs Shelbourne", fecha: "19 Junio", pronostico: "Más de 4.5 Tarjetas", cuota: "1.45", prob: "86%", explicacion: "Shelbourne basa su juego defensivo en faltas tácticas constantes. El histórico directo promedia 5.84 amonestaciones." },
  { liga: "Premier Div (IRL)", partido: "Bohemians vs Dundalk", fecha: "19 Junio", pronostico: "Más de 9.5 Córneres", cuota: "1.40", prob: "85%", explicacion: "Ambos equipos abusan del juego exterior, sumando un brutal promedio combinado de más de 20 córneres por partido." },
  { liga: "Premier Div (IRL)", partido: "Bohemians vs Dundalk", fecha: "19 Junio", pronostico: "Ambos Marcan (BTTS)", cuota: "1.55", prob: "78%", explicacion: "Bohemians ejerce alta presión pero descuida el repliegue defensivo. Juego vertical que garantiza ocasiones en ambas áreas." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 19.")
