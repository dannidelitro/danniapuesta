import re

file_path = r"c:\Users\dany\Documents\GitHub\danniapuesta\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Premier League", partido: "Chelsea vs Tottenham", fecha: "19 Mayo", pronostico: "Más de 8.5 Córners", cuota: "1.50", prob: "88%", explicacion: "Derbi abierto. Ambos promedian más de 10 córners totales por partido debido a transiciones rápidas y defensas frágiles." },
  { liga: "Pro League", partido: "Genk vs Antwerp", fecha: "19 Mayo", pronostico: "Genk o Empate (1X)", cuota: "1.25", prob: "87%", explicacion: "Brecha motivacional absoluta. Genk pelea puestos europeos mientras Antwerp (colista) acumula 3 partidos sin anotar." },
  { liga: "Superettan", partido: "Helsingborgs vs Varbergs", fecha: "19 Mayo", pronostico: "Ambos Marcan (BTTS)", cuota: "1.72", prob: "84%", explicacion: "Dinámica de transiciones de altísima velocidad. El visitante ha cumplido el BTTS en sus últimos 4 encuentros consecutivos." },
  { liga: "Premier League", partido: "Bournemouth vs Man City", fecha: "19 Mayo", pronostico: "Más de 9.5 Córners", cuota: "1.65", prob: "83%", explicacion: "Asedio total del City (21,325 pases completados) frente a un bloque bajo del Bournemouth. Altísima frecuencia de saques de esquina." },
  { liga: "Premier League", partido: "Chelsea vs Tottenham", fecha: "19 Mayo", pronostico: "Ambos Marcan (BTTS)", cuota: "1.45", prob: "82%", explicacion: "Las dos retaguardias sufren extrema fragilidad. Chelsea suma 14 jornadas seguidas sin valla invicta." },
  { liga: "Premier League", partido: "Bournemouth vs Man City", fecha: "19 Mayo", pronostico: "Más de 1.5 Goles", cuota: "1.15", prob: "81%", explicacion: "Hegemonía histórica de Pep Guardiola sobre los 'Cherries'. El City superó la línea de 2.5 en 8 de sus últimos 9 cruces." },
  { liga: "Premier League", partido: "Chelsea vs Tottenham", fecha: "19 Mayo", pronostico: "Más de 3.5 Tarjetas", cuota: "1.55", prob: "80%", explicacion: "Derbi intenso conducido por Stuart Attwell (árbitro riguroso) ante un Tottenham que lidera la liga en amonestaciones." },
  { liga: "Pro League", partido: "KVC Westerlo vs Standard Liege", fecha: "19 Mayo", pronostico: "Menos de 1.5 Goles 1T", cuota: "1.40", prob: "78%", explicacion: "Rigidez táctica máxima. En 29 de los últimos 30 partidos del Westerlo, hubo menos de 2 goles al descanso." },
  { liga: "Pro League", partido: "Genk vs Antwerp", fecha: "19 Mayo", pronostico: "Más de 1.5 Goles", cuota: "1.30", prob: "78%", explicacion: "Genk asediará la portería visitante (15.8 disparos por partido en casa) ante un rival desmotivado y con bajas críticas." },
  { liga: "Superettan", partido: "Helsingborgs vs Varbergs", fecha: "19 Mayo", pronostico: "Más de 2.5 Goles", cuota: "1.85", prob: "75%", explicacion: "Inestabilidad defensiva del local (recientes 2-2 y 3-3) choca con el potente ataque visitante en una liga muy over." }
];"""

pattern = r"const PICKS_DATA\s*=\s*\[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("PICKS_DATA updated successfully for May 19.")
