import re

html_path = r"..\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Amistosos FIFA", partido: "Croacia vs Bélgica", fecha: "2 Junio", pronostico: "Menos de 2.5 Goles", cuota: "1.75", prob: "68%", explicacion: "Croacia buscará ralentizar el ritmo y minimizar transiciones con largas posesiones defensivas." },
  { liga: "Amistosos FIFA", partido: "Marruecos vs Madagascar", fecha: "2 Junio", pronostico: "Marruecos a Cero (Sí)", cuota: "1.60", prob: "75%", explicacion: "Madagascar usará un bloque 5-4-1 ultradefensivo sin volumen de ataque frente a la zaga marroquí." },
  { liga: "Amistosos FIFA", partido: "Georgia vs Rumanía", fecha: "2 Junio", pronostico: "Más de 4.5 Tarjetas", cuota: "1.80", prob: "72%", explicacion: "Georgia destaca por su agresividad en duelos físicos y presión alta; partido de alta fricción en Tbilisi." },
  { liga: "Iraq Stars League", partido: "Al-Quwa Al-Jawiya vs Zakho", fecha: "2 Junio", pronostico: "Empate al Descanso", cuota: "2.10", prob: "65%", explicacion: "Zakho es el mejor bloque visitante y plantará un cerrojo en los primeros 45 minutos." },
  { liga: "Iraq Stars League", partido: "Al-Quwa Al-Jawiya vs Zakho", fecha: "2 Junio", pronostico: "Menos de 2.5 Goles", cuota: "1.65", prob: "70%", explicacion: "El líder enfrentará dificultades severas para romper el orden táctico de Zakho bajo altas temperaturas." },
  { liga: "Amistosos FIFA", partido: "Croacia vs Bélgica", fecha: "2 Junio", pronostico: "Empate al Descanso", cuota: "2.05", prob: "60%", explicacion: "Laboratorio táctico mundialista donde ambos priorizarán el orden defensivo en la primera mitad." }
];"""

pattern = r"const PICKS_DATA = \[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Picks updated successfully for June 2.")
