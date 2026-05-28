import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Erovnuli Liga (GEO)", partido: "Torpedo Kutaisi vs FC Gagra", fecha: "28 Mayo", pronostico: "Torpedo o Empate (1X)", cuota: "1.08", prob: "93%", explicacion: "Récord invicto del local en casa contra este oponente en 8 de sus últimos 9 H2H ligueros." },
  { liga: "Erovnuli Liga (GEO)", partido: "Torpedo Kutaisi vs FC Gagra", fecha: "28 Mayo", pronostico: "Más de 1.5 Goles", cuota: "1.18", prob: "92%", explicacion: "Torpedo promedia 1.95 goles en casa contra un Gagra que concede 1.47 fuera de su feudo." },
  { liga: "Erovnuli Liga (GEO)", partido: "Torpedo Kutaisi vs FC Gagra", fecha: "28 Mayo", pronostico: "Local +0.5 Goles", cuota: "1.10", prob: "91%", explicacion: "Estado de gracia futbolística de Torpedo (3 victorias al hilo)." },
  { liga: "Stars League (IRQ)", partido: "Naft Maysan vs Al Quwa Al Jawiya", fecha: "28 Mayo", pronostico: "Jawiya o Empate (X2)", cuota: "1.25", prob: "85%", explicacion: "El líder de la liga domina el H2H con 3 victorias consecutivas contra Naft." },
  { liga: "Premier League (EGY)", partido: "Petrojet vs El Gouna", fecha: "28 Mayo", pronostico: "Petrojet o Empate (1X)", cuota: "1.36", prob: "83%", explicacion: "Petrojet acumula una probabilidad de victoria o empate del 83% dada su imbatibilidad en sus últimos 5 juegos." },
  { liga: "Stars League (IRQ)", partido: "Al Minaa vs Al Talaba", fecha: "28 Mayo", pronostico: "Al Minaa o Empate (1X)", cuota: "1.40", prob: "80%", explicacion: "Tasa de imbatibilidad histórica en casa de Al Minaa frente a Talaba del 65% en sus últimos 20 duelos." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for May 28.")
