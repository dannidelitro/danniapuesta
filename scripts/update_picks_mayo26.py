import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Besta deildin", partido: "KR Reykjavík vs Valur", fecha: "26 Mayo", pronostico: "Más de 1.5 Goles", cuota: "1.15", prob: "95%", explicacion: "Promedio combinado altísimo. KR anota 3.50 por partido pero encaja 2.30." },
  { liga: "Premijer Liga", partido: "Borac Banja Luka vs Posušje", fecha: "26 Mayo", pronostico: "Local +0.5 Goles", cuota: "1.20", prob: "92%", explicacion: "Borac domina en casa (83% fortaleza) ante una visita muy débil que promedia solo 0.68 goles." },
  { liga: "Primera B Metro", partido: "Comunicaciones vs UAI Urquiza", fecha: "26 Mayo", pronostico: "Comunicaciones o Empate (1X)", cuota: "1.25", prob: "91%", explicacion: "Comunicaciones invicto (62%) en casa contra un UAI Urquiza ineficaz (12% victorias visitante)." },
  { liga: "Besta deildin", partido: "KR Reykjavík vs Valur", fecha: "26 Mayo", pronostico: "Más de 2.5 Goles", cuota: "1.45", prob: "88%", explicacion: "Tendencia del 100% de BTTS en casa para KR Reykjavík. Estructuras hiperofensivas." },
  { liga: "Besta deildin", partido: "KR Reykjavík vs Valur", fecha: "26 Mayo", pronostico: "Más de 9.5 Córners", cuota: "1.55", prob: "84%", explicacion: "Promedio combinado de 13.80 saques de esquina por juego debido al alto flujo en bandas." },
  { liga: "Besta deildin", partido: "Stjarnan vs Víkingur", fecha: "26 Mayo", pronostico: "Víkingur o Empate (X2)", cuota: "1.30", prob: "82%", explicacion: "Víkingur llega invicto (100%) como visitante ante un Stjarnan sumamente irregular." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for May 26.")
