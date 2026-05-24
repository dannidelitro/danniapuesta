import re

file_path = r"c:\Users\dany\Documents\GitHub\danniapuesta\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Premier League", partido: "Tottenham vs Everton", fecha: "24 Mayo", pronostico: "Tottenham o Empate (1X)", cuota: "1.22", prob: "89%", explicacion: "Tottenham necesita sumar en casa para asegurar la permanencia. La urgencia máxima blinda la doble oportunidad." },
  { liga: "Premier League", partido: "Liverpool vs Brentford", fecha: "24 Mayo", pronostico: "Más de 1.5 Goles", cuota: "1.12", prob: "93%", explicacion: "Despedida de figuras en Anfield en un duelo sin presión clasificatoria, escenario ideal para goles." },
  { liga: "Serie A", partido: "AC Milan vs Cagliari", fecha: "24 Mayo", pronostico: "Milan Anota (Más 0.5)", cuota: "1.05", prob: "92%", explicacion: "Milan necesita sellar su billete a la Champions ante un rival replegado y de escasa resistencia." },
  { liga: "Premier League", partido: "Man City vs Aston Villa", fecha: "24 Mayo", pronostico: "Más de 2.5 Goles", cuota: "1.45", prob: "86%", explicacion: "Partido festivo para el City ya campeón ante el campeón de Europa League. Transiciones rápidas y cero rigor defensivo." },
  { liga: "Premier League", partido: "Brighton vs Man Utd", fecha: "24 Mayo", pronostico: "Ambos Marcan (BTTS)", cuota: "1.55", prob: "84%", explicacion: "Tendencia fortísima de BTTS en el historial directo (H2H) con alto flujo ofensivo y relajación táctica." },
  { liga: "Premier League", partido: "Tottenham vs Everton", fecha: "24 Mayo", pronostico: "Tottenham Más 1.5 Tarj.", cuota: "1.60", prob: "83%", explicacion: "Los Spurs son el equipo más amonestado del torneo. La extrema tensión por no descender garantizará faltas tácticas." },
  { liga: "Premier League", partido: "Man City vs Aston Villa", fecha: "24 Mayo", pronostico: "Más de 8.5 Córners", cuota: "1.40", prob: "82%", explicacion: "El asedio clásico de Guardiola sumado a un partido abierto asegura un alto volumen de tiros de esquina." },
  { liga: "Premier League", partido: "West Ham vs Leeds", fecha: "24 Mayo", pronostico: "Más de 3.5 Tarjetas", cuota: "1.50", prob: "81%", explicacion: "Duelo dramático de supervivencia. La obligación absoluta del West Ham por ganar forzará fricción extrema." },
  { liga: "Premier League", partido: "Liverpool vs Brentford", fecha: "24 Mayo", pronostico: "Liverpool Más 5.5 Córners", cuota: "1.50", prob: "80%", explicacion: "Anfield empujará al equipo en las despedidas, generando volumen constante de llegadas por las bandas." },
  { liga: "Serie A", partido: "Torino vs Juventus", fecha: "24 Mayo", pronostico: "Juventus o Empate (X2)", cuota: "1.25", prob: "78%", explicacion: "La Juve tiene la mejor defensa visitante de Italia (0.40 encajados). Obligados a no perder el derbi para asegurar Champions." }
];"""

pattern = r"const PICKS_DATA\s*=\s*\[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("PICKS_DATA updated successfully for May 24.")
