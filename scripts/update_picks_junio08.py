import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Série B (BRA)", partido: "Vila Nova vs Botafogo-SP", fecha: "8 Junio", pronostico: "Local o Empate (1X)", cuota: "1.25", prob: "92%", explicacion: "Vila Nova invicto en casa (2.20 PPG) contra un Botafogo con 9 partidos sin ganar." },
  { liga: "Botola Pro (MAR)", partido: "Berkane vs Tanger", fecha: "8 Junio", pronostico: "Local Anota (Más 0.5)", cuota: "1.18", prob: "91%", explicacion: "Berkane anotó en el 91% de sus juegos locales; Tanger es débil de visita." },
  { liga: "Ettan Norra (SUE)", partido: "Stockholm vs Vasalund", fecha: "8 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.20", prob: "89%", explicacion: "Consenso absoluto: ambos equipos promedian cerca de 3.00 goles por encuentro." },
  { liga: "Série B (BRA)", partido: "Vila Nova vs Botafogo-SP", fecha: "8 Junio", pronostico: "Más de 4.5 Tarjetas", cuota: "1.58", prob: "84%", explicacion: "El árbitro Maguielson Lima promedia 5.86; partido de altísima fricción proyectada." },
  { liga: "Série B (BRA)", partido: "América-MG vs Atlético-GO", fecha: "8 Junio", pronostico: "Más de 9.5 Corners", cuota: "1.65", prob: "80%", explicacion: "América-MG en casa promedia 11.07 córneres totales. Urgencia obliga ataque por bandas." },
  { liga: "Série B (BRA)", partido: "Vila Nova vs Botafogo-SP", fecha: "8 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.35", prob: "78%", explicacion: "Mercado secundario con valor (EV+) frente a la mala defensa visitante." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 8.")
