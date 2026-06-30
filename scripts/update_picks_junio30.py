import re
import os

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Ligi Kuu Bara (TAN)", partido: "Simba SC vs KMC", fecha: "30 Junio", pronostico: "1X (Local o Empate)", cuota: "1.05", prob: "99%", explicacion: "Asimetría absoluta: Simba SC invicto choca contra KMC, ya descendido con 11 partidos sin ganar." },
  { liga: "Virslīga (LET)", partido: "RFS vs BFC Daugavpils", fecha: "30 Junio", pronostico: "1X (Local o Empate)", cuota: "1.08", prob: "96%", explicacion: "RFS promedia 2.50 goles a favor en casa. La probabilidad de que el visitante logre la victoria es marginal." },
  { liga: "Virslīga (LET)", partido: "FK Liepāja vs Ogre United", fecha: "30 Junio", pronostico: "Más de 0.5 Goles Local", cuota: "1.12", prob: "94%", explicacion: "Ogre United encaja un promedio crítico de 3.20 goles fuera de casa. Liepāja tiene una expectativa de 2.15 goles (Poisson)." },
  { liga: "Ligi Kuu Bara (TAN)", partido: "Simba SC vs KMC", fecha: "30 Junio", pronostico: "Más de 1.5 Goles Local", cuota: "1.30", prob: "92%", explicacion: "KMC registra una vulnerabilidad extrema, concediendo casi 2 goles por salida. Simba SC arrollará ofensivamente." },
  { liga: "Virslīga (LET)", partido: "FK Liepāja vs Ogre United", fecha: "30 Junio", pronostico: "1X (Local o Empate)", cuota: "1.25", prob: "92%", explicacion: "El frágil bloque defensivo visitante anula sus opciones de dominar el trámite. El 1X es matemáticamente la opción más segura." },
  { liga: "Série B (BRA)", partido: "Botafogo-SP vs CRB", fecha: "30 Junio", pronostico: "Más de 4.5 Tarjetas", cuota: "1.65", prob: "85%", explicacion: "Índice de fricción altísimo: ambos empatan con 16 puntos al borde del descenso. Regresión de tarjetas proyecta 5.7 amonestaciones." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 30.")
