import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Premier League (ARM)", partido: "Ararat-Armenia vs Gandzasar", fecha: "27 Mayo", pronostico: "Ararat o Empate (1X)", cuota: "1.05", prob: "99%", explicacion: "Asimetría total. El líder recibe al colista con un historial de 6 victorias consecutivas en H2H." },
  { liga: "Premier League (ARM)", partido: "Pyunik vs Van", fecha: "27 Mayo", pronostico: "Pyunik o Empate (1X)", cuota: "1.08", prob: "94%", explicacion: "Dominio abrumador del local (75% fortaleza) contra una visita inestable." },
  { liga: "Premier League (ARM)", partido: "Ararat-Armenia vs Gandzasar", fecha: "27 Mayo", pronostico: "Más de 1.5 Goles", cuota: "1.15", prob: "92%", explicacion: "El líder promedia casi 2 goles por partido, y la visita ha encajado 12 goles en sus últimas 5 salidas." },
  { liga: "Premier League (ARM)", partido: "Urartu vs Noah", fecha: "27 Mayo", pronostico: "Noah o Empate (X2)", cuota: "1.25", prob: "88%", explicacion: "Noah llega con 16 goles en 5 partidos y un 61% de fortaleza visitante frente a un Urartu irregular." },
  { liga: "Premier League (ARM)", partido: "Pyunik vs Van", fecha: "27 Mayo", pronostico: "Local +0.5 Goles", cuota: "1.12", prob: "91%", explicacion: "El histórico Pyunik promedia 1.75 goles en casa." },
  { liga: "PFL (FIL)", partido: "Davao Aguilas vs Taguig", fecha: "27 Mayo", pronostico: "Taguig o Empate (X2)", cuota: "1.30", prob: "82%", explicacion: "Taguig es el bloque más vertical, promediando 2.30 goles y habiendo vencido a Davao por 4-1 recientemente." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for May 27.")
