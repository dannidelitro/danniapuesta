import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Premier Div (IRL)", partido: "Shamrock Rovers vs Galway Utd", fecha: "26 Junio", pronostico: "1X (Local o Empate)", cuota: "1.15", prob: "94%", explicacion: "Shamrock ostenta un 73% de victorias en casa. Galway, de visitante, reduce su posesión y ha encajado en el 100% de sus salidas." },
  { liga: "Premier Div (IRL)", partido: "Derry City vs Drogheda Utd", fecha: "26 Junio", pronostico: "Más de 0.5 Goles Local", cuota: "1.12", prob: "92%", explicacion: "Derry City genera 1.85 xG en casa y se enfrenta a la peor defensa a domicilio, que promedia 2.20 goles recibidos." },
  { liga: "First Div (IRL)", partido: "Cork City vs Bray Wanderers", fecha: "26 Junio", pronostico: "1X (Local o Empate)", cuota: "1.16", prob: "91%", explicacion: "Cork ejerce un monopolio de puntos absoluto en la división y su muro defensivo apenas ha concedido 11 goles en el año." },
  { liga: "Premier Div (IRL)", partido: "Dundalk vs Waterford", fecha: "26 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.25", prob: "88%", explicacion: "Necesidad urgente de sumar de los locales contra un Waterford con una fortísima inercia ofensiva fuera de casa." },
  { liga: "Virsliga (LVA)", partido: "FK Liepaja vs RFS Riga", fecha: "26 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.22", prob: "87%", explicacion: "RFS promedia 2.58 goles a favor. Liepaja renace en casa con 4 victorias al hilo y múltiples anotaciones por partido." },
  { liga: "Premier Div (IRL)", partido: "Shamrock Rovers vs Galway Utd", fecha: "26 Junio", pronostico: "Menos de 10.5 Corners", cuota: "1.35", prob: "83%", explicacion: "Shamrock promedia solo 8.65 córners por encuentro, siendo uno de los equipos que menos saques de esquina genera y concede." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 26.")
