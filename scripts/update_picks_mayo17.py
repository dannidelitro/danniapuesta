import re

file_path = r"c:\Users\dany\Documents\GitHub\danniapuesta\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "LaLiga", partido: "FC Barcelona vs Real Betis", fecha: "17 Mayo", pronostico: "Barcelona +5.5 Córners", cuota: "1.66", prob: "82%", explicacion: "Dominio absoluto del Barcelona en casa (69% posesión, 6.9 córners de media). Betis concede 4.3 córners fuera." },
  { liga: "Eredivisie", partido: "PSV vs FC Twente", fecha: "17 Mayo", pronostico: "Ambos Equipos Marcan", cuota: "1.28", prob: "84%", explicacion: "Poderío ofensivo histórico pero con debilidad defensiva crónica del PSV en casa (solo 2 clean sheets)." },
  { liga: "Serie A", partido: "AS Roma vs Lazio", fecha: "17 Mayo", pronostico: "Más de 4.5 Tarjetas", cuota: "1.68", prob: "88%", explicacion: "Derbi de máxima tensión. El colegiado Fabio Maresca tiene un promedio altísimo de tarjetas (5.52 amarillas por partido)." },
  { liga: "Serie A", partido: "Inter vs Hellas Verona", fecha: "17 Mayo", pronostico: "Inter Anota (Más 0.5)", cuota: "1.10", prob: "95%", explicacion: "El Inter busca ratificar jerarquía ante un Verona hundido. Selección segura para construir combinadas." },
  { liga: "Premier League", partido: "Man. United vs N. Forest", fecha: "17 Mayo", pronostico: "Más de 1.5 Goles", cuota: "1.25", prob: "88%", explicacion: "Ausencia de presión competitiva genera escenarios de transiciones rápidas y desequilibrio ofensivo sin rigor táctico." },
  { liga: "Serie A", partido: "Juventus vs Fiorentina", fecha: "17 Mayo", pronostico: "Juventus o Empate (1X)", cuota: "1.30", prob: "88%", explicacion: "Sólido rendimiento local de la Juve (94.4% imbatibilidad) frente a la inconsistencia de la Fiorentina." },
  { liga: "LaLiga", partido: "FC Barcelona vs Real Betis", fecha: "17 Mayo", pronostico: "Betis +2.5 Córners", cuota: "1.61", prob: "82%", explicacion: "Ineficiencia del mercado (EV+): Betis promedia 4.5 córners fuera y ha superado la línea en 16 de 18 desplazamientos." },
  { liga: "Eredivisie", partido: "PSV vs FC Twente", fecha: "17 Mayo", pronostico: "Más de 2.5 Goles", cuota: "1.33", prob: "80%", explicacion: "El duelo de mayor volumen ofensivo de Europa. Promedio combinado de 3.52 expected goals (xG)." },
  { liga: "Ligue 1", partido: "LOSC Lille vs Auxerre", fecha: "17 Mayo", pronostico: "Lille o Empate (1X)", cuota: "1.20", prob: "75%", explicacion: "Urgencia máxima del Lille por asegurar Champions frente a un Auxerre que pelea el descenso." },
  { liga: "Serie A", partido: "AS Roma vs Lazio", fecha: "17 Mayo", pronostico: "Lazio +1.5 Tarjetas", cuota: "1.45", prob: "85%", explicacion: "Frustración táctica de la Lazio tras perder la copa, combinada con la rigurosidad extrema del árbitro Maresca." }
];"""

pattern = r"const PICKS_DATA\s*=\s*\[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("PICKS_DATA updated successfully for May 17.")
