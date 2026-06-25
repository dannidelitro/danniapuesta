import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Zain Premier (KUW)", partido: "Al Kuwait vs Kazma SC", fecha: "25 Junio", pronostico: "1X (Local o Empate)", cuota: "1.15", prob: "96%", explicacion: "Al Kuwait se mantiene invicto en la campaña regular, promediando 2.3 goles por partido con solidez absoluta de local." },
  { liga: "Besta deild (ISL)", partido: "Breidablik vs Vikingur", fecha: "25 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.18", prob: "94%", explicacion: "Vikingur promedia 3.27 goles a favor. El modelo de Poisson proyecta un promedio conjunto espectacular de 4.32 goles." },
  { liga: "Virsliga (LVA)", partido: "BFC Daugavpils vs Riga FC", fecha: "25 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.20", prob: "92%", explicacion: "Riga FC promedia 3.44 goles como visitante, logrando superar esta línea en el 100% de sus salidas en liga." },
  { liga: "Besta deild (ISL)", partido: "Breidablik vs Vikingur", fecha: "25 Junio", pronostico: "Más de 9.5 Corners", cuota: "1.45", prob: "88%", explicacion: "Dinámica arrolladora por bandas de ambos equipos, incrementando drásticamente la producción de saques de esquina del 75 al 90." },
  { liga: "Zain Premier (KUW)", partido: "Al Salmiyah vs Al Arabi SC", fecha: "25 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.35", prob: "85%", explicacion: "Alta probabilidad cruzada entre modelos de FootyStats y Statarea respaldada por la constancia goleadora local y visitante." },
  { liga: "Virsliga (LVA)", partido: "Super Nova vs FS Jelgava", fecha: "25 Junio", pronostico: "Ambos Anotan (BTTS)", cuota: "1.65", prob: "82%", explicacion: "Super Nova anota en casa el 87.5% de veces pero su defensa concede muchísimo (0% vallas invictas). Jelgava aprovechará los espacios." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 25.")
