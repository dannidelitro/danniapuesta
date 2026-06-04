import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Serie B (ECU)", partido: "Atl. Vinotinto vs Cumbayá", fecha: "4 Junio", pronostico: "Vinotinto o Empate (1X)", cuota: "1.15", prob: "92%", explicacion: "Consistencia defensiva del Vinotinto en su feudo frente a un visitante con nulo volumen de ataque." },
  { liga: "Serie B (ECU)", partido: "San Antonio vs Ind. Juniors", fecha: "4 Junio", pronostico: "Ind. Juniors o Empate (X2)", cuota: "1.45", prob: "82%", explicacion: "Independiente Juniors registra una tasa de imbatibilidad del 83.3% y domina el H2H histórico (77.8%)." },
  { liga: "Ligue 1 (ALG)", partido: "Ben Aknoun vs USM Alger", fecha: "4 Junio", pronostico: "Local anota (Más 0.5)", cuota: "1.35", prob: "86%", explicacion: "Modelo de probabilidad complementaria arroja que Ben Aknoun anota en el 86% de sus localías." },
  { liga: "Ligue 1 (ALG)", partido: "Ben Aknoun vs USM Alger", fecha: "4 Junio", pronostico: "Más de 1.5 Goles", cuota: "1.45", prob: "78%", explicacion: "El 100% de los choques previos entre ambos superó esta barrera, promediando 3.00 goles." },
  { liga: "Serie B (ECU)", partido: "Atl. Vinotinto vs Cumbayá", fecha: "4 Junio", pronostico: "Más de 7.5 Córners", cuota: "1.55", prob: "76%", explicacion: "Proyección matemática ajustada a 9.43 saques de esquina por el uso de bandas." },
  { liga: "Ligue 1 (ALG)", partido: "Ben Aknoun vs USM Alger", fecha: "4 Junio", pronostico: "Más de 7.5 Córners", cuota: "1.50", prob: "75%", explicacion: "La inercia de transiciones rápidas en la liga argelina consolida este mercado sobre el 75%." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 4.")
