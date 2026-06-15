import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Superettan (SUE)", partido: "Norrköping vs Varbergs", fecha: "15 Junio", pronostico: "Doble Oportunidad (X2)", cuota: "1.80", prob: "70%", explicacion: "Varbergs lidera invicto hace 10 partidos; excelente valor en X2 visitando a un Norrköping vulnerable atrás." },
  { liga: "Superettan (SUE)", partido: "Sundsvall vs Östers IF", fecha: "15 Junio", pronostico: "Visita (Gana Östers)", cuota: "1.70", prob: "75%", explicacion: "Sundsvall sufre déficit ofensivo severo; Östers llega con racha ganadora y claro dominio táctico." },
  { liga: "Besta deild (ISL)", partido: "KA Akureyri vs Fram", fecha: "15 Junio", pronostico: "Doble Oportunidad (X2)", cuota: "1.55", prob: "68%", explicacion: "Fram promedia 2.8 goles y está invicto en sus últimos 6, la dinámica ofensiva anula la localía histórica del KA." },
  { liga: "Ykkösliiga (FIN)", partido: "SJK Akatemia vs FC Haka", fecha: "15 Junio", pronostico: "Visita (Gana Haka)", cuota: "1.57", prob: "64%", explicacion: "SJK suma 450 minutos de sequía absoluta de goles; Haka es la ofensiva más letal del torneo." },
  { liga: "Série C (BRA)", partido: "Ypiranga vs Botafogo-PB", fecha: "15 Junio", pronostico: "Empate (X)", cuota: "2.90", prob: "45%", explicacion: "Extrema paridad histórica (3 empates al hilo). Transición de técnicos fuerza un planteamiento ultra defensivo." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 15.")
