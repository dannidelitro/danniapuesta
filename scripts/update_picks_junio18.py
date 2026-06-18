import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Veikkausliiga (FIN)", partido: "AC Oulu vs Mariehamn", fecha: "18 Junio", pronostico: "1X (Local o Empate)", cuota: "1.25", prob: "96%", explicacion: "Oulu impecable en casa (100% victorias); Mariehamn promedia 0.20 goles y 80% derrotas de visitante." },
  { liga: "Ettan South (SUE)", partido: "Eskilsminne vs Trollhättan", fecha: "18 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.30", prob: "90%", explicacion: "Trollhättan tiene 100% de Over 1.5 a domicilio. Ambos bloques muestran enorme fragilidad defensiva." },
  { liga: "Série B (BRA)", partido: "Goiás vs Operário PR", fecha: "18 Junio", pronostico: "1X (Local o Empate)", cuota: "1.28", prob: "89%", explicacion: "Goiás concede apenas 0.60 goles en casa; Operário sufre fuerte regresión ofensiva fuera de su estadio." },
  { liga: "Botola Pro (MAR)", partido: "RSB Berkane vs Olympic Safi", fecha: "18 Junio", pronostico: "1X (Local o Empate)", cuota: "1.22", prob: "88%", explicacion: "Safi gana solo el 8% de sus juegos de visitante y concede 1.5 goles. Gran control táctico local." },
  { liga: "Veikkausliiga (FIN)", partido: "AC Oulu vs Mariehamn", fecha: "18 Junio", pronostico: "Más de 8.5 Córneres", cuota: "1.45", prob: "85%", explicacion: "Oulu presiona intensamente por bandas; Mariehamn concede 10.5 córneres de visitante bajo presión." },
  { liga: "Série B (BRA)", partido: "Goiás vs Operário PR", fecha: "18 Junio", pronostico: "Más de 4.5 Tarjetas", cuota: "1.50", prob: "84%", explicacion: "Árbitro muy estricto; choque de estilos con mucha fricción y transiciones desesperadas." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 18.")
