import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "1. Divisjon (NOR)", partido: "Kongsvinger vs Strømsgodset", fecha: "21 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.22", prob: "95%", explicacion: "Choque de líderes de alta posesión. Kongsvinger anota 2.8 goles en casa; Strømsgodset 2.4 de visita." },
  { liga: "1. Divisjon (NOR)", partido: "Strømmen vs Stabæk", fecha: "21 Junio", pronostico: "X2 (Visita o Empate)", cuota: "1.30", prob: "88%", explicacion: "Stabæk domina el mediocampo y las transiciones, penalizando severamente la fragilidad defensiva local." },
  { liga: "Superettan (SUE)", partido: "Östers IF vs Falkenbergs FF", fecha: "21 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.25", prob: "88%", explicacion: "Falkenbergs anota y encaja más de 2 goles por salida. Östers llega en racha con 11 goles en 6 juegos." },
  { liga: "1. Divisjon (NOR)", partido: "Kongsvinger vs Strømsgodset", fecha: "21 Junio", pronostico: "Más de 9.5 Córneres", cuota: "1.45", prob: "85%", explicacion: "Ataque directo por bandas incesante. El promedio combinado proyecta casi 13 lanzamientos de esquina." },
  { liga: "Superettan (SUE)", partido: "Helsingborgs vs GIF Sundsvall", fecha: "21 Junio", pronostico: "1X (Local o Empate)", cuota: "1.20", prob: "83%", explicacion: "Dominio táctico local ante el colista absoluto, que concede 2.1 goles por partido fuera de casa." },
  { liga: "Série B (BRA)", partido: "Avaí FC vs Cuiabá EC", fecha: "21 Junio", pronostico: "X2 (Visita o Empate)", cuota: "1.35", prob: "82%", explicacion: "Avaí suma 11 jornadas sin ganar. Cuiabá tiene defensa de élite, recibiendo apenas 0.46 goles globales." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 21.")
