import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Besta deild (ISL)", partido: "Keflavik vs KR Reykjavik", fecha: "28 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.15", prob: "94%", explicacion: "KR Reykjavik anota 3.43 pero recibe 2.29 goles. El 100% de sus partidos este año superan tranquilamente esta línea." },
  { liga: "Besta deild (ISL)", partido: "Stjarnan vs KA Akureyri", fecha: "28 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.18", prob: "92%", explicacion: "Stjarnan encaja 2.33 por partido consistentemente por sus nulas transiciones defensivas. Probabilidad altísima." },
  { liga: "Besta deild (ISL)", partido: "FH Hafnarfjordur vs IBV", fecha: "28 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.20", prob: "91%", explicacion: "Choque de las dos peores defensas de Islandia (2.55 y 2.27 goles recibidos respectivamente). 0% de vallas invictas para ambos." },
  { liga: "2. Divisjon (NOR)", partido: "Skeid vs SK Trygg/Lade", fecha: "28 Junio", pronostico: "1X (Local o Empate)", cuota: "1.12", prob: "89%", explicacion: "Trygg/Lade es colista absoluto con 9 derrotas y 27 goles en contra. Skeid domina holgadamente ante bloques tan frágiles." },
  { liga: "Superettan (SUE)", partido: "Landskrona vs IFK Värnamo", fecha: "28 Junio", pronostico: "1X (Local o Empate)", cuota: "1.22", prob: "88%", explicacion: "Landskrona ostenta un sólido 71.4% de imbatibilidad en casa frente a un Värnamo que hila 5 derrotas consecutivas." },
  { liga: "Superettan (SUE)", partido: "Sandvikens IF vs Helsingborg", fecha: "28 Junio", pronostico: "Más de 7.5 Corners", cuota: "1.30", prob: "87%", explicacion: "Promedio combinado de 9.64. El planteamiento de transiciones rápidas por banda de Sandviken estabiliza completamente la línea." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 28.")
