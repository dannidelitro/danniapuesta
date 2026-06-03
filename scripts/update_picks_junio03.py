import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Serie B (ECU)", partido: "Atlético FC vs 9 de Octubre", fecha: "3 Junio", pronostico: "Atlético o Empate (1X)", cuota: "1.45", prob: "88%", explicacion: "El local solo ha perdido 1 de 12 partidos, usando un sólido repliegue medio que ahoga a los visitantes." },
  { liga: "Serie B (ECU)", partido: "Atlético FC vs 9 de Octubre", fecha: "3 Junio", pronostico: "Más de 4.5 Tarjetas", cuota: "1.55", prob: "85%", explicacion: "Disputa directa por la cima. Ambos promedian altísima fricción en la medular (5.75 y 4.75 tarjetas globales)." },
  { liga: "Serie B (ECU)", partido: "Atlético FC vs 9 de Octubre", fecha: "3 Junio", pronostico: "Local anota (Más 0.5)", cuota: "1.40", prob: "82%", explicacion: "Atlético ha marcado en casi todos sus juegos, aprovechando la vulnerabilidad del 9 de Octubre en transiciones." },
  { liga: "Serie B (ECU)", partido: "Atlético FC vs 9 de Octubre", fecha: "3 Junio", pronostico: "Más de 6.5 Córners", cuota: "1.65", prob: "81%", explicacion: "Proyección matemática ajustada a 7.0 córners totales dada la tendencia a bloquear el juego interior." },
  { liga: "USL (USA)", partido: "Birmingham vs Louisville", fecha: "3 Junio", pronostico: "Más de 7.5 Córners", cuota: "1.60", prob: "80%", explicacion: "Louisville usa un esquema 3-4-3 por bandas (carrileros muy abiertos), forzando múltiples despejes." },
  { liga: "USL (USA)", partido: "Birmingham vs Louisville", fecha: "3 Junio", pronostico: "Menos de 2.5 Goles", cuota: "1.70", prob: "75%", explicacion: "Birmingham es un muro absoluto en casa, donde el 80% de sus juegos no superan la barrera de 1.5 goles." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 3.")
