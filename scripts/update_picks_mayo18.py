import re

file_path = r"c:\Users\dany\Documents\GitHub\danniapuesta\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_picks_data = """const PICKS_DATA = [
  { liga: "Premier League", partido: "Arsenal vs Burnley", fecha: "18 Mayo", pronostico: "Arsenal o Empate (1X)", cuota: "1.05", prob: "95%", explicacion: "Asimetría extrema. Arsenal se juega el título en casa frente a un Burnley ya descendido y con una defensa muy frágil." },
  { liga: "Allsvenskan", partido: "Djurgården vs IK Sirius", fecha: "18 Mayo", pronostico: "Más de 1.5 Goles", cuota: "1.22", prob: "83%", explicacion: "Choque de estilos de alta velocidad. Sirius promedia 2.71 goles como visitante y Djurgården 2.29 como local." },
  { liga: "Premier Div.", partido: "Waterford vs Drogheda", fecha: "18 Mayo", pronostico: "Ambos Marcan (BTTS)", cuota: "1.75", prob: "78%", explicacion: "Debilidad defensiva crónica de ambos equipos. Waterford promedia 81% de BTTS en casa y Drogheda 63% de visita." },
  { liga: "Liga Hypermotion", partido: "Leganés vs Huesca", fecha: "18 Mayo", pronostico: "Leganés o Empate (1X)", cuota: "1.30", prob: "77%", explicacion: "Duelo dramático por la permanencia. Huesca acusa bajas críticas en defensa, lo que refuerza la doble oportunidad local." },
  { liga: "1. Liga (Polonia)", partido: "Arka Gdynia vs Termalica", fecha: "18 Mayo", pronostico: "Arka Gdynia o Empate (1X)", cuota: "1.28", prob: "82%", explicacion: "Fuerte tendencia local. El modelo asigna una alta probabilidad de imbatibilidad en casa frente a un rival inestable." },
  { liga: "Premier League", partido: "Arsenal vs Burnley", fecha: "18 Mayo", pronostico: "Más de 9.5 Córners", cuota: "1.55", prob: "80%", explicacion: "Arsenal promedia 6.80 córners en casa y someterá a un Burnley replegado en bloque bajo." },
  { liga: "Allsvenskan", partido: "Djurgården vs IK Sirius", fecha: "18 Mayo", pronostico: "Más de 9.5 Córners", cuota: "1.60", prob: "78%", explicacion: "Volumen proyectado de 12.14 tiros de esquina por partido debido al juego vertical por bandas en césped artificial." },
  { liga: "Premier Div.", partido: "Waterford vs Drogheda", fecha: "18 Mayo", pronostico: "Waterford o Empate (1X)", cuota: "1.45", prob: "75%", explicacion: "Pese a no ganar, Waterford es resiliente en casa (solo 2 derrotas en 8 partidos). Drogheda sufre muchísimo de visitante." },
  { liga: "Liga Hypermotion", partido: "Leganés vs Huesca", fecha: "18 Mayo", pronostico: "Más de 4.5 Tarjetas", cuota: "1.70", prob: "75%", explicacion: "Tensión máxima por evitar el descenso directo en Butarque eleva drásticamente la probabilidad de juego brusco." },
  { liga: "Premier League", partido: "Arsenal vs Burnley", fecha: "18 Mayo", pronostico: "Arsenal Anota (Más 0.5)", cuota: "1.05", prob: "94%", explicacion: "Burnley lidera la liga en xGA (goles esperados en contra). El Arsenal anotará al menos un gol con altísima seguridad." }
];"""

pattern = r"const PICKS_DATA\s*=\s*\[.*?\];"
new_content = re.sub(pattern, new_picks_data, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("PICKS_DATA updated successfully for May 18.")
